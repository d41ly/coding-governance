# TOOL-aRepatriatedFork-25 — printed and usage strings in received code name no install prefix

**Status:** CLOSED · rev-3 · 2026-09-29 · node a · Tier-1 · base 2143b6d6 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-25-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-25-1-acceptance-ledger.md) | journal | — |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-25-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-25-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 TOOL-aRepatriatedFork-48 |

<!-- /gen:spec-records -->

## 1. Goal

Received kit code tells its reader where to run it, and it does so at gov's prefix. Two programs
print that path at run time, and 56 source headers, docstrings and prose strings state it. At any
other prefix each one points at a file that is not there. This unit makes a printed path derive
from where the program actually runs, and spells every unprinted one in a form correct at any
prefix. It closes backlog `TOOL-dPolishedVitrine-5` for the files it owns.

## 2. Scope (IN)

- **S1** — The two printed sites derive. `merge-rows.py`'s `main()` prints its first two docstring
  paragraphs, which name its own path and the gov-internal launcher `pyrun.sh`; the printed text
  names the program by its path from the repo root, derived from `__file__`, and names no launcher
  an adopter does not have. (rev-3) The launcher it names is the kit's own `merge-rows.sh`, which
  ships beside the program and is what `check-wiring.sh` wires, so the printed line is
  `bash <kit dir>/merge-rows.sh %O %A %B %P` with the kit dir derived. `derive-ceilings.py --help`
  names the leg manifest the program resolved. Observed by AC1, AC2.
- **S2** — Every in-source usage header in a received, non-test, non-gov-side file spells its path
  as §8 F1 resolves. Census §3 lists them as "usage header in source". Observed by AC3.
- **S3** — The eight other literals in received code outside a comment: docstrings in `map_lib.py`
  (three), `map_imports.py`, `recall_conf.py` and `map_extractors.template.py`; the printed
  `cp <gov>/tools/settings-merge.py` hint in `adopt-memory-recall.sh:203`, spelled as
  `TOOL-aRepatriatedFork-23` §8 F2 resolves; and the foreign-hook fixture string at
  `settings-merge.py:620`, which becomes a name that is not a kit path. Observed by AC3.
  (rev-3) F2 (c) says derive where printed, but gov's kit root is not observable from an adopter's
  tree, so the printed source half takes F2's prose token: `cp <gov>/<prefix>/settings-merge.py`.
- **S4** — `map_lib.REGEN_CMD`, the legacy root-install regen command a pre-1.1 `GATE_FILE` still
  reads, takes its value from `regen_cmd()` at import. An old gate then prints a command correct at
  its own prefix. The self-test pin that held it equal to the root answer holds it equal to
  `regen_cmd()`. The waiver row for that line is struck. Observed by AC4.
- **S5** — The ledger rows for these files are lowered, and every kit moved takes its version bump in
  every carrier. Observed by AC5.

## 3. Non-goals (OUT)

- Usage headers inside test files, which `TOOL-aRepatriatedFork-28` owns, and inside gov-side or
  withheld files, which `TOOL-aRepatriatedFork-29` owns. The printed `map_extractors.py:253`
  message is the latter's: that file is withheld.
- Comment prose that is not a usage header. `TOOL-aRepatriatedFork-27` owns it.
- The two prose lines quoting the legacy regen command in `gen_map.py` and `adopt-codebase-map.sh`.
  They are comments, and `TOOL-aRepatriatedFork-27` owns them.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger, and the rule that a
  `<prefix>/`-led path is not counted. Without it the S2 form reds as a new root spelling.

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed). PINNED,
measured 2026-09-25.

- Census §3 lists 93 class-B literals over 56 files. Four are printed at run time
  (`merge-rows.py:8` twice, `derive-ceilings.py:4`, `map_extractors.py:253`). The rest are read in
  source, and every printed `usage:` line in those files already derives from `$0`, `basename` or
  `$SELF`.
- The ownership rule (the census record's section 7) gives this unit 59 literals over 33 files: 51 counted
  today and 8 invisible. The largest are `memory-tree/gen_build_index.py` with 5, and
  `check-line-length.sh`, `drift-audit/drift_report.py`, `memory-recall/adopt-memory-recall.sh`,
  `playbook/adopt-playbook.sh`, `settings-merge.py` and `codebase-map/map_lib.py` with 3 each.
- The remaining 34 class-B literals sit in test files (to `TOOL-aRepatriatedFork-28`), in withheld
  or gov-side files (to `TOOL-aRepatriatedFork-29`), and in the seeded `drift_signals.template.py`
  (to `TOOL-aRepatriatedFork-26`).
- Arm 1's one class-B line is `map_lib.py:1493`, the `REGEN_CMD` legacy, waived (census §1).
- `pyrun.sh` ships to no adopter at any prefix (census §3, the `merge-rows.py:8` row).

### Ownership rule

One literal, one writer, and the rule is `TOOL-aRepatriatedFork-23` §8 F3's. This unit owns a
class-B or other non-comment literal in a received file that is not a test, not withheld and not
gov-side.

(rev-3) Measured at `d0674c67` under epoch 5, these 33 files carry more counted literals than the
census allocated, in four classes. Comment prose and the canonical-copy markers are
`TOOL-aRepatriatedFork-27`'s, so those rows only fall here. `map_lib.py`'s module, `resolve_root`,
`kit_rel` and `boundedK`-note docstrings carry four, all class B by this rule, so this unit takes
all four and the row goes to zero. What is left is outside class B: a kit segment joined under an
already-derived base on an EXECUTING line, which `TOOL-aRepatriatedFork-23` §8 F1 (a) says the
owning unit derives. They are `settings-merge.py`'s fragment and hook joins, the agent-cap probes in
`check-review-join.sh` and `check-verifier-fanout.sh`, `check-verdict-epoch.sh`'s extract probe and
`run-unattended-gates.sh`'s `RUNNER`. Two JSON `"hooks"` keys in `settings-merge.py`'s self-test are
counted by the predicate too, as a homonym. This unit is Tier-1 and priced text, not executing
lines. Deriving those segments changes code paths whose suites this pass cannot run, which is
M3 veto 3, so they are RETURNED to the main loop to assign, not taken here.

### Files touched (estimate)

The 33 files the census record's section 7 lists for this unit, across `tools/memory-tree/`,
`tools/codebase-map/`, `tools/drift-audit/`, `tools/memory-recall/`, `tools/unattended/`,
`tools/workflows/`, `tools/lexicon/`, `tools/playbook/`, `tools/process-monitor/`,
`tools/run-gates/`, `tools/gate-lint/` and `tools/hooks/`, the loose checkers under `tools/`, plus
`tools/install-prefix-waivers.txt` and `tools/install-prefix-carried.txt`.

### Alternatives rejected

- A deploy-time `{prefix}` placeholder in these bodies. `govkit apply` writes engine bytes verbatim
  and substitutes into no body (census §6), so the token would arrive unrendered.

## 5. Production-readiness checklist

- security — none; comment, docstring and usage text.
- perf / scale — none.
- error / empty / loading states — S1's derivation has no failure mode beyond `__file__`, which
  Python always sets for a script.
- observability — the printed usage now names a path that exists.
- risks — a suite that asserts on printed usage text. AC2's control and the main loop's suite run
  catch it.
- testing — `merge-rows.py`'s own usage output in a fixture at `scripts/`.
- migration — none.
- user docs — none beyond the headers themselves.

## 6. Acceptance criteria

- **AC1** — When `merge-rows.py` runs with no arguments from a fixture that installs the kit under
  `scripts/memory-tree/`, its output names the program at that directory and names no `pyrun.sh`.
  (rev-3) The wiring line it prints runs the kit's `merge-rows.sh` from that same directory.
  Red when: the output names `tools/` or the launcher.
- **AC2** — Red-first control: the same fixture on `2143b6d6`'s file prints the `tools/` path.
  Recorded in the acceptance ledger.
  Red when: the old file already prints a derived path.
- **AC3** — (rev-3) When `bash tools/check-install-prefix.sh --list` runs, no ledger row counts a
  literal S1 to S4 name. A file whose every counted literal is this unit's keeps no row, and every
  other owned file's count falls by exactly the literals drained here, as a per-line scan with the
  gate's own counter shows.
  Red when: an S1 to S4 line still counts, or an owned file's row fell by less than its drained
  lines.
  figure: DERIVED at observation time.
- **AC4** — When `map_lib` is imported from a fixture install at `scripts/codebase-map/`,
  `REGEN_CMD` equals `regen_cmd()` and names the generator under `scripts/codebase-map/`.
  Red when: it still names the root form.
- **AC5** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `line length` · `row-keyed merge driver replay` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `settings-merge selftest` · `memory-recall kit selftest` · `drift-audit selftest` · `lexicon naming predicates` · `shell-hygiene selftest` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `process-monitor census selftest` · `process-monitor adopter selftest` · `hook destinations self-test` · `lexicon selftest` · `govkit acceptance matrix` · `playbook render selftest` · `run-selftests self-test`

## 8. Open questions

- **F1 — how is an unprinted usage header spelled?** Option (a): `<prefix>/` followed by the
  kit-relative path, as census §6 recommends. Option (b): the bare file name, which says nothing
  about where the file is. Option (c): no path at all, only the arguments, since the printed
  `usage:` line already derives the name. Recommendation: (a). It keeps the kit segment a reader
  needs to find the file, and it is the one form every doc unit in this set also uses.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: drain every hard-coded kit
  prefix before `TOOL-aRepatriatedFork-18`'s held leg, with no class exempted. This unit is census
  class B for received code.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.
- rev-3 · 2026-09-29 · the unit pass, before code. AC3 said no owned file keeps a row, which the
  ownership rule itself forbids once epoch 5 counts the comments and markers `TOOL-aRepatriatedFork-27`
  owns in the same files, so AC3 now grades the lines this unit drains. §4 records the executing
  derived-base joins epoch 5 newly counts and returns them to the main loop under M3 veto 3. S1 pins
  the launcher `merge-rows.py` prints to the kit's own `merge-rows.sh`, and S3 pins the prose token
  the printed `cp` hint takes, since gov's kit root cannot be derived from an adopter's tree.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "usage header names the script by its own path"` ranked
`owners_of`, `attribute_paths` and `build_usage`, none of which spells a usage path. No existing seam
fits S2, which is a spelling rule. S4 reuses `regen_cmd()` in `tools/codebase-map/map_lib.py`, which
the kit already calls everywhere else.

Recall terms used: `usage header install-prefix carried remedy string printed derive __file__
REGEN_CMD regen_cmd legacy`.
