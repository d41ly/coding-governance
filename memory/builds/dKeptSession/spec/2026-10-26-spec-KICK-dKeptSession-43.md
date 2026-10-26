# KICK-dKeptSession-43 — the `actions.free` arm reads every form of the item pointer, a skipped pointer leaving it unarmed and saying so

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-43-deviation-431.md](../build/2026-10-26-build-KICK-dKeptSession-43-deviation-431.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 57 at HIGH**, report item **H10**, which no other id shares.

`KICK-dKeptSession-8` S3 reads the build card's `item —` line as an instance key or `none`, and S7
says a throw anywhere in an armed arm refuses. `KICK-dKeptSession-13` S2 also prints
`item — skipped: <why>` when the position engine does not resolve. Read as a key, the arm fails
open: every write, commit, push and spawn is admitted with no item in flight. Read as a throw, every
write is refused, the commit that would repair the engine included. This unit gives the reader the
third form and makes it unarmed, visibly. It repairs `KICK-dKeptSession-8` and builds one step after
it (order 26).

## 2. Scope (IN)

- **S1** — id 57. Three forms. `readItemPointer` in `tools/hooks/scratch-guard.js` parses the
  `item —` line of `## pointers` into exactly one of `{ key, at }`, `{ none: true, at }` or
  `{ skipped: <why> }`, by `KICK-dKeptSession-13` S2's grammar: `item — <instance key|none> · at
  <sha8>` or `item — skipped: <why>`. A line matching none of the three is the fourth answer,
  `{ malformed: <line> }`. Observed by AC1 and AC3.
- **S2** — id 57. Unarmed on skipped. `checkFreeAction` admits the act when the pointer is
  `skipped`, printing `scratch-guard: actions.free unarmed — item pointer skipped: <why>`, one line,
  beside `KICK-dKeptSession-8` S7's three unarmed cases. Observed by AC1.
- **S3** — id 57. Refused on malformed. A malformed `item —` line is a throw inside the armed arm,
  so it refuses as `KICK-dKeptSession-8` S7 says, naming the line. Observed by AC3.
- **S4** — id 57. The plants `item-skipped` and `item-malformed` in
  `tools/hooks/actions-free.fixture.sh` (`KICK-dKeptSession-8` S8). Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- Writing the pointer, and keeping it current under `card.pointers = at-transitions`: id 11, item
  M8, batched into `KICK-dKeptSession-44`.
- The decision table for a key or `none`: `KICK-dKeptSession-8` S4, unchanged.
- The report's left-shift checklist entry, that a consumer enumerates every form its producer
  prints. No clause of this build names it; S1's closed parse is its instance here.

### Edges

- **consumes-from** `KICK-dKeptSession-8` — `readItemPointer` and `checkFreeAction`, whose pointer parse this unit closes over the producer's forms (id 57)
- **consumes-from** `KICK-dKeptSession-13` — S2's `item —` grammar, `skipped: <why>` included, which S1 parses
- **hands-off** `KICK-dKeptSession-56` — the pointer arm's help text and §7's legs, the batch's S42 and S26 (ids 41, 35)

## 4. Design

### Evidence

- `KICK-dKeptSession-8` S3 (spec-8 lines 43-49): "an instance key, or `none`"; S7 (:68-70) lists three
  unarmed cases and refuses on any throw once armed; `skipped` appears nowhere in spec 8.
- `KICK-dKeptSession-13` S2 (spec-13 lines 39-44): "A source that does not resolve prints its own
  `skipped: <why>` on its line", the `item —` line among them.

### The forms

| `item —` line | Parse | Arm |
|---|---|---|
| `item — tFix.build.u1@1#0a1b2c3d · at 1a2b3c4d` | key | `KICK-dKeptSession-8` S4 |
| `item — none · at 1a2b3c4d` | none | S4's table |
| `item — skipped: position.py not resolved` | skipped | unarmed, admits, one line |
| anything else | malformed | refuses, naming the line |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item-skipped`, `item-malformed` | fixture plants | none |

### Migration

None.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`: S1 to S3; `KIT_SCRATCH_GUARD_VERSION` moved
- `tools/hooks/actions-free.fixture.sh`: S4
- `tools/hooks/scratch-guard.test.sh`: the arm in §7

### Alternatives rejected

- **Refusing on skipped.** A missing loop kit would then block the commit that installs it.
- **Treating any unknown line as unarmed.** A corrupted card would silently disarm the gate.

## 5. Production-readiness checklist

- security — fails closed on a malformed line and open only on the producer's declared skip, which
  says so.
- perf / scale — one regex per armed call.
- error / empty / loading states — S1's four answers are exhaustive.
- observability — the unarmed line names the producer's why.
- risks — a producer printing `skipped` for a resolvable engine disarms the arm; the line shows it on
  every call.
- testing — the plants of §6 and the arm in §7.
- migration — none.
- user docs — `help/orientation-card.md`'s `actions.free` section (`KICK-dKeptSession-8` S9) names
  the skipped case.

## 6. Acceptance criteria

- **AC1** — When `bash actions-free.fixture.sh --plant item-skipped` runs in the hooks kit and pipes
  a Bash payload running `echo x > f` with the build card's line
  `item — skipped: position.py not resolved`, the hook exits 0 and prints
  `scratch-guard: actions.free unarmed — item pointer skipped: position.py not
  resolved`.
  Red when: an arm parsing `skipped:` as a key admits it silently, or a throw refuses it.
- **AC2** — When the same plant runs `git commit -m x`, the hook exits 0 with the same line.
  Red when: the repairing commit is refused.
- **AC3** — When `--plant item-malformed` writes `item — ???`, the `echo x > f` payload exits 2 naming
  the line.
  Red when: an unparsable pointer admits the act.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · the two plants, `item-skipped` staged red against a copy of the arm parsing `skipped:` as an instance key · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H10 (id 57).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-8`'s `readItemPointer` in `tools/hooks/scratch-guard.js`,
reading `KICK-dKeptSession-13` S2's grammar as written there. `python
tools/codebase-map/reuse_lookup.py "parse the item pointer line of a build card"` ranked `parse`
(`tools/memory-recall/query.py`), `build`, `parse_args`, `parse_conf` and `build_commit` by name stem
only; none parses a card line, and the arm and its reader are new in unit 8, so no existing seam in
the tree fits and unit 8's reader is the one extended.

Recall terms used: `python tools/memory-recall/query.py "what does actions.free do when the item
pointer is skipped" --terms "actions.free item pointer skipped unarmed readItemPointer scratch-guard
pointers card position.py"`
