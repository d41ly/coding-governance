# TOOL-aDistilledCharter-1 — the renderer grades one-line regions and renders section 2 from `[charter] adopter_rules`

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

The v4.0 charter states its governing practices and each adopter's own rules as one physical line
per rule. This unit makes that a property the renderer enforces at every render, and gives an
adopter's rules a declared source, so neither the template nor an adopter can grow a paragraph-rule
back without the render refusing it.

## 2. Scope (IN)

- **S1** — `tools/playbook/render_playbook.py` grades every region between a `<!-- one-line -->`
  line and a `<!-- /one-line -->` line AFTER substitution: each non-blank line opens `- ` followed
  by a non-space, and is at most `ONE_LINE_MAX` characters. A continuation line, an over-length line,
  a nested opener and an unclosed region are each a refusal naming the line. Observed by AC1, AC2
  and AC3.
- **S2** — `tools/govkit/entries/playbook.kit.toml` declares placeholder `ADOPTER_RULES`, class
  `defaulted`, default `- none — this repository adds no rules of its own`. An adopter supplies it as
  `[charter] adopter_rules`, a multi-line string `read_charter_table` already admits. Observed by AC4.
- **S3** — Every substituted value loses its trailing newlines, so a TOML multi-line string does not
  add a blank line after the region it fills. Observed by AC4.
- **S4** — The engine's selftest carries the arms of AC1 to AC4, and `adopt-playbook.sh --selftest`
  runs them. Observed by AC5.

## 3. Non-goals (OUT)

- The template text that uses the region. PLAY-aDistilledCharter-1 writes it.
- Gov's own `adopter_rules` answer. PLAY-aDistilledCharter-4 writes it.
- Grading line length outside one-line regions. `tools/check-line-length.sh` keeps its 450 pin.
- Grading what a rule SAYS. The render grades shape: one line, one bullet, bounded length.

### Edges

- **hands-off** `PLAY-aDistilledCharter-1` — fencing section 1 and section 2 of the template.
- **hands-off** `PLAY-aDistilledCharter-4` — gov's `[charter] adopter_rules`.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `render()` (`render_playbook.py:640`) drops fences, then substitutes every placeholder through
  `build_substitution`, then returns. The grade runs at the end of `render()`, so `--check` (the
  `playbook render wiring` leg) and the write mode both pass through it.
- `read_charter_table` (`:486`) admits a newline in a `[charter]` value and refuses the `{{` opener,
  a region marker and control characters. A one-line marker inside a value would let an adopter close
  the region early; the grade refuses a region whose markers do not pair, which catches it.
- `OPEN_RE` (`:115`) matches only the `kit:` and `when:` namespaces, so a `<!-- one-line -->`
  marker passes through `remove_fenced` untouched and survives into the charter. That is intended:
  the rendered `AGENTS.md` keeps the markers, so a reader can see where the shape applies.

### The grade

```
check_one_line_regions(text) -> None, or raise Refusal
  inside = False
  for n, line in numbered lines:
    if line.strip() == '<!-- one-line -->':   refuse on nested; inside = True; continue
    if line.strip() == '<!-- /one-line -->':  refuse on unopened; inside = False; continue
    if inside and line.strip():
      refuse unless line matches ^- \S
      refuse when len(line.rstrip()) > ONE_LINE_MAX
  refuse when inside at end
```

`ONE_LINE_MAX = 200`, a module constant beside `REGION_OPEN`. PINNED on 2026-10-09 as a design
bound, twice the width this corpus wraps prose to; the v4.0 template fitting it is
PLAY-aDistilledCharter-1's observation, not a measurement made here. A refusal names the 1-based line
of the rendered body and its first 60 characters, because the operator edits the source, not the
render.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_one_line_regions` | function | `py.function`; `lexicon.py --suggest check_one_line_regions --as py.function` answered OK |
| `ONE_LINE_MAX` | constant | module constant, no naming cell graded |
| `ADOPTER_RULES` | placeholder | declared in `playbook.kit.toml` |

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/govkit/entries/playbook.kit.toml` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A new gate leg over the template.** It would grade the template only, never an adopter's
  section 2, which exists only after substitution. The render is the one place both are visible.
- **Lowering `check-line-length.sh`'s pin for the whole charter.** It measures length but cannot see
  a continuation line, and the generated node table legitimately holds rows past 200 characters.
- **An `asked` class for `ADOPTER_RULES`.** Every adopter's next `govkit update` would refuse to
  re-render until it answered, and the update would roll the kit back.

## 5. Production-readiness checklist

- security — no new write path; one more refusal before the existing write.
- perf / scale — one pass over the rendered body, linear in its lines.
- error / empty / loading states — an empty region is legal; the default supplies one bullet.
- observability — every refusal names the line and the rule it broke.
- risks — an adopter whose `[charter]` value carries a continuation line is refused at its next
  update and rolled back; the refusal names the line, and DEPL-aDistilledCharter-1 documents the shape.
- testing — selftest arms in `render_playbook.py`, run by `adopt-playbook.sh --selftest`.
- migration — none: the default renders for every adopter that has not answered.
- user docs — `tools/playbook/README.md` gains the region rule and the `adopter_rules` key.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` renders a fixture whose
  one-line region holds a bullet followed by an indented continuation line, the arm sees a refusal
  naming that line. Red when: the continuation renders.
- **AC2** — When the fixture's region holds a bullet longer than `ONE_LINE_MAX`, the arm sees a
  refusal naming the length. Red when: the long bullet renders.
- **AC3** — When the fixture opens a `<!-- one-line -->` region and never closes it, or nests a
  second opener, the arm sees a refusal for each. Red when: either renders.
- **AC4** — When a fixture template carries `{{ADOPTER_RULES}}` inside a region and `deploy.toml`
  gives no answer, the body holds the declared default; given `[charter] adopter_rules` as a
  multi-line string ending in a newline, the body holds those bullets with no blank line added.
  Red when: the default is absent, or a trailing blank line appears.
- **AC5** — When `bash tools/playbook/adopt-playbook.sh --selftest` runs, it prints
  `render_playbook.selftest OK` with the new arms counted. Red when: an arm prints `arm FAIL`.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 AC4 · the BASE engine, which renders a continuation line and an over-length line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` ranked `render` in
`tools/playbook/render_playbook.py` first; this unit extends that engine's `render()` and its
`read_charter_table` grading rather than adding a gate. No existing seam grades line shape after
substitution: `tools/check-line-length.sh` reads files on disk, never a render.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
