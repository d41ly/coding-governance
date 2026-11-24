# TOOL-dBoundRoles-88 — harness admission holds every nested harness a landed harness calls to its landed blob

**Status:** OPEN · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 42

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-24-prompt-TOOL-dBoundRoles-88-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-88-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`checkHarnessLanded` compares one file, the `scriptPath` the `Workflow` call names. `unattended-build.js`
runs `tier2-review.js` through its own `workflow()` call, which no hook sees, so an edited review harness
runs under a landed parent and its verdict reads as landed-harness evidence. Admission will hold every
declared harness the admitted script's text nests, transitively, to its landed blob. This is item H2
(finding 4) of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 2. Scope (IN)

- **S1** — The nested reader. `extractNestedHarnesses(text, index)` in `tools/roles/spawn-guard.js` reads
  a harness script's text and returns the index's `harnesses` entries its nested calls name, or
  `{ why }`. A nested call is a match of `\bworkflow\s*\(` on a line whose first non-blank characters
  are not `//`. Its argument must open with an object literal whose first key is `scriptPath` and whose
  value is one single-quoted or double-quoted literal naming an entry of `index.harnesses`, both sides
  folded by `buildComparablePath` with a leading `./` ignored, as `resolveHarnessEntry` folds them.
  Observed by AC1, AC3 and AC4.
- **S2** — The transitive hold. `checkHarnessCall` calls `checkHarnessClosure(entry, root, index)` where
  it calls `checkHarnessLanded(entry, root)` today. The closure runs `checkHarnessLanded` on the entry,
  reads its text, and repeats for each callee not yet held. It ends when no new entry is found, so
  the length of `index.harnesses` bounds it and a cycle ends it. Observed by AC1, AC2 and AC3.
- **S3** — The refusals. A callee that is not landed, or differs, is refused with `checkHarnessLanded`'s
  own text, which names the callee, then one sentence naming the harness whose nested call runs it and
  saying the landed bytes cover both files for the whole call. A nested call whose path is no such
  literal, or whose literal names no declared harness, is refused naming the calling harness, the line
  and what was read there (§8 F2). A working-tree harness that cannot be read is refused naming it. Each
  refusal names the driver as the remedy's actor. Observed by AC2, AC4 and AC5.
- **S4** — The text read is the working-tree file, read after its blob compared equal to the landed one,
  so the bytes scanned are the bytes the runtime loads, and they are the landed bytes through the
  repository's clean filters (§8 F1). Observed by AC2 and AC5.
- **S5** — The texts. The docblock's `ADMISSION HELD TO THE LANDED BLOB` and `CEILING` paragraphs of
  `tools/roles/spawn-guard.js`, the spawn guard's section of `tools/roles/README.md` and the
  listed-harness bullet of `help/roles.md` say that admission holds nested harnesses too, that a swap to
  landed bytes covers every nested harness for the whole call, and what the scan cannot see (§4
  "Ceiling"). Observed by AC6.

## 3. Non-goals (OUT)

- A nested-harness key in `.claude/roles.json` (§8 F1).
- Refusing by `args`: a call with `specAudit` unset is held to the callee as well (§8 F3).
- A JavaScript parser, a comment view or a string view. `tools/workflows/script-views.js` is the review
  kit's, and the roles kit declares one in-process edge to a sibling kit, the hooks kit's.
- The spawn guard leg's `guard` list in `tools/govkit/registry.toml`, which is item M10's (finding 21),
  promoted with the minors. The new arm reads the declared harnesses and `.claude/roles.json`, which
  that list does not hold. A harness edited past that guard still meets S3's refusal at call time, which
  fails closed.
- The harnesses themselves. `unattended-unit.js`, which `unattended-build.js` names in a hand-out, is
  run by the main loop as a call of its own, which admission already judges.

It relates to `TOOL-dBoundRoles-25`, whose S3 made the admission this unit widens.

### Edges

none

## 4. Design

### Evidence at HEAD `c31769972`

- `checkHarnessLanded` has one call site, in `checkHarnessCall`, with the top-level entry
  (`tools/roles/spawn-guard.js@139eada2:583`), and `readHarnessBlobs` hashes that path alone
  (`tools/roles/spawn-guard.js#readHarnessBlobs`).
- The nested call is `await workflow(` with `{ scriptPath: 'tools/workflows/tier2-review.js' }` on the
  line under it (`tools/workflows/unattended-build.js@4ecf3bb3:1831`). Its template spells the path
  `{{KIT_DIR}}/tier2-review.js`, so the render in an adopter at another prefix names that install's own
  path, the spelling its role index lists.
- The predicate over the real tree: `grep -niE '\bworkflow\s*\('` over the declared harnesses matches
  `unattended-build.js` alone, at lines 1530, 1534 and 1831 (PINNED, 2026-11-24). The first two open
  with `//` and spell the call in prose, so a scan with no comment rule would refuse every call.
- The defect, observed by this pass's own probe: a fixture repository under `%TEMP%` holding the pack,
  the hooks and policy kits' readers and the declared harnesses at HEAD's bytes, committed on `main`,
  its index listing them. A `Workflow` payload naming `unattended-build.js` exits 0 with all landed. It
  exits 0 with `tier2-review.js` edited in the working tree, which is the hole. It exits 2 naming
  `unattended-build.js` with that file edited.

### The mechanism

```js
function extractNestedHarnesses(text, index) {
  const { buildComparablePath } = loadScratchGuard()
  const fold = (p) => buildComparablePath(p).replace(/^\.\//, '')
  const code = text.split('\n').map((l) => (/^\s*\/\//.test(l) ? '' : l)).join('\n')
  const callees = []
  for (const m of code.matchAll(/\bworkflow\s*\(/g)) {
    const line = code.slice(0, m.index).split('\n').length
    const lit = /^\s*\{\s*scriptPath\s*:\s*(['"])([^'"\\\r\n]+)\1\s*[,}]/.exec(code.slice(m.index + m[0].length))
    if (!lit) return { why: /* line, no literal */ }
    const hit = index.harnesses.find((h) => fold(h) === fold(lit[2]))
    if (hit === undefined) return { why: /* line, the literal, undeclared */ }
    callees.push(hit)
  }
  return { callees }
}

function checkHarnessClosure(entry, root, index) {
  const caller = new Map([[entry, null]])
  for (const [rel, by] of caller) {               // a Map iterates entries added during the walk
    const unlanded = checkHarnessLanded(rel, root)
    if (unlanded) return by === null ? unlanded : /* unlanded, then the sentence naming `by` */
    const nested = extractNestedHarnesses(/* rel under root, utf8 */, index)
    if (nested.why) return /* rel, nested.why, the driver */
    for (const n of nested.callees) if (!caller.has(n)) caller.set(n, rel)
  }
  return null
}
```

The block is the design's shape; the pass fits it to the file, and `resolveHarnessEntry` may share the
fold. A top-level refusal keeps its bytes. A literal is compared as the runtime resolves it,
repository-relative, so an absolute literal names no entry and refuses. Blanking a comment line keeps the
line the refusal names. `checkHarnessLanded` reads the landed revision once per file, so an admission of
`unattended-build.js` pays that read and its git calls for each file held.

### Ceiling

Stated in the docblock, the README and here. The scan reads text. It does not see `workflow` bound to
another name and called through it, or a call on a line of a template literal that opens with `//`. A
block comment spelling `workflow(`, and a comment between the parenthesis and the object, refuse rather
than hide. Each hiding form needs a landed harness that hides its call, and the bar read that
harness. A file edited after admission and before the nested call loads it is not compared again.

### Inventory

Minted: `extractNestedHarnesses` and `checkHarnessClosure`, each answered `OK` by
`python tools/lexicon/lexicon.py --suggest checkHarnessClosure --as js.function` and the same call over
the other name. Neither is exported.

### The arms

They sit in `tools/roles/spawn-guard.test.sh`, beside the `BR25` landed-blob rows and through their
`run_landed` helper. This table's rows derive the floor's term:

| row | fixture | owed |
|---|---|---|
| liveness | `h.js` nests `h5.js`, `h5.js` nests `h6.js`, `h6.js` nests `h.js`, all landed | exit 0, the cycle ended |
| callee edited | `h5.js` edited | exit 2 naming `h5.js` and `h.js` |
| transitive | `h6.js` edited | exit 2 naming `h6.js` and `h5.js` |
| no literal | `workflow({ scriptPath: p })` | exit 2 naming the line |
| undeclared | the literal names a path outside the index | exit 2 naming that path |
| comment | a `//` line spelling `workflow({scriptPath}, args)` | exit 0 |
| real, liveness | every declared harness of gov's `.claude/roles.json`, landed in the fixture | each exits 0 |
| real, held | each callee the arm's own grep finds, edited, its caller called | exit 2 naming the callee; no pair found is a FAIL |

The last row derives its pairs with its own `grep` over the declared harnesses and never through
`extractNestedHarnesses`, since a guard shares no state with what it guards. It fails where a
non-comment `workflow(` line its grep finds yields no pair.

### Migration

None for data. A repository whose own declared harness nests a path that is no literal, or no declared
harness, is refused at its next call by S3's text. Gov's harnesses nest only the literal above.

### Rollout

Live at landing. The consequence for this run's close: a build that edited a harness runs it at its
landed bytes, and from this unit's commit on a call to `unattended-build.js` is admitted only where
`tier2-review.js` is at its landed bytes too, with a spec audit or without one. The trap-guarded swap
the build README's build-level rules state (`TOOL-dBoundRoles-44` S9) therefore covers both files in one
shell, and its restore runs when the call returns, not when it starts, because the nested harness is
loaded when the script reaches it. Calls to `unattended-unit.js` and `tier2-review.js` nest nothing
and need what they need today.

### Files touched (estimate)

- `tools/roles/spawn-guard.js` (S1 to S5)
- `tools/roles/spawn-guard.test.sh` (the rows and the floor)
- `tools/run-gates/selftest-budgets.txt` (the `spawn-guard self-test` row, re-priced)
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **Nested harnesses recorded per entry in the role index** (§8 F1).
- **Comparing every declared harness on every call.** It needs no scan, and it refuses a closing review
  while `unattended-build.js` alone is edited, which no nested call reaches.
- **The callee checking itself.** A workflow script has no filesystem and no git.

## 5. Production-readiness checklist

- security — narrows admission: a call over landed files is refused only where the text nests an
  undeclared or unreadable path. The scan reads bytes the bar has read.
- perf / scale — one more landed-revision read and its git calls per nested harness; the walk is bounded
  by the index's list.
- error / empty / loading states — an unreadable file, an unreadable landed revision and a throw each
  refuse, the last by `main()`'s own catch.
- observability — the refusal names callee, caller and the landed revision's first eight hex digits.
- risks — a harness edited to nest by a variable refuses itself at call time; the real-harness rows red
  first, at the close.
- testing — AC1 to AC5 by direct payloads over a fixture repository, AC6 by grep; §7's arm at the close.
- migration — none.
- user docs — `help/roles.md` per S5.

## 6. Acceptance criteria

- **AC1** — When `node spawn-guard.js` reads a `Workflow` payload naming `unattended-build.js` in a
  fixture repository whose `main` holds gov's declared harnesses, each at its landed bytes, it exits 0.
  Red when: a `//` line spelling the call is read as a nested call, or a landed callee is refused.
- **AC2** — When `node spawn-guard.js` reads the same payload with `tier2-review.js` edited in the working
  tree and `unattended-build.js` landed, it exits 2, and stderr names `tier2-review.js`, the landed sha's
  first eight digits and `unattended-build.js`. The edit committed and not landed exits 2 too, and the
  landed bytes restored exit 0.
  Red when: admission holds the top-level file alone, as HEAD does, so the edited callee exits 0.
- **AC3** — When the fixture's `h.js`, `h5.js` and `h6.js` nest one another in a cycle, all landed,
  `node spawn-guard.js` exits 0 on `h.js`; with `h6.js` edited it exits 2 naming `h6.js` and `h5.js`.
  Red when: the hold stops one call deep, or the cycle never ends.
- **AC4** — When `h.js` nests `workflow({ scriptPath: p })`, `node spawn-guard.js` exits 2 naming the
  line; when it nests a quoted path that is no entry of `harnesses`, it exits 2 naming that path.
  Red when: a nested call the scan cannot place is admitted.
- **AC5** — When the fixture's top-level harness is edited and nests a path the scan cannot place,
  `node spawn-guard.js` exits 2 and its stderr equals, byte for byte, what the pack at `f3ec096a8` prints.
  Red when: the text is scanned before the compare, or the top-level refusal is rewritten.
- **AC6** — When `grep -n "nested" tools/roles/README.md help/roles.md tools/roles/spawn-guard.js` runs,
  it prints a line of the spawn guard's section of the README, one of the listed-harness bullet of the
  help page and one of each of the docblock paragraphs S5 names.
  Red when: a page or paragraph still says admission holds the named harness alone.

## 7. Gates

`spawn-guard self-test` · `policy fixtures` · `roles catalogue` · `roles render wiring` · `docs` · `help page commands` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/spawn-guard.test.sh · covers AC1 AC2 AC3 AC4 · the §4 row table, each refusal staged by calling `checkHarnessLanded` on the entry alone and by a scan returning no callee · `FLOOR_ASSERTIONS` up by the rows' executed assertions, one per row of that table, the term stated in the floor's comment and re-counted at the pass

The `spawn-guard self-test` row of `tools/run-gates/selftest-budgets.txt` is re-priced by the rows' hook
payloads at that row's 0.7s proxy (PINNED there), x1.5, marked as its earlier terms are.

## 8. Open questions

- **F1 — Where does admission learn what a harness nests?** Options: (a) the script's own text, read once
  its blob compared equal to the landed one; (b) a nested-harness key per entry of `.claude/roles.json`,
  rendered by `render_agents.py`. (b) is a second statement of what the script says, adds a render key
  every index reader meets, and can be stale while the script is landed; (a) reads the one source at the
  bytes that run and adds no surface. Both meet every criterion. RESOLVED (agent, 2026-11-24,
  delegated): (a). options: (a) > (b) · pick: (a) · admitted-by: principle.p18 · widens: none ·
  relaxes: none
- **F2 — What is a nested call the scan cannot place?** Options: (a) refused, a non-literal path and an
  undeclared literal alike; (b) admitted, and stated as the ceiling. Under (b) one variable undoes the
  hold with no refusal anywhere, and the pack's own rule is that a guard that cannot read does not admit.
  No declared harness holds such a call, so (a) refuses nothing today. RESOLVED (agent, 2026-11-24,
  delegated): (a), and a call the text scan cannot see at all stays the stated ceiling. options: (a) >
  (b) · pick: (a) · admitted-by: principle.p18 · widens: none · relaxes: none
- **F3 — Is the callee held where the call's `args` carry no `specAudit`?** Options: (a) held on every
  call; (b) held only where `specAudit` is set. (b) puts one harness's argument semantics into the guard
  and fails open for the next nested call under another condition; (a) costs a swap of both files on a
  run that never audits. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief `2026-11-24-prompt-TOOL-dBoundRoles-88-spec-brief`
  and item H2 of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `tools/roles/spawn-guard.js#checkHarnessLanded`, called per file unchanged, its one
caller `#checkHarnessCall`, and `#resolveHarnessEntry`'s fold over the hooks kit's `buildComparablePath`,
with the suite's `run_landed` rows. `python tools/codebase-map/reuse_lookup.py "admit a workflow harness
only at its landed blob"` ranked `readLandedRevision`, which `readHarnessBlobs` already calls,
`resolveHarnessName` of `tools/workflows/script-views.js`, which reads a script's own name and no call,
and Python readers the hook cannot load; no existing seam fits a nested call beyond the module. The
recall probe returned `TOOL-dBoundRoles-25`, whose S3 states no nesting exception, the review's item and
this unit's brief, and `TOOL-dRetiredFork-41`, the ruling that put the nested call in the script.

Recall terms used: `python tools/memory-recall/query.py "does harness admission cover a nested workflow call a harness makes" --terms "spawn-guard harness admission landed blob nested workflow scriptPath declared harness checkHarnessLanded roles.json tier2-review unattended-build"`
