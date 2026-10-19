# TOOL-dRenderedAnchor-1 — the kit resolver finds a rendered file through its receipt row, and the role render reds a harness listed where it is not installed

**Status:** SPECCED · rev-1 · 2026-10-19 · node d · Tier-2 · base a60b0c7d · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-19-build-TOOL-dRenderedAnchor-1-1-repro.md](../build/2026-10-19-build-TOOL-dRenderedAnchor-1-1-repro.md) | research | — |
| [2026-10-19-prompt-TOOL-dRenderedAnchor-1-brief.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

In an adopter, `resolve_kit_dir` misses every file govkit RENDERED from a template, because the
receipt row names the template and the kit directory carries the entry id, not gov's home. The role
index then lists two of gov's own harnesses at paths that do not exist, and agent-cap refuses both.
This unit widens the resolver's receipt step to find a rendered row, in the canonical and all 70
inline copies, and adds a red to `render_agents.py --check` for a harness the index lists where it
is absent while a file of its name is installed beside it.

## 2. Scope (IN)

- **S1** — The defect reproduced on a fresh scratch install, recorded as
  `build/2026-10-19-build-TOOL-dRenderedAnchor-1-1-repro.md`. It is present at `f576bd19`, and the
  build pass leaves it as written. Observed by AC1.
- **S2** — The receipt step of the canonical `tools/lib/resolve_kit_dir.py` also matches a row whose
  `role` is `rendered`, whose `source` sits directly under `<home>/` and whose `path` names a file
  called `<anchor>`. The exact `<home>/<anchor>` match, the in-tree and is-a-file tests, the probe
  step and the refusal keep their behaviour. The block's docstring and the module docstring name the
  rendered row. Observed by AC2 and AC4.
- **S3** — Every inline copy of the block carries the canonical's bytes: 70 copies in 70 files, the
  population the parity table of the `python resolver` leg reads. Observed by AC3.
- **S4** — `tools/roles/render_agents.py` gains `scan_misplaced_harnesses`. For each harness the
  resolver did not hold, it lists every file of that name sitting directly inside a directory under
  the tool root. A harness with a hit prints `MISPLACED_LINE` in place of `NOTE_LINE`, under both
  modes, and `--check` exits 1 on it. A harness with no hit prints `NOTE_LINE` and exits as today.
  Observed by AC5, AC7 and AC8.
- **S5** — Selftest arm 16 in `render_agents.py`: an adopter-shaped fixture whose harness directory
  is renamed and whose rendered harness's receipt row is sourced from its template. The index lists
  the harness where it sits and `--check` is clean. Observed by AC6.
- **S6** — Selftest arm 17 in `render_agents.py`: the same renamed directory with no receipt row
  reads `misplaced` and `--check` exits 1, and with no file of that name anywhere it reads the note
  and exits 0. Observed by AC7.
- **S7** — The user-facing text names the new red: the module docstring of `render_agents.py`, the
  index paragraph of `tools/roles/README.md` and the review-harness bullet of `help/roles.md`.
  Observed by AC9.
- **S8** — The comment above `resolve_receipt_path` in `tools/check-wiring.sh` states that it joins
  the exact `<home>/<anchor>` row only, that the Python reader also joins a rendered row, and that no
  caller of the shell reader passes a rendered anchor. Its awk body is unchanged. Observed by AC10.

## 3. Non-goals (OUT)

- Where govkit installs a kit. `{kit}` stays `<prefix>/<id>`, and the receipt's `source` keeps
  naming the template.
- `tools/hooks/agent-cap.js`, `.claude/rules/product.md` and `tools/roles/check_roles.py`. The
  catalogue checker's R9 note reads the same resolver and is correct once S2 lands, so it gains no
  `misplaced` arm.
- A red for a harness found nowhere in the install. That stays a note, by the owner's 2026-10-19
  ruling in the build README.
- A file of the harness's name outside a directory directly under the tool root, such as a hand copy
  under `.claude/workflows/`. The scan does not look there, and §4 says why.
- Widening the awk reader `resolve_receipt_path` in `tools/check-wiring.sh`. No caller of it passes a
  rendered anchor (§4), so S8 corrects its comment and nothing else.
- Kit version bumps. The lander's `mint` writes them (`tools/push-main.sh:26-29`).
- Merge and push, which wait for the owner's explicit ask.

### Edges

none

## 4. Design

### The defect, at the line

`tools/lib/resolve_kit_dir.py:36` keeps a receipt row only when the last two segments of its
`source` are `[home, anchor]`. govkit writes a rendered file's row with the TEMPLATE as `source`:
`tools/govkit/govkit.py:7807-7808` builds the row for a skipped file, and the repro's receipt listing
shows the four harnesses. The review-harness descriptor lands each at `{kit}/<file>`, on lines 64,
78, 84 and 90 of `tools/workflows/kit.toml`, where `{kit}` is `<prefix>/review-harness`. So
`resolve_kit_dir("workflows", "tier2-review.js", …)` finds no row, its probes of `<here>/workflows` and `<here>/../workflows` miss, and it raises.
`roles_lib.resolve_harness_path` (`tools/roles/roles_lib.py:585-594`) catches that and returns the
unheld `<tool root>/workflows/<file>`, which `derive_harness_paths`
(`tools/roles/render_agents.py:141-152`) writes into `harnesses`. agent-cap's rule 6
(`tools/hooks/agent-cap.js:2172-2174`) then refuses the path the install does hold.

### The receipt predicate (S2, S3)

The loop body of the block becomes:

```python
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
```

Step 1 of the block's docstring names both joins: the exact row, or a `rendered` row whose `source`
(its template) sits directly under `<home>/` and whose `path` names a file `<anchor>`. The module
docstring at `tools/lib/resolve_kit_dir.py:8-10` adds one sentence: a rendered row's `source`
spells its template, so that row joins on its home and its `path`'s file name, citing
TOOL-dRenderedAnchor-1. The builder writes the block once in the canonical and copies its bytes into
the 70 other files between the existing markers. Every shell copy reads the block through a quoted
heredoc (`tools/lib/resolve-python.test.sh:106-110` is one), and the new lines carry no backslash and
no single quote, so no copy needs an escape.

The three terms of the widened join, each measured on a scratch fixture under `%TEMP%` on
2026-10-19 with the predicate above, the base predicate, and the predicate without its role term:

| Row | role | source | path | Fixed | Base | No role term |
|---|---|---|---|---|---|---|
| 1 | rendered | `…/workflows/t.template.js` | `tools/review-harness/t.js` | `tools/review-harness` | LookupError | `tools/review-harness` |
| 2 | engine | `…/workflows/u.js` | `tools/review-harness/u.js` | `tools/review-harness` | `tools/review-harness` | `tools/review-harness` |
| 3 | merged | `…/hooks/s.fragment.json` | `.claude/s.json` | LookupError | LookupError | `.claude` |
| 4 | rendered | `…/other/v.template.js` | `tools/review-harness/v.js` | LookupError | LookupError | LookupError |
| 5 | rendered | `…/workflows/w.template.js` | `../<fixture>-out/w.js`, a file | LookupError | LookupError | LookupError |
| 6 | rendered | `…/workflows/x.template.js` | `tools/review-harness/x.js`, absent | LookupError | LookupError | LookupError |

Row 1 is the defect. Row 3 is why the role term exists: a `merged` row's `path` is a shared file such
as the settings file, and its parent is no kit's directory. Rows 4 to 6 hold the home, escape and
existence tests. AC2 re-observes this table.

**Receipt order cannot pick between the two joins.** For one `(home, anchor)`, an exact row and a
rendered row would need one kit to ship a file `<anchor>` and also render a template to `<anchor>`.
`scan_claimed_paths` (`tools/govkit/govkit.py:6669`) drops from the engine pool every destination
another rule claims, so a rendered destination never also lands as an engine file.

### Which callers move

Enumerated over every literal `resolve_kit_dir` call in `tools/`, `skills/` and `.githooks/` at
`a60b0c7d`. Only these pass a rendered anchor, and each answers in an adopter where it raised before:

| Caller | Anchor | Ships |
|---|---|---|
| `tools/roles/roles_lib.py:592`, through `resolve_harness_path` | each `workflow`-driver harness | yes |
| `tools/codebase-map/map_extractors.py:206` | `tier2-review.js` | yes |
| `tools/drift-audit/selftest.py:2607` | `drift-audit-code.js`, `drift-audit-state.js` | selftest |
| `tools/govkit/selftest.py:112` | `tier2-review.js` | selftest |
| `tools/hooks/agent-cap.test.sh:877` | `tier2-review.js` | suite |

No caller passes a rendered anchor whose `to` sits outside `{kit}`. The guides, the skills and
`REVIEW-PROTOCOL.md` render to `{memory_root}/` or `.claude/skills/`, and no call names them. In gov,
which holds no `.governance/install.json`, the receipt step reads no rows and every answer is the
probe's, as today.

### The misplaced red (S4)

```python
#: A harness the resolver did not hold while a file of its name sits in a kit directory.
MISPLACED_LINE = ("render_agents: misplaced %s — the workflow table names it and it is absent "
                  "here, while %s is installed; the kit resolver did not find it")


def scan_misplaced_harnesses(absent, tool_root, target_root):
    """`{rel: [found rel, ...]}` for each absent harness whose file name sits directly inside a
    directory under the tool root; a harness with no such file is not a key."""
```

The scan walks `sorted(pathlib.Path(tool_root).iterdir())`, keeps each directory `d` for which
`d / <file name>` is a file, and spells each hit repo-relative as `derive_harness_paths` does. The
file name is the last segment of the absent path. Only absent harnesses are scanned, so a held
harness never reads as misplaced, which AC8 observes in gov.

In `run_mode`, the loop at `tools/roles/render_agents.py:239-240` becomes: each absent harness prints
`MISPLACED_LINE % (rel, ", ".join(hits))` when the scan has it, else `NOTE_LINE % rel`. Under
`--check`, the graded line and any drift lines print as today, then the mode returns 1 when there is
drift OR a misplaced harness. Under `--write`, the exit code is unchanged: `--write` never reds on
what it graded, and the `roles render wiring` leg runs `--check`. The note's claim "its kit is not
installed" is then printed only where no file of the name was found, which is the case it describes.

**One level, and why.** govkit lands every kit at `<prefix>/<id>` (`{kit}`), and the render's tool
root is that `<prefix>`, so a directory directly under the tool root is where any govkit install
puts a harness. Going deeper reads fixture copies and caches as installs. A hand copy elsewhere is
the documented non-goal.

`adopt-roles.sh --check` (`tools/roles/adopt-roles.sh:205-209`) passes the line through and then
prints its own `--scaffold` remedy. A re-render does not clear a misplaced harness, so the line names
its own cause, the resolver, and §5 records the remedy line as a known imprecision.

### The selftest arms (S5, S6)

Both arms build on `build_fixture` (`tools/roles/render_agents.py:271-294`), each in its own
`tempfile.TemporaryDirectory`, as arms 8, 11 and 14 do. Each moves `<FIXTURE_ROOT>/workflows` to
`<FIXTURE_ROOT>/renamed`, the shape govkit gives a kit whose id is not its home, and makes a `.git`
directory at the fixture root, so the resolver's root walk stops at the fixture root and reads
`.governance/install.json` there, as it does in an adopter.

- **Arm 16** writes `.governance/install.json` holding one row: `role` `rendered`, `kit` any id,
  `source` `FIXTURE_HARNESS` with `.js` turned into `.template.js`, and `path`
  `<FIXTURE_ROOT>/renamed/a.js`. `--write` then `--check` both return 0, `harnesses` is the one
  path under `renamed`, and neither output carries a `note` or a `misplaced` line for `a.js`.
- **Arm 17** writes no receipt. `--write` returns 0 and prints `MISPLACED_LINE` for
  `<FIXTURE_ROOT>/workflows/a.js` naming `<FIXTURE_ROOT>/renamed/a.js` and no `NOTE_LINE` for it;
  `--check` returns 1 printing that line. With the file under `renamed` unlinked, `--check` returns 0
  and prints `NOTE_LINE` and no `misplaced` line, which is the owner's found-nowhere ruling.

The receipt `source` is derived from `FIXTURE_HARNESS` and never typed: a literal kit segment followed
by a file is a hit under rule 3 of `tools/check-install-prefix.sh:48`, and the `{prefix}/` lead is a
drained spelling under its rule 5. The rename target `renamed` names no kit directory.

### The awk reader's comment (S8)

`tools/check-wiring.sh:327-341` says the reader's join is "exactly that reader's join, which the
self-test holds this one equal to". After S2 it is the exact half of it. The callers of
`resolve_receipt_path` pass `agent-cap.js`, `scratch-guard.fragment.json`,
`recall-opened.fragment.json`, `merge-rows.py`, `settings-merge.py`, `push-main.sh` and the kickoff
fragments, at lines 606, 839, 907, 975, 1041, 1220 and 1478 of `tools/check-wiring.sh`. None of them
is rendered, and the S5 parity arm at `tools/check-wiring.test.sh:1707-1721` compares three engine
pairs. The comment says so in two sentences. The file also carries a block copy, so S3 already
writes it.

### Inventory

Minted: the function `scan_misplaced_harnesses` and the constant `MISPLACED_LINE` in
`tools/roles/render_agents.py`, and selftest arms 16 and 17. `scan` is a declared verb in the VERBS
table of `.lexicon.conf` ("walk a population looking for matches"). No receipt field, conf key, leg
or file is minted.

### Rollout

Tier-2: a shipped kit edit, and a cross-kit change to a carried predicate. No receipt, conf or deploy
shape moves, so no adopter needs an upgrade step: `govkit update` carries the new bytes and the next
`adopt-roles.sh --scaffold` writes the corrected index. Kit versions are minted at landing
(`tools/push-main.sh:26-29`), and the generated map regenerates there through the run-gates kit's
`regen.py --write` (`tools/push-main.sh:35-40`).

### Files touched (estimate)

- `tools/lib/resolve_kit_dir.py`, the canonical
- `tools/roles/render_agents.py`, `tools/roles/roles_lib.py`, `tools/roles/README.md`, `help/roles.md`
- `.githooks/pre-push`, `.githooks/pre-push.runlog.test.sh`, `.githooks/pre-push.test.sh`
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/manifest-check.test.sh`
- `tools/check-agent-cap-restatement.test.sh`, `tools/check-hook-destinations.test.sh`,
  `tools/check-install-prefix.sh`, `tools/check-kit-versions.sh`, `tools/check-line-length.test.sh`,
  `tools/check-playbook-parity.sh`, `tools/check-playbook-parity.test.sh`,
  `tools/check-spec-tokens.test.sh`, `tools/check-testsuite-counts.test.sh`, `tools/check-wiring.sh`,
  `tools/check-wiring.test.sh`, `tools/push-main.sh`, `tools/settings-merge.py`
- `tools/codebase-map/map_extractors.py`, `tools/codebase-map/test_codebase_map.py`,
  `tools/codebase-map/test_codebase_map.template.py`
- `tools/drift-audit/drift_report.py`, `tools/drift-audit/selftest.py`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`
- `tools/hooks/agent-cap.test.sh`, `tools/hooks/format-guard.test.sh`,
  `tools/hooks/scratch-guard.test.sh`
- `tools/lexicon/adopt-lexicon.sh`
- `tools/lib/render-doc.sh`, `tools/lib/resolve-python.test.sh`
- `tools/memory-recall/extract.py`
- `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/backlog.py`,
  `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/check-verdict-epoch.sh`,
  `tools/memory-tree/corpus_ids.py`, `tools/memory-tree/kit-dogfood-parity.test.sh`,
  `tools/memory-tree/marker-contract.test.sh`, `tools/memory-tree/merge-rows.py`,
  `tools/memory-tree/merge-rows.test.sh`, `tools/memory-tree/row_grammar.py`,
  `tools/memory-tree/transition_audit.py`
- `tools/playbook/render_playbook.py`
- `tools/run-gates/measure_legs.py`, `tools/run-gates/run-gates.evidence.test.sh`,
  `tools/run-gates/run-gates.runlog.test.sh`, `tools/run-gates/run-gates.sh`,
  `tools/run-gates/run-gates.test.sh`, `tools/run-gates/run-gates.turnstile.test.sh`,
  `tools/run-gates/run-selftests.test.sh`
- `tools/runlog/selftest.py`
- `tools/unattended/adopt-unattended.sh`, `tools/unattended/adopt-unattended.test.sh`,
  `tools/unattended/check-brief-recorded.test.sh`, `tools/unattended/check-pass-order.test.sh`,
  `tools/unattended/gate-guard.test.sh`, `tools/unattended/lib-unattended.sh`,
  `tools/unattended/run-unattended-gates.sh`, `tools/unattended/runlog-writer.test.sh`,
  `tools/unattended/stall-recorder.test.sh`, `tools/unattended/stop-guard.test.sh`
- `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/check-review-join.sh`,
  `tools/workflows/check-review-join.test.sh`, `tools/workflows/check-verifier-fanout.sh`,
  `tools/workflows/check-verifier-fanout.test.sh`, `tools/workflows/tier2-review.test.sh`,
  `tools/workflows/unattended-build.test.sh`
- `memory/builds/dRenderedAnchor/build/`, for this unit's acceptance ledger

The 71 block files are DERIVED by
`git grep -l '^# >>> resolve_kit_dir' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md`, measured
at `a60b0c7d` on 2026-10-19. The builder writes the population that command prints at build time.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — widen the resolver's receipt step, canonical and every copy | rows 1 to 6 above read as intended; every caller in the callers table answers | Chosen, the owner's 2026-10-19 ruling |
| C2 — fix only roles' harness lookup | `tools/codebase-map/map_extractors.py:206` and the selftest callers keep raising in an adopter | Rejected by the owner, 2026-10-19 |
| C3 — the brief's join with no role term | row 3 answers `.claude`: a `merged` row's shared file reads as a kit directory | Rejected |
| C4 — derive the template name from the anchor (`t.js` to `t.template.js`) | `fixture-record-one.template.md` renders to a file whose name is not its stem (`tools/unattended/kit.toml:144-146`), so a naming rule is a second convention to keep true | Rejected |
| C5 — the misplaced scan reads the receipt's `path` column | the scan would share its state with the resolver it guards, against the charter's `[class]` rule, and stay silent on a receipt-less install | Rejected |
| C6 — the scan reads `git ls-files`, the brief's "tracked" | `apply` never commits (`tools/govkit/govkit.py:7938`), and the four harnesses are written by the hand render after it, so an index read misses the files AC5 must name. Whether that render stages them is UNVERIFIED | Rejected |
| C7 — the scan walks the whole tool root recursively | fixture copies and caches under a kit read as installs | Rejected |
| C8 — the arm in the resolver's own suite instead of the roles selftest | the brief and the owner's scope put it in `render_agents.py --selftest`; the parity table holds the other 70 copies to the one the arm exercises | Not taken |
| C9 — split the misplaced red into a second unit | the owner's "go" approved the brief's one-unit scope; the two halves write disjoint files (S2 and S3 against S4 to S7), so a closing finding still lands on one half. The precedent is `TOOL-dRedressedBar-24`, a fix and its class red in one unit | Not taken |

## 5. Production-readiness checklist

- security — No new write path, input or egress. The widened join trusts a `rendered` receipt row
  exactly as far as an exact row: the hit must be a file inside the tree, with no `..` part. The scan
  reads one directory listing under the tool root and writes nothing.
- perf / scale — One more comparison per receipt row per call. The scan runs only for an absent
  harness, one `iterdir` of the tool root each, which in gov is zero runs.
- error / empty / loading states — An absent, unreadable or malformed receipt reads as no rows, as
  before. An unreadable tool root raises `OSError` out of the scan; it is the directory the render
  already reads its kit from, so the render could not have started without it.
- observability — `MISPLACED_LINE` names the listed path and every installed path. The adopter's
  trailing remedy line names `--scaffold`, which does not clear a misplaced harness; the line itself
  names the resolver as the cause.
- risks — 71 files move in one pass, so a copy left behind is the main risk; AC3 and the parity leg
  each catch it. A caller that relied on the raise for a rendered anchor now gets an answer; the
  callers table shows each one wants it.
- testing — AC2 and AC6 to AC8 are in-process probes; AC4 and AC5 run a scratch install. Arms 16
  and 17 are the suite's, observed RED then GREEN by the main loop at the close (§7).
- migration — N/A — no receipt, conf or deploy field moves; the next render corrects the index.
- user docs — `help/roles.md` names the new red beside the existing note (S7).

## 6. Acceptance criteria

`<p1>` is this unit's build pass commit, `$T` a fresh scratch target at `%TEMP%/rh2`, and every
command runs from the worktree root unless it says it runs in `$T`.

- **AC1** — When `grep -cE '^## (Instruments|Results|Root cause)$'` runs over
  `memory/builds/dRenderedAnchor/build/2026-10-19-build-TOOL-dRenderedAnchor-1-1-repro.md`, it prints
  3, and `grep -c 'not a declared harness'` over the same file prints 2.
  Red when: the record is absent or carries no measured agent-cap verdicts, and both counts read 0.
- **AC2** — When a python program loads `tools/lib/resolve_kit_dir.py`, builds a fixture under
  `%TEMP%/rka` with a `.git` directory, `.governance/install.json` and the six rows of §4's table,
  and calls `resolve_kit_dir` for each row's home and anchor with `here` at the fixture's `tools`,
  it prints `tools/review-harness` for rows 1 and 2 and `LookupError` for rows 3 to 6.
  Red when: the block holds its `a60b0c7d` text, and row 1 prints `LookupError`; or the role term is
  left out, and row 3 prints `.claude`.
  fixture: built by the probe and deleted after; observed at spec time on the §4 predicates.
- **AC3** — When a python program lists the files
  `git grep -l '^# >>> resolve_kit_dir' -- '*.sh' '*.py' '.githooks/*' WIRE-INTO-PROJECT.md` prints,
  extracts every block from its `# >>>` marker to its `# <<<` marker with carriage returns stripped,
  and prints the block count, the file count and the count of distinct blocks, it prints `71 71 1`
  at `<p1>`, and the one block carries `row.get("role") == "rendered"`.
  Red when: one copy keeps the `a60b0c7d` block, and the distinct count reads 2.
  figure: 71 is DERIVED by the grep at observation; it read 71 at `a60b0c7d`, PINNED 2026-10-19.
- **AC4** — When the five instruments of the S1 record run from `<p1>` into `$T`, then
  `python -c "import json; print(json.load(open('.claude/roles.json'))['harnesses'])"` run in `$T`
  prints `['tools/review-harness/tier2-review.js', 'tools/review-harness/unattended-build.js',
  'tools/review-harness/unattended-unit.js']`, each of the three is a file in `$T`, and the
  `adopt-roles.sh --scaffold` output carries no `render_agents: note` and no `render_agents:
  misplaced` line naming a harness. `node tools/hooks/agent-cap.js`, run in `$T` with
  `CLAUDE_PROJECT_DIR` set to it, exits 0 on the instrument-5 payload for
  `tools/review-harness/tier2-review.js` and for `tools/review-harness/unattended-build.js`, each
  carrying as `args.roles` what `python tools/roles/handoff.py harness-args tier2-review` and
  `harness-args unattended-build` print in `$T`.
  Red when: run from `a60b0c7d`, where the record measured two `tools/workflows/` paths absent from
  disk and rc 2 with `not a declared harness` for both payloads.
  cost: a 26-kit intake and apply plus one render; its duration is UNVERIFIED.
  fixture: `$T` is built by the instruments under `%TEMP%`, never inside the worktree; none exists
  today.
- **AC5** — When, in the AC4 target, `tools/roles/roles_lib.py` is overwritten by
  `git show a60b0c7d:tools/roles/roles_lib.py` and `python tools/roles/render_agents.py --check` runs
  in `$T`, it exits 1 and prints one `render_agents: misplaced tools/workflows/tier2-review.js` line
  naming `tools/review-harness/tier2-review.js` and one for `unattended-build.js` naming
  `tools/review-harness/unattended-build.js`, and no `render_agents: note` line for either. With the
  file restored from `<p1>`, the same command exits 0 and prints no `misplaced` line.
  Red when: `scan_misplaced_harnesses` finds nothing, as the `a60b0c7d` render does, and the
  overwritten install prints two `note` lines and exits 1 on index drift alone.
- **AC6** — When a python program imports `tools/roles/render_agents.py`, calls `build_fixture` in a
  scratch directory with one agent role whose `workflow` is `w1`, moves `toolroot/workflows` to
  `toolroot/renamed`, makes `.git` at the scratch root, writes arm 16's one-row
  `.governance/install.json`, and calls `run_mode("write", kit, tool_root, root)` then
  `run_mode("check", kit, tool_root, root)`, both return 0, `harnesses` in `.claude/roles.json` is
  `["toolroot/renamed/a.js"]`, and neither output carries a `render_agents: note` line naming `a.js`
  or any `render_agents: misplaced` line. The fixture writes no gate manifest, so `MANIFEST_NOTE`
  prints and is not graded here.
  Red when: `tools/roles/roles_lib.py`'s block holds its `a60b0c7d` text, and `harnesses` reads
  `["toolroot/workflows/a.js"]` with `check` returning 1 on a `misplaced` line.
- **AC7** — When the AC6 program runs with no `.governance/install.json`, `run_mode("write", …)`
  returns 0 and prints exactly one line opening `render_agents: misplaced`, which equals
  `MISPLACED_LINE % ("toolroot/workflows/a.js", "toolroot/renamed/a.js")`, and no
  `NOTE_LINE % "toolroot/workflows/a.js"`; `run_mode("check", …)` returns 1 and prints that line.
  With `toolroot/renamed/a.js` unlinked, `run_mode("check", …)` returns 0, prints `NOTE_LINE % "toolroot/workflows/a.js"` and prints no `misplaced` line.
  Red when: `scan_misplaced_harnesses` returns `{}`, and the first `check` returns 0 with the note; or
  the scan keys a harness with no hit, and the last `check` returns 1.
- **AC8** — When `python tools/roles/render_agents.py --check` runs in this repository at `<p1>`, it
  exits 0 and prints no `render_agents: misplaced` line, and
  `git diff --quiet a60b0c7d <p1> -- .claude/roles.json .claude/agents/` exits 0.
  Red when: the scan reads held harnesses too, and each listed `tools/workflows/` harness reads as
  misplaced against itself with an exit of 1.
- **AC9** — When `grep -c 'misplaced'` runs over `help/roles.md`, `tools/roles/README.md` and
  `tools/roles/render_agents.py`, each count is at least 1, and `grep -c 'rendered'` over
  `tools/lib/resolve_kit_dir.py` is at least 2, one in the module docstring and one in the block.
  Red when: a page is left as at `a60b0c7d`, where every one of the four counts reads 0.
- **AC10** — When `sed -n '/THE RECEIPT RUNG/,/^resolve_receipt_path/p' tools/check-wiring.sh` runs,
  its output carries `rendered` and `TOOL-dRenderedAnchor-1`, and
  `sed -n '/^resolve_receipt_path() {/,/^}/p' tools/check-wiring.sh` prints the same bytes at
  `a60b0c7d` and at `<p1>`.
  Red when: the comment still claims the full join, where the `rendered` count reads 0 at
  `a60b0c7d`, or the awk body moves.

## 7. Gates

`roles render selftest` · `roles render wiring` · `roles catalogue` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `install-prefix (shipped surface)` · `memory hygiene` · `agent-cap self-test` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `codebase-map kit selftest` · `drift-audit selftest` · `format-guard self-test` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `hook destinations self-test` · `lexicon naming predicates` · `lexicon selftest` · `line-length gate selftest` · `manifest-check self-test` · `measure-legs selftest` · `playbook parity selftest` · `playbook render selftest` · `pre-push run-log line` · `recall floor` · `recall floor arms` · `review-join self-test` · `run-gates run-log line` · `run-selftests self-test` · `runlog selftest` · `scratch-guard self-test` · `straggler-guard arms` · `tier2-review self-test` · `transition-audit arms` · `unattended-build self-test` · `verifier fan-out self-test`

The first seven are the brief's. The rest are owed by the non-broad guards the Files touched paths
trip, derived on 2026-10-19 from `tools/gate-legs.json` with the breadth floor of
`tools/check-spec-tokens.py:262`. The guards `{prefix}/`, `{prefix}/lib/`, `{prefix}/memory-tree/`,
`{prefix}/memory-recall/`, `{prefix}/run-gates/` and `.githooks/` are broad and owe nothing here.
The close runs the bar once, after the unit is terminal; no pass runs a leg.

New arm: tools/roles/render_agents.py --selftest, arm 16 · covers AC6 · the `a60b0c7d` resolve_kit_dir block restored in tools/roles/roles_lib.py · none
New arm: tools/roles/render_agents.py --selftest, arm 17 · covers AC7 · scan_misplaced_harnesses stubbed to return an empty dict · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-19 · initial draft from the unit's brief and repro record. The widened join was
  measured over six receipt rows on a scratch fixture against the base predicate and a role-less
  variant, which is why the role term is in the design. Every literal resolver call was enumerated;
  four callers besides the role render pass a rendered anchor. The misplaced scan reads the disk,
  not the receipt or the git index, and §4 records why.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "find the installed directory of a sibling kit from the
install receipt when the file was rendered from a template"` ranked `resolve_kit_dir` a SEAM, fan-in
11 with 71 installs. It is the seam this unit extends: its receipt step exists and one predicate
widens, in the canonical and the 70 copies the parity table already holds byte-identical. The role
render's own `derive_harness_paths`, `run_mode` and `build_fixture` in `tools/roles/render_agents.py`
are extended rather than paralleled. The same probe listed `resolve_receipt_path`
(`tools/check-wiring.sh:342`), the awk twin, which S8 corrects in comment only, and
`make_adopter_receipt.py`'s `resolve_kit_homes`, a govkit fixture builder the roles kit cannot import.
`rendered_at` in `tools/lib/render-doc.sh:176-185` is the precedent for joining a rendered row on
`role` and `source`; it keys on the kit id, which the resolver does not have, so it is followed and
not called.

The brief and the code disagree in three places. The repro record says the role render is the only
caller passing a rendered anchor; `tools/codebase-map/map_extractors.py:206` ships one too, and three
selftests pass others (§4). The brief says "a tracked file"; the owner's ruling says "installed", and
§4 row C6 reads the disk. The brief says about 70 copies; the derived count is 70 inline copies and
the canonical. The recall probe returned `TOOL-aRepatriatedFork-2`, the resolver's design;
`TOOL-aMendedFleet-102`, two drifted copies re-synced, which is why AC3 counts distinct blocks;
`TOOL-aRepatriatedFork-4`, harness gates that look where adopters keep harnesses; and
`DEPL-dRemeasuredRender-1`, the rendered row's receipt measure.

The gotchas checklist for the touched paths selected `fixture-passes-by-finding-nothing`, which is
why every criterion's red half was observed or named against `a60b0c7d`;
`staged-break-substitutes-a-synthetic-value`, which is why AC4 and AC5 run the shipped harnesses on a
real install beside the arms' `a.js` stub; `heredoc-escape-reaches-the-regex`, which is why §4 keeps
backslashes out of the block; and `two-answers-to-one-question`, which is why S8 corrects the awk
twin's comment.

Recall terms used: `python tools/memory-recall/query.py "how does the sibling kit resolver find a
rendered file whose receipt row names its template, and how does the role render list harnesses"
--terms "resolve_kit_dir receipt install.json source rendered template harness roles.json
render_agents review-harness renamed kit dir"`
