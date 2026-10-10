# TOOL-aSparedSpawn-9 — fixture templates and environment git identity across the named suites

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-1 · base 22efab65 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Most suites build a scratch repository per arm and then pay two to four `git config` spawns on it for
an identity and `core.autocrlf`, plus the sample-hook writes of a default `git init`. Exported once
per suite through the environment, the same settings cost no spawn at all, and a repository built
once can be copied per arm. Round one priced it at 2 to 4 git spawns per fixture across about 1,000
fixtures (census R9), worth 10 to 30 % of each small suite's spawns.

## 2. Scope (IN)

- **S1** — Each suite in §4's table exports, once in its prologue or at selftest start,
  `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and `GIT_COMMITTER_EMAIL`, and
  `GIT_CONFIG_COUNT` with `GIT_CONFIG_KEY_<n>`/`GIT_CONFIG_VALUE_<n>` for `core.autocrlf=false` and
  for any other key the suite sets on every fixture today (`commit.gpgsign=false` in
  `tools/memory-tree/migrate_backlog.py`). Its fixtures then write no per-repo config for those keys.
  Observed by AC1 and AC2.
- **S2** — Every fixture `git init` in those suites passes `--template=`, the spelling
  `tools/codebase-map/selftest.py:1477` already uses, so no sample hook is written. Observed by AC3.
- **S3** — `newrepo` in `tools/check-wiring.test.sh` builds its repository once per run and copies it
  with `cp -a` per call, so each arm still starts from a fresh, unshared tree. Observed by AC4.
- **S4** — Every suite keeps its arm inventory: the arm labels and the assertion count it prints are
  identical before and after. Observed by AC5.
- **S5** — A suite that runs `git` against the HOST repository in a way that hashes working-tree
  files keeps `core.autocrlf` per fixture rather than through the environment, because environment
  config reaches every git the arm runs, the host's included. Observed by AC6.
- **S6** — The before and after spawn count of each converted suite is recorded in the build folder.
  Observed by AC7.

## 3. Non-goals (OUT)

- `tools/check-hook-destinations.test.sh`. Its `scratch()` is rebuilt once per run by
  TOOL-aSparedSpawn-11's S4, and two units editing one fixture function in one parallel group is a
  merge waiting to happen. Its two `git config` calls ride along with that unit.
- Repo templates beyond `newrepo`: the evidence suite's `rec_repo`/`ru_repo` and the canary's
  `build_hv_repo` (round one's run-gates levers 14 and 18), and the drift-audit `make_repo` copy
  (memory-tree report, drift-audit lever 3). Follow-ups, each with its own inventory compare.
- Reading `HEAD` from the ref file instead of `git rev-parse HEAD` (memory-tree lever 10's second
  half). It changes what an arm reads, not only how a fixture is built.
- Suites outside the named sources: govkit selftest and the unattended driver suite carry the most
  config sites, and neither is in the levers this unit takes.

### Edges

none

## 4. Design

### The named suites

Estimates are the round-one reports' (`memory/builds/aMeteredSweep/build/`), on node `a`, from static
counts; none was measured.

| suite | source lever | estimated saving |
|---|---|---|
| `tools/run-gates/run-gates.test.sh` | run-gates 8 | inside ~75-225 s for the run-gates family |
| `tools/run-gates/run-gates.evidence.test.sh` | run-gates 8 | ~15 s |
| `tools/run-gates/run-gates.turnstile.test.sh` | run-gates 8 | ~15 s |
| `.githooks/pre-push.test.sh` | run-gates 8 | ~20 s |
| `tools/push-main.test.sh` | run-gates 8 | ~10 s |
| `.githooks/pre-push.runlog.test.sh` | run-gates 8 | ~5 s |
| `.githooks/pre-commit.test.sh` | run-gates 8 | ~5 s |
| `tools/memory-tree/check-memory-hygiene.test.sh` | memory-tree 10 | ~50 spawns, 15-35 s quiet |
| `tools/memory-tree/gen_build_index.py` selftest | memory-tree 10 | 144 spawns, ~4 s quiet, ~60 s pool |
| `tools/memory-tree/corpus_ids.py` selftest | memory-tree 10 | 50 spawns |
| `tools/memory-tree/gotchas.py` selftest | memory-tree 10 | 28 spawns |
| `tools/memory-tree/row_grammar.py` selftest | memory-tree 10 | 10-30 % of spawns; 20-70 s pool |
| `tools/memory-tree/migrate_backlog.py` selftest | memory-tree 10 | part of 20-30 s serial |
| `tools/memory-tree/check-arms.py` selftest | memory-tree 10 | 8 spawns; folded in, not worth it alone |
| `tools/drift-audit/selftest.py` | memory-tree 10 | 10-30 % of spawns; 20-70 s pool |
| `tools/check-wiring.test.sh` | govkit 16, other-legs 18 | ~60 s from the template alone |
| `tools/lexicon/selftest.py` | other-legs 18 | part of ~30-60 s serial across its legs |
| `tools/memory-tree/check-verdict-epoch.test.sh` | other-legs 18 | part of ~30-60 s serial |

The four `tools/memory-tree/` engines whose selftest lives in the module itself sit in the verdict-epoch
scan set (`tools/memory-tree/check-verdict-epoch.sh:180`), so a selftest-only edit to them owes the
memory-tree kit bump; F1 decides whether they are in.

### The mechanism

`GIT_CONFIG_COUNT` needs git 2.31 or later; node `a` runs 2.54. Command-scope config outranks the
global file, so a node whose `~/.gitconfig` sets `core.autocrlf=true` no longer leaks into a fixture,
which is the class `memory/gotchas/fixture-inherits-ambient-machine-state.md` records for a bare origin
that inherited nothing from its worktree. Two traps bind (census §3 R9):

- An arm asserting behaviour under a DIFFERENT `core.autocrlf` or identity sets it on its own command;
  a per-call `GIT_AUTHOR_DATE` such as `tools/memory-tree/row_grammar.py:2313` already does keeps working.
- Product code that reads `git config user.email` sees an environment identity only through `git var`.
  Each suite's arms touching identity are read before the conversion.

### Files touched (estimate)

- `tools/run-gates/run-gates.test.sh`, `tools/run-gates/run-gates.evidence.test.sh`,
  `tools/run-gates/run-gates.turnstile.test.sh`, `tools/push-main.test.sh`
- `.githooks/pre-push.test.sh`, `.githooks/pre-push.runlog.test.sh`, `.githooks/pre-commit.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/migrate_backlog.py`,
  `tools/memory-tree/check-arms.py`, `tools/memory-tree/check-verdict-epoch.test.sh`
- `tools/drift-audit/selftest.py`, `tools/check-wiring.test.sh`, `tools/lexicon/selftest.py`
- Per F1: `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/corpus_ids.py`,
  `tools/memory-tree/gotchas.py`, `tools/memory-tree/row_grammar.py`

### Alternatives rejected

- **A shared fixture library every suite sources.** `tools/lib/lib-selftest.sh` exists, but porting a
  suite onto it is a rebuild with its own inventory risk; three exported variables are not.
- **A global `git config --global` in a scratch `HOME`.** Same effect, one more file per suite, and
  it hides the identity from a reader of the prologue.

## 5. Production-readiness checklist

- security — No write path; fixtures stay in scratch directories under `TMPDIR`.
- perf / scale — Two to four git spawns fewer per fixture, plus the template's hook writes.
- error / empty / loading states — A failed `cp -a` of the template exits like a failed `git init`.
- observability — Each suite's printed assertion count is the inventory witness, unchanged.
- risks — Environment config reaching a host-tree `git` call; S5 is the guard.
- testing — The suites themselves, compared before and after; no new arm.
- migration — Kit versions bump once after the last move in each touched kit.
- user docs — N/A — no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a fresh repository is made with `git init --template=` under the exported
  `GIT_CONFIG_COUNT` triple and a scratch `HOME` whose `.gitconfig` sets `core.autocrlf=true`,
  `git config --get core.autocrlf` prints `false` and `git config --local --get core.autocrlf` exits 1.
  Red when: the global value wins, or the key lands in `.git/config`.
- **AC2** — When `git grep -nE 'config (user\.(email|name)|core\.autocrlf)'` runs over the converted
  suites after the pass, every hit is a site §4 keeps with its reason.
  Red when: an unlisted per-fixture identity or `core.autocrlf` write remains.
- **AC3** — When a converted fixture is inspected after its `git init`, its `.git/hooks` holds no
  `*.sample` file.
  Red when: a converted init still writes the sample hooks.
- **AC4** — When `newrepo` runs twice in one check-wiring run, both trees start at the same `HEAD`
  sha, and a commit an arm makes in the first is absent from the second.
  Red when: the second tree carries the first arm's commit or a shared `.git` directory.
  cost: one run of the check-wiring suite.
- **AC5** — When each converted suite runs at base 22efab65 and after the pass, its arm labels and the
  assertion count on its last line (for example `PASS (<n> assertions)`) are identical, recorded in
  an acceptance ledger in the build folder.
  Red when: any label or count differs.
  permission: kit suites are the owner's manual run of the merged tree (owner ruling, 2026-10-06).
- **AC6** — When each converted suite is read for `git -C "$ROOT"` and `cd "$ROOT"` calls running
  `status`, `diff` or `add`, none sits in a suite that exports `core.autocrlf` through the environment.
  Red when: such a call exists in a suite carrying the exported triple.
- **AC7** — When each converted suite runs once under a `PS4='+ ' bash -x` trace before and after, the
  count of traced `git` execs is lower after, and both counts are recorded in the build folder.
  Red when: a suite's count is not lower.
  figure: DERIVED at observation; the table's estimates are the round-one reports' and not a target.
  cost: one traced run per suite per side.

## 7. Gates

`codebase-map kit selftest` · `drift-audit selftest` · `lexicon selftest` · `run-gates canary` ·
`run-gates evidence` · `run-gates turnstile` · `pre-push self-test` · `pre-push run-log line` ·
`branch-guard self-test` · `push-main self-test` · `memory-hygiene self-test` · `build-index selftest` ·
`corpus-ids selftest` · `gotchas selftest` · `row-grammar selftest` · `backlog migration selftest` ·
`check-arms selftest` · `verdict-epoch self-test` · `check-wiring self-test` · `memory hygiene` ·
`kit version markers` · `kit epoch (shipped bytes move, the version moves)` ·
`verdict epoch (kit version dates the engine)` · `testsuite counts (every bar self-test prints one)` ·
`harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`

No arm is added or moved. The converted suites are their own observation, at the owner's manual run.

## 8. Open questions

- **F1 — Whether the four verdict-epoch scan-set engines are in this unit.** `gen_build_index.py`,
  `corpus_ids.py`, `gotchas.py` and `row_grammar.py` hold their selftests inside the module, so even
  a fixture-only edit moves scanned lines and owes the memory-tree kit bump in every carrier.
  - (a) Include them, and take the one memory-tree bump with the other memory-tree edits of this build.
  - (b) Leave them out; this unit touches only files outside the scan set.
  - Recommendation: (a). The bump is owed once per build whichever unit moves first, and these four
    hold most of the memory-tree lever's estimated spawns.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The probe `tools/codebase-map/reuse_lookup.py "fixture repo git init and identity config"` ranks
`build_fixture` (`tools/lib/lib-selftest.sh`, fan-in 5, SEAM), whose snapshot-and-`cp -a` model is
the template S3 follows; porting suites onto it is rejected in §4 as a rebuild. The `--template=`
spelling is reused from `tools/codebase-map/selftest.py:1477`.

Recall terms used: fixture git config user.email core.autocrlf GIT_CONFIG_COUNT template newrepo
scratch hermetic identity
