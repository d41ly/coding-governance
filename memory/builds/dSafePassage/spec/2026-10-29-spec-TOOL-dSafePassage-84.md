# TOOL-dSafePassage-84 — the read-only preview reads the write run's walk predicate, so a receipt below schema 3 is previewed as not walked

**Status:** CLOSED · rev-3 · 2026-10-29 · node a · Tier-2 · base 460ffb58 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-29

**Derived:** TOOL-dSafePassage-78

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dSafePassage-84-ledger.md](../build/2026-10-29-build-TOOL-dSafePassage-84-ledger.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-84-1-spec-writer.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-1-spec-writer.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-84-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-build-brief.md) | journal | — |
| [2026-10-29-prompt-TOOL-dSafePassage-84-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-84-spec-brief.md) | research | — |
| [2026-10-29-review-TOOL-dSafePassage-84-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dSafePassage-84-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-78 made `govkit update --write` walk no step over a receipt below schema 3, and the
read-only preview of the same run still prints `would walk <id>` for every pending step. Two sites
answer one question two ways. This unit makes both read one predicate, defined once inside
`_cmd_update`, so for `--kits` and for a receipt below schema 3 the preview prints the write run's
`steps: not walked` line and the two cannot drift on those conditions again. The findings condition
stays the write run's alone, because the preview passes no findings (§8 F1).

## 2. Scope (IN)

- **S1** — One predicate. `_cmd_update` gains a nested `derive_walk_hold(findings)` that returns
  the reason this run walks no step forward, or `None` when it walks. It reads `kits` and `schema`
  from the enclosing scope (`schema` at `tools/govkit/govkit.py:9470`) and tests, in 78's order,
  `kits`, then `findings`, then `schema < 3`. Each reason is the text the write branch prints today
  (`govkit.py:11716-11721` at `460ffb587`), held once. The schema reason is worded so it is true
  from a read-only run as well, §4 "The schema reason". Observed by AC1, AC2 and AC5.
- **S2** — The preview reads it. The preview's `elif kits:` arm (`govkit.py:10603-10605` at
  `460ffb587`) becomes `elif _sw_hold := derive_walk_hold(0):`, printing
  `govkit update — steps: not walked — <reason> · <n> pending`. The `else` arm
  (`govkit.py:10606-10609`) is unchanged and is reached only when the predicate returns `None`, so
  `would walk <id>` prints only for a run the write path would walk, findings aside (§8 F1).
  Observed by AC2, AC3 and AC4.
- **S3** — The write run reads it. The walk branch's `elif kits or r.problems or schema < 3:` and
  its inline ternary (`govkit.py:11715-11721` at `460ffb587`) become
  `elif _sw_hold := derive_walk_hold(len(r.problems)):` with the same print as S2. The rollback arm
  above it (`:11712-11714`) and the walk below it (`:11722-11735`) do not move. This moves the guard
  TOOL-dSafePassage-2 S4 §8 F3 set, that a write run with a finding walks no step, into the
  predicate, so AC5 watches its findings branch. Observed by AC1, AC2 and AC5.
- **S4** — Two selftest checks in `check_receipt_schema` (`tools/govkit/selftest.py:4828`), §4
  "S4: the two checks". `[dSP-84 AC2]` adds a read-only `update` to the `rs-ac2` case
  (`:4906-4915`). `[dSP-84 AC5]` is a new case, `rs-84f`, a schema-4 receipt with one finding
  planted. Observed by AC7, and re-observed by §7's first two New arms.
- **S5** — The `scoped-read-only` plant. `tools/govkit/upgrade_steps.py`'s `UPDATE_PLANTS`
  (`:3627-3628`) and `run_update_fixture`'s read-only branch (`:4421-4433`) gain a plant that runs
  `--kits demo` without `--write`. The selftest's fixture table (`selftest.py:4520-4535`) gains its
  row, and the tagger (`:4541-4549`) tags it `dSP-84`. §4 "S5: the plant". Observed by AC3 and AC7,
  and re-observed by §7's third New arm.
- **S6** — The page. The read-only bullet of `help/upgrade-steps.md` narrows its lead sentence
  (`:228-229`) and gains two sentences after 78's (`:233-234`), §4 "The page". Observed by AC6.

## 3. Non-goals (OUT)

- The findings arm in the preview. Whether the preview passes its own finding count is §8 F1,
  resolved to A: the preview passes `0`. The write site's findings branch is in scope and AC5
  observes it.
- The source-mode preview (`govkit.py:9432-9437`). Its write run builds the receipt at
  `RECEIPT_SCHEMA` (`:9444-9446`) and takes no `--kits` (`:9418-9420`), so no hold applies there.
- The rollback arms of both sites. The preview lists the reverse set (`:10599-10602`) and the write
  run prints its own line (`:11712-11714`); neither is a forward walk held.
- Any change to when the receipt is lifted to 3. That is 78's S2 and the stamp's (`:12735-12742`).
- A below-3 option for `build_update_gov`. The schema-2 case is S4's `[dSP-84 AC2]` check.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-78, whose walk condition and
reason text S1 holds once; TOOL-dSafePassage-2, whose S4 wrote the preview block and whose §8 F3 set
the findings hold S3 moves; TOOL-dSafePassage-4, whose rollback arms stay. The edge join counts
CLOSED specs, and a CLOSED spec cannot take the matching line. The order against
TOOL-dSafePassage-81 is a sequence, not an edge, and §4 "Rollout" states it.

## 4. Design

### The two sites, at `460ffb587`

`tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/govkit/upgrade_steps.py` and
`help/upgrade-steps.md` are byte-identical at `460ffb587` and at the writing head `ec870d637`, so
every line cited here holds at both.

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

    DEFINED ONCE AND CALLED TWICE, by the read-only preview and by the write run's walk branch, so
    the preview cannot list a step the write run would not walk for `--kits` or for the schema. The
    preview passes no findings (TOOL-dSafePassage-84 §8 F1), so a write run's findings hold is its
    own."""
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
gains: the condition is `derive_walk_hold`'s, which the preview reads too, with no findings.

### The schema reason

78's text reads "this run lifts it to 3, and the next `update --write` walks them". Printed by a
read-only run, followed by `read-only. NOTHING was written` (`:10610`), "this run" is false. The held
text reads "a clean `update --write` lifts it to 3, and the next one walks them", true from both
sites. It keeps the prefix `the receipt is at schema <n>` that 78's AC2 reads.
`git grep -n "this run lifts it" -- tools help skills WIRE-INTO-PROJECT.md` printed only
`govkit.py:11720` at writing time, so no other reader holds the old words.

### S4: the two checks

`_steps` is defined once at the head of the two checks:

```python
_steps = lambda q: [ln for ln in q.stdout.splitlines() if ln.startswith("govkit update — steps:")]
```

**`[dSP-84 AC2]`.** In the `rs-ac2` case, between `plant(t, cut)` (`selftest.py:4908`) and the
`--write` run (`:4909`), `pv = run("update", "--target", str(t))`. After the two `[dSP-3 AC2]`
checks (`:4911-4915`):

```python
check("[dSP-84 AC2] the read-only run over the schema-2 receipt prints the write run's `steps:` line "
      "and lists no `would walk`",
      pv.returncode == 0 and "would walk" not in pv.stdout and _steps(pv) == _steps(p)
      and any("the receipt is at schema 2" in ln for ln in _steps(p)),
      f"{_steps(pv)} != {_steps(p)}")
```

A read-only run writes nothing, so the two `[dSP-3 AC2]` checks read the same receipt as today.

**`[dSP-84 AC5]`.** A new case after it. The planted finding is the unknown-role refusal at
`govkit.py:10005-10009`: it records a finding, holds the row and continues, and nothing between it
and the walk branch returns on a finding, so the run reaches `:11715` with one finding over a
receipt at schema 4. The receipt `apply` writes is at 4 with `"steps": []` (the `[dSP-3 AC4]` check,
`selftest.py:4877-4879`).

```python
t, _p = installed("rs-84f")
plant(t, lambda rec: next(f for f in rec["files"] if f.get("role", "engine") == "engine")
      .update(role="gk-unknown-role"))
p = run("update", "--target", str(t), "--write")
check("[dSP-84 AC5] a write run over a schema-4 receipt that already has a finding walks no step "
      "and names the finding",
      p.returncode == 1 and read(t).get("steps") == []
      and any("steps: not walked — this run already has 1 finding(s)" in ln for ln in _steps(p)),
      f"{_steps(p)} · {read(t).get('steps')}")
```

The `run` helper threads the suite's pin as `--to` (`selftest.py:226-228`), so the pending count
may differ from the probe's. The line assertion does not read it: with the write site passing `0`,
the predicate returns `None` at schema 4 and the run prints `steps: <n> pending · …`, which the
check refuses whatever `<n>` is.

### S5: the plant

`UPDATE_PLANTS` gains `"scoped-read-only"` after `"scoped"`. The fixture usage line derives from the
tuple (`upgrade_steps.py:5174`), so it needs no edit. The branch at `:4421` widens to the three
plants and passes `--kits demo` alone for the new one:

```python
elif plant in ("read-only", "scoped", "scoped-read-only"):
    rc, out = govkit("update", "--target", str(t), "--to", sha_b,
                     *(("--kits", "demo", "--write") if plant == "scoped"
                       else ("--kits", "demo") if plant == "scoped-read-only" else ()))
```

The `scoped` expectation (`:4431-4432`) then holds for both scoped plants, and one line follows it:

```python
expect(plant == "scoped" or "would walk" not in out, "the scoped read-only run prints `would walk`")
```

The table at `selftest.py:4520-4535` gains
`("update", "scoped-read-only", 0, ("govkit update — steps: not walked — a --kits run walks no step", "update: step canaries none"))`,
and the tagger gains `else "dSP-84" if plant == "scoped-read-only"`. The walking case stays with the
gated `read-only` plant (`upgrade_steps.py:4426-4429`, table row `selftest.py:4521`). The fixture's
receipt is at schema 4 and `build_update_gov` has no below-3 option, so the schema-2 case stays with
`[dSP-84 AC2]`.

### The page

In `help/upgrade-steps.md`, the lead sentence of the read-only bullet (`:228-229`) reads, with
`for each pending step a write run would walk` kept on one source line:

> Without `--write`, `update` prints `would walk <id>` for each pending step a write run would walk
> and runs none of them, witnesses included.

Appended to 78's sentence at `:233-234`:

> A read-only run over such a receipt with no finding prints the same `steps: not walked` line, and
> no `would walk`. A read-only run does not weigh its own findings, so with a finding it still lists
> the steps a clean write run would walk.

### The probes

Each runs from the root of a `git clone --shared` of the build head in a short directory under the
temp root, from a file written to the scratchpad, and loads no `tools/govkit/selftest.py`.

The preview probe, for AC2 and AC4: `python <scratch>/preview_probe.py <schema>`. It installs
`check-wiring` into a scratch target, plants the receipt at `<schema>` with no `steps`, commits,
runs a read-only `update` and then `update --write`, and prints the preview's exit, whether the
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

The findings probe, for AC5: `python <scratch>/findings_probe.py`. It installs `check-wiring` at
schema 4, gives one engine row the role `gk-unknown-role`, commits, runs `update --write`, and
prints the exit, the receipt's schema and `steps`, then the run's `steps:` line.

```python
import json, pathlib, subprocess, sys, tempfile
sys.path.insert(0, "tools/govkit")
from fixture_target import build_target
gk = pathlib.Path("tools/govkit/govkit.py").resolve()
deploy = ('gov_source = "local"\nprefix = "tools"\nkits = ["memory-tree"]\n\n[answers]\nmemory_root = "memory"\n'
          'playbook_path = "docs/PARALLEL.md"\nplaybook_dir = "docs"\nmanifest_path = "docs/SESSION-KICKOFF.md"\n'
          'user_skills = "~/.claude/skills"\n')
t = build_target(pathlib.Path(tempfile.mkdtemp(prefix="p84f-")), deploy)
go = lambda *a: subprocess.run([sys.executable, str(gk), *a], capture_output=True, text=True, encoding="utf-8")
def commit(msg):
    subprocess.run(["git", "-C", str(t), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(t), "commit", "-qm", msg], check=True)
assert go("apply", "--target", str(t), "--kits", "check-wiring").returncode == 0
commit("install")
rp = t / ".governance/install.json"
rec = json.loads(rp.read_text(encoding="utf-8"))
next(f for f in rec["files"] if f.get("role", "engine") == "engine")["role"] = "gk-unknown-role"
rp.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
commit("an unknown role")
p = go("update", "--target", str(t), "--write")
rec = json.loads(rp.read_text(encoding="utf-8"))
print(p.returncode, rec.get("schema"), rec.get("steps"))
print([ln for ln in p.stdout.splitlines() if ln.startswith("govkit update — steps:")])
```

### Measured at writing time

In a `git clone --shared` of `ec870d637` under the temp root, 2026-10-29.

| Observation | At the head | S1 to S3 staged | Staged break |
|---|---|---|---|
| preview probe at `2` | `0 True True False`, `steps: 3 pending` | `0 True False True`, the schema not-walked line, `3 pending` | — |
| preview probe at `3` | `0 True True False` | `0 True True False` | — |
| findings probe | `1 4 []`, `not walked — this run already has 1 finding(s) · 3 pending` | the same | write site passing `0`: `1 4 [...]` with three `applied` rows, `steps: 3 pending · 0 applied · 3 skipped` |
| `scoped-read-only` plant, S5 staged | exit 0, the `--kits` not-walked line | exit 0, the same | preview arm `elif (_sw_hold := derive_walk_hold(0)) and not kits:`: exit 1, two `would walk` lines, two `update: FAILED` lines |
| `read-only` and `scoped` plants, S5 staged | — | each exit 0, no `FAILED` | — |

The findings probe and the `scoped-read-only` plant are green at the head by design: each watches
behaviour S1 to S3 move into the predicate and must keep, so their reds are the staged breaks in the
last column, not the head. The preview probe at `2` is the one observation red at the head.

### Inventory

Minted: the nested function `derive_walk_hold` inside `_cmd_update`.
`python tools/lexicon/lexicon.py --suggest derive_walk_hold --as py.function` answered OK on
2026-10-29, leading with the declared verb `derive`. It is not top-level, so
`memory/map/generated/symbols.json` does not move: the nested `derive_unclaimed_candidates` is absent
from it while the top-level `demand_forward_vintage` is present, read at writing time. Also minted:
the plant `scoped-read-only`, the selftest case `rs-84f`, and the arm tags `[dSP-84 AC2]`,
`[dSP-84 AC5]` and `dSP-84`. No `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None. No stored shape changes.

### Rollout

Live at landing, at order 16. TOOL-dSafePassage-61 holds order 16 and stays DEFERRED, so the order
is not closed by this unit. This unit builds before TOOL-dSafePassage-81, which renames last of
order 16 so its renames see every sibling's names (81's §4 "Rollout"). `derive_walk_hold` leads with
a declared verb, so it adds no verb offender for 81 to rename and moves no lexicon pin. Siblings of
order 16 that write the files below are sequenced by order of dispatch (M6); the builder re-reads
each cited line by content before editing.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/upgrade_steps.py`
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
- **A scratch probe as the only watch on the read-only `--kits` hold.** No gate would hold it after
  landing; S5's plant extends the gated `update` fixture family instead.

## 5. Production-readiness checklist

- security: no new write path, spawn or surface. The preview still spawns nothing.
- perf / scale: none at runtime. The `govkit selftest` leg gains one read-only `update`, one
  install and `update --write`, and one fixture run, under a minute together.
- error / empty / loading states: a read-only run over a receipt below 3 prints the not-walked line
  with the pending count in place of `would walk` lines.
- observability: the preview names why no step would walk, in the write run's words.
- risks: the schema reason's wording moves on the write run too; nothing reads the old words. A
  read-only run with a finding still lists steps, by §8 F1, and the page says so.
- testing: §7's three New arms, AC1's greps, §4's two probes and two fixture plants.
- migration: none.
- user docs: S6's lead sentence and two sentences.

## 6. Acceptance criteria

- **AC1** — When `git grep -n -F "derive_walk_hold(" -- tools/govkit/govkit.py` runs, it prints
  three lines, the definition and one call in each of the two sites;
  `git grep -n -F "elif kits" -- tools/govkit/govkit.py` prints nothing; and
  `git grep -h -c -F "a --kits run walks no step" -- tools/govkit/govkit.py` prints `1`.
  Red when: either site keeps its own condition, so the second grep prints the preview's `elif kits:`
  or the write branch's `elif kits or r.problems or schema < 3:`, and the third prints `2`, as at
  `460ffb587`.
- **AC2** — When §4's preview probe runs as `python <scratch>/preview_probe.py 2`, it prints
  `0 True False True` and a line holding `steps: not walked — the receipt is at schema 2`.
  Red when: the preview lists the pending steps over the schema-2 receipt, so it prints
  `0 True True False`, as at `460ffb587`.
  cost: one install and two `update` runs, under a minute.
  fixture: a `git clone --shared` of the build head under the temp root.
- **AC3** — When `python tools/govkit/upgrade_steps.py fixture update --plant scoped-read-only`
  runs, it exits 0, prints `govkit update — steps: not walked — a --kits run walks no step` ending
  `· 2 pending`, and prints no `would walk` and no `update: FAILED`.
  Red when: a preview arm sits ahead of the predicate with no `--kits` hold, so the run prints
  `would walk fx/s1` and exits 1 with an `update: FAILED` line naming the scoped read-only run.
  The `--kits` behaviour is green at `460ffb587`, where the preview's own `elif kits:` holds it, so
  this criterion guards the hold after the move; AC1 is what is red at the base for the `--kits`
  site.
  cost: one scratch gov and one `update`, under a minute.
- **AC4** — When the preview probe runs as `python <scratch>/preview_probe.py 3`, it prints
  `0 True True False`; and `python tools/govkit/upgrade_steps.py fixture update --plant read-only`
  exits 0 printing `would walk fx/s1` and `would walk fx/s2`.
  Red when: the predicate holds a receipt at schema 3 or above, so the probe prints
  `0 True False True` and the fixture's `would walk` lines are absent.
  cost: one install and two `update` runs, plus the fixture, under two minutes.
  fixture: the same clone.
- **AC5** — When §4's findings probe runs as `python <scratch>/findings_probe.py`, it prints
  `1 4 []` and a line holding `steps: not walked — this run already has 1 finding(s)`.
  Red when: the write site passes `0`, or the predicate skips `findings`, so the walk runs over the
  run's finding and the probe prints `applied` step rows and a `steps: <n> pending · …` line. Green
  at `460ffb587` by design: this observes the moved guard, and its red is that staged break.
  cost: one install and one `update --write`, under a minute.
  fixture: the same clone.
  figure: the count `1` is PINNED, measured at `ec870d637`; the probe plants one finding.
- **AC6** — When `git grep -n -F "for each pending step a write run would walk" -- help/upgrade-steps.md`,
  `git grep -n -F "A read-only run over such a receipt with no finding prints the same" -- help/upgrade-steps.md`
  and `git grep -n -F "A read-only run does not weigh its own findings" -- help/upgrade-steps.md`
  run, each prints one line, in the read-only bullet.
  Red when: the bullet's lead still says a read-only run prints `would walk <id>` for each pending
  step without exception, so the first grep prints nothing.
- **AC7** — When `git grep -n -F "[dSP-84 AC" -- tools/govkit/selftest.py` runs, it prints two
  lines, both inside `check_receipt_schema`; and
  `git grep -n -F "scoped-read-only" -- tools/govkit/upgrade_steps.py tools/govkit/selftest.py`
  prints at least one line in each file.
  Red when: either check or the plant is absent, so a grep prints nothing for it.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 · the `[dSP-84 AC2]` check of `check_receipt_schema`'s `rs-ac2` case, staged red by a `tools/govkit/govkit.py` at `460ffb587`, whose preview lists `would walk` over the schema-2 receipt · none
New arm: tools/govkit/selftest.py · covers AC5 · the `[dSP-84 AC5]` check of `check_receipt_schema`'s `rs-84f` case, staged red by a `tools/govkit/govkit.py` whose write site calls `derive_walk_hold(0)`, which then walks the steps over the run's finding · none
New arm: tools/govkit/upgrade_steps.py · covers AC3 · the `update` family's `scoped-read-only` plant, run by its `dSP-84` row in the selftest's fixture table; staged red by a preview arm `elif (_sw_hold := derive_walk_hold(0)) and not kits:`, which prints `would walk` for the `--kits` run · none

AC1, AC6 and AC7 are greps, and AC2, AC4 and AC5 are the probes and a fixture. No floor moves. No
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
- rev-3 · 2026-10-29 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · S1 · S2 · S3 · S4 · S5 · S6 · AC1 ·
  AC2 · AC3 · AC4 · AC5 · AC6 · AC7 · folded the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-84-spec-audit-round1.md`,
  at the fixes its skeptic judged sound, its corrected fix where it rejected the finder's. M1 (id
  1): the new `[dSP-84 AC5]` check and AC5 watch the moved findings hold, staged red by the write
  site passing `0`. L1 (ids 2, 8): AC1's count grep is `git grep -h -c`, a bare count. L2 (ids 3,
  7): S6 narrows the bullet's lead sentence and AC6 greps it. L3 (id 4): AC2's `--kits` clause is
  gone; AC3 states that the `--kits` hold is green at the base and that AC1 is red there. L4 (id
  5): S5's gated `scoped-read-only` plant takes the place of the `--kits` probe run, with
  `run_update_fixture` named in §10 and `tools/govkit/upgrade_steps.py` in the files touched. L5
  (id 9): §1, the docstring and the page sentence say what §8 F1-A delivers, and the page says a
  read-only run does not weigh its findings. Each new observation was measured red on its staged
  break and green otherwise in a clone of `ec870d637`. The old S4 splits into S4 and S5, and the old
  S5 is S6; the old AC3 to AC5 are AC4, AC6 and AC7.

## 10. Reuse audit

S1 extends the pattern `_cmd_update` already uses for the same defect class: the nested
`derive_unclaimed_candidates` (`tools/govkit/govkit.py:10492`), defined once and called by the
read-only preview (`:10587`) and by the write path (`:10650`) so the preview cannot drift. S2 and S3
keep the `_sw_pending` both sites derive through `upgrade_steps.derive_pending_steps`. S4 extends
`check_receipt_schema`'s `installed`, `plant` and `read` helpers and the suite's `run` helper
(`tools/govkit/selftest.py:221`). S5 extends the gated `update` fixture family, `run_update_fixture`
(`tools/govkit/upgrade_steps.py:4369`), whose `read-only` and `scoped` plants already share the
branch S5 widens, and the selftest's fixture table that runs it. The probes build their targets
through `build_target` (`tools/govkit/fixture_target.py`), the factory the selftest uses.
`python tools/codebase-map/reuse_lookup.py "one predicate the read-only preview and the write run of update share to decide whether the upgrade-step walk is held"`
ranked name-stem seams only, `read_text`, `read`, `run`, `write`, `walk`, `step` and `read_steps`;
none decides whether a walk is held, so no further seam fits beyond the nested-helper pattern and the
fixture family named above. The recall probe ranked TOOL-dSafePassage-78's spec, this unit's brief,
TOOL-dSafePassage-62, TOOL-dSafePassage-15, TOOL-dSafePassage-2's S4 (the preview block's origin)
and TOOL-dRetiredFork-38, a `--kits` update re-stamping the whole receipt, which this unit does not
change.

Recall terms used: `python tools/memory-recall/query.py "why does the read-only update preview list would walk for a receipt the write run does not walk" --terms "preview read-only would walk not walked schema 3 receipt drift one implementation two calls derive_unclaimed_candidates"`
