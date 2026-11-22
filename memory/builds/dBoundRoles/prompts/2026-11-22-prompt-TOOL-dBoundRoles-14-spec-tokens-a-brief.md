**Serves:** journal TOOL-dBoundRoles-14 TOOL-dBoundRoles-2 TOOL-dBoundRoles-1 TOOL-dBoundRoles-21 TOOL-dBoundRoles-37 TOOL-dBoundRoles-22 TOOL-dBoundRoles-49 TOOL-dBoundRoles-16 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-15

# Brief — dBoundRoles: batch A of the live-spec token re-ground

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
   - `TOOL-dBoundRoles-14` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md`):
     - [guards] `policy fixtures <- tools/playbook/tag_index.py` — the Files touched list names tools/playbook/tag_index.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-2` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-1` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`):
     - [guards] `policy fixtures <- tools/roles/agents/` — the Files touched list names tools/roles/agents/, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2157` — file has 1227 lines
   - `TOOL-dBoundRoles-21` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md`):
     - [guards] `routed-commits selftest <- tools/policy/catalogue.toml` — the Files touched list names tools/policy/catalogue.toml, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `scratch-guard self-test <- tools/policy/catalogue.toml` — the Files touched list names tools/policy/catalogue.toml, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-37` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-37.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-22` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-49` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-49.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-16` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2179` — file has 1227 lines
   - `TOOL-dBoundRoles-54` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-55` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-15` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md`):
     - [guards] `routed-commits selftest <- tools/policy/caps.toml` — the Files touched list names tools/policy/caps.toml, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `scratch-guard self-test <- tools/policy/caps.toml` — the Files touched list names tools/policy/caps.toml, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line

### Acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-37.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-49.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md`

### Reuse

Not applicable: a re-ground of existing specs.
