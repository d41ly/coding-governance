# TOOL-dSafePassage-84 — the read-only preview reads the write run's walk predicate, so a receipt below schema 3 is previewed as not walked

**Status:** DEFERRED · rev-2 · 2026-10-29 · node a · Tier-2 · base 460ffb58 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-29

**Derived:** TOOL-dSafePassage-78

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-84-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-84-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-build-brief.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-84-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-78 made `govkit update --write` walk no step over a receipt below schema 3, and the
read-only preview of the same run still prints `would walk <id>` for every pending step. Two sites
answer one question two ways. This unit makes both read one predicate, defined once inside
`_cmd_update`, so the preview prints the write run's `steps: not walked` line and the two cannot
drift again.

## 2. Scope (IN)

- **S1** — One predicate. `_cmd_update` gains a nested `derive_walk_hold(findings)` that returns
  the reason this run walks no step forward, or `None` when it walks. It reads `kits` and `schema`
  from the enclosing scope (`schema` at `tools/govkit/govkit.py:9470`) and tests, in 78's order,
  `kits`, then `findings`, then `schema < 3`. Each reason is the text the write branch prints today
  (`govkit.py:11716-11721` at `460ffb587`), held once. The schema reason is worded so it is true
  from a read-only run as well, §4 "The schema reason". Observed by AC1 and AC2.
- **S2** — The preview reads it. The preview's `elif kits:` arm (`govkit.py:10603-10605` at
  `460ffb587`) becomes `elif _sw_hold := derive_walk_hold(0):`, printing
  `govkit update — steps: not walked — <reason> · <n> pending`. The `else` arm
  (`govkit.py:10606-10609`) is unchanged and is reached only when the predicate returns `None`, so
  `would walk <id>` prints only for a run the write path would walk. Observed by AC2 and AC3.
- **S3** — The write run reads it. The walk branch's `elif kits or r.problems or schema < 3:` and
  its inline ternary (`govkit.py:11715-11721` at `460ffb587`) become
  `elif _sw_hold := derive_walk_hold(len(r.problems)):` with the same print as S2. The rollback arm
  above it (`:11712-11714`) and the walk below it (`:11722-11735`) do not move. Observed by AC1 and
  AC2.
- **S4** — The arm. In `check_receipt_schema` (`tools/govkit/selftest.py:4828`), the `rs-ac2` case
  (`:4906-4915`) runs a read-only `update` after `plant(t, cut)` and before its `--write`, and one
  new check, labelled `[dSP-84 AC2]`, asserts the read-only run exits 0, prints no `would walk`,
  and prints the same `govkit update — steps:` line as the write run, a line naming schema 2.
  Observed by AC5, and re-observed by §7's New arm.
- **S5** — The page. The sentence 78 appended to the read-only bullet of `help/upgrade-steps.md`
  (`:233-234`) gains one sentence, §4 "The page". Observed by AC4.

## 3. Non-goals (OUT)

- The findings arm in the preview. Whether the preview passes its own finding count is §8 F1,
  resolved to A: the preview passes `0`.
- The source-mode preview (`govkit.py:9432-9437`). Its write run builds the receipt at
  `RECEIPT_SCHEMA` (`:9444-9446`) and takes no `--kits` (`:9418-9420`), so no hold applies there.
- The rollback arms of both sites. The preview lists the reverse set (`:10599-10602`) and the write
  run prints its own line (`:11712-11714`); neither is a forward walk held.
- Any change to when the receipt is lifted to 3. That is 78's S2 and the stamp's (`:12735-12742`).

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-78, whose walk condition and
reason text S1 holds once; TOOL-dSafePassage-2, whose S4 wrote the preview block; TOOL-dSafePassage-4,
whose rollback arms stay. The edge join counts CLOSED specs, and a CLOSED spec cannot take the
matching line. The order against TOOL-dSafePassage-81 is a sequence, not an edge, and §4 "Rollout"
states it.

## 4. Design

### The two sites, at `460ffb587`

`tools/govkit/govkit.py` is byte-identical at `460ffb587` and at the writing head `ec870d637`
(`git diff --stat 460ffb587 ec870d637 -- tools/govkit/govkit.py tools/govkit/selftest.py help/upgrade-steps.md`
prints nothing), so every line cited here holds at both.

| Site | Lines | What it tests | What it prints when held |
|---|---|---|---|
| the read-only preview, inside `if not write:` (`:10586`) | `:10603-10609` | `kits` only | the `--kits` reason, else `would walk <id>` per pending step |
| the write run's walk branch | `:11715-11721` | `kits or r.problems or schema < 3` | the `--kits`, findings or schema reason |

Both sites already derive `_sw_pending` the same way (`:10598` and `:11711`), so the pending count
needs no change.

### S1: the predicate

Defined directly above the preview's banner comment (`:10573`), after
`derive_unclaimed_candidates` (`:10492`), whose docstring states the same contract: defined once and
called by the preview and by the write path, so the preview cannot drift from what the write does.

```python
def derive_walk_hold(findings: int) -> str | None:
    """Why this run walks no step forward, or None when it walks. TOOL-dSafePassage-84.

    DEFINED ONCE AND CALLED TWICE, by the read-only preview and by the write run's walk branch,
    so the preview cannot list a step the write run would not walk."""
    if kits:
        return "a --kits run walks no step, since a subset would run a later step before an earlier one"
    if findings:
        return f"this run already has {findings} finding(s)"
    if schema < 3:
        return (f"the receipt is at schema {schema}, and its first step starts from 3: a clean "
                "`update --write` lifts it to 3, and the next one walks them")
    return None
```

The builder may wrap the strings to the line-length limit. The phrase `a --kits run walks no step`
stays on one source line, because AC1 counts it.

### S2 and S3: the two calls

Preview, in place of `:10603-10605`:

```python
elif _sw_hold := derive_walk_hold(0):
    print(f"govkit update — steps: not walked — {_sw_hold} · {len(_sw_pending)} pending")
```

The `0` is §8 F1's resolution, with a `ponytail:` comment saying the preview's findings are not
the write run's at the walk, so it passes none. Write run, in place of `:11715-11721`:

```python
elif _sw_hold := derive_walk_hold(len(r.problems)):
    print(f"govkit update — steps: not walked — {_sw_hold} · {len(_sw_pending)} pending")
```

The comment above the walk (`:11702-11710`) keeps its two sentences on the schema condition and
gains: the condition is `derive_walk_hold`'s, which the preview reads too.

### The schema reason

78's text reads "this run lifts it to 3, and the next `update --write` walks them". Printed by a
read-only run, followed by `read-only. NOTHING was written` (`:10610`), "this run" is false. The held
text reads "a clean `update --write` lifts it to 3, and the next one walks them", true from both
sites. It keeps the prefix `the receipt is at schema <n>` that 78's AC2 reads.
`git grep -n "this run lifts it" -- tools help skills WIRE-INTO-PROJECT.md` printed only
`govkit.py:11720` at writing time, so no other reader holds the old words.

### S4: the arm

In `check_receipt_schema`, between `plant(t, cut)` (`selftest.py:4908`) and the `--write` run
(`:4909`), `pv = run("update", "--target", str(t))`. After the two `[dSP-3 AC2]` checks (`:4911-4915`):

```python
_steps = lambda q: [ln for ln in q.stdout.splitlines() if ln.startswith("govkit update — steps:")]
check("[dSP-84 AC2] the read-only run over the schema-2 receipt prints the write run's `steps:` line "
      "and lists no `would walk`",
      pv.returncode == 0 and "would walk" not in pv.stdout and _steps(pv) == _steps(p)
      and any("the receipt is at schema 2" in ln for ln in _steps(p)),
      f"{_steps(pv)} != {_steps(p)}")
```

A read-only run writes nothing, so the two `[dSP-3 AC2]` checks read the same receipt as today.

### The page

Appended to 78's sentence at `help/upgrade-steps.md:233-234`:

> A read-only run over such a receipt prints the same `steps: not walked` line, and no `would walk`.

### The probe

Runs from the root of a `git clone --shared` of the build head under the temp root, from a file
written to the scratchpad, and loads no `tools/govkit/selftest.py`:
`python <scratch>/preview_probe.py <schema> [update args...]`. It installs `check-wiring` into a
scratch target, plants the receipt at `<schema>` with no `steps`, commits, runs a read-only `update`
and then `update --write` with the extra arguments, and prints the preview's exit, whether the
receipt's bytes held, whether the preview printed any `would walk`, whether the two `steps:` lines
are equal, then the preview's `steps:` line.

```python
import json, pathlib, subprocess, sys, tempfile
sys.path.insert(0, "tools/govkit")
from fixture_target import build_target
schema, extra = int(sys.argv[1]), sys.argv[2:]
gk = pathlib.Path("tools/govkit/govkit.py").resolve()
deploy = ('gov_source = "local"\nprefix = "tools"\nkits = ["memory-tree"]\n\n[answers]\nmemory_root = "memory"\n'
          'playbook_path = "docs/PARALLEL.md"\nplaybook_dir = "docs"\nmanifest_path = "docs/SESSION-KICKOFF.md"\n'
          'user_skills = "~/.claude/skills"\n')
t = build_target(pathlib.Path(tempfile.mkdtemp(prefix="p84-")), deploy)
go = lambda *a: subprocess.run([sys.executable, str(gk), *a], capture_output=True, text=True, encoding="utf-8")
def commit(msg):
    subprocess.run(["git", "-C", str(t), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(t), "commit", "-qm", msg], check=True)
assert go("apply", "--target", str(t), "--kits", "check-wiring").returncode == 0
commit("install")
rp = t / ".governance/install.json"
rec = json.loads(rp.read_text(encoding="utf-8"))
rec["schema"] = schema
rec.pop("steps", None)
rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
commit(f"schema {schema}")
before = rp.read_bytes()
pv = go("update", "--target", str(t), *extra)
same = rp.read_bytes() == before
wr = go("update", "--target", str(t), "--write", *extra)
line = lambda q: [ln for ln in q.stdout.splitlines() if ln.startswith("govkit update — steps:")]
walks = sum("would walk" in ln for ln in pv.stdout.splitlines())
print(pv.returncode, same, walks > 0, line(pv) == line(wr))
print(line(pv))
```

### Measured at writing time

In a `git clone --shared` of `ec870d637` under the temp root, 2026-10-29. At the head, the probe at
`2` printed `0 True True False` and `['govkit update — steps: 3 pending']`, while the write run
printed the schema not-walked line: the two answers. At `3` it printed `0 True True False`. With S1
to S3 staged in the clone, the probe at `2` printed `0 True False True` and the not-walked line
naming schema 2 and `3 pending`; at `3`, `0 True True False`; at `2 --kits check-wiring`,
`0 True False True` and the `--kits` line. With S1 to S3 staged,
`python tools/govkit/upgrade_steps.py fixture update --plant read-only` and `--plant scoped` each
exited 0; that fixture's receipt is at schema 4, so its `would walk fx/s1` lines stand.

### Inventory

Minted: the nested function `derive_walk_hold` inside `_cmd_update`.
`python tools/lexicon/lexicon.py --suggest derive_walk_hold --as py.function` answered OK on
2026-10-29, leading with the declared verb `derive`. It is not top-level, so
`memory/map/generated/symbols.json` does not move: the nested `derive_unclaimed_candidates` is absent
from it while the top-level `demand_forward_vintage` is present, read at writing time. The arm tag
`[dSP-84 AC2]` is minted. No `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None. No stored shape changes.

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-61 holds order 16 and stays DEFERRED, so the order
is not closed by this unit. This unit builds before TOOL-dSafePassage-81, which renames last of
order 16 so its renames see every sibling's names (81's §4 "Rollout"). `derive_walk_hold` leads with
a declared verb, so it adds no verb offender for 81 to rename and moves no lexicon pin. Siblings of
order 16 that write `tools/govkit/govkit.py`, `tools/govkit/selftest.py` or `help/upgrade-steps.md`
are sequenced by order of dispatch (M6); the builder re-reads each cited line by content before
editing.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The preview tests `kits or schema < 3` inline, as the write run does.** It fixes today's case
  and keeps two conditions, which is how 78's change left the preview behind.
- **A top-level function.** Both callers are inside `_cmd_update` and read its locals, and a
  top-level name would move `memory/map/generated/symbols.json` for no second caller.
- **Two texts, one per site, so the preview can say "would not walk".** A second text is a second
  fact; the held text is worded true from both sites instead.
- **A predicate returning a boolean, with each site keeping its message.** The message is the half
  that drifted in wording; holding only the test leaves the text to drift.

## 5. Production-readiness checklist

- security: no new write path, spawn or surface. The preview still spawns nothing.
- perf / scale: none at runtime. The `rs-ac2` case gains one read-only `update`, a few seconds of the
  `govkit selftest` leg.
- error / empty / loading states: a read-only run over a receipt below 3 prints the not-walked line
  with the pending count in place of `would walk` lines.
- observability: the preview names why no step would walk, in the write run's words.
- risks: the schema reason's wording moves on the write run too; nothing reads the old words.
- testing: §7's New arm, AC1's greps, and §4's probe at three argument sets.
- migration: none.
- user docs: S5's sentence.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -F "derive_walk_hold(" -- tools/govkit/govkit.py` runs, it prints
  three lines, the definition and one call in each of the two sites;
  `git grep -n -F "elif kits" -- tools/govkit/govkit.py` prints nothing; and
  `git grep -c -F "a --kits run walks no step" -- tools/govkit/govkit.py` prints `1`.
  Red when: either site keeps its own condition, so the second grep prints the preview's `elif kits:`
  or the write branch's `elif kits or r.problems or schema < 3:`, and the third prints `2`.
- **AC2** — When §4's probe runs as `python <scratch>/preview_probe.py 2`, it prints
  `0 True False True` and a line holding `steps: not walked — the receipt is at schema 2`; and as
  `python <scratch>/preview_probe.py 2 --kits check-wiring` it prints `0 True False True` and a line
  holding `a --kits run walks no step`.
  Red when: the preview lists the pending steps over the schema-2 receipt, so the first run prints
  `0 True True False`, as at `460ffb587`.
  cost: two installs and four `update` runs, about a minute.
  fixture: a `git clone --shared` of the build head under the temp root.
- **AC3** — When the probe runs as `python <scratch>/preview_probe.py 3`, it prints
  `0 True True False`; and `python tools/govkit/upgrade_steps.py fixture update --plant read-only`
  exits 0 printing `would walk fx/s1` and `would walk fx/s2`.
  Red when: the predicate holds a receipt at schema 3 or above, so the probe prints
  `0 True False True` and the fixture's `would walk` lines are absent.
  cost: one install and two `update` runs, plus the fixture, under two minutes.
  fixture: the same clone.
- **AC4** — When `git grep -n -F "A read-only run over such a receipt prints the same" -- help/upgrade-steps.md`
  runs, it prints one line, in the read-only bullet after 78's sentence.
  Red when: the page still says only that a read-only run prints `would walk <id>` for each pending
  step.
- **AC5** — When `git grep -n -F "[dSP-84 AC2]" -- tools/govkit/selftest.py` runs, it prints one
  line, inside `check_receipt_schema`'s `rs-ac2` case.
  Red when: the case runs no read-only `update`, so the grep prints nothing.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 · the `[dSP-84 AC2]` check of `check_receipt_schema`'s `rs-ac2` case, staged red by a `tools/govkit/govkit.py` at `460ffb587`, whose preview lists `would walk` over the schema-2 receipt · none

AC1, AC4 and AC5 are greps, and AC2 and AC3 are the probe and a fixture. No floor moves. No
`Refusal` site is added, so `tools/govkit/refusal_join.py`'s count does not move.

## 8. Open questions

- **F1 — Does the preview pass its own finding count to `derive_walk_hold`?**
  - **A, pass `0` (recommended).** The preview answers as the write run for `--kits` and for a
    receipt below 3, the brief's scope, and keeps `would walk` when it already has a finding. The
    preview's findings at `:10586` are not the write run's at `:11715`: the write path's
    preconditions and write loop sit between, and whether every read-only finding is also a write
    run's finding was not verified. So a count printed there would claim a number the write run may
    not print.
  - **B, pass `len(r.problems)`.** One predicate with the same inputs at both sites, so a preview
    that already has a finding prints `not walked — this run already has <n> finding(s)`. It errs
    safe, since `Report.problems` only grows (`govkit.py:1387-1388`), but it widens the change past
    the schema case and the page's "A write run that already has a finding" sentence (`:230-232`)
    would need a read-only clause.
  - Recommendation: A. B is a one-argument change a later unit can take with its page clause.
  - RESOLVED (agent, 2026-10-29, delegated): A, the preview passes `0`.

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-84-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-84-spec-brief.md`.
  The two answers were reproduced at `ec870d637`, byte-identical to `460ffb587` on the three files,
  and S1 to S3 were staged and measured in a `git clone --shared` under the temp root (§4
  "Measured at writing time").
- rev-2 · 2026-10-29 · header · §3 · §4 · §8 · S2 · F1 resolved by the coordinator under the
  delegated mandate to option A, the preview passes `0`; the header carries `ratified 2026-10-29`,
  and §3 and §4 cite the resolution in place of the recommendation.

## 10. Reuse audit

S1 extends the pattern `_cmd_update` already uses for the same defect class: the nested
`derive_unclaimed_candidates` (`tools/govkit/govkit.py:10492`), defined once and called by the
read-only preview (`:10587`) and by the write path (`:10650`) so the preview cannot drift. S2 and S3
keep the `_sw_pending` both sites derive through `upgrade_steps.derive_pending_steps`. S4 extends the
`rs-ac2` case of `check_receipt_schema` and its `run` helper (`tools/govkit/selftest.py:221`), and
the probe builds its target through `build_target` (`tools/govkit/fixture_target.py`), the factory
the selftest uses. `python tools/codebase-map/reuse_lookup.py "one predicate the read-only preview and the write run of update share to decide whether the upgrade-step walk is held"`
ranked name-stem seams only, `read_text`, `read`, `run`, `write`, `walk`, `step` and `read_steps`;
none decides whether a walk is held, so no further seam fits beyond the nested-helper pattern named
above. The recall probe ranked TOOL-dSafePassage-78's spec, this unit's brief, TOOL-dSafePassage-62,
TOOL-dSafePassage-15, TOOL-dSafePassage-2's S4 (the preview block's origin) and TOOL-dRetiredFork-38,
a `--kits` update re-stamping the whole receipt, which this unit does not change.

Recall terms used: `python tools/memory-recall/query.py "why does the read-only update preview list would walk for a receipt the write run does not walk" --terms "preview read-only would walk not walked schema 3 receipt drift one implementation two calls derive_unclaimed_candidates"`
