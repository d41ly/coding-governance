# TOOL-aGraftedHelix-35 — no by-design entry reaches a spec audit unless it stood at the run's pinned base, and the spec commit's checklist reads its invariants there

**Status:** CLOSED · rev-1 · 2026-10-06 · node a · Tier-2 · base 290d0d2d · streams tooling · order 19 · ratified 2026-10-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-35-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-35-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md](../build/2026-10-06-build-TOOL-aGraftedHelix-29-runlog-b9bb22c3.md) | journal | TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34 TOOL-aGraftedHelix-36 TOOL-aGraftedHelix-37 TOOL-aGraftedHelix-38 TOOL-aGraftedHelix-39 TOOL-aGraftedHelix-40 TOOL-aGraftedHelix-41 |
| [2026-10-06-prompt-TOOL-aGraftedHelix-35-1-spec-brief.md](../prompts/2026-10-06-prompt-TOOL-aGraftedHelix-35-1-spec-brief.md) | journal | TOOL-aGraftedHelix-36 |

<!-- /gen:spec-records -->

## 1. Goal

On the spec-audit route the build harness merges two checker outputs into the audit's checklist: the
resolver's `--for-paths --base <auditBase>`, which unit 29 pinned at the run's base, and the spec
commit's own `--for-diff HEAD~1..HEAD`, whose by-design block is read at the spec commit's parent.
That parent sits inside the build, and `renderChecklistUnion` keeps every by-design entry of both
inputs, so a ruling an earlier pass added can exempt the specs being audited. That is the closing
review's H1 (finding id 1), and its M1 (finding id 18) is the same defect at its binding grade, so
the one fix here discharges both ids. This unit closes it at the union, and gives the spec commit's
checklist the run's base for the one other reader that keeps its block, the audit-OFF hand-out.

## 2. Scope (IN)

- **S1** — `renderChecklistUnion` takes its by-design block from its FIRST input alone. The second
  input's by-design head and entries never reach the merged block, and neither does a header line
  of the second input opening `# invariants are read `, so the merged checklist states one read
  point for its invariants. The second input's class items and its `NEW/CHANGED invariant` items
  still merge as today. This holds whatever command produced the second input. Observed by AC1 and
  AC2.
- **S2** — The union omits any first-input by-design entry whose invariant name appears as a
  whitespace-separated token on the first line of an item in either input. The checker's only item
  that names an invariant is its `NEW/CHANGED invariant <name>` item, so a ruling one input
  itemises as moved never stands as by design beside it. The merged head counts the entries that
  remain, plus the existing `gap`, so the review harness's head-count refusal still fires on a
  truncated block. Observed by AC3.
- **S3** — The spec commit stage runs a pinned checker when `auditBase` is set:
  `python {{MEMORY_TREE_DIR}}/gotchas.py --for-paths --base <auditBase>` over the paths
  `git diff --no-renames --name-only HEAD~1..HEAD` lists, held in one constant,
  `SPEC_COMMIT_CHECKLIST`, which the step-6 prompt, the union's label and the `checklist from` log
  line all read. With `auditBase` empty it runs `CHECKLIST` as today. Observed by AC1 and AC4.
- **S4** — On the audit-OFF route, where `specCommit` rides the hand-out, a spec commit run with
  `auditBase` empty logs one `WARNING:` that `specCommit.checklist` reads invariants at the spec
  commit's parent. A pinned run logs none. Observed by AC4.
- **S5** — The build-harness suite gains a GH35 block: a real-checker arm over a three-commit
  fixture, a cross-input omission arm and the S3 and S4 prompt and log arms. The GH15 arm that
  asserts a merged head counting both blocks is rewritten to assert the first input's block alone.
  `FLOOR_ASSERTIONS` rises by the executed sites added. Observed by AC1, AC2, AC3 and AC4.
- **S6** — The prose that describes the merge says the spec commit's block is left out and where
  the hand-out's block is read: the harness header's Audit stage line, the comments above
  `auditBase`, `renderChecklistUnion` and the union call, and the build-harness paragraph of the
  workflows README. Observed by AC5.
- **S7** — The review-harness kit version and the harness's `unattended-build@` engine identity
  each move once, after the unit's last move, with the suite's engine pin and the render. Observed
  by AC6.

## 3. Non-goals (OUT)

- **The resolver's own checklist is not touched.** Its pin is unit 29's S9, and its unpinned form
  already logs a `WARNING:`. A first input read from the working tree still contributes its block;
  making the shipped caller pass `base` is the review's M3, unit 36's.
- **A caller's `checklist` argument is not checked.** As unit 29 §3 states, a caller's word is the
  caller's authority. S2 still applies to it when a spec commit is merged in.
- **The per-pass checklist the hand-out gives each child, `dispatch.args.checklist`, keeps
  `CHECKLIST`.** No review consumes it: a child acts on its own pass, and the build's review is the
  closing diff review, whose `--for-diff <BASE>..HEAD` unit 29 already reads at the run's base.
  BUILD-METHOD M6 and the unattended skill also spell that per-pass command, and no unit of this
  build edits the method (shared invariant 10).
- **`gotchas.py` is not changed.** `--for-paths --base` already reads the block at a revision and
  itemises what moved since it; S3 composes it. A `--base` on `--for-diff` is rejected in §4.
- **The unattended skill is not changed.** It never names `specCommit`, and its harness-call
  paragraph is unit 36's M3. The brief lists the skill in both units' overlap; this unit's write set
  does not reach it.
- **No new gate leg** (shared invariant 5). Every arm rides `unattended-build self-test`.
- **No class record is edited.** The review's Left-shift line asks for the suite arm, which is S5.

### Edges

- **consumes-from** external — the checker's `--for-paths --base` verb, the harness's `auditBase`
  constant and `renderChecklistUnion` as they stand at `45ce8c76`, the tip this spec was grounded
  on; this unit builds none of them.
- **hands-off** `TOOL-aGraftedHelix-36` — the shipped caller passing the run's pinned base to the
  build harness, the review's M3; until it does, the shipped route runs S3's unpinned branch, and S4
  or unit 29's resolver warning says so.

## 4. Design

### Evidence

Read at `45ce8c76`, the run branch's tip after the closing review's round-1 record.

- `tools/workflows/unattended-build.template.js:433` holds `CHECKLIST`, the `--for-diff HEAD~1..HEAD`
  command. `:456` holds `AUDIT_CHECKLIST`, the bare `--for-paths`, and `:460` holds `auditBase`, the
  `base` argument when it is 7-40 hex and `''` otherwise.
- `renderChecklistUnion` at `:506-525` walks `[first, '# ' + label, second]`. A line matching
  `BY_DESIGN_HEAD` opens a block and adds its count to `gap`; each `- ` line inside a block is
  pushed to `design`, deduplicated against `design` only, from either input. That is the defect.
- The spec commit stage's step 6 at `:1041-1042` runs `CHECKLIST` over the commit and returns its
  stdout as `checklist`, which `:1091` stores as `specCommit.checklist`.
- On the audit route `:1377-1385` merges it after the resolver's checklist and logs
  `merged with the spec commit <sha12>'s --for-diff` at `:1389`. On the audit-OFF route `:2193-2195`
  tells the caller to ACT on `specCommit.checklist` before the first dispatch, and `:2242` puts
  `specCommit` on the hand-out. Those two are every reader of the spec commit's checklist.
- `tools/memory-tree/gotchas.py:588` `cmd_for_paths` takes `base`; with it, `:619-622` derives the
  changed set as every record whose text differs between the base and the working tree, `:624`
  itemises the moved invariants through `derive_moved_invariants`, and `:625-626` builds the block
  from the base's records alone. `cmd_for_diff` at `:692` delegates to it over the range's paths, so
  the class half of `--for-diff HEAD~1..HEAD` and of `--for-paths` over the same paths is one
  selection.
- `render_by_design` at `:687` writes each entry as `- <name> — <looks wrong> → <actually> (<id>)`,
  the shared brief's I4. `MOVED_INVARIANT_ITEM` at `:91` opens `- [ ] NEW/CHANGED invariant <name>`.
- The suite's GH15 arm at `tools/workflows/unattended-build.test.sh:1556` asserts
  `# by design — 2` over `inv-one` and `inv-two`, the second from the commit double: it pins the
  defect. GH16 at `:2201-2251` extracts the commit prompt's fenced block from its `promptjson:`
  line and runs it in a fixture that carries the memory-tree kit at its rendered directory, with
  `python` shadowed by a shell function. `FLOOR_ASSERTIONS` is 532 at `:2458`, and `:1839` pins the
  engine identity at 1.10.

### The probe that decides the fork

Run on node `a`, 2026-10-06, with the real `gotchas.py` at `45ce8c76` over a scratch repository: a
base holding invariant `inv-base` anchored on `memory/LIVE.md`, a pass commit adding invariant
`inv-build` anchored on `memory/LIVE.md`, and a spec commit writing `memory/LIVE.md` and a spec that
declares one script.

| command | `# by design` | items |
|---|---|---|
| `--for-paths --base <base> <the script>`, the resolver's | 0 | none |
| `--for-diff HEAD~1..HEAD`, the spec commit's today | 2: `inv-base`, `inv-build` | none |
| `--for-paths --base <base>` over the spec commit's paths | 1: `inv-base` | `NEW/CHANGED invariant inv-build` |

The second row is H1 reproduced, and it is also what the audit-OFF hand-out carries today. The
third row is S3's command: the build-added ruling becomes an item and the base's ruling stands.
PINNED, measured on that date. AC1 re-derives the first and third rows in the suite's own fixture,
and its staged break, the parent render, re-derives the second.

### Hits and near-misses over the real tree

- **No live instance.** For each of the six newest `spec(aGraftedHelix)` commits since `018b5675`,
  `--for-diff <c>~1..<c>` and `--for-paths --base 018b5675` over that commit's paths both print a
  block of 0. The catalogue holds three invariants, and none is anchored on a path a spec commit
  writes.
- **What the leave-out costs.** `--for-paths --base 018b5675` over `memory/LIVE.md`, the build
  README, the month's ledger and `memory/backlog/TOOL.md` prints a block of 0, so leaving the second
  input's block out of the audit drops no ruling today. DERIVED by that command at build time.

### The union (S1, S2)

`renderChecklistUnion(first, label, second)` keeps its signature and its one caller. The walk
learns which of its three texts it is in. In the third, a `BY_DESIGN_HEAD` line opens a block whose
entries are skipped without touching `gap`, and a header line, one met before that text's first
item, that opens with `INVARIANTS_READ_PREFIX`, the constant `'# invariants are read '`, is skipped.
Both checker header shapes open with it: the pinned `INVARIANTS_AT_BASE` and the unpinned
`INVARIANTS_UNPINNED`. `INVARIANTS_UNPARSED` stays, because what it says holds whichever block
survives.

After the walk, every token on the first line of every collected item, from both inputs, is one set.
An entry in `design` whose `^- (\S+) — ` capture is in that set is omitted. An entry that does not
match that shape is kept, as today. The head renders `BY_DESIGN_FORMAT` at the remaining entries
plus `gap`, so a first input whose own head disagreed with its lines still carries the difference.

The header comment's WHAT IT DOES NOT CHECK grows two lines. A checker header reworded away from
the prefix passes into the merged preamble, though no entry rides with it, because the block is cut
by the parity-gated `BY_DESIGN_HEAD`. An entry the I4 shape does not describe is never matched by
name.

### The spec commit's checklist (S3, S4)

```js
const SPEC_COMMIT_CHECKLIST = auditBase
  ? AUDIT_CHECKLIST + ' --base ' + auditBase + ' $(git diff --no-renames --name-only HEAD~1..HEAD)'
  : CHECKLIST
```

Step 6 runs `SPEC_COMMIT_CHECKLIST` and returns its stdout verbatim whatever its exit status, an
empty selection returning an empty string. The sentence that says it always exits 0 goes, because
both forms exit 1 on a refusal since unit 29. `--no-renames` is
`memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md`'s spelling, so a renamed
path's source is listed too. The command substitution splits on whitespace; a path carrying a space
is split, which the commit block's own `for f in $changed` loop already assumes away, and the header
says so.

The union's label becomes `'the spec commit ' + sha + ' — ' + SPEC_COMMIT_CHECKLIST`. `commitFrom`
becomes `the spec commit <sha12>'s --for-paths at base <auditBase12>` when pinned and keeps
`'s --for-diff` otherwise, and both close on ` (its by-design block left out)`. The existing GH15
arm reads that line as a substring, so it keeps its verdict.

Where `specCommit` is stored, `!specAudit && !auditBase` logs one line:

```text
WARNING: the spec commit's checklist reads invariants at its parent — no pinned `base` was passed,
so an invariant this build added in an earlier pass can stand as by design in `specCommit.checklist`
```

The two lines above are one log line, wrapped here. On the audit route the union leaves that block
out, and the resolver already warns about an unpinned first input, so no second warning prints
there.

### The suite (S5)

GH35 sits after GH16, so it reuses `$LAY`, `$GKD`, the `promptjson:` decode and the `python` shadow.

1. **The real-checker arm.** A fixture repository under `$LAY` holds the memory-tree kit at `$GKD`,
   `.memory-tree.conf` naming `MEMORY_ROOT=memory`, `memory/LIVE.md`, a fixture script and
   `inv-base`, anchored on `memory/LIVE.md`, in its base commit. A pass commit adds `inv-build`,
   anchored the same way, and edits the script. A spec commit writes `memory/LIVE.md` and the
   double's spec path. The harness runs with `base` set to the fixture's base sha and the audit on.
   The arm extracts step 6's command from the commit prompt and the resolver's command from its
   prompt, with `<paths>` as the fixture script, runs both in the fixture, and feeds their stdout to
   a second harness run as the commit double's and the resolver double's `checklist`. It asserts
   the step-6 output's block holds `inv-base` alone and itemises `inv-build`, and that the audit's
   merged checklist carries `NEW/CHANGED invariant inv-build`, a head of 0, and neither entry.
2. **GH15's merged-head arm**, rewritten. Each of the fixture's two checklists gains an
   `# invariants are read at` line after its first header line. The merged checklist carries the
   first's line and not the second's, and `# by design — 1` over `inv-one` with no `inv-two`.
3. **The omission arm.** The first input's block holds `inv-keep`, `inv-q` and `inv-z`, and the
   first input itemises `inv-q`; the second itemises `inv-z`. The merged block is `inv-keep` alone
   under `# by design — 1`.
4. **The prompt and log arms.** With a 40-hex `base` and the audit on, the commit prompt and the
   union label carry the pinned command and the log names the base. With no `base` and the audit
   off, the prompt carries `--for-diff HEAD~1..HEAD` and S4's `WARNING:` prints. With `base` set to
   `origin/main` and the audit off, the same. With a 40-hex `base` and the audit off, no `WARNING:`.

Each arm is observed red on a scratch copy of the render with one break staged, named in §6.

### Inventory

| identifier | where | cell |
|---|---|---|
| `SPEC_COMMIT_CHECKLIST` | `unattended-build.template.js` | constant; none declared |
| `INVARIANTS_READ_PREFIX` | `unattended-build.template.js` | constant; none declared |

No function is added, so the map's symbol index does not move, and no file, leg or conf key is
minted.

### Rollout

Edit the template; re-render with the protocol-parity suite's `--render` mode; observe each GH35
arm and the rewritten GH15 arm red on a scratch copy of the parent render, then green on the new
render; bump both versions and the suite's engine pin after the last move. One build commit.

### Files touched (estimate)

- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`, by the render
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.template.js`, the version line only
- `tools/workflows/tier2-review.js`, by the render

### Alternatives rejected

Each with the observation that rejected it, per BUILD-METHOD M12.

- **The union alone (the review's M1 fix, option A).** It leaves the audit-OFF hand-out reading
  its block at the spec commit's parent: the probe's second row, `# by design — 2` with
  `inv-build`. This build runs with the audit off, so that is its own live route.
- **The pinned command alone (the review's H1 fix, first option).** With no `base` passed, the
  spec commit stage runs `CHECKLIST` and the union keeps its block, so the probe's second row
  reaches the audit; the brief asks for the close at the union.
- **Leaving the second input's block out only when `auditBase` is set**, as the M1 skeptic's text
  reads. With no base the second input is the spec commit's `--for-diff`, read at its parent, which
  is the probe's second row, so the condition would keep H1's input in the audit on the unpinned
  route. Unconditional is one rule and is never the weaker one.
- **Keeping the second input's block when S3 pinned it.** The union cannot see which command an
  agent ran, so the keep would rest on the agent's claim; and the entries it would keep are rulings
  about the specs and the generated views, which bear on no file an audited spec declares. The
  near-miss measurement shows it would keep nothing today.
- **A `--base` option on `--for-diff`.** It is new surface on a verb this unit otherwise leaves
  alone, and it moves the memory-tree kit's shipped bytes, which unit 36 also moves for M2. The
  probe's third row shows the existing `--for-paths --base` already prints what is needed.
- **Matching only the exact `NEW/CHANGED invariant <name>` spelling in S2.** It copies a second
  checker string into the harness with no parity gate, and a rewording would silently stop the
  omission. The token rule depends on the I4 entry shape alone, which the shared brief pins.
- **Pinning `dispatch.args.checklist` the same way.** §3 says why its reader is not a review.

## 5. Production-readiness checklist

- security — Narrows what a by-design block can exempt on the spec-audit route and on the hand-out;
  no write surface widens. The composed command carries `auditBase`, which matched
  `/^[0-9a-f]{7,40}$/` before it was spelled into a prompt, so nothing a caller passes reaches the
  shell unvalidated.
- perf / scale — One `git diff` and one checker run per spec commit, replacing one checker run.
  The union's extra work is one set over the merged items, tens of lines.
- error / empty / loading states — A checker refusal returns its output as `checklist`; with no
  `- ` item the union is not passed and the existing `selected no bug class either` clause says so.
  An empty first input contributes a head of 0.
- observability — The `checklist from` line names the read point and says the spec commit's block
  is left out; the unpinned audit-OFF route logs S4's `WARNING:`. An omitted entry's name is still
  on the checklist as the item that caused the omission.
- risks — The union now discards rulings a pinned second input could have kept; measured at zero
  today (§4). The commit agent runs the composed command through its Bash tool, where `$(...)`
  holds; a shell without command substitution would hand the checker the literal text as paths,
  its output would then carry no item, and the existing clause announces that.
- testing — The GH35 arms and the rewritten GH15 arm, each observed red on a staged break (§6).
- migration — None. A caller passing no `base` sees the same step-6 command; its audit loses only
  the spec commit's by-design entries.
- user docs — The workflows README's build-harness paragraph and the harness header (S6).

## 6. Acceptance criteria

Criteria AC1 to AC4 run as a slice of the build-harness suite in the session scratchpad, under a
name that is not a suite name: the suite's prologue, the GH16 definitions GH35 reuses, and the GH15
and GH35 blocks. Each staged break is made in a scratch COPY of the render and deleted after its
run.

- **AC1** — When the GH35 real-checker arm runs, the step-6 command the commit prompt carries,
  extracted and run in the fixture, prints `NEW/CHANGED invariant inv-build` and a
  `# by design — 1` block holding `inv-base` alone, and the audit's merged checklist, read off the
  `wargs:` line, carries `NEW/CHANGED invariant inv-build` and `# by design — 0` and no `inv-build — `
  or `inv-base — ` entry.
  Red when: the spec commit's by-design block reaches the audit, or the hand-out's block is read
  inside the build. Staged: the parent render, whose step 6 runs `--for-diff HEAD~1..HEAD` and whose
  union keeps both blocks, so the extracted output prints `# by design — 2` and the merged block
  carries `inv-build`.
  fixture: the suite builds the three-commit repository under its own `$LAY`; the tree holds no
  live instance (§4).
  permission: the whole suite is the main loop's, run once at VERIFYING; a pass runs the slice.
- **AC2** — When the rewritten GH15 merged-head arm runs, the merged checklist carries the first
  input's `# invariants are read at` line and not the second's, and `# by design — 1` followed by
  the `inv-one` entry, with no `inv-two` anywhere in its block.
  Red when: the second input's block or its read-point line survives the merge. Staged: the parent
  render, which prints `# by design — 2` over both entries and both header lines.
- **AC3** — When the GH35 omission arm runs, the merged block is `# by design — 1` over `inv-keep`
  alone, and both `NEW/CHANGED invariant inv-q` and `NEW/CHANGED invariant inv-z` stay items.
  Red when: a ruling either input itemises as moved stands as by design. Staged: the name filter
  cut from a render copy, which keeps all three entries under a head of 3.
- **AC4** — When the GH35 prompt arms run, a 40-hex `base` with the audit on puts
  `--for-paths --base <that sha> $(git diff --no-renames --name-only HEAD~1..HEAD)` on the
  `prompt:commit:specs:tB:` line and on the merged checklist's label line, and the log carries
  `merged with the spec commit` and `--for-paths at base` and the base's first 12 characters. No
  `base`, and a `base` of `origin/main`, with the audit off, each keep `--for-diff HEAD~1..HEAD` on
  that prompt line and print the `WARNING: the spec commit's checklist reads invariants at its parent`
  line. A 40-hex `base` with the audit off prints no such line.
  Red when: a pinned base never reaches the spec commit's checker, or an unpinned hand-out is silent.
  Staged: the `auditBase` branch of `SPEC_COMMIT_CHECKLIST` cut, which keeps `--for-diff`; the
  warning deleted; and the shape test dropped from `auditBase`, which forwards `origin/main`.
- **AC5** — When the renderer's `--render` mode has run at the build commit,
  `git status --porcelain tools/workflows/` prints nothing,
  `node tools/workflows/check-workflow-syntax.js` reports every script parsed clean, and
  `python tools/workflows/check_by_design_parity.py tools/memory-tree` exits 0.
  `grep -c "by-design block left out" tools/workflows/README.md tools/workflows/unattended-build.js`
  counts at least 1 in each file, and `grep -c "s --for-diff output" tools/workflows/unattended-build.js`
  prints 0; it prints 1 at `45ce8c76`, the Audit stage line of the harness header.
  Red when: the render is stale, the by-design head copies drift, or a document still describes the
  spec commit's block as merged.
- **AC6** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no review-harness carrier left behind, and
  `bash tools/check-kit-versions.sh` exits 0. Line 3 of `tools/workflows/unattended-build.js`
  carries an engine identity one minor step above its value at the pass's parent, and the suite's
  engine pin names it.
  Red when: the kit's shipped bytes moved without its version, or the pin names the old identity.
  figure: both versions are DERIVED from the pass's parent at observation time.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · GH35, the real checker's step-6 and resolver outputs over a three-commit fixture merge with no build-added ruling by design; stage the parent render · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH15 rewritten, the merged block is the first input's alone and states one read point; stage the parent render · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH35, a ruling either input itemises is omitted from the merged block; stage the name filter cut · the suite's floor rises by the arms added

New arm: tools/workflows/unattended-build.test.sh · GH35, the spec commit's checker is pinned at a 40-hex base and an unpinned hand-out warns; stage the pinned branch cut, the warning deleted and the shape test dropped · the suite's floor rises by the arms added

The close runs the legs and the suite. A pass runs the slice of §6 and the commands of AC5 and AC6
as its check.

## 8. Open questions

- **F1 — Where do H1 and M1 close: at the union, at the spec commit's checker, or at both?**
  Option A is the union alone, the M1 skeptic's corrected fix: the spec commit's block is left out
  and an itemised ruling is omitted. Option B is the H1 fix's first form alone: the spec commit
  stage runs `--for-paths --base <auditBase>` over its commit's paths. Option C is both. A leaves
  the audit-OFF hand-out reading its block inside the build, which the probe measured, and the brief
  asks for that reader to get the base. B leaves the union trusting whatever second input arrives,
  which reaches the audit with no `base` passed, and the brief asks for the close at the union. C
  satisfies every criterion either satisfies and both of the brief's asks. Veto 1: no criterion or
  non-goal is broken. Veto 2: C composes an existing verb and an existing constant, adds no
  dependency, surface or install location, and edits no governance carrier; BUILD-METHOD M6's
  obligation is the checklist over the commit, whose class selection is unchanged. Veto 3: C
  narrows what can be exempted.
  RESOLVED (agent, 2026-10-06, delegated): option C, as S1 to S4 state.

## 9. Revision log

- rev-1 · 2026-10-06 · initial draft, from the unit 35-36 spec brief and the rotated run's closing
  review round 1, H1 (id 1) and M1 (id 18), grounded against the build harness, its suite and
  `gotchas.py` at `45ce8c76`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "merge two bug-class checklists into one by-design block"`
ranked `render_by_design` and name-stem neighbours such as `merge` in `tools/settings-merge.py`, none
of which merges checker outputs; a second probe, `"read the invariant exemptions at the run's pinned
base for a checklist over a commit's paths"`, ranked `read_text` and `run` only. Both printed
`unscanned layers: .sh`, so the suite was read by hand. No map seam fits beyond the ones this unit
extends, read from source: `renderChecklistUnion`, `auditBase` and the step-6 prompt in
`tools/workflows/unattended-build.template.js`, `cmd_for_paths`'s `--base` read in
`tools/memory-tree/gotchas.py`, used unchanged, and the GH15 and GH16 blocks of the build-harness
suite, whose extraction and `python` shadow GH35 reuses. Recall ranked this unit's brief first, then
unit 29's brief and spec, the closing review's H1, and the previous closing review's id 1, which
named this same channel through `renderChecklistUnion`; `TOOL-aFoldedQuarry-6` is why a checker's
stdout is a reviewer's checklist, and `TOOL-aWardedAudit-4` is why the audit route needs the owner's
opt-in. `gotchas.py --for-paths --base 45ce8c76` over the files touched selected six universal
classes and seven anchored ones; §4 and §5 answer `degradation-known-but-unreported` with S4 and the
log line, `two-answers-to-one-question` with the one `SPEC_COMMIT_CHECKLIST`,
`fixture-passes-by-finding-nothing` with positive reads in every arm,
`staged-break-substitutes-a-synthetic-value` with AC1's real checker, and
`orchestrator-hand-off-owed-a-disposition` with the §3 hand-off to unit 36, which exists to dispose
of it.

Recall terms used: by-design invariant exemption spec-audit renderChecklistUnion spec-commit checklist pinned base for-paths for-diff self-exempt union

The question passed with them: "should the spec audit's merged checklist take by-design exemptions
from the spec commit read inside the build".
