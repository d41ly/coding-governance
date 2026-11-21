**Serves:** journal TOOL-dWitnessedBar-107

# Brief — dWitnessedBar: TOOL-dWitnessedBar-107, verify-peer publishes only a slot the current bar run witnessed

## The prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. The closing diff review's round 1 (`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md`) read CLEAN WITH
FIXES under `review.follow-up` `after-high`, so its loop is CONVERGING and every confirmed finding is promoted to a
unit while the rework budget remains (`memory/guides/UNATTENDED-VERBS.md`, "Review rounds, and the loop that ends
itself").

## The brief

### Goal

Write the NEW spec `memory/builds/dWitnessedBar/spec/2026-11-21-spec-TOOL-dWitnessedBar-107.md` for
TOOL-dWitnessedBar-107, a Tier-2 unit at `order 51` with status DEFERRED, rev-1, that closes H2 (finding 2) of that review
record by their mechanism, so a builder can build it as written over HEAD.

### Items

1. Read the review record's sections for H2 (finding 2) whole: the finding, its reachable path, the skeptic's
   class-level fix (the one the record carries, never the finder's instance fix) and its left-shift gate. The spec's
   design is that class fix, re-derived against the code at HEAD; settle every path, symbol and count it names.
   The code is `tools/run-gates/verdict_backends.py#run_verify_peer`, with `#read_local_verdict`, `#check_local_record` and `#write_peer_tag` beside it; the arm lives in the `run-gates gov canary` suite `tools/run-gates/run-gates.gov.test.sh`, whose `FLOOR_ASSERTIONS` this unit restates for its own arm with its `# RAISED` comment below the constant, the line above staying unit 90's owner line.
2. Follow `memory/TEMPLATE-SPEC.md` section by section, as the other specs in this build folder do: Goal, Scope,
   Non-goals, §3 Edges (a `consumes-from` edge to each CLOSED unit whose built code this changes, found from that
   code's `git log` `Pass:` trailers; the consumed spec is CLOSED and frozen, so name no hands-off edge in it),
   Acceptance criteria each with its Red-when, §4 Evidence with probes you ran, §5 Risks, §7 the gates leg line
   (every leg whose guard names a path in Files touched, read through `python tools/check-spec-tokens.py --legs-for
   <path>`) and a `New arm:` line for each arm the left-shift gate adds, §8 forks, §9 revision log, §10 reuse audit.
   The planted stale slot carries `reused_cache 1` for the candidate's tree, and the stubbed bar exits 1 without writing.
3. Files touched lists every path exactly. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix
   (shipped surface)`; keep every home under `memory/project/`. Cite code-file lines as `path#symbol` or
   blob-pinned at HEAD, never a bare `path:line`. The spec's ceiling is 49152 B (PINNED 2026-11-20 by the spec size
   check); keep it well under, since each pass adds rows to its generated records region.
4. Name every new function with a verb from `.lexicon.conf`'s VERBS table, nested helpers included.
5. A choice the class fix leaves open is a fork: decide it by the build method's M3, mark it RESOLVED in §8 with
   the delegated mark, and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-107` and
`python tools/check-spec-tokens.py --spec <path>`, and fix every finding either names. Write no numeric fact
without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the new spec, and the spec carries rev-1 and one revision-log line naming this brief by its
file stem.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but TOOL-dWitnessedBar-107's. No product code. No edit to the build README, which the main loop owns.

### Limitations

The spec audit of this build is stopped by the owner (prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-owner-review-stop.md),
so this spec closes unaudited; the closing review's round 2 reads the fold this unit builds.

### Reuse

The seam is the code the finding names; `python tools/codebase-map/reuse_lookup.py "<behaviour>"` for anything new.
