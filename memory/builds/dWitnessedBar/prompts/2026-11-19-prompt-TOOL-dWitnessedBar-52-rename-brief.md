**Serves:** journal TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-84

# Brief — dWitnessedBar: TOOL-dWitnessedBar-52's conf read renamed to a declared verb

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 52's first builder stopped before writing code: the spec names
its new function `root_confs`, which `lexicon naming predicates` refuses because it leads with no declared verb, and
raising `VERB_OFFENDER_PIN` in `.lexicon.conf` is outside the unit's write set.

## The brief

### Goal

Revise each spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem, so
the function unit 52 adds carries a name `python tools/lexicon/lexicon.py --suggest <name> --as py.function` accepts.

### Items

1. Read the builder's return, `build/2026-11-19-build-TOOL-dWitnessedBar-52-1-builder-return.md`, whole.
2. Rename `root_confs` in TOOL-dWitnessedBar-52 everywhere it is named: S1, S3, §4 The read and Inventory, AC2, AC3
   and the §7 `New arm:` line. The return names `read_root_confs` as accepted; choose it unless the lexicon accepts a
   better-fitting declared verb, and run `--suggest` on the name you choose.
3. Unit 17 landed the conf walk as `tools/memory-tree/ratchet.py#read_root_conf_lines`; restate unit 52's seam over
   it where the spec still describes the walk unit 17 replaced. Add `memory/map/generated/symbols.json` to Files
   touched, since a new definition makes the map stale.
4. Align the name in TOOL-dWitnessedBar-53, TOOL-dWitnessedBar-62 and TOOL-dWitnessedBar-84, which cite it. Leave the
   CLOSED specs 14 and 17 as they stand.
5. A choice the revision forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. Leave carried clause tokens byte-identical;
   blob-pin only code-file line citations.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-84`,
`python tools/check-spec-tokens.py --spec <path>` over each, `python tools/playbook/writing_practice.py check pinned-facts`
and `python tools/memory-tree/gen_build_index.py --check-coverage`, and fix every finding about these specs they name.
Write no numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

The four commands report nothing against these specs; no open spec names `root_confs`; each revised spec carries
the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve) · lexicon naming predicates

### Non-goals

No spec outside the four named. No product code. Each status header keeps its status.

### Limitations

The write grant is `memory/builds/dWitnessedBar/spec/2026-10-25-spec-<id>.md` for TOOL-dWitnessedBar-52,
TOOL-dWitnessedBar-53, TOOL-dWitnessedBar-62 and TOOL-dWitnessedBar-84.

### Reuse

Unit 16's renames to declared verbs, recorded beside `VERB_OFFENDER_PIN` in `.lexicon.conf`, as precedent.
