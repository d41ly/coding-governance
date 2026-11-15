# TOOL-aMeasuredDrag-4 — the instruction-edits leg stops re-running the tags check the tags leg already runs

**Status:** INPROGRESS · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md) | research | TOOL-aMeasuredDrag-3 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-4-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-4-1-builder.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The `instruction edits (manifest checks)` leg runs `instructions_edit.py check`, whose `check_tree`
calls `run_tag_check`, which runs `gov_tag.py`'s `check` verb in-process. The `tags (the resolver's
checks)` leg runs that same verb, so every bar runs the tag checks twice, and the two legs contend
on the tag index's write lock. This unit drops the tag checks from the `check` verb, keeps them on
the write verbs' pre-write check, and pins the tags leg as the compensating control.

## 2. Scope (IN)

- **S1** — `check_tree(root, candidate=None, tags=True)` in `tools/playbook/instructions_edit.py`
  runs its `run_tag_check` block only when `tags` is true. The write path's call
  (`instructions_edit.py@57e11a29:299`) is unchanged, so a write still runs the tag checks.
  Observed by AC1.
- **S2** — `run_check` calls `check_tree(root, tags=False)`, so the `check` verb, which is the leg,
  runs no tag check. Observed by AC1, AC2.
- **S3** — The module docstring's `check` usage line and its "THE CHECKS" paragraph say the `check`
  verb leaves the tree's tag checks to `gov_tag.py check`, and what a caller running `check` alone
  no longer sees (§4, "What a caller running `check` alone loses"). The docstring's first paragraph,
  which is the parser's `description`, does not move. Observed by AC3.
- **S4** — The `instruction edits (manifest checks)` row's `why` in `tools/govkit/registry.toml`
  (`registry.toml@7738d217:821`) drops "among them the tag checks" and the clauses that describe
  the tag check's reads, and says the tree's tag checks are the `tags (the resolver's checks)` leg's.
  Observed by AC3.
  **Readers:**
  by name: `tools/govkit/registry.toml` at `:821` is the only tracked file outside the build
  records that spells the retired text, by a git grep at writing. No generated page or other
  file copies the row's `why`. The docstring of `tools/playbook/instructions_edit.py` spells
  "the tag checks over the tree", which is S3's subject and not this text.
  by value: `tools/govkit/govkit.py`'s `exempt_leg` walk reads the `why` only to refuse an empty
  reason, at `:2757` and `:2761`. The new text is not empty, and no reader compares, counts or
  derives from its words.
- **S5** — Arm G8 in `tools/run-gates/run-gates.gov.test.sh`, and `FLOOR_ASSERTIONS` raised from 17
  to 18 with its history line (§4, "The compensating control"). Observed by AC4.
- **S6** — A measured before and after of the `check` verb over the real tree, beside a spawn
  baseline, written into this unit's acceptance ledger. Observed by AC5.

## 3. Non-goals (OUT)

- Dropping the `tags (the resolver's checks)` leg instead, the review's other option.
- The write verbs' tag checks, which stay: a write is still refused on a tag red in the tree.
- Either leg's `ceiling`, and the `instruction edits (manifest checks)` row of
  `tools/run-gates/ceiling-evidence.txt`, which measured the two legs racing. A ceiling moves on a
  measurement at the close or later, never in this pass.
- The tag index's lock and its cleanup scan (contention-3), which the review lists separately.
- A switch or flag that keeps the tag checks on the `check` verb for some callers. It would add a
  public surface, the shape M3's second veto discards.
- `gov_tag.py`, `tag_index.py` and the `fixture` verb's plants.
- The kit version: the lander's mint moves it.
- A `help/` page: none describes the `check` verb (`git grep` of `instructions_edit.py check` under
  `help/` matches nothing at base).

### Edges

- **hands-off** external — re-deriving the `instruction edits (manifest checks)` ceiling from the
  shorter leg is the ceiling tooling's, after this build's bar has measured it.

## 4. Design

### Evidence

Read at base `aebbb4a72`. Lines name blobs of that tree.

| Line | What sits there |
|---|---|
| `tools/playbook/instructions_edit.py@57e11a29:425` | `run_tag_check`: `gov_tag.run_kit_verb(root, "check", …, as_json=True)`, its reds returned |
| `tools/playbook/instructions_edit.py@57e11a29:501` | `check_tree(root, candidate=None)`: every check of a write over the would-be tree |
| `tools/playbook/instructions_edit.py@57e11a29:525` | the `run_tag_check` call; a `PolicyRefused` or `RuntimeError` becomes `red · tags · <exc>` |
| `tools/playbook/instructions_edit.py@57e11a29:534` | `run_check`: `check_tree(root)`, its reds, its lines, the `check · <n> red` count |
| `tools/playbook/instructions_edit.py@57e11a29:299` | the write path: `check_tree(root, {rel: candidate.text})`, a red refuses the write |
| `tools/playbook/instructions_edit.py@57e11a29:1129` | the parser's `description` is `__doc__.split("\n\n")[0]` |
| `tools/gate-legs.json@f9c1a1f8:2097` | `instruction edits (manifest checks)`: `instructions_edit.py check`, chunk `declarations`, no guard |
| `tools/gate-legs.json@f9c1a1f8:2121` | `tags (the resolver's checks)`: `gov_tag.py check`, chunk `declarations`, no guard |
| `tools/run-gates/run-gates.gov.test.sh@17d30d22:454` | G7, the pin that `memory hygiene` stays unguarded, with a liveness check |
| `tools/run-gates/run-gates.gov.test.sh@17d30d22:214` | `FLOOR_ASSERTIONS=17`, stated absolutely with a history line per raise |

`check_tree` has two callers, the write path and `run_check`. `run_verb` reaches `run_check` for the
`check` verb alone. The fixture's `check` cases (`instructions_edit.py@57e11a29:939`, `:943`, `:951`,
`:956`, `:964`) assert this module's own guard, conflict and reference arms, and none asserts a tag
red. The retired-tag case calls `run_tag_check` directly (`:1058`), so it does not move.

### The change

```python
def check_tree(root, candidate=None, tags=True) -> tuple[list, list]:
    """S6 over the tree, `candidate` the would-be manifest: `(reds, the lines a green arm prints)`. `tags`
    false skips the tag checks: the `check` verb leaves them to `gov_tag.py check`, the tags leg
    (TOOL-aMeasuredDrag-4)."""
    ...
    if tags:
        try:
            reds += run_tag_check(root)
        except (PolicyRefused, RuntimeError) as exc:     # RuntimeError: the tag index's TagError
            reds.append(f"{SAY}: red · tags · {exc}")
    ...

def run_check(root) -> tuple[list, int]:
    reds, lines = check_tree(root, tags=False)
```

An explicit keyword, not `candidate is not None`: the call site says what it skips.

### What a caller running `check` alone loses

`python tools/playbook/instructions_edit.py check` no longer prints the reds `gov_tag.py check` names
over the tree: the address and retirement checks the tags leg declares it enforces
(`practice.writing.address`, `practice.writing.retirement`), a retired tag cited in new text among
them. It no longer prints `red · tags · <exc>` when the policy read or the tag index refuses that
verb. Its exit no longer goes to 1 on either. A caller that wants both runs
`python tools/playbook/gov_tag.py check` too, which is what the bar does. Every other red, line and
the count line are as before.

The docstring's usage line becomes:

```
    python instructions_edit.py check             # the leg: a write's checks over the tree, but the tag checks
```

and "THE CHECKS" paragraph's "the tag checks over the tree" becomes "the tag checks over the tree,
on a write only, since the `check` verb leaves them to `gov_tag.py check`, the tags leg, and run
alone does not report them". Both sit below the first blank line, so `--help` does not move.

### The registry row

The `why` becomes: "it runs `<prefix>/playbook/instructions_edit.py check`, the write command's
checks over gov's own manifests and change records, resolving the tags they name through gov's own
index. The tree's tag checks are the `tags (the resolver's checks)` leg's, which the `check` verb
leaves to it (TOOL-aMeasuredDrag-4)." The rest of the string, from "The command ships", is kept.

### The compensating control

Dropping the embedded call is a coverage reduction on any bar that runs `instruction edits (manifest
checks)` and not `tags (the resolver's checks)`. Today none does: both are unguarded, so a scoped bar
never skips either, and both sit in chunk `declarations`. G8 pins that, in the shape of G7:

```
# ---- G8. `tags (the resolver's checks)` DECLARES NO GUARD, AND SHARES THE INSTRUCTION-EDITS CHUNK --
# TOOL-aMeasuredDrag-4 took the tree's tag checks out of `instructions_edit.py check`. Its compensating
# control is that the tags leg runs on every bar that runs `instruction edits (manifest checks)`:
# unguarded, so a scoped bar never skips it, and in the same chunk, so no chunk selection splits them.
#
# WHAT THIS DOES NOT CHECK: a run that names one leg alone, a pass-leg selection, or a cached verdict.
```

The arm's Python loads `$LEGS_FILE`. It requires exactly one row named each of the two legs, and
says it graded nothing otherwise, the liveness G7 states. It then reds when the tags row carries a
`guard` key, or when the two rows' `chunk` values differ, naming the field. `a` gains one, and
`FLOOR_ASSERTIONS=18` with the line `# Raised 17 -> 18 by TOOL-aMeasuredDrag-4, which adds G8, the
tags leg's unguarded pin.`

### Files touched (estimate)

- `tools/playbook/instructions_edit.py`
- `tools/govkit/registry.toml`
- `tools/run-gates/run-gates.gov.test.sh`

### Inventory

No identifier is minted. `check_tree` gains the keyword `tags`. No function is added, so
`memory/map/generated/symbols.json` does not move.

### Rollout

Live, with no switch: the bar's verdict does not move, because the tags leg grades the same tree.

### Alternatives rejected

- **Drop the tags leg and keep the embedded call.** The tags leg carries the `enforces` rows for
  the address and retirement practices and is in the `tags` pack, so the leg is the declared owner.
- **Gate the call on an environment variable the runner sets.** `tools/run-gates/run-gates.sh`
  exports no leg identity to its legs at base, so this adds a runner contract for one leg.
- **Gate it on `candidate is not None`.** It works today, and it couples the tag checks to an
  argument whose meaning is the would-be manifest.

## 5. Production-readiness checklist

- security — no new input, write path or surface; the write path keeps every check it runs.
- perf / scale — the leg stops running the tag verb.
  Its ledger median was 291.5 s, and the tags leg's 263.2 s, PINNED 2026-11-15.
  AC5 measures this unit's code.
- error / empty / loading states — a tag-index refusal now shows on the tags leg alone.
- observability — on a tree with no tag red, the `check` verb's output is unchanged (AC2).
- risks — a later guard on the tags leg, or a chunk move, would leave a bar grading no tag checks;
  G8 reds on either.
- testing — AC1 to AC5 and the arm on the `New arm:` line in §7.
- migration — N/A: no data or record shape moves.
- user docs — the module docstring and the registry row (S3, S4); no `help/` page covers the verb.

## 6. Acceptance criteria

- **AC1** — When the probe below runs from the repository root, it prints `OK`.
  ```
  python -c "
  import sys; sys.path.insert(0, 'tools/playbook'); import instructions_edit as ie
  calls = []; ie.run_tag_check = lambda root: calls.append(1) or []
  root = ie.resolve_root()
  ie.run_check(root); n_check = len(calls)
  ie.check_tree(root); n_tree = len(calls) - n_check
  assert (n_check, n_tree) == (0, 1), (n_check, n_tree); print('OK')"
  ```
  Red when: the `check` verb still calls `run_tag_check`, or the write path's default lost it.
  cost: two passes of the non-tag checks over the real tree.
- **AC2** — When `python tools/playbook/instructions_edit.py check > out; echo $? >> out` runs in the
  worktree before the change and again after it, with `python tools/playbook/gov_tag.py check`
  exiting 0 before, `diff` of the two `out` files prints nothing.
  Red when: any line other than a tag red differs, such as the count line or a reference red.
  cost: the before-run carries the tag verb; the leg's median was 291.5 s, PINNED 2026-11-15.
- **AC3** — When `grep -c "run alone does not report them" tools/playbook/instructions_edit.py` runs
  it prints 1, and over `tools/govkit/registry.toml` `grep -c "among them the tag checks"` prints 0 and
  `grep -c "which the \`check\` verb leaves to it (TOOL-aMeasuredDrag-4)"` prints 1.
  Red when: the docstring or the registry row still says the `check` verb runs the tag checks.
- **AC4** — When the probe below runs from the repository root, it prints `OK`.
  ```
  python -c "
  import json; legs = json.load(open('tools/gate-legs.json', encoding='utf-8'))
  t = [l for l in legs if l.get('name') == \"tags (the resolver's checks)\"]
  e = [l for l in legs if l.get('name') == 'instruction edits (manifest checks)']
  assert len(t) == len(e) == 1 and 'guard' not in t[0] and t[0].get('chunk') == e[0].get('chunk'); print('OK')"
  ```
  Red when: the tags leg carries a guard, or its chunk differs from the instruction-edits leg's.
- **AC5** — When the two AC2 runs are each timed with `time`, and `time (for i in 1 2 3 4 5 6 7 8 9
  10; do /usr/bin/true; done)` is timed beside each, the acceptance ledger records the four wall
  times and the after-run is shorter than the before-run.
  Red when: the after-run is not shorter than the before-run.
  figure: every time is DERIVED at observation and recorded in the ledger with its date.

## 7. Gates

`instruction edits (manifest checks)` · `instruction edits selftest` · `tags (the resolver's checks)` · `run-gates gov canary` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `docs`

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC4 · `tools/gate-legs.json` with a `guard` added to the tags row, then with its chunk moved to `selftests`; and the arm with the tags row renamed, which must red on its liveness check · FLOOR_ASSERTIONS 17 to 18

The close's `instruction edits selftest` run re-observes, unchanged, the fixture's five `check`
cases and the retired-tag case that calls `run_tag_check` directly.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seam is `check_tree` in `tools/playbook/instructions_edit.py`, edited in place as the brief's
Reuse names, with `run_tag_check` and the tags leg's `gov_tag.py check` left as they are. The
compensating arm reuses G7's shape in `tools/run-gates/run-gates.gov.test.sh`, the gov-only home that
file's header gives arms keyed on gov's own legs. `tools/codebase-map/reuse_lookup.py`, given
"skip a duplicate check another leg already runs", ranked `run`, `check`, `legs` and `leg` by name
stem, none a mechanism for de-duplicating legs, so no existing seam fits beyond the function and the
arm shape named here. Recall returned `TOOL-aLiftedCeiling-1`, which raised the instruction-edits
ceiling to cover its wait on the tag index while the two legs race; this unit leaves that ceiling as
it is (§3), and AC5 measures what the wait becomes. `gotchas.py --for-paths` selected `vacuous-selector-empty-population`,
answered by G8's exactly-one-row liveness, and `a-grep-for-a-word-is-a-presence-probe`, answered by
AC1 calling the code rather than reading it.

Recall terms used: `python tools/memory-recall/query.py "instruction edits leg runs the tags check
inside itself" --terms "instructions_edit run_tag_check gov_tag tags leg instruction edits manifest
checks duplicate tag index ceiling"`
