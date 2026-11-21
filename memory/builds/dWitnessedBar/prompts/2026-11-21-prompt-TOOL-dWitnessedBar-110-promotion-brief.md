**Serves:** journal TOOL-dWitnessedBar-110

# Brief — dWitnessedBar: TOOL-dWitnessedBar-110, the round-2 closing review's five minors batched

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The closing diff review's round 2 (`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-106-closing-diff-review-round2.md`) read CLEAN WITH
FIXES and NON-CONVERGENT, so its loop stopped and every confirmed finding is promoted to a
unit while the rework budget remains (`memory/guides/UNATTENDED-VERBS.md`, "Review rounds, and the loop that ends
itself").

## The brief

### Goal

Write the NEW spec `memory/builds/dWitnessedBar/spec/2026-11-21-spec-TOOL-dWitnessedBar-110.md` for
TOOL-dWitnessedBar-110, a Tier-2 unit at `order 51` with status DEFERRED, rev-1, that closes M1 (finding 1), M2 (finding 4), L1 (finding 3), L2 (finding 7) and L3 (finding 8) of that review
record by their mechanism, so a builder can build it as written over HEAD.

### Items

1. Read the review record's sections for M1 (finding 1), M2 (finding 4), L1 (finding 3), L2 (finding 7) and L3 (finding 8) whole: the finding, its reachable path, the skeptic's
   class-level fix (the one the record carries, never the finder's instance fix) and its left-shift gate. The spec's
   design is that class fix, re-derived against the code at HEAD; settle every path, symbol and count it names.
   M1 and L2 are `tools/run-gates/verdict_backends.py#run_verify_peer` and its `peer-stale-slot` plant; M2 is `tools/unattended/unattended.sh#check_commit_message`'s handling of `ATTRIBUTION unarmed`; L1 is the whitespace rule of the attribution value and last-line checks in the three `commit_trailers.py` copies; L3 is a root dotted-key fixture row for `.githooks/pre-push#scan_policy_bytes` in `.githooks/pre-push.test.sh`. Unit 109 builds first and owns the attribution reader; build L1 over its landed shape.
2. Follow `memory/TEMPLATE-SPEC.md` section by section, as the other specs in this build folder do: Goal, Scope,
   Non-goals, §3 Edges (no edge bullet onto a CLOSED unit, whose frozen spec cannot carry the reciprocal hands-off,
   and never a same-build id spelled `external`: name in §3 prose the CLOSED units that built the code this changes,
   found from that code's `git log` `Pass:` trailers, as units 106 to 108 do),
   Acceptance criteria each with its Red-when, §4 Evidence with probes you ran, §5 Risks, §7 the gates leg line
   (every leg whose guard names a path in Files touched, read through `python tools/check-spec-tokens.py --legs-for
   <path>`) and a `New arm:` line for each arm the left-shift gate adds, §8 forks, §9 revision log, §10 reuse audit.
   Name in your return whether the batch's write sets split; write one spec either way.
3. Files touched lists every path exactly. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix
   (shipped surface)`; keep every home under `memory/project/`. Cite code-file lines as `path#symbol` or
   blob-pinned at HEAD, never a bare `path:line`. The spec's ceiling is 49152 B (PINNED 2026-11-20 by the spec size
   check); keep it well under, since each pass adds rows to its generated records region.
4. Name every new function with a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
5. A choice the class fix leaves open is a fork: decide it by the build method's M3, mark it RESOLVED in §8 with
   the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-110` and
`python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>`, and fix every finding either names. Write no numeric fact
without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the new spec, and the spec carries rev-1 and one revision-log line naming this brief by its
file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but TOOL-dWitnessedBar-110's. No product code. No edit to the build README, which the main loop owns.

### Limitations

The spec audit of this build is stopped by the owner (prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-owner-review-stop.md),
so this spec closes unaudited; the loop ended at round 2, so no review round reads this unit; the close's bar observes it.

### Reuse

The seam is the code the finding names; `python tools/codebase-map/reuse_lookup.py "<behaviour>"` for anything new.
