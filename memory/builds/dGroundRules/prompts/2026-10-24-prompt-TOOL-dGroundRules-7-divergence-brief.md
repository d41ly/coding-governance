**Serves:** research TOOL-dGroundRules-7

# Divergence brief — TOOL-dGroundRules-7, which report a row no home yields gets

## The prompt

> Its builder handed TOOL-dGroundRules-7 back as a DIVERGENCE: §4 "The check and the write" item 1 reports any committed row the derivation does not yield as `legacy homes: typed row <row>`, while §6 AC7's `shrink` case (a key removed from the fixture's `.unattended.conf`, its row still listed) requires the stale-list report, which item 2 gives only to a derived row the list lacks. Item 3 also leaves open whether "a derived row the list at the landed revision lacks" compares the full `<home> <key> <mark>` or the pair (home, key).

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md` to the run's ruling (B), the option that keeps both AC2's and AC7's observations. Author only: no product code, no commit, no gate.

### Items
1. §4 item 1 splits. A committed row that no home yields, and whose (home, key) the list at the landed revision holds, reports the stale-list report (its key left its home; `--write` drops it). A committed row that no home yields and that the landed list lacks reports `legacy homes: typed row <row>` (AC2's planted row). A hand-edited mark whose (home, key) is still derived stays the typed-row report.
2. Item 3's identity is the pair (home, key), never the full row, so a re-marked `GATE_ENV_MARKS` entry is a mark change `--write` can write, not a new legacy home.
3. AC2 and AC7 each name the report their plant reaches under items 1 to 3; add a red-when to AC7 for the typed-row report printed in the shrink case.
4. §4's Files touched adds `tools/policy/README.md`: `arm_legacy_homes` joins `ARMS`, and TOOL-dGroundRules-16's `adopter-fresh-target` case joins that README's "Each arm in an adopter" table to `ARMS` both ways.
5. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` exits 0; items 1 to 3 give each AC2 and AC7 plant exactly one report; every `**Carries:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
Ruling (A), AC7 renamed to the typed-row report with a separate hand-deleted-row case, was set aside: it is the narrower option, since it drops the distinction between a planted row and a key that left its home (BUILD-METHOD M3, the most feature-rich survivor).

### Reuse
The builder's probes at HEAD: 102 kit-conf rows after the `_CUTOFF`/`_PIN` filter, 11 gate-env keys matching the mark table, `lists --check` green.
