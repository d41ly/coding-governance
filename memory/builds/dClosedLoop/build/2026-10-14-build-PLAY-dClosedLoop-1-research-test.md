# Research — the Test stage: how gov decides a change is safe to land today, and the contract it should have

**Serves:** research PLAY-dClosedLoop-1

Returned by `gov-researcher` at its role's effort on handoff
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md`, session `1799cb98`, 2026-10-14:
77.4k subagent tokens, 31 tool uses, 227 s. Recorded verbatim below the rule. The main loop's
reading of it lives in the gap register, not here.

---

## 1. Inventory

- **run-gates.sh**: the merge bar. It iterates the manifest, runs legs through a bounded pool and reports per leg. Exit codes are 0 green, 1 red, 2 refused, 3 tree moved, 4 host. `tools/run-gates/run-gates.sh:1-7`
- **gate-legs.json**: the single leg source. It has 140 legs. By chunk: selftests 67, declarations 37, product 18, wiring 12, records 4, e2e 2. By subject: repo 76, kit 64. 76 legs carry a `guard`, 13 `doc_reads`, 4 `signature`. `tools/gate-legs.json`
- **Held tier**: a leg is held when `subject=kit` or `chunk=selftests`. That is 70 held and 70 run by default (56 of the default 70 are unguarded). `run-gates.sh:3115-3116`
- **`GATE_SELFTESTS=1|changed`**: runs the held tier, or only the held legs whose kit moved. `run-gates.sh:2936-2958`
- **Guards and `GATE_FULL`**: guards limit which legs run, never the verdict. `GATE_FULL=1` ignores them. `memory/guides/MERGE-BAR.md:17-27`
- **Profiles and wall**: `gate-profiles.txt` sets the pool width and a whole-run wall of 21,600 s. `tools/run-gates/gate-profiles.txt`
- **Ceilings**: each leg has a `ceiling`. `ceiling-evidence.txt` holds the measured maxima, which only ever rise, and `derive-ceilings.py` writes them. `tools/run-gates/ceiling-evidence.txt:1-27`
- **Turnstile**: a per-host admission queue (`slots`), plus `--hold` for bars that are not this runner. `run-gates.sh:1458-1520`
- **GATE_ATTRIBUTE**: re-runs each red leg at a base revision and labels it OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE. It is report-only. `run-gates.sh:19-21`, `lib-attribute.sh`
- **--regen / --regen-check**: the bar refuses stale generated outputs before it queues. `run-gates.sh:8-11, 218-220`
- **Timeout retry**: a timed-out leg is retried once, serially. `run-gates.sh:2441-2444`
- **Run record**: `<git-dir>/gate-run/`, `gate-logs/`, `gate-ledger.tsv` and `gate-last-failure.txt`. `MERGE-BAR.md:45-56`
- **gate-fingerprint.sh**: a tree digest. The at-a-rev form hashes `$rev^{tree}`. `tools/run-gates/gate-fingerprint.sh`
- **.githooks/pre-push**: binds the bar at the push. It decides whether to set `GATE_FULL` (lag bound 10), reuses a recorded full green, refuses a dirty tree, and writes refusal tokens. `.githooks/pre-push:1275, 1462`
- **.githooks/pre-commit**: fast staged-only legs plus the branch guard. Its legs are named by hand in the hook. `.githooks/pre-commit:179-225`
- **push-main.sh**: the lander. It pushes `HEAD:refs/heads/<default>` directly. `tools/push-main.sh:975`
- **post-merge.sh**: a full bar on a sha that has already landed. It publishes `refs/gov/bar-red` to the remote. `tools/run-gates/README.md:153, 565`
- **remote-ci.yml**: `history-audit` and `bar` run on push to main; `held-plan` and `held` run daily. No job is a required check. `.github/workflows/remote-ci.yml`, `MERGE-BAR.md:75`
- **run-selftests.sh**: the held suites on demand, with a cost verdict. It writes down the Definition of Done for kit work. `tools/run-gates/run-selftests.sh:1-25`
- **check-testsuite-counts.sh**: every manifest `*.test.sh` must print an executed count against a non-zero `SELFTEST_FLOOR`. 20 waivers are filed. `tools/check-testsuite-counts.sh:1-24`, `memory/project/testsuite-count-waivers.txt`
- **check-arms.py**: every `fail` branch in a gate must be armed by its sibling test, or pinned. It checks text only. `tools/memory-tree/check-arms.py:1-10`. Its `--check` runs as a leg (`gate-legs.json:561`).
- **gate-lint**: shell and PowerShell hygiene scans. The PowerShell half is on no leg. `tools/gate-lint/README.md:1-10`
- **pytest-parallel-guardrails**: an xdist recipe that keeps runs bounded and attributable. It is the only kit aimed at product tests. `tools/pytest-parallel-guardrails/README.md`
- **Charter rules**: `[verify] [gate] [class] [left-shift] [bar] [cost]` at `coding-governance-agents.template.md:22-27`.
- **Dossiers**: `memory/map/features/run-gates.md`, `run-gates-turnstile.md`, `testsuite-counts.md`, `gate-lint.md`

## 2. Flow

- **In from Build:** a committed change.
- **Commit:** pre-commit runs hand-picked staged legs (ENFORCED by the hook; `--no-verify` bypasses it).
- **Push:** pre-push checks for stale outputs, then decides between a scoped and a full run, then runs the bar on the pushed tip (ENFORCED, `pre-push:1462`). The held tier is never set at the push, by owner ruling F1 (`run-gates.sh:2957-2958`). So 70 kit self-tests are only STATED as owed, through the Definition of Done in `run-selftests.sh:12-20`.
- **After landing:** remote CI runs the bar on main and the held matrix daily, and post-merge publishes `refs/gov/bar-red`. All of this is detection after the fact, and none of it is a required check.
- **Out to Deploy:** the landed sha with a local green stamp in the git common dir. Other nodes cannot see that stamp.
- **Out to Maintain:** the ceiling evidence, the gate ledger and inherited-red backlog records.
- **Enforced:**
  - stale-output refusal
  - the wall and ceiling reds (`[cost]`)
  - count floors (as a leg)
  - armed branches (as a leg)
  - guard canary
  - fingerprint reuse
- **Stated only:**
  - `[gate]` seen-red
  - `[verify]` exercising THIS change
  - running the held tier for kit edits
  - every product-test practice

## 3. The implicit contract today

- **Entry:** a clean tree and fresh generated outputs (refused otherwise). The bar must run from the repository and take a turnstile slot.
- **Exit:**
  - The bar is green on the pushed tip at the push boundary.
  - For gov, the 70 held self-tests are owed only through the Definition of Done in prose.
  - For an adopter, exit is whatever legs its selected kits emit. Its manifest starts empty and "does not travel" (`run-gates/README.md:902-906`).
- **Artifacts** (all untracked and per node):
  - the run directory
  - per-leg logs
  - the ledger
  - the full-green stamp
  - the last-failure file
- **Tracked artifacts:** `ceiling-evidence.txt` and `selftest-budgets.txt`.
- **Who does the work:** the implementing agent runs the bar, and the lander runs it again at the push. The owner sets policy rulings (F1, F2, the self-test split of 2026-08-23). No Test-stage role exists, and grading the gates themselves falls to whatever gov-reviewer pass happens to run.
- **Review at this stage** (how a gate is reviewed):
  - **Armed branches:** `check-arms.py` checks that fail branches have arms, by reading text.
  - **Count floors:** `check-testsuite-counts.sh` checks that suites actually execute assertions.
  - **Attribution:** GATE_ATTRIBUTE labels whose red it is, report-only. The runner refuses to grade its own edits as anything other than OWN (`run-gates.sh:25-29`).
  - **Liveness checks:** CI checks that the history audit reached its last check (`remote-ci.yml` "liveness").
  - **Seen red:** "a gate never seen red" is a charter line with no recorder.

## 4. Gaps

- **HIGH:** kit self-tests are not on any pre-landing path. That is 70 of 140 legs, and on the evidence file they carry 23,494 s of the 28,066 s summed per-leg maxima. Evidence: `run-selftests.sh:12-16`, owner ruling F1 at `run-gates.sh:2957-2958`.
- **HIGH:** the binding verdict is a local hook on one node. `--no-verify` bypasses it (`MERGE-BAR.md:58`), and remote CI "detects after landing, and no job is a required check" (`MERGE-BAR.md:75`).
- **HIGH:** an adopter gets no product-test contract.
  - Absent (searched template, WIRE, every kit README and kit.toml): "test strategy", "unit/integration test", "test level", "test selection" and "affected test".
  - "flak" appears only in `memory-recall/README.md:243`.
  - The adopter's manifest starts empty (`run-gates/README.md:905`).
- **MED:** flaky-test handling covers timeouts only: one serial retry (`run-gates.sh:2441`). An intermittent assertion red has no retry, quarantine or flake record. GATE_ATTRIBUTE is report-only.
- **MED:** the green is not shared across nodes. The full-green stamp lives in the git common dir. Absent: any `refs/gov/` green ref (only `bar-red` exists, `README.md:565`).
- **MED:** `[gate]` "seen red" has no recorder or leg. The phrase appears only in harness prose (grep over `tools/`, `.githooks`).
- **MED:** the pre-commit leg list is named by hand, not derived from the manifest (`pre-commit:179-225`). The repository's own gotcha `hand-named-gate-list-green-while-the-bar-reds.md` names this class.
- **MED:** no ceiling evidence exists for 21 of 140 legs. All 119 rows come from node `a` and none from another node (`ceiling-evidence.txt`).
- **MED:** there is no recorded whole-bar wall time. Records claim "4 to 7 hours" (`memory/builds/aSparedSpawn/README.md:15`). The per-leg sum is 28,066 s serial, and the longest leg is 3,358.7 s.
- **LOW:** the README example `43/43 … (42 held …)` (`run-gates/README.md:98`) disagrees with the manifest's current 70/70 split.
- **LOW:** 8 held legs carry no guard. Under `changed` they select by suite file only.
- **LOW:** the gate-lint PowerShell scan is on no leg (`gate-lint/README.md:9`).

## 5. Candidates

**A. Change-selected held tier at the push boundary (the local verdict, extended).**
- **Mechanism:** pre-push sets `GATE_SELFTESTS=changed`. Product tests become manifest legs with a selection key.
- **Seam:** `run-gates.sh:2936-2958` and `.githooks/pre-push` predicate 8.
- **Losing test:** the held set it selects for real landings makes a push unaffordable, or the push stays bypassable.
- **Result (lost on cost and on bypass):**
  - I replayed the last 60 first-parent landings on main. The selection proxy was guard plus suite file, not govkit EPOCH_ROLES.
  - 59 of 60 landings select at least one held leg. The selected set's median is 8,024 s serial (max 24,471 s), and the median longest leg is 2,494 s.
  - So a median push waits about 42 minutes even at width 8.
  - It also stays a local hook that `--no-verify` skips, and it reverses owner ruling F1.

**B. An independent pre-merge verifier that is a required check (the remote owns the verdict).**
- **Mechanism:** the lander pushes the candidate to a staging ref. CI runs the bar plus the held matrix, and only a green moves the default branch. The local bar becomes early signal.
- **Seam:**
  - `remote-ci.yml`, whose `held-plan` matrix already derives from `--list`
  - `post-merge.sh` remote-ref publication
  - `push-main.sh:975`
- **Losing test:** a held leg exceeds a CI job's limit, or the mechanism cannot exist outside gov.
- **Result (passes for gov, fails portability as shipped):**
  - The longest leg (3,358.7 s) is far below the 360-minute job limit, so sharding fits.
  - The lander pushes main directly today, so it would need a staging step.
  - Portability fails: no `kit.toml` or WIRE section ships a workflow (grep for `.github/workflows` and `remote-ci`: absent), and `remote-ci.yml` hard-codes `PRIMARY_TREE: C:/projects/coding-governance`. A kit would have to ship the workflow for adopters.

**C. A receipt keyed by tree, published as a remote ref.**
- **Mechanism:** the bar's green, carrying the manifest sha, the self-test coverage and the leg set, is pushed as a ref under `refs/gov/` keyed by the tree hash. Any node accepts that receipt instead of re-running.
- **Seam:** `gate-fingerprint.sh` (rev form), pre-push full-green reuse, `refs/gov/bar-red`.
- **Losing test 1:** the fingerprint does not reproduce across nodes. Result: passes. It hashes `$rev^{tree}`, which is content-addressed, and CI pins `autocrlf` off.
- **Losing test 2:** the receipt is writable by the pusher it certifies. Result: **lost.**
  - Searching `pre-push` and `post-merge.sh` for `gpg`, `ssh-keygen -Y` or a signed stamp found none.
  - The pusher writes the ref, so the guard shares state with what it guards, which breaks `[class]`.

## 6. Pick

My recommendation is B: the verdict comes from a verifier the pushing agent does not control, and it binds before the default branch moves.

- **Why not A or C:** A lost on cost: a median of about 42 minutes per push even at width 8, while staying bypassable and reversing ruling F1. C lost because a receipt the pusher can write certifies nothing.
- **What closes the two gov gaps:** B closes the held-tier gap and the bypass gap, because CI's held matrix (already derived from `--list`) and the full bar run before main moves.
- **What it costs:** a staging step in the lander, and a run-gates-shipped workflow template so adopters get the same contract.
- **What it does not close:** the adopter product-test gap still needs a declared shape in the manifest (test level, selection key, ceiling, flake policy) that B's verifier would run. That is the contract's second clause, not a separate mechanism.
