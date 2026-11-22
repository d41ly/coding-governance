**Serves:** journal TOOL-dBoundRoles-5 TOOL-dBoundRoles-10 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-4 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-12 TOOL-dBoundRoles-41 TOOL-dBoundRoles-11 TOOL-dBoundRoles-26

# Brief — dBoundRoles: batch C of the live-spec token re-ground

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. `check-spec-tokens.py --spec` over every roster spec reds 42 of 59 specs at
`062906ffd`, and `--dispatch` refuses a spec the checker reds. This batch re-grounds its share before any is dispatched.

## The brief

### Goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so
`python tools/check-spec-tokens.py --spec <that spec>` exits 0 and `--dispatch` will admit it.

### Items

1. For each spec, fix every hit listed under it, as the checker printed it on 2026-11-22 at `062906ffd`:
   - `[guards]`: add the named leg to the Gates leg line, spelled as `tools/gate-legs.json` names it; or, where the
     path is not one the unit writes at HEAD, correct Files touched and say why in the revision-log line.
   - `[cite]`: the citation names a line of `tools/hooks/agent-cap.js` as it stood at the chain baseline `59ff8f2ac`
     (2427 lines); TOOL-dFairHearing-16 has since moved rules 0, 2 and 5 to the review kit and the file is 1227 lines.
     Find the cited function or constant at HEAD (`git show 59ff8f2ac:tools/hooks/agent-cap.js | sed -n '<N>p'` names
     it; grep HEAD for that name) and re-point the line, or the range, at where it lives now, in whichever file holds
     it. Where the code the spec relies on is gone or changed in behaviour, re-ground the dependent sentence too and
     name the change in the revision-log line.
2. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. The write grant is this
   batch's spec files alone, listed under Limitations.
3. The specs and their hits:
   - `TOOL-dBoundRoles-5` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-10` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md`):
     - [guards] `policy fixtures <- tools/hooks/scratch-guard.js` — the Files touched list names tools/hooks/scratch-guard.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2089` — file has 1227 lines
   - `TOOL-dBoundRoles-39` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-39.md`):
     - [guards] `policy fixtures <- tools/roles/handoff.py` — the Files touched list names tools/roles/handoff.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2102` — file has 1227 lines
   - `TOOL-dBoundRoles-40` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-40.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-4` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/handoff.py` — the Files touched list names tools/roles/handoff.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2089` — file has 1227 lines
   - `TOOL-dBoundRoles-23` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-24` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2135` — file has 1227 lines
   - `TOOL-dBoundRoles-12` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md`):
     - [guards] `policy fixtures <- tools/roles/handoff.py` — the Files touched list names tools/roles/handoff.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2135` — file has 1227 lines
   - `TOOL-dBoundRoles-41` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-41.md`):
     - [guards] `policy fixtures <- tools/roles/handoff.py` — the Files touched list names tools/roles/handoff.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-11` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md`):
     - [guards] `routed-commits selftest <- tools/policy/catalogue.toml` — the Files touched list names tools/policy/catalogue.toml, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the Gates leg line
     - [guards] `scratch-guard self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `tier2-review self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'tier2-review self-test', absent from the Gates leg line
   - `TOOL-dBoundRoles-26` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md`):
     - [guards] `scratch-guard self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `tier2-review self-test <- tools/unattended/unattended.sh` — the Files touched list names tools/unattended/unattended.sh, which trips the guard of leg 'tier2-review self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2077` — file has 1227 lines

### Acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-39.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-40.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-41.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-11.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md`

### Reuse

Not applicable: a re-ground of existing specs.
