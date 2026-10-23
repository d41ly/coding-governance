# TOOL-dSafePassage-11 — the interpreter floor at Python 3.15, declared once, refused below by the resolver, and raised as the second upgrade step

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0028@032ca791 whole
**Carries:** node:policy-key.platforms.provision

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-11-deviation-111.md](../build/2026-10-23-build-TOOL-dSafePassage-11-deviation-111.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-11-deviation-31.md](../build/2026-10-23-build-TOOL-dSafePassage-11-deviation-31.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-7 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

Raise gov's interpreter floor to Python 3.15 (the owner's AP-31) as the step kind's second step,
`lib/python-floor-3.15`, after the receipt's schema-4 step whose `steps` field records its progress.
The floor is declared once and every floor statement reads it or points at it. The one Python
resolver refuses an interpreter below it, prefers a direct executable over an alias, and names the
install command as `platforms.provision` says. The step's down refuses while tracked files would not
run under the floor it restores, and the step is the template a later raise copies. This closes
`gap-tool-22` and `gap-tool-12`.

## 2. Scope (IN)

- **S1** — The declaration. `tools/lib/python-floor.txt` holds one line, `3.15`, the brief's S9.
  `read_floor` in `tools/lib/python_floor.py` reads it and refuses any content but `<major>.<minor>`
  and one optional newline. Observed by AC8 and AC9.
- **S2** — The resolver refuses below the floor. The canonical block in `tools/lib/resolve-python.sh`
  (`:24-54`) gains the literal line `_rp_floor="3.15"`, the generated copy of the declaration. Each
  candidate is probed once with `-I -c`, and the probe prints its `major.minor` and its own
  `sys.executable`. A candidate that runs below the floor is passed over and named in the refusal,
  exactly as a candidate that does not run is passed over today. Observed by AC1.
- **S3** — The resolver prefers the direct executable. An accepted candidate echoes the executable
  its probe printed, forward-slashed, when that path is a file, and its own name otherwise. The
  Windows App Execution Alias, measured at 129 ms per spawn against 25 ms for the interpreter it
  starts on node d on 2026-10-23, is then spawned once per resolve and never by a consumer.
  Observed by AC2.
- **S4** — The refusal names the install command as `platforms.provision` says (`name`, `uv` or
  `off`, default `name`, v2:1403). `name` prints the platform's command, `uv python install 3.15`
  first, then `py install 3.15` on Windows. `uv` offers that command once, on the terminal, when
  stderr is a terminal and `uv` runs, and otherwise prints what `name` prints with the reason it
  offered nothing. `off` prints no command. The key is read through `read_policy_key`
  (`cl-dClosedLoop-0008`) at the landed revision, and where no reader can run, the catalogue default
  applies and the refusal says so (`cl-dClosedLoop-0009`). Observed by AC3.
- **S5** — Every inline copy of the block is re-synced byte-identically: the 69 files the parity
  population names today, and the two unmarked copies `tools/check-line-length.sh:57` and
  `tools/playbook/adopt-playbook.sh:18`, which gain the markers so the parity rows grade them. A new
  arm reds any multi-line definition of `resolve_python` that carries no marker, measured at exactly
  those two files on 2026-10-23. Observed by AC10.
- **S6** — The preflight. `tools/lib/python-floor.sh preflight` sources the resolver and calls
  `resolve_python`. At the floor it prints the interpreter and its version and exits 0. Below it, it
  exits 1 with the resolver's own refusal, byte for byte, so it refuses the same way.
  Observed by AC4.
- **S7** — The step row. `tools/govkit/steps.toml` gains the `[[upgrade]]` row
  `lib/python-floor-3.15`, placed immediately after `govkit/receipt-schema-4` (the brief's S5), in
  the grammar TOOL-dSafePassage-1 owns. Its up and its witness are the preflight, and its down is
  `python-floor.sh down 3.11 {target}`. Observed by AC5 and AC11.
- **S8** — The down. `python-floor.sh down <prior> <target>` runs `check_down_floor`, which grades
  every tracked `.py` and `.toml` file of the target under the floor it restores. A finding exits 1,
  names each `path:line`, and writes nothing. With no finding, in a target that carries
  `<prefix>/lib/python-floor.txt`, which only gov's own source tree does, it runs `write_floor` to
  restore the prior value in the declaration and in every copy's literal line.
  Observed by AC6 and AC7.
- **S9** — One query finds every floor statement, whatever version it names.
  `scan_floor_statements` runs the pattern in §4 over tracked files outside `memory/`. At the base
  it finds six statements, `tools/settings-merge.py`'s `py>=3.10` among them. Each is rewritten in
  this unit to point at the declaration, so the query finds none afterwards. `check_floor_copies`
  grades every copy's literal against the declaration. Observed by AC8 and AC9.
- **S10** — The PEP 701 text ban in `merge-rows.test.sh`
  (`tools/memory-tree/merge-rows.test.sh:349-372`) is retired in this unit, because the resolver
  now refuses the interpreters it guarded against. The compile arm above it (`:345-347`) stays, since it compiles the driver under the interpreter the
  shim resolves. **Readers:** by name: `tools/memory-tree/merge-rows.test.sh`, the only file
  that spells the ban's `FSTR` predicate. by value: `tools/gate-legs.json`, whose
  `row-keyed merge driver replay` leg reads the suite's exit status the ban set. Observed by AC12.
- **S11** — The catalogue row for `platforms.provision` under `cl-dClosedLoop-0007`: its Allowed
  values `name`, `uv` and `off`, its default `name`, its summary and its usage, owner build
  dSafePassage. It is one of the keys presets never touch, because how a node gets its interpreter
  is the operator's (the away pass, interpretation for AP-32). Observed by AC3 and AC13.
- **S12** — The help page `help/python-floor.md`, with its row in `help/README.md`. It covers what
  the floor is, what the refusal says, how to install the floor, and the three values of
  `platforms.provision`. Observed by AC13.

## 3. Non-goals (OUT)

- The real-interpreter floor arm, which runs a real interpreter at the floor in the bar, and the
  TOML 1.0 arm. They are dWitnessedBar's (the answers-fold review, finding H2's fix), and this unit
  leaves them alone.
- Gov's own CI interpreter. Setting up Python at the floor in `.github/workflows/remote-ci.yml` is
  TOOL-dSafePassage-12's.
- Running the step on gov's tree at the landing. That is TOOL-dSafePassage-8's lander.
- Walking the step in the release-0 fixture. That is TOOL-dSafePassage-5's `upgrade-walk` leg.
- The emitted adopter CI and any macOS row. They are dShippedRelease's.
- A floor override in the environment. A variable that lowers the floor is a fail-open, and
  `GOV_PYTHON` already names the interpreter without moving the floor.
- Provisioning any node. The owner's AP-31 has every node upgrade, and the refusal names the command.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the `[[upgrade]]` row grammar, `tools/govkit/steps.toml` and its one reader; without them S7's row has no home and no reader
- **consumes-from** `TOOL-dSafePassage-3` — the `govkit/receipt-schema-4` row this row follows, and the receipt's `steps` field its progress is written to; without them AC11's receipt names no step
- **consumes-from** `TOOL-dSafePassage-2` — the walk that runs the row and stops at a failed step; without it AC11 has no walk to observe
- **consumes-from** `TOOL-dSafePassage-7` — the isolated runner the row's argv runs under, which resolves `{gov}` and hands the step its target root through `{target}`; without it `down` has no declared target
- **hands-off** `TOOL-dSafePassage-12` — the declaration `python-floor.txt`, read by remote CI's setup step, and `python-floor.sh preflight`, the bar's first step
- **hands-off** `TOOL-dSafePassage-8` — the row `lib/python-floor-3.15`, which the lander's gov-first walk runs on gov's tree
- **hands-off** `TOOL-dSafePassage-5` — the row `lib/python-floor-3.15` walked by the release-0 fixture: a planted below-floor interpreter stops the walk at this step, skipping the row lets the walk past it, and its down returns the fixture to release-0
- **hands-off** `TOOL-dSafePassage-13` — `help/python-floor.md` and the `platforms.provision` usage row, which the docs leg fingerprints
- **consumes-from** external — dGroundRules, landed: the policy catalogue (`cl-dClosedLoop-0007`) this row joins, and `read_policy_key` (`cl-dClosedLoop-0008`, `cl-dClosedLoop-0009`)
- **consumes-from** external — every node, and the build node first, running Python 3.15 (AP-31); node d runs 3.14.5 and 3.12 on 2026-10-23, so its resolver refuses once this lands
- **hands-off** external — dWitnessedBar's real-interpreter floor arm and its TOML 1.0 arm
- **consumes-from** `TOOL-dSafePassage-15` — the forward walk passing the schema step on a scratch adopter's schema-3 receipt; without it the walk refuses before it reaches the floor row
- **hands-off** `TOOL-dSafePassage-17` — the floor row declaring that its down's own exit decides a rollback, the repair of finding 51
- **hands-off** `TOOL-dSafePassage-23` — the resolver keeping an override's own name, the repair of finding 35
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### Data model

The declaration is the one line `3.15`. Every other spelling of the floor is one of two kinds.
A generated copy is the resolver block's `_rp_floor` literal, held equal to the declaration by
`check_floor_copies` and by the parity rows of `tools/lib/resolve-python.test.sh`. A pointer is
prose that names `python-floor.txt` and spells no version. The literal is a copy rather than a
read because the block also runs inline in copy-installed kits, where `{prefix}/lib` is not
installed (`tools/govkit/registry.toml:194`). §8 F2 records this choice.

The step row, in TOOL-dSafePassage-1's grammar (brief S1):

```toml
[[upgrade]]
id = "lib/python-floor-3.15"
up = ["bash", "{gov}/lib/python-floor.sh", "preflight"]
down = ["bash", "{gov}/lib/python-floor.sh", "down", "3.11", "{target}"]
witness = ["bash", "{gov}/lib/python-floor.sh", "preflight"]
surfaces = []
needs-target = false
resume = "atomic"
```

The row carries no `introduced` key, because TOOL-dSafePassage-1's reader derives the introducing
commit and refuses an authored one. `{gov}` and `{target}` are the grammar's placeholders, which
TOOL-dSafePassage-7's runner resolves; the runner's working directory is gov's checkout root. The
up writes nothing, so it is atomic and its witness is the same check it makes. The down's first
argument is the floor that step restores. A later raise's row carries its own pair, so a landed row
never reads the current declaration for its history. `needs-target` is `false`, because the down
compiles and parses the target's files and never executes them.

### The resolver block

The probe runs each candidate in turn: the caller's override, `GOV_PYTHON`, then `python3`,
`python` and `py`, as `resolve-python.sh:30` orders them today:

```bash
"$_rp_c" -I -c 'import sys; print("%d.%d" % sys.version_info[:2], sys.executable.replace("\\", "/"))'
```

The first word is compared with `_rp_floor` numerically, by major and then by minor. That keeps
one spawn per candidate, as today. A candidate at the floor echoes the printed executable when
`[ -f ]` holds, and otherwise its own name. Every candidate is recorded with its outcome, `did not
run` or `<ver>, below the floor 3.15`. The refusal prints them, the override lines that exist today
(`resolve-python.sh:43-50`), and then the S4 line. The forward slash is required: a backslashed
`C:\` path handed to MSYS bash loses its separators
(`memory/gotchas/bash-c-multiline-flattens-under-msys.md`). The measured alias rule in
`tools/run-gates/measure_legs.py:903-915` resolves the same way.

The S4 read. The block's refusal path reads `.governance/policy.toml` at `HEAD` through the
parent's `read_policy_key`, as the landed parent ships it to shell callers. If that reader is
shell, it rides the block as one more inline-copied function on its own parity row. If it is
Python only, the block runs it with the newest candidate that ran at any version, since `tomllib`
needs 3.11. With no reader able to run, the default `name` applies, and the refusal says why.
Today's three shell copies of `read_policy_key` (`tools/push-main.sh:404`,
`tools/run-gates/post-merge.sh:171`, `tools/unattended/unattended.sh:9517`) read `KEY=value` text,
and `cl-dClosedLoop-0008` extends that contract. §8 F1 records the re-ground.

### The floor module, `tools/lib/python_floor.py`

| Function | Does |
|---|---|
| `read_floor(root)` | the declaration as `(major, minor)`, refusing any other content |
| `scan_floor_statements(root, rev=None)` | `[(path, line, text)]` for every tracked file outside `memory/` matching the pattern below, read at `rev` through `git grep <rev>` when given |
| `check_floor_copies(root)` | each file of the parity population whose `_rp_floor` literal differs from the declaration, and each multi-line `resolve_python` definition that carries no marker |
| `resolve_floor_interpreter(version)` | the first of `python<X.Y>`, `py -<X.Y>` and `uv python find <X.Y>` (the last only when `uv` runs) whose probe reports exactly that `major.minor`, or `None` |
| `check_down_floor(target, prior)` | `(mode, findings)`, defined below |
| `write_floor(root, value)` | writes the declaration and the literal line of every file the parity population names |

The pattern, PINNED on 2026-10-23 at `a255d0de`, where it finds the six statements of S9 and no
other line:

```python
FLOOR_STATEMENT_RX = re.compile(r"""(?ix)
  \b(?:c?python|py)\s*(?:>=|≥|=>)\s*\d+\.\d+
| \bc?python\s*\d+\.\d+\s*(?:\+|or\s+(?:newer|later|above))
| \bat\s+least\s+c?python\s*\d+\.\d+
| \bpython-version\s*:\s*["']?\d+\.\d+
| \brequires-python\b
""")
```

Its CLI, from the worktree root: `python tools/lib/python_floor.py check [--rev <sha>]`. It prints
each statement and each copy finding, and exits 1 when there is any. With `--rev` it grades
statements only. `python tools/lib/python_floor.py down <prior> <target>` is the down's body.

`check_down_floor` takes the tracked `*.py` and `*.toml` files of the target
(`git -C <target> ls-files`). When `resolve_floor_interpreter(prior)` returns an interpreter, mode
`interpreter <path>`, one child of that interpreter, run with `-I`, applies `compile()` to every
`.py` and `tomllib.loads` to every `.toml`, and prints each failure. Otherwise, mode `static`,
the running interpreter applies `ast.parse(src, feature_version=prior)` to each `.py` and also runs
the PEP 701 check over its tokens. The check flags any string token inside a replacement field that
reuses the enclosing f-string's quote. It also flags a backslash or a `#` in a replacement field,
and a line break in a single-quoted f-string's field. Each `.toml` is parsed by the running
`tomllib`, and the static check then flags the four TOML 1.1 deltas: a line break or a trailing
comma inside an inline table, a `\e` or `\xHH` escape, and a time without seconds. The mode is
printed on the down's first line.

The static mode exists because `ast.parse(feature_version=(3, 11))` accepts a PEP 701 f-string
(measured by the floor research, `research-python-floor.md:31`). It was probed again on
2026-10-23, with 3.14.5 tokenizing `v = f"{"X" if c else "y"}"`: the inner `STRING` token reuses
the outer quote, and the ordinary f-string beside it showed no such token. What the static mode
does not see is every grammar change after the prior floor other than the four PEP 701 shapes, the
four TOML 1.1 deltas and what `feature_version` models. It is a departure, recorded as deviation-31 (§8 F3).

### Inventory

Minted:

- the files `tools/lib/python-floor.txt`, `tools/lib/python-floor.sh`, `tools/lib/python_floor.py`
  and `help/python-floor.md`;
- the functions in the table above;
- the block-local `_rp_floor` and the probe line;
- the verbs `preflight` and `down` on `python-floor.sh`, and `check` and `down` on
  `python_floor.py`;
- the step id `lib/python-floor-3.15`;
- the catalogue row for `platforms.provision`.

Naming cells: the six functions each pass `py.function`. `tools/lexicon/lexicon.py --suggest <name>
--as py.function` printed OK for `read_floor`, `scan_floor_statements`, `check_floor_copies`,
`resolve_floor_interpreter`, `check_down_floor` and `write_floor` on 2026-10-23. It refused
`find_*` for `scan_*`. No conf key and no gate leg.

### Migration

The six floor statements of S9 become pointers. Their new text names `python-floor.txt` in gov's
lib dir and spells no version:

- `README.md:90`
- `tools/codebase-map/README.md:18`
- `tools/codebase-map/map_lib.py:17`
- `tools/govkit/check_runbook_parity.py:34`
- `tools/govkit/govkit.py:108`
- `tools/settings-merge.py:3`

The two `tomllib` guards keep their import test. Only their message changes, to say that `tomllib`
ships with every interpreter at the floor. Every kit whose shipped bytes carry the block moves.
The lander mints those kit versions at the landing (`tools/push-main.sh:902`), so no unit pass
bumps one.

### Rollout

The change is live at landing, with no switch. The owner set the floor "now" (AP-31), so a node
below 3.15 is refused by every gate and hook from that commit on, and the refusal names the
command. A merge driver that cannot resolve exits 2 through `tools/lib/pyrun.sh:30` without
writing `%A`, so git marks the file conflicted rather than merging it, which is loud, not silent.

### A later raise

A later raise copies this unit. It writes the new value with `write_floor`. It appends a row
`lib/python-floor-<X.Y>` after the newest row, with `down` naming the floor it replaces. It
rewrites any statement the query finds, and it re-syncs the copies through the parity rows.

### Files touched (estimate)

- `tools/lib/python-floor.txt` (new)
- `tools/lib/python-floor.sh` (new)
- `tools/lib/python_floor.py` (new)
- `tools/lib/resolve-python.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/govkit/steps.toml`
- `tools/memory-tree/merge-rows.test.sh`
- `tools/settings-merge.py`
- `tools/govkit/govkit.py`
- `tools/govkit/check_runbook_parity.py`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/README.md`
- `README.md`
- `tools/check-line-length.sh`
- `tools/playbook/adopt-playbook.sh`
- `help/python-floor.md` (new)
- `help/README.md`
- The catalogue file of `cl-dClosedLoop-0007`, at the path the landed parent gives it. It is
  re-grounded at the build run's first pass.
- The inline copies, 69 files, derived by
  `git grep -l '^# >>> resolve_python' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md`
  less the canonical, on 2026-10-23:

`.githooks/pre-push` `.githooks/pre-push.runlog.test.sh` `.githooks/pre-push.test.sh`
`skills/session-kickoff/manifest-check.sh` `skills/session-kickoff/manifest-check.test.sh`
`tools/check-agent-cap-restatement.test.sh` `tools/check-hook-destinations.sh`
`tools/check-hook-destinations.test.sh` `tools/check-install-prefix.sh`
`tools/check-kit-placeholders.test.sh` `tools/check-kit-versions.sh`
`tools/check-line-length.test.sh` `tools/check-playbook-parity.sh`
`tools/check-playbook-parity.test.sh` `tools/check-spec-tokens.test.sh`
`tools/check-testsuite-counts.test.sh` `tools/check-wiring.sh` `tools/check-wiring.test.sh`
`tools/codebase-map/adopt-codebase-map.sh` `tools/codebase-map/adopt-codebase-map.test.sh`
`tools/drift-audit/adopt-drift-audit.sh` `tools/govkit/census.test.sh`
`tools/hooks/agent-cap.test.sh` `tools/hooks/format-guard.test.sh`
`tools/hooks/scratch-guard.test.sh` `tools/lexicon/adopt-lexicon.sh`
`tools/memory-recall/adopt-memory-recall.sh` `tools/memory-tree/adopt-memory-tree.sh`
`tools/memory-tree/check-memory-hygiene.sh` `tools/memory-tree/check-memory-hygiene.test.sh`
`tools/memory-tree/check-verdict-epoch.sh` `tools/memory-tree/kit-dogfood-parity.test.sh`
`tools/memory-tree/merge-rows.sh` `tools/process-monitor/adopt-process-monitor.sh`
`tools/process-monitor/adopt-process-monitor.test.sh` `tools/push-main.sh`
`tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh` `tools/roles/adopt-roles.sh`
`tools/run-gates/foreign-prefix.gov.test.sh` `tools/run-gates/run-gates.evidence.test.sh`
`tools/run-gates/run-gates.gov.test.sh` `tools/run-gates/run-gates.runlog.test.sh`
`tools/run-gates/run-gates.sh` `tools/run-gates/run-gates.test.sh`
`tools/run-gates/run-gates.turnstile.test.sh` `tools/run-gates/run-held-wsl.sh`
`tools/run-gates/run-selftests.sh` `tools/run-gates/run-selftests.test.sh`
`tools/runlog/adopt-runlog.sh` `tools/unattended/adopt-unattended.sh`
`tools/unattended/adopt-unattended.test.sh` `tools/unattended/check-brief-recorded.test.sh`
`tools/unattended/check-pass-order.test.sh` `tools/unattended/check-unattended.sh`
`tools/unattended/gate-guard.test.sh` `tools/unattended/run-unattended-gates.sh`
`tools/unattended/runlog-writer.test.sh` `tools/unattended/stall-recorder.test.sh`
`tools/unattended/stop-guard.test.sh` `tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh` `tools/workflows/check-protocol-parity.test.sh`
`tools/workflows/check-review-join.sh` `tools/workflows/check-review-join.test.sh`
`tools/workflows/check-verifier-fanout.sh` `tools/workflows/check-verifier-fanout.test.sh`
`tools/workflows/tier2-review.test.sh` `tools/workflows/unattended-build.test.sh`

### Alternatives rejected

- **The block reads `python-floor.txt` at run time.** A copy-installed kit has no `{prefix}/lib`,
  so the read would fail in every adopter (§8 F2).
- **A version-flagged parse alone for the down.** `feature_version` accepts PEP 701, as measured
  (`research-python-floor.md:31`), so it cannot be the only check.
- **A real interpreter at the restored floor, or refuse.** This fails `cl-dClosedLoop-0022`'s
  rollback on every node without 3.11, node d among them (§8 F3).
- **An environment variable that sets the floor.** It is a fail-open (§3).

## 5. Production-readiness checklist

- security: the probe is fixed text, run with `-I` so no `PYTHON*` variable or user site enters it,
  exactly as each candidate is already run today. `uv` is offered only on a terminal and runs only
  on an explicit `y`, never in an unattended run. The down executes no target code: it compiles and
  parses, and its child interpreter runs with `-I`. Its writes are the declaration and one literal
  line per copy, in a source-mode target only.
- perf / scale: one spawn per candidate, as today. Each consumer's later spawns go to the direct
  executable, 25 ms against the alias's 129 ms (PINNED, node d, 2026-10-23, ten spawns each). The
  down's interpreter mode is one child for the whole tracked population.
- error / empty / loading states: no candidate at the floor is a refusal naming every candidate and
  its outcome. An unreadable declaration is a refusal naming the file. A down with no interpreter at
  the prior floor runs in `static` mode and says so on its first line. `check` over an empty
  population is impossible on gov, because the parity population is non-empty by
  `resolve-python.test.sh`'s own arm.
- observability: the refusal lists each candidate. `preflight` prints the interpreter and the
  version it accepted. The down prints its mode and each finding as `path:line`.
- risks: a node below 3.15 stops at the first gate. That is the owner's stated cost (AP-31), and
  node d is such a node on 2026-10-23. A consumer splicing `$PY` unquoted into a `bash -c` string
  breaks on a path with spaces: `remote-ci.yml:317` is one, and a hosted runner's toolcache path
  carries none. The static down sees eight shapes and `feature_version`'s model and nothing else
  (deviation-31). Under TOOL-dSafePassage-7's environment only the names its `STEP_ENV_KEEP` lists
  survive, so the step's preflight resolves through `PATH` and never reads `GOV_PYTHON`, and a
  launcher that needs another variable to start fails there. AC11 runs the step under that
  runner, so a node where this bites reds there first.
- testing: the resolver arms over fake launchers in `resolve-python.test.sh`, the query and
  copy arms there, the down over a fixture repository, and the direct probes of §6.
- migration: §4 "### Migration". Kit versions are minted at the landing.
- user docs: `help/python-floor.md` and its `help/README.md` row (S12).

## 6. Acceptance criteria

A fake launcher is a two-line bash script under the run's scratch directory that prints
`<version> <its own path>` for any `-c` and exits 0. A floor interpreter is the path the resolver
returns on a node at 3.15.

- **AC1** — When `PATH="<fakes>:$PATH" GOV_PYTHON=<fake> bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  runs with `python3`, `python`, `py` and `GOV_PYTHON` all fakes printing `3.14`, it exits
  non-zero. Its stderr names each candidate with `3.14, below the floor 3.15`, and names
  `uv python install 3.15`.
  Red when: the probe asks only whether the candidate runs, as `resolve-python.sh:33` does at the
  base.
  fixture: the fakes under the run's scratch.
- **AC2** — When the same command runs with a fake `python3` printing `3.15 <floor interpreter>`
  first on `PATH`, it prints the floor interpreter's path with forward slashes, and not `python3`.
  Red when: an accepted candidate echoes its own name.
  fixture: a node at 3.15, which node d is not on 2026-10-23.
- **AC3** — When AC1's command runs in a scratch clone whose committed policy file sets
  `platforms.provision` to `off`, the refusal prints no install command. Set to `uv`, with stderr
  not a terminal, it prints `name`'s command and the words `not offered`. With the key unset, it
  prints `name`'s command.
  Red when: the block reads the working tree's file, or prints the same line for all three values.
  fixture: a scratch clone under `%TEMP%`, after dGroundRules lands.
- **AC4** — When `bash "tools/lib/python-floor.sh" preflight` runs under AC1's fakes, it exits 1,
  and its stderr equals that of AC1's command byte for byte. On a node at the floor it exits 0 and
  prints the interpreter and its version.
  Red when: the preflight compares versions itself instead of calling `resolve_python`.
- **AC5** — When `python -c "import sys, tomllib; print([r['id'] for r in tomllib.load(open(sys.argv[1], 'rb'))['upgrade']][:2])" "tools/govkit/steps.toml"`
  runs, it prints `['govkit/receipt-schema-4', 'lib/python-floor-3.15']`.
  Red when: the floor row is placed first, or anywhere but immediately after the schema-4 row.
- **AC6** — When `bash "tools/lib/python-floor.sh" down 3.11 <clone>` runs from a scratch clone with a
  planted tracked `.py` holding `v = f"{"X" if c else "y"}"`, landed after the raise, it exits 1.
  It names the planted file and line, and leaves `python-floor.txt` reading `3.15`. With the plant
  removed it exits 0, and the declaration and every copy's `_rp_floor` literal read `3.11`.
  Red when: the down grades with `ast.parse(feature_version=...)` alone, or writes before grading.
  fixture: a scratch clone under `%TEMP%`. Node d has no 3.11, so the run is in `static` mode,
  and the first line says so.
- **AC7** — When the down of AC6 runs over a planted tracked `.toml` holding a multi-line inline
  table, it exits 1 naming that file.
  Red when: the TOML half only calls the running `tomllib`, which accepts TOML 1.1 on 3.15.
- **AC8** — When `python "tools/lib/python_floor.py" check --rev 3708a705` runs, it prints six
  statements, `tools/settings-merge.py:3` with `py>=3.10` among them, and exits 1. When
  `python "tools/lib/python_floor.py" check` runs on the tree after the pass, it prints none and
  exits 0.
  Red when: the pattern misses `py>=3.10`, as the gap's `git grep -l '3\.11'` does, or a statement
  is left unrewritten.
  figure: six is PINNED, measured on 2026-10-23 at `a255d0de`, whose tree equals the base's
  outside `memory/`.
- **AC9** — When `python "tools/lib/python_floor.py" check` runs in a scratch clone where
  `python-floor.txt` reads `3.16`, it exits 1 naming every copy whose literal reads `3.15`. With a
  planted line `needs Python 3.12 or newer` in a tracked `.md`, it exits 1 naming that line.
  Red when: a copy's literal is not compared with the declaration.
  fixture: a scratch clone under `%TEMP%`.
- **AC10** — When `git grep -c '_rp_floor="3.15"' -- '*.sh' '.githooks/*'` runs, every file the
  parity population names prints `1`, and so do `tools/check-line-length.sh` and
  `tools/playbook/adopt-playbook.sh`. When `python "tools/lib/python_floor.py" check` runs with
  one of those two files' markers deleted, it names that file as an unmarked definition.
  Red when: either unmarked copy keeps the base's block, or the unmarked-definition arm reads only
  marked files.
- **AC11** — When `python tools/govkit/govkit.py update --target <scratch adopter> --to HEAD --write`
  runs under AC1's fakes, the walk stops at `lib/python-floor-3.15`. Its failure carries the
  preflight's refusal, and the receipt's `steps` holds `govkit/receipt-schema-4` as the last
  `applied` row.
  Red when: the floor row runs before the schema-4 row, or its failure leaves no `failed` row.
  fixture: a scratch adopter under `%TEMP%`, after TOOL-dSafePassage-1, -2, -3 and -7 are built.
- **AC12** — When `git grep -n 'FSTR=' -- tools/memory-tree/merge-rows.test.sh` runs, it prints
  nothing, and `git grep -n 'py_compile' -- tools/memory-tree/merge-rows.test.sh` still prints the
  compile arm.
  Red when: the ban survives, or the compile arm goes with it.
- **AC13** — When `git grep -n 'platforms.provision' -- help` runs, it names the new page
  `python-floor.md`, and the catalogue row it describes carries `name`, `uv`, `off` and the
  default `name`, a summary and a usage.
  Red when: the page or the row is absent, or the row's values differ from v2:1403.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `row-keyed merge driver replay` · `settings-merge selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `agent-cap self-test` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `format-guard self-test` · `hook destinations self-test` · `lexicon naming predicates` · `lexicon selftest` · `line-length gate selftest` · `manifest-check self-test` · `measure-legs selftest` · `playbook parity selftest` · `playbook render selftest` · `pre-push run-log line` · `process-monitor adopter selftest` · `pytest-guardrails self-test` · `review-join self-test` · `run-gates run-log line` · `run-selftests self-test` · `runlog selftest` · `scratch-guard self-test` · `straggler-guard arms` · `tier2-review self-test` · `transition-audit arms` · `unattended-build self-test` · `verifier fan-out self-test` · `push-main self-test` · `pre-push self-test` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC4 · fake launchers printing a below-floor version, and a fake alias printing a floor interpreter's path · none
New arm: tools/lib/resolve-python.test.sh · covers AC3 · a fixture repository whose committed policy file sets each value of `platforms.provision` · none
New arm: tools/lib/resolve-python.test.sh · covers AC8 AC9 AC10 · a planted floor statement, a declaration differing from the copies' literal, and an unmarked definition · none
New arm: tools/lib/resolve-python.test.sh · covers AC6 AC7 · a fixture repository carrying a planted PEP 701 f-string and a planted TOML 1.1 inline table · none

The PEP 701 ban leaves `tools/memory-tree/merge-rows.test.sh` (S10). That is an arm removed, not
added, so no `New arm:` line names it; the AC1 arm stages the case it guarded. What the arms above
do not check: a real 3.11 compile, which stays dWitnessedBar's, and any grammar change outside the
static mode's eight shapes.

## 8. Open questions

- **F1 — The parent is unbuilt, so what does this spec call the policy file, its catalogue and its
  reader?** dGroundRules has no spec yet, and its clauses are this build's interface to policy.
  Options: invent names now; cite the parent's clauses as the contract and re-ground at the build
  run. RESOLVED (agent, 2026-10-23, delegated): cite `cl-dClosedLoop-0007` for the catalogue row,
  `cl-dClosedLoop-0008` for `read_policy_key` and `cl-dClosedLoop-0009` for the default with its
  reason. The build run re-grounds against the landed parent first, before its first pass, and
  amends this spec where a name differs. Rung 1: the brief's "Every spec" list and v2:1765 state
  the contract. widens: none · relaxes: none
- **F2 — Where does each reader read the floor?** The brief's S9 says the resolver reads
  `python-floor.txt`. Options: (a) the block reads the file at run time, which fails in every
  copy-installed kit, because `{prefix}/lib` is a registry exemption and is not installed
  (`tools/govkit/registry.toml:194`); (b) the block carries a literal, the generated copy, held
  equal to the file by `check_floor_copies` and by the parity rows; (c) ship the file to adopters,
  which is a new install location (veto 2), outside what the grant names. RESOLVED (agent,
  2026-10-23, delegated): (b). The charter's `[contract]` rule is one source with generated copies
  and a parity gate, and (a) fails S2 in every adopter. Rung 3. widens: none · relaxes: none
- **F3 — How does the down grade "under the floor it restores" on a node with no interpreter at
  that floor?** Options: (a) a real interpreter at the prior floor or refuse, which fails
  `cl-dClosedLoop-0022`'s rollback to release-0 on every node without 3.11, node d among them;
  (b) a real interpreter when `resolve_floor_interpreter` finds one, otherwise the static mode of
  §4, which fails this clause's "fails to compile under the floor it restores" on such a node,
  while still catching its planted PEP 701 case; (c) the static mode always, which fails it
  everywhere. Every option fails a clause-tier bound, so rung 6 relaxes the weakest. (b) relaxes
  one bound on some nodes and keeps the stated red case. (a) breaks a sibling clause's rollback on
  every such node. RESOLVED (agent, 2026-10-23, delegated): (b), by the owner's "Relax the weakest
  bound" (ER:328), recorded as `2026-10-23-build-TOOL-dSafePassage-11-deviation-31.md`.
  relaxes: the down compiles under the restored floor's own interpreter only where one runs · widens: none
- **F4 — What does the down restore in an adopter's tree, which carries no declaration?** Options:
  (a) write a new declaration file into the adopter, which is a new install location (veto 2);
  (b) restore the declaration where the target carries it, which is gov's source tree, and leave an
  adopter's copies to the reverse of its file update, TOOL-dSafePassage-4's rollback. RESOLVED
  (agent, 2026-10-23, delegated): (b). In an adopter the old declaration is the inline copies,
  which are file rows, and a down step owns what lies outside them (the supersession research,
  candidate E's "Reversibility" row). Rung 1. widens: none · relaxes: none
- **F5 — Is the bar's own preflight this unit's, or remote CI's?** The clause's "the floor's
  preflight as the bar's first step" is TOOL-dSafePassage-12's text. Options: this unit adds a
  preflight leg to the bar; this unit ships `preflight` and TOOL-dSafePassage-12 runs it in remote
  CI. RESOLVED (agent, 2026-10-23, delegated): the latter, since a local bar already resolves Python
  first (`tools/run-gates/run-gates.sh:218`) and so refuses below the floor through S2. Rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-15`, `TOOL-dSafePassage-17`, `TOOL-dSafePassage-23`, `TOOL-dSafePassage-26`; no other section moved.

## 10. Reuse audit

The seam extended is the one resolver, `tools/lib/resolve-python.sh:24-54`, with its parity rows in
`tools/lib/resolve-python.test.sh` (`PARITY_ROWS`, the `blk` extractor and the population grep).
The direct-executable rule reuses the measured alias rule of
`tools/run-gates/measure_legs.py:903-915`. The step row lands in TOOL-dSafePassage-1's
`tools/govkit/steps.toml`. `reuse_lookup.py "refuse a python interpreter below the version floor
and name the install command"` ranked `resolve_python` first, a SEAM with 70 installs. Its install
list disagrees with source in three places: it includes `tools/check-line-length.sh` and
`tools/playbook/adopt-playbook.sh`, which carry the block without the marker, so the parity grep
misses them (S5), and `tools/push-main.test.sh`, whose definition is a one-line stub
(`tools/push-main.test.sh:915`), not a copy. Its other ranks, `CensusRefused`, `ScopeRefused` and
`read_host_name`, are name-token neighbours that resolve no version. No existing code reads a
floor, so the declaration, the query and the down are new. The recall probe found the
answers-fold review's H2 and M5 (`2026-10-18-review-PLAY-dClosedLoop-1-answers-fold-a.md:55`,
`:105`), which put the resolver's refusal in this unit, and
`memory/gotchas/step-depends-on-a-later-build.md`, which this unit's edges answer.

Recall terms used: `python tools/memory-recall/query.py "how is the python interpreter floor declared, enforced by the resolver and raised as an upgrade step" --terms "interpreter floor python 3.15 resolve_python resolver PEP 701 tomllib platforms.provision upgrade step preflight"`
