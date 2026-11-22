**Serves:** journal TOOL-dWitnessedBar-20

# Brief — dWitnessedBar: TOOL-dWitnessedBar-20 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The run's first two builders each stopped at a divergence, because the
specs were written at `cdfbd1cf` and the tree has moved since; each spec is now re-grounded before its dispatch.

## The brief

### Goal

Revise each spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read each spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge. Re-derive each PINNED count with the command the
   spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every new member listed
   in Files touched with the legs its guard names on the gates section's leg line, and a prose-only mention named as
   outside the population. Cite moved code-file lines as `path#symbol` or blob-pinned, never a bare `path:line`; leave a carried clause token byte-identical.
   What is built so far:
   - Built and landed through order 12: units 26, 27, 48, 49, 13, 50, 15, 12, 61, 22, 47, 19, 11, 14, 45, 54, 16
     (`3a7a51471`, `450f7b322`: gov's registries on the ledger, homes once under `tools/` moved to `memory/project/`,
     the step program `tools/govkit/steps/registry_to_ledger.py`), 46, 17 (`9a29f1e96`: `{prefix}` resolved in seed
     argvs by the factory), 52 (`6a075440b`), 53 (`3ab7c7312`) and 18 (`c91fc4e55`: the playbook lists registered,
     `memory/project/instructions-legacy.txt` moved off the tool root).
   - A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`, which takes no waiver:
     `tools/lib/legacy_ledger.py#read_registrations` reads `home` literally, so a home under the tool root names
     nothing at an adopter installed elsewhere. Unit 16 moved four such homes to `memory/project/`; unit 18 moved
     `instructions-legacy.txt` the same way.
2. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return.
3. Settle where `legacy-homes.txt`'s ledger home lives so `install-prefix (shipped surface)` stays green: a home
   outside the tool root (as units 16 and 18 moved theirs), or another route the landed factory reads literally.
   Restate S1, S2, S7, S10, Files touched and every reader that names the path. The choice is a fork for item 2.
Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-20` and
`python tools/check-spec-tokens.py --spec <path>` over each spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for every spec; each spec carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dWitnessedBar-20. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

Each status header keeps its status. The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md` alone.

### Reuse

Each spec's §10 seam, re-verified at HEAD.
