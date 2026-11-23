# KICK-dKeptSession-43 — the `actions.free` arm reads every form of the item pointer, a skipped pointer leaving it unarmed and saying so

**Status:** CLOSED · rev-5 · 2026-11-23 · node a · Tier-2 · base 0e5b281a · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-43-deviation-431.md](../build/2026-10-26-build-KICK-dKeptSession-43-deviation-431.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-1 |
| [2026-11-21-build-KICK-dKeptSession-43-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-43-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-40 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief.md) | research | KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 |
| [2026-11-21-prompt-KICK-dKeptSession-43-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-43-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-8-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-8-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-8 KICK-dKeptSession-11 |
| [2026-11-22-prompt-KICK-dKeptSession-43-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-43-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-43-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-43-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 57 at HIGH**, report item **H10**, which no other id shares.

The landed card renderer prints the `item —` line in three forms: an instance key or `none`, and
`item — skipped: <why> · at <at>` when the position read does not answer, `at` being HEAD's sha8 or
`unborn` with no commit (`skills/session-kickoff/manifest-check.sh#render_pointers`). Its whys are
`run_item_boundary`'s lines, among them `no loop kit position.py resolves in this tree`
(`skills/session-kickoff/manifest-check.sh#run_item_boundary`). `KICK-dKeptSession-8` S3 at rev-6
parses that third form as `{ malformed, at }`, and its S3 and S7 make a malformed item a throw once
the arm is armed, so every write is refused, the commit that would repair the engine included. An arm
that loosened its parse to admit the line would read `skipped:` as an item instead and fail open,
admitting every write, commit, push and spawn with no item in flight. This unit gives the reader the
third form and makes it unarmed, visibly. It repairs `KICK-dKeptSession-8` and builds one step after
it (order 26).

## 2. Scope (IN)

- **S1** — id 57. Three forms. `readItemPointer(top)` in `tools/hooks/scratch-guard.js`, minted by
  `KICK-dKeptSession-8` S3, parses the `item —` line's value, the text before its ` · at
  <hex|unborn>` tail, into exactly one of `{ key, at }`, `{ none: true, at }` or
  `{ skipped: <why>, at }`, in that key order. The third is a value opening `skipped: ` followed by a
  non-empty why, the why running to the line's last ` · at` tail, so a why that itself holds ` · at `
  stays whole. Any other value, `skipped:` with no why included, stays unit 8's
  `{ malformed: <line>, at }`. `at` is read by the one pattern unit 8 lands, never a second, and the
  skipped answer carries it, so `checkItemBoundary`, which reads its `at` through `readItemPointer`,
  starts no verb at a skipped line whose `at` is HEAD, as the landed step does today
  (`tools/hooks/scratch-guard.js#checkItemBoundary`). The parse is extended inside
  `readItemPointer`, minting no function. Observed by AC5.
- **S2** — id 57. Unarmed on skipped. `checkFreeAction(data, env)`, armed as unit 8 S3 arms it, returns
  `{ unarmed: 'item pointer skipped: <why>' }` when the item is a skipped answer, before any policy
  read, beside unit 8 S7's unarmed cases. Each caller prints it as unit 8 S7 prints those:
  `scratch-guard.js` one line `scratch-guard: actions.free unarmed — item pointer skipped: <why>` and
  admits, and `agent-cap.js`'s rule 9, the arm's other caller (unit 8 S6), one line `agent-cap: rule 9
  unarmed — item pointer skipped: <why>` and admits, its code unchanged. Observed by AC1, AC2 and AC4.
- **S3** — id 57. Refused on malformed. Armed, a malformed item stays unit 8's throw, its message
  `item pointer malformed: <line>`, which replaces unit 8's message where that differs, so `main`'s
  refusal `BLOCKED by scratch-guard: the actions.free arm threw (<message>) and fails closed on a
  <tool>.` names the line. Observed by AC3.
- **S4** — id 57. The plants `item-skipped` and `item-malformed` in
  `tools/hooks/actions-free.fixture.sh` (unit 8 S8), each a branch of the fixture's plant dispatch,
  minting no shell function, so `memory/map/generated/symbols.json`, which indexes the hooks' and the
  fixtures' functions, does not move. Both run under the policy stub's `read-only-probes`, under which
  unit 8's arm refuses a write at `item — none`. `item-skipped` writes
  `item — skipped: no loop kit position.py resolves in this tree · at <HEAD sha8>` into
  `## pointers` and pipes three payloads, a Bash `echo x > f` and a Bash `git commit -m x` to
  `scratch-guard.js` and an `Agent` payload to `agent-cap.js`, printing each call's exit code and
  stderr as unit 8's plants do; `item-malformed` writes `item — ???` and pipes the Bash `echo x > f`.
  Observed by AC1, AC2, AC3 and AC4.
- **S5** — id 57. The shipped texts the skipped answer makes false, each rewritten in place and read at
  this unit's base as unit 8 lands them. In `tools/hooks/scratch-guard.js`: `readItemPointer`'s doc
  comment, which lists the parsed forms; `checkFreeAction`'s doc comment, which lists the unarmed
  cases; and the header's THE FIFTH CHECK paragraph (unit 8 S10). In `tools/hooks/README.md`: the
  section "Rule 9 and scratch-guard's fifth check: `actions.free`", whose unarmed lines gain
  `item pointer skipped: <why>`. In `tools/hooks/agent-cap.js`: the header's RULE 9 paragraph, where
  it names the unarmed cases. Each sentence naming the pointer's forms gains the skipped one, and one
  saying that a line other than a key or `none` refuses reads that a skipped line is unarmed and any
  other line refuses. Observed by AC6.
- **S6** — id 57. The floor and the budget rows. `tools/hooks/scratch-guard.test.sh`'s
  `FLOOR_ASSERTIONS` rises by the arm's 3 rows (DERIVED: §4's suite floor), in the pin's style; the
  `scratch-guard self-test` and `agent-cap self-test` rows of `tools/run-gates/selftest-budgets.txt`
  are re-priced as §4's budget rows state. NOT OBSERVED: a floor and a budget price a whole suite,
  which runs once, after the build, never as a criterion.

## 3. Non-goals (OUT)

- Writing the pointer, and keeping it current under `card.pointers = at-transitions`: id 11, item
  M8, batched into `KICK-dKeptSession-44`.
- The decision table for a key or `none`, and the arm's wiring: `KICK-dKeptSession-8` S4 and S6,
  unchanged.
- The page's text on the skipped case: `KICK-dKeptSession-56` S42 writes it into
  `help/orientation-card.md` (id 41), at order 31.
- A null item, a `## pointers` section with no `item —` line: unit 8's throw, its message unchanged.
- The kit version constant: the lander mints it (`tools/push-main.sh@78f40c3c2475:27`).
- The report's left-shift checklist entry, that a consumer enumerates every form its producer
  prints. No clause of this build names it; S1's closed parse is its instance here.

### Edges

- **consumes-from** `KICK-dKeptSession-8` — `readItemPointer` and `checkFreeAction`, whose pointer parse this unit closes over the producer's forms (id 57)
- **consumes-from** `KICK-dKeptSession-13` — S2's `item —` grammar, `skipped: <why> · at <sha8>` included, which S1 parses
- **hands-off** `KICK-dKeptSession-56` — the pointer arm's help text and §7's legs, the batch's S42 and S26 (ids 41, 35)

## 4. Design

### Evidence

- The producer, read at `0e5b281a`: `render_pointers` prints `item — skipped: %s · at %s`, its why the
  boundary file's first line or `no boundary was read`, and its `at` from `git rev-parse --short=8
  HEAD` or `unborn` (`skills/session-kickoff/manifest-check.sh#render_pointers`).
- The landed step reads `at` by ` · at ([0-9a-f]+|unborn)$` from any `item — ` line of `## pointers`,
  so a skipped line's `at` already stops its verb (`tools/hooks/scratch-guard.js#checkItemBoundary`).
- `KICK-dKeptSession-8` S3 at rev-6: `readItemPointer` extracted from that read, the value parsed into
  `{ key, at }`, `{ none: true, at }` or `{ malformed: <line>, at }`, a null or malformed item a throw
  once armed; S7 lists the unarmed cases; S8 the fixture; its AC10 prints
  `{"malformed":"item — x y","at":null}` for an unknown value and counts one `unborn)` pattern.

### The forms

| `item —` line | Parse | Arm |
|---|---|---|
| `item — item.build.base@TOOL-tFix-1#aaaa0001 · at 1a2b3c4d` | key | `KICK-dKeptSession-8` S4 |
| `item — none · at 1a2b3c4d` | none | S4's table |
| `item — skipped: no loop kit position.py resolves in this tree · at 1a2b3c4d` | skipped | unarmed, admits, one line |
| `item — skipped: · at unborn`, `item — ???` | malformed | refuses, naming the line |

The parse tests a key, then `none`, then the `skipped: ` opening: an instance key holds no space, so
no key reads as skipped. Unit 8's AC10 keeps its output, since its three values read as before.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item-skipped`, `item-malformed` | fixture plants, branches of the plant dispatch | none |

### Migration

None.

### The suite floor

`tools/hooks/scratch-guard.test.sh` pins `FLOOR_ASSERTIONS=401` at `0e5b281a` (PINNED 2026-11-23),
and unit 8 raises it to 430 (PINNED 2026-11-23, that spec's §4 at rev-6). This unit's arm writes one
ok-or-FAIL row per call its criteria name, 1 for AC1, 1 for AC2 and 1 for AC3, 3 rows (PINNED
2026-11-23, the count of those calls), so the pin becomes the value unit 8 lands plus 3, 433 by that
spec (DERIVED: the landed pin plus 3). `tools/hooks/agent-cap.test.sh` pins no floor of its own.
This unit edits no `tools/unattended/unattended.sh`, so no driver refusal site and no harness-arms
ceiling moves.

### The budget rows

The estimate is unit 8's, 2 s per plant (PINNED 2026-11-22, that spec's §4). The scratch-guard arm runs
both plants and the agent-cap arm runs `item-skipped` alone.

| Figure | `scratch-guard self-test` | `agent-cap self-test` |
|---|---|---|
| `r` after unit 8, its §4 (PINNED 2026-11-22) | 208 s | 393 s |
| this unit's plants, estimates (PINNED 2026-11-22) | 2 times 2 s | 1 times 2 s |
| `r` after this unit (PINNED 2026-11-23, the sum) | 212 s | 395 s |
| budget, max of the row's value and 1.5 `r` | 318, over unit 8's 312 | 593, over the row's 590 |
| the leg's ceiling in `tools/gate-legs.json` (PINNED 2026-11-23 at `0e5b281a`) | 490 | 1800 |

The builder reads each arm's plants alone by direct CLI and appends `Then re-read by
KICK-dKeptSession-43 as PINNED proxy r <s>` to each row's note, each budget the row's value or 1.5 `r`
rounded up, whichever is higher. `tools/run-gates/ceiling-evidence.txt` is generated and never
hand-edited. Where a reading takes `r` to its leg's ceiling, the unit stops before it lands and names
the raise for the owner (`memory/guides/BUILD-METHOD.md`, M3), and never edits `tools/gate-legs.json`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`: S1 to S3, and S5's three comments
- `tools/hooks/actions-free.fixture.sh`: S4
- `tools/hooks/scratch-guard.test.sh`: the first arm in §7, and S6's floor
- `tools/hooks/agent-cap.test.sh`: the second arm in §7
- `tools/hooks/README.md`: S5's section
- `tools/hooks/agent-cap.js`: S5's RULE 9 paragraph, where it names the unarmed cases
- `tools/run-gates/selftest-budgets.txt`: S6, both rows' notes and budgets

### Texts left true

- `help/orientation-card.md`: "A line whose source does not answer reads `<word> — skipped: <why>`" and
  the `item —` bullet describe the line, not what the arm admits, and unit 8 S9's paragraph speaks of
  `item — none` alone; the skipped case is unit 56 S42's.
- `skills/session-kickoff/manifest-check.sh`: the grammar comment above `run_item_boundary` and the
  comment above `run_card_boundary`, naming unit 8 as the line's reader, describe the producer, which
  this unit does not move.
- `tools/policy/catalogue.toml`: the `actions.free` row holds values, default and owner, and no summary
  (`tools/policy/unsummarised-keys.txt`), so no clause edits it and `.governance/policy.json` does not
  move.
- `help/reference/policy.md` lists the key from the catalogue; `tools/hooks/kit.toml`'s rule from unit
  8 already claims the fixture, and this unit adds no file.

### Alternatives rejected

- **Refusing on skipped.** A missing loop kit would then block the commit that installs it.
- **Treating any unknown line as unarmed.** A corrupted card would silently disarm the gate.
- **A second parse for the skipped form beside `readItemPointer`.** Unit 8 extracted one parse so the
  arm and the step cannot drift; a second would reopen that drift.

## 5. Production-readiness checklist

- security — fails closed on a malformed line and open only on the producer's declared skip, which
  says so on every call.
- perf / scale — one more prefix test per armed call; no spawn and no policy read on the skipped path.
- error / empty / loading states — S1's four answers are exhaustive over the `item —` line.
- observability — the unarmed line names the producer's why.
- risks — a producer printing `skipped` for a resolvable engine disarms the arm, and the line shows
  it on every call; `KICK-dKeptSession-11`, in this unit's step, edits another row of the budgets file.
- testing — the plants of S4 and the arms in §7, and AC5's direct probe.
- migration — none.
- user docs — `help/orientation-card.md`'s `actions.free` paragraph (`KICK-dKeptSession-8` S9) names
  the skipped case by `KICK-dKeptSession-56` S42; `tools/hooks/README.md` by S5.

## 6. Acceptance criteria

- **AC1** — When `bash actions-free.fixture.sh --plant item-skipped` runs in the hooks kit's directory
  and pipes the Bash payload running `echo x > f` under `read-only-probes`, the hook exits 0 and prints
  `scratch-guard: actions.free unarmed — item pointer skipped: no loop kit position.py resolves in
  this tree`.
  Red when: an arm parsing `skipped:` as an item admits it silently, or a throw refuses it.
- **AC2** — When the same plant pipes `git commit -m x`, the hook exits 0 with the same line.
  Red when: the repairing commit is refused.
- **AC3** — When `bash actions-free.fixture.sh --plant item-malformed` writes `item — ???`, the
  `echo x > f` payload exits 2 and stderr carries `item pointer malformed: item — ???`.
  Red when: an unparsable pointer admits the act, or its refusal does not name the line.
- **AC4** — When the `item-skipped` plant pipes its `Agent` payload to `agent-cap.js`, it exits 0 and
  prints `agent-cap: rule 9 unarmed — item pointer skipped: no loop kit position.py resolves in this
  tree`.
  Red when: rule 9 refuses a spawn on the skipped line, or admits it silently.
- **AC5** — When
  `node -e "const g = require(require('path').resolve(process.argv[1])), fs = require('fs'), p = require('path'); const d = fs.mkdtempSync(p.join(require('os').tmpdir(), 'rip-')); fs.mkdirSync(p.join(d, '.claude')); console.log(['skipped: no boundary was read · at 1a2b3c4d', 'skipped: a · at b · at unborn', 'skipped: · at 1a2b3c4d'].map((v) => { fs.writeFileSync(p.join(d, '.claude', 'orientation-card.md'), 'card-owner — s1 · x\n## route\n- build: tFix\n## pointers\nitem — ' + v + '\nREADY — tFix\n'); return JSON.stringify(g.readItemPointer(d).item) }).join(' '))" scratch-guard.js`
  runs in the hooks kit's directory, it prints
  `{"skipped":"no boundary was read","at":"1a2b3c4d"} {"skipped":"a · at b","at":"unborn"} {"malformed":"item — skipped: · at 1a2b3c4d","at":"1a2b3c4d"}`;
  and `grep -c 'unborn)' scratch-guard.js` there prints `1`.
  Red when: the skipped answer drops its `at`, a why holding ` · at ` is cut, an empty why reads as
  skipped, or a second `at` pattern stands beside unit 8's.
- **AC6** — When `grep -c 'item pointer skipped' README.md` runs in the hooks kit's directory, it
  prints a count of at least `1`.
  Red when: the kit's section on rule 9 and the fifth check lists unarmed lines without the skipped
  one.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `policy fixtures` · `every held leg is budgeted, every budget row resolves` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · the two plants, `item-skipped` staged red against unit 8's arm, which parses the line as malformed and refuses it · FLOOR_ASSERTIONS the landed pin plus 3

New arm: tools/hooks/agent-cap.test.sh · covers AC4 · `item-skipped`'s `Agent` payload through rule 9, staged red against unit 8's arm, which refuses the throw · none

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
- rev-4 · 2026-11-22 · S1 · S2 · S4 · §4 Files touched · AC4 · §7 · checked for behaviour by
  `2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief`: the skipped answer reaches the arm's
  second caller, `agent-cap.js`'s rule 9, which prints its own unarmed line, observed by AC4 on the
  `agent-cap.test.sh` arm now in Files touched; the parse kept inside `readItemPointer`, so the symbol
  map does not move.
- rev-5 · 2026-11-23 · §1 · S1 to S6 · §3 · §4 · §5 · AC1 to AC6 · §7 · §10 · re-grounded at
  `0e5b281a` by `2026-11-23-prompt-KICK-dKeptSession-43-1-spec-writer`, units 8 rev-6 and 13 read as
  landed: the skipped `at` may be `unborn` and the why is the producer's own text, so the plant writes
  `no loop kit position.py resolves in this tree`; unit 8's `{ malformed, at }` kept for every other
  value, an empty why included, and the skipped answer carries `at` so `checkItemBoundary` keeps its
  bytes, observed by the new AC5; the malformed throw's message fixed so AC3 can name the line; the
  shipped texts unit 8 lands that list forms or unarmed cases rewritten, observed by AC6; the floor
  and both budget rows re-priced (S6); the budget-row leg named.

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-8`'s `readItemPointer` in `tools/hooks/scratch-guard.js`,
itself extracted from `checkItemBoundary`'s `item —` read (`tools/hooks/scratch-guard.js#checkItemBoundary`,
read at `0e5b281a`), and its `checkFreeAction`'s unarmed answer; the producer's grammar is
`render_pointers`' (`skills/session-kickoff/manifest-check.sh#render_pointers`). Neither unit 8
function stands in the tree at `0e5b281a`, so the seam is unit 8's as specified at rev-6.
`python tools/codebase-map/reuse_lookup.py "parse the item pointer line of a build card, its skipped
form included"`, re-run 2026-11-23, ranked `parse` (`tools/memory-recall/query.py`), `skipped`,
`parse_args`, `build`, `parse_conf` and `read_item_rows` by name stem only; none parses a card line, so
no existing seam fits beyond unit 8's reader, which is the one extended. The recall query returned
this spec, unit 8's brief row and the audit's H10, which agree with source.

Recall terms used: `python tools/memory-recall/query.py "what does actions.free do when the item pointer is skipped" --terms "actions.free item pointer skipped unarmed readItemPointer checkFreeAction scratch-guard pointers render_pointers unborn malformed"`
