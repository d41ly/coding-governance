# Hard-coded kit-prefix census — shipped files

**Serves:** research TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30

Read-only census of worktree `arepatriated-fork-build-e42158` at HEAD `2143b6d6`, taken 2026-09-25.
No gate suite or test suite was run. The one gate invocation was `bash tools/check-install-prefix.sh --list`.

Working files are under `scratchpad/pcensus/`, and every count below comes from one of them:

- `list.txt` is the gate's `--list` output.
- `shipped.tsv` is `govkit.py shipped` (291 rows).
- `occ.tsv` holds the 904 carried occurrences with line numbers.
- `classified.tsv` holds the per-occurrence class.
- `invisible.tsv` holds the literals no arm counts.
- The scripts are `extract.py`, `classify.py`, `invisible.py` and `bucket.py`.

## 0. How the population was measured

- **Arm 2 (carried ban, `tools/<kit>/<file>` spelling).** `extract.py` re-implements the gate's epoch-4 `re_ship` predicate, including the loose-file existence filter. It enumerated **904 occurrences over 139 files**. Every per-file count equals `tools/install-prefix-carried.txt` exactly, with zero mismatches. The live `--list` rows also equal the pinned file byte-for-byte after the reason column is dropped.
- **Arm 1 (root spelling, `<kit>/<file>`).** 43 hit lines: 11 waived and 32 marked `gov:root-fixture`.
- **Arm 3 (runtime literals, engine/rendered code, `gov:prefix-literal`).** 24 hit lines, all marked. 8 of them are also counted by arm 2, so 16 are arm-3-only.
- **Classification.** Rules come first: `.md` is C, the `# >>> … canonical copy:` line is E, a test with a usage shape is B, other test lines are D, and comments are G. **53 per-site overrides** follow, each set after reading the line and its context. They are listed in `classify.py`. Zero sites are left unclassified.
- "Withheld" means the file's descriptor role is `project-owned`, so `govkit apply` does not write it. A copy-installer who runs `cp -r <gov>/tools/<kit>` still receives it unless they follow WIRE's removal step.

## 1. Counts per class — arm 2 (the 904 carried literals)

| Class | Literals | Files | in received files | in withheld files |
|---|---|---|---|---|
| A EXECUTES | 6 | 2 | 6 | 0 |
| B PRINTS / usage | 93 | 56 | 80 | 13 |
| C RENDERED DOC | 112 | 18 | 112 | 0 |
| D FIXTURE-INTERNAL | 179 | 27 | 54 | 125 |
| E BYTE-PINNED MARKER | 24 | 22 | 20 | 4 |
| F GOV-SIDE ONLY | 362 | 16 | 125 | 237 |
| G COMMENT PROSE | 128 | 74 | 104 | 24 |
| **Total** | **904** | 139 distinct | 601 | 303 |

These rows sum to 904. The file counts overlap because one file can hold several classes.

**Drainable (A+B+C+E+G) = 363. Correct as literals (D+F) = 541.** The ratchet's headline of 904 therefore overstates the drain by 60%.

### Arm 1 (43 root-spelling hit lines)

| Class | Lines | Sites |
|---|---|---|
| A strands | 1 | `.githooks/pre-commit:48` (waived; the same line as the arm-2 A) |
| A-fallback | 4 | `tools/check-wiring.sh:496, 547, 770, 780` (waived; a receipt rung and a `KIT_REL` rung precede each one) |
| B | 1 | `tools/codebase-map/map_lib.py:1493` `REGEN_CMD` legacy (waived; the remedy text read by pre-1.1 adopter gate files) |
| C | 2 | `tools/memory-tree/README.md:117` (waived), `tools/codebase-map/.codebase-map.conf.example:28` (marked; `adopt-codebase-map.sh` restamps it per prefix) |
| D | 31 | every other `gov:root-fixture` marker (the check-install-prefix, check-wiring, adopt-codebase-map, codebase-map selftest, drift-audit selftest, agent-cap, adopt-unattended, unattended and unattended-build suites), plus `corpus_ids.py:967, 971` (waived) |
| G | 4 | `gen_map.py:47` and `adopt-codebase-map.sh:155` (both waived), `adopt-codebase-map.test.sh:164` and `codebase-map/selftest.py:382` (both marked "quoting the defect") |

### Arm 3 (24 `gov:prefix-literal` lines)

| Class | Lines | Sites |
|---|---|---|
| A strands | 1 | `.githooks/pre-push:367` |
| A-fallback | 1 | `skills/session-kickoff/manifest-check.sh:426` |
| D | 7 | `corpus_ids.py:966, 977, 978`, `gotchas.py:521, 523, 525, 526` |
| F | 5 | `check-install-prefix.sh:100, 102, 155` (the kit-source test), `render_playbook.py:384, 385` (`gov_root`) |
| not a prefix literal | 10 | 4 homonyms: `map_diff.py:188` and `reuse_lookup.py:752` (sidecars under the git dir), `render_playbook.py:185` (`.github/workflows`), `runlog/extract.py:252` (a transcript `workflows` dir). 6 kit segments joined under an already-DERIVED base: `test_codebase_map.template.py:65`, `corpus_ids.py:88`, `settings-merge.py:554, 580, 634, 635` |

### What the gate cannot see

- **1098** candidate occurrences of `tools/<tracked-kit-or-loose-name>`, or of a quoted `"tools"` join, sit in the shipped population with no arm counting them. This uses the broad regex in `invisible.py`.
- **168** of those are inside `install-prefix-carried.txt` itself, which is excluded by design.
- That leaves **930**. Of these, **514** are in withheld files and **416** are in received files: 154 in tests, 72 in `.md`, 54 in comments, and 136 on other lines, including docstrings and data.
- The misses have four causes: a `/` lead (`$ROOT/tools/…`, `<project>/tools/…`, `<gov>/tools/…`), a directory-only reference, a fixture loose name that the existence filter drops, and test or seed files that arm 3's population excludes.
- **Files no descriptor resolves:** 57 tracked files under `tools/ skills/ .githooks/ *.template.*` are absent from `govkit shipped`. They hold 562 literals under the arm-2 predicate.
  - 51 files (544 literals) are covered by a registry `[[exempt]]` path. Those are `tools/govkit`, `tools/lib`, gov's own gates and sidecars, `.githooks/gate-env.sh` and `.githooks/pre-commit.test.sh`.
  - 6 are not exempt: `skills/deploy-governance/SKILL.md` (7, gov-side), `tools/unattended/playbook.fixture.md` (2), and `tools/workflows/{unattended-build,tier2-review,drift-audit-state,drift-audit-code}.js` (5/3/1/0). The last four are gov's own renders of shipped `{{TOOL_ROOT}}`/`{{KIT_DIR}}` templates, so they are correct at gov's prefix.

## 2. Class A — every site (all arms plus invisible)

**Strands an adopter (12 sites, 16 literals):**

- `.githooks/pre-commit:48` — `tools/memory-tree/check-memory-hygiene.sh` (arm 2) + `memory-tree/check-memory-hygiene.sh` (arm 1, waived) — `gate_at` probes only gov's prefix and the root, so at `scripts/` or `vendor/gov/` the staged hygiene leg is skipped silently and the hook exits 0.
- `.githooks/pre-commit:54` — `tools/manifest-check.sh` (+ `scripts/manifest-check.sh`) — a fixed candidate list, so at any other prefix the kickoff-manifest staged leg skips silently. **Invisible:** that loose file does not exist in gov, so the epoch-2 existence filter drops it, and `scripts/` is not a `tools/` spelling.
- `.githooks/pre-push:367` — `$top/tools/gate-legs.json`, `$top/tools/run-gates` (+ `:368` `scripts/…`) — `GOV_KITROOT` can only ever be `tools` or `scripts`. At a root or `vendor/gov/` install, `GATE_RUNNER` (:374) and the default bar (:835) name `tools/run-gates/run-gates.sh`, which does not exist. Arm 3 sees it but it is marked. The marker says it "falls back to the derived prefix below", but the only fallback is the literal `scripts`.
- `tools/unattended/.unattended.conf.example:268` ×2 — `tools/memory-tree/gen_build_index.py` — `GENERATED_INDEXES` is not REPLACE-marked and the kit says it is copied verbatim. `unattended.sh:5742` uses the generator half as the overlap key for the condition-3 refusal. At another prefix the key never matches the real generator path, so the refusal cannot fire. The driver's own comment at :330 says the kit "may not presume" that path.
- `tools/unattended/.unattended.conf.example:18` — `tools/push-main.sh` — the `LANDER` the driver executes. It is REPLACE-marked, so it strands only an adopter who keeps the default.
- `tools/unattended/.unattended.conf.example:25` — `tools/run-gates/run-gates.sh` — `GATE_CMD`, executed for the `gates-green` DoD item. REPLACE-marked, same caveat.
- `tools/unattended/.unattended.conf.example:71` — `tools/check-wiring.sh` — `WIRING_CHECK`, the command `--preflight` delegates to. REPLACE-marked, same caveat.
- `tools/check-microformats.test.sh:11` — `$ROOT/tools/check-microformats.sh` (`ROOT=$HERE/..`) — a received suite. At any other prefix `GATE` names nothing and every arm fails to reach the gate. **Invisible:** `/` lead, and a test suffix is outside arm 3.
- `tools/check-placeholders.test.sh:14` — `$ROOT/tools/check-placeholders.sh` — same failure as the entry above. **Invisible.**
- `tools/check-wiring.test.sh:823` — `$REPO/tools/memory-tree/README.md` / `$REPO/memory-tree/README.md` — at `scripts/` the AC12 README arms SKIP with the false reason "the memory-tree kit README is not installed in this repo". **Invisible.**
- `tools/codebase-map/selftest.py:1613` — `m.repo_root() / "tools" / "lexicon"` — withheld, but `cp -r` installers receive it. At incms, whose lexicon sits at `scripts/lexicon/`, the arm skips with a false reason. This is backlog TOOL-aProbedToolkit-3's second site and is still open. **Invisible:** a P2-shaped join in a test, outside arm 3's population.
- `tools/govkit/govkit.py:5415` — `for prefix in ("tools", ""):` — the AC8 foreign-kit refusal (`foreign_kit_present`) probes a target only at gov's prefix and at the root, so a foreign install at `scripts/` is not detected. This is gov-internal code (a `tools/govkit` registry exemption) and outside every arm by construction. The two kit.toml `sentinel =` lines feed the same probe; they are counted as F.

**A-fallback (executes, but a derived rung precedes it, so it cannot strand; 6 sites):** `tools/check-wiring.sh:496, 547, 770, 780`, `skills/session-kickoff/manifest-check.sh:426` and `tools/playbook/render_playbook.py:204`. The last one is invisible, and its candidates name adopter-owned gate scripts rather than kit files.

**Withheld suites that run against the host tree:** a grep for `$ROOT/tools/…`, `ROOT / "tools"` and similar found 45 more lines in project-owned files. Examples are `run-gates.evidence.test.sh:20`, `run-selftests.test.sh:24/26/47`, `merge-rows.test.sh:47/1212`, `agent-cap.test.sh:1170`, `memory-recall/selftest.py:1093`, `map_extractors.py:46/93/101/159/192/212/213` and `unattended-build.test.sh:299/304`. They are correct in gov and are F by descriptor. They become A only for a copy-installer who skips WIRE's removal step.

## 3. Class B — every site (93)

Four are PRINTED at run time: merge-rows.py:8 (both literals), derive-ceilings.py:4 and map_extractors.py:253. Every other B site is read in source. Every printed `usage:` line in these files is already derived from `$0`, `basename` or `$SELF`.

- tools/check-agent-cap-restatement.sh:9 — tools/check-agent-cap-restatement.sh — usage header in source (comment or docstring, not printed)
- tools/check-install-prefix.sh:4 — tools/check-install-prefix.sh — usage header in source (comment or docstring, not printed)
- tools/check-install-prefix.sh:5 — tools/check-install-prefix.sh — usage header in source (comment or docstring, not printed)
- tools/check-install-prefix.sh:6 — tools/check-install-prefix.sh — usage header in source (comment or docstring, not printed)
- tools/check-install-prefix.test.sh:4 — tools/check-install-prefix.test.sh — usage header in source (comment or docstring, not printed)
- tools/check-line-length.sh:4 — tools/check-line-length.sh — usage header in source (comment or docstring, not printed)
- tools/check-line-length.sh:5 — tools/check-line-length.sh — usage header in source (comment or docstring, not printed)
- tools/check-line-length.sh:6 — tools/check-line-length.sh — usage header in source (comment or docstring, not printed)
- tools/check-microformats.sh:4 — tools/check-microformats.sh — usage header in source (comment or docstring, not printed)
- tools/check-placeholders.sh:4 — tools/check-placeholders.sh — usage header in source (comment or docstring, not printed)
- tools/check-placeholders.sh:5 — tools/check-placeholders.sh — usage header in source (comment or docstring, not printed)
- tools/check-testsuite-counts.sh:5 — tools/check-testsuite-counts.sh — usage header in source (comment or docstring, not printed)
- tools/check-testsuite-counts.test.sh:6 — tools/check-testsuite-counts.test.sh — usage header in source (comment or docstring, not printed)
- tools/check-wiring.test.sh:3 — tools/check-wiring.test.sh — usage header in source (comment or docstring, not printed)
- tools/codebase-map/adopt-codebase-map.test.sh:4 — tools/codebase-map/adopt-codebase-map.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/codebase-map/map_extractors.py:253 — tools/codebase-map/INVENTORY-DERIVATION.md — PRINTED in the MapError an empty EXTRACTORS raises; the doc it points at is under gov's prefix [withheld]
- tools/drift-audit/adopt-drift-audit.sh:10 — tools/drift-audit/adopt-drift-audit.sh — usage header in source (comment or docstring, not printed)
- tools/drift-audit/adopt-drift-audit.sh:11 — tools/drift-audit/adopt-drift-audit.sh — usage header in source (comment or docstring, not printed)
- tools/drift-audit/drift_report.py:6 — tools/drift-audit/drift_report.py — usage header in source (comment or docstring, not printed)
- tools/drift-audit/drift_report.py:7 — tools/drift-audit/drift_report.py — usage header in source (comment or docstring, not printed)
- tools/drift-audit/drift_report.py:8 — tools/drift-audit/drift_report.py — usage header in source (comment or docstring, not printed)
- tools/drift-audit/drift_signals.template.py:5 — tools/drift-audit/drift_signals.template.py — instructions inside the adopter's own seeded drift_signals.py: the command it tells them to run is at gov's prefix
- tools/drift-audit/drift_signals.template.py:6 — tools/drift-audit/drift_report.py — instructions inside the adopter's own seeded drift_signals.py: the command it tells them to run is at gov's prefix
- tools/gate-lint/ps-hygiene.py:4 — tools/gate-lint/ps-hygiene.py — usage header in source (comment or docstring, not printed)
- tools/hooks/agent-cap.js:52 — tools/settings-merge.py — the per-project wiring instruction names settings-merge.py at gov's prefix
- tools/hooks/scratch-guard.test.sh:3 — tools/hooks/scratch-guard.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/lexicon/adopt-lexicon.sh:4 — tools/lexicon/adopt-lexicon.sh — usage header in source (comment or docstring, not printed)
- tools/lexicon/adopt-lexicon.sh:5 — tools/lexicon/adopt-lexicon.sh — usage header in source (comment or docstring, not printed)
- tools/lexicon/selftest.py:4 — tools/lexicon/selftest.py — usage header in source (comment or docstring, not printed) [withheld]
- tools/memory-recall/adopt-memory-recall.sh:4 — tools/memory-recall/adopt-memory-recall.sh — usage header in source (comment or docstring, not printed)
- tools/memory-recall/adopt-memory-recall.sh:5 — tools/memory-recall/adopt-memory-recall.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/adopt-memory-tree.sh:6 — tools/memory-tree/adopt-memory-tree.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-arms.py:4 — tools/memory-tree/check-arms.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-arms.py:5 — tools/memory-tree/check-arms.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-arms.py:6 — tools/memory-tree/check-arms.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-arms.py:8 — tools/memory-tree/check-arms.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-memory-hygiene.sh:8 — tools/memory-tree/check-memory-hygiene.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-memory-hygiene.sh:9 — tools/memory-tree/check-memory-hygiene.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-method-carriers.sh:5 — tools/memory-tree/check-method-carriers.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-method-carriers.test.sh:4 — tools/memory-tree/check-method-carriers.test.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/check-verdict-epoch.sh:4 — tools/memory-tree/check-verdict-epoch.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gen_build_index.py:4 — tools/memory-tree/gen_build_index.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gen_build_index.py:5 — tools/memory-tree/gen_build_index.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gen_build_index.py:6 — tools/memory-tree/gen_build_index.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gen_build_index.py:7 — tools/memory-tree/gen_build_index.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gen_build_index.py:8 — tools/memory-tree/gen_build_index.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:4 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:5 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:6 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:7 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:8 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:9 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/gotchas.py:10 — tools/memory-tree/gotchas.py — usage header in source (comment or docstring, not printed)
- tools/memory-tree/hygiene-parity.test.sh:8 — tools/memory-tree/hygiene-parity.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/memory-tree/kit-dogfood-parity.test.sh:5 — tools/memory-tree/kit-dogfood-parity.test.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/kit-dogfood-parity.test.sh:6 — tools/memory-tree/kit-dogfood-parity.test.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/marker-contract.test.sh:11 — tools/memory-tree/marker-contract.test.sh — usage header in source (comment or docstring, not printed)
- tools/memory-tree/merge-rows.py:8 — tools/lib/pyrun.sh — PRINTED by main() when run with no args (first two docstring paragraphs); also names tools/lib/pyrun.sh, which ships to no adopter at any prefix
- tools/memory-tree/merge-rows.py:8 — tools/memory-tree/merge-rows.py — PRINTED by main() when run with no args (first two docstring paragraphs); also names tools/lib/pyrun.sh, which ships to no adopter at any prefix
- tools/memory-tree/merge-rows.test.sh:29 — tools/memory-tree/merge-rows.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/playbook/adopt-playbook.sh:4 — tools/playbook/adopt-playbook.sh — usage header in source (comment or docstring, not printed)
- tools/playbook/adopt-playbook.sh:5 — tools/playbook/adopt-playbook.sh — usage header in source (comment or docstring, not printed)
- tools/playbook/adopt-playbook.sh:6 — tools/playbook/adopt-playbook.sh — usage header in source (comment or docstring, not printed)
- tools/process-monitor/adopt-process-monitor.sh:10 — tools/process-monitor/adopt-process-monitor.sh — usage header in source (comment or docstring, not printed)
- tools/process-monitor/adopt-process-monitor.sh:11 — tools/process-monitor/adopt-process-monitor.sh — usage header in source (comment or docstring, not printed)
- tools/process-monitor/adopt-process-monitor.test.sh:10 — tools/process-monitor/adopt-process-monitor.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/run-gates/derive-ceilings.py:4 — tools/gate-legs.json — PRINTED by --help (argparse description=__doc__); names the leg manifest at gov's prefix
- tools/settings-merge.py:24 — tools/settings-merge.py — usage header in source (comment or docstring, not printed)
- tools/settings-merge.py:25 — tools/settings-merge.py — usage header in source (comment or docstring, not printed)
- tools/unattended/adopt-unattended.sh:4 — tools/unattended/adopt-unattended.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/adopt-unattended.sh:5 — tools/unattended/adopt-unattended.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/adopt-unattended.test.sh:4 — tools/unattended/adopt-unattended.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/unattended/check-brief-recorded.sh:6 — tools/unattended/check-brief-recorded.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/check-pass-order.sh:5 — tools/unattended/check-pass-order.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/check-unattended.sh:10 — tools/unattended/check-unattended.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/check-unattended.test.sh:6 — tools/unattended/check-unattended.test.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/gate-guard.test.sh:4 — tools/unattended/gate-guard.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/unattended/kit.toml:201 — tools/unattended/run-unattended-gates.sh — the kit's compensating-check command, stated in its descriptor at gov's prefix
- tools/unattended/kit.toml:202 — tools/unattended/run-unattended-gates.sh — the kit's compensating-check command, stated in its descriptor at gov's prefix
- tools/unattended/resume-tick.test.sh:4 — tools/unattended/resume-tick.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/unattended/run-unattended-gates.sh:253 — tools/unattended/run-unattended-gates.sh — usage header in source (comment or docstring, not printed)
- tools/unattended/stall-recorder.test.sh:4 — tools/unattended/stall-recorder.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/unattended/stop-guard.test.sh:4 — tools/unattended/stop-guard.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/unattended/unattended.test.sh:7 — tools/unattended/unattended.test.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-protocol-parity.test.sh:5 — tools/workflows/check-protocol-parity.test.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-protocol-parity.test.sh:6 — tools/workflows/check-protocol-parity.test.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-review-join.sh:4 — tools/workflows/check-review-join.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-review-join.sh:5 — tools/workflows/check-review-join.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-review-join.test.sh:5 — tools/workflows/check-review-join.test.sh — usage header in source (comment or docstring, not printed) [withheld]
- tools/workflows/check-verifier-fanout.sh:9 — tools/workflows/check-verifier-fanout.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-verifier-fanout.sh:10 — tools/workflows/check-verifier-fanout.sh — usage header in source (comment or docstring, not printed)
- tools/workflows/check-workflow-syntax.js:4 — tools/workflows/check-workflow-syntax.js — usage header in source (comment or docstring, not printed)
- tools/workflows/check-workflow-syntax.js:5 — tools/workflows/check-workflow-syntax.js — usage header in source (comment or docstring, not printed)

## 4. Classes C–G — per-file counts (arm 2)

**C RENDERED DOC (112 literals, 18 files):**

- WIRE-INTO-PROJECT.md 52
- tools/lexicon/README.md 10
- tools/memory-recall/README.md 8
- tools/memory-tree/README.md 5
- tools/agent-instructions/README.md 4
- tools/drift-audit/README.md 4
- tools/hooks/README.md 4
- tools/workflows/README.md 4
- coding-governance-agents.template.md 3
- tools/gate-lint/README.md 3
- tools/playbook/README.md 3
- tools/process-monitor/README.md 3
- skills/session-kickoff/SKILL.md 2
- tools/lexicon/LEXICON.md 2
- tools/run-gates/README.md 2
- tools/drift-audit/drift_signals.template.py 1 (a commented example value)
- tools/lexicon/SKILL.template.md 1
- tools/workflows/drift-audit-state.template.js 1 (a commented example value)

Separately, and invisible to every arm, WIRE carries **19 `<project>/tools/…` install destinations**. These are the runbook telling the operator where to put the kit, so they are the highest-leverage C literals. It also carries 17 `<gov>/tools/…` spellings, which are correct because they name gov's checkout.

**D FIXTURE-INTERNAL (179 literals, 27 files):**

- tools/unattended/gate-guard.test.sh 62 (withheld)
- tools/check-line-length.test.sh 25
- tools/lexicon/selftest.py 22 (withheld)
- tools/run-gates/run-selftests.test.sh 9 (withheld)
- tools/workflows/unattended-build.test.sh 8 (withheld)
- tools/check-install-prefix.test.sh 6
- tools/codebase-map/selftest.py 5 (withheld)
- tools/unattended/check-pass-order.test.sh 5 (withheld)
- tools/unattended/unattended.test.sh 5
- tools/memory-tree/merge-rows.test.sh 4 (withheld)
- tools/unattended/check-brief-recorded.test.sh 4
- tools/memory-tree/corpus_ids.py 3
- tools/unattended/check-playbook.test.sh 3
- .githooks/pre-push.test.sh 2
- tools/memory-tree/gotchas.py 2
- tools/run-gates/run-gates.test.sh 2 (withheld)
- tools/workflows/check-review-join.test.sh 2 (withheld)
- 1 each: tools/check-agent-cap-restatement.test.sh, tools/check-testsuite-counts.test.sh, tools/check-wiring.test.sh, tools/memory-tree/check-memory-hygiene.test.sh
- 1 each, withheld: tools/hooks/scratch-guard.test.sh, tools/run-gates/profile_bar.test.sh, tools/run-gates/run-gates.evidence.test.sh, tools/run-gates/run-gates.turnstile.test.sh, tools/unattended/adopt-unattended.test.sh, tools/unattended/cross-component.test.sh

**E BYTE-PINNED MARKER (24 literals, 22 files).** There are 22 `# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh` lines and 2 `# >>> render_doc — canonical copy: tools/lib/render-doc.sh` lines.

- tools/memory-tree/adopt-memory-tree.sh 2
- tools/memory-tree/kit-dogfood-parity.test.sh 2
- 1 each: skills/session-kickoff/manifest-check.sh, skills/session-kickoff/manifest-check.test.sh, tools/check-wiring.test.sh, tools/codebase-map/adopt-codebase-map.sh, tools/drift-audit/adopt-drift-audit.sh, tools/lexicon/adopt-lexicon.sh, tools/memory-recall/adopt-memory-recall.sh, tools/memory-tree/check-memory-hygiene.sh, tools/memory-tree/check-memory-hygiene.test.sh, tools/memory-tree/merge-rows.sh, tools/process-monitor/adopt-process-monitor.sh, tools/run-gates/run-gates.sh, tools/run-gates/run-selftests.sh, tools/runlog/adopt-runlog.sh, tools/unattended/check-unattended.sh, tools/unattended/unattended.sh
- 1 each, withheld: tools/codebase-map/adopt-codebase-map.test.sh, tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh, tools/run-gates/run-gates.gov.test.sh, tools/run-gates/run-gates.test.sh

**F GOV-SIDE ONLY (362 literals, 16 files):**

- tools/codebase-map/scen-adversarial.json 201 (withheld)
- tools/govkit/registry.toml 74
- tools/check-kit-versions.sh 33
- tools/run-gates/selftest-budgets.txt 27 (withheld)
- tools/install-prefix-waivers.txt 10
- tools/check-install-prefix.sh 3 (the kit-source test)
- tools/run-gates/run-gates.gov.test.sh 3 (withheld)
- tools/drift-audit/drift_signals.py 2 (withheld)
- tools/runlog/selftest.py 2 (withheld)
- .githooks/pre-commit 1 (`:59` probes check-template-size.sh, which no descriptor ships)
- WIRE-INTO-PROJECT.md 1 (`:1028`, the `contribute` verb)
- tools/agent-instructions/kit.toml 1 (`sentinel`)
- tools/gate-lint/kit.toml 1 (`sentinel`)
- tools/memory-recall/recall-fixture.json 1 (withheld)
- tools/playbook/kit.toml 1 (a `root_relative` source)
- tools/run-gates/ceiling-evidence.txt 1 (withheld)

**G COMMENT PROSE (128 literals, 74 files):**

- 5 each: tools/memory-tree/check-memory-hygiene.sh; tools/run-gates/run-gates.gov.test.sh (withheld)
- 4 each: tools/memory-tree/merge-rows.sh, tools/unattended/run-unattended-gates.sh; tools/run-gates/run-gates.test.sh (withheld)
- 3 each: tools/check-install-prefix.sh, tools/check-line-length.sh, tools/check-testsuite-counts.sh, tools/memory-recall/adopt-memory-recall.sh, tools/run-gates/kit.toml, tools/run-gates/run-gates.sh, tools/workflows/tier2-review.template.js; tools/hooks/agent-cap.test.sh (withheld)
- 2 each: .githooks/pre-push, skills/session-kickoff/manifest-check.sh, skills/session-kickoff/manifest-check.test.sh (lines 353-354, which are outside the parity-compared block), tools/check-agent-cap-restatement.sh, tools/check-line-length.test.sh, tools/check-wiring.test.sh, tools/codebase-map/adopt-codebase-map.sh, tools/drift-audit/adopt-drift-audit.sh, tools/hooks/agent-cap.js, tools/lexicon/kit.toml, tools/lexicon/lexicon_conf.py, tools/memory-tree/adopt-memory-tree.sh, tools/memory-tree/check-memory-hygiene.test.sh, tools/memory-tree/kit-dogfood-parity.test.sh, tools/run-gates/run-selftests.sh, tools/settings-merge.py, tools/unattended/unattended.test.sh, tools/workflows/check-review-join.sh
- 2 each, withheld: tools/codebase-map/map_extractors.py, tools/memory-tree/merge-rows.test.sh, tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh
- 1 each (8 kit.toml "WITHHELD BY CLAIMING THE DESTINATION" comments among them): tools/agent-instructions/kit.toml, tools/check-microformats.sh, tools/check-placeholders.test.sh, tools/check-testsuite-counts.test.sh, tools/check-wiring.sh, tools/codebase-map/kit.toml, tools/codebase-map/map_lib.py, tools/drift-audit/kit.toml, tools/hooks/scratch-guard.js, tools/lexicon/scaffold_lexicon.py, tools/memory-recall/extract.py, tools/memory-recall/kit.toml, tools/memory-recall/recall-opened.js, tools/memory-tree/build-readme-slot-highwater.txt, tools/memory-tree/build-readme-slot-limits.txt, tools/memory-tree/corpus_ids.py, tools/memory-tree/gen_build_index.py, tools/memory-tree/kit.toml, tools/memory-tree/merge-rows.py, tools/pytest-parallel-guardrails/kit.toml, tools/run-gates/gate-profiles.txt, tools/run-gates/profile_bar.py, tools/unattended/.unattended.conf.example, tools/unattended/check-brief-recorded.sh, tools/unattended/check-pass-order.sh, tools/unattended/check-playbook.sh, tools/unattended/check-unattended.sh, tools/unattended/check-unattended.test.sh, tools/unattended/kit.toml, tools/unattended/lib-unattended.sh, tools/unattended/unattended.sh, tools/workflows/check-protocol-parity.test.sh, tools/workflows/check-verifier-fanout.sh, tools/workflows/kit.toml
- 1 each, withheld: tools/codebase-map/adopt-codebase-map.test.sh, tools/drift-audit/drift_signals.py, tools/hooks/scratch-guard.test.sh, tools/lexicon/selftest.py, tools/memory-tree/hygiene-parity.test.sh, tools/run-gates/run-selftests.test.sh, tools/workflows/check-verifier-fanout.test.sh

## 5. Stale records found while classifying (not fixed; read-only census)

- **Backlog `TOOL-aProbedToolkit-3` is OPEN, but its lead example is fixed.** `check-verdict-epoch.sh` now derives `ENGINE="${_kit}check-memory-hygiene.sh"` (:79). Its second site, `codebase-map/selftest.py:1613`, formerly cited as 1243, is still live.
- **Two carried reason columns describe literals that no longer exist.**
  - `tools/check-agent-cap-restatement.sh` says it was "RAISED 3 -> 4" by a `WAIVERS=${1:-…}` default at :54. The count is 3, and :54 now derives `${_self_pre}` (TOOL-aRepatriatedFork-2 S7).
  - `tools/check-line-length.sh` cites the `DECL=${DECL:-…}` default at :49 as the seventh literal. The count is 6, and that line is derived.
- **`skills/session-kickoff/manifest-check.test.sh`'s reason is wrong.** It says all three literals are the byte-compared resolver block. `resolve-python.test.sh`'s `blk()` compares only from the `# >>>` line (:355) to `# <<<`, so :353 and :354 are ordinary comments and can be drained. The same two preamble lines sit uncompared in adopt-codebase-map.sh, adopt-drift-audit.sh, adopt-memory-recall.sh, adopt-memory-tree.sh, check-memory-hygiene.sh and merge-rows.sh.
- **The `stall-recorder.test.sh` and `stop-guard.test.sh` reasons name the wrong literal.** Both say the one literal is `KIT_REL="${KIT_REL:-tools/unattended}"`. That literal is directory-only and invisible to arm 2. The counted literal is the `# Run: bash tools/unattended/<suite>` header at :4.
- **The `.githooks/pre-push:367` marker reason promises a derivation that the code does not perform.** See §2.

## 6. Recommendation — drain order and mechanism

1. **A goes first, and it goes with the gate fix.**
   - **Hooks.** `pre-commit:48/54` and `pre-push:367` should derive their prefix at run time the way `check-wiring.sh` already does: receipt first, then `resolve_kit_dir`/`KIT_REL`, then a `GOV_KITROOT` declared in `.githooks/gate-env.sh`. The `tools|scripts` pair should not be the answer.
   - **The unattended conf example.** `adopt-unattended.sh` should stamp `LANDER`, `GATE_CMD`, `WIRING_CHECK` and `GENERATED_INDEXES` with the real prefix at adopt time. That is a deploy-time render, the mechanism `adopt-codebase-map.sh` already uses for `MAP_DIFF_CMD`.
   - **The three received suites.** Derive from `$HERE` at run time.
   - **The gate.** In the same unit, widen arm 3 to received tests and to `.conf.example` values, so that §2's invisible sites become visible before they are fixed. Otherwise the gate stays green over the class it exists to catch.
   - **govkit.** `foreign_kit_present` should probe the intake prefix, not `("tools", "")`.
2. **B second, by derivation.**
   - The four printed sites should derive from `$0`/`__file__`. `merge-rows.py:8` is the worst of them because it prints a launcher, `tools/lib/pyrun.sh`, that no adopter has at any prefix.
   - For the 89 in-source headers, spell the path through a literal `<prefix>/` token. A deploy-time `{prefix}` placeholder would not work: `apply` writes bytes verbatim and substitutes into no body.
   - Beware that the bare `<kit>/file` form is itself an arm-1 ban hit.
3. **C third.**
   - Docs that `govkit` renders take `{prefix}` at deploy time.
   - Verbatim READMEs and WIRE take the `<prefix>/` prose token.
   - WIRE's 19 invisible `<project>/tools/` destinations come first, because they prescribe the install.
   - Arm 2's lead class needs a `<project>/` carve-in for this change to be graded.
4. **E fourth, as one mechanical lockstep commit.** Reword the canonical marker line in `tools/lib/resolve-python.sh` and `render-doc.sh` together with all 24 copies. `kit-rel.sh`'s marker ("canonical copy: kit-rel.sh in gov's lib dir") is the in-tree precedent, so these literals can be derived away after all, despite several reason columns saying otherwise.
5. **G last, opportunistically.** Name the file, or name the kit in words, and not both, which is the rule the gate's own epoch-4 note gives.

**D (179) and F (362) are genuinely correct as literals.**

- A fixture chooses its own `tools/` layout inside a scratch tree, so the path is right at every prefix. The one sweep that tried to derive them broke 14 of 19 arms, per the `check-pass-order.test.sh` reason.
- F literals name gov's own checkout by definition: the deployer registry, gov's version gate, gov's declared self-test population, the adversarial scenario corpus, and the kit-source test. A registry that derived its own rows would stop being a declaration.
- The drain should therefore move D and F out of the shrink-only count into a declared, per-line or per-file exemption with a reason. That leaves the ratchet counting only the 363 drainable literals, so "drained" means zero rather than 541.

## 7. Allocation per drain unit

Each literal has exactly one writer, by precedence: a stranding site (unit 24), then a marker line (27), then a test or fixture file (28), then a doc (26), then a gov-side file (29), then class B (25) or G (27). Per unit: the kit entries it moves, then literal count per file.

```
== 24
entries: agent-instructions,check-microformats,check-placeholders,check-wiring,codebase-map,gate-lint,gov-internal,push-main,unattended
5 tools/unattended/.unattended.conf.example
3 .githooks/pre-commit
1 tools/agent-instructions/kit.toml
1 tools/gate-lint/kit.toml
1 tools/check-microformats.test.sh
1 tools/check-placeholders.test.sh
1 tools/check-wiring.test.sh
1 tools/codebase-map/selftest.py
1 tools/govkit/entries/check-agent-cap-restatement.kit.toml
1 tools/govkit/entries/check-install-prefix.kit.toml
1 tools/govkit/entries/check-kit-versions.kit.toml
1 tools/govkit/entries/check-placeholders.kit.toml
1 tools/govkit/entries/push-main.kit.toml
== 25
entries: agent-cap,check-agent-cap-restatement,check-line-length,check-microformats,check-placeholders,check-testsuite-counts,codebase-map,drift-audit,gate-lint,lexicon,memory-recall,memory-tree,playbook-render,process-monitor,review-harness,run-gates,settings-merge,unattended
5 tools/memory-tree/gen_build_index.py
3 tools/check-line-length.sh
3 tools/drift-audit/drift_report.py
3 tools/memory-recall/adopt-memory-recall.sh
3 tools/playbook/adopt-playbook.sh
3 tools/settings-merge.py
3 tools/codebase-map/map_lib.py
2 tools/check-placeholders.sh
2 tools/drift-audit/adopt-drift-audit.sh
2 tools/lexicon/adopt-lexicon.sh
2 tools/memory-tree/check-memory-hygiene.sh
2 tools/memory-tree/merge-rows.py
2 tools/process-monitor/adopt-process-monitor.sh
2 tools/unattended/adopt-unattended.sh
2 tools/workflows/check-review-join.sh
2 tools/workflows/check-verifier-fanout.sh
2 tools/workflows/check-workflow-syntax.js
1 tools/check-agent-cap-restatement.sh
1 tools/check-microformats.sh
1 tools/check-testsuite-counts.sh
1 tools/gate-lint/ps-hygiene.py
1 tools/hooks/agent-cap.js
1 tools/memory-tree/adopt-memory-tree.sh
1 tools/memory-tree/check-method-carriers.sh
1 tools/memory-tree/check-verdict-epoch.sh
1 tools/run-gates/derive-ceilings.py
1 tools/unattended/check-brief-recorded.sh
1 tools/unattended/check-pass-order.sh
1 tools/unattended/check-unattended.sh
1 tools/unattended/run-unattended-gates.sh
1 tools/codebase-map/map_extractors.template.py
1 tools/codebase-map/map_imports.py
1 tools/memory-recall/recall_conf.py
== 26
entries: agent-cap,agent-instructions,codebase-map,drift-audit,gate-lint,gov-internal,kickoff-manifest,lexicon,memory-recall,memory-tree,playbook,playbook-render,process-monitor,review-harness,run-gates,unattended
112 WIRE-INTO-PROJECT.md
10 tools/lexicon/README.md
8 tools/memory-recall/README.md
7 tools/drift-audit/README.md
7 skills/deploy-governance/SKILL.md
6 skills/session-kickoff/SKILL.md
5 tools/memory-tree/README.md
5 tools/workflows/README.md
4 tools/agent-instructions/README.md
4 tools/hooks/README.md
4 tools/process-monitor/README.md
3 coding-governance-agents.template.md
3 tools/drift-audit/drift_signals.template.py
3 tools/gate-lint/README.md
3 tools/playbook/README.md
3 tools/run-gates/README.md
2 tools/lexicon/LEXICON.md
2 skills/session-kickoff/MANIFEST-TEMPLATE.md
2 tools/unattended/fixture-records/tools~unattended~fixture-pieces~one~piece.md.md
2 tools/unattended/fixture-records/tools~unattended~fixture-pieces~two~piece.md.md
1 tools/lexicon/SKILL.template.md
1 tools/workflows/drift-audit-state.template.js
1 tools/codebase-map/README.md
== 27
entries: agent-cap,check-agent-cap-restatement,check-line-length,check-microformats,check-placeholders,check-testsuite-counts,check-wiring,codebase-map,drift-audit,gov-internal,kickoff-manifest,lexicon,memory-recall,memory-tree,process-monitor,push-main,pytest-parallel-guardrails,review-harness,run-gates,runlog,settings-merge,unattended
7 tools/run-gates/run-gates.sh
6 tools/drift-audit/adopt-drift-audit.sh
6 tools/memory-tree/check-memory-hygiene.sh
6 tools/memory-tree/merge-rows.sh
5 tools/memory-recall/adopt-memory-recall.sh
5 tools/unattended/run-unattended-gates.sh
4 skills/session-kickoff/manifest-check.sh
4 tools/codebase-map/adopt-codebase-map.sh
4 tools/memory-tree/adopt-memory-tree.sh
4 tools/run-gates/run-selftests.sh
4 tools/unattended/unattended.sh
4 tools/workflows/tier2-review.template.js
3 tools/check-line-length.sh
3 tools/check-testsuite-counts.sh
3 tools/hooks/agent-cap.js
2 .githooks/pre-push
2 tools/check-agent-cap-restatement.sh
2 tools/lexicon/adopt-lexicon.sh
2 tools/lexicon/lexicon_conf.py
2 tools/memory-tree/kit-dogfood-parity.test.sh
2 tools/process-monitor/adopt-process-monitor.sh
2 tools/settings-merge.py
2 tools/unattended/check-unattended.sh
2 tools/workflows/check-review-join.sh
2 tools/check-placeholders.sh
1 skills/session-kickoff/manifest-check.test.sh
1 tools/check-microformats.sh
1 tools/check-wiring.sh
1 tools/check-wiring.test.sh
1 tools/codebase-map/adopt-codebase-map.test.sh
1 tools/codebase-map/map_lib.py
1 tools/hooks/scratch-guard.js
1 tools/lexicon/scaffold_lexicon.py
1 tools/memory-recall/extract.py
1 tools/memory-recall/recall-opened.js
1 tools/memory-tree/build-readme-slot-highwater.txt
1 tools/memory-tree/build-readme-slot-limits.txt
1 tools/memory-tree/check-memory-hygiene.test.sh
1 tools/memory-tree/gen_build_index.py
== 29
entries: agent-cap,agent-instructions,check-install-prefix,check-kit-versions,codebase-map,drift-audit,gate-lint,gov-internal,lexicon,memory-recall,memory-tree,playbook-render,process-monitor,pytest-parallel-guardrails,review-harness,run-gates,runlog,unattended
202 tools/codebase-map/scen-adversarial.json
137 tools/gate-legs.json
100 tools/govkit/registry.toml
41 tools/check-kit-versions.sh
35 tools/govkit/govkit.py
27 tools/run-gates/selftest-budgets.txt
13 tools/check-install-prefix.sh
13 tools/codebase-map/map_extractors.py
10 tools/install-prefix-waivers.txt
10 tools/dead-path-waivers.txt
8 tools/check-spec-tokens.py
7 tools/unattended/kit.toml
7 tools/check-dead-paths.sh
6 tools/run-gates/kit.toml
6 tools/check-playbook-parity.sh
5 tools/drift-audit/drift_signals.py
5 tools/lexicon/kit.toml
5 tools/playbook/kit.toml
5 tools/govkit/entries/check-line-length.kit.toml
5 tools/workflows/unattended-build.js
4 tools/drift-audit/kit.toml
4 tools/check-hook-destinations.sh
4 tools/check-template-size.sh
4 tools/govkit/entries/check-install-prefix.kit.toml
4 tools/govkit/subject-pins.tsv
4 tools/lib/extract-arms.sh
4 tools/lib/pyrun.sh
4 tools/template-size-limits.txt
3 tools/agent-instructions/kit.toml
3 tools/codebase-map/kit.toml
3 tools/memory-recall/kit.toml
3 tools/memory-tree/kit.toml
3 tools/pytest-parallel-guardrails/kit.toml
3 tools/workflows/kit.toml
3 tools/hooks/kit.toml
3 tools/playbook/render_playbook.py
3 tools/process-monitor/kit.toml
3 tools/check-kit-placeholders.py
3 tools/govkit/entries/check-agent-cap-restatement.kit.toml
```

The scratchpad working files named above were not committed; unit 23's widened gate re-derives every population from the tree.
