# TOOL-aClearedLedger-1 — the `[spec]` practice states its one exception: an inline red fix commits no spec and owes its typed record

**Status:** INPROGRESS · rev-1 · 2026-11-13 · node a · Tier-2 · base 8db6f4be · streams tooling · order 1 · closes TOOL-aNimbleMend-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-aClearedLedger-1-1-builder.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-1-builder.md) | journal | — |
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-5 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The charter's `[spec]` practice says every product-code unit commits its spec first, while the
unattended protocol's section 12 lets a leg recorded red be fixed with no spec. The owner ruled on
2026-11-13 that the practice gains the exception, so this unit writes it at the practice's source
and re-renders the three files that carry the line.

## 2. Scope (IN)

- **S1** — In `tools/playbook/practices.toml`, the `line` of the row tagged `practice.spec`
  becomes the text of §4, "The line". The row's tag, its two reach keys and its place in the
  catalogue stay as they are. Observed by AC1.
- **S2** — `AGENTS.md` is re-rendered by the playbook adopter, never edited, so its `[spec]` line
  is the catalogue's and its row in `.governance/instructions.lock` holds the new blob. Observed
  by AC2.
- **S3** — The two role agents whose `rules` key cites `spec`, `.claude/agents/gov-spec-writer.md`
  and `.claude/agents/gov-spec-reviewer.md`, are re-rendered by the roles renderer. Observed by AC3.
- **S4** — The rendered rule stays one line of at most `ONE_LINE_MAX` characters, and no carrier
  outside the catalogue and its three renders states the old rule. Observed by AC2 and AC4.

## 3. Non-goals (OUT)

- Any edit to the text of `AGENTS.md` or of a role agent by hand. The charter template says a rule
  changes at its source and never in the rendered text
  (`coding-governance-agents.template.md@82ceaab5:10`).
- `coding-governance-agents.template.md`. It carries the token `{{PRACTICES}}` where the practice
  lines render and no practice line of its own, so it does not move.
- The row's reach table. `plan` and `build` are derived into a role's load set, never into the
  charter, and a role agent's pass is a specced unit's pass, so both stay true as written.
- The `AGENTS.md` row of `tools/template-size-limits.txt`. §4, "The size row", says why it is the
  owner's.
- `tools/unattended/PROTOCOL.template.md`, which is the second sentence of the ask.
- `help/red-fix-lane.md` and `memory/guides/SESSION-KICKOFF.md`. Both already call the lane the
  one exception to the specced route, so neither is stale after this unit.
- What the lane admits, its limits or its record. This unit states a rule the tree already
  enforces.
- The kit version markers, which the lander's `mint` moves once, after the last unit.

### Edges

- **hands-off** `TOOL-aClearedLedger-2` — the ask's second sentence, the protocol's reason that a
  fix's record is the next commit. This unit's `closes` verb covers the whole ask, so the ask reads
  closed truthfully only once that unit has landed too.
- **hands-off** external — the main loop asks the owner F1 before the pass, and runs the legs of §7
  at the close.

## 4. Design

### Evidence

Read at 82ceaab5, which adds only records to 8db6f4be.

| Fact | Where |
|---|---|
| The practice's line is one catalogue row, and its reach holds the keys `plan` and `build`. | `tools/playbook/practices.toml@6f6d5779:107-112` |
| Four files state the line: the catalogue, the charter and two role agents. | `git grep -n "commits its spec first" -- . ':!memory/builds'` |
| The practices render inside a one-line region, and a line past the cap is refused or warned. | `tools/playbook/render_playbook.py#check_one_line_regions` |
| The cap is `ONE_LINE_MAX`, 200 characters, compared as `len(line.rstrip()) > limit` (PINNED, 2026-11-13). | `tools/playbook/render_playbook.py@918c5286:270`, `:927` |
| The rendered line is 157 characters today, so 43 are free (PINNED, 2026-11-13). | `grep "^- \[spec\] " AGENTS.md`, measured |
| No practice line names a policy key today. Four lines carry a backticked token and none is a key. | `grep -n '^line = .*`' tools/playbook/practices.toml` |
| A role agent carries the practice lines its `rules` key cites, and two roles cite `spec?`. | `tools/roles/roles_lib.py#render_charter_blocks`, `tools/roles/agents/` |
| The charter render records its target's blob in the lock, and that blob is `git hash-object` of the file. | `.governance/instructions.lock`, `git hash-object AGENTS.md` at 82ceaab5 |
| The lane is real and on by default: the write gate admits the write and the commit grader holds the fix. | `tools/unattended/PROTOCOL.template.md@b48ad9f5:722-728` |
| `AGENTS.md` measures 23192 bytes CR-stripped against a row of 23161, past it before this unit (PINNED, 2026-11-13). | `tr -d '\r' < AGENTS.md`, `tools/template-size-limits.txt@a7cfff29:95` |

### The line

The catalogue row's `line` becomes this text, which is F1's recommended option:

```text
Spec before code: every product-code unit commits its spec first, a micro-spec if mechanical, a full design pass if substantive; an inline red fix commits none and owes its typed record.
```

Rendered as `- [spec] ` plus that text it is 195 characters, 5 under the cap (PINNED, 2026-11-13).
It is ASCII, so characters and bytes agree. It keeps both halves of the rule the line states today,
with the sizing clause shortened from "for a mechanical change" and "for a substantive one", and it
adds both halves of the ruling: the fix commits no spec, and it owes its record.

The line does not name the key `bar.inline-red-fixes`, which the build's brief asked for. With the
key the clause is 28 characters longer and the line does not fit beside the sizing clause (PINNED,
2026-11-13). F1 puts that choice to the owner. The switch is named where a reader acts on it:
the protocol's section 12 and `help/red-fix-lane.md`.

### Rendering

Two commands, in this order, each a write and neither a check:

```bash
bash tools/playbook/adopt-playbook.sh --target .
python tools/roles/render_agents.py --write
```

The first writes the charter's region and the lock row. The second reads the charter's practices
region, so it runs after the first. A hook that refuses either command in a role agent's pass
returns the need to the main loop, and the builder edits no rendered file by hand.

### The size row

The `charter size` leg measures `AGENTS.md` against its row.
The file is 31 bytes past that row at 82ceaab5, from an owner's edit in `ee02650d5` (PINNED).
This unit adds 38 bytes and raises no row (PINNED, 2026-11-13). The limits file's first raise term asks that the unit's own
change take the subject past the row (`tools/template-size-limits.txt@a7cfff29:16-28`), and the
subject was past it already, so the movement stays the owner's. `budgets.enforce` reads `warn` in
`.governance/policy.toml`, so the leg warns and does not refuse. PLAY-dOrderedCharter-23 met the
same state and left the row alone, by its commit `33e7b5945`.

### What it does not check

- That a run obeys the line. The write gate and the commit grader enforce the lane, and they do
  not move.
- An adopter's charter. Each adopter renders the new line at its next update, under its own cap.
- The `rules` pairing of the practice. The row carries no `rules` key before or after.

### Inventory

Nothing is minted: no tag, key, flag, leg or file.

### Migration

None. The line's tag and reach are unchanged, so every reader that resolves `practice.spec` still
resolves it.

### Rollout

No switch. The exception the line states is the lane's, which `bar.inline-red-fixes` already turns
on or off.

### Files touched (estimate)

- `tools/playbook/practices.toml`
- `AGENTS.md`
- `.governance/instructions.lock`
- `.claude/agents/gov-spec-writer.md`
- `.claude/agents/gov-spec-reviewer.md`

### Alternatives rejected

- **Raising the one-line cap.** The catalogue ships to every adopter, whose render grades the line
  against the shipped constant, so a longer line warns or refuses there.
- **Stating the exception in the reach table.** Reach text never renders into the charter, and the
  ask is about the level-0 sentence.
- **A second practice row for the lane.** One rule and its exception are one line; a second row
  costs every reader a line and gives the exception a tag nothing cites.
- **Raising the charter's size row here.** See "The size row".

## 5. Production-readiness checklist

- security — No write path or boundary moves. The line describes a lane the write gate already
  bounds, and widens nothing.
- perf / scale — The charter and two role agents each grow 38 bytes (PINNED, 2026-11-13).
- error / empty / loading states — A render that changes any line but the one is drift from an
  earlier landing. The builder returns it and does not fold it in.
- observability — The lock row's blob moves with the render, and `git diff` shows one line per
  carrier.
- risks — The owner may resolve F1 to another wording. Then §4's fenced line and the tokens AC1
  to AC3 grep change in a revision of this spec before code.
- testing — AC1 to AC4 are greps, a `git diff` and a hash compare. The close's render and roles
  legs grade the renders against a fresh one.
- migration — None (§4, "Migration").
- user docs — `help/red-fix-lane.md` already states the exception, so no page moves.

## 6. Acceptance criteria

- **AC1** — When `git diff --numstat 8db6f4be -- tools/playbook/practices.toml` runs it prints one
  row, one line added and one removed, and
  `grep -c "an inline red fix commits none and owes its typed record" tools/playbook/practices.toml`
  prints 1.
  Red when: the exception sits in a second row, or the tag or a reach key moved with the line.
- **AC2** — When `grep "^- \[spec\] " AGENTS.md | awk '{ print length($0) }'` runs after the
  re-render it prints one number, at most 200; `git diff --numstat 8db6f4be -- AGENTS.md` prints one
  line added and one removed; and `git hash-object AGENTS.md` prints the `blob` value of the
  `AGENTS.md` row of `.governance/instructions.lock`.
  Red when: the rule wraps to a second line, the line is past the cap, or the charter was edited by
  hand and the lock keeps the old blob.
  figure: 200 is `ONE_LINE_MAX`, PINNED at 82ceaab5; the printed length is DERIVED, and is 195 for
  §4's line.
  fixture: one changed line rests on the charter being a fresh render at the base. A second moved
  line is drift the builder returns.
- **AC3** — When `grep -c "an inline red fix commits none and owes its typed record" .claude/agents/*.md`
  runs it prints 1 for `gov-spec-writer.md` and for `gov-spec-reviewer.md` and 0 for every other
  file, and `git diff --numstat 8db6f4be -- .claude/agents` prints two rows, each one line added
  and one removed.
  Red when: a role agent keeps the old line, or the render moved an agent that cites no `spec` rule.
- **AC4** — When `git grep -n "commits its spec first" -- . ':!memory/builds'` runs it prints four
  lines, one in each of the catalogue, `AGENTS.md` and the two role agents, and each carries
  `an inline red fix`.
  Red when: a fifth carrier states the rule, or one of the four still states it with no exception.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `instruction render (one renderer of record)` · `charter size` · `roles render wiring` · `roles catalogue` · `check-wiring self-test` · `lexicon naming predicates` · `core practices conformance` · `writing practice (records and units)` · `govkit acceptance matrix` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close's bar runs these once, after the last unit. The two wiring legs and the instruction
render leg compare each render to a fresh one. `charter size` warns today and will warn after this
unit (§4, "The size row").

This unit adds no arm. The class it could break is a charter line that no catalogue row spells, or
a rule past the cap, and both have arms already: the render's `--check-charter` compare and the
one-line refusal of `check_one_line_regions`.

## 8. Open questions

- **F1 — Which wording does the `[spec]` line take, given that the brief's clause and the present
  sizing clause do not both fit in 200 characters?** (PINNED, 2026-11-13)
  The brief asks for a clause saying an inline red fix under `bar.inline-red-fixes` commits no spec
  and owes its typed record, on one line inside the cap. Each option is measured as rendered.
  - **Option A, recommended.** §4's line, 195 characters (PINNED, 2026-11-13). It keeps the sizing
    rule in shorter words and states both halves of the ruling. It does not name the policy key.
  - **Option B.** `Spec before code: every product-code unit commits its spec first, a micro-spec
    or a full design pass; an inline red fix under bar.inline-red-fixes commits no spec and owes
    its typed record.` with the key backticked, 200 characters, exactly the cap (PINNED,
    2026-11-13). It carries the brief's clause whole. It no longer says which change takes which
    spec, a rule the owner did not rule on, and it leaves no character free.
  - **Option C.** Today's sentence unchanged, then `; an inline red fix owes its typed record.`,
    198 characters (PINNED, 2026-11-13). It moves no existing word. It names no key, and does not
    say the fix commits no spec.
  - Recommendation: A. It is the only option that removes no rule from the level-0 line and still
    says the whole ruling. No practice line names a policy key today, and an adopter with no policy
    kit has the lane on with no key to read.
  RESOLVED (owner, 2026-11-13): A, the 195-character line of section 4. It keeps the sizing rule and states both halves of the ruling. <!-- PINNED 2026-11-13 -->

## 9. Revision log

- rev-1 · 2026-11-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render the practice catalogue line into the charter and
role agents"` names the seams this unit extends: `read_practice_catalogue` in
`tools/playbook/instruction_units.py`, `render` in `tools/playbook/render_playbook.py` and
`render_charter_blocks` in `tools/roles/roles_lib.py`. The unit changes one value those three read
and adds no code. The recall probe returned the ask's row, TOOL-aNimbleMend-8 and
TOOL-aNimbleMend-11, whose non-goal left the charter to this ask; PLAY-dOrderedCharter-23 is the
precedent for a practice-line change and its size row, found by `git log` on the catalogue. The
probes and source agree.

Recall terms used: `practice catalogue spec line red-fix lane inline record next commit protocol size row raise one-line`
