# Composition — where your rules render, what a document may weigh, and what an update did

Every document an agent loads is composed from gov's units and your repository's in one place, the
charter renderer of the `playbook-render` kit. This page says where your own units land, how size caps
and a harness's own limit act on the result, how to read the delta report a render and an update print,
and what the practice census moved out of gov's shipped set.

## Where your units render

Your units live in the overlay, `.governance/instructions.toml` (see [the instruction overlay](overlay.md)).
The render reads it at your landed revision.

- **Level 0, the project block.** The charter's section `This repository's own rules` holds the lines of
  `[charter] adopter_rules` in `.governance/deploy.toml`, then one `- <text>` line per level-0 unit of your
  overlay, in the order the overlay holds them. A unit whose `scope` or `trigger` does not select it is
  left out. The declared default bullet, `- none — this repository adds no rules of its own`, renders only
  when neither the key nor a unit supplies a line. The block is a one-line region, so every line is graded
  as one short rule.
- **Levels 3 to 5, the marked part.** A unit of yours at level 3, 4 or 5 renders where a unit slot,
  `<!-- units: <selector> -->`, of a template the renderer renders selects it: an edge-free unit after
  gov's units of its level, an amending one right after the gov unit it names, a replacing one in that
  unit's place. Each run of your units in a slot's output sits between `<!-- gov:repo -->` and
  `<!-- /gov:repo -->`, so a reader can tell your part from gov's; a slot placing none of yours writes no
  pair, and a re-render writes the same pair again rather than nesting a second.
- **Unplaced.** A level-3 to level-5 unit no slot of the render selects renders nowhere, and the render
  names it on one line: `unplaced   repo.four · level 4 · no unit slot of this render selects it`. Today
  the renderer of record renders the charter and its entry files; a slot in another document is that
  document's owning kit's to add.
- **Refused levels.** A unit at level 1, 6 or 7 is refused, naming it: a repository writes neither the
  card, the task nor memory.

## Budgets and harness limits

Each composed document is measured at render, CR stripped, against its cap under `budgets.*`, the
charter's being `budgets."AGENTS.md"`. Over its cap it warns or refuses as `budgets.enforce` says (see
[the size caps](size-caps.md)). Over a harness's own limit, Codex's `CODEX_MAX` for a file it reads whole,
it is refused whatever `budgets.enforce` says, `warn` included. Nothing is ever truncated: a refused
render writes no file.

Every overflow line names the cap and the largest contributors by origin, each with its bytes, so you
know what to move:

```text
budget    load-set — BUDGET WARN · AGENTS.md · 21311 bytes over AGENTS.md 20480 · budgets.enforce is warn · key budgets."AGENTS.md" · largest: gov:playbook 18019 · repository 2292 · gov:alpha 1000
render-playbook: REFUSED — load-set — BUDGET REFUSE · AGENTS.md · 33210 bytes over CODEX_MAX 32768 · Codex's limit for a file it reads whole · largest: gov:playbook 18076 · repository 14134 · gov:alpha 1000
```

`repository` is your project block and your units in the marked parts; `gov:<kit>` a gov kit's units;
`gov:playbook` the template's own text.

## One composition for every harness

`CLAUDE.md` and the other harness files (`GEMINI.md`, `.github/copilot-instructions.md`, `.cursorrules`,
`.windsurfrules`) each hold an `@AGENTS.md` import line, a link to `AGENTS.md`, or a copy of its bytes. A
copy still holding the charter's previous bytes is re-written in the same run that writes `AGENTS.md`, so
it never trails it. The charter's check reds a harness file holding anything else, naming it; re-render,
or re-wire it with the entry-files scope.

## The delta report

A render that writes the charter prints a `composition` heading and one line per gov unit and per gov
row, then one per unit of yours, then each widening; `govkit update` relays the same lines from its
re-render under `govkit update — composition: <n> line(s)`, after its tally, and nothing else of the
render's output. Each line uses update's verdict widths:

```text
  unchanged          [gov:playbook ] practice.yagni
  amended            [repository   ] practice.cost
  excluded           [gov:roles    ] role.scout
  widening           [repository   ] fixture.adopter.alpha-tuned on fixture.alpha · needs remove fixture.beta (gov: fixture.beta, fixture.gamma)
```

| State | What became of gov's unit or row |
|---|---|
| `unchanged` | It renders as gov ships it. A unit of yours with no edge reads `unchanged` too. |
| `amended` | One of your units or rows amends it and renders right after it, or patches it. |
| `replaced` | One of yours supersedes it and renders in its place. |
| `excluded` | `instructions.exclude` lists it, so it renders nowhere. |
| `stale` | A semantic change of gov's landed behind your pin; `instructions.stale` says what happens. |
| `orphaned` | Gov renamed it away, split it or removed it; your amendment is held out. |
| `widening` | A patch of yours grants more than gov's row did, named with gov's value. |

## The practice census

Gov's own rules leave the practice set it ships by a census. The census tool, `practice_census.py` in the
renderer kit, prints one ruling per row of the practice catalogue with its evidence, the paths its line
names and the gate legs enforcing it:

```text
census: practice.writing · gov-only · stays
census:   leg 'writing practice (records and units)' · exempt · enforces practice.writing.one-subject
census: 39 row(s) · ship 38 · gov-only 1 · moves 0 · moves, row kept 0 · stays 1
```

A row is `gov-only` when its evidence is gov's alone: every path it names is shipped by no kit, every leg
naming it runs in gov only, and no role cites it. Every other row, and a row with no evidence, ships.
Beside a `gov-only` row the census prints what becomes of it: `moves`, `moves, row kept`, or `stays` for
a row outside the default set, which gov's charter does not render. At its first run one row ruled
`gov-only`, `practice.writing`, and it stays, so nothing moved out of the set an install takes by default.
