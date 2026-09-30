# TOOL-aRepatriatedFork-47 — every copy of the `{prefix}` resolution gives one answer

**Status:** SPECCED · rev-1 · 2026-09-30 · node a · Tier-1 · base 6830f257 · streams tooling · order 17 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-prompt-TOOL-aRepatriatedFork-47-build-brief.md](../prompts/2026-09-30-prompt-TOOL-aRepatriatedFork-47-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-29` made the `{prefix}` token the spelling of the tool root in the registry,
the descriptors and the leg manifest. Its readers each resolve the token in their own words, because
a copy-installed kit cannot import a shared helper. Nothing holds those copies to one answer, and
they already disagree on two inputs. This unit gives the rule one canonical block per language and
gates every copy against it, the way the resolver's inline-parity leg gates `resolve_python`.

## 2. Scope (IN)

- **S1** — One canonical Python block, `resolve_prefix_token(spelled, troot)`, in a new
  `tools/lib/resolve_prefix_token.py`. An empty or `.` tool root drops the token and its slash, and
  a bare token becomes `.`. Any other root replaces the token. The name is the one `govkit.py`
  already defines, so its callers keep their spelling. Observed by AC1, AC4.
  **Readers:** by name: `govkit.py`'s callers of `resolve_prefix_token`, which keep the name. by value:
  `load_registry` in `govkit.py`, the leg runner in `run-gates.sh` and `check-spec-tokens.py`, which
  receive the same repo-relative path the per-site rules returned.
- **S2** — One canonical shell block with the same contract, in `tools/lib/kit-rel.sh` beside
  `derive_self_rel`. Its marker stem is not a prefix of S1's, nor S1's of it, because the parity
  grep matches a stem as a prefix. Observed by AC1, AC4.
- **S3** — Every copy carries its language's block inline between markers and calls it. The Python
  copies are `tools/run-gates/run-gates.sh`, both programs in `tools/run-gates/run-selftests.sh`,
  `tools/check-spec-tokens.py`, `tools/govkit/govkit.py`, `tools/codebase-map/rank_harness.py`,
  `tools/govkit/selftest.py` and the `templates()` program in `WIRE-INTO-PROJECT.md`. The shell copies
  are `tools/check-dead-paths.sh` and `tools/check-testsuite-counts.sh`. Observed by AC1, AC7.
  **Readers:** by name: NO NAME READERS - each site's hand-written rule was local to it, and the inline
  block keeps the call shape. by value: `load_registry`, the `run-gates.sh` leg runner and
  `check-dead-paths.sh`, which now receive one answer.
- **S4** — The resolver leg's parity table gains one row per canonical, and its population grep also
  reads `WIRE-INTO-PROJECT.md`. Observed by AC1, AC2.
- **S5** — The parity arm compares EVERY block of a stem in a file, not only the first. Today's
  extractor stops at the first closing marker, so a second copy in the same file would go ungraded,
  and `run-selftests.sh` is the first file to carry two. Observed by AC3.
- **S6** — A behaviour arm runs both canonicals over one truth table and requires identical
  output. Observed by AC4.
- **S7** — A ban arm: outside a marked block, no tracked `*.sh` or `*.py` line and no line of
  `WIRE-INTO-PROJECT.md` resolves the token by hand. The forms banned are a Python
  `.replace("{prefix}` in either quote style, and a shell `#"{prefix}/"` strip or a `sed`
  substitution whose pattern begins with `{prefix}/`. The arm's header says what spelling it cannot
  see. Observed by AC5.
- **S8** — Every kit whose shipped bytes move takes its version bump in every carrier. Observed by
  AC6.

## 3. Non-goals (OUT)

- The drained-form recognizer in `tools/check-install-prefix.sh`. It asks whether a token is
  present and does not resolve one.
- Destination templates in descriptors, whose `{prefix}` is the TARGET's and which govkit resolves
  at install through its own seam.
- Fixture text that spells the token as data, such as `tools/govkit/matrix.py`'s scratch registry.

### Edges

- **hands-off** `TOOL-aRepatriatedFork-30` — its held leg installs the suites at `scripts/`,
  `vendor/gov/` and the repo root, and every reader of the token must resolve all three the same way
  before it runs.

## 4. Design

### Evidence

Measured at `6830f257` with `git grep` for the three banned forms: 16 lines in 10 files resolve the
token, at 11 sites, all listed in S3. The copies disagree on two inputs:

| Input | `run-gates.sh` | `govkit.py`, `check-spec-tokens.py`, `run-selftests.sh` | `rank_harness.py`, the govkit selftest, both shell sites | the runbook program |
|---|---|---|---|---|
| a `.` tool root | the root install | a `./` lead | a `./` lead | a `./` lead |
| a bare `{prefix}` with no slash | `.` or the root | `.` or the root | left unresolved | the root |

Neither disagreement changes a result today: every token in the tree is followed by `/`, and `./x`
opens the same file as `x`. That is why this is Tier-1, and why the canonical takes the widest
existing reading, the runner's, without moving any observed output.

### Contract

| `spelled` | `troot` | result |
|---|---|---|
| `{prefix}/a/b` | empty | `a/b` |
| `{prefix}/a/b` | `.` | `a/b` |
| `{prefix}` | empty | `.` |
| `{prefix}/a` | `tools` | `tools/a` |
| `{prefix}/a` | `vendor/gov` | `vendor/gov/a` |
| `x/y` | `tools` | `x/y` |

S6's truth table is this table.

### Inventory

This unit mints the S2 shell function and the two marker stems. Each is named by
`python tools/lexicon/lexicon.py --suggest` at build time. S1 reuses govkit's existing name.

### Files touched (estimate)

- `tools/lib/resolve_prefix_token.py` (new)
- `tools/lib/kit-rel.sh`
- `tools/lib/resolve-python.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-selftests.sh`
- `tools/check-spec-tokens.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/codebase-map/rank_harness.py`
- `tools/check-dead-paths.sh`
- `tools/check-testsuite-counts.sh`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- A behaviour-only gate that runs every copy on the truth table. The copies are expressions inside
  larger programs, so each would need a harness of its own, and none would catch a drift the table
  does not exercise.
- One canonical for both languages. The parity arm compares bytes, and a shell copy cannot carry
  Python's bytes unless it runs Python for a string replace.

## 5. Production-readiness checklist

- security — none; a string substitution with no filesystem access.
- perf / scale — one function call where an expression stood.
- error / empty / loading states — the empty and `.` roots are rows of the contract table.
- observability — the parity arm names the drifted file and the stem.
- risks — the population grep reading a Markdown file for the first time. It reads one named file,
  and no other `.md` in the tree carries a column-0 marker today.
- testing — AC1 to AC7.
- migration — none. The contract changes no observed output on today's tree.
- user docs — the runbook's embedded program gains the inline block.

## 6. Acceptance criteria

- **AC1** — When `git grep -c '^# >>> '` for each of the two stems runs on the built tree, it
  lists exactly the S3 files, and the budget checker's file shows 2. Each extracted block is
  byte-identical to its canonical, in `resolve_prefix_token.py` or in `tools/lib/kit-rel.sh`.
  Red when: a copy is missing, or one differs.
- **AC2** — Red-first control: in a scratch clone, one byte of the runner's copy is changed. The
  parity section of the `python resolver (behaviour + inline parity + idiom ban)` leg, run as a
  slice, names the runner's file and the stem. Restored, it is green.
  Red when: the slice stays green with the byte changed.
- **AC3** — Red-first control: in the same clone, the SECOND block in the budget checker's file is
  changed and the first left intact. The slice names that file, and the `blk` extractor as it stands
  at `6830f257` does not.
  Red when: only the first block of a file is graded.
- **AC4** — When `python -c` imports `resolve_prefix_token` from the canonical and evaluates the six
  rows of §4's contract, and `bash -c` sources `tools/lib/kit-rel.sh` and runs the shell function on
  the same rows, both print the table's results.
  Red when: either canonical disagrees with the table, or with the other.
- **AC5** — Red-first control: a line `x = s.replace("{prefix}/", "")` is planted outside any block
  in a scratch copy of `tools/check-spec-tokens.py`, and the ban slice names it. Removed, it is
  silent.
  Red when: the ban misses the plant, or reds on a copy inside a block.
- **AC6** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 6830f257` names no kit this unit moved without its bump.
  Red when: a moved kit's carrier was missed.
- **AC7** — On the built tree, `python tools/check-spec-tokens.py`, `bash
  tools/check-testsuite-counts.sh`, `bash tools/check-dead-paths.sh` and `python
  tools/govkit/check_runbook_parity.py` each exit 0.
  Red when: a reader that now calls the block resolves a guard, a suite path or a waiver path
  differently than it did.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `testsuite counts (every bar self-test prints one)` · `testsuite counts self-test` · `dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `govkit runbook parity` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `run-gates canary` · `run-gates gov canary` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)`

New arm: the resolver leg's parity section · a drifted copy, and a drifted SECOND copy in one file ·
its floor rises by the new arm count

New arm: the resolver leg's behaviour section · a canonical that disagrees with the contract table ·
its floor rises by the new arm count

New arm: the resolver leg's ban section · a hand-written resolution outside a block · its floor
rises by the new arm count

## 8. Open questions

- **F1 — which copies does the gate hold?** Option (a): the seven Python sites
  `TOOL-aRepatriatedFork-29` named. The two shell sites and the govkit selftest's copy stay free to
  drift. Option (b): every site that resolves the token, with a shell canonical beside the Python one
  and a behaviour arm that makes the two agree, plus a ban so a new unmarked copy cannot appear.
  Option (c): (b) without the ban. Recommendation: (b). A parity gate over marked copies only is
  how these copies came to exist unseen.
  RESOLVED (agent, 2026-09-30, delegated): (b), the most feature-rich option. It adds no dependency
  and no install location: `tools/lib/` is an existing gov-internal directory with a standing
  registry exemption.
- **F2 — what does a `.` tool root mean?** Option (a): the root install, as the runner reads it.
  Option (b): a literal `./` lead, as three other copies produce. Recommendation: (a). It is the
  only reading under which `troot` and `troot + "/"` cannot disagree, and neither changes a result
  on today's tree.
  RESOLVED (agent, 2026-09-30, delegated): (a).

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, adopted under the unattended protocol §11 from the run's
  rescope entry of 2026-09-29.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "hold every inline copy of a shared block byte-identical
to its canonical"` ranked `canonical_ctx`, `find_block` and `lf_pin_block` in govkit, none of which
gates inline copies, and it cannot see shell. The seam is `tools/lib/resolve-python.test.sh`'s
`PARITY_ROWS` table, found by recall and verified against source. It already gates six stems with a
non-empty-population arm per row, and this unit adds two rows and fixes its extractor.

Recall terms used: `inline copy canonical block byte-identical parity gated resolve-python lib
gov-internal marker stem prefix token`, with the question "how are inline copies of a shared function
kept identical across copy-installed kits". The hits were `TOOL-aDrainedSluice-6`, the resolver's
origin, and the `TOOL-dPromptedSeam-2` spec audit that pointed at the same `PARITY_ROWS` engine.
