# TOOL-dClosedLexicon-11 — a build may have more than one unattended run

**Status:** SPECCED · rev-1 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

The unattended kit allows exactly ONE run per build folder, and nothing says so. `--preflight` writes
`<MEMORY_ROOT>/builds/<slug>/RUN.md`; once that record reaches a terminal phase, `refuse_if_terminal`
(`unattended.sh:574`) refuses every verb that would write it, including `--preflight`:

> the run is already finished and a finished record is not something to move, re-open or re-pin

That refusal is RIGHT about the record and WRONG as a policy about the build. Hit for real on
2026-08-16: this build's first run ABORTED, three units remained, and the second run could not start
— the remaining work proceeded on an explicit owner ask instead, outside the machinery meant to make
an unattended run checkable. A build that aborts once can never be carried unattended again.

## 2. Scope (IN)

- **S1** — `--preflight` on a build whose run-state file is TERMINAL ROTATES that record to an
  immutable archive name and creates a fresh `RUN.md`. It refuses if the archive name already exists,
  rather than overwriting a finished record.
- **S2** — the archive name is `RUN.<phase>.<witness8>.md`, derived from the record being retired:
  both halves come from facts the finished record already carries, so the name cannot be chosen and
  two runs cannot collide unless they ended at the same phase AND the same witness, which is the same
  run.
- **S3** — `check-unattended.sh`'s population becomes `RUN.md` PLUS `RUN.*.md`. Every archived record
  must be terminal; the live-run rule ("at most one in a non-terminal phase") is unchanged and now
  quantifies over the wider set, which is what makes rotation safe rather than a way to hide a second
  live run.
- **S4** — protocol §2 records rotation as the way a build gets a second run, and states what it does
  NOT do: it does not re-open, re-pin or edit the retired record, whose bytes are preserved.
- **S5** — arms in `tools/unattended/unattended.test.sh` and `check-unattended.test.sh`: preflight
  over a terminal record rotates and starts fresh; the archived bytes are IDENTICAL to what was
  retired; a second rotation with a colliding name REFUSES; a NON-terminal record is still refused by
  every verb that refused it before; and the leg reds on an archived record left in a live phase.

## 3. Non-goals (OUT)

- Relaxing `refuse_if_terminal` for any other verb. `--phase`, `--close`, `--landed` and `--abort`
  keep refusing a finished record. Only `--preflight` gains the rotation, because only `--preflight`
  is the start of something new.
- Editing a retired record's CONTENT in any way. Rotation is a rename; the bytes are asserted equal.
- A run counter, a run id, or an index of runs. The archive names ARE the enumeration; a second
  spelling of the same population is the class this repo has a record about.
- Any change to what a run may DO. This is about how many runs a build may have, not their powers.

## 4. Design

### Why rotate rather than reopen

The refusal protects a real property: a later run is measured against the counter a finished record
left, so re-opening one destroys the evidence a reader needs. Rotation keeps that property intact —
the finished record still exists, still says what it said, and is still readable — while removing the
policy nobody chose, that a build gets one run.

The alternative shapes were considered and are worse. Allowing `--preflight` to overwrite destroys
the record. A `runs/<seq>.md` directory changes the path shape every reader globs and collides with
hygiene check 4's folder grammar. A `--force` flag makes the destructive path the one an operator
reaches for when blocked, which is exactly when they should not have it.

### The name carries its own provenance

`RUN.<phase>.<witness8>.md` is DERIVED from the retired record rather than chosen. That is what makes
the refusal-on-collision meaningful: two runs producing the same archive name ended at the same phase
on the same commit, which is one run archived twice, and refusing is correct.

### Data model

No conf key. The run-state file's authored facts are unchanged; `units-at-landing` already freezes
what a terminal record must answer, which is what makes an archived record still useful.

### Files touched (estimate)

`tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, their two self-tests,
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (kept byte-equal
by check 15), and the kit version pair.

## 5. Production-readiness checklist

- security — a run cannot use rotation to escape the anchor: `--preflight` re-observes the remote and
  re-pins BASE exactly as it does on a first run. Rotation happens BEFORE those checks, so a refusal
  still leaves no fresh record.
- perf / scale — one rename per new run.
- a11y / i18n — N/A.
- error / empty / loading states — a build with no prior record is the unchanged path; a build whose
  record is NON-terminal is still refused.
- observability — the rotation is printed with both names, so an operator sees what was retired.
- risks — the real one is rotating a record that is not actually finished. The terminal test is the
  same `is_terminal` the rest of the kit uses, and S5 arms the non-terminal refusal.
- testing + left-shift gates — S5, on two legs that already ride the bar.
- migration / rollback — none; existing records keep their names until a second run rotates them.
- user docs — protocol §2 (S4) and the Skill's "Start a run" step.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a build whose `RUN.md` is `ABORTED` or `LANDED`, it rotates
  that file to `RUN.<phase>.<witness8>.md` and writes a fresh `RUN.md`, and both exist afterwards.
- **AC2** — When the rotation happens, `cmp -s` between the archived file and a copy of the retired
  record taken before the call reports them byte-IDENTICAL.
- **AC3** — When a rotation would overwrite an existing archive name, `--preflight` REFUSES and
  writes nothing.
- **AC4** — When the run-state file is NON-terminal, `--preflight` still refuses exactly as before.
- **AC5** — When an archived record is left in a non-terminal phase, `check-unattended.sh` reds.
- **AC6** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`bash tools/unattended/check-unattended.sh`, `bash tools/unattended/check-unattended.test.sh`,
`bash tools/unattended/unattended.test.sh`, `bash tools/unattended/adopt-unattended.sh --check`. No
new leg; arms are added to legs already on the bar.

## 8. Open questions

- **F1 — should the archive live in the build folder or under `archive/`?** RESOLVED (agent,
  2026-08-17, delegated): the build folder. The memory tree's `archive/` holds ROTATED index shards
  whose rotation is a size decision; a retired run record is build state and belongs beside the build
  it describes, where `--resume` and the leg already look. Moving it would put the record outside the
  population every existing reader globs, for no gain.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, written from the refusal that was hit on 2026-08-16 rather than
  from the backlog row's summary.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "retire a record and start a fresh one"` surfaces the
memory-tree kit's index ROTATION (`memory/archive/<FAMILY>.<date>.md`), which is the nearest seam and
the precedent for "the retired copy is byte-identical and still readable". This unit reuses that
DISCIPLINE, not its code: rotation there is size-triggered over an index, here it is
terminal-triggered over one record. `refuse_if_terminal` is the single branch every phase-writer
already routes through (`unattended.sh:574`), so S1 extends one call site rather than adding a second
rule — the shape that file's own comment argues for.
