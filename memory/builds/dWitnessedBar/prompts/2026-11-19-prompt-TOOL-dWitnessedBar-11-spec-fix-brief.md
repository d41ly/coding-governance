**Serves:** journal TOOL-dWitnessedBar-11

# Brief — dWitnessedBar: TOOL-dWitnessedBar-11 revised over its first builder's divergence

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 11's first builder stopped at a divergence before writing any
code, because units 12, 22 and 19 landed into the selfcheck block this spec retires after the spec was re-grounded.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD.

### Items

1. Read the first builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-11-1-builder-return.md`, whole, and
   settle all four of its points in one revision, against the tree at HEAD:
   - Unit 19's purpose block in selfcheck 7h (presence, shape and uniqueness arms, and its pending note): which arms
     leave govkit in this unit, whether presence stays in 7h until unit 51 adds it to `--conform` or is graded
     nowhere in the gap, whether uniqueness is part of the shape arm the gate table moves, and where
     `PURPOSE_MAX_CHARS` lives once the factory grades the shape, without a second copy or an import of govkit.
   - Selftest runs f to i (units 12, 22 and 19's plants): which move to `leg_factory.py --selftest`, under which arm,
     and which are deleted with the arms they grade.
   - The population of comments naming 7h has grown; re-derive it with the spec's own command and list every new
     member in Files touched with its guard's legs, including `tools/run-gates/run-gates.gov.test.sh`.
   - Files touched also gains the paths the builder named as owed: `memory/guides/SESSION-KICKOFF.md`, the
     codebase-map dossier that claims the two new legs, `memory/map/generated/symbols.json` and
     `memory/builds/dWitnessedBar/RUN.md`.
   Cite every moved line as `path#symbol` or blob-pinned.
2. Built so far, each landed on this branch: units 26, 27, 48, 49, 13, 50, 15, 12 (`6b3f271c6`), 61, 22 (`d92f12115`),
   47 and 19 (`e4e4e7ef0`). Units 14, 45 and 54 are being re-grounded beside this revision and read this spec as the
   contract; their specs are not yours to edit.
3. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-11` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no numeric
fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0; the spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-11. No product code. No change to Goal or Scope intent beyond what the divergence
forces.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md` alone.

### Reuse

The spec's §10 seam, re-verified at HEAD.
