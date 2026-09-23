# TOOL-aRepatriatedFork-7 — agent-cap: the nested-interpolation fix, and a declared lower cap

**Status:** SPECCED · rev-1 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two agent-cap changes that each retire an adopter fork. First, fix the interpolation-depth defect
`TOOL-dRetiredFork-24` records, which this unit measured as a live fail-open rather than the masked
one the backlog row describes. Second, let a repo declare a fan-out cap LOWER than the kit's 5 in one
tracked place, read by the hook and rendered into the shipped harnesses, so nc's cap of 4 stops
costing a five-file fork.

## 2. Scope (IN)

- **S1** — `renderLexedView` in `tools/hooks/agent-cap.js` saves the enclosing interpolation's brace
  depth when a nested `${` opens and restores it when that interpolation closes, instead of zeroing
  one scalar (`:668`, `:697`, `:705`). This is inCMS's D1, `.claude/hooks/agent-cap.js:699-746` at
  inCMS. Observed by AC1 and AC2.
- **S2** — `renderShippedView` stays byte-identical to its BASE `d65da7ab` body, as the S10 arm at
  `tools/hooks/agent-cap.test.sh:1668-1709` requires, and the hook header states why the frozen view
  keeping the defect is sound: `runBothViews` (`:375-398`) denies when EITHER view denies, so the
  corrected lexed view decides every case the shipped view loses. Observed by AC3.
- **S3** — A nesting matrix of fixtures arms the class: depths two and three, an object literal
  opened before the inner `${`, an arrow body, and a multi-line interpolation, each hiding an
  unbounded verify stage after the inner template and each with a flat control. Observed by AC1 and AC2.
- **S4** — A repo may declare `FANOUT_CAP=<n>` in a tracked `.agent-cap.conf` at its root. The hook
  reads it on every call and enforces `min(n, 5)` wherever it enforces `CAP` or `MAX_VERIFIERS` today:
  the call-site bound, the helper's default parameter, the `gov:bounded-fanout` width, the verify-stage
  total and the direct-spawn slots. The file constants stay 5 and remain the ceiling. Observed by AC4,
  AC5 and AC6.
- **S5** — A declared value that is not an integer from 1 to 5 DENIES every `Workflow` and `Agent`
  call with a message naming the file and the value, the way `AGENT_CAP` is refused today
  (`:1884-1892`). An absent file or key means 5. Observed by AC6.
- **S6** — Every hook message that prints the cap prints the effective one, and so does
  `tools/workflows/check-verifier-fanout.sh:121`, which types `≤5`. Observed by AC7.
- **S7** — The four shipped harnesses carry the cap as a render token, `{{FANOUT_CAP}}`, rendered from
  the same conf by the kit's existing renderer, so a repo declaring 4 receives harnesses the hook admits.
  Observed by AC8.
- **S8** — `agent-cap`, `review-harness` and `drift-audit` bump, and `TOOL-dRetiredFork-24` closes
  with its "not live today" paragraph corrected by the measurement in §4. Observed by AC9.

## 3. Non-goals (OUT)

- Raising the cap above 5 by any route. The ceiling is the file constant and the charter's number.
- `MAX_LENSES`, the array-literal allowance at `tools/hooks/agent-cap.js:453`. nc keeps it at 5 while
  capping concurrency at 4, so one key does not move it.
- Separate keys for concurrency and for the verify-stage total. Both adopters that run a lower cap
  run one number for both; see F1.
- The charter's digits. `tools/check-playbook-parity.sh:120-124` compares the charter template with
  the file constants, which stay 5. A rendered charter stating an adopter's lower cap belongs to the
  charter renderer, `DEPL-aRepatriatedFork-1`'s ground, and is not taken here.
- Fixing `renderShippedView`. Rejected in §4 Alternatives.
- inCMS's pointer rewrites in the same file. They are the remedy-string class `TOOL-dPolishedVitrine-5`
  tracks and `TOOL-aRepatriatedFork-2` drains.

### Edges

none

## 4. Design

### The defect is live, measured

`TOOL-dRetiredFork-24` says a nested interpolation corrupts the view but the fan-out "is still
denied, because a rule matching RAW TEXT catches what the blanked view drops", and
`memory/DECISIONS.md:27` records "the fail-open does not" reproduce. That holds for a raw
`parallel(` and does not hold for a verify stage routed through a sanctioned helper, which the
raw-text rule has no reason to fire on.

Reproduced 2026-09-23 by piping one `Workflow` payload to each hook. The script defines the cap-5
`boundedParallel` helper and one line:

```js
const s = `a ${ f({ k: `b ${ x } c` }) + await boundedParallel(findings.map((g) => () => agent(g)), 5) } d`
```

| hook | nested form | flat form, `f({ k: 1 })` |
|---|---|---|
| gov a7c78ad2 | exit 0, admitted | exit 2, one-agent-per-item verify stage |
| inCMS 1bc57da27, D1 | exit 2, the same rule | exit 2 |
| nc f69e2ffb | exit 2, but only because its cap-4 rule refuses the helper default of 5 | exit 2 |

The lexed view of that line, at gov and at inCMS:

```text
gov    const s = `   f({ k: `   x  `  `
inCMS  const s = `   f({ k: `   x  ` }) + await boundedParallel(findings.map((g) => () => agent(g)), 5)  `
```

At gov everything after the inner template's close is gone. inCMS measured the same pair at its 1.9
bytes and armed it at `.claude/hooks/agent-cap.test.sh:780-791`.

### S1, the fix

A stack of saved depths beside the mode stack: on `${` push the current depth and zero it; on the
closing `}` of an interpolation pop the saved depth back. Exactly inCMS's D1 shape, which pushes onto
`interpDepths` at `:746` and restores at `:735` of its file.

### S2, why the shipped view keeps its bytes

The shipped view is the no-regression baseline. `runBothViews` evaluates each rule over both views
and unions the findings, and the S9 property arm (`tools/hooks/agent-cap.test.sh:1711`) asserts no
script BASE denied is admitted now. A corrupted shipped view can only LOSE code, so its failure mode
is a false negative that the corrected lexed view covers. Editing it would move the baseline the
property is measured against, for no verdict the union does not already reach.

### S4, the declared cap

| where | key | grammar | absent | out of range or malformed |
|---|---|---|---|---|
| `<repo root>/.agent-cap.conf` | `FANOUT_CAP` | `FANOUT_CAP=4` or `FANOUT_CAP="4"`, one line | 5 | deny every call, naming the file |

The root is the directory holding `.git`, found by the walk `gitCommonDir` already does from
`data.cwd` (`tools/hooks/agent-cap.js:1521-1550`). A linked worktree reads its own checkout's file.

**Lower-only is what makes an untracked edit harmless.** `AGENT_CAP` was refused because an
environment override is "a ceiling raise that leaves no diff behind" (`:1889`). A value that can only
LOWER the cap cannot raise anything, so a local edit is at worst stricter than the tracked one.

### S7, rendering the harnesses

`tools/workflows/check-protocol-parity.test.sh` already renders `unattended-build.template.js` into
`unattended-build.js` with three derived tokens, and its no-argument mode is the leg that grades the
render. It gains a fourth token, `FANOUT_CAP`, derived from the same conf with the same default, and
three more pairs.

| live copy | template | sites carrying the token today as a literal 5 |
|---|---|---|
| `tools/workflows/tier2-review.js` | new `tier2-review.template.js` | `:17` helper default, `:396` `MAX_VERIFIERS` |
| `tools/workflows/drift-audit-code.js` | new `drift-audit-code.template.js` | `:24` `CAP`, `:89` `MAX_VERIFIERS` |
| `tools/workflows/drift-audit-state.js` | new `drift-audit-state.template.js` | `:23` `CAP`, `:90` `MAX_VERIFIERS` |
| `tools/workflows/unattended-build.js` | `unattended-build.template.js`, existing | `:131` helper default, `:569` `SPEC_WRITERS` |

The three new pairs move from role `engine` to `rendered` in `tools/workflows/kit.toml`, the move
`unattended-build` made at review-harness 1.8. The adopter migration for that move is the runbook
section `tools/workflows/README.md:50-53` points at.

### Inventory

| minted | cell or kind |
|---|---|
| `.agent-cap.conf` | a new conf file, repo root |
| `FANOUT_CAP` | conf key and render token |
| `loadDeclaredCap` | `js.function`; `lexicon.py --suggest` answered OK for it on 2026-09-23 |
| `EFFECTIVE_CAP` | JS module constant, the value every enforcement site reads |
| three `*.template.js` files | review-harness and drift-audit templates |

### Migration

| adopter | record | disposition |
|---|---|---|
| inCMS | the D1 half of `KIT_AGENT_CAP_DELTA` on `.claude/hooks/agent-cap.js` (`kits.json:267`) | deleted; the row narrows to the pointer rewrites until `TOOL-aRepatriatedFork-2` takes those |
| inCMS | the D1 arm pair in `KIT_AGENT_CAP_TEST_DELTA`, `.claude/hooks/agent-cap.test.sh:780-791` | carried by gov's suite |
| nc | `nc carve-out 13/24` in `scripts/hooks/agent-cap.js:79-86`, `:455-462` | deleted; nc declares `FANOUT_CAP=4` in `.agent-cap.conf` |
| nc | `nc carve-out 13/24` in `scripts/workflows/tier2-review.js:17-18`, `:397` | deleted; rendered |
| nc | `nc carve-out 13/24` in `scripts/workflows/unattended-build.template.js:131-136`, `:574-578`, and its render | deleted; rendered |
| nc | `nc carve-out 13/24` in `scripts/workflows/drift-audit-code.js:24`, `:89` and `drift-audit-state.js:23`, `:90` | deleted; rendered |
| nc | census denominator, `scripts/check-nc-wiring.sh:260-269` | falls by one |
| nc | nc's `CLAUDE.md`, line 145, which names the cap-4 value as an agent-cap carve-out | nc's own prose, pointed at `.agent-cap.conf` |

### Rollout

One gov commit carrying the hook, the renderer, the templates and the bumps. The hook defaults to 5
with no conf, so gov and inCMS see no verdict change except the S1 fix. nc's update lands the
templates, runs the kit's `[[regenerate]]` render and then needs its conf line in the same commit,
or its own cap-4 fork is overwritten by a cap-5 render its hook denies.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/tier2-review.js`
- `tools/workflows/drift-audit-code.js`
- `tools/workflows/drift-audit-state.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/kit.toml`
- `tools/workflows/README.md`
- `tools/drift-audit/drift_report.py` (the `KIT_DRIFT_AUDIT_VERSION` carrier)
- `memory/backlog/TOOL.md` (closing `TOOL-dRetiredFork-24`)

### Alternatives rejected

- **Fix `renderShippedView` too.** It fails the S10 byte arm and moves the baseline S9 measures
  against, and the union already decides every case it would change.
- **An environment knob.** Refused by the hook's own reasoning at `:1880-1892`; even lower-only, an
  environment value leaves no record of what bound a run.
- **The key in `.memory-tree.conf`.** Every tree has one, but it couples the hooks kit to the
  memory-tree kit's conf, which is the coupling `TOOL-aRepatriatedFork-9` is removing from check-arms.
- **Harnesses reading the cap from `args`.** The hook denies an unresolvable bound, which is the
  point of resolving it at the call site (`:1208-1211`).

## 5. Production-readiness checklist

- security — the cap is a rate-limit guard. S5 fails closed on a malformed value, and the ceiling
  cannot be raised; an attacker editing the conf can only make the hook stricter.
- perf / scale — one small file read per `Workflow` or `Agent` call, beside the README and conf reads
  the hook already does for rule 0.
- error / empty / loading states — absent file means 5; a malformed one denies with its own message.
- observability — every denial names the effective cap and, when lowered, the file that lowered it.
- risks — nc's update ordering in §4 Rollout; a missed conf line renders cap-5 harnesses its hook
  denies, and verifier-fanout reds, which is loud rather than silent.
- testing — the nesting matrix and the conf arms in `tools/hooks/agent-cap.test.sh`, the render pairs
  in the parity script.
- migration — three harnesses change role, following the documented 1.8 migration.
- user docs — `tools/hooks/README.md` documents `.agent-cap.conf`; `tools/workflows/README.md`
  lists the new pairs and token.

## 6. Acceptance criteria

- **AC1** — When the §4 nested payload is piped to `tools/hooks/agent-cap.js`, it exits 2 naming the
  verify-stage rule; the a7c78ad2 hook exits 0.
  Red when: the depth is still zeroed and the fan-out after the inner template is invisible.
- **AC2** — When each nesting-matrix fixture and its flat control are piped to
  `tools/hooks/agent-cap.js`, every one exits 2.
  Red when: a shape the matrix names is still admitted, so the fix covered the instance and not the class.
- **AC3** — When the S10 byte arm compares `renderShippedView` with its BASE body, it reports
  `bodies-compared 3 drifted 0` from `tools/hooks/agent-cap.test.sh:1668-1709`'s comparator.
  Red when: the fix leaked into the frozen view.
- **AC4** — When a fixture repo carries `FANOUT_CAP=4` in `.agent-cap.conf`, a harness calling
  `boundedParallel(thunks, 5)` is denied by `tools/hooks/agent-cap.js` and the same harness at 4 is
  admitted; with no conf both are admitted at 5.
  Red when: the declared value is not read, or is read and not enforced at the call site.
- **AC5** — With `FANOUT_CAP=4`, a fifth direct `Agent` spawn in one turn is denied by
  `tools/hooks/agent-cap.js`.
  Red when: the direct-spawn slots still count to the file constant.
- **AC6** — With `FANOUT_CAP=6`, `FANOUT_CAP=0` or `FANOUT_CAP=four`, `tools/hooks/agent-cap.js`
  denies a bounded harness and names `.agent-cap.conf`.
  Red when: an out-of-range value raises the cap or is silently ignored.
- **AC7** — With `FANOUT_CAP=4`, `tools/workflows/check-verifier-fanout.sh` prints `obey the ≤4` in
  its clean line.
  Red when: a message still types 5 over a cap of 4.
- **AC8** — When the renderer runs in a fixture declaring `FANOUT_CAP=4`, every rendered harness
  carries 4 at each site of the §4 table, and `tools/workflows/check-verifier-fanout.sh` judges all of
  them clean under that fixture's cap-4 hook.
  Red when: a rendered site still carries 5, which the adopter's own hook denies.
- **AC9** — After the bumps, `bash tools/check-kit-versions.sh` exits `0`, and with one bumped carrier
  reverted it exits non-zero naming it.
  Red when: a carrier was missed.

## 7. Gates

`agent-cap self-test` · `agent-cap restatement` · `verifier fan-out` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `scratch-guard self-test` · `hook destinations self-test` · `drift-audit selftest` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `playbook parity` · `recall floor` · `recall floor arms` · `kit version markers`

New arm: `tools/hooks/agent-cap.test.sh` · the nesting matrix, piped first to the a7c78ad2 hook to observe the nested forms admitted at exit 0 · none
New arm: `tools/hooks/agent-cap.test.sh` · conf fixtures at 4, 6, 0 and a word, observed first against the a7c78ad2 hook admitting a cap-5 helper under a declared 4 · none
New arm: `tools/workflows/check-protocol-parity.test.sh` · a template with a surviving `{{FANOUT_CAP}}`, observed first to pass the pre-change parity mode · none

## 8. Open questions

- **F1 — one key, or one for concurrency and one for the verify-stage total?** The charter states two
  rules. Both adopters that lower the cap lower both to the same number. Recommendation: one key now;
  a second key is additive later.
  RESOLVED (owner, 2026-09-23): one key for both rules; a second is additive later, as recommended.
  The declared lower-only cap itself, parked by `dRetiredFork`, is ratified.
- **F2 — `.agent-cap.conf` as its own file, or a key in an existing conf?** A new file is one more
  root dotfile; `.memory-tree.conf` couples two kits. Recommendation: its own file, documented in the
  hooks README.
  RESOLVED (owner, 2026-09-23): its own `.agent-cap.conf`, documented in the hooks README, as
  recommended.
- **F3 — should the S9 property arm's population gain the nesting matrix?** It would pin that no
  matrix fixture BASE denied is admitted now. Recommendation: yes, it costs only fixture files.
  RESOLVED (owner, 2026-09-23): yes, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, measured against gov a7c78ad2, inCMS 1bc57da27 and nc f69e2ffb,
  with the nested fail-open reproduced by piping one payload to all three hooks.

## 10. Reuse audit

S1 is inCMS's D1 at `.claude/hooks/agent-cap.js:699-746` there. S7 reuses the one render seam the
workflows kit already has, `render()` in `tools/workflows/check-protocol-parity.test.sh:139-148`,
and its kit.toml `rendered` role. S4's conf reading has no node precedent in the hooks kit;
`tools/codebase-map/reuse_lookup.py` ranked the Python `load_conf` family, which a node hook cannot
call, so no existing seam fits for the reader itself.

Recall terms used: `interpDepth renderLexedView renderShippedView nested interpolation D1 CAP MAX_VERIFIERS lower-only ceiling AGENT_CAP`.
