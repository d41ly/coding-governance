**Serves:** research DEPL-dShippedRelease-78

# Brief: DEPL-dShippedRelease-78 S59 names the surface its lease-epoch re-read goes through

## The prompt

> fix, take recommendations on the forks, land it

— owner, 2026-11-03, on the report of the parents cross-check of dMindYourWords, dShippedRelease,
dScopedBuild and dTendedCadence. The report listed one gap of this build's own, under "Follow-ups
outside this pass" in
`memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`:
sr78 S59 "re-reads the lease epoch" of its own release lease and names no surface for that read.

## The brief

### Goal

S59 names the read-only surface the rest of this build already uses for a lease's epoch,
TOOL-dPlacedRequest-34 S22's `--lease status`. The exit-3 behaviour does not change.

### Items

All in `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-78.md`.

1. **S59 (line 176).** The lease is the run lease unit 15 takes with `--lease acquire run release <E>`
   (DEPL-dShippedRelease-15, line 81). Read that line first and check the kind, name and sub.
   - Name the re-read as TOOL-dPlacedRequest-34 S22's `unattended.sh --lease status run release <E>`,
     using its sixth TAB field. This is the field and parser DEPL-dShippedRelease-138 S48's
     `read_lease_epoch` reads for the build lease.
   - S48's `read_lease_epoch` takes only `build <slug>`. Do not widen S48 here. Say that S59 reads
     the same field of the same verb for the run lease, and that `lease — none · <tail>` reads as
     not the holder.
   - If unit 15's text gives a kind, name or sub other than `run release <E>`, use unit 15's and say
     so in the return.
2. Keep S59 a single bullet and keep its `Observed by AC49.` sentence. Change no other S-item.

### Each revision

- Bump the **Status:** line from `rev-3` to `rev-4`, dated 2026-11-03. Keep the status word
  `DEFERRED` and every other field.
- Add one §9 line in the existing form, naming S59 and this brief.
- Re-open no fork and resolve none.

### Acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-4`, and §9 holds the new line.
- `grep -n -- "--lease status" <spec>` prints S59's line.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`. It names none of your spec's lines. A finding
  that only a `gen_build_index.py --write` render cures belongs to the main loop: name it and leave it.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No file outside spec 78. No commit, no staging into the real index and no deviation record.
- No edit to DEPL-dShippedRelease-15, -138 or any dPlacedRequest spec.

### Reuse

DEPL-dShippedRelease-138 S48's `read_lease_epoch` and TOOL-dPlacedRequest-34 S22's `--lease status`.
