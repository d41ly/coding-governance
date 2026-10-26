**Serves:** research TOOL-dGroundRules-21

# Fold brief — the `policy fixtures` leg on every live spec's leg line, and three specs under the size ceiling

## The prompt

> A sweep of this build's specs read as INPROGRESS (a scratch clone, every DEFERRED header flipped, `python tools/check-spec-tokens.py` run once) found the same `[guards]` finding on 27 specs: §4's files touched names a path under `tools/policy/`, which trips the guard of the `policy fixtures` leg TOOL-dGroundRules-1 added after these specs were written, and §7's leg line lacks that leg. `--dispatch` refuses each such unit at check 49 the moment its builder flips the spec to INPROGRESS. The same sweep found three specs over the 49152-byte spec ceiling (`[size]`): `-21` by 358 bytes, `-25` by 494, `-34` by 108.

## The brief

### Goal
For each spec named below, under `memory/builds/dGroundRules/spec/`, add `policy fixtures` to §7's leg line; and bring `-21`, `-25` and `-34` under the 49152-byte ceiling. Author only: no product code, no commit, no gate.

### Items
1. Add `policy fixtures` to the §7 leg line of: `TOOL-dGroundRules-9`, `-15`, `-17`, `-18`, `-20`, `-21`, `-22`, `-23`, `-25`, `-27`, `-29`, `-31`, `-32`, `-33`, `-34`, `-35`, `-36`, `-37`, `-38`, `-39`, `-41`, `-43`, `-50`, `-52`, `-61`, `-62`. Spell the leg exactly as `tools/gate-legs.json` names it; change nothing else on the line.
2. Bring `-21`, `-25` and `-34` to at most 49152 bytes by moving history out of the spec, as the size finding says: condense the §9 revision log's older lines to one line each naming the rev, the date and what changed, never deleting a rev's line and never touching §1-§8 or §10.
3. Each spec touched gets its status header's rev raised by one and one §9 line: `policy fixtures` added to the leg line (and, for the three, the revision log condensed under the size ceiling); no design change.
4. Do not edit `TOOL-dGroundRules-10`: another writer holds it.

### Acceptance
In each touched spec the §7 leg line names `policy fixtures`; `-21`, `-25` and `-34` measure at most 49152 bytes (`wc -c`); every touched spec keeps its H1, `**Carries:**`/`**Derived:**` lines, §8 marks and every §9 rev; the status cells are unchanged.

### Gates
No gate runs in this pass; the main loop re-runs the sweep after the commit.

### Non-goals
Any change to a spec's design, criteria or files touched; specs not named; product code.

### Limitations
None beyond the items.

### Reuse
The sweep's output is the evidence; `tools/check-spec-tokens.py --list` prints the legs a path trips.
