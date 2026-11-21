# KICK-dKeptSession-43 — the `actions.free` arm reads every form of the item pointer, a skipped pointer leaving it unarmed and saying so

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-43-deviation-431.md](../build/2026-10-26-build-KICK-dKeptSession-43-deviation-431.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-8-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-8-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-8 KICK-dKeptSession-11 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 57 at HIGH**, report item **H10**, which no other id shares.

`KICK-dKeptSession-8` S3 reads the card's `item —` line in two forms, an instance key or `none`, each
ending ` · at <sha8>`, and its S7 says a throw anywhere in an armed arm refuses.
`KICK-dKeptSession-13` S2 also prints `item — skipped: <why> · at <sha8>` when the position read does
not resolve. Unit 8 takes that line as a throw, so every write is refused, the commit that would
repair the engine included; an arm that loosened its parse to admit it would read `skipped:` as a
key instead and fail open, admitting every write, commit, push and spawn with no item in flight. This
unit gives the reader the third form and makes it unarmed, visibly. It repairs `KICK-dKeptSession-8`
and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — id 57. Three forms. `readItemPointer` in `tools/hooks/scratch-guard.js` parses the
  `item —` line of `## pointers` into exactly one of `{ key, at }`, `{ none: true, at }` or
  `{ skipped: <why>, at }`, by `KICK-dKeptSession-13` S2's grammar: `item — <instance key|none> · at
  <sha8>` or `item — skipped: <why> · at <sha8>`, the why running to the last ` · at <sha8>` of the
  line. A line matching none of the three is the fourth answer, `{ malformed: <line> }`. Observed by
  AC1 and AC3.
- **S2** — id 57. Unarmed on skipped. `checkFreeAction` admits the act when the pointer is
  `skipped`, printing `scratch-guard: actions.free unarmed — item pointer skipped: <why>`, one line,
  beside `KICK-dKeptSession-8` S7's unarmed cases. Observed by AC1 and AC2.
- **S3** — id 57. Refused on malformed. A malformed `item —` line is a throw inside the armed arm, so
  it refuses as `KICK-dKeptSession-8` S7 says, naming the line. Observed by AC3.
- **S4** — id 57. The plants `item-skipped` and `item-malformed` in
  `tools/hooks/actions-free.fixture.sh` (`KICK-dKeptSession-8` S8). Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Writing the pointer, and keeping it current under `card.pointers = at-transitions`: id 11, item
  M8, batched into `KICK-dKeptSession-44`.
- The decision table for a key or `none`: `KICK-dKeptSession-8` S4, unchanged.
- The page's text on the skipped case: `KICK-dKeptSession-56` S42 writes it into
  `help/orientation-card.md` (id 41).
- The kit version constant: the lander mints it (`tools/push-main.sh@78f40c3c2475:27`).
- The report's left-shift checklist entry, that a consumer enumerates every form its producer
  prints. No clause of this build names it; S1's closed parse is its instance here.

### Edges

- **consumes-from** `KICK-dKeptSession-8` — `readItemPointer` and `checkFreeAction`, whose pointer parse this unit closes over the producer's forms (id 57)
- **consumes-from** `KICK-dKeptSession-13` — S2's `item —` grammar, `skipped: <why> · at <sha8>` included, which S1 parses
- **hands-off** `KICK-dKeptSession-56` — the pointer arm's help text and §7's legs, the batch's S42 and S26 (ids 41, 35)

## 4. Design

### Evidence

- `KICK-dKeptSession-8` S3 at rev-4: the `item —` line parsed into `{ key, at }` or
  `{ none: true, at }`, any other line a throw; S7 lists its unarmed cases and refuses on any throw
  once armed. `skipped` is a form unit 8 names only to hand it here.
- `KICK-dKeptSession-13` S2 at rev-4: "A source that does not resolve prints `<word> — skipped:
  <why>` on its line, and the `item —` line then still ends ` · at <sha8>`"; its §5 risks row names
  the case, a position read past its bound.

### The forms

| `item —` line | Parse | Arm |
|---|---|---|
| `item — item.build.base@TOOL-tFix-1#aaaa0001 · at 1a2b3c4d` | key | `KICK-dKeptSession-8` S4 |
| `item — none · at 1a2b3c4d` | none | S4's table |
| `item — skipped: position.py not resolved · at 1a2b3c4d` | skipped | unarmed, admits, one line |
| anything else | malformed | refuses, naming the line |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item-skipped`, `item-malformed` | fixture plants | none |

### Migration

None.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`: S1 to S3
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
  the skipped case, by `KICK-dKeptSession-56` S42.

## 6. Acceptance criteria

- **AC1** — When `bash actions-free.fixture.sh --plant item-skipped` runs in the hooks kit and pipes
  a Bash payload running `echo x > f` with the card's line
  `item — skipped: position.py not resolved · at <HEAD sha8>`, the hook exits 0 and prints
  `scratch-guard: actions.free unarmed — item pointer skipped: position.py not
  resolved`.
  Red when: an arm parsing `skipped:` as a key admits it silently, or a throw refuses it.
- **AC2** — When the same plant runs `git commit -m x`, the hook exits 0 with the same line.
  Red when: the repairing commit is refused.
- **AC3** — When `--plant item-malformed` writes `item — ???`, the `echo x > f` payload exits 2 naming
  the line.
  Red when: an unparsable pointer admits the act.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · the two plants, `item-skipped` staged red against unit 8's arm, which takes the line as a throw and refuses it · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H10 (id 57).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 · S2 · S4 · §3 · §4 · §5 · AC1 · §7 · §10 · re-grounded on the landed
  tree at `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-8-orders-25-26-reground-brief`: the
  skipped form read as unit 13 rev-4 spells it, ending ` · at <sha8>`, and the parsed answer carries
  that `at`; the instance key re-spelled to the engine's form; unit 8 rev-4's reader, which takes the
  line as a throw, named as the failing case the arm stages; the evidence re-cited from line numbers
  to scope ids; the page's text handed to unit 56 in §3; the version-constant move left to the
  lander; `policy fixtures` named.

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-8`'s `readItemPointer` in `tools/hooks/scratch-guard.js`,
reading `KICK-dKeptSession-13` S2's grammar as written there; neither function stands in the tree at
`c2a407b0`, so the seam is unit 8's as specified. `python tools/codebase-map/reuse_lookup.py "parse
the item pointer line of a build card"`, re-run 2026-11-21, ranked `parse`
(`tools/memory-recall/query.py`), `parse_args`, `build`, `build_records`, `parse_conf` and
`parse_unit_rows` by name stem only; none parses a card line, so no existing seam in the tree fits and
unit 8's reader is the one extended. The recall query returned this spec, unit 8's brief row and the
audit's H10, which agree.

Recall terms used: `python tools/memory-recall/query.py "what does actions.free do when the item
pointer is skipped" --terms "actions.free item pointer skipped unarmed readItemPointer scratch-guard
pointers card position.py"`
