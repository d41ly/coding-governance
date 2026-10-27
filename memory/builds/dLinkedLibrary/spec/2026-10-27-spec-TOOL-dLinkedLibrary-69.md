# TOOL-dLinkedLibrary-69 — the lookup's retirement step reads `MAP_CLI` the way bash `source` reads it

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 27 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-69-deviation-691.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-69-deviation-691.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 19 at HIGH**, report item **H4**. Id 35 shares the item and is its own unit,
`TOOL-dLinkedLibrary-70`.

`TOOL-dLinkedLibrary-57` S1 reads `MAP_CLI` as "the last `MAP_CLI=` line winning, a value in double
quotes or bare". `.unattended.conf` is sourced by the unattended kit (`. "$CONF"`), so single quotes, an
`export` prefix, a trailing `# comment`, a BOM and a CR are all legal there. A value the step reads
another way grades a value the kit never sees: `MAP_CLI='tools/codebase-map/reuse_lookup.py'` keeps its
quotes, falls to 57 S2's "names any other file" row, and the witness passes a conf that still names the
deleted lookup. `govkit.parse_conf_assignment` already reads one conf line by bash's word rule, pinned to
bash by a parity selftest.

This unit gives the step one reader of `MAP_CLI` built on that function, and has the witness read both the
before-image's conf and the target's conf through it. It repairs `TOOL-dLinkedLibrary-57` and builds one
step after it (order 27).

## 2. Scope (IN)

- **S1** — The reader. `read_map_cli(text)` in `tools/govkit/steps/retire_reuse_lookup.py` strips one
  leading BOM, splits the text into lines with `splitlines`, passes each through
  `parse_conf_assignment` (`tools/govkit/govkit.py:5143`), and returns the value of the last assignment
  whose key is `MAP_CLI`, or `None` when no line assigns it, as `read_conf_key_gaps` (:5210-5213) keeps the
  last value per key. `govkit.py` is loaded by its file path, as each step program loads
  `upgrade_steps.py` (TOOL-dSafePassage-1 §4). Observed by AC1.
- **S2** — The witness. `witness` reads the before-image's `.unattended.conf` bytes, decoded as UTF-8, and
  the target's `.unattended.conf` now, each through `read_map_cli`, and selects 57 S2's row and its
  "unchanged" test on those two values; no other read of `MAP_CLI` exists in the step. Observed by AC2.

## 3. Non-goals (OUT)

- `up`'s re-point and its rewrite of the assignment line: `TOOL-dLinkedLibrary-70` (id 35), which
  calls S1's reader.
- Whether `up` images the conf on every row, and what a missing image entry means:
  `TOOL-dLinkedLibrary-74`'s items for ids 13 and 36.
- The witness table's rows: 57 S2, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-57` — S1's read of `MAP_CLI` and S2's witness table, which S1 replaces with `read_map_cli` and S2 selects through it (id 19)
- **hands-off** `TOOL-dLinkedLibrary-70` — `read_map_cli`, which `up`'s lookup-naming test calls (id 19)
- **hands-off** `TOOL-dLinkedLibrary-80` — `read_map_cli` and AC1's variants, which unit 80 corrects (ids 14, 38 of the spec audit of units 65 to 74)

## 4. Design

### Evidence

- `tools/unattended/unattended.sh:617`: `. "$CONF"`, so the kit reads `MAP_CLI` as bash does.
- `tools/govkit/govkit.py:5139-5170`: `CONF_KEY_RX` admits an `export` prefix; `parse_conf_assignment`
  returns `(key, value)` "as bash reads it under `source`": whitespace after `=` is an empty value, a
  quoted value ends at its matching quote, an unquoted value ends at a `#` after whitespace.
- `tools/govkit/govkit.py:5172-5213`: `read_conf_key_gaps` reads a conf with `splitlines` and keeps the
  last value per key.
- `CONF_KEY_RX` opens `^\s*`, and a BOM is not whitespace to it, so S1 drops the BOM first.
- TOOL-dSafePassage-1 §4: step programs load `upgrade_steps.py` by their own file's path, "because the
  runner's `-I` drops the script directory from `sys.path`".

### Files touched (estimate)

- `tools/govkit/steps/retire_reuse_lookup.py`: S1, S2

### Alternatives rejected

- **Sourcing the conf in a `bash` subprocess.** It executes whatever the conf holds, a write surface a
  read-only witness does not price.
- **A second parser in the step.** `parse_conf_assignment` is already the copy the govkit selftest pins
  to bash; a third copy is the duplicate the charter's reuse rule refuses.

## 5. Production-readiness checklist

- security — the reader parses text and executes nothing.
- perf / scale — one pass over two small files.
- error / empty / loading states — conf bytes that do not decode exit 1 naming the file.
- observability — the witness names the value it read and the row it selected.
- risks — a conf line bash would treat differently from `parse_conf_assignment` is the parity selftest's
  to catch, not this step's.
- testing — AC1 and AC2 by probe over scratch targets.
- migration — none.
- user docs — none under `help/`: the step program's docstring states the table.

## 6. Acceptance criteria

- **AC1** — When `python -I -c` loads `retire_reuse_lookup.py` by its path and calls `read_map_cli` on
  four conf texts, a single-quoted lookup value, an `export` line with a trailing comment, a blank value
  followed by `# left blank`, and two assignments, each result equals what `bash -c '. <file>; printf %s
  "$MAP_CLI"'` prints for the same text written to a scratch file under `%TEMP%/rl69`; and the same four
  texts with a leading BOM and with CRLF line ends return the same four results.
  Red when: any result differs from bash's, or a BOM or a CR changes one.
- **AC2** — When `python retire_reuse_lookup.py witness <target>` runs over a scratch target whose
  before-image records a conf assigning `MAP_CLI` the lookup in single quotes and whose conf still assigns
  it so, it exits 1 naming the value.
  Red when: a single-quoted lookup value reads as a foreign one and the witness exits 0.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the step program has no test home at base, as 57 §7 records, so AC1 and AC2 are this pass's
probes.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 3 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 19 (HIGH, item
  H4).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.

## 10. Reuse audit

The seam extended is `govkit.parse_conf_assignment` (`tools/govkit/govkit.py:5143`), the conf-line reader
the govkit selftest pins to bash, with `read_conf_key_gaps`'s last-value rule. `python
tools/codebase-map/reuse_lookup.py "read a kit conf assignment line the way bash source reads it"` ranked
`read`, `read_text`, `load_conf`, `resolve_kit_dir` and `parse_conf`; `parse_conf` (`tree_lib.py`) is the
memory-tree kit's reader of whole files, and the probe missed `parse_conf_assignment`, found by reading
`govkit.py`, a miss recorded here as M5 asks.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
