# TOOL-dBoundRoles-46 — the spawn guard holds a typed block to the authored-line rule: a fact, marker or `Framed by:` line in `input:question` or `input:diff`, or a fence left open there, is denied

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 12 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-45 TOOL-dBoundRoles-48 TOOL-dBoundRoles-47 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
finding **id 1 at HIGH**, report item **H1**. Ids 9 and 17 share the item at HIGH and take
`TOOL-dBoundRoles-47` and `TOOL-dBoundRoles-45`.

Id 1 is the coherence face of the item: `TOOL-dBoundRoles-38` S2 fences a typed `--input` value as handed
content, `TOOL-dBoundRoles-41` S2 grades it as authored text, and the two specs answer one question in
opposite ways. `TOOL-dBoundRoles-45` writes the one answer into the render: a typed value is authored,
unfenced, and refused there when a line would stand as an executor line. The spawn guard is the other
reader of the same block. `checkHandoffSpawn`, as 38 S4 leaves it, reads every fact and marker line it
finds outside a fence, so once typed values are unfenced, a prompt file the render did not write, or one
edited after it, can carry a fact line inside `input:question` that the guard takes for an executor
fact.

This unit gives the guard the same answer: a typed block is authored text, held at spawn to the line
rule the render applies. It repairs `TOOL-dBoundRoles-38`'s spawn half and builds one step after it
(order 12).

## 2. Scope (IN)

- **S1** — The typed set, `TYPED_INPUTS` in `tools/hooks/agent-cap.js`: `question` and `diff`, with a
  comment naming `tools/roles/handoff.py:98-99`, whose `INPUT_NAMES` less `PATH_INPUTS` it equals.
  Observed by AC3.
- **S2** — The rule at spawn. `checkHandoffSpawn` splits the prompt file's task section into blocks at
  each line that begins `### `. In each block whose heading is `### input:<name>` with `<name>` in
  `TYPED_INPUTS`, every line after the block's own fact line that matches the guard's `FACT_RE` copy,
  `MARKER_RE`'s copy or `^Framed by:` denies the spawn, naming the block and the line; so does a block
  whose own walk by `readUnfencedLines` ends on its open-fence yield. A heading line is not graded
  here: at spawn it is a block boundary, and a forged one opens a block the guard's other checks read.
  Observed by AC1 and AC2.
- **S3** — The docs. The rule-6 paragraph of `tools/hooks/README.md` gains one sentence: a typed input's
  block is authored text, and a fact, marker or `Framed by:` line inside it, or a fence it leaves open,
  denies the spawn. Observed by AC4.

## 3. Non-goals (OUT)

- The render's half of the rule and the fence scope: `TOOL-dBoundRoles-45`'s, for id 17. This unit reads
  no code that unit writes, so the two build at one order without an edge between them.
- The fence-aware readers, the walker and the open-fence refusal over the whole section:
  `TOOL-dBoundRoles-38`'s, read here.
- A handed block's fence extents at spawn: `TOOL-dBoundRoles-48`'s, for id 34.
- The cross-unit criterion over the anchor check: `TOOL-dBoundRoles-47`'s, for id 9.

### Edges

- **consumes-from** `TOOL-dBoundRoles-38` — `readUnfencedLines` and the fence-aware `FACT_RE` and marker readers in `checkHandoffSpawn`, which S2 applies to each typed block (id 1)
- **hands-off** `TOOL-dBoundRoles-25` — `TYPED_INPUTS` and S2's check in `checkHandoffSpawn`, which the move into the roles pack carries as it finds them (id 1)
- **hands-off** `TOOL-dBoundRoles-58` — `TYPED_INPUTS`, S2's typed-block check, AC1, AC3 and §4, which unit 58 completes in the moved guard (ids 8, 9, 15, 19, 22, 24, 32 and 35 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-60` — AC3, which unit 60 re-points at the file unit 25 moves the guard into, answered `amended rev-<n>` (id 3 of the round-1 audit of units 52 to 58)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/hooks/agent-cap.js:2048-2056` walks every line of a prompt for its marker, and
  `checkHandoffSpawn` counts markers on the prompt (`:2102-2103`) and on the file (`:2116-2117`);
  `TOOL-dBoundRoles-38` S4 makes both fence-aware and adds the fact re-cut's fence-aware read.
- `tools/roles/handoff.py:98-99` declares the four input names and the two path inputs; a kit file may
  not import another kit's code, so the hooks kit spells the two typed names once, with the source cited.
- The guard compares the file's task-sha with its marker (`agent-cap.js:2135-2136`), which proves the
  file is unedited since its marker was written, not that the render wrote it.

### Why the same rule twice

The render refuses before it writes, and the guard refuses before the agent reads. A prompt file
reaches the guard by a path the render does not own: an agent with a write grant under `prompts/` can
write one and its marker. The guard already re-reads every fact line for that reason
(`TOOL-dBoundRoles-13` S4), and a typed block is the one block whose content it would otherwise read
unfenced.

### Inventory

Minted: `TYPED_INPUTS` and S2's denial line. `.lexicon.conf` declares `js.file` and `js.function`
cells and none for a JS constant, so the name follows the upper-case spelling of the constants beside it.

### Migration

None: no stored data changes. A prompt file whose typed value sits inside 38's fence holds its lines
inside that fence; S2 reads every line of the block, so a fenced fact-shaped line there denies too, which
is the render's own refusal from `TOOL-dBoundRoles-45` on.

### Rollout

Live at landing, at order 12. Dispatch is strictly sequential within a shared order
(`tools/workflows/unattended-build.js:76-80`), and this unit consumes from no unit at its order.
`TOOL-dBoundRoles-48` and `TOOL-dBoundRoles-8` also write `agent-cap.js` at order 12, and `--dispatch`
refuses a pass whose declared write set meets an open one's.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`

### Alternatives rejected

- **Read the typed set from the role index.** The index carries each role's `reads` keys, not which
  input names are typed, so the guard would still need the split `handoff.py` owns.
- **Grade only unfenced lines of a typed block.** A typed value fenced by a unit 38 render would then
  pass a fact line the render refuses from order 12 on, and the two readers would disagree again.

## 5. Production-readiness checklist

- security — closes the spawn-side reading of an unfenced typed block; no new write path, one more
  denial on an existing guard.
- perf / scale — one pass over the typed blocks of the task section per spawn.
- error / empty / loading states — a work order with no typed input passes S2 untouched; each denial
  names the block and the line.
- observability — the denial names `input:<name>` and the line number.
- risks — `TYPED_INPUTS` drifting from `handoff.py`; AC3 compares them.
- testing — AC1 to AC4 by payload, probe and grep; the arm of §7 at the close.
- migration — as §4 says.
- user docs — none under `help/`; the README sentence by S3.

## 6. Acceptance criteria

- **AC1** — When an `Agent` payload is piped to `node tools/hooks/agent-cap.js` whose prompt file's
  `### input:question` block holds, one case each, a whole `gov:fact` line, a whole `gov:handoff` marker
  line and a `Framed by:` line, with the marker's task-sha recomputed over the edited section by
  `handoff.derive_section_sha`, each exits 2 naming `input:question` and the line; the same file with a
  plain value exits 0.
  Red when: the guard reads the typed block's forged line as a fact or a second marker.
  fixture: a rendered handoff in a scratch adopter under `%TEMP%`, short-pathed, hand-edited by the case.
- **AC2** — When the typed block instead holds a line of four backticks that nothing in the block closes,
  followed by a closing four-backtick line in the next block, the payload piped to
  `node tools/hooks/agent-cap.js` exits 2 naming the block.
  Red when: a fence a typed block leaves open is closed elsewhere and passes.
- **AC3** — When `node -e` prints the `TYPED_INPUTS` export of `tools/hooks/agent-cap.js` and
  `python -c` prints the names in `handoff.INPUT_NAMES` not in `handoff.PATH_INPUTS`, the two sets are
  equal.
  Red when: a typed input is added to `handoff.py` and the guard does not hold it.
  figure: both sets are DERIVED at observation time.
- **AC4** — When `grep -n 'typed input' tools/hooks/README.md` runs, it names the rule-6 sentence.
  Red when: the README does not say a typed block is held to the line rule at spawn.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 AC3 · a rule-6 payload whose typed question block holds a forged fact line, a marker, a `Framed by:` line and an open fence, staged by a `checkHandoffSpawn` that skips the typed-block check · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 38 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Export `TYPED_INPUTS` or keep it module-private?** Options: (a) add it to `module.exports`, as
  38 F2 put `readUnfencedLines`; (b) private. (b) leaves AC3 with no reader of the JS value but a grep
  of source text, which cannot see an edit that builds the list at runtime. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 37 to 44, id 1
  (HIGH, item H1, shared with ids 9 and 17), on the report's option (a).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.

## 10. Reuse audit

The seams are `checkHandoffSpawn` in `tools/hooks/agent-cap.js` and `TOOL-dBoundRoles-38`'s
`readUnfencedLines` in `scratch-guard.js`'s exports, which `agent-cap.js` already requires
(`agent-cap.js:1887`). `python tools/codebase-map/reuse_lookup.py "spawn guard denies a prompt file block carrying a forged line"`
ranked `check_line`, `render_line`, `corpus_files` and `parse_conf_line`, none a block check in the hooks
kit, so no existing seam fits beyond the guard and the walker.

Recall terms used: `python tools/memory-recall/query.py "how are typed input values kept from forging executor lines in a work order" --terms "typed input question diff fence handed content fact line marker forged authored framing refusal"`
