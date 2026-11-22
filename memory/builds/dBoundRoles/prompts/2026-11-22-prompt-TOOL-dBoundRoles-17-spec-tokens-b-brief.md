**Serves:** journal TOOL-dBoundRoles-17 TOOL-dBoundRoles-6 TOOL-dBoundRoles-13 TOOL-dBoundRoles-3 TOOL-dBoundRoles-38 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-7

# Brief — dBoundRoles: batch B of the live-spec token re-ground

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
   - `TOOL-dBoundRoles-17` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2044` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2049` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2044` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-6` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md`):
     - [guards] `routed-commits selftest <- tools/policy/guarded-paths.txt` — the Files touched list names tools/policy/guarded-paths.txt, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/hooks/scratch-guard.js` — the Files touched list names tools/hooks/scratch-guard.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2282` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-13` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-3` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2089` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-38` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2048` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2048` — file has 1227 lines at 062906ffd
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2048` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-45` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-46` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2048` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-48` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-48.md`):
     - [guards] `format-guard self-test <- tools/hooks/agent-cap.js` — the Files touched list names tools/hooks/agent-cap.js, which trips the guard of leg 'format-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-8` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-8.md`):
     - [guards] `policy fixtures <- tools/hooks/scratch-guard.js` — the Files touched list names tools/hooks/scratch-guard.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js@d4c072df:2278` — file has 1227 lines at 062906ffd
   - `TOOL-dBoundRoles-9` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-9.md`):
     - [guards] `policy fixtures <- tools/hooks/scratch-guard.js` — the Files touched list names tools/hooks/scratch-guard.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-7` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md`):
     - [guards] `policy fixtures <- tools/hooks/scratch-guard.js` — the Files touched list names tools/hooks/scratch-guard.js, which trips the guard of leg 'policy fixtures', absent from the Gates leg line

### Acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-48.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-8.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-9.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md`

### Reuse

Not applicable: a re-ground of existing specs.
