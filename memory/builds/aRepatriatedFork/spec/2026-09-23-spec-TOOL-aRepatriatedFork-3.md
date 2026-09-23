# TOOL-aRepatriatedFork-3 — shipped Python names its encoding on every text-IO call

**Status:** CLOSED · rev-2 · 2026-09-23 · node a · Tier-1 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-23-build-TOOL-aRepatriatedFork-3-1-acceptance-ledger.md](../build/2026-09-23-build-TOOL-aRepatriatedFork-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-TOOL-aRepatriatedFork-3-build-brief.md](../prompts/2026-09-23-prompt-TOOL-aRepatriatedFork-3-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Gov's shipped Python opens text-mode subprocesses and reads files with no `encoding=`, so it decodes
with the platform default: cp1251 or cp1252 on the Windows nodes, UTF-8 in CI. inCMS's
`encoding-posture` leg reds on every such call the moment gov's bytes land, and inCMS carries a fork
per file to add one keyword. This unit adds the keyword at every shipped site, puts the same check
on gov's own bar so the class cannot come back, and makes `gotchas.py --declares` print its verdict
so a crash cannot read as "does not declare".

## 2. Scope (IN)

- **S1** — Every text-IO call in gov's LANDABLE shipped Python passes `encoding="utf-8"`: 29 sites
  in 14 files (§4 table). Observed by AC1.
- **S2** — The gate-lint kit gains `encoding_posture.py`, a port of inCMS's AST scanner
  (`services/api/scripts/check_encoding_posture.py` in the inCMS tree) with its two arms — text-mode
  file IO and text-mode `subprocess` — made project-agnostic: its population is the tracked `*.py`
  under a root, and an OPTIONAL registry positional takes the shape
  `tools/gate-lint/sh_hygiene.py` already uses. It carries a `--selftest` that proves both arms fire
  and both clear. Observed by AC2 and, red-first, by AC3.
- **S3** — Gov's bar gains a leg running S2 over `tools/` and `skills/`, with gov's registry holding
  the gov-internal sites S1 does not reach. Observed by AC4. The scanner's CLI is
  `[registry] [root] [pathspec ...]`, so the leg narrows the population with the pathspecs `tools`
  and `skills` rather than a second root. The leg is gov-only (§8 F2), so it is an `[[exempt_leg]]`
  row in the govkit registry and not a `[[gate_leg]]` in the gate-lint descriptor.
- **S4** — `tools/memory-tree/gotchas.py --declares` prints `declares: yes` or `declares: no` before
  it exits, reads stdin as bytes decoded UTF-8, and exits 2 with a named message when stdin cannot
  be read. Observed by AC5.

## 3. Non-goals (OUT)

- Draining the 151 gov-internal sites (§4). They sit in `tools/govkit/`, test suites and fixtures no
  adopter receives; S3 pins them in a shrink-only registry and a follow-up row drains them (§8 F1).
- A gate leg shipped to adopters. The scanner file travels with the kit's `**` include, and whether
  a kit leg declares it is §8 F2.
- The third arm inCMS deliberately does not gate — stdout encoding — for the reason its own header
  gives: a static check of it is vacuous.
- `check-arms.py`'s other two blockers at inCMS, the `parse_conf` import and the pin path. They are
  `TOOL-aRepatriatedFork-9`'s; this unit fixes only its encoding.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-13` — the `declares: yes|no` line S4 adds, which that unit's
  contract table lists for an adopter-owned gotchas engine.

## 4. Design

### The sites, measured

Measured on node a, 2026-09-23, by running inCMS's scanner over the landable shipped set of gov
a7c78ad2: every `.py` source a descriptor resolves with role `engine`, `seed`, `rendered` or
`merged` — 43 files. PINNED.

| File | Lines | Arm |
|---|---|---|
| `tools/codebase-map/map_diff.py` | `:180` | subprocess |
| `tools/gate-lint/sh_hygiene.py` | `:274` | subprocess |
| `tools/lexicon/lexicon.py` | `:410`, `:4064`, `:4114` | subprocess |
| `tools/lexicon/scaffold_lexicon.py` | `:207` | subprocess |
| `tools/memory-recall/recall_conf.py` | `:106` | subprocess |
| `tools/memory-tree/check-arms.py` | `:71` | subprocess |
| `tools/memory-tree/corpus_ids.py` | `:98`, `:341` | subprocess |
| `tools/memory-tree/gen_build_index.py` | `:235` | subprocess |
| `tools/memory-tree/gotchas.py` | `:67` | subprocess |
| `tools/memory-tree/row_grammar.py` | `:54`, `:653`, `:776` | subprocess |
| `tools/playbook/render_playbook.py` | `:82` | subprocess |
| `tools/run-gates/check-receipt.py` | `:151`, `:155`, `:164`, `:170`, `:180`, `:190` | file IO |
| `tools/run-gates/check-receipt.py` | `:213` | subprocess |
| `tools/run-gates/derive-ceilings.py` | `:97`, `:105`, `:430` | subprocess |
| `tools/run-gates/profile_bar.py` | `:279`, `:290`, `:383` | subprocess |

`tools/memory-tree/row_grammar.py:653` is the rotated-archive probe that arrived after inCMS's last
carry, and it is the one inCMS patched on this pull as `scripts/row_grammar.py:659`. The two
`forked` recall files carry one site each (`tools/memory-recall/extract.py:203`,
`tools/memory-recall/query.py:216`); a forked source is never sent, so they sit with the
gov-internal sites below.

Over all of gov's tracked `tools/` Python the scanner reports 180 sites in 30 files, so 151 sites in
16 files lie outside the landable set: `tools/govkit/govkit.py`, the kit self-tests, the recall
selftest and floor, and fixtures. PINNED, same run. At the build pass's base `85fcb90f` the same
files carry 153: govkit's self-test gained two `subprocess` sites after a7c78ad2. The registry
seeds from that measurement, and the landable set's lines have moved but its 29 sites have not.

### What inCMS carries today

Each row below differs from gov only by the keyword this unit adds, plus a delta header. Measured by
a CR-insensitive diff on node a, 2026-09-23.

| inCMS file | Record in `.governance/kits.json` | inCMS lines | gov lines |
|---|---|---|---|
| `scripts/row_grammar.py` | `KIT_MEMORY_TREE_ROW_GRAMMAR_DELTA` | `:59`, `:659`, `:782` | `:54`, `:653`, `:776` |
| `scripts/codebase-map/map_diff.py` | `KIT_CODEBASE_MAP_DELTA` | `:186-187` | `:180-181` |

### The scanner

`tools/gate-lint/encoding_posture.py` keeps inCMS's AST logic whole — the positional-slot rule for
`read_text`/`write_text`, the Path-receiver-only rule for `.open`, the binary-mode exemption — and
changes three things. Its population is `git ls-files` under a root, not inCMS's four globs. Its
registry positional keys on `<path>\t<arm>\t<count>\t<reason>`, never a line number, with set
equality in both directions, as `tools/gate-lint/sh_hygiene.py`'s registry does. And it prints its
graded file count on the clean line, so a green run over an empty population cannot pass as
coverage.

### The probe line

`tools/memory-tree/gotchas.py:614-615` returns the verdict as an exit code only. An uncaught
exception also exits 1, which reads as "this record names no gate". inCMS's copy prints
`declares: yes|no` (`scripts/gotchas.py:548-557`), and its hygiene check 25 refuses a run that did
not print one (`scripts/check-docs-hygiene.sh:1207-1208`). Gov's own selftest calls `declares()`
directly, so the line is additive for gov and is the contract an adopter-owned engine needs.

### Inventory

- `encoding_posture.py` in `tools/gate-lint/`. Its functions keep inCMS's names where the lexicon
  admits them; `scan_text_io` replaces `_offenders_in`, and the entry point is `main`.
- `memory/project/encoding-posture-sites.txt`, gov's registry, admitted under
  `PROJECT_REGISTRY_EXTRA` in `.memory-tree.conf` beside `substitution-fed-loops.txt`.
- One gov leg, named in §7's arm line; `memory/map/features/gate-lint.md` lists it among its legs.

### Migration

- inCMS deletes the two rows in the table above, takes gov's `scripts/row_grammar.py` and
  `scripts/codebase-map/map_diff.py` verbatim, and its `encoding-posture` leg stays green over them.
- inCMS's `KIT_CODEBASE_MAP_SELFTEST_DELTA` stays: that file is `project-owned` at gov, so gov never
  sends it, and its second delta is unrelated.
- nc: nothing to delete for encoding alone; its `scripts/row_grammar.py` fork is
  `TOOL-aRepatriatedFork-9`'s.

### Rollout

One commit, carrying every version bump, because shipped bytes move in seven kits: codebase-map
1.7 → 1.8, lexicon 1.5 → 1.6, memory-recall 1.9 → 1.10, memory-tree 2.86 → 2.87, playbook-render
1.1 → 1.2 and run-gates 1.8 → 1.9, each in every carrier. gate-lint declares no constant. The leg's
red case was observed at a7c78ad2 before the commit, and the leg lands with the fixes and the seeded
registry, so its first run in the tree is green. The backlog row §8 F1 files is owed by the main
loop: `--dispatch` refuses a unit pass that declares a write to `memory/backlog/`, a shared record.

### Files touched (estimate)

- `tools/codebase-map/map_diff.py`
- `tools/gate-lint/sh_hygiene.py`
- `tools/lexicon/lexicon.py`
- `tools/lexicon/scaffold_lexicon.py`
- `tools/memory-recall/recall_conf.py`
- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/row_grammar.py`
- `tools/playbook/render_playbook.py`
- `tools/run-gates/check-receipt.py`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/profile_bar.py`
- `tools/gate-legs.json`
- `.memory-tree.conf`
- `memory/map/features/gate-lint.md`

### Alternatives rejected

- **Set `PYTHONUTF8=1` in the gate runner.** It fixes the bar and nothing else: a session or a hook
  running the same script directly still decodes with the locale, which is the population inCMS's
  scanner header says actually crashed.
- **A `grep` for `text=True` without `encoding`.** inCMS's header records why it chose the AST: a
  line grep cannot see a call split across lines, and every site in the table above that sits on a
  continuation line would pass.

## 5. Production-readiness checklist

- security — N/A. No new input surface.
- perf / scale — one AST parse per tracked Python file on gov's bar; inCMS runs the same scanner
  over 687 files in its fast phase.
- error / empty / loading states — an unparseable file is a named refusal with exit 2, as inCMS's
  scanner does; an empty population prints its zero and exits 1.
- observability — the clean line names the graded file count; a hit names `<path>:<line>:<col>` and
  its arm.
- risks — a keyword added to a call that passed `errors=` or read binary would change behaviour; the
  table holds none, and S2's binary-mode rule is what keeps that true for later sites.
- testing — S2's `--selftest`; AC3's red-first run on a7c78ad2.
- migration — inCMS deletes two divergence rows.
- user docs — the gate-lint README gains the scanner's paragraph beside its two siblings.

## 6. Acceptance criteria

- **AC1** — When inCMS's scanner is pointed at the 14 files in §4's table after the change, it
  prints `OK` over all 14; checked by `grep -c 'encoding=' tools/memory-tree/row_grammar.py` rising
  by three. Red when: any listed site still lacks the keyword.
- **AC2** — When `cd tools/gate-lint && python3 encoding_posture.py --selftest` runs, both arms
  report a fixture hit and a fixture clear. Red when: either arm passes its offending fixture.
- **AC3** — When the new scanner runs over `tools/` at a7c78ad2 with gov's registry empty, it exits
  1 and names `tools/memory-tree/row_grammar.py:653` and `tools/run-gates/check-receipt.py:151`
  among its hits. Red when: it exits 0 there, which would mean it cannot see the class it was
  written for.
- **AC4** — When the new leg runs over gov after the change, it exits 0, and every row of gov's
  registry `encoding-posture-sites.txt` names a file outside §4's landable set. Red when: a registry
  row names one of the 14 fixed files.
  figure: the registry's row count is derived by the scanner; the 151 above is the PINNED start.
- **AC5** — When `python3 tools/memory-tree/gotchas.py --declares` reads a record that names a gate,
  it prints `declares: yes` and exits 0; a record naming none prints `declares: no` and exits 1.
  Red when: either run prints no `declares:` line, as a7c78ad2 does.

## 7. Gates

`gotchas selftest` · `row-grammar selftest` · `check-arms selftest` · `codebase-map kit selftest` ·
`codebase-map gate coverage` · `codebase-map adopter e2e` · `shell-hygiene selftest` ·
`lexicon selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` ·
`row-keyed merge driver replay` · `hook destinations self-test` · `govkit acceptance matrix` ·
`playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `kit version markers` ·
`verdict epoch (kit version dates the engine)`

New arm: the gate-lint kit's `encoding_posture.py --selftest` · an offending fixture per arm,
observed red before the clean twin is written · none.

New arm: gov leg `encoding posture (text IO names its encoding)` in `tools/gate-legs.json` · first
run at a7c78ad2 with an empty registry, observed red on the 29 landable sites, then green after S1
and the registry seed · none.

## 8. Open questions

- **F1 — drain the 151 gov-internal sites here, or pin them?** Draining touches
  `tools/govkit/govkit.py` in about fifty places and every kit's self-test. Recommendation: pin them
  in this unit and file one backlog row to drain them, because none reaches an adopter and the
  registry reds on any new one.
  RESOLVED (owner, 2026-09-23): pin the 151 sites here and file one backlog row to drain them, as
  recommended.
- **F2 — does the gate-lint kit declare an adopter leg for the scanner?** A declared leg reds at
  every adopter's next pull until they seed a registry, which is what gate-lint's two existing legs
  already do. Recommendation: not in this unit; ship the file, keep the leg gov-only, and let inCMS
  decide whether gov's scanner replaces its own.
  RESOLVED (owner, 2026-09-23): no adopter leg in this unit; the scanner stays gov-only, as
  recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from audit-A's and audit-B's encoding findings and a run of
  inCMS's scanner over gov a7c78ad2's shipped Python.
- rev-2 · 2026-09-23 · built. S3 names the scanner's pathspec CLI and the `[[exempt_leg]]` row that
  keeps the leg gov-only. §4 records the 153 carried sites at the pass base beside the pinned 151,
  so AC4's registry is measured rather than copied. §4 Rollout is one commit rather than one per kit,
  and hands §8 F1's backlog row to the main loop because `--dispatch` refuses the shared record.

## 10. Reuse audit

The seam is inCMS's `services/api/scripts/check_encoding_posture.py`, ported whole rather than
rewritten, and the registry shape is `tools/gate-lint/sh_hygiene.py`'s.
`python3 tools/codebase-map/reuse_lookup.py "check text IO names an explicit encoding"` ranks
`gen_build_index.py`'s `read_text` and `write_text` helpers first — callers of text IO, not a check
of it — and no scanner of this class; no existing seam fits inside gov, and the adopter's is the one
taken.

Recall terms used: `encoding-posture`, `encoding="utf-8"`, `text=True`, `cp1251`, `cp1252`,
`subprocess`, `read_text`, `gate-lint`, `declares`, `completion probe`, `row_grammar`, `map_diff`.
