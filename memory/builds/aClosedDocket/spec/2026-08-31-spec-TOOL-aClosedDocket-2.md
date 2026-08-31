# TOOL-aClosedDocket-2 — `reuse_lookup.py` logs, and `reuse-probed` counts either probe

**Status:** OPEN · rev-4 · 2026-08-31 · node a · Tier-2 · base 733552e1 · streams tooling · order 2 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aClosedDocket-1.md](../prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md) | research | TOOL-aClosedDocket-1 TOOL-aClosedDocket-3 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round1.md) | spec-audit | TOOL-aClosedDocket-1 TOOL-aClosedDocket-3 |
| [2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aClosedDocket-1-spec-audit-round2.md) | spec-audit | TOOL-aClosedDocket-1 TOOL-aClosedDocket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Give the map half of `BUILD-METHOD` M5 the same liveness evidence the recall half already has.
`tools/memory-recall/query.py` logs every query; `tools/codebase-map/reuse_lookup.py` logs nothing,
so `reuse-probed` observes one of the two probes the `reuse-first` directive names.

## 2. Scope (IN)

- **S1** — `reuse_lookup.py` appends one JSONL row per answered lookup to
  `<git-common-dir>/codebase-map/lookups.jsonl`: its OWN directory under its own kit's name, never
  the recall kit's file.
- **S2** — the row carries `type`, `at`, `query`, `worktree` and `n_shown`, spelled the way the
  recall log ACTUALLY spells them rather than the way rev-1 guessed. Measured: `query.py` writes
  `"type": "query"`, `n_shown` and `n_hits`; rev-1 pinned `n_candidates` and omitted `type`
  entirely, and `type` is the field the existing reader filters on FIRST
  (`grep '"type": "query"'` at `unattended.sh:3268`), so a row without it is invisible to a reader
  built in the recall log's image. The map row's discriminator is `"type": "lookup"`.
- **S3** — the write is NEVER FATAL and never gates: an `OSError` warns on stderr and the lookup
  still answers. `reuse_lookup.py`'s own `main` records that a RESULT never fails and only its
  refusal exits non-zero, and a log must not be the thing that breaks that.
- **S3a** — **the resolution adds NO subprocess, which removes the failure mode rather than guarding
  it.** Round 1's H4 was right that `reuse_lookup.py` makes zero git calls today and that adding one
  would be a new class of failure. It is not added: the common git dir is read the way
  `tools/memory-recall/recall-opened.js` reads it — `.git` as a directory IS the git dir; `.git` as a
  FILE holds `gitdir: <path>`, and that directory's `commondir`, when present, names the common one.
  Pure path math and two small file reads, matching `map_lib.repo_root()`'s own refusal to shell out.
  The resolution still sits INSIDE the `try`, because `log_event`'s `p = log_path(repo)` sits outside
  its own and that is a hole worth not copying; a failure to LOCATE the log warns and answers exactly
  as a failure to write it does.
- **S4** — a `MAP_CLI` declaration in `.unattended.conf`, optional and blank by default, in
  `kit.toml`'s `optional_keys` and the protocol's §8 key table. Same shape and same reason as
  `RECALL_CLI`: a kit path spelled into the driver arrives verbatim in an adopter at another prefix
  and resolves to nothing.
- **S5** — `dod_met`'s `reuse-probed` arm counts rows from EITHER log. `not adopted` now means
  neither CLI is declared-and-readable; a tree with one of them is measured on that one, and the
  message names which logs were read.
- **S6** — self-test arms for the new outcomes, and a `codebase-map` arm asserting the row is written
  and that a write failure does not change the exit code. **The map arm sets `CODEBASE_MAP_ROOT` to a
  scratch repo, and a `cd` is NOT sufficient.** Measured: `map_lib.repo_root()` resolves from the KIT
  directory, not the working directory (`map_lib.py:113-119`), so an arm that merely changes
  directory still writes into THIS tree's log. Round 2's H5 caught that rev-2's scratch-repo rule was
  insufficient for exactly this reason. A test that invokes `reuse_lookup.py` here writes a
  real row, carrying this worktree's own path, into the very log `reuse-probed` counts — so every bar
  run would manufacture the liveness evidence the DoD item exists to observe, and the item would
  become unfalsifiable. That is round 1's blocker B3, and it is the same class as a fixture that
  passes by finding nothing, one level up: a fixture that passes by CREATING what it looks for.
- **S6a** — the `codebase-map` arm lands in `tools/codebase-map/selftest.py`, the kit's own suite.
  NOT `test_codebase_map.py`, which rev-1 named: that file is byte-identical to
  `test_codebase_map.template.py` and runs as the `subject:repo` coverage leg, so an arm added there
  is graded as adopter-facing template content and its copy would diverge.
- **S7** — both kit versions move, their renders refresh, and the `.unattended.conf.example` gains
  `MAP_CLI` beside `RECALL_CLI`.

## 3. Non-goals (OUT)

- **N1** — a shared log file, a shared writer, or either kit importing the other. That coupling is
  exactly why `TOOL-aProvenReuse-4` was filed rather than built, and it has not become acceptable.
  Two kits, two logs, one reader that knows both only through declarations.
- **N2** — requiring BOTH probes. A build may legitimately satisfy M5 with recall alone when the map
  returns nothing; the item measures that a probe ran, never that every probe ran.
- **N3** — logging the RESULT set. The recall log's own header records that embedding every hit cost
  12 987 B per record; `n_candidates` is the count and nothing more.
- **N4** — a `reuse-lookup-opened` hook, the map analogue of `recall-opened.js`. It infers which hit
  was read, which is a different question from whether the probe ran, and nothing asks it yet.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `tools/codebase-map/reuse_lookup.py` | S1–S3 — the appender and its call site in `main` |
| `tools/codebase-map/kit.toml`, `README.md` | S7 — version, and what the log is for |
| `tools/unattended/unattended.sh` | S4 default, S5 the arm |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | S4 — the declaration |
| `tools/unattended/PROTOCOL.template.md` and its render | S4 key row, S5 the `reuse-probed` row |
| `tools/unattended/unattended.test.sh` | S6 — the driver arms |
| `tools/codebase-map/selftest.py` | S6, S6a — the map arm, in a scratch repo |

### Why the log location is derived and not declared

`query.py` puts its log under the git COMMON dir, which every worktree of a repo shares, and
`recall-opened.js` finds it by the same rule. S1 copies that rule rather than inventing one: a
per-worktree log would count a sibling worktree's probes as absent, and this is a fleet where five
worktrees of one repo run at once.

### What the two declarations buy that a probe does not

`RECALL_CLI` exists because a `tools/<kit>/` literal in shipped bytes resolves to nothing at another
install prefix — `tools/check-install-prefix.sh` reds on exactly that, and it caught the first cut of
`reuse-probed`. `MAP_CLI` is the same fact one kit over. Neither is a `requires` edge: `govkit`
resolves a `requires_if` against a condition key, and conditioning "needs the map kit" on "declares
the map kit" is a tautology.

### Alternatives rejected

- **`reuse_lookup.py` writing to the recall kit's log.** N1. It makes `codebase-map` depend on a
  `memory-recall` convention that neither kit's descriptor declares.
- **One shared telemetry module in `tools/lib/`.** Every copy-installed kit carries `tools/lib/`
  contents INLINE rather than depending on it, so a shared module becomes two copies with a parity
  gate — three mechanisms where two appenders is one.
- **Counting the map probe by its cache mtime.** A derived signal with no liveness assertion: an
  absent cache and an unused one are indistinguishable, which is the class the kit refuses by name.

### Rollout

Two commits, S1–S3 then S4–S6, because the driver arm cannot be exercised until something writes the
log it reads.

## 5. Production-readiness checklist

- **Security** — one append inside the git common dir, a directory both kits already write to. No
  new input from outside the repo.
- **Performance** — one append per lookup, on a tool a session runs a handful of times. The recall
  log measured 358 453 B over 174 rows; this one carries no result list, so its rows are smaller.
- **Error states** — S3: an `OSError` warns and the lookup still answers. A log that can fail a probe
  is worse than no log.
- **Observability** — S5's message names which logs were read, so a partial adoption is visible
  rather than inferred from a count.
- **Testing** — S6, both sides.
- **Migration/rollback** — an adopter gains an optional key that defaults blank. Existing runs with
  only `RECALL_CLI` behave exactly as they do today, which is N2 restated as a property.

## 6. Acceptance criteria

- **AC1** — running `python tools/codebase-map/reuse_lookup.py "<phrase>"` appends exactly one row to
  `<git-common-dir>/codebase-map/lookups.jsonl` carrying `type` set to `lookup`, plus `at`, `query`,
  `worktree` and `n_shown`. Observed by reading the file before and after. Rev-2 rewrote S2 to these
  names and left this criterion grading rev-1's `n_candidates` with no `type` — round 2's B4, and
  AC1 is the only criterion that observes the row shape at all.
- **AC2** — with that directory made unwritable, the same command still prints its candidates and
  exits `0`, warning on stderr. This is S3's observable, and without it "never fatal" is a claim.
- **AC3** — with only `MAP_CLI` declared and a map row present, `--close` reports `reuse-probed` MET
  and the message names the map log. Observed against a fixture.
- **AC4** — with both declared and rows in both, `--close` reports `reuse-probed` MET and the count
  is the SUM of the two logs. Observed against a fixture carrying a row in each.
- **AC5** — with neither declared, the `not adopted` skip fires and names both keys, so an adopter is
  told which declarations would make the item measurable.
- **AC6** — `bash tools/unattended/unattended.test.sh --shard 2/2` and
  `python tools/codebase-map/selftest.py` both pass with S6's arms present.
- **AC6a** — after the whole suite runs, `<git-common-dir>/codebase-map/lookups.jsonl` in THIS tree
  holds no row the suite wrote. Observed by comparing the SHA of the file before and after, not by
  row count: five worktrees of this repo share one common dir and a concurrent session's genuine row
  would change a count without this arm having written it. A hash equal before and after is the only
  form of this observation that attributes correctly.
- **AC7** — `python tools/codebase-map/reuse_lookup.py` run where `.git` cannot be read still prints
  candidates and exits `0`. This is S3a's observable, which round 2's H3 found had none.
- **AC7a** — `grep -cE "^\s*(import subprocess|from subprocess|import os\.popen)" tools/codebase-map/reuse_lookup.py`
  returns `0`. The predicate is the IMPORT, not the word: the first cut grepped for `subprocess`
  anywhere and its own docstring — which says the resolution spawns none — satisfied it. A gate
  answered by its own comment prose is the class this repo names, and it appeared inside the
  criterion written to prevent it.
- **AC7** — `bash tools/check-install-prefix.sh` exits `0` and its carried-prefix ratchet does not
  RISE, which is the leg the first `reuse-probed` cut turned red and the reason S4 exists.
- **AC8** — `bash tools/check-kit-versions.sh` exits `0` and `bash tools/unattended/check-unattended.sh`
  exits `0`, the latter proving check 22's key-table join accepts `MAP_CLI`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. Named because this unit reaches each: `install-prefix (shipped
surface)`, `unattended kit gate`, `unattended skill wiring`, `codebase-map coverage + freshness`.
`bash tools/unattended/run-unattended-gates.sh` and the codebase-map kit self-test for AC6, which
this unit owes because it IS kit work.
What no gate here checks: that the logged probe was run FOR the build being closed, or that its query
was relevant. Both are `reuse-probed`'s existing stated limits and this unit widens neither.

## 8. Open questions

- **Q1 — should `n_candidates` count the shortlist or the whole corpus scan?** **RESOLVED (agent,
  2026-08-31, delegated):** the shortlist, which is what the caller was SHOWN. The recall log's
  `n_shown` means the same thing and S2 exists to keep the two parseable by one reader; a corpus
  count is a property of the index, not of the lookup.
- **Q2 — does the `not adopted` message change break any existing arm?** **FACT-QUESTION · RESOLVED
  (agent, 2026-08-31, delegated):** the probe is `grep -c` over the current suite for the existing
  message text, and the observation that decides it is the hit count; a non-zero count means the arms
  must be updated with the message. The probe can return zero, which is the liveness half. Answered
  at build time, before the message is edited.

## 9. Revision log

- rev-4 · 2026-08-31 · build-time amendment, per M2's rule that the spec changes before the code
  diverges from it. S3a assumed the git-dir resolution would be a subprocess and specified a guard
  around it. Reading `map_lib.resolve_root` at source showed the kit already refuses to shell out and
  does pure path math, and `recall-opened.js` already reads the common dir the same way — so the
  resolution adds NO process at all and AC7a observes that absence. The failure mode H4 named is
  removed rather than guarded, which is the better answer and was not available until the code was
  read.
- rev-3 · 2026-08-31 · round-2 spec-audit fold. B4: AC1 still graded rev-1's field names after S2
  was rewritten, and it is the only criterion observing the row shape. H5: the scratch-repo rule was
  INSUFFICIENT — `map_lib.repo_root()` resolves from the kit directory, so only `CODEBASE_MAP_ROOT`
  redirects the log and a `cd` does not; AC6a also moved from a row count to a file hash, because
  five worktrees share one common dir and a count cannot attribute a change. H3 gave S3a the
  criterion it lacked, as AC7.
- rev-2 · 2026-08-31 · round-1 spec-audit fold. Blocker B3: rev-1's map arm would have run
  `reuse_lookup.py` against this tree, writing a real row into the log `reuse-probed` counts, so the
  suite would manufacture the item's own evidence and the DoD item would stop being falsifiable —
  S6 now requires a scratch repo and AC6a observes that the real log did not move. H2 moved the arm
  from `test_codebase_map.py`, which is template-mirrored and graded as adopter content, to the
  kit's own `selftest.py`. H3 replaced rev-1's guessed field names with the measured ones and added
  the `type` discriminator the existing reader filters on first. H4 added S3a: the file makes no git
  call today, so S1 adds the first one and the guard must cover resolution as well as write.
- rev-1 · 2026-08-31 · authored by the aClosedDocket run.

## 10. Reuse audit

The seam is `tools/memory-recall/query.py`'s `log_event` at `:755` — its shape, its never-fatal
`OSError` handling, its `<git-common-dir>` location rule and its field names are all COPIED rather
than invented, so one reader can parse both logs. What is deliberately NOT reused is the file itself:
sharing it would make `codebase-map` depend on a `memory-recall` convention, which is exactly why
`TOOL-aProvenReuse-4` was filed rather than built. The second seam is `RECALL_CLI`, the declaration
idiom that already ships, which `MAP_CLI` copies one kit over.

`python tools/codebase-map/reuse_lookup.py "recording a telemetry log line when a lookup tool runs so
a later check can observe it"` returned `run` in `settings-merge.py` and `check` in
`test_recall_floor.py`, both high-fan-in seams and neither a logger; it surfaced no logging seam
inside `codebase-map` at all, which is the finding this unit builds from rather than a probe failure.

Recall terms used: `non-convergent review loop blocker promotion spec subject mechanism unit
disposition wall-clock timing assertion flake elapsed bound contention` — the set composed for this
build, per M5's rule that the obligation is satisfied once for the SET.

Where a hit was STALE: none. `log_event`'s body and `reuse_lookup.py`'s `main` were read at source at
writing time, and `main`'s closing comment — that a RESULT never fails and only the refusal exits
non-zero — is what S3 is written to preserve.
