**Serves:** journal TOOL-dWitnessedBar-16

# Brief — dWitnessedBar: TOOL-dWitnessedBar-16 revised over its first builder's divergence

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 16's first builder stopped at a divergence before writing any
code; the spec is revised by its writer before a second dispatch.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so a
builder can build it as written over HEAD.

### Items

1. Read the first builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-16-1-builder-return.md`, whole, and
   settle both its points in one revision:
   - The `refusal-retirements.txt` row keeps only unit, path and check, while its reader
     `tools/memory-tree/check-arms.py#check_retirements` also grades each row's R1 to R4 criteria, its survivor file,
     the survivor's signature join and its replay line, and `check-arms selftest` plants rows lacking a survivor or a
     replay. Either keep what the reader grades as verbatim key fields, or declare the survivor join retired with its
     selftest cases and a risk line saying so. The choice is a fork for item 3; S4's promise that every reader keeps its
     messages and exit codes must hold or be narrowed in so many words.
   - The `unarmed-branches.txt` row cannot register: `tools/lib/legacy_ledger.py#_check_table` refuses a `site` table
     with no `path` field, and its integer check field needs `verbatim`. Name the fields so each converted header
     registers, and do the same for `corpus-path-unresolved.txt`, `trace-waiver.txt` and `fork-ceilings.txt`'s integer
     `base`.
   Every other claim the builder probed held at `9b69042ee`; leave those as they are.
2. `memory/project/readme-contract.txt` is a shared record no pass may declare; the build brief already routes its
   converted bytes through the main loop, so the spec need not change for that. Leave carried clause tokens
   byte-identical; blob-pin only code-file line citations.
3. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-16`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/memory-tree/gen_build_index.py --check-coverage`,
and fix every finding about this spec they name. Write no numeric fact without an id, a path:line, PINNED or DERIVED on
its line.

### Acceptance

The three commands exit 0; the spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-16. No product code. No change to Goal or Scope intent beyond what the divergence
forces.

### Limitations

The status header keeps its status. The write grant is
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md` alone.

### Reuse

The spec's §10 seam, re-verified at HEAD.
