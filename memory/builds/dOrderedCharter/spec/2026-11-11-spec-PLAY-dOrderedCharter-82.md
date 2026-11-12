# PLAY-dOrderedCharter-82 — the acceptance matrix reads the renderer's bullet keys in a child process, so its closure stays its own

**Status:** CLOSED · rev-2 · 2026-11-11 · node a · Tier-1 · base c2ac2c03a · streams playbook · order 44 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-86 PLAY-dOrderedCharter-87 PLAY-dOrderedCharter-88 |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-83 |
| [2026-11-11-build-PLAY-dOrderedCharter-82-1-builder-return.md](../build/2026-11-11-build-PLAY-dOrderedCharter-82-1-builder-return.md) | journal | — |
| [2026-11-11-build-PLAY-dOrderedCharter-82-ledger.md](../build/2026-11-11-build-PLAY-dOrderedCharter-82-ledger.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The python-reads leg reds on fourteen modules the `govkit acceptance matrix` leg's closure imports
and its guard does not cover. Widening that guard reds the spec-token check on other builds' specs,
so this unit removes the cause: the matrix reads the renderer's bullet keys from a child process, the
import edge that pulled the renderer's closure into the matrix's goes away, and the guard stays as it
is.

## 2. Scope (IN)

- **S1** — `tools/playbook/render_playbook.py` gains `derive_bullet_keys(template)`, the sorted
  lowercased keys whose token is a whole line inside a one-line region of `template`, and a
  `--bullet-keys` flag that prints those keys for the template the engine renders, one per line, and
  exits 0. A refusal exits 1 and names itself on stderr, as the engine's other verbs do. Observed by
  AC3.
- **S2** — `derive_bullet_placeholders` in `tools/govkit/matrix.py` keeps its name, its signature and
  its one caller. It runs `render_playbook.py --bullet-keys` in a child process, at the path it
  already resolves through `govkit.resolve_kit_dir`, and returns the set of words the child prints.
  It no longer touches `sys.path` or imports the renderer. A non-zero exit raises, naming the exit
  code and the child's stderr. Observed by AC1, AC2 and AC4, with AC5 at the close.

## 3. Non-goals (OUT)

- Any edit to `tools/gate-legs.json`. The matrix row's guard, ceiling, argv, chunk and subject stay
  as they are.
- Any edit to the reads checker, `render_deploy_tail` or the stub rule PLAY-dOrderedCharter-81 S2
  set. Which keys take a `- ` stub is unchanged (AC4).
- A selftest arm for the flag in the renderer's `--selftest`. AC3 runs the flag over gov's own
  template and AC4 and AC5 run its one consumer.
- A `[[usage]]` row or a help page for the flag (section 4, Docs).
- A bump of `KIT_PLAYBOOK_RENDER_VERSION`. PLAY-dOrderedCharter-80 edited the renderer without one
  (`827115352`).

## 4. Design

### Evidence

Read at `c2ac2c03a`, whose `tools/` and charter template are those of `8ecef2cf1`. The reads leg is
refused to this writer's role, so each figure comes from calling the checker's own
`derive_guard_gaps` and `read_legs`, `tools/run-gates/py_reads.py@cf8f2730:179`.

- The red: fourteen gaps, all on the matrix row; eleven under `tools/memory-tree/`, two under
  `tools/policy/` and one under `tools/roles/` (PINNED, that probe at `8ecef2cf1`).
- The cause (PINNED, the same probe over a `git archive` of each commit): the matrix closure was 2
  files with 0 gaps at `84a28f634~1` and is 33 files with 14 gaps (PINNED) at `84a28f634`,
  PLAY-dOrderedCharter-81's build. The import that pulls them in is `import render_playbook as rp`,
  `tools/govkit/matrix.py@0d6bbdf0:113`, after the `sys.path` insert at
  `tools/govkit/matrix.py@0d6bbdf0:112`. The walk resolves a name against every kit directory a
  walked file resolves by a literal `resolve_kit_dir` call, `tools/run-gates/py_reads.py@cf8f2730:169`,
  so the renderer's own imports reach the three kits.
- Why the guard is not widened: rev-1 added the fourteen files to the matrix guard. At build, the
  spec-token check's guard join then flagged an OPEN spec of another build,
  `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md`. Its estimate names
  `tools/roles/roles_lib.py` and its leg line does not name the matrix leg. The modules appear in
  other builds' specs too, so any exact-file or directory guard over them causes the same problem.
- The fix measured: a scratch copy of the tree carrying S1 and S2 as section 4 writes them. There,
  the matrix closure is 2 files (PINNED), `tools/govkit/govkit.py` and `tools/govkit/matrix.py`,
  with 0 gaps, and the whole guard arm walks 26 rows with 0 gaps (PINNED, `derive_guard_gaps` over that copy).
  The walk does not follow a subprocess, `tools/run-gates/py_reads.py@cf8f2730:18`. The literal
  `resolve_kit_dir("playbook", ...)` call still adds the playbook directory, and no name the two
  govkit files import resolves there. `tools/govkit/govkit.py@37f075e4:9411` resolved the playbook kit
  literally before PLAY-dOrderedCharter-81 too, and the closure was two files then.
- The same copy's `--bullet-keys` prints seven keys: `adopter_rules`, `decision_principles`,
  `drive`, `override_rule`, `practices`, `principles` and `role_roster` (PINNED, that run). These
  are the seven that PLAY-dOrderedCharter-81 derived in process. Its stub probe prints the line AC4
  quotes. The child also works with the working directory outside the repository, because the
  template is resolved from the engine's own path.
- The template read: in gov, `resolve_template_path(root, root)` with `root` the engine's
  grandparent returns the root `coding-governance-agents.template.md`. That is the file the matrix
  reads today as `ROOT / rp.TEMPLATE_NAME` (PINNED, a probe at `8ecef2cf1`). In an install it
  returns the kit's copy, as every render does, `tools/playbook/render_playbook.py@bb09280e:1066`.

### The renderer (S1)

```python
def derive_bullet_keys(template: Path) -> list[str]:
    """PLAY-dOrderedCharter-82 S1. The sorted lowercased keys whose token is a whole line inside a
    one-line region of `template`: the render grades that line as a `- ` bullet, so an answer that
    fills it must be one."""
    inside, keys = False, set()
    for line in template.read_text(encoding='utf-8').splitlines():
        bare = line.strip()
        if bare in (ONE_LINE_OPEN, ONE_LINE_CLOSE):
            inside = bare == ONE_LINE_OPEN
        elif inside and (m := PLACEHOLDER_RE.fullmatch(bare)):
            keys.add(m.group(1).lower())
    return sorted(keys)
```

It sits after `resolve_template_path`, `tools/playbook/render_playbook.py@bb09280e:1066`. In
`main`, one `add_argument` follows the `--reference` one at
`tools/playbook/render_playbook.py@bb09280e:3734`, with a comment naming this unit. One branch
follows the `--selftest` branch at `tools/playbook/render_playbook.py@bb09280e:3742`:

```python
    if a.bullet_keys:
        root = Path(__file__).resolve().parent.parent.parent
        try:
            keys = derive_bullet_keys(resolve_template_path(root, root))
        except (Refusal, ValueError) as e:   # ValueError: the units module's LevelError
            print(f'render-playbook: REFUSED — {e}', file=sys.stderr)
            return 1
        print(chr(10).join(keys))
        return 0
```

`ValueError` is caught because `resolve_template_path` asks git for the kit prefix and the units
module raises `LevelError`, a `ValueError`, when git cannot answer,
`tools/playbook/instruction_units.py@1ac380c7:233`.

### The matrix (S2)

```python
def derive_bullet_placeholders() -> set[str]:
    """PLAY-dOrderedCharter-81 S2, PLAY-dOrderedCharter-82 S2. The lowercased keys whose token is a
    whole line inside a one-line region of gov's charter template, as the renderer's `--bullet-keys`
    prints them. A child process, so no import edge joins the renderer's closure to this one."""
    kd = govkit.resolve_kit_dir("playbook", "render_playbook.py", HERE)
    p = subprocess.run([sys.executable, str(kd / "render_playbook.py"), "--bullet-keys"], capture_output=True,
                       text=True, encoding="utf-8", stdin=subprocess.DEVNULL)
    if p.returncode:
        raise RuntimeError(f"render_playbook.py --bullet-keys exited {p.returncode}: {p.stderr.strip()}")
    return set(p.stdout.split())
```

`subprocess` and `sys` are already imported at `tools/govkit/matrix.py@0d6bbdf0:29`. The function
no longer reads `ROOT` or `NL`, which other code in the module still uses.

### What it does not check

The renderer's modules now run in a child process that the reads arm does not walk. An edit to
one of the fourteen no longer trips the matrix leg in a scoped bar, as it never did before
PLAY-dOrderedCharter-81. The same is already true of every kit the matrix reaches through `govkit
apply`. The pre-push hook's forced total run bounds how long such a break can go unseen,
`tools/run-gates/run-gates.sh@4ab05900:528`.

### Docs

The docs leg reds a flag only where a page under `help/` shows a command whose flag the entry's row
does not declare, `tools/govkit/docs_leg.py@259afa60:363`. The renderer's row,
`tools/govkit/usage.toml@fa34ce95:358`, declares only the three flags a page shows. `--bullet-keys`
is used only by gov's own matrix, which never travels, so no page shows it and no row is owed.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `derive_bullet_keys` | `tools/playbook/render_playbook.py` | `py.function`, `OK` by `--suggest` at design |
| `--bullet-keys` | the renderer's `main` | no cell in `.lexicon.conf` grades a flag |

### Risk

The leg's ceiling does not move. The matrix calls `render_deploy_tail` three times, at
`tools/govkit/matrix.py@0d6bbdf0:870`, `tools/govkit/matrix.py@0d6bbdf0:941` and
`tools/govkit/matrix.py@0d6bbdf0:999`. Each call now adds one child process, measured at 0.25 s on
node a (PINNED, one timed run over the scratch copy). The leg's evidenced run is 218.8 s against a
ceiling of 7030 (PINNED, `tools/run-gates/ceiling-evidence.txt@0d5d8d62:57`).

### Files touched (estimate)

- `tools/playbook/render_playbook.py` (S1)
- `tools/govkit/matrix.py` (S2)

## 5. Acceptance criteria

| Leg | Criteria |
|---|---|
| `python reads (a name never bound, an import outside its guard)` | AC1, with AC2 |
| `govkit acceptance matrix` | AC5, with AC3 and AC4 |

- **AC1** — When `python tools/run-gates/py_reads.py` runs over the tree after the pass, it exits
  0, prints no line opening `py-reads: RED`, and prints
  `py-reads: guards · 26 suites walked, 45 guarded legs of another head not read`. At the base it
  exits 1 and prints fourteen lines opening `py-reads: RED guard · govkit acceptance matrix ·`.
  Red when: the matrix still imports the renderer, so its closure reaches a kit outside its guard.
  figure: PINNED, 26 rows walked and 0 gaps by `derive_guard_gaps` over a scratch copy carrying the pass.
  permission: the main loop runs it; a role agent's scratch guard refuses this leg.
- **AC2** — When `python tools/run-gates/py_reads.py --guards "govkit acceptance matrix"` runs after
  the pass, it exits 0 and prints exactly two closure lines,
  `py-reads: closure · govkit acceptance matrix · tools/govkit/govkit.py` and
  `py-reads: closure · govkit acceptance matrix · tools/govkit/matrix.py`. The base prints 33
  closure lines and exits 1.
  Red when: an import edge from the matrix to the renderer survives.
  figure: PINNED, a closure of two files by the same probe; PLAY-dOrderedCharter-81's base `84a28f634~1` held the same two.
  permission: the main loop runs it, as for AC1.
- **AC3** — When `python tools/playbook/render_playbook.py --bullet-keys` runs after the pass, it
  exits 0 and prints seven lines, in order: `adopter_rules`, `decision_principles`, `drive`,
  `override_rule`, `practices`, `principles`, `role_roster`.
  Red when: the loop reads a placeholder outside every one-line region, or misses one inside.
  figure: PINNED, the seven by the flag over the scratch copy, as PLAY-dOrderedCharter-81 derived in process.
- **AC4** — When `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import matrix; print([l for l in matrix.render_deploy_tail(['roles'], {}).splitlines() if l.startswith(('role_roster', 'adopter_rules', 'node_table'))])"`
  runs after the pass, it prints
  `['adopter_rules = "- stated"', 'node_table = "stated"', 'role_roster = "- stated"']`, as the base
  does.
  Red when: the child's keys do not reach the stub rule, so a whole-line placeholder inside a
  one-line region takes the plain stub.
- **AC5** — When `python tools/govkit/matrix.py` runs after the pass, it prints `ok` for
  `default install: apply completes` and for `aged install: apply from the aged vintage completes`.
  Red when: the child refuses or prints nothing, so the default and aged installs meet the
  renderer's one-line refusal again.
  cost: one matrix run; its evidenced maximum is 218.8 s on node a (PINNED, `tools/run-gates/ceiling-evidence.txt`).
  permission: the main loop runs it at the close, since a role agent's scratch guard refuses a
  scratch install (PLAY-dOrderedCharter-72 AC6).

## 6. Gates

`python reads (a name never bound, an import outside its guard)` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

The guarded legs on the line are those the two touched files trip: `govkit acceptance matrix`,
`playbook render selftest` and `policy fixtures` for the renderer, and the govkit legs with `recall
floor arms` for `tools/govkit/` (DERIVED, the spec-token check's `--legs-for` over both paths).
`lexicon naming predicates` grades `derive_bullet_keys`.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-11 · initial draft, from `2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md`.
  The gaps were re-read at `8ecef2cf1` by a probe of the checker's own `derive_guard_gaps`, and
  attributed to PLAY-dOrderedCharter-81's build by the same probe over each commit's archived
  `tools/`. The brief named PLAY-dOrderedCharter-78 as the cause and counted fourteen memory-tree
  modules; three of the fourteen belong to the policy and roles kits.
- rev-1 · 2026-11-11 · AC3 · its command reads the manifest on stdin, `< tools/gate-legs.json`, in
  place of a quoted path inside `open(...)`, which the spec-token check graded as an untracked
  path. The observation and its printed figures are unchanged, re-probed at `8ecef2cf1`; the rev
  stays.
- rev-2 · 2026-11-11 · §1 §2 §3 §4 §6 §9 · S1 S2 · AC1 AC2 AC3 AC4 AC5 · diverged at build. The
  rev-1 guard widening made the spec-token check's guard join red on
  `2026-10-13-spec-TOOL-aOrientedCast-28.md`, so the cause is removed instead. S1, the guard scope
  item, and its AC3 are dropped. The new S1 is the renderer's `--bullet-keys` flag, and S2 runs it
  in a child process from `derive_bullet_placeholders`. The new AC2 observes the closure back at its
  pre-81 two files, AC3 the flag, AC4 keeps PLAY-dOrderedCharter-81's stub probe, and AC5 runs the
  matrix. Each figure was re-probed over a scratch copy carrying the pass, at `c2ac2c03a`.

## 9. Reuse audit

This unit extends an existing seam: the renderer's own CLI, whose verbs already serve other kits
(`--answers` serves another kit's renderer, `tools/playbook/render_playbook.py@bb09280e:3715`), and
its own one-line constants and `resolve_template_path`. `derive_bullet_placeholders` keeps its
`resolve_kit_dir` lookup and its caller. A child process is how the matrix already drives the
deployer, `tools/govkit/matrix.py@0d6bbdf0:165`. No new mechanism is added.

Recall terms used: `py_reads guard gap closure import edge subprocess render_playbook bullet placeholder one-line region resolve_kit_dir acceptance matrix spec-tokens guards join`
