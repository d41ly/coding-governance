# TOOL-aSparedSpawn-13 — content-addressed reuse: declared read classes, a shared cache, a soundness sample

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `GATE_REUSE` worth turning on outside one worktree's second bar, without letting it lie. Today
the key carries `BASE` for every leg, so it misses after every landing; the store is one row per leg
in one git dir, so a fresh worktree starts cold; and the only statement about what a leg reads beyond
the tree is the boolean `impure`. aMeteredSweep's round-two research estimated 25014 leg-s reusable
against a green parent with the self-test tier on (`2026-10-09-build-TOOL-aMeteredSweep-1-research2-reuse.md`
§5 U1; PINNED, an estimate from leg-second sums over one contended profile at fa68a767, ±2x, not an
A/B). This unit takes that only behind a sample that would catch a wrong hit.

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
    population in prose, and states one such leg where the manifest carries three.
    by value: `tools/run-gates/run-gates.sh` reads the field's PRESENCE to decide reuse, and nothing
    reads the reason text.
- **S2** — The key. Per leg, one hash over what `TOOL-aSparedSpawn-1` already folds in (its content
  key for dirty guarded files, its toolchain, environment and host digest, and `REUSE_SCHEMA`), plus
  the manifest row's own bytes and only the read classes the row declares: `BASE` for `base`, the
  `HEAD` sha for `history`, the UTC day for `clock`. `BASE` enters no other leg's key. A leg declaring
  `remote` is never reused in this unit. Observed by AC1, AC2, AC3.
- **S3** — Declarations. Every leg the research's §1.4 found reading history, a base or the clock
  carries its class, each re-read against its script at build time. The research's list is a floor
  and not the population; a missed reader is what S6 exists to catch. Observed by AC2.
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
  neither `gate-full-green` nor the inherited-green record. Observed by AC8.

## 3. Non-goals (OUT)

- Reuse at the push boundary, including the `remote` trio keyed on an observed tip. That is F1, and
  this unit leaves `.githooks/pre-push`'s scrub of `GATE_REUSE` exactly as it is.
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
and a quarantine file per leg holding the row hash that quarantined it. A drawn leg is dispatched as
an ordinary leg and its line says it was sampled.

### Data model

- Cache entry: `ok<TAB>secs<TAB>run_id<TAB>head<TAB>ended`, one per key, about 100 bytes.
- Age counter: the count of consecutive reuses, reset to 0 by any execution.
- Quarantine: the manifest row hash at the time of the disagreement.

### Inventory

- The manifest key `reads` and its four class values; the directory
  `gate-cache` under the git common dir; the knob `GATE_REUSE_SAMPLE` for the rate, and a pinned-day
  seam for the `clock` arm, pinned the way the run id already is (TOOL-aGraftedHelix-7). New function
  names come from `lexicon.py --suggest` at build.

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

## 5. Production-readiness checklist

- security: the cache sits in the git common dir, never pushed; writers are this runner on a clean tree only; a run with full shell access can still forge an entry, which is why no reused verdict carries authority (S8).
- perf / scale: a lookup is a file read and spawns nothing; the per-run digest is `TOOL-aSparedSpawn-1`'s; the sample costs about its rate times the saving.
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

## 7. Gates

`recall floor` · `recall floor arms` · `run-gates gov canary` · `run-gates canary` · `run-gates evidence` · `codebase-map coverage + freshness` · `memory hygiene` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · a key that ignores the declared class, a reused verdict writing an entry, a sample that never reds · none
New arm: tools/run-gates/run-gates.test.sh · covers none · the manifest key set refusing a near-miss of `reads` · none

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
- **F2 — The sample rate.**
  - (a) 0.25, drawn uniformly per leg: about 78% detection within 5 runs, certain within 10 with S7.
  - (b) 0.25, cost-weighted: one expensive leg per run by round-robin plus 25% of the rest, so the
    sample's own cost stays near a quarter of the saving.
  - (c) 0.10: cheaper, 41% within 5 runs.
  - Recommendation: (a) for this unit; (b) once per-leg hit rates are recorded.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "reuse a proven green leg verdict keyed on inputs"` ranks generic
`key`/`legs` symbols and no reuse seam; the seam this unit extends is the existing one,
`input_key` and the reuse block in `tools/run-gates/run-gates.sh` (TOOL-aPacedTurnstile-6, the reuse
unit), with the common-dir convention `gate-full-green.shared` and the turnstile already use. No
second key or store is built beside them.

Recall terms used: GATE_REUSE reuse proven green ledger input_key impure fingerprint gate-full-green
reuses stamp BASE
