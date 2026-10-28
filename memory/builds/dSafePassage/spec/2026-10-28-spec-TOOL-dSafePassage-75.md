# TOOL-dSafePassage-75 — the step environment keeps `GOV_PYTHON`, so the floor step resolves the interpreter every gate and hook resolves

**Status:** CLOSED · rev-3 · 2026-10-28 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dSafePassage-75-ledger.md](../build/2026-10-28-build-TOOL-dSafePassage-75-ledger.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md) | research | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 |
| [2026-10-28-prompt-TOOL-dSafePassage-75-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-75-build-brief.md) | journal | — |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

`STEP_ENV_KEEP` (`tools/govkit/upgrade_steps.py:170-171`) leaves out `GOV_PYTHON`, so
`build_step_env` (`:1364`) strips it. The `lib/python-floor-3.15` row runs
`bash {gov}/lib/python-floor.sh preflight` as its up and witness (`tools/govkit/steps.toml:33-36`),
and `resolve_python` tries `GOV_PYTHON` before `python3`, `python` and `py`
(`tools/lib/resolve-python.sh:36`). On a node whose launchers on `PATH` run below 3.15 and whose
`GOV_PYTHON` names 3.15, the setup `help/python-floor.md:46-48` documents as the remedy, every gate
passes and the floor step refuses: `update --write` stops, `update --rollback` stops at its down, and
push-main's `check_gov_first` re-run fails, so every landing from that node aborts. This unit closes
H5 (id 9) and M2 (id 5) of the closing diff review, round 1, one defect: the name joins the keep
list, and the help page's clean-environment list names it.

## 2. Scope (IN)

- **S1** — The keep list. `STEP_ENV_KEEP` gains `"GOV_PYTHON"`, and the comment above it
  (`tools/govkit/upgrade_steps.py:167-169`) says why: it names the interpreter the resolver tries
  first, it carries no credential, and it is the same class of name as `PATH`, which already decides
  what a step spawns. Observed by AC1 and AC2.
- **S2** — The help. `help/upgrade-steps.md`'s "A clean environment" bullet (lines 39-41) names
  `GOV_PYTHON` among the names copied in, as the interpreter override the resolver reads, so a step
  resolves the interpreter gov's gates and hooks resolve on the same node. Observed by AC3.
- **S3** — The arm. `check_step_isolation` (`tools/govkit/selftest.py:3505`) gains a `[dSP-75]`
  check. It writes fake `python3`, `python` and `py` launchers that report 3.12, shaped as
  `write_fake_launcher` in `tools/lib/resolve-python.test.sh:181-183`, puts their directory first on
  the parent's `PATH`, sets `GOV_PYTHON` to `sys.executable`, and runs the floor row's witness
  through `run_step_isolated` on gov's own tree. The verdict must be `ok`. Observed by AC2.

## 3. Non-goals (OUT)

- Passing the runner's own interpreter as the step's `GOV_PYTHON`. The review offers it as an
  alternative; §4 rejects it.
- A checklist row that every override a step program's resolver reads is on the keep list. It
  belongs to the project's bug-class checklist, not to this unit.
- `help/python-floor.md`. It already documents `GOV_PYTHON` as the override every consumer spawns,
  and this unit makes the step one of them.
- M5 (id 10), the floor down's default `<to>`, batched into TOOL-dSafePassage-76.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-7's isolation contract and its
allowlist; TOOL-dSafePassage-11's floor step and `python-floor.sh`; TOOL-dSafePassage-23's resolver,
which keeps an override's own name; and TOOL-dSafePassage-8's `check_gov_first`, the lander's re-run
of the witness. The edge join counts CLOSED specs, and a CLOSED spec cannot take the matching
`hands-off` line.

## 4. Design

### Observed at base

A scratchpad probe on node a on 2026-10-28, at `83817478`, wrote three fake launchers reporting
`3.12`, put them first on `PATH`, set `GOV_PYTHON` to a Python 3.15 executable, and ran the floor
row's witness through `run_step_isolated(row, "witness", <gov>, <gov>)`.

| Keep list | `GOV_PYTHON` in `build_step_env`'s result | Verdict | Last stderr line |
|---|---|---|---|
| base | absent | `failed`, rc 1 | `resolve_python: tried: python3 python py` |
| base plus `GOV_PYTHON`, set in the probe's process | present | `ok`, rc 0 | none |

The second row shows the one name is all the step needs: nothing else in `python-floor.sh`'s
preflight reads a name the contract strips.

### Why the name and not the runner's interpreter

The floor step's witness asks whether this node's resolver finds an interpreter at the floor,
because that is what every gate and hook will spawn. Keeping the parent's `GOV_PYTHON` asks exactly
that. Exporting govkit's own `sys.executable` as `GOV_PYTHON` would ask instead whether govkit's
interpreter is at the floor. On a node where govkit was started with an explicit 3.15 path but the
resolver finds only 3.12, every gate would fail while the witness held.

### The isolation check follows

The isolation fixture's allowlist is derived from `STEP_ENV_KEEP` (`tools/govkit/upgrade_steps.py:2800`),
so `GOV_PYTHON` reaching a step reads as allowed with no second edit. No credential name joins: the
value is a command name or path, as `PATH`'s entries are.

### Inventory

Minted: the arm tag `[dSP-75]`. One string joins the existing `STEP_ENV_KEEP` tuple. No function,
`Refusal` site, conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, in order 16 with TOOL-dSafePassage-72, -73 and -74, sequenced by M6 because all
four write `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Export `GOV_PYTHON=<sys.executable>` in `build_step_env`.** It answers about govkit's
  interpreter, not the node's resolver, as above, and it would set the name on nodes where the
  operator never did.
- **Have the floor row's argv name `{python}`.** No such placeholder exists, and the floor's own
  preflight is the program that must run the resolver as gates do.

## 5. Production-readiness checklist

- security: one name joins the isolation contract's allowlist. It names an interpreter, which a step
  already reaches through `PATH`, and carries no credential. A step running gov's own programs
  resolves the interpreter the operator chose.
- perf / scale: none.
- error / empty / loading states: an unset `GOV_PYTHON` is not copied, as today, and the resolver
  falls through to the launcher names. A set and unusable one is the resolver's own named refusal
  (`tools/push-main.sh:685-688` carries the inline copy of that text).
- observability: the floor step's failure tail is the resolver's own list of what it tried, which
  now includes the override.
- risks: a node whose `GOV_PYTHON` names an interpreter below the floor now refuses inside the step
  as it refuses in every gate, where before the step might have found a launcher at the floor on
  `PATH`. That is the agreement this unit is for.
- testing: the `[dSP-75]` check in `check_step_isolation`, under §7's `New arm:` line.
- migration: none.
- user docs: `help/upgrade-steps.md`, S2.

## 6. Acceptance criteria

The probes run from the repository root.

- **AC1** — When
  `python -c "import os, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import upgrade_steps as us; os.environ['GOV_PYTHON'] = 'probe-py'; print(us.build_step_env(tempfile.mkdtemp()).get('GOV_PYTHON'))"`
  runs, it prints `probe-py`.
  Red when: `STEP_ENV_KEEP` leaves the name out, so it prints `None`, as at base.
- **AC2** — When the probe below runs the floor row's witness under the step contract, with fakes
  reporting 3.12 first on `PATH` and `GOV_PYTHON` naming the running interpreter, it prints a line
  opening `ok 0`.
  Red when: the step environment strips `GOV_PYTHON`, so it prints
  `failed 1 resolve_python: tried: python3 python py`, as the base probe showed.
  fixture: the running interpreter must be at the floor, 3.15, which the bar's own preflight already
  requires of this node.
  cost: a few seconds, one resolver spawn per candidate.

  ```python
  import os, pathlib, sys, tempfile
  sys.path.insert(0, "tools/govkit")
  import upgrade_steps as us
  root = pathlib.Path(".").resolve()
  row = next(r for r in us.read_steps(root, None, None) if r.id == "lib/python-floor-3.15")
  with tempfile.TemporaryDirectory() as td:
      fakes = pathlib.Path(td) / "below"
      fakes.mkdir()
      for nm in ("python3", "python", "py"):
          (fakes / nm).write_bytes(b'#!/usr/bin/env bash\necho "3.12 $0"\n')
          (fakes / nm).chmod(0o755)
      os.environ["PATH"] = str(fakes) + os.pathsep + os.environ["PATH"]
      os.environ["GOV_PYTHON"] = sys.executable
      got = us.run_step_isolated(row, "witness", root, root)
      print(got["verdict"], got["rc"], *(got["tail"].splitlines() or [""])[-1:])
  ```

- **AC3** — When `sed -n '/A clean environment/,/^- \*\*No git config/p' help/upgrade-steps.md`
  runs, its output holds `GOV_PYTHON`.
  Red when: the bullet does not name it.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 · `check_step_isolation` gains a `[dSP-75]` check running the floor row's witness under the contract with 3.12 fakes on `PATH` and `GOV_PYTHON` at the floor; observed RED at base 83817478, where the witness fails naming `python3 python py`, and GREEN after the build · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, closing H5 (id 9) and M2 (id 5) of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  by `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md`.
- rev-2 · 2026-10-28 · §7 · the leg line names `policy fixtures`, the leg whose guard
  `tools/govkit/selftest.py`, listed in §4's files touched, trips.
- rev-3 · 2026-10-28 · §4 · the header's node and §4's probe read `a`, the host the probe ran on,
  as the coordinator directed with the fold of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md`,
  which names no item against this spec.

## 10. Reuse audit

The seam extended is `STEP_ENV_KEEP` (`tools/govkit/upgrade_steps.py:170-171`), the isolation
contract's one allowlist, which `build_step_env` copies from and the isolation fixture derives its
expected set from (`:2800`). `tools/lib/resolve-python.sh`'s `resolve_python` and the inline copy in
`tools/push-main.sh:647` are the readers whose input the step now shares; neither changes. The
arm's fake launchers follow `write_fake_launcher` in `tools/lib/resolve-python.test.sh:181-183`.
`python tools/codebase-map/reuse_lookup.py "environment variables a step process inherits from the
parent"` ranked `step`, `read_steps`, `read_step_states`, `StepRow`, `derive_reverse_steps` and
`run_step_isolated`, none of them an allowlist, so the seam came from the code. The recall probe
ranked TOOL-dSafePassage-7, the contract's own spec, first, and TOOL-dSafePassage-11, the floor
step, third.

Recall terms used: `python tools/memory-recall/query.py "which environment names reach a step under the isolation contract and how does the resolver find the interpreter override" --terms "STEP_ENV_KEEP build_step_env GOV_PYTHON resolve_python allowlist isolation contract floor preflight interpreter override"`
