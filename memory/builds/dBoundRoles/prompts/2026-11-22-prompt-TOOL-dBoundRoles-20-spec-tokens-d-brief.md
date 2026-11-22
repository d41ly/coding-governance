**Serves:** journal TOOL-dBoundRoles-20 TOOL-dBoundRoles-19 TOOL-dBoundRoles-18 TOOL-dBoundRoles-25 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-50 TOOL-dBoundRoles-58 TOOL-dBoundRoles-60

# Brief — dBoundRoles: batch D of the live-spec token re-ground

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. `check-spec-tokens.py --spec` over every roster spec reds 42 of 59 specs (DERIVED by --plan --paths) at
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
     (2427 lines at 59ff8f2ac); TOOL-dFairHearing-16 has since moved rules 0, 2 and 5 to the review kit and the file is 1227 lines at 062906ffd.
     Find the cited function or constant at HEAD (`git show 59ff8f2ac:tools/hooks/agent-cap.js | sed -n '<N>p'` names
     it; grep HEAD for that name) and re-point the line, or the range, at where it lives now, in whichever file holds
     it. Where the code the spec relies on is gone or changed in behaviour, re-ground the dependent sentence too and
     name the change in the revision-log line.
2. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. The write grant is this
   batch's spec files alone, listed under Limitations.
3. The specs and their hits:
   - `TOOL-dBoundRoles-20` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md`):
     - [guards] `policy fixtures <- tools/playbook/tag_index.py` — the Files touched list names tools/playbook/tag_index.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2157` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-19` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md`):
     - [guards] `policy fixtures <- tools/roles/kit.toml` — the Files touched list names tools/roles/kit.toml, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-18` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md`):
     - [guards] `policy fixtures <- tools/govkit/upgrade_steps.py` — the Files touched list names tools/govkit/upgrade_steps.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-25` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`):
     - [guards] `playbook render selftest <- tools/lexicon/lexicon.py` — the Files touched list names tools/lexicon/lexicon.py, which trips the guard of leg 'playbook render selftest', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/kit.toml` — the Files touched list names tools/roles/kit.toml, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-43` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-43.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-44` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-44.md`):
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the Gates leg line
   - `TOOL-dBoundRoles-50` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-58` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2051` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-60` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md`):
     - [guards] `govkit selftest <- tools/govkit/registry.toml` — the Files touched list names tools/govkit/registry.toml, which trips the guard of leg 'govkit selftest', absent from the Gates leg line
     - [guards] `govkit refusal join <- tools/govkit/registry.toml` — the Files touched list names tools/govkit/registry.toml, which trips the guard of leg 'govkit refusal join', absent from the Gates leg line
     - [guards] `govkit acceptance matrix <- tools/govkit/registry.toml` — the Files touched list names tools/govkit/registry.toml, which trips the guard of leg 'govkit acceptance matrix', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/govkit/registry.toml` — the Files touched list names tools/govkit/registry.toml, which trips the guard of leg 'policy fixtures', absent from the Gates leg line

### Acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-19.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-18.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-43.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-44.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md`

### Reuse

Not applicable: a re-ground of existing specs.
