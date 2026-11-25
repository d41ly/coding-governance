# TOOL-dBoundRoles-89 — a sent-back orientation return is one shape that the return check and `place` both take

**Status:** CLOSED · rev-1 · 2026-11-24 · node a · Tier-2 · base f3ec096a8 · streams tooling · order 43

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 TOOL-dBoundRoles-93 TOOL-dBoundRoles-95 TOOL-dBoundRoles-96 |
| [2026-11-24-build-TOOL-dBoundRoles-89-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-89-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-89-deviation-891.md](../build/2026-11-24-build-TOOL-dBoundRoles-89-deviation-891.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-89-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-89-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-89-spec-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-89-spec-brief.md) | journal | — |
| [2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-86-closing-diff-review-round2.md) | diff-review | TOOL-dBoundRoles-86 TOOL-dBoundRoles-87 TOOL-dBoundRoles-88 TOOL-dBoundRoles-90 TOOL-dBoundRoles-91 TOOL-dBoundRoles-92 |

<!-- /gen:spec-records -->

## 1. Goal

The return check sends a failing return back asking for one corrected `json` block, and `place` reads
bare `key: value` lines alone, so an orienter that answers as told is refused at line 1. Its template
also lacks `build`, `breakpoint` and `playbook`, so a JSON placement naming a build fails the check. This
unit gives the template those fields and makes `place` read the very JSON object the check graded. It is item H3
(findings 5 and 29) of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 2. Scope (IN)

- **S1** — The template. The `return` line of `tools/roles/agents/gov-orienter.agent.md` gains
  `build:text?, breakpoint:text?, playbook:text?` after `disposition:text?`, so its fields but `outcome`
  and `card` are the keys of `RETURN_KEYS` (`tools/loop/placement.py#RETURN_KEYS`). Its body's list of
  placement keys, which the rendered `## Return` states, gives way to §4's sentence naming both shapes.
  `.claude/agents/gov-orienter.md` and `.claude/roles.json` are re-rendered by `render_agents.py --write`.
  Observed by AC1, AC2 and AC7.
- **S2** — The budget. The role's static block stays within its `budget` of 6530 bytes, which S1's body
  sentence pays for (§4 "The price", §8 F3). Observed by AC7.
- **S3** — The verb. `handoff.py check-return-file` takes `--object`. On exit 0 with the flag it prints the
  return's JSON object as one line where the return is JSON, and nothing where it is `key: value` lines. The
  object is `roles_lib.extract_return_object`'s over the same text the verb graded, read once. Without
  the flag, and on exit 1 or 2, the verb prints what it prints today. Observed by AC3.
- **S4** — The reader. `check_scout_return` (`tools/loop/placement.py#check_scout_return`) passes
  `--object` and returns the object, or None for lines. `read_scout_return`
  (`tools/loop/placement.py#read_scout_return`) takes it. With None it reads the lines as today, every
  refusal of theirs kept. With an object it refuses an `outcome` other than `placed` first, then a key
  outside `RETURN_KEYS` and `TYPED_RETURN_KEYS`, then a value that is no string or holds a line break, and
  returns the placement keys. A printed line that is no JSON object is refused naming the verb. Observed
  by AC1, AC4, AC5 and AC6.
- **S5** — The texts. `tools/loop/placement.py`'s TYPED CHANNEL paragraph, `tools/roles/handoff.py`'s
  `check-return-file` paragraph and usage line, `tools/roles/README.md`'s "A return read from a file",
  step 2 of `help/roles.md` and the `agent-places` bullet of `help/loop.md` state that a return is `key:
  value` lines or one JSON object, and that a sent-back return is the JSON. Observed by AC8.

## 3. Non-goals (OUT)

- A refused return's own message and its route through `handoff.py route-refusal`, which is item L4
  (finding 30) and `TOOL-dBoundRoles-92`'s. S4 refuses a JSON `outcome: refused` by its outcome alone,
  and the `key: value` form keeps today's refusal.
- The send-back's text, in `run_return_check` (`tools/roles/handoff.py#run_return_check`). It asks every
  role for one `json` block, which is right for every other reader.
- The byte binding of `place --agent`, which holds for a JSON text as it does for lines.
- `add_placement`'s value checks, which both shapes meet after S4.
- A JSON reader inside the loop kit, or an import of the roles kit (§8 F1).

It relates to `TOOL-dBoundRoles-12`, whose typed channel it widens, and `TOOL-dBoundRoles-5`, whose
send-back it answers.

### Edges

none

## 4. Design

### Evidence at HEAD `c31769972`

Probed in-process by this pass, `roles_lib.check_return` beside `placement.read_scout_return` over one
text each:

| return | `check_return` | `read_scout_return` |
|---|---|---|
| a fenced `json` block naming `build` | `build — a field the template does not name` | refused, line 1 is no `key: value` |
| the same block without `build` | no defect | refused, line 1 is no `key: value` |
| `key: value` lines naming `build` | no defect | read whole, `build` among the keys |

- The block reason orders one corrected `json` block holding every required field and no field the
  template does not name (`tools/roles/handoff.py@d123282e:1925-1929`).
- The last row's check passes because the line reader takes only lines naming a template field
  (`tools/roles/roles_lib.py#extract_return_object`), so `build` was never graded.
- `place --agent` requires the file to equal the agent's last text
  (`tools/loop/placement.py#check_agent_return`), so a driver cannot convert the block.
- `check_scout_return` already runs the roles kit's verb as a subprocess, found by `resolve_kit_dir`, and
  discards its stdout on exit 0, which is empty today.
- `extract_return_object(text, [])`, an empty template, returns the fenced or whole JSON object and
  `None` for `key: value` lines, probed on each.
- `add_placement` refuses a value holding a line break, and `write_placement` prints the keys under
  `owner-places` before it, so a JSON value with a line break would print a forged evidence line.

### The verb and the reader

```python
# handoff.py, the check-return-file arm, after a clean grade
if a.object and not lines:
    obj, _why = lib.extract_return_object(text, [])      # JSON alone: no template field, so no line is read
    if obj is not None:
        sys.stdout.buffer.write((json.dumps(obj, ensure_ascii=False) + "\n").encode("utf-8"))

# placement.py
def read_scout_return(path, graded=None):
    if graded is not None:
        if graded.get("outcome", PLACED_OUTCOME) != PLACED_OUTCOME:
            raise PlacementRefused(...)                   # the same text as the lines' outcome refusal
        for key, value in graded.items():
            if key not in RETURN_KEYS + TYPED_RETURN_KEYS: raise PlacementRefused(...)
            if not isinstance(value, str) or "\n" in value or "\r" in value: raise PlacementRefused(...)
        return {k: v.strip() for k, v in graded.items() if k in RETURN_KEYS}
    ...                                                   # the lines, as today
```

The block is the design's shape. `write_placement` hands `check_scout_return`'s answer on. The verb
decides which shape the return is, by the reader that graded it, so the kits hold one answer: a text with
both a block and lines is the block in each. A `card` key in a JSON return is refused, being no placement
key. The text is read once in the verb, so the graded bytes and the printed object are the same bytes.

A `build`, `breakpoint` or `playbook` line is graded once the template names it, so one with an empty
value, which `add_placement` read as `none`, is now a defect naming the field, as an empty `reason` is.

### The body sentence and the price

The body's sentence opening "Write them as" becomes:

```
Write them as `key:
  value` lines or, sent back, as a `json` block: the loop kit's `placement.py place` reads either,
  and its `check` re-reads every fact from source and re-runs every scenario predicate.
```

The static block measures 6530 bytes at HEAD, its `budget` (PINNED 2026-11-24, by
`roles_lib.render_static_block` in-process). S1's template adds 80 to the rendered `## Return` line and
this sentence takes 81 off the body, so the block measures 6529 by that arithmetic, and AC7 measures it
again. Where the pass's bytes land above 6530, the pass trims the body and raises nothing.

### Inventory

Minted: the flag `--object` and the plants `return-json` and `return-sent-back` of `PLANTS`
(`tools/loop/placement.py#PLANTS`). No function name is minted.

### The plants

- `return-json`, in this order: a fenced `json` return naming `build`, put through
  `check-return-file` and then `place`, exits 0 each, and its block equals the one the same fields as
  lines write, but for `placed-utc`; the whole text as one JSON object places; a return naming `build`,
  `breakpoint` and `playbook` writes all of them; a reason holding a line break, a `card` key and an
  `outcome` reading `oriented` are each refused with no block written; and the fields of the `return`
  line in the role file beside the resolved `handoff.py`, less `outcome` and `card`, equal `RETURN_KEYS`.
- `return-sent-back`: a first `key: value` return lacking `outcome` is refused naming it and writes no
  block, then the corrected fenced `json` block, the shape the send-back orders, places with exit 0.

### Migration

None for data: `place` takes every return it takes today, less the empty optional line above. The two
kits ship together, and a `check-return-file` without the flag answers exit 2, which `place` refuses naming it.

### Rollout

Live at landing. The role's `role-sha` moves with its body, so a work order rendered before the pass is
re-rendered, as the spawn guard's refusal names.

### Files touched (estimate)

- `tools/roles/agents/gov-orienter.agent.md`
- `.claude/agents/gov-orienter.md`, `.claude/roles.json` (renders)
- `tools/roles/handoff.py` (`--object`, the docstring)
- `tools/roles/README.md`
- `tools/loop/placement.py` (S4, the docstring, the plants)
- `tools/run-gates/selftest-budgets.txt` (the `loop placement fixtures` row)
- `help/roles.md`, `help/loop.md`

### Alternatives rejected

- **The send-back ordering `key: value` lines of this one role.** The first JSON return still fails at
  `place`, and the text would branch by role.
- **Adding the keys to the line reader of `check_return` only.** A JSON return would still be unplaceable.

## 5. Production-readiness checklist

- security — no new write path; `place` refuses a JSON value that is no string or holds a line break
  before anything is printed or written. The graded object crosses a pipe from the kit's own verb.
- perf / scale — one more parse of a text already read.
- error / empty / loading states — a non-JSON stdout, a non-string value, a foreign key and an `outcome`
  other than `placed` each refuse naming what was found; a verb exit but 0 or 1 refuses as today.
- observability — every refusal opens `placement: refused` and names the key.
- risks — a third-party caller of `check-return-file` sees the same stdout without the flag.
- testing — AC1 to AC6 by plants and direct calls, AC7 by a probe, AC8 by grep; §7's arm at the close.
- migration — none.
- user docs — `help/roles.md` and `help/loop.md` per S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/placement.py --fixture --plant return-json` runs, it prints `held`:
  the fenced JSON return naming a build exits 0 at `check-return-file` and at `place`, and the block it
  writes equals the lines' block but for `placed-utc`.
  Red when: `read_scout_return` parses the fence's first line, or the template lacks `build`.
- **AC2** — When the same `return-json` plant joins the `return` line's fields with `RETURN_KEYS`, they
  are equal less `outcome` and `card`.
  Red when: either side gains a key the other lacks, so a return passes one reader and fails the other.
- **AC3** — When `python tools/roles/handoff.py check-return-file --role gov-orienter --file <file> --object` runs
  over a passing JSON return, it prints that object on one line and exits 0. Over passing `key: value`
  lines it prints nothing and exits 0, and without `--object` it prints nothing over either.
  Red when: the flag prints for lines, or the plain call's stdout changes.
- **AC4** — When `python tools/loop/placement.py --fixture --plant return-sent-back` runs, it prints
  `held`: the first return lacking `outcome` is refused, and the JSON block the send-back orders places.
  Red when: `place` still reads one shape and the send-back orders the other, as at HEAD.
- **AC5** — When the `return-json` plant places a JSON return whose `reason` holds a line break, one with
  a `card` key and one whose `outcome` is `oriented`, each exits 1 naming the key, and no block is
  written.
  Red when: a JSON value reaches a print or a block unchecked.
- **AC6** — When `python tools/loop/placement.py --fixture --plant refusals`, `--plant return-untyped` and
  `--plant return-wrong-role` run, each prints `held`.
  Red when: the lines' own refusals, an odd line and a key given twice among them, are loosened.
- **AC7** — When `python -c` calls `roles_lib.render_static_block` for `gov-orienter` with gov's charter
  and document registry, its UTF-8 length is at most `roles_lib.read_role_budget`'s 6530, and
  `python tools/roles/render_agents.py --check` exits 0.
  Red when: the template grew with the body uncut, the budget was raised instead, or a render is stale.
  figure: 6530 is PINNED by the role file's `budget`; the length is DERIVED at observation time.
- **AC8** — When `grep -n -i "json" help/roles.md help/loop.md tools/roles/README.md
  tools/loop/placement.py` runs, it prints a line of step 2 of the first, of the `agent-places` bullet of
  the second, of the README's "A return read from a file" and of the module's TYPED CHANNEL paragraph, each saying a return may be one JSON object.
  Red when: a page still says a placement return is lines alone.

## 7. Gates

`loop placement fixtures` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `policy fixtures` · `docs` · `help page commands` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/placement.py · covers AC1 AC2 AC4 AC5 · the `return-json` and `return-sent-back` plants, staged by `read_scout_return` ignoring the graded object and by a `return` line without `build` · none

The `loop placement fixtures` row of `tools/run-gates/selftest-budgets.txt` is scaled by the plant count
the pass leaves over the count it holds at HEAD, its `plants=` field moved, marked as its earlier proxies
are. The module derives its cases from `PLANTS`, so it pins no floor.

## 8. Open questions

- **F1 — How does `place` get the JSON object the check graded?** Options: (a) `check-return-file
  --object` prints it; (b) `read_scout_return` parses the fence and the whole object itself; (c) a new
  verb of `handoff.py`. (b) is a second reader of one shape question, the class both findings name, and a
  text with two blocks would read differently in each; (c) grades or reads the file twice. (a) adds one
  flag to the subprocess call `place` already makes, whose stdout on exit 0 is empty. RESOLVED (agent,
  2026-11-24, delegated): (a). options: (a) > (c) > (b) · pick: (a) · admitted-by: principle.p18 ·
  widens: none · relaxes: none
- **F2 — Do `key: value` lines stay a placement shape?** Options: (a) both shapes; (b) JSON alone. (b)
  refuses the return the role's body asks for today and every plant writes; (a) is the report's fix.
  RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none
- **F3 — Does the template's growth raise `budget`?** Options: (a) the body's restated key list pays for
  it and 6530 stands; (b) `budget` moves to the measured bytes. (b) raises a ceiling this run already
  raised once, where (a) removes a list the rendered `## Return` now states whole. The brief asks that
  the growth be priced and the line re-priced; §4 prices it, and the re-priced line reads the same.
  RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) · admitted-by:
  principle.p18 · widens: none · relaxes: none
- **F4 — Is a JSON value with a line break refused, or folded to one line?** Options: (a) refused naming
  the key; (b) folded. (b) records a reason the scout did not write, and `add_placement` already refuses
  the same value. RESOLVED (agent, 2026-11-24, delegated): (a). options: (a) > (b) · pick: (a) ·
  admitted-by: principle.p18 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-24 · initial draft, from the brief `2026-11-24-prompt-TOOL-dBoundRoles-89-spec-brief`
  and item H3 of `2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1`.

## 10. Reuse audit

The seams extended are `tools/loop/placement.py#check_scout_return`, the one subprocess route from the
loop kit to the roles kit's grade, `#read_scout_return`, and `tools/roles/roles_lib.py#extract_return_object`,
whose empty-template call answers which shape a return is. `python tools/codebase-map/reuse_lookup.py
"read an orientation scout's return as JSON or key value lines"` ranked generic readers, `read_text` and
`read_rows` first, and no return reader, so no existing seam fits beyond those. The recall probe returned
`TOOL-dBoundRoles-12` with its deviation and ledger, the review's item, this unit's brief and
`TOOL-dPlacedRequest-10`; the first states that the verb exists because a kit imports no sibling kit.

Recall terms used: `python tools/memory-recall/query.py "how does place read a sent-back orientation return" --terms "placement place read_scout_return check-return-file gov-orienter return template json block send-back key value lines extract_return_object typed channel"`
