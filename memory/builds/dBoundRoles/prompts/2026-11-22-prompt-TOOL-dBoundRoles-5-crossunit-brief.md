**Serves:** journal TOOL-dBoundRoles-5 TOOL-dBoundRoles-4 TOOL-dBoundRoles-12 TOOL-dBoundRoles-23 TOOL-dBoundRoles-39 TOOL-dBoundRoles-41 TOOL-dBoundRoles-3 TOOL-dBoundRoles-24 TOOL-dBoundRoles-13

# Brief — dBoundRoles: the cross-unit corrections the re-ground batches surfaced

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. The re-ground batches of build orders 3 to 31 surfaced corrections each
outside its own grant, and the main loop overrode two delegated fork resolutions. This pass folds them all before any
of these units is dispatched.

## The brief

### Goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so the corrections below hold.

### Items

1. Units 5, 4, 12, 23 and 39: rename `validate_return` to `check_return`, the name the lexicon answers, everywhere
   each spec spells it. Unit 5: rewrite §8 F7 to that resolution, RESOLVED (agent, 2026-11-22, delegated), rung 1,
   `widens: none · relaxes: none`, because raising the lexicon's verb pin moves a declared ceiling, which is the
   owner's; drop `.lexicon.conf` from its Files touched and any criterion or leg that re-measures the pin.
2. Unit 23: rewrite §8 F6 to keep F3's floor, so a run's own change to the policy file is never read as the owner's
   write under `owner-only`, RESOLVED (agent, 2026-11-22, delegated), `widens: none · relaxes: none`; the other
   option widens a security surface past the unit's tier (M3 veto 3). S6 and §1 keep "only by the owner's explicit
   write".
3. Unit 41: its AC2 renders `--role gov-builder` with `--input question=`, which exits 2 at HEAD because
   `gov-builder` reads no `input:question`. Move the pair to `gov-orienter` with `--input prompt=`, as unit 47's
   F2 and unit 52's S1 state, keeping AC2's number.
4. Unit 3: state the heading level of S2's `### inputs` sub-blocks so unit 48's S3 admits every work order unit 3
   renders, checked against unit 48's spec.
5. Unit 24: its S2 relies on unit 38's `read_unfenced_lines`; add the edge to unit 38 its §3 Edges owes, in the edge
   grammar `memory/TEMPLATE-SPEC.md` states.
6. Unit 13: its build pushes the unattended Skill's render past its size row, which has no headroom at HEAD; add the
   `unattended skill size` leg to its Gates leg line, and state in its Rollout which of the size file's stated raise
   terms its build takes, or the trim, as unit 44's F4 puts it.
7. Change nothing else. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Each status stays
   `DEFERRED`; one revision-log line per spec names this brief by its file stem.
8. `python tools/check-spec-tokens.py --spec <path>` and `check-memory-hygiene.sh --only 12 --spec <path>` exit 0 for
   each before you return.

### Acceptance

Each item is folded where it names; each spec carries the next rev; both checks exit 0 for each.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the items.

### Limitations

The write grant is these specs alone:
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-5.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-4.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-12.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-23.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-39.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-41.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-3.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-24.md`
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md`

### Reuse

Each spec's own §10.
