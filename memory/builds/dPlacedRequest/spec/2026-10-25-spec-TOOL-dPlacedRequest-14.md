# TOOL-dPlacedRequest-14 — the pre-claim budget: placement loops before `entry.claim` drawing on a budget keyed to the request's content key

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 18 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0132@6096ecb9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A request that loops at entry, placed, refused by its check and placed again, or claimed under a slug another
session already holds and retried, stops after a bounded number of laps, like every other route back (P39).
TOOL-dDeclaredLoop-30 bounds a build's repetitions and hands the laps before a build exists here by name
("No budget before `entry.claim`: the intake's content-keyed budget is dPlacedRequest's",
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md:97`). The whole-design audit found
the clause first keyed that budget to an intake record no build before dWellOiledMachine writes (C2-F4,
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-fold-inventory.md:72`), so the key is
computed from the request's text and holds with no intake record at all.

## 2. Scope (IN)

- **S1** — The selector. TOOL-dDeclaredLoop-30's `tools/loop/budget.py draw` gains `--request <content key>`
  beside `--build <slug>` (shared interface I21), the two exclusive. `--request-text <file>` computes the key
  from the request's text through `request_content_key` (TOOL-dPlacedRequest-19's
  `derive_request_content_key`, I11), so a caller holding only the text, with no intake record and no request
  record yet, keys the draw exactly as one holding the record does. Observed by AC2.
- **S2** — The size. The total is the base of `flow.rework-budget` (TOOL-dDeclaredLoop-30 S1's
  `<base>+<per-unit>` parse, default `4+2`, so 4): a request has no units, nothing is frozen, and a later
  build's budget is its own, keyed to its slug. Observed by AC1.
- **S3** — The rows and their home. A draw reads the request's earlier rows, and writes nothing but prints
  `draw · <cause> · <item> · <spent>/<total>` and exits 0, or prints `exhausted · <spent>/<total>` and exits 3,
  the exit TOOL-dDeclaredLoop-30 §4 gives `exhausted`. The rows live on the request record,
  `refs/gov/requests/<content key>` (I12), one parented commit per row: the driver verb
  `bash tools/unattended/unattended.sh --request-draw <content key> --cause <c> --item <tag>` reads the
  ref's first-parent messages, passes them to `budget.py draw --request <key> --rows <file>`, and on `draw`
  builds the row's commit with `build_gov_commit` parented on the tip it read (I2) and writes it through
  `write_gov_ref` (TOOL-dPlacedRequest-11, I1) with that tip as the expected sha, so two nodes drawing at once serialize: the loser's push answers 1, it re-reads and draws again, at
  most three times, then reports contention. A request whose ref does not exist yet is recorded first by TOOL-dPlacedRequest-19's
  `unattended.sh --request <file>` from the `--request-text` file, a create carrying only the key, the fleet
  tag and the session, so the draw adds no text to the remote; with neither a ref nor a text file the draw
  refuses naming that verb.
  Observed by AC3 and AC4.
- **S4** — The causes, TOOL-dDeclaredLoop-30 S3's closed set and nothing new: a re-placement after a refused
  check draws `route-back` on `item.entry.place`; a probe round trip an observation sends before placement
  (TOOL-dPlacedRequest-4 S6) draws `research` on `item.entry.place`; a fresh slug after the claim was found
  under another key draws `route-back` on `item.entry.claim` (flow-steps.md:127, "each retry drawing on the
  pre-claim budget keyed to the intake's content key"). Observed by AC1 and AC5.
- **S5** — The draw sites. `python tools/loop/placement.py place` (TOOL-dPlacedRequest-4 S1) calls
  `--request-draw` before writing a block when the content key's placement file already holds a block whose
  `check:` is `refused`, and before a block that follows a probe record; TOOL-dPlacedRequest-21's
  `entry.claim` calls it before each fresh slug. On exit 3 the caller stops: `place` refuses printing
  `placement: pre-claim budget exhausted — <content key> · <spent>/<total>` and writes no block. Observed by
  AC1.
- **S6** — Contention draws nothing (`[rules]`, flow-steps.md:44-46): a lease wait, an unreachable remote and
  a lost compare-and-swap race are retried without a row, matching TOOL-dDeclaredLoop-30 S5's
  `classify_repeat`. Observed by AC4.
- **S7** — After exhaustion only the owner places. A placement under `--owner <record>` (TOOL-dPlacedRequest-4
  S2) draws nothing and is admitted past an exhausted budget, an owner's route being no repetition
  (TOOL-dDeclaredLoop-33 S4's owner edge). Observed by AC6.
- **S8** — The fixture plants of §6, run by `python tools/loop/budget.py --fixture` under TOOL-dDeclaredLoop-30's
  leg, with a bare scratch remote. Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- The build budget, its freeze, its draw sites and its ending: TOOL-dDeclaredLoop-30's and -31's.
- The request record, its create and its local text: TOOL-dPlacedRequest-19's; this unit adds rows to it.
- The compare-and-swap writer: TOOL-dPlacedRequest-11's `write_gov_ref`, called and never copied.
- The intake record: dWellOiledMachine's. The key is computed from text, so its absence changes nothing here.
- Moving the rows into the build once claimed: the claim commit carries the request's `content-key`
  (shared interface I23), which is the join; the build's own budget starts at its own base.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `request_content_key`, the key computed from text by `derive_request_content_key`, and the request record the rows ride on
- **consumes-from** `TOOL-dPlacedRequest-4` — `disposition`, the placement record whose refused blocks mark a lap and whose `place` is the draw site
- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, the one compare-and-swap writer each row is pushed through, with `build_gov_commit` parenting it on the tip read
- **hands-off** `TOOL-dPlacedRequest-21` — `--request-draw`, the draw `entry.claim` makes before each fresh slug
- **hands-off** `TOOL-dPlacedRequest-3` — `--request`, the pre-claim draw selector the placing and claiming items' route-backs make before any build exists
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The rows on the request ref

```
refs/gov/requests/3f9c2a7d01be
  c3  draw · route-back · item.entry.claim · 3/4     (parent c2)
  c2  draw · research · item.entry.place · 2/4       (parent c1)
  c1  draw · route-back · item.entry.place · 1/4     (parent c0)
  c0  TOOL-dPlacedRequest-19's create: content-key, fleet-tag, session
```

Each row commit's message is a header line `gov-request <content key>`, the shape `read_claims` reads
(shared interface I6's header rule), then the one row. `spent` is the count of `draw` rows on the first-parent
chain plus one, re-derived on every draw; a typed figure that disagrees is ignored and the count wins.

### The driver verb

```
--request-draw <key> --cause <c> --item <tag>
  fetch refs/gov/requests/<key> (bounded, as read_claims fetches)
  absent  -> unattended.sh --request <text file> (TOOL-dPlacedRequest-19), then re-read; no text file -> refused
  rows    -> python budget.py draw --request <key> --cause <c> --item <tag> --rows <tmp>
  exit 3  -> print the exhausted line, exit 3
  draw    -> c = build_gov_commit <tip read> <header + row>
             write_gov_ref refs/gov/requests/<key> <tip read> $c
             rc 1 -> re-read and redraw, at most 3 times, then print contention and exit 2
             rc 2 -> print the GOVREF_WHY cause and exit 2, nothing drawn
```

The python is resolved by the driver's inlined `resolve_python`, as TOOL-dDeclaredLoop-30 §4's draw sites call
`budget.py`. The temp file goes through the driver's own bounded scratch, as `write_claim` makes its
(`tools/unattended/unattended.sh:2417`).

### Inventory

| Minted | Kind |
|---|---|
| `--request`, `--request-text`, `--rows` | `budget.py draw` flags |
| `read_request_rows`, `record_request_draw` | functions, `tools/loop/budget.py` |
| `--request-draw` | driver verb, `tools/unattended/unattended.sh` |
| `run_request_draw` | bash function, `tools/unattended/unattended.sh` |
| `gov-request` | row-commit header word |

Each name is put to `python tools/lexicon/lexicon.py --suggest <name>` with its cell (`py.function`,
`sh.function`) in the build pass.

### Migration

None. No request ref carries rows before this unit; the first draw on one starts at 1.

### Rollout

Live at landing: the draw sites are `place` and `entry.claim`, both landing in this build, so no request
loops unbounded in between.

### Files touched (estimate)

- `tools/loop/budget.py`: the `--request` arm, `read_request_rows`, `record_request_draw`, the fixture plants
- `tools/loop/placement.py`: the draw before a re-placement and the exhausted refusal
- `tools/unattended/unattended.sh`: `--request-draw` and `run_request_draw`
- `tools/unattended/VERBS.template.md`: the verb's line
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `help/loop.md`: the budget section names the pre-claim budget

### Alternatives rejected

- **Key the budget to the intake record.** No build before dWellOiledMachine writes one (C2-F4).
- **A node-local draw file.** A request any node may claim by lease (TOOL-dPlacedRequest-19) would restart
  its count on each node that takes it, so a hand-over would reset the bound the clause sets.
- **Write the row from python.** It would be a third hand copy of the compare-and-swap push that
  TOOL-dPlacedRequest-11 merges into one; the driver already carries the canonical writer inline.

## 5. Production-readiness checklist

- security — a row carries a cause word, an item tag and two counts; no request text reaches the remote, and
  the create is TOOL-dPlacedRequest-19's key-only write.
- perf / scale — one bounded fetch and at most three pushes per draw; a request loops at most four times.
- error / empty / loading states — an unreachable remote draws nothing and is contention; a malformed row is
  skipped and named on stderr, never counted.
- observability — every lap is a commit on the request ref, readable from any node.
- risks — a request placed on two nodes at once draws on one shared count, which is the clause's intent.
- testing — the fixture plants of AC1 to AC6; the suite arm in §7 at the close.
- migration — none.
- user docs — `help/loop.md`'s budget section gains the pre-claim budget, its size and its causes.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant placement-loop` places one request and has its check
  refuse four times, the fourth re-placement prints `draw · route-back · item.entry.place · 4/4`, and the
  fifth `place` exits 3 printing `pre-claim budget exhausted` and writes no block.
  Red when: the loop places a fifth time, so a placement loop runs unbounded.
- **AC2** — When `python budget.py --fixture --plant no-intake` runs the same loop with no intake record and
  no request ref, keying each draw by `--request-text`, the key equals `request_content_key` of the text, and
  the loop is refused at the same lap.
  Red when: the budget reads an intake record, so a request without one draws nothing and loops.
- **AC3** — When `python budget.py --fixture --plant rows-on-ref` makes two draws, `git log --first-parent
  --format=%B refs/gov/requests/<key>` in the scratch remote shows two row commits, each parented on the tip
  before it, and no line of the request's text.
  Red when: a row commit is parentless, so the remote keeps only the last row.
- **AC4** — When `python budget.py --fixture --plant two-nodes` has two clones draw on one key at once, both
  rows land with the counts `1/4` and `2/4`, the loser having re-read once, and `--plant unreachable` draws
  nothing.
  Red when: both nodes write `1/4`, so a race resets the count.
- **AC5** — When `python budget.py --fixture --plant slug-retry` has `entry.claim` find its slug under another
  key, the retry's row reads `route-back · item.entry.claim`, and a cause outside TOOL-dDeclaredLoop-30's set
  is refused naming it.
  Red when: a slug retry draws nothing.
- **AC6** — When `python budget.py --fixture --plant owner-after-exhausted` places an exhausted request under
  `--owner <record>`, the placement is written and no row is added.
  Red when: an exhausted request can never be placed again, even by the owner.

## 7. Gates

`recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/budget.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `loop budget fixtures` leg's plants, its failing case staged by `placement-loop` with the draw site removed from `place` · none
New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 · the `--request-draw` case over a scratch remote, its failing case staged by a parentless row commit · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: `DRAFT` is
  not in the tuple. Liveness: the tuple would list it if the vocabulary admitted it. RESOLVED (agent,
  2026-10-25, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Where do the pre-claim rows live?** Options: (a) on the request ref, one parented commit per row,
  written by the driver through `write_gov_ref`; (b) a node-local file per content key; (c) the session's
  run-state file. (b) resets on a hand-over to another node; (c) exists for unattended builds only, and a
  request has no build. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, shared interface I21's "the draw
  rows live on the request record until a build exists". grants: PLAY-dClosedLoop-3 the --request-draw verb
  and its line in tools/unattended/VERBS.template.md and its render memory/guides/UNATTENDED-VERBS.md ·
  widens: none · relaxes: none
- **F3 — What does an exhausted request do?** Options: (a) refuse further placement until the owner places
  it; (b) file it as an ask; (c) drop it. (b) needs a build to file into, which a request has not; (c) loses
  the owner's request. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the owner's placement value
  `owner-places` already being the route that reads an owner's record. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 14, the brief's shared interfaces I11, I12 and
  I21, scout B's row for TOOL-dPlacedRequest-14, flow-steps.md:40-60 and :127, and TOOL-dDeclaredLoop-30
  S1 to S5, read at base `c63aabbb`.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: S1 and the consumes-from bullet name
  `derive_request_content_key`, the function unit 19 hands off.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seam is TOOL-dDeclaredLoop-30's `budget.py draw` (its §4 "The driver, in shell"), extended by one selector
as its Non-goals hand it here, plus TOOL-dPlacedRequest-11's `write_gov_ref` for the row and
TOOL-dPlacedRequest-19's `request_content_key` for the key. `python tools/codebase-map/reuse_lookup.py "draw on
a rework budget keyed by content before a build exists"` ranked only name stems (`key`, `before`, `build`), and
`budget.py` is not built at base, so nothing in code draws a budget today. The normalisation the key rests on
is `derive_content_key` (`tools/memory-tree/row_grammar.py:1475`), which scout B cites and source confirms;
where the scout and source disagree: none. `python tools/memory-recall/query.py "what bounds placement loops
before a claim"` returned scout B's row, the packet's Items 14 and the brief's row.

Recall terms used: pre-claim budget content key flow.rework-budget draw route-back placement loop intake request record exhausted
