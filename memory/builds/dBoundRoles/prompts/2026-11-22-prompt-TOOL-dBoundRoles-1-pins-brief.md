**Serves:** journal TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-10 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-46 TOOL-dBoundRoles-58

# Brief — dBoundRoles: the re-grounded specs' citations and figures pinned

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. The pass legs after TOOL-dBoundRoles-14's pass commit `7a58950fb` red
two legs on specs this run re-grounded: `positional (the citation check alone)` on line citations that carry no
blob pin, and `writing practice (records and units)` on figures with no pin on their line. Both legs were green at the
run's base `8b8b1374`, so these reds are this run's.

## The brief

### Goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so neither leg names it.

### Items

1. For each `[positional]` hit: cite the code as `path#symbol`, or pin the line to the blob it was read at, as
   `path@<blob8>:<line>`. `python tools/playbook/positional.py pin <spec>` pins a full-path citation to its HEAD blob;
   a basename citation needs its full path first. A citation of the chain baseline (`59ff8f2ac`) pins to that commit's
   blob of the file (`git rev-parse 59ff8f2ac:<path>`), never to HEAD's.
2. For each `[pinned-facts]` hit: put a pin on that line — a bare sha of the commit the figure was read at, a
   `path:line`, or the word `DERIVED` naming what derives it. Text inside backticks does not count as a pin.
3. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. One revision-log line per
   spec names this brief by its file stem.
4. Before you return, `python tools/playbook/positional.py check` and `python tools/playbook/writing_practice.py check`
   name none of these specs, and `python tools/check-spec-tokens.py --spec <path>` exits 0 for each.
5. The specs: each one either check names at HEAD. Read each hit from the two checks' own output rather than
   from this brief, which quotes none so that it reds neither.
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-8.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`
   - `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md`
   - `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md`
   - `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-39.md`
   - `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md`
   - `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`

### Acceptance

Neither check names any spec of this batch; spec tokens exit 0 for each; each spec carries the next rev and one
revision-log line naming this brief.

### Gates

positional (the citation check alone) · writing practice (records and units) · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch, and never `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md`, which
is CLOSED. No register under `memory/project/`. No product code.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-6.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-7.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-8.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-17.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-20.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-25.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-26.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-38.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-39.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-46.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`

### Reuse

`tools/playbook/positional.py pin`, the checker's own remedy.
