# TOOL-dBoundRoles-48 — the composed task section checked block by block: every block opens outside a fence, and each handed block's content lies inside its own, at render and at spawn

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 12 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
finding **id 34 at HIGH**, report item **H3**. No other id shares the item.

`TOOL-dBoundRoles-38` S5 refuses a task section only when the walk ends inside a fence. Nothing checks
that each handed block's content is actually read inside a fence. Framing blocks are unfenced authored
text, and `TOOL-dBoundRoles-23` places `### framing:job` before the `reads` blocks and `### framing:added`
and `### framing:no-stop` after the allowance. A bare three-backtick line in `framing:job` opens a fence,
the handed block's own opening line closes it, and a later framing field holding a backtick run longer
than the handed fence closes the last one, so the walk ends balanced. The handed content, with any fact,
marker or `### allowance` line it quotes, then reads as unfenced, and the render's real fact lines and
the authored allowance fall inside the flipped fence: the forgery 38 exists to close, on the prompt
writer's path.

This unit checks the fence state at every block's extents rather than only at the end of the walk, on
the skeptic's corrected fix. It repairs `TOOL-dBoundRoles-38` and builds one step after it (order 12).

## 2. Scope (IN)

- **S1** — The check, `check_block_fences(section, extents)` in `tools/roles/roles_lib.py`, walking
  `section` with `read_unfenced_lines`. `extents` lists each block's first and last line in the section
  and, for a handed block, the lines of its opening and closing fence. It returns one refusal line, naming
  the block key and the line, for each block whose first line the walk reads inside a fence, each handed
  block whose heading or fact line it reads inside a fence, each handed content line it reads outside
  one, and a walk that ends inside one. Observed by AC1.
- **S2** — The call at render. `render_handoff` computes `extents` from the parts it appended, never by
  re-reading headings or fences in the joined bytes, and calls S1 once, after the last block is added and
  before the marker is hashed. Each line joins `refusals`, so the render raises and writes no file. A
  block a later unit adds before that point is checked with the rest. Observed by AC2.
- **S3** — The check at spawn. `checkHandoffSpawn` (`tools/hooks/agent-cap.js`), as
  `TOOL-dBoundRoles-38` S4 leaves it, denies a prompt file whose task section, walked by
  `readUnfencedLines`, holds an unfenced `FACT_RE` line that is not the line two below an unfenced `### `
  heading, or a block headed by such a pair whose next non-blank line is not a fence opener, whose lines
  up to that fence's closer are not all read inside it, or which holds anything but blank lines between
  that closer and the next unfenced heading. A block whose heading names a typed input, `question` or
  `diff`, is exempt from the fence-shape half. Each denial names the block and the line. Observed by
  AC3.
- **S4** — The docs. `tools/roles/README.md`'s handoff section and the rule-6 paragraph of
  `tools/hooks/README.md` each say that every block of the task section opens outside a fence and that a
  handed block's content must lie inside its own fence, checked at render and at spawn. Observed by AC4.

## 3. Non-goals (OUT)

- The fence writer, the walker and the end-of-walk refusal: `TOOL-dBoundRoles-38`'s, read here.
- A typed value's own line rule: `TOOL-dBoundRoles-45` S2 at render and `TOOL-dBoundRoles-46` at spawn.
  S1 and S3 hold a typed block to the boundary rule only, so this unit reads no code either writes and
  the three build at one order without an edge between them.
- Refusing a fence-opener line inside a framing field, the third part of the skeptic's fix, which would
  extend `TOOL-dBoundRoles-43` S36. S1's boundary rule refuses every framing field that leaves a fence
  open, and a framing field holding a fence it closes hides only its own lines, so the extension adds no
  refusal S1 does not make (§4 "Why the boundary rule covers the framing fields").
- The `--framed-by` composition and the frame's block order: `TOOL-dBoundRoles-4`'s and
  `TOOL-dBoundRoles-23`'s, which build later and add their blocks before S2's call.

### Edges

- **consumes-from** `TOOL-dBoundRoles-38` — `read_unfenced_lines`, `readUnfencedLines`, `render_handed_fence` and S5's open-fence refusal, which S1 and S3 extend from the end of the walk to every block's extents (id 34)
- **hands-off** `TOOL-dBoundRoles-23` — S2's call, which runs after the frame places its `### framing:` blocks, so a framing field that flips the fence state across the handed blocks is refused at render (id 34)
- **hands-off** `TOOL-dBoundRoles-25` — S3's check in `checkHandoffSpawn`, which the move into the roles pack carries as it finds it (id 34)
- **hands-off** `TOOL-dBoundRoles-58` — `check_block_fences`, S3's fence check, AC2 and AC3, which unit 58 completes (ids 5, 10, 21, 22, 23, 24, 26, 33 and 35 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md` S5 refuses only a walk that
  ends inside a fence, and S2 leaves charter and framing blocks unfenced.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md` §4 places `### framing:job`
  before the `reads` blocks and `### framing:added` and `### framing:no-stop` after the allowance.
- `tools/roles/handoff.py:381-416` builds the section from a list it appends block by block, so the render
  knows every block's extent without reading its own output.

### The attack, walked

```
### framing:job        ```                 opens a fence of 3 (unfenced authored text)
### input:spec         heading, fact line   read INSIDE the flipped fence
                       ````                 run 4 >= 3: closes it
                       quoted fact line     read OUTSIDE: forged
                       ````                 opens a fence of 4
### allowance          the real allowance   read INSIDE: hidden
### framing:added      `````                run 5 >= 4: closes it; the walk ends balanced
```

S1 refuses at three points: `input:spec`'s heading read inside a fence, its content read outside one,
and `allowance`'s first line read inside one. Any one is enough.

### Why the boundary rule covers the framing fields

A framing field can move the walk's state only by leaving a fence open at its last line, and then the
next block's first line is read inside a fence and S1 refuses. A framing field that opens and closes a
fence changes nothing outside its own lines. A fence-opener refusal in the framing fields would refuse
that second, harmless case and catch nothing the boundary rule misses.

### Inventory

Minted: `check_block_fences` (`py.function`), its refusal line, and S3's denial line, asked of
`python tools/lexicon/lexicon.py --suggest check_block_fences --as py.function` at the pass. If the pass
lifts S3 into a function, its name is asked with `--as js.function`.

### Migration

None: no stored data changes. A handoff rendered before this unit with an unflipped section passes S3
unchanged.

### Rollout

Live at landing, at order 12. Dispatch is strictly sequential within a shared order
(`tools/workflows/unattended-build.js:76-80`), and this unit consumes from no unit at its order.
`TOOL-dBoundRoles-45`, `-46` and `-8` write some of the same files at order 12, and `--dispatch` refuses
a pass whose declared write set meets an open one's.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`

### Alternatives rejected

- **The finder's fix, a fence-line refusal in framing fields alone.** The skeptic judged it unsound: it
  leaves the end-only check, so any other unfenced authored block that flips the state passes.
- **Re-parse headings in the composed bytes at render.** A flipped section hides headings inside a
  fence, which is the defect; the render's own extents carry no such ambiguity.

## 5. Production-readiness checklist

- security — closes the fence flip across handed blocks at render and at spawn; no new write path.
- perf / scale — one walk of the task section per render and per spawn.
- error / empty / loading states — a work order with no handed block checks only block boundaries; each
  refusal names the block and the line.
- observability — every refusal names the block key and the line number.
- risks — a later unit that appends a block after S2's call escapes the check; the hands-off to unit 23
  names the order, and AC2's staged break is a call moved before the last block.
- testing — AC1 to AC4 by probe, render, payload and grep; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`; the two READMEs by S4.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.check_block_fences` on §4's walked section with its
  extents, a `framing:job` block holding a three-backtick line, an `input:spec` block whose content quotes
  a fact line and a `### allowance` block inside a four-backtick fence, an `allowance` block and a
  `framing:added` block holding a run of five backticks, it returns refusal lines naming `input:spec` and
  `allowance`; the same section without the two framing lines returns `[]`.
  Red when: a section whose walk ends balanced passes with its handed content read outside its fence.
- **AC2** — When the roles adopter fixture renders a work order handing a scratch spec, the render exits
  0; and a scratch copy of `tools/roles/handoff.py` that appends one unfenced block holding a lone
  three-backtick line after the handed block, before S2's call, exits non-zero naming that block and
  writes no file.
  Red when: the render checks only the end of the walk, or calls S1 before its last block.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC3** — When an `Agent` payload is piped to `node tools/hooks/agent-cap.js` whose prompt file is
  AC2's render hand-edited into §4's flipped shape, with the marker's task-sha recomputed by
  `handoff.derive_section_sha`, it exits 2 naming the block; the unedited render exits 0.
  Red when: the guard reads the surfaced quoted fact line as an executor fact.
- **AC4** — When `grep -n 'opens outside a fence' tools/roles/README.md tools/hooks/README.md` runs, it
  prints one line per file.
  Red when: either README still describes only the end-of-walk refusal.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · §4's flipped section by direct call and a render with an extra unfenced block, staged by a `check_block_fences` that reads only the end of the walk · none
New arm: tools/hooks/agent-cap.test.sh · covers AC3 · a rule-6 payload whose prompt file is flipped by two authored lines around a handed block, staged by a `checkHandoffSpawn` without S3's check · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 38 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Also refuse a fence-opener line in a framing field, extending `TOOL-dBoundRoles-43` S36?**
  Options: (a) S1 and S3 alone; (b) both, as the skeptic's fix lists. (b) refuses a framing field holding
  a fence it closes, which flips nothing, and adds scope to a converged unit at order 28 that no
  refusal of S1 misses (§4). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, fewer follow-ups. The
  skeptic's `--framed-by` fixture is AC1's section by direct call, because `--framed-by` does not exist
  until order 17. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 37 to 44, id 34
  (HIGH, item H3), on the skeptic's corrected fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dBoundRoles-38`'s two walkers and its S5 refusal, `render_handoff`'s block list
(`tools/roles/handoff.py:381-416`), and `checkHandoffSpawn` in `tools/hooks/agent-cap.js`.
`python tools/codebase-map/reuse_lookup.py "assert each handed block's fence extent in a composed work order section"`
ranked `render_charter_blocks`, `build_aborted_work_landed` and `check_work_landed`, none a fence-extent
check, so no existing seam fits beyond the walkers and the render's list.

Recall terms used: `python tools/memory-recall/query.py "how are typed input values kept from forging executor lines in a work order" --terms "typed input question diff fence handed content fact line marker forged authored framing refusal"`
