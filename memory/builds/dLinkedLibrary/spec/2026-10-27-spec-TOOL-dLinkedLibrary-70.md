# TOOL-dLinkedLibrary-70 — the lookup's retirement step re-points every spelling of a lookup-naming `MAP_CLI`

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 27 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 |
| [2026-10-27-build-TOOL-dLinkedLibrary-70-deviation-701.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-70-deviation-701.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 35 at HIGH**, report item **H4**. Id 19 shares the item and is its own unit,
`TOOL-dLinkedLibrary-69`.

`TOOL-dLinkedLibrary-57` S3 keeps `TOOL-dLinkedLibrary-42`'s re-point: `up` rewrites only a `MAP_CLI`
naming the lookup, read by 57 S1's double-quoted-or-bare rule. A conf the unattended kit sources may
spell that value in single quotes, after `export`, or before a trailing comment, and `up` then leaves the
lookup in place. Once the lookup files are deleted the conf names a file that is gone, and the driver
silently treats the map as not adopted (`tools/unattended/unattended.sh:10557-10559`).

This unit has `up` decide "names the lookup" through `read_map_cli` and rewrite the assignment line that
bash would read, whatever its spelling. It repairs `TOOL-dLinkedLibrary-57` and builds one step after it
(order 27).

## 2. Scope (IN)

- **S1** — The test. `up` (`tools/govkit/steps/retire_reuse_lookup.py`) decides whether `MAP_CLI` names
  the lookup by calling `read_map_cli` (`TOOL-dLinkedLibrary-69` S1) on the target's conf, never by
  matching the line's text. Observed by AC1.
- **S2** — The rewrite. Where it names the lookup, `up` rewrites the last line whose
  `parse_conf_assignment` key is `MAP_CLI`, and only that line: an `export ` prefix and a trailing `#`
  comment it held are kept, the value is written double-quoted as `{prefix}/codebase-map/house_index.py`
  (42 S2), and the file's line ends and every other byte are unchanged. Observed by AC1 and AC2.
- **S3** — The blank and foreign rows. A value `read_map_cli` reads as blank or as naming another file is
  left byte for byte, including a blank value whose line carries a trailing comment. Observed by AC2.

## 3. Non-goals (OUT)

- The witness and the one reader: `TOOL-dLinkedLibrary-69` (id 19).
- The before-image's coverage of the conf: `TOOL-dLinkedLibrary-74`'s item for id 13.
- Which value `MAP_CLI` takes in gov's own conf: `TOOL-dLinkedLibrary-42` S1, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-57` — S3's re-point rule for `up`, which S1 tests through the shared reader and S2 widens to every spelling (id 35)
- **consumes-from** `TOOL-dLinkedLibrary-69` — `read_map_cli`, the one reader S1 calls (id 35)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:5139-5143`: `CONF_KEY_RX` admits an `export` prefix, and
  `parse_conf_assignment` returns the key a line assigns.
- `tools/unattended/unattended.sh:617`: the kit sources the conf, so the last assignment is the one it
  reads.
- `tools/unattended/unattended.sh:10557-10559`: a `MAP_CLI` that names no file reads as "the map's range
  reader is not adopted here", with no refusal.

### Rollout

Order 27 beside `TOOL-dLinkedLibrary-69`. Both write `retire_reuse_lookup.py` and this unit calls 69's
reader, so BUILD-METHOD M6's clauses 1 and 2 sequence the two passes, 69 first.

### Files touched (estimate)

- `tools/govkit/steps/retire_reuse_lookup.py`: S1 to S3

### Alternatives rejected

- **Rewriting every `MAP_CLI` line.** Bash reads the last, so an earlier line is not the kit's value and
  rewriting it edits a byte the step does not need.
- **Writing the value back in its original quoting.** A double-quoted repository path is what 42 S2 and
  the shipped example (`tools/unattended/.unattended.conf.example:202`) spell; the original quoting
  carries no meaning bash keeps.

## 5. Production-readiness checklist

- security — `up`'s write set is 42's, one line of one file, imaged before the write.
- perf / scale — one pass over the conf.
- error / empty / loading states — a conf that does not decode makes `up` exit 1 naming it, before any
  write.
- observability — `up` prints the line it rewrote, before and after.
- risks — an operator's comment on the `MAP_CLI` line survives the re-point.
- testing — AC1 and AC2 by probe over scratch targets.
- migration — S2 is the step's own migration.
- user docs — none under `help/`: the step program's docstring states the rule.

## 6. Acceptance criteria

- **AC1** — When `python retire_reuse_lookup.py up <target>` runs over a scratch target under
  `%TEMP%/rl70a` whose conf assigns `MAP_CLI` the map kit's `reuse_lookup.py` in single quotes, then over
  one under `%TEMP%/rl70b` whose conf spells it `export` with a trailing `# map` comment, each conf
  afterwards yields the house index path under `bash -c '. <conf>; printf %s "$MAP_CLI"'`, and the second
  still opens `export` and ends `# map`.
  Red when: a lookup-naming value in either spelling is left in place.
- **AC2** — When the same `up` runs over a target under `%TEMP%/rl70c` whose conf reads a blank
  `MAP_CLI` followed by `# left blank`, the conf's bytes are unchanged, as `git hash-object` before and
  after shows.
  Red when: a blank value with a comment is rewritten or read as naming a file.

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

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 35 (HIGH, item
  H4).

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-69`'s `read_map_cli` and `govkit.parse_conf_assignment`
(`tools/govkit/govkit.py:5143`), the reader `up`'s test and its line choice both rest on. `python
tools/codebase-map/reuse_lookup.py "read a kit conf assignment line the way bash source reads it"` ranked
`read`, `read_text`, `load_conf`, `resolve_kit_dir` and `parse_conf`, none a line rewriter, so no existing
seam fits beyond the reader and the step being repaired.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
