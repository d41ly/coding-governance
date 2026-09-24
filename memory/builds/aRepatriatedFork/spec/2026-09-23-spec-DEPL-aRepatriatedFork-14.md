# DEPL-aRepatriatedFork-14 — hole probes and descriptors that cannot pass at an adopter

**Status:** CLOSED · rev-2 · 2026-09-24 · node a · Tier-1 · base a7c78ad2 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-DEPL-aRepatriatedFork-14-1-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-14-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-DEPL-aRepatriatedFork-14-build-brief.md](../prompts/2026-09-23-prompt-DEPL-aRepatriatedFork-14-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`govkit check` reports six problems at inCMS and six at nc on 2026-09-23, and four of the twelve are
defects in gov's own descriptors rather than in either tree: a hole probe that reads only a root
`pyproject.toml`, a hole probe that demands a row its own file says should be absent, an entry that
declares neither a check argv nor a reason, and two gate legs that name files gov withholds. This
unit repairs each descriptor and gates each CLASS in `selfcheck`, so the next descriptor carrying
the same defect reds in gov instead of at an adopter. Tier-1: every change is a descriptor row, a
probe string or a `selfcheck` arm, with no new write path, no sanitiser and no shared-contract
change.

## 2. Scope (IN)

- **S1** — `pytest-ini-knobs` READS WHERE THE CONFIG IS. The probe at
  `tools/pytest-parallel-guardrails/kit.toml:53` loads `pyproject.toml` at the repo root only. It
  becomes a probe over every tracked `pyproject.toml` whose `[tool.pytest.ini_options]` table
  exists, requiring at least one and requiring every one found to satisfy the unchanged knob rule.
  Zero found exits 1 with a line saying no pytest configuration is tracked, so an absent config
  never reads as a sized one. Observed by AC1, AC2.
- **S2** — THE `stale-header-waiver` HOLE IS RETIRED. Its probe at `tools/memory-tree/kit.toml:306`
  passes only when the waiver file holds a non-comment row, while the hole's own `why` at `:305`
  and the file's header both say an empty file is the expected state. The one state the hole could
  meaningfully detect, a MISSING file, is already a refusal of `gen_build_index.py --check`
  (`gen_build_index.py:716-722`), which hygiene check 9 runs on every bar. Observed by AC3.
  **Readers:** by name: `tools/memory-tree/kit.toml` declares the hole id, and the sibling unit 13's
  S5 names it for a stand-down. by value: `tools/govkit/govkit.py` reads every hole's probe
  generically in `cmd_check` and `exempt_leg`; no reader keys on this hole's value.
- **S3** — `check-testsuite-counts` DECLARES ITS ABSENCE.
  `tools/govkit/entries/check-testsuite-counts.kit.toml` gains `[check] none = "…"` stating that its
  gate leg is the check. `selfcheck` gains an arm that refuses any descriptor declaring neither
  `[check].argv` nor `[check].none`, which today only `govkit check` reports, per target and after
  the install (`govkit.py:3673-3676`). Observed by AC4, AC5.
- **S4** — `process-monitor`'s TWO SELF-TEST LEGS LEAVE ITS DESCRIPTOR. The legs at
  `tools/process-monitor/kit.toml:38-48` run `selftest.py` and `adopt-process-monitor.test.sh`,
  which the same descriptor withholds with `role = "project-owned"` (`kit.toml:26-32`). They move
  to `[[exempt_leg]]` rows in `tools/govkit/registry.toml`, worded like the siblings that took the
  same move under `TOOL-aQuenchedHarness-3`, and stay legs on gov's bar. `selfcheck` gains an arm
  refusing a descriptor `[[gate_leg]]` whose argv names a path a `project-owned` rule in the same
  descriptor withholds. Observed by AC6, AC7.
- **S5** — `kit-versions-need-list` SAYS WHAT ITS PROBE MEASURES. Its probe is the gate itself,
  `bash {prefix}/check-kit-versions.sh` (`check-kit-versions.kit.toml:31`), so it reds on ANY
  kit-versions finding and not only on an unedited need list. The hole's `why` gains that sentence.
  The probe is unchanged, and at inCMS it discharges once `TOOL-aRepatriatedFork-15` bumps the two
  kits whose bytes moved without their version. Observed by AC8.

## 3. Non-goals (OUT)

- The merged `pyproject-snippet.toml` rule's `to = "pyproject.toml"`
  (`tools/pytest-parallel-guardrails/kit.toml:35-40`). `merged` has no writer yet
  (`govkit.py:249`), so the destination lands nothing anywhere and S1 is about the probe only.
- Re-selecting `pytest-parallel-guardrails` at nc. nc deselected it because nc tracks no pytest
  configuration at all, and S1 keeps that state undischarged, correctly.
- nc's three lexicon findings from the same `govkit check` run. They are about nc's pins and its
  lexicon adopter's exit, not about a descriptor.
- `check-testsuite-counts.sh` hardcoding `tools/gate-legs.json` at `:27`. That is the prefix class
  `TOOL-aRepatriatedFork-2` owns.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-15` — the version bumps that make inCMS's kit-versions
  gate green on an update branch. Without them AC8 cannot be observed and the need-list hole stays
  red at inCMS for a reason that is not its own.
- **consumes-from** `DEPL-aRepatriatedFork-13` — the `stale-header-waiver` hole's fate, which that
  unit leaves here. If the owner keeps the hole rather than taking S2, that unit's S5 stand-down is
  what quiets it at inCMS.

## 4. Design

### Evidence, measured at a7c78ad2 on 2026-09-23

`python tools/govkit/govkit.py check --target <tree>`, read-only:

| Problem | inCMS | nc | Owner |
|---|---|---|---|
| `kit-versions-need-list` UNDISCHARGED | exit 1 | discharged | S5, then `TOOL-aRepatriatedFork-15` |
| `check-testsuite-counts` declares neither | yes | yes | S3 |
| `measured-pins` UNDISCHARGED | exit 1 | discharged | `DEPL-aRepatriatedFork-13` |
| `stale-header-waiver` UNDISCHARGED | exit 2, file absent | exit 1, header only | S2 |
| `playbook-placeholders` UNDISCHARGED | exit 1 | exit 1 | `DEPL-aRepatriatedFork-1` |
| `pytest-ini-knobs` UNDISCHARGED | exit 1 | kit deselected | S1 |
| lexicon adopter and two lexicon holes | none | three problems | out of scope |

Every cell is PINNED from those two runs. The S1 probe, run by hand from inCMS's `services/api/`
directory against its own `pyproject.toml`, exits 0: every knob is present and sized, with
`faulthandler_timeout = 240` under `timeout = 300`. `govkit plan` at inCMS prints two `SILENT` rows
for the S4 legs, naming `scripts/process-monitor/selftest.py` and
`scripts/process-monitor/adopt-process-monitor.test.sh`, which neither adopter tracks.

`selfcheck`'s bare-target arm (`govkit.py:2090-2105`) never flagged S4 because it counts an `order`
row as a file some rule produces, and `project-owned` is `order` in `ROLE_KINDS`
(`govkit.py:2448`). At a real target that row produces nothing.

### Data model

S1's probe, as the descriptor string would carry it, reformatted here:

```python
import subprocess, sys, tomllib
out = [f for f in subprocess.run(["git", "ls-files", "-z", "--", "*pyproject.toml"],
                                 capture_output=True, text=True,
                                 encoding="utf-8").stdout.split(chr(0)) if f]
inis = []
for f in out:
    t = tomllib.load(open(f, "rb")).get("tool", {}).get("pytest", {}).get("ini_options")
    if t is not None:
        inis.append((f, t))
need = ("timeout", "timeout_method", "session_timeout", "faulthandler_timeout")
ok = lambda i: (all(k in i for k in need) and "--max-worker-restart=0" in str(i.get("addopts", ""))
                and int(i["faulthandler_timeout"]) < int(i["timeout"]))
if not inis:
    sys.exit("no tracked pyproject.toml carries [tool.pytest.ini_options]")
sys.exit(0 if all(ok(i) for _f, i in inis) else 1)
```

### Inventory

No function is minted in govkit's module surface. The two `selfcheck` arms are inline blocks in
`selfcheck()`, as its existing arms are, numbered 7j2 (S3) and 7j3 (S4). `selftest.py` gains
`check_pytest_ini_probe` for AC2.

### Files touched (estimate)

`tools/pytest-parallel-guardrails/kit.toml` · `tools/memory-tree/kit.toml` ·
`tools/govkit/entries/check-testsuite-counts.kit.toml` ·
`tools/govkit/entries/check-kit-versions.kit.toml` ·
`tools/process-monitor/kit.toml` · `tools/govkit/registry.toml` · `tools/govkit/govkit.py` ·
`tools/govkit/selftest.py` · `tools/pytest-parallel-guardrails/README.md` · and, because the
epoch rule grades shipped bytes, the version carriers of `pytest-parallel-guardrails` (1.0 to 1.1),
`process-monitor` (0.4 to 0.5) and `memory-tree` (2.90 to 2.91)

### Adopter deletions this unit enables

Neither adopter forked these descriptors, so nothing is deleted from either tree. What moves is
`govkit check`'s problem count: at inCMS, three of the six clear on this unit alone. nc's
deselection of `pytest-parallel-guardrails`, recorded at lines 151-156 of nc's deploy descriptor, stays
correct, because nc tracks no pytest configuration.

### Alternatives rejected

- An answer key naming the pytest config path. Deriving the population from `git ls-files` needs no
  intake question and cannot name a path that is not there.
- Rewording the `stale-header-waiver` probe to test existence. It would duplicate the generator's
  own refusal as a second observer of one fact, which is the class `DEPL-aRepatriatedFork-13` S5
  already has to reason around.
- Moving the process-monitor suites into the shipped set. The 2026-08-23 owner ruling withholds
  self-tests whose subject is the kit's own checker, and the sibling suites in `registry.toml`'s
  `[[exempt_leg]]` rows already follow it.

## 5. Production-readiness checklist

- security — S1's probe spawns `git ls-files` from a gov-authored argv with no target-supplied
  token, and reads TOML with `tomllib`.
- perf / scale — one `git ls-files` and one TOML parse per tracked `pyproject.toml`.
- error / empty / loading states — S1 states zero configs found. A malformed TOML file raises, and
  the probe exits non-zero, which reads as undischarged, correctly.
- observability — the two new `selfcheck` arms name the entry, the leg or the key they refuse.
- risks — S2 retires a hole two adopters see as red today, so the only risk is losing an observer,
  and the generator's refusal is that observer.
- testing — each `selfcheck` arm is observed RED on a fixture descriptor before it lands.
- migration — none. Descriptors change; receipts and deploy files do not.
- user docs — `tools/pytest-parallel-guardrails/README.md` states where the probe looks.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py check --target <inCMS worktree>` runs after S1, no
  line reports `pytest-ini-knobs`.
  Red when: the probe still reads only a root file.
  cost: a full read-only `check`, about two minutes.
- **AC2** — When a `govkit selftest` fixture tracks two `pyproject.toml` files with pytest tables and
  one lacks `faulthandler_timeout`, the hole reports UNDISCHARGED; with no pytest table anywhere it
  reports UNDISCHARGED with the no-configuration line.
  Red when: one sized file hides an unsized one, or an absent config discharges.
- **AC3** — When `govkit check` runs at either adopter after S2, no line names `stale-header-waiver`,
  and a fixture whose waiver file is missing still fails hygiene check 9 through
  `gen_build_index.py --check`.
  Red when: the retirement also retires the missing-file refusal.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs with a fixture descriptor declaring
  no `[check]` table, it exits 1 naming the entry; the arm is observed RED against a7c78ad2's
  descriptors before S3 lands, because `check-testsuite-counts` trips it.
  Red when: the arm passes on the unrepaired tree, so it arms nothing.
- **AC5** — When `govkit check` runs at either adopter after S3, no line says `declares neither`.
  Red when: the reason was added somewhere `run_kit_check` does not read.
- **AC6** — When `python tools/govkit/govkit.py plan --target <inCMS worktree>` runs after S4, it
  prints no `SILENT` row.
  Red when: either process-monitor self-test is still a descriptor leg.
- **AC7** — When `selfcheck` runs on a fixture descriptor with a `[[gate_leg]]` naming a file its
  own `project-owned` rule withholds, it exits 1 naming the leg and the path; the arm is observed
  RED against a7c78ad2's `process-monitor` descriptor before S4 lands.
  Red when: the class is left to `silenced_legs` at a target.
- **AC8** — When `grep -c 'any kit-versions finding' tools/govkit/entries/check-kit-versions.kit.toml`
  runs after S5 it prints 1, and after `TOOL-aRepatriatedFork-15` lands, `govkit check` at an inCMS
  update branch reports no `kit-versions-need-list` line.
  Red when: the hole still reads as a need-list observation only.
  permission: the second half needs an inCMS update branch after that unit lands, which this run cannot create.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `pytest-guardrails self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/govkit/selftest.py` · a descriptor with no `[check]` table, and one whose leg names a withheld file · none
New arm: `tools/govkit/selftest.py` · two pytest fixtures for S1, one unsized and one absent · none

## 8. Open questions

- **F1 — retire `stale-header-waiver`, or keep it with an existence probe?** Recommendation: retire,
  per S2. The generator already refuses the missing file on every bar, and a second observer of one
  fact is how the two drift apart.
  RESOLVED (owner, 2026-09-23): retire `stale-header-waiver`, per S2, as recommended.
- **F2 — should S1 also read `pytest.ini`, `setup.cfg` and `tox.ini`?** Recommendation: not now. The
  kit ships a `pyproject.toml` snippet and every adopter measured uses that file. Widen it when an
  adopter configures pytest elsewhere.
  RESOLVED (owner, 2026-09-23): not now; widen when an adopter configures pytest elsewhere, as
  recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, grounded at a7c78ad2 on read-only `govkit check` and
  `govkit plan` runs at both adopters on 2026-09-23.
- rev-2 · 2026-09-24 · build-time divergences. Section 4 data model: the S1 probe lists paths with
  `git ls-files -z` and splits on NUL, so a path with a space or a quoted non-ASCII name is read
  whole. Section 4 Inventory names the arms 7j2 and 7j3 and the `selftest.py` function. Section 4
  Files touched adds the three version bumps the epoch rule owes. AC2's no-configuration line is the
  probe's own stderr, which `check` does not print, so AC2 is observed through `check` for the verdict
  and by running the descriptor's probe for the line.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a hole discharge probe that reads a subproject config"`
ranked `read_text` and the per-kit `read` helpers, none of which a descriptor probe can import. No
existing seam fits as a mapped symbol. The live seams are reused as they stand: the
`[[exempt_leg]]` registry table and its `selfcheck` arm at `govkit.py:1836-1869` for S4, and
`run_kit_check`'s existing `declares neither` refusal, lifted into `selfcheck` for S3.

Recall terms used: `hole discharge probe pytest ini_options pyproject stale-header-waiver
exempt_leg project-owned silenced_legs selfcheck check none`.
