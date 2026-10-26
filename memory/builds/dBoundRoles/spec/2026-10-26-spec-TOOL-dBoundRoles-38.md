# TOOL-dBoundRoles-38 — handed content fenced inside the work order, and every reader of a fact line or a marker line skips what a fence holds

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 11 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 |
| [2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-37 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 26 unit specs
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md`) confirmed finding **id 52 at
HIGH**, report item **H4**. No other id shares the item.

`TOOL-dBoundRoles-13` S3 pastes each handed input's content into `## Task` raw, straight after its fact
line, and S4's spawn guard re-derives every `FACT_RE` line of the task section. A fact line quoted inside
handed content therefore reads exactly like one the executor wrote. Spec 13's own §4 example is such a
line, keyed to a `memory/builds/tFix/...` path that does not exist, so handing spec 13 to its builder
refuses every spawn. Three tracked specs quote a `<!-- gov:handoff role=` line, and a quoted marker
breaks the exactly-one-marker rule that rule 6 and `TOOL-dBoundRoles-4` S4 read. A quoted fact line also
carries a class its author typed, which P29 forbids.

This unit puts each handed block's content inside a backtick fence longer than any backtick run the
content holds, with the fact line outside and before it, and makes every reader of a fact line or a
marker line walk the text fence-aware, so nothing inside a fence is read as either. It repairs
`TOOL-dBoundRoles-13` and builds one step after it (order 11).

## 2. Scope (IN)

- **S1** — The fence writer, `render_handed_fence(content)` in `tools/roles/roles_lib.py`: the content between
  an opening and a closing line of `n` backticks and nothing else, `n` one more than the longest run of
  backticks anywhere in the content and at least 3. The content's bytes are unchanged inside. Observed
  by AC2.
- **S2** — The render. `render_handoff` (`tools/roles/handoff.py:312`), as `TOOL-dBoundRoles-13` S3
  leaves it, writes each handed block as its `### <key>` heading, a blank line, its fact line, a blank
  line, and `render_handed_fence(<content>)`. Every block a `reads` value renders is handed content and is
  fenced, the card, brief and argument values included. The charter blocks and the prompt writer's
  `### framing:` blocks are not handed content and are not fenced. Observed by AC1.
- **S3** — One fence walker per language. `read_unfenced_lines(text)` in `tools/roles/roles_lib.py`
  yields `(line number, line)` for every line outside a fence, and finally `(opened at, None)` when the
  text ends inside one. A fence opens on a line of at most three spaces of indent and then three or more
  backticks or three or more tildes, and closes only on a line of the same character whose run is at
  least as long, with nothing after it but whitespace. `readUnfencedLines(text)` in
  `tools/hooks/scratch-guard.js`, added to its `module.exports`, is the same walker for the hooks.
  Observed by AC2 and AC4.
- **S4** — The readers walk it. `extract_prompt_marker` (`tools/roles/roles_lib.py:246-255`) counts the
  marker lines it finds outside a fence. `extractHandoffMarker` (`tools/hooks/agent-cap.js:2048-2056`),
  which rule 6 calls on the prompt and on the prompt file and which `TOOL-dBoundRoles-4` S4 calls on the
  prompt writer's file, reads only unfenced lines. Every reader of `FACT_RE` `TOOL-dBoundRoles-13` builds,
  the Python reader in `roles_lib.py` and the JavaScript copy in `checkHandoffSpawn`, reads only
  unfenced lines. Observed by AC1 and AC3.
  **Readers:** by name: `tools/roles/roles_lib.py` (`extract_prompt_marker` and the `FACT_RE` reader),
  `tools/hooks/agent-cap.js` (`extractHandoffMarker` and the `FACT_RE` copy in `checkHandoffSpawn`) ·
  by value: `checkHandoffSpawn`'s two marker counts (`agent-cap.js:2102-2103`, `:2116-2117`), its fact re-cut, and
  every `handoff.py` verb that reads a prompt's marker through `extract_prompt_marker`, each now counting
  unfenced lines only.
- **S5** — A fence left open refuses. `render_handoff` refuses a task section whose walk ends inside a
  fence, naming the block and the line the fence opened at, and writes no file. `checkHandoffSpawn` denies
  a prompt file whose task section ends inside a fence, naming the line. A framing or input value that
  opens a fence and never closes it would otherwise hide every later fact line from the re-cut. Observed
  by AC4.
- **S6** — The docs. `tools/roles/README.md`'s handoff section and the rule-6 paragraph of
  `tools/hooks/README.md` say that handed content is fenced, that the fact line sits outside its fence,
  and that a fact line or marker line inside a fence is content. Observed by AC5.

## 3. Non-goals (OUT)

- The fact key, its class and the re-cut itself: `TOOL-dBoundRoles-13`'s, read here.
- The allowance block's reader in `scratch-guard.js`: `TOOL-dBoundRoles-7`'s, and naming which
  `### allowance` heading wins is `TOOL-dBoundRoles-43`'s item for id 54, which walks S3's walker.
- Refusing heading, fact and marker lines inside the prompt writer's framing fields:
  `TOOL-dBoundRoles-43`'s item for id 55. Those fields are authored text and are not fenced here.
- The anchor check's scan scope: `TOOL-dBoundRoles-41`'s, by the extents the render assembled.
- A fence-aware reading of any document other than a rendered handoff and its prompt.
- The report's left-shift checklist entry. S3's walker, shared by every reader, is the regression.

### Edges

- **consumes-from** `TOOL-dBoundRoles-13` — the fact line, `FACT_RE` and its JavaScript copy, and the handed blocks `render_handoff` writes, which S2 fences and S4 makes fence-aware (id 52)
- **hands-off** `TOOL-dBoundRoles-4` — the fence-aware `extractHandoffMarker`, through which S4's exactly-one-marker check reads the prompt writer's file, whose `input:work-order` block now hands quoted markers inside a fence (id 52)
- **hands-off** `TOOL-dBoundRoles-25` — the fence-aware marker and fact readers in `checkHandoffSpawn` and `readUnfencedLines` in `scratch-guard.js`'s exports, which the move into the roles pack carries as it finds them (id 52)
- **hands-off** `TOOL-dBoundRoles-43` — `readUnfencedLines`, which id 54's item uses to name the one `### allowance` heading outside every fence
- **hands-off** `TOOL-dBoundRoles-45` — S2's fence over typed values, which unit 45 narrows to every block but a typed input's; AC4's render half holds from unit 45 on, so this unit's ledger answers it AMENDED, naming unit 45 (id 17 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-46` — `readUnfencedLines` and the fence-aware readers in `checkHandoffSpawn`, which unit 46 applies to each typed block (id 1 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-48` — both walkers and S5's open-fence refusal, which unit 48 extends from the end of the walk to every block's extents (id 34 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-50` — the walkers, the marker readers, AC1's fixture and AC5's grep, which unit 50 completes (ids 10, 18, 25, 35, 36 and 39 of the round-1 audit of units 37 to 44)
- **hands-off** `TOOL-dBoundRoles-58` — AC4, which unit 58 bumps with the text unit 50 answers it by, so the answer names a revision (id 48 of the round-1 audit of units 45 to 51)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md` §4 "The fact line" holds a
  line that `FACT_RE` matches whole, keyed `record:memory/builds/tFix/...`, inside a three-backtick fence.
  `ls memory/builds/tFix` fails. Handed raw into an unfenced block, the line is read as a fact; handed
  inside a three-backtick fence, spec 13's own inner fence closes it early. S1's length rule is what
  keeps the outer fence closed.
- `tools/hooks/agent-cap.js:2048-2056` walks every line, so `checkHandoffSpawn` counts a quoted marker
  (`:2102-2103` on the prompt, `:2116-2117` on the file).
- `tools/memory-tree/tree_lib.py:149-174` is the house's fence walker, with the final open-fence yield
  S3 copies. It toggles on any run of three, so a three-backtick line inside a four-backtick fence closes
  it, and a kit file may not import another kit's library.
- The dClosedLoop instruction review asked for each handed fact to sit in its own data envelope, so a
  quoted directive is not read as one
  (`memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-instruction-b.md:303`).

### The block

~~~
### input:spec

<!-- gov:fact key=record:<path>@<sha12> class=claimed -->

````
<the spec's bytes, CRLF folded; they hold a three-backtick fence, so the run here is four>
````
~~~

The run is one backtick more than the content's longest run, and at least three. The heading and the fact line stay where `TOOL-dBoundRoles-13` put them, so a reader that anchors on
either is unchanged. The fence lines carry no info string. The task-sha covers the fence lines, as it
covers every byte of the section.

### Why a longer fence and fence-aware readers, both

A fence alone fails when the content holds a fence of its own: spec 13 does. A reader alone fails when
the content holds a `### ` heading followed by a fact line, which spec 13 §4 is. Only the two together
close it: the writer guarantees the outer fence cannot be closed from inside, and the readers skip
every line it holds.

### Inventory

Minted: `render_handed_fence` and `read_unfenced_lines` (`py.function`), `readUnfencedLines` (`js.function`),
and S5's two refusal lines. Each name is asked of `python tools/lexicon/lexicon.py --suggest <name>`
with its `--as` cell at the pass.

### Migration

A handoff rendered before this unit carries unfenced content. Its marker and fact lines are still read,
because an unfenced line is read as before, so nothing that admitted before is refused, and a
re-render fences it.

### Rollout

Live at landing on the direct route. At order 11, dispatch sorts a tie by id string
(`tools/workflows/unattended-build.js:608-613`), so `TOOL-dBoundRoles-3` builds first and its card
binding in `checkHandoffSpawn` is present when this unit edits that function.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/README.md`

### Alternatives rejected

- **A sentinel line after each heading.** The report's skeptic found it does not cure the defect:
  handed content can hold a heading followed by a fact line, and spec 13 §4 already does.
- **Escaping each quoted fact or marker line.** It changes the handed bytes, so the content no longer
  equals the source the key was cut from, and the re-cut compares keys of bytes.
- **Importing `tree_lib.unfenced_lines`.** It is the memory-tree kit's, and its rule closes a long fence
  on a short run.

## 5. Production-readiness checklist

- security — closes a forging path: content a role did not write can no longer stand as an executor
  line. No new write path.
- perf / scale — one pass over the task section per read; fences add two lines per handed block.
- error / empty / loading states — an empty handed value renders an empty fence; a fence left open
  refuses at render and at spawn (S5).
- observability — each refusal names the block or the line the open fence started at.
- risks — a role reading its task sees fenced content; the fence is the convention every agent already
  reads as quoted material.
- testing — AC1 to AC5 by render, probe and payload; the arms of §7 at the close.
- migration — as §4 says.
- user docs — none under `help/`; the two READMEs change by S6.

## 6. Acceptance criteria

- **AC1** — When `python handoff.py render --role gov-spec-writer --build tFix --unit TOOL-tFix-1
  --input spec=<scratch spec> --stdout` runs in a scratch adopter, and the scratch spec holds a whole
  `gov:fact` line whose key names a record path that does not exist, a `### input:spec` line followed by
  a second fact line, and a whole `gov:handoff` marker line, the render exits 0. The Python fact reader over the rendered task returns exactly one
  fact per handed block, none of them the scratch spec's, and `extract_prompt_marker` over the rendered
  prompt returns the render's own marker.
  Red when: a reader counts a line inside the fence, so the planted fact or marker is read.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When `python -c` calls `roles_lib.render_handed_fence` on a text holding a run of five backticks it
  returns a fence of six on each end, and on a text holding none a fence of three; and
  `list(roles_lib.read_unfenced_lines(t))` over a four-backtick fence holding a three-backtick line yields
  nothing from inside the fence.
  Red when: the fence has a fixed length, or a shorter run closes a longer fence.
- **AC3** — When an `Agent` payload carrying AC1's handoff is piped to `node tools/hooks/agent-cap.js`, it
  exits 0. When a hand-edited copy of that prompt file moves the quoted marker line outside the fence, the
  payload exits 2 naming `2` marker lines.
  Red when: the guard counts the fenced marker, or stops counting an unfenced one.
- **AC4** — When the render is given `--input question=` holding a line of four backticks that nothing
  closes, it exits non-zero naming the block and the open fence's line, and writes no file; and an
  `Agent` payload whose prompt file's task section ends inside a fence is denied naming the line.
  Red when: a fence left open hides the fact lines after it.
- **AC5** — When `grep -n "fence" tools/roles/README.md tools/hooks/README.md` runs, each names the
  handed-content fence and the rule that a line inside it is content.
  Red when: the READMEs still describe handed content as pasted raw.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC4 · a render handing a spec that quotes a fact line, a heading-then-fact pair and a marker line, staged by a `render_handoff` that writes the content unfenced · none
New arm: tools/hooks/agent-cap.test.sh · covers AC3 AC4 · a rule-6 payload whose handed content quotes a marker inside its fence, staged by an `extractHandoffMarker` that walks every line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 13 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Where does the JavaScript walker live?** Options: (a) `scratch-guard.js`'s exports, which
  `agent-cap.js` already requires (`agent-cap.js:1887`, `:2160`) and which `TOOL-dBoundRoles-7`'s
  allowance reader shares; (b) a function inside `agent-cap.js`; (c) a new module. (b) leaves the
  allowance reader in `scratch-guard.js` to copy it, which the reuse rule forbids at the second
  instance; (c) adds a file every install must ship and wire. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, tie-broken by reuse of the export seam `TOOL-dBoundRoles-25` S4 names as the home of a
  helper two packs read. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 26 unit specs, id 52
  (HIGH, item H4), on the skeptic's corrected fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dBoundRoles-45, -46, -48 and -50, promotions of the round-1 audit of units 37 to 44; the -45 bullet names AC4's AMENDED answer. Nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-58, the minors batch of the round-1 audit of units 45 to 51; nothing else moved.

## 10. Reuse audit

The seams are `render_handoff`'s block list (`tools/roles/handoff.py:381-416`), the two marker readers
(`extract_prompt_marker`, `tools/roles/roles_lib.py:246`; `extractHandoffMarker`,
`tools/hooks/agent-cap.js:2048`), and `scratch-guard.js`'s exports, which `agent-cap.js` already
imports. The fence machine's shape, with its final open-fence yield, is
`tools/memory-tree/tree_lib.py:149` `unfenced_lines`, copied with a length rule rather than imported.
`python tools/codebase-map/reuse_lookup.py "skip lines inside a fenced code block when reading a document line by line"`
ranked `read`, `read_text`, `skip` and `read_conf`, none a fence walker, so no existing seam fits in the
roles or hooks kits beyond the precedent above.

Recall terms used: `python tools/memory-recall/query.py "how is handed content kept from forging machine-read lines in a work order" --terms "fence handed content fact line marker gov:handoff FACT_RE spawn guard work order untrusted quoted"`
