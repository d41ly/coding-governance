**Serves:** journal TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-88

# Brief — dWitnessedBar: batch D of the live-spec token re-ground

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Its first `--dispatch` refused at check 49 because the spec-token checker
reds on a spec once it is live, and `check-spec-tokens.py --spec` over every remaining roster spec reds 101 hits in 48
specs. This batch re-grounds its share before any of them is dispatched.

## The brief

### Goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so
`python tools/check-spec-tokens.py --spec <that spec>` exits 0 and `--dispatch` will admit it.

### Items

1. For each spec, fix every hit listed under it, as the checker printed it on 2026-11-19 at `c6df3e901`:
   - `[guards]`: add the named leg to the §7 leg line, spelled as `tools/gate-legs.json` names it; or, where the path
     is not one the unit writes at HEAD, correct §4 Files touched and say why in the revision-log line.
   - `[leg]`: the token is not a leg name in `tools/gate-legs.json`; replace it with the leg that now carries that
     check, found by reading `tools/gate-legs.json`, or drop it when none does.
   - `[path]`: the cited path is not tracked; re-point it at the tracked file that holds the fact, or rewrite the
     citation so it no longer reads as a path.
   - `[bar]`: an acceptance observation spells a suite; rewrite it as the staged break, `--selftest` flag or fixture
     observation the checker names, keeping the suite on a `New arm:` line.
   - `[source]`: a shell file sourced by bare name; spell the sourcing through the kit-relative path the kit uses.
2. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. The write grant is this batch's spec files alone, each `memory/builds/dWitnessedBar/spec/2026-10-25-spec-<id>.md`: TOOL-dWitnessedBar-51, TOOL-dWitnessedBar-57, TOOL-dWitnessedBar-60, TOOL-dWitnessedBar-62, TOOL-dWitnessedBar-63, TOOL-dWitnessedBar-65, TOOL-dWitnessedBar-67, TOOL-dWitnessedBar-73, TOOL-dWitnessedBar-78, TOOL-dWitnessedBar-84, TOOL-dWitnessedBar-88.
3. The specs and their hits:
   - `TOOL-dWitnessedBar-51` (order 31):
     - [guards] `scratch-guard self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'scratch-guard self-test', absent from the §7 leg line
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the §7 leg line
     - [guards] `tier2-review self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'tier2-review self-test', absent from the §7 leg line
     - [guards] `policy fixtures <- AGENTS.md` — the Files touched list names AGENTS.md, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-57` (order 32):
     - [bar] `python measure_legs.py --selftest` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete; this spells the manifest leg `measure-legs selftest`, a suite by its declared ceiling of 500 s (PINNED, tools/gate-legs.json)
     - [guards] `playbook render selftest <- tools/memory-tree/corpus_ids.py` — the Files touched list names tools/memory-tree/corpus_ids.py, which trips the guard of leg 'playbook render selftest', absent from the §7 leg line
     - [guards] `policy fixtures <- tools/memory-tree/row_grammar.py` — the Files touched list names tools/memory-tree/row_grammar.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-60` (order 33):
     - [guards] `scratch-guard self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'scratch-guard self-test', absent from the §7 leg line
     - [guards] `tier2-review self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'tier2-review self-test', absent from the §7 leg line
   - `TOOL-dWitnessedBar-62` (order 34):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-63` (order 35):
     - [guards] `scratch-guard self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'scratch-guard self-test', absent from the §7 leg line
     - [guards] `tier2-review self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'tier2-review self-test', absent from the §7 leg line
     - [guards] `policy fixtures <- tools/govkit/govkit.py` — the Files touched list names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-65` (order 37):
     - [guards] `policy fixtures <- tools/govkit/govkit.py` — the Files touched list names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-67` (order 39):
     - [guards] `policy fixtures <- tools/govkit/govkit.py` — the Files touched list names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-73` (order 41):
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-78` (order 42):
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-84` (order 44):
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-88` (order 45):
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line

### Acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### Limitations

The write grant is this batch's spec files alone, each `memory/builds/dWitnessedBar/spec/2026-10-25-spec-<id>.md`:
TOOL-dWitnessedBar-51, TOOL-dWitnessedBar-57, TOOL-dWitnessedBar-60, TOOL-dWitnessedBar-62, TOOL-dWitnessedBar-63, TOOL-dWitnessedBar-65, TOOL-dWitnessedBar-67, TOOL-dWitnessedBar-73, TOOL-dWitnessedBar-78, TOOL-dWitnessedBar-84, TOOL-dWitnessedBar-88.

### Reuse

Not applicable: a re-ground of existing specs.
