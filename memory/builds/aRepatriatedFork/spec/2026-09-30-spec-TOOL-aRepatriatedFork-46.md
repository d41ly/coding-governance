# TOOL-aRepatriatedFork-46 — no line joins a literal kit name under a derived base

**Status:** SPECCED · rev-2 · 2026-09-30 · node a · Tier-2 · base 6830f257 · streams tooling · order 16 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-prompt-TOOL-aRepatriatedFork-46-build-brief.md](../prompts/2026-09-30-prompt-TOOL-aRepatriatedFork-46-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-23` §8 F1 ruled (a): a kit's name typed as a literal is the class even under
a derived base, and the owning unit derives the segment. Units 25 to 29 each returned such lines
rather than change code paths their passes could not run. This unit derives them, and fixes the two
places the epoch-5 counter misjudges that class: it counts kit ids and JSON keys as paths, and it
does not see a kit name that follows a brace.

## 2. Scope (IN)

- **S1** — The counter's homonym rule. In rule 4's comma branch, a quoted kit segment counts only
  inside an open path-join call: `join(`, `joinpath(` or `Path(`. A kit id passed as an argument, a
  list member and a JSON key stop counting, and `os.path.join(w, "scripts", "run-gates")` still
  counts. Observed by AC1.
- **S2** — The counter's brace rule. Rule 3 treats a kit segment as drained only after the render
  tokens `{prefix}/`, `{kit}/` and `{{TOOL_ROOT}}`, or the prose tokens `<prefix>/` and
  `<tool-root>/`. Any other brace before a kit name, such as `${PFX}hooks/` or `{PFX}lexicon/`,
  counts. Observed by AC2.
- **S3** — `PREDICATE_EPOCH` moves from 5 to 6, `--rebaseline` runs once, and the gate's epoch
  block records what S1 and S2 cost. Observed by AC3.
- **S4** — Every occurrence of the class at epoch 6 is derived, in engines and suites alike, by the
  rule §4 "Mechanism" states for its shape: the file's own kit, a sibling kit, gov's internal
  library, and a target's kit named by govkit. Observed by AC4, AC5, AC6, AC7.
- **S5** — The runbook's `harness-migration` blocks and `.githooks/gate-env.sh` name no literal kit
  segment. They were returned here by `TOOL-aRepatriatedFork-26` and by the run's rescope entry.
  Observed by AC8.
- **S6** — Every kit whose shipped bytes move takes its version bump in every carrier. Observed by
  AC9.

## 3. Non-goals (OUT)

- Literal-prefix fixtures: a kit segment led by `scripts/`, `vendor/`, `kit/` or gov's own `tools/`
  in a fixture, the frozen adopter receipt and the waiver cells that must match it, the unattended
  kit's rendered fixture playbook and piece records, and `tools/check-install-prefix.test.sh`.
  `TOOL-aRepatriatedFork-28` returned all of them to `TOOL-aRepatriatedFork-30`.
- Deleting the ledger, the waiver registry or either marker. That is `TOOL-aRepatriatedFork-30`.
- A new render token or a new govkit surface for sibling kits (§8 F1).
- `TOOL-aRepatriatedFork-23` and units 25 to 29 are CLOSED. Their returns are this unit's input and
  are cited in §4, not declared as edges a frozen record would have to reciprocate.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-30` — the epoch-6 predicate, which becomes the pure ban's,
  and a ledger holding only the literal-prefix classes listed above.

## 4. Design

### Evidence

Measured at `6830f257` by running the counter's own python source per line, in a scratch probe that
is not committed. It reproduces the ledger exactly: 56 files, 605 lines and 625 occurrences. The
split below is a context heuristic over the 40 characters before each match, so its per-class
figures are PINNED at that sha and UNVERIFIED per line. The build re-derives them.

| Class at epoch 5 | Occurrences | Owner |
|---|---|---|
| kit segment under a derived base | 372 | this unit, less 4 in `tools/check-install-prefix.test.sh` |
| gov's literal `tools/`, in the runbook and `.githooks/gate-env.sh` | 10 | this unit (S5) |
| gov's literal `tools/`, in fixtures and the two workflow scripts | 21 | `TOOL-aRepatriatedFork-30` |
| a foreign literal prefix, the frozen receipt included | 175 | `TOOL-aRepatriatedFork-30` |
| homonyms the S1 rule stops counting | 47 | S1 |

S1, measured before wiring: 47 occurrences drop and none is added. Forty-one are `--kits` argv or
fixture-builder arguments in `tools/govkit/selftest.py`, two are the system directory `'lib'` in
`tools/hooks/scratch-guard.js`, two are JSON `"hooks"` keys in `tools/settings-merge.py`, one is a
deploy `kits` list in `tools/memory-tree/check-memory-hygiene.test.sh` and one is a keyword tuple in
`tools/runlog/selftest.py`. The two `os.path.join` lines in `.githooks/pre_push_bar_selftest.py`
stay counted.

S2, measured the same way: 426 occurrences in 46 files join the count. 29 sit in
`tools/check-install-prefix.test.sh` and go to `TOOL-aRepatriatedFork-30`. They include
`tools/unattended/gate-guard.test.sh` at 62, `tools/govkit/selftest.py` at 41,
`tools/check-kit-versions.sh` at 30 and two in `.githooks/pre-push`. `TOOL-aRepatriatedFork-28` chose
`${PFX}` as its spelling, and the epoch-5 rule read every brace as a render token, so a literal kit
name after it was never counted.

The total this unit derives is about 775 occurrences: 368 and 10 from the table, and 397 from
S2. PINNED at `6830f257`.

### Mechanism

One rule per shape, and every rule reuses a seam that already exists.

- **The file's own kit.** The segment is the file's own directory. A shell file reads it from
  `$HERE` or from `KIT_REL`, which `derive_self_rel` already gives every suite. A Python file reads
  it from `Path(__file__).resolve().parent`, and govkit from `GOVKIT.parent`. A fixture that mirrors
  gov's layout takes that directory's NAME.
- **A sibling kit.** The path comes from `resolve_kit_dir(<home>, <anchor>, <here>)`, the inline
  block `tools/lib/resolve_kit_dir.py` holds canonically and the parity leg gates. It reads the
  install receipt first, so a kit homed under its entry id at an adopter resolves. A shell file runs
  the block through the python it already resolved, the shape `tools/run-gates/run-gates.sh` and
  `tools/unattended/lib-unattended.sh` carry. A fixture takes the resolved directory's NAME.
- **gov's internal library.** `lib` ships nowhere, so a file reaches its contents through the inline
  canonical block, never through a probe of `../lib/`. A suite that sources a file with no parity
  row, `lib-selftest.sh`, resolves it as a sibling kit.
- **A target's kit, named by govkit.** `govkit.py`'s runner probe names the target's `run-gates`
  path through that entry's destination, from the descriptor govkit already loads.
- **The runbook and `gate-env.sh`.** The executed migration blocks locate gov's deployer by its own
  file through `git -C "$GOV" ls-files`, and every other gov path follows from that one answer. The
  three comment lines in `gate-env.sh` take the `<prefix>/` prose token.
- **A literal that only equals a kit name.** `tools/runlog/selftest.py` asserts the runlog state
  directory, which the engine names in `STATE_DIR_NAME`. The suite reads that constant.
- **A kit the resolver cannot reach from where the file sits.** The kickoff kit lives under
  `skills/`, where no resolver probe walks, and gov keeps no receipt. Its suite's flat-reader
  fixture takes the memory-tree kit's name the way `manifest-check.sh` itself finds that kit: the
  resolver anchored at the checker's directory and then at the root, then the one tracked
  `corpus_ids.py`, which is the checker's own last rung. This is the only use of an index lookup.
- **A hook with no extension.** The pre-push hook finds its runner through the resolver under the
  kit root its ladder chose, and a runner miss REFUSES the default bar. It carries both canonical
  blocks, so the resolver self-test's parity population reads `.githooks/` as well.
- **A gov-only suite.** govkit ships nowhere, so its self-test resolves every sibling it names at
  import: a real read goes through the resolved directory, a fixture through its name.
- **The install-prefix gate's own lines.** Its kit-source test finds govkit through the resolver,
  anchored on the engine rather than the registry because the playbook renderer also ships the
  registry, and it carries the python resolver inline. A launcher that does not run is a refusal.

The homonym rule's ceiling is written beside it: a path a callee assembles from separate arguments,
such as `a_evil_target('clean', 'scripts', 'drift-audit')`, is not seen. That is the same blind spot
as a path assembled from two variables, which `TOOL-aRepatriatedFork-30` S6 already names.

### Order of work

The counter changes and the rebaseline land first, in one commit, so the ledger shows the widened
population before any line is derived. Each later commit derives one kit's lines, lowers its rows
through the gate's write mode and bumps that kit's carriers. The flat gates at the tool root share
one commit, since they share one directory, and so do the git hooks with the runbook. A suite whose
lines move records its executed assertion count before and after, the discipline
`TOOL-aRepatriatedFork-28` used.

### Inventory

This unit mints no function. A shell file that needs a sibling kit gains the existing inline
`resolve_kit_dir` block, and the parity leg's population grows by those files.

### Files touched (estimate)

`tools/check-install-prefix.sh` · `tools/install-prefix-carried.txt` ·
`tools/check-install-prefix.test.sh` · `tools/settings-merge.py` · `tools/check-kit-versions.sh` ·
`tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `tools/check-hook-destinations.sh` ·
`tools/check-hook-destinations.test.sh` · `tools/check-playbook-parity.sh` ·
`tools/check-playbook-parity.test.sh` · `tools/check-spec-tokens.test.sh` ·
`tools/check-line-length.test.sh` · `tools/check-testsuite-counts.test.sh` ·
`tools/check-kit-placeholders.test.sh` · `tools/check-agent-cap-restatement.test.sh` ·
`tools/workflows/check-review-join.sh` · `tools/workflows/check-verifier-fanout.sh` ·
`tools/workflows/check-review-join.test.sh` · `tools/workflows/check-verifier-fanout.test.sh` ·
`tools/workflows/unattended-build.test.sh` · `tools/workflows/check-protocol-parity.test.sh` ·
`tools/memory-tree/check-verdict-epoch.sh` · `tools/memory-tree/corpus_ids.py` ·
`tools/memory-tree/gotchas.py` · `tools/memory-tree/merge-rows.test.sh` ·
`tools/memory-tree/marker-contract.test.sh` · `tools/memory-tree/check-verdict-epoch.test.sh` ·
`tools/memory-tree/check-memory-hygiene.test.sh` · `tools/unattended/run-unattended-gates.sh` ·
`tools/unattended/adopt-unattended.sh` · `tools/unattended/gate-guard.test.sh` ·
`tools/unattended/adopt-unattended.test.sh` · `tools/unattended/check-pass-order.test.sh` ·
`tools/unattended/check-playbook.test.sh` · `tools/unattended/check-brief-recorded.test.sh` ·
`tools/unattended/runlog-writer.test.sh` · `tools/unattended/stall-recorder.test.sh` ·
`tools/unattended/stop-guard.test.sh` · `tools/unattended/unattended.test.sh` ·
`tools/codebase-map/map_extractors.py` · `tools/codebase-map/selftest.py` ·
`tools/codebase-map/test_codebase_map.py` · `tools/codebase-map/test_codebase_map.template.py` ·
`tools/codebase-map/adopt-codebase-map.test.sh` · `tools/govkit/govkit.py` ·
`tools/govkit/matrix.py` · `tools/govkit/selftest.py` · `tools/govkit/census.test.sh` ·
`tools/govkit/fixtures/make_adopter_receipt.py` · `tools/hooks/agent-cap.test.sh` ·
`tools/hooks/scratch-guard.test.sh` · `tools/lexicon/selftest.py` · `tools/drift-audit/selftest.py` ·
`tools/memory-recall/selftest.py` · `tools/memory-recall/test_recall_floor.py` ·
`tools/process-monitor/adopt-process-monitor.test.sh` · `tools/run-gates/run-gates.test.sh` ·
`tools/run-gates/run-gates.evidence.test.sh` · `tools/run-gates/run-gates.turnstile.test.sh` ·
`tools/run-gates/run-gates.gov.test.sh` · `tools/run-gates/run-gates.runlog.test.sh` ·
`tools/run-gates/run-selftests.test.sh` · `tools/run-gates/adopt-run-gates.test.sh` ·
`tools/run-gates/profile_bar.test.sh` · `tools/runlog/selftest.py` · `tools/lib/resolve-python.test.sh` ·
`tools/lib/extract-arms.test.sh` · `skills/session-kickoff/manifest-check.test.sh` ·
`.githooks/pre-push` · `.githooks/pre-push.test.sh` · `.githooks/pre-push.runlog.test.sh` ·
`.githooks/gate-env.sh` · `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- A predicate rule that skips a kit segment whose left operand is a variable. The owner rejected it
  as `TOOL-aRepatriatedFork-23` §8 F1 (b): a variable can hold a literal, so the hole looks like a
  pass.
- A `{sibling:<kit>}` render token, which backlog rows `TOOL-aCollapsedScan-11` and
  `TOOL-aScouredKit-26` propose. Engines and suites are not rendered, so it reaches none of these
  lines, and it is a new govkit surface (§8 F1).
- `git ls-files` lookups by anchor file in the suites. It works, but it is a second mechanism beside
  the resolver, and it ignores the receipt.

## 5. Production-readiness checklist

- security — `tools/settings-merge.py` writes `.claude/settings.json`, and the two agent-cap probes
  guard the fan-out cap. Each keeps its refusal when the resolver finds nothing, and never falls
  back to a guessed prefix.
- perf / scale — the resolver reads the receipt once per call, and no engine calls it in a loop.
- error / empty / loading states — `resolve_kit_dir` raises naming the three places it looked, and
  each caller keeps the message it prints today.
- observability — the epoch block records both rule costs, and the acceptance ledger records every
  moved suite's assertion count before and after.
- risks — a suite that passes because a derived path now points at nothing, so an arm skips. AC7
  compares executed counts, not exit codes.
- testing — AC1 to AC9, and the new counter arms in §7.
- migration — the one rebaseline in S3. Adopters receive derived code and bumped versions.
- user docs — the runbook's migration blocks change (S5). No `help/` page describes them.

## 6. Acceptance criteria

- **AC1** — When a scratch clone's fixture file carries `run("plan", "--kits", "memory-tree")`,
  `x = ["bin", "lib"]` and `{"matcher": "a", "hooks": []}`, `bash tools/check-install-prefix.sh
  --list` counts none of them. The same file's `os.path.join(w, "scripts", "run-gates")` stays
  counted. With S1 reverted in the clone, the first three are counted.
  Red when: an argv, list or key is counted, or the path join is not.
- **AC2** — When the same fixture carries `"$ROOT/${PFX}hooks/agent-cap.js"` and a Python
  f-string that spells `{PFX}` directly before the lexicon kit's name, both are counted. The hooks
  path led instead by `{prefix}/`, by `{{TOOL_ROOT}}` or by `<prefix>/` is not. With S2 reverted in
  the clone, the first two are not counted.
  Red when: a brace other than a render token hides a kit name, or a render token is counted.
- **AC3** — When `grep -n '^PREDICATE_EPOCH=' tools/check-install-prefix.sh` runs, it prints 6, the
  ledger's epoch line matches, and a second `--rebaseline` refuses naming the epoch guard.
  Red when: the epoch did not move, or the guard lets a second rebaseline through.
- **AC4** — When `bash tools/check-install-prefix.sh --list` runs on the built tree, no row remains
  for a file whose every occurrence this unit owns. Each remaining row equals that file's
  `TOOL-aRepatriatedFork-30` count, which the acceptance ledger records per file.
  Red when: an owned occurrence remains.
  figure: DERIVED at observation time.
- **AC5** — In a scratch clone whose `hooks` kit is moved to `scripts/agent-cap/` with a matching
  install-receipt row, `bash tools/workflows/check-review-join.sh` and `bash
  tools/workflows/check-verifier-fanout.sh` find the hook through the receipt.
  Red when: either reports no hook while the receipt names one.
  cost: a scratch clone; seconds.
- **AC6** — In the same clone, `python tools/settings-merge.py --selftest` exits 0, and the merged
  fragment paths name `scripts/agent-cap/`.
  Red when: a fragment path names `hooks/`.
- **AC7** — Every suite whose lines this unit moved executes the same assertion count before and
  after, and the unit's acceptance ledger under `memory/builds/aRepatriatedFork/build/` records the
  pair. Red when: any count differs.
  permission: whole suites are the main loop's at VERIFYING; a pass runs the sliced blocks it
  changed and returns the rest as a need.
- **AC8** — When `git grep -nE 'tools/(govkit|unattended|run-gates)/' -- .githooks/gate-env.sh
  WIRE-INTO-PROJECT.md` runs, it finds no line inside a `harness-migration` block and none in
  `gate-env.sh`, and `python tools/govkit/check_runbook_parity.py` exits 0.
  Red when: a literal survives, or the runbook drifts from govkit.
- **AC9** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 6830f257` names no kit this unit moved without its bump.
  Red when: a moved kit's carrier was missed.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `settings-merge selftest` · `review-join ban (no ref-keyed join)` · `review-join self-test` · `tier2-review self-test` · `verifier fan-out` · `verifier fan-out self-test` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `agent-cap self-test` · `scratch-guard self-test` · `check-wiring self-test` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `corpus-ids selftest` · `gotchas selftest` · `row-keyed merge driver replay` · `memory-hygiene self-test` · `marker contracts` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon selftest` · `lexicon naming predicates` · `drift-audit selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `runlog selftest` · `process-monitor adopter selftest` · `unattended-build self-test` · `run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `run-selftests self-test` · `profile-bar selftest` · `pre-push self-test` · `pre-push run-log line` · `manifest-check self-test` · `spec-tokens self-test` · `kit-placeholders self-test` · `agent-cap restatement self-test` · `line-length gate selftest` · `testsuite counts (every bar self-test prints one)` · `testsuite counts self-test` · `extract-arms self-test` · `playbook parity` · `playbook parity selftest` · `dead-path carriers (deleted files still named)` · `encoding posture (text IO names its encoding)` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum`

New arm: `tools/check-install-prefix.test.sh` · a kit id in argv, a list member and a JSON key
beside a path join, each staged against epoch 5 · the suite's floor rises by its new arm count

New arm: `tools/check-install-prefix.test.sh` · `${PFX}<kit>/` and `{PFX}<kit>/` beside the three
render tokens, each staged against epoch 5 · the suite's floor rises by its new arm count

## 8. Open questions

- **F1 — how does a file reach a SIBLING kit's segment?** Option (a): `resolve_kit_dir`, the
  receipt-first resolver the kit-boundary rule in `tools/hooks/README.md` already names for engines,
  applied to suites as well. Option (b): a `{sibling:<kit>}` render token, which reaches rendered
  files only and is a new govkit surface. Option (c): a counter rule that skips a kit segment under
  a variable, which the owner rejected as `TOOL-aRepatriatedFork-23` §8 F1 (b). Option (d): anchor
  lookups through `git ls-files` in suites, with the resolver kept for engines. Recommendation: (a).
  It is one existing, parity-gated seam, it reads the receipt, and it satisfies every criterion.
  RESOLVED (agent, 2026-09-30, delegated): (a). (b) trips M3 veto 2, (c) veto 1, and (d) is a
  second mechanism that ignores a renamed kit.
- **F2 — does this unit close the brace blind spot, S2, or leave it?** Option (a): close it here,
  with epoch 6, and derive the 397 occurrences it makes visible. Option (b): leave it. The pure ban
  `TOOL-aRepatriatedFork-30` builds would then pass with those literals in place, which the owner's
  end state and ruling 23-F1 (a) both exclude. Option (c): park it as a new unit. That leaves an
  open follow-up and needs a minted id. Recommendation: (a).
  RESOLVED (agent, 2026-09-30, delegated): (a), the most feature-rich option and the only one that
  leaves no follow-up. It trips no veto: it widens a gate, not a security or write surface.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, adopted under the unattended protocol §11 from the returns of
  units 25 to 29 and the run's rescope entry of 2026-09-29.
- rev-2 · 2026-09-30 · during the build, before the kits after the review harness: §4 Mechanism
  names four shapes the build met that rev-1 did not, the kickoff suite, the pre-push hook, govkit's
  gov-only self-test and the install-prefix gate's own kit-source test, and §4 Order of work groups
  the tool-root gates and the hooks with the runbook. The install-prefix self-test's source fixtures
  declared a prefixed descriptor home, which govkit reads as kit-relative since
  `TOOL-aRepatriatedFork-29`; the epoch-6 arms build on them, so their homes are repaired.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "locate a sibling kit directory in this install"` ranked
`kit_rel`, `kit_dir` and `resolve_kit_dir`. This unit extends `resolve_kit_dir`, whose canonical
block is `tools/lib/resolve_kit_dir.py`. `python tools/codebase-map/reuse_lookup.py "tell a kit path
from a same-named key or system directory"` found no seam that judges a homonym outside
`tools/check-install-prefix.sh`, which S1 and S2 amend in place. The probe cannot see shell, so the
shell resolver wrappers in `tools/run-gates/run-gates.sh` and `tools/unattended/lib-unattended.sh`
were found by grep and verified against source.

Recall terms used: `sibling kit resolve_kit_dir receipt probe literal segment derived base homonym
render token kit boundary`, with the question "how should a kit reach a sibling kit's file without a
literal kit segment". The hits were `TOOL-aRepatriatedFork-23`'s epoch-5 statement, the returns in
`TOOL-aRepatriatedFork-28` and `TOOL-aRepatriatedFork-29`, and backlog rows `TOOL-aCollapsedScan-11`
and `TOOL-aScouredKit-26`, which propose the render token F1 rejects.
