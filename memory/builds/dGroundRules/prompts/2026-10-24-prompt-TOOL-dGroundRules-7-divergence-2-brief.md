**Serves:** research TOOL-dGroundRules-7

# Divergence brief 2 — TOOL-dGroundRules-7, the legacy list spelled without an install prefix

## The prompt

> Its builder handed TOOL-dGroundRules-7 back a second time as a DIVERGENCE: the merge bar's `install-prefix (shipped surface)` leg (`tools/check-install-prefix.sh`, a pure ban with no waiver) reads every tracked file under the tool root, `.txt` included, and refuses any `tools/<kit>` spelling. The spec puts the generated list at `tools/policy/legacy-homes.txt` and requires it to hold `tools/roles/house/policy.toml` rows (§4 Data model and the derivation table; AC5's grep) and a header naming `python tools/policy/policy.py lists --write`; both are offenders, and so is item 3's report text if typed as a literal in `policy.py`.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-7.md` so nothing it writes under the tool root spells `tools/<kit>`. Author only: no product code, no commit, no gate.

### Items
1. §4 Data model and the house row of the derivation table spell the house home with the drained token `<tool-root>/roles/house/policy.toml`, which is also right in an adopter installed at another prefix; the reader resolves the token from the kit's own location.
2. AC5's grep becomes `grep "^<tool-root>/roles/house/policy.toml " legacy-homes.txt`.
3. The list's header names `python <this kit>/policy.py lists --write`, as `tools/policy/unsummarised-keys.txt` already does; verify its spelling there before writing it.
4. Item 3's report text names the catalogue through a path derived from the kit's location at runtime, never a literal, and the spec says so.
5. §7 names `install-prefix (shipped surface)` among the legs the close runs; re-run `python tools/check-spec-tokens.py --list` against the files touched.
6. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling.

### Acceptance
`python tools/check-spec-tokens.py` exits 0; no token the spec requires inside a file under `tools/` spells `tools/<kit>`; every `**Carries:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass; the close runs the spec's §7 legs.

### Non-goals
Moving the list out of the tool root (TOOL-dGroundRules-17 consumes `tools/policy/legacy-homes.txt`); any other spec; the status cell, which stays `DEFERRED`.

### Limitations
The builder's measured figures stand: 102 kit-conf rows, 11 gate-env keys, the house file's `[effort]` and `[gates]` tables.

### Reuse
`tools/policy/unsummarised-keys.txt`'s header is the drained-token precedent.
