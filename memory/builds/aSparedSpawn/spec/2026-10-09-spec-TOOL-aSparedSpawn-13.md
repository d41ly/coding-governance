# TOOL-aSparedSpawn-13 — content-addressed reuse: declared read classes, a shared cache, a soundness sample

**Status:** CLOSED · rev-5 · 2026-10-12 · node a · Tier-2 · base 22efab65 · streams tooling · order 3 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aSparedSpawn-13-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-13-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Make `GATE_REUSE` worth turning on outside one worktree's second bar, without letting it lie. Today
the key carries `BASE` for every leg, so it misses after every landing; the store is one row per leg
in one git dir, so a fresh worktree starts cold; and the only statement about what a leg reads beyond
the tree is the boolean `impure`. aMeteredSweep's round-two research estimated 25014 leg-s reusable
against a green parent with the self-test tier on (`2026-10-09-build-TOOL-aMeteredSweep-1-research2-reuse.md`
§5 U1; PINNED, an estimate from leg-second sums over one contended profile at fa68a767, ±2x, not an
A/B). This unit takes that only behind a sample that would catch a wrong hit, and by owner ruling F1
(b) it extends reuse to the push boundary for the legs that read the remote or history, at the exact
pushed sha and the observed tip only.

## 2. Scope (IN)

- **S1** — A manifest row declares what it reads beyond its inputs as `reads`, an object mapping a
  class to a one-line reason. The closed classes are `history`, `base`, `clock` and `remote`; the
  `impure` key is replaced by `reads` with `remote`, carrying its reason over verbatim. The runner
  keeps honouring a legacy `impure` on an adopter's row as "never reuse", so no adopter verdict
  changes meaning. Observed by AC1, AC2, AC3, AC10.
  - **Readers:** by name: `tools/gate-legs.json` carries the three rows; `tools/run-gates/run-gates.sh`
    parses the field and skips reuse on it; `tools/run-gates/run-gates.test.sh` lists it in its
    manifest key set; `tools/run-gates/run-gates.evidence.test.sh` declares it on a fixture row;
    `tools/run-gates/README.md` documents it; `memory/map/features/run-gates.md` describes its
    population in prose, and states one such leg where the manifest carries four;
    `tools/govkit/govkit.py` compares a kit descriptor's row against the manifest's and emits the
    row into an adopter; `tools/unattended/kit.toml` and `tools/memory-tree/kit.toml` carry the
    four descriptors, which move from `impure` to `reads` with the manifest rows.
    by value: `tools/run-gates/run-gates.sh` reads the field's PRESENCE to decide reuse, and nothing
    reads the reason text; `tools/govkit/govkit.py` compares a descriptor's `reads` with the
    manifest's where the descriptor declares one, as it compares `ceiling`, and writes an adopter
    row's legacy `impure` from the descriptor's reasons, so an adopter's runner keeps never reusing
    those legs whatever runner version it holds.
- **S2** — The key. Per leg, one hash over what `TOOL-aSparedSpawn-1` already folds in (its content
  key for dirty guarded files, its toolchain, environment and host digest, and `REUSE_SCHEMA`), plus
  the manifest row's own bytes and only the read classes the row declares: `BASE` and
  `GATE_PUSH_BASE` for `base`, the `HEAD` sha for `history`, the UTC day for `clock`, and the `HEAD`
  sha plus the observed tip of the default branch and the digest of the whole `ls-remote --heads`
  advertisement for `remote`, because `unattended kit gate` grades against every advertised head and
  not only the default's. `BASE` enters no other leg's key, so the environment digest leaves out
  `GATE_BASE`, `GATE_PUSH_BASE`, `GATE_RUN_ID` and every `GATE_REUSE*` knob, and `REUSE_SCHEMA`
  moves to 3. A `remote` leg with no observed tip writes no entry and reuses nothing. A class
  outside the four, or a `reads` that is no object, reads as a legacy `impure`. Observed by AC1, AC2,
  AC3 and AC12.
- **S3** — Declarations. Every leg the research's §1.4 found reading history, a base or the clock
  carries its class, each re-read against its script at build time. The research's list is a floor
  and not the population; a missed reader is what S6 exists to catch. Observed by AC2. Re-read at
  build: `history` for the dead-path carriers, the spec tokens and the leg ceilings; `history` and
  `base` for the drift-audit records, which compare against a base ref, the lexicon naming
  predicates, the verdict epoch, the kit epoch, the codebase-map coverage and the routed commits,
  which grades the graph from `GATE_PUSH_BASE`; `clock`, `history` and `base` for memory hygiene,
  whose later checks diff since the mainline merge-base; `history` for the kickoff-manifest ratchet, whose `health.log` window the research flagged is read
  by the `--card` writer and not by the leg's argv; `remote` for the other three rows that carried
  `impure`.
- **S4** — The cache, in the git common dir and never in a pushable ref: one file per key under a
  two-character fan-out, holding `ok`, seconds, run id, `HEAD` and end time, written tmp-then-rename.
  Only a leg that EXECUTED `ok` on a tree whose `TREE_CLEAN` reads `yes` writes an entry; a reused
  verdict writes none, so a wrong entry cannot carry itself forward. `gate-ledger.tsv` stays as the
  dispatch-duration hint and is read for reuse no more. Observed by AC4, AC5.
- **S5** — Pruning at run end: an entry older than 30 days is erased. Bumping `REUSE_SCHEMA` makes
  every entry unreachable at once. Observed by AC9.
- **S6** — The soundness sample. On every run that reuses, each reusable leg is drawn for execution
  at the sample rate (F2), seeded from the run id so a run's draw can be replayed. A drawn leg that
  executes `ok` agrees. One that executes red against a cached `ok` is re-run once: red again prints
  `cache disagreement · <leg> · <key>`, erases the entry and quarantines the leg; red then green
  prints `nondeterministic · <leg>` and quarantines it too. Either reds the run. A quarantined leg
  is never reused until its manifest row's bytes change. Observed by AC6.
- **S7** — The age bound. A leg reused on 10 consecutive reuse-enabled runs executes on the next
  one, whatever the sample drew, so a wrong entry survives at most that long. Observed by AC7.
- **S8** — Authority, kept and enforced in the runner rather than only by the hook's scrub: under
  `GATE_FULL` nothing is reused even with `GATE_REUSE` set, and a run with any reused leg stamps
  neither `gate-full-green` nor the inherited-green record. Every green stamp gains a `reused` field
  carrying the run's reused count, and `check_green_record` in `.githooks/pre-push` forces the full
  bar on a record whose field is present and not `0`, so a reused verdict can never satisfy the
  full-green predicate even through a record written some other way. Observed by AC8 and AC14.
- **S9** — The observed tip. The runner probes the default branch's advertised tip once before
  dispatch with a bounded `git ls-remote`, only when a `remote` leg is to execute on a clean tree, and
  again after the last such leg ends; an entry is written only when the two agree. At pre-push the
  hook probes the tip FIRST, before its decision, and offers reuse only when the probe answers and
  agrees with the remote sha git fed it on stdin. Observed by AC12.
- **S10** — Push-time reuse (owner ruling F1 (b)). On a SCOPED decision only, the hook exports one
  hook-owned knob, `GATE_REUSE_PUSH`, holding the pushed sha and the observed tip, after its scrub has
  cleared any inherited value. Under it the runner reuses only a leg declaring `remote` or `history`,
  only when `HEAD` equals the pushed sha, and only from an entry whose key, built with that tip,
  equals this run's. Every other leg executes. The S6 sample and the S7 age bound apply unchanged.
  The run is stamped `scoped`, in the hook's decision line and run-log line and in the run's own
  record, never `full`. Observed by AC12, AC13 and AC15.
- **S11** — The changed rule, rewritten in every place it is stated, in this unit: "an authoritative
  run never reuses" becomes "an authoritative run reuses only a `remote` or `history` leg, at the
  exact pushed sha and observed tip, and is then scoped". Observed by AC15.
  **Readers:** by name: `tools/run-gates/README.md` states it in its reuse section (`:137-139`);
  `tools/run-gates/run-gates.sh` in the comment above the reuse block (`:2280-2283`);
  `.githooks/pre-push` in the comment above `BAR_SCRUBBED_KNOBS` (`:1408-1420`);
  `tools/run-gates/run-gates.evidence.test.sh` in the opt-in arm's comment (`:905-907`). Each is
  rewritten in this unit. by value: `.githooks/pre-push` acts on it by scrubbing `GATE_REUSE`
  (`:1421`), which stays, and clears `GATE_REUSE_PUSH` beside `GATE_DOCS_BASE`, for every bar a STUB
  included, so only the hook sets it: the scrubbed list is kept for a STUB, and this knob, like the
  docs knob, is the hook's alone;
  the opt-in arm of `tools/run-gates/run-gates.evidence.test.sh` and the H49 arm of
  `.githooks/pre-push.test.sh` (`:868-875`) assert it, and both keep passing, since a FULL run and
  an environment-set `GATE_REUSE` still reuse nothing.

## 3. Non-goals (OUT)

- Reuse at the push boundary of any leg declaring neither `remote` nor `history`, and any reuse under
  a FULL decision. The environment's `GATE_REUSE` stays scrubbed at the hook exactly as it is.
- Trace-calibrated declarations (the research's U5, an audit hook plus `strace`), and the sandbox
  probe by subtraction. Named follow-ups; S6 and S7 carry soundness until then.
- A floor under which a cheap leg never reuses. The research suggested about 30 s; it is a cost
  tune, not a soundness rule, and can be added once hit rates are measured.
- Scrubbing a leg's environment to the hashed allowlist. `TOOL-aSparedSpawn-1` hashes the allowlist;
  withholding the rest is a larger change.
- Selection of the held tier, which is `TOOL-aSparedSpawn-12`.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-1` — the guarded key built from the CONTENT of dirty and
  untracked guarded files, the toolchain, environment and host digest, and `REUSE_SCHEMA`; without
  them a shared cache spreads today's status-line key to every worktree on the node.

## 4. Design

`input_key` in `tools/run-gates/run-gates.sh` today hashes the argv, `BASE` and the guard's index
blobs plus its porcelain lines, and the reuse block reads one ledger row per leg name from the
per-git-dir `gate-ledger.tsv`. This unit changes three things around it and keeps the opt-in shape:

1. **Parse.** The manifest reader that carries `impure` as a presence flag carries `reads` as the
   sorted, comma-joined class list instead, with a legacy `impure` read as `remote`.
2. **Key.** `input_key` takes the classes the row declares, so `BASE`, `HEAD` and the day enter only
   where declared, and the row's bytes enter always. The digest and schema stay
   `TOOL-aSparedSpawn-1`'s, computed once before dispatch.
3. **Store.** Lookup is a `read` of `<git-common-dir>/gate-cache/<k[0:2]>/<key>`, which costs no
   process. The write happens where the ledger row is written today, under the S4 preconditions.

The sample and the age counter live beside the cache: a per-leg counter file of consecutive reuses,
and a quarantine file per leg holding the row hash that quarantined it, `age.<name key>` and
`quarantine.<name key>` in `gate-cache`, the name key being `TOOL-aSparedSpawn-12`'s. A drawn leg is
dispatched as an ordinary leg and its line says it was sampled. The draw is a polynomial hash of the
run id and the leg name in shell arithmetic, so it spawns nothing and replays from the run id. A
sampled leg whose first attempt reds runs once more after the serial retry pass; the first attempt's
`GATE FAIL` already reds the run, and the second attempt picks the line, `cache disagreement` or
`nondeterministic`. Every cache write and the 30-day prune, by file mtime, run in ONE python process
at run end, so a bar pays one spawn for them however many legs it records.

The tip probe is `ls-remote --heads` under `timeout -k`, redirected to a file and read back, the
idiom of `check-unattended.sh`, against the remote the runner's ladder resolves; the hook probes the
URL git hands it. Both hash the advertisement with `git hash-object --stdin`, so the two sides agree
on the digest by construction. The hook probes only on a scoped decision: a FULL one exports
`GATE_FULL`, under which nothing is reused, so a probe there would buy nothing.

### Push-time reuse (S9 to S11)

The hook already decides FULL or scoped before the bar (`.githooks/pre-push:1455-1469`); a FULL
decision exports `GATE_FULL`, under which S8 reuses nothing, so reuse can only ever ride a scoped
decision. The order at the hook is: scrub the knobs (`:1421`), probe the tip with a bounded
`git ls-remote` against the remote the ladder resolves, decide, and only on the scoped branch with a
probe that answered and matched stdin's remote sha, export `GATE_REUSE_PUSH`. A probe that fails,
times out or disagrees exports nothing, and the decision line says why reuse was not offered.

The runner reads the knob instead of `GATE_REUSE`. Three checks bind every reuse under it: the leg
declares `remote` or `history`; `HEAD` is the pushed sha; the entry key, which for `remote` carries
`HEAD` and the tip, equals the one built from the knob's tip. A moved tip, another sha or a changed
input each moves the key, so none can match. A sampled leg executes as it does off the boundary.

What it costs: one `ls-remote` per gated push, and one or two per bar that executes a `remote` leg.
What it buys: the remote trio is 5780 of 7640 default-bar leg-seconds (research, PINNED at
fa68a767), and a push right after a green bar at the same sha and tip reuses the trio.

### Data model

- Cache entry: `ok<TAB>secs<TAB>run_id<TAB>head<TAB>ended`, one per key, about 100 bytes; `ended`
  is epoch seconds.
- The knob: `GATE_REUSE_PUSH=<pushed sha> <tip> <advertisement digest>`.
- Age counter: the count of consecutive reuses, reset to 0 by any execution.
- Quarantine: the manifest row hash at the time of the disagreement.

### Inventory

- The manifest key `reads` and its four class values; the directory
  `gate-cache` under the git common dir; the knob `GATE_REUSE_SAMPLE` for the rate, and a pinned-day
  seam for the `clock` arm, pinned the way the run id already is (TOOL-aGraftedHelix-7):
  `GATE_REUSE_DAY`, defaulting to the UTC days since the epoch. New function names come from
  `lexicon.py --suggest` at build: `read_remote_heads`, the runner's probe.
- The header keys `reuse` (`off`, `env` or `push`) and `reuse_sample`.
- The hook-owned knob `GATE_REUSE_PUSH`; the stamp field `reused`; predicate 9 of
  `check_green_record`.

### Migration

- gov's three `impure` rows move to `reads` in one commit. An adopter's `impure` keeps its meaning.
  The run-gates kit owes a version bump in every carrier. The existing per-git-dir ledger keeps its
  rows; nothing reads them for reuse after this unit, so no entry is trusted across the change.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/gate-legs.json`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.test.sh`
- `memory/map/features/run-gates.md`
- `.githooks/pre-push` — the tip probe, the knob and its scrub, predicate 9, the rewritten comment
- `.githooks/pre-push.test.sh` — the push-time reuse arms
- `tools/govkit/govkit.py` — the descriptor parity on `reads`, and the legacy `impure` an adopter row gets
- `tools/unattended/kit.toml`, `tools/memory-tree/kit.toml` — the four descriptors move to `reads`

### Alternatives rejected

- **Keep the boolean and widen it.** A flag says "do not reuse" and nothing about why, so the eight
  legs reading history, a base or the clock would all be shut out, or all trusted on file bytes.
- **A cache in `refs/gate-cache/*` on origin, or a CI artifact.** A pushable cache is a poisoning
  channel: anyone with push access writes a green another node trusts. Host classes also differ
  across nodes, so cross-node hits would be rare as well as risky.
- **No sample, the age bound alone.** Detection is then certain within 10 runs but never sooner; at a
  rate of 0.25 the expected latency is about 4 runs (research §2 table).
- **Reuse below the push boundary only by trusting the hook's scrub.** The scrub lives in a different
  kit and a hand-set `GATE_FULL` with `GATE_REUSE` reuses today; S8 puts the rule in the runner.
- **Honouring the environment's `GATE_REUSE` at the hook** instead of a hook-owned knob. H49 exists
  because an exported knob decided what a vetted runner checked; the hook must be the only setter.
- **Keying `remote` legs on the stdin remote sha alone.** That sha is what this clone last fetched,
  not what the remote advertises now, which is the question the ruling pins to `ls-remote`.
- **Stamping a reusing push run `full` when every reused leg is `remote` or `history`.** The ruling
  forbids it, and the full-green record is what the next push trusts without re-running anything.

## 5. Production-readiness checklist

- security: the cache sits in the git common dir, never pushed; writers are this runner on a clean tree only. A run with full shell access can still forge an entry, and at the push boundary a forged `remote` or `history` entry can now spare those legs; the sample (S6) still draws there, the stamp stays `scoped`, and no reused verdict can earn a full green (S8).
- perf / scale: a lookup is a file read and spawns nothing; the per-run digest is `TOOL-aSparedSpawn-1`'s; the sample costs about its rate times the saving; the tip probe is one bounded `ls-remote` per push and one or two per bar running a `remote` leg.
- error / empty / loading states: a missing, unreadable or malformed entry means execute; a missing cache directory is created; every failure mode does more work, never less.
- observability: every reused leg prints its line, a sampled leg says so, and disagreement, nondeterminism and quarantine each print a named line; the header records the sample rate and the schema.
- risks: an under-declared read makes a wrong hit; S6 and S7 bound how long it lives, and a disagreement reds the run rather than passing it.
- testing: evidence-suite arms for each class, the shared cache, the writers, the sample, the age bound, pruning and the authority rule; the canary's manifest key set accepts `reads`.
- migration: the three gov rows move in one commit, the legacy key keeps its meaning, the kit bumps once.
- user docs: `tools/run-gates/README.md`'s reuse section is rewritten for classes, the cache, the sample and quarantine.

## 6. Acceptance criteria

- **AC1** — When two reuse-enabled runs differ only in `GATE_BASE`, a leg declaring no class is
  reused and a leg declaring `base` executes. Red when: the undeclared leg executes, or the `base`
  leg is reused.
- **AC2** — When a commit lands that touches no guarded path, a leg declaring `history` executes and an
  undeclared guarded leg is reused; at the same `HEAD` the `history` leg is reused. Red when: the
  `history` leg is reused across the commit.
- **AC3** — When the runner's pinned day differs between two otherwise identical runs, a leg declaring
  `clock` executes. Red when: it is reused. fixture: the day seam named in §4 Inventory.
- **AC4** — When a green run in one worktree is followed by a reuse-enabled run in a fresh worktree of
  the same clone at identical inputs, the second run prints `GATE reuse` for the first's legs.
  Red when: it executes them, which is today's per-git-dir behaviour.
- **AC5** — When a leg executes red, when a run starts on a tree whose `TREE_CLEAN` is `no`, and when
  a leg is reused, no cache entry is written by that leg. Red when: any of the three writes one.
- **AC6** — When a planted `ok` entry meets a leg that now reds, with `GATE_REUSE_SAMPLE` drawing
  every leg, the run reds with `cache disagreement`, the entry is gone, and the next run executes that
  leg although its key matches. Red when: the run is green, the entry survives, or the leg is reused.
- **AC7** — When a leg has been reused on 10 consecutive `GATE_REUSE` runs and the sample draws
  nothing, the next run executes it. Red when: it is reused an eleventh time.
- **AC8** — When `GATE_FULL` and `GATE_REUSE` are both set, every leg executes; when a run reuses
  any leg, no `gate-full-green` is written. Red when: either reuses or stamps.
- **AC9** — When a `GATE_REUSE` run ends with one cache entry dated 31 days back and one 29 days back,
  the first is gone and the second remains. Red when: the old entry survives, or the young one is erased.
- **AC10** — When a manifest row carries a legacy `impure` and no `reads`, the leg is never reused, and
  `input_key` treats it as `remote`. Red when: it is reused on a byte-identical tree.
- **AC11** — When a second bar runs in a fresh worktree of a frozen clone after a recorded green
  parent, with reuse on and the self-test tier on, the run's verdict reports its reused count and the
  reused legs' recorded seconds. Red when: the count is zero. figure: DERIVED at observation; the
  research's 25014 leg-s is the PINNED expectation (estimate, ±2x). cost: two whole bars with the
  self-test tier, hours on node `a`; run on a frozen clone, not beside a pass.
- **AC12** — When a pre-push fixture finds a cache entry for a `remote` leg at the pushed sha, and in
  three variants the advertised tip moved, the pushed sha is not the entry's `HEAD`, or a guarded
  input changed, the leg executes in each; with the `ls-remote` probe failing it executes and the
  decision line names the probe. Red when: any variant reuses, or a leg declaring neither class
  reuses at the hook.
- **AC13** — When a pre-push fixture reuses a `remote` leg at the exact sha and tip, the decision line
  and the run-log line read `scoped`, and the run record's reused count is not 0. Red when: either
  reads `full`, or the reused leg is reported as executed.
- **AC14** — When a pre-push fixture run reuses any leg, no `gate-full-green`,
  `gate-full-green.shared` or inherited-green record is written; and a planted `gate-full-green`,
  otherwise valid, whose `reused` field reads 1 makes `check_green_record` force the full bar.
  Red when: a record is written, or the planted record is accepted.
- **AC15** — When `GATE_REUSE_PUSH` is exported from the environment into a push, the hook clears it
  and the bar reuses nothing unless the hook set it itself; the H49 arm still sees an environment
  `GATE_REUSE` ignored; and `git grep -n 'never sets it'` over `tools/run-gates/README.md` prints
  nothing. Red when: the inherited knob reaches the runner, or a rewritten rule statement still says
  an authoritative run never reuses.

## 7. Gates

`branch-guard self-test` · `check-wiring self-test` · `dead-path carriers self-test` ·
`foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` ·
`kit-placeholders self-test` · `lexicon naming predicates` · `pre-push bar self-test` ·
`pre-push run-log line` · `pre-push self-test` · `profile-bar selftest` · `push-main self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` ·
`run-gates adopter e2e` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` ·
`run-gates run-log line` · `run-gates turnstile` · `settings-merge selftest` ·
`spec-tokens self-test` · `straggler-guard arms` · `transition-audit arms` ·
`codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` ·
`memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit selftest` ·
`govkit refusal join` · `govkit acceptance matrix` · `spawn budget (forks per hot entrypoint)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · a key that ignores the declared class, a reused verdict writing an entry, a sample that never reds · none
New arm: tools/run-gates/run-gates.test.sh · covers none · the manifest key set refusing a near-miss of `reads` · none
New arm: .githooks/pre-push.test.sh · covers AC12 AC13 AC14 AC15 · a moved tip still reusing, a reusing run stamped full, a planted reused record accepted, an inherited knob honoured · none

## 8. Open questions

- **F1 — Push-time reuse of the `remote` legs, keyed on the tip `ls-remote` observes at the push?**
  The trio is the bulk of the default bar's leg-seconds per the research (5780 of 7640, PINNED at
  fa68a767). Two of them grade only the commits `HEAD` carries past the advertised tip, so
  `(HEAD, tip, inputs)` determines their verdict.
  - (a) Not in this unit: `remote` legs never reuse; revisit once S6 has evidence. Crosses no rule.
  - (b) In this unit: probe the tip first and allow reuse at pre-push for `remote` and `history`
    legs at the exact pushed sha, stamped `scoped` and never `full`. Crosses "an authoritative run
    never reuses" (`tools/run-gates/README.md`, `.githooks/pre-push`).
  - Recommendation: (a).
  - RESOLVED (owner, 2026-10-10): (b) in this unit: push-time reuse of the remote-reading legs at the exact pushed sha, stamped scoped.
- **F2 — The sample rate.**
  - (a) 0.25, drawn uniformly per leg: about 78% detection within 5 runs, certain within 10 with S7.
  - (b) 0.25, cost-weighted: one expensive leg per run by round-robin plus 25% of the rest, so the
    sample's own cost stays near a quarter of the saving.
  - (c) 0.10: cheaper, 41% within 5 runs.
  - Recommendation: (a) for this unit; (b) once per-leg hit rates are recorded.
  - RESOLVED (owner, 2026-10-10): (a) 0.25 uniform.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §1 §2 §3 §4 §5 §6 §7 S2 S8 S9 S10 S11 AC12 AC13 AC14 AC15 · folded the owner's F1
  ruling (b): push-time reuse of `remote` and `history` legs at the exact pushed sha and observed tip,
  the tip probed with `ls-remote` first, the run stamped scoped, a `reused` field and predicate 9 so a
  reused verdict never satisfies the full green, and the never-reuses rule changed in all four places
  it is stated, with Readers.
- rev-3 · 2026-10-12 · S1 S2 S3 S11 §4 · build-time divergences: govkit and the two kit descriptors
  join S1's Readers, since govkit compares and emits the key and the manifest holds four `impure`
  rows; the `remote` key adds the digest of the whole `ls-remote --heads` advertisement, because the
  unattended kit gate grades every head; the environment digest drops `GATE_BASE`, `GATE_PUSH_BASE`,
  `GATE_RUN_ID` and `GATE_REUSE*`, without which AC1 cannot hold, and `REUSE_SCHEMA` moves to 3; S3's
  population is stated as re-read; `GATE_REUSE_PUSH` is cleared beside `GATE_DOCS_BASE` so a STUB
  bar cannot inherit it either; the day seam, the age and quarantine files, the draw, the re-run, the
  one-process cache write and prune, and the probe idiom are pinned.
- rev-4 · 2026-10-12 · S3 §4 §7 · the drift-audit records declare `base` beside `history`, since they
  compare against a base ref; §7 names the three govkit legs the files-touched list trips and the
  spawn budget, whose two run-gates rows rise by the cache's one python per bar, with
  `memory/project/fork-ceilings.txt` added to the files touched.
- rev-5 · 2026-10-12 · §4 · the fork ceilings leave the files touched again: measured by
  `fork-count.sh --only`, the one-leg and two-leg rows read 51 and 53 forks with this change and at its
  parent alike, since the cache's python is an exec and no fork to that counter. Both rows already
  read STALE against ceilings of 72 and 74 at the parent, a saving an earlier unit did not bank.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "reuse a proven green leg verdict keyed on inputs"` ranks generic
`key`/`legs` symbols and no reuse seam; the seam this unit extends is the existing one,
`input_key` and the reuse block in `tools/run-gates/run-gates.sh` (TOOL-aPacedTurnstile-6, the reuse
unit), with the common-dir convention `gate-full-green.shared` and the turnstile already use. No
second key or store is built beside them.

Recall terms used: GATE_REUSE reuse proven green ledger input_key impure fingerprint gate-full-green
reuses stamp BASE
