# TOOL-aSparedSpawn-32 — reconcile the build with origin/main 37200355

**Status:** CLOSED · rev-4 · 2026-10-12 · node a · Tier-2 · base fce4b707 · streams tooling · order 5 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md) | journal | — |
| [2026-10-12-build-TOOL-aSparedSpawn-32-fixtures.sh](../build/2026-10-12-build-TOOL-aSparedSpawn-32-fixtures.sh) | journal | — |
| [2026-10-12-prompt-TOOL-aSparedSpawn-32-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aSparedSpawn-32-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge origin/main at 37200355d into the run branch before the close's bar, so that the bar and the
lander grade the tree that will land. Origin is 183 commits past the merge-base 69e0ff0f5. Those
commits carry aDistilledCharter, aFrugalTurnstile, dHomedResolver, dRemeasuredRender, aHomedAnchor,
aSparedHolder, aSignalledHook and aBenchedProbe. A trial `git merge --no-commit origin/main` taken
by the driver conflicted in 16 files.

## 2. Scope (IN)

The conflict set is the driver's trial merge at this base; the builder re-takes it at the merge and
records any difference in the ledger. Conflicted files, with hunk counts:

| File | Hunks | Kind |
|---|---|---|
| `tools/run-gates/run-gates.sh` | 11 | product |
| `.githooks/pre-push` | 7 | product |
| `tools/run-gates/run-gates.evidence.test.sh` | 3 | suite |
| `tools/run-gates/README.md` | 3 | doc |
| `tools/run-gates/run-gates.turnstile.test.sh` | 1 | suite |
| `tools/push-main.test.sh` | 1 | suite |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 1 | suite |
| `tools/hooks/agent-cap.test.sh` | 1 | suite |
| `.githooks/pre-push.test.sh` | 1 | suite |
| `.memory-tree.conf` | 1 | conf |
| `memory/guides/SESSION-KICKOFF.md` | 1 | stamps |
| `memory/backlog/TOOL.md` | 1 | generated |
| `memory/map/features/run-gates.md` | 1 | dossier |
| `memory/map/generated/symbols.json`, `MAP.md`, `CARDS.md` | 1 each | generated |

- **S1** — Every conflict in a product, suite or doc file is resolved by keeping BOTH sides' intent,
  never by picking a side. Each conflicted file's merge result is then diffed against BOTH parents,
  so that no hunk either side added is lost. This covers the "auto-took" class, a conflict-free hunk
  silently taken from one side, and the merge-drops-a-side's-hunks class `TOOL-dUnstuckLanding-26`
  names. Where both sides rewrote one function, the result carries both behaviours, and the ledger
  says how they compose. Observed by AC1 and AC2.
- **S2** — Generated files are re-rendered, never hand-merged. `memory/map/generated/symbols.json`,
  `MAP.md` and `CARDS.md` come from `python tools/codebase-map/gen_map.py --write`, and
  `memory/backlog/TOOL.md` and the build index from `python tools/memory-tree/gen_build_index.py --write`,
  each run after the hand-merged sources are resolved and staged. Observed by AC3.
- **S3** — The kickoff manifest's stamps, `last-audit` and `last-body-change` in
  `memory/guides/SESSION-KICKOFF.md`, take origin's side at the merge. They are re-stamped in a
  follow-up commit after the merge commit, per the manifest's merge exception, because a commit
  cannot carry its own sha. Observed by AC4.
- **S4** — The `.memory-tree.conf` conflict is resolved additively, keeping both sides' keys and
  their comment blocks. The run-gates dossier, `memory/map/features/run-gates.md`, is merged by hand
  keeping both sides' claims, and its claims must still name live inventory keys. Observed by AC5.
- **S5** — The post-merge direct checks are green. A row this build owns in
  `memory/project/fork-ceilings.txt` or `memory/project/spawn-idiom-sites.txt` is re-measured when
  origin's changes to the runner or the hook moved its count, and the ledger records both readings.
  Observed by AC6.

S6 to S10 compose the two reuse designs, per the owner's ruling in §8 F1: origin's LINEAGE reuse
(`TOOL-aFrugalTurnstile-4`) and this build's content-addressed CACHE reuse
(`TOOL-aSparedSpawn-13`, `-16`, `-17`). §4 "Composing the two reuse designs" is the contract; these
items are what it builds.

- **S6** — Disjoint knobs, one read site. Lineage reuse is asked for by a new knob,
  `GATE_REUSE_LINEAGE`, which `.githooks/pre-push` exports on a FULL decision for a runner bar where
  origin exported `GATE_REUSE=lineage`. Cache reuse keeps `GATE_REUSE` (the env mode) and
  `GATE_REUSE_PUSH` (the push mode). The runner reads the three knobs once, at the site of origin's
  `REUSE_MODE=${GATE_REUSE:-}; unset GATE_REUSE`, into `REUSE_ASK_ENV`, `REUSE_ASK_PUSH` and
  `REUSE_ASK_LINEAGE`, and unsets all three there; the mode block reads those variables and never the
  environment. The hook clears an inherited `GATE_REUSE_LINEAGE` for every bar, a STUB included,
  beside `GATE_REUSE_PUSH`, and names it on the `not honoured from the environment` line. Observed by
  AC9 and AC10.
  - **Readers:** by name: READER NOT IN TREE — the `lineage` value of `GATE_REUSE` is spelled only
    on origin/main 37200355d, by its hook's FULL branch, its runner's reuse block, its README and its
    two suites' lineage arms, which this merge brings in and S6 and S10 re-stage. by value: the
    runner's reuse block branches on the mode, and its header writes the mode as `reuse`.
- **S7** — One mode per run, by a fixed precedence. Under `GATE_FULL` the mode is `lineage` when
  `REUSE_ASK_LINEAGE` is set and `off` otherwise, and a set `GATE_REUSE` or `GATE_REUSE_PUSH` is
  named as not used. Without `GATE_FULL` the mode is `push`, then `env`, then `off`, exactly as this
  build's mode block decides today, and a set `GATE_REUSE_LINEAGE` is named as not used. The header's
  `reuse` key records the one mode: `off`, `env`, `push` or `lineage`. Observed by AC10 and AC12.
- **S8** — The stamp says which kind of reuse it carries. `gate-full-green` keeps origin's
  `reused <n>`, the legs the run carried forward, and gains `reused_cache <n>`, the legs it took from
  the cache, always 0 on a full green. Predicate 9 in `.githooks/pre-push` forces FULL when
  `reused_cache` is non-zero, or when it is absent and `reused` is non-zero, because a record written
  before the composition cannot say which kind it reused. A full stamp with `reused` above 0 and
  `reused_cache` 0 is a lineage stamp, keeps origin's meaning, and does not force the next push FULL.
  The inherited-green stamp keeps "reused nothing" on both sides. Observed by AC7 and AC8.
- **S9** — The texts. `tools/run-gates/README.md` states each rule once: the cache's env and push
  modes, lineage at the boundary's FULL decision, the precedence, the two stamp fields and
  predicate 9's reading. The runner's mode block and the hook's scrub, FULL branch and predicate 9
  comments each state the rule they implement once and point at the README for the other. Origin's
  not-checked sentence for lineage and this build's for the cache both survive verbatim. Observed by
  AC11.
- **S10** — The arms of both sides re-staged to the composed names. Origin's lineage arms set
  `GATE_REUSE_LINEAGE` and read `reuse lineage` from the header; origin's opt-in arms over the
  ledger are re-staged on the cache env mode, which has been the opt-in store since this build's
  `TOOL-aSparedSpawn-13`; this build's predicate-9 arm plants `reused_cache 1`.
  NOT OBSERVED by a criterion of its own: each re-staged arm executes when its suite runs at the
  close, and AC1 and AC2 account for every line either side added.

## 3. Non-goals (OUT)

- A kit version mint. The lander mints every carrier at `--prepare`.
- Running any suite or the bar inside the pass. The close's bar runs once, after this unit.
- Any behaviour change beyond reconciling the two sides, which for reuse is the composition §4
  states. A defect found in either side's code is recorded as an ask, not fixed here.
- Re-deriving origin's own records, decisions or backlog rows. They arrive as origin wrote them.
- The reuse digest's view of the hook's environment is `TOOL-aSparedSpawn-33`, not this unit.
- Any change to either reuse design's own terms: lineage's four row terms and its base filter, and
  the cache's key, sample and age bound, arrive as each side wrote them. The composition decides
  only which knob asks for which design, which mode a run takes, and what the stamp records.

### Edges

- **hands-off** `TOOL-aSparedSpawn-33` — the digest's view of the hook's environment, read beside
  `REUSE_ASK_PUSH` at the one knob read site this unit builds.

## 4. Design

The merge follows the build's earlier reconcile, b9b24646f, and aMeteredSweep's two, 345900823 and
2da5ad1d6: a `--no-ff` merge commit named `merge: origin/main 37200355 into aSparedSpawn`, then a
pass commit, then a stamps commit. The merge commit carries `Pass: none`, as those three did: the
commit-msg hook's `--check-commit` grades a trailered commit's whole index against the pass's
declaration, a merge's index holds every path origin's 183 commits moved, and two of them,
`memory/DECISIONS.md` and `memory/project/readme-contract.txt`, are shared records `--dispatch`
refuses to declare. A merge commit also lists no paths to `diff-tree`, so check 23 could not
attribute the pass to it. The pass commit after it, `Pass: TOOL-aSparedSpawn-32`, carries this
spec's CLOSED header and the acceptance ledger, which is a write check 23 can grade. The order
inside the merge is fixed so that generated output is rendered from the resolved sources:

1. Resolve the product, suite and doc conflicts by hand, both sides kept, and stage them.
2. Resolve `.memory-tree.conf` and the run-gates dossier additively, and stage them.
3. Take origin's side of the manifest stamps.
4. Run `gen_map.py --write` and `gen_build_index.py --write`, and stage what they change.
5. Run the two-parent diff over every conflicted file and record the result in the ledger.
6. Run the direct checks, then commit the merge.

The two-parent diff reads, per conflicted file F, every line `git diff 69e0ff0f5 37200355d -- F`
adds and every line `git diff 69e0ff0f5 fce4b707 -- F` adds, and checks each is present in the
result or is justified by a ledger line. The justification is either a line the other side rewrote
on purpose or a line both sides moved.

### Composing the two reuse designs

Kept side by side, the two designs disable each other. Origin's `unset GATE_REUSE` sits about 900
lines above this build's mode block, which reads `GATE_REUSE`, so the env mode never fires. And a
lineage FULL run stamps `reused <n>` with n above 0, which this build's predicate 9 reads as a reused
verdict, so every push after a lineage green is forced FULL and runs lineage again. The owner ruled
to compose both (§8 F1). The composition, in five parts:

**(a) Disjoint triggers and names.**

| Design | Asked for by | Set by | Store it reads | Mode |
|---|---|---|---|---|
| cache, env | `GATE_REUSE` | a person or a script, by hand | the common-dir cache | `env` |
| cache, push | `GATE_REUSE_PUSH` | `.githooks/pre-push`, on a SCOPED decision | the common-dir cache | `push` |
| lineage | `GATE_REUSE_LINEAGE` | `.githooks/pre-push`, on a FULL decision for a runner bar | the per-git-dir `gate-ledger.tsv` | `lineage` |

The runner reads all three at ONE site, origin's, right after `unset GATE_RUN_ID`:
`REUSE_ASK_ENV=${GATE_REUSE:-}`, `REUSE_ASK_PUSH=${GATE_REUSE_PUSH:-}` and
`REUSE_ASK_LINEAGE=${GATE_REUSE_LINEAGE:-}`, then `unset GATE_REUSE GATE_REUSE_PUSH GATE_REUSE_LINEAGE`,
so a leg's nested runner inherits no mode, which is origin's S4 intent extended to all three. The
mode block, later, reads only the `REUSE_ASK_*` variables. `GATE_REUSE_SAMPLE` and `GATE_REUSE_DAY`
stay read where they are, as the cache's seams. The digest's env loop already leaves out every
`GATE_REUSE*` name, so the new knob changes no key. A lineage run reuses only from ledger rows; it
never reads a cache entry to decide a reuse. The cache's upkeep after the legs, the entry writes and
`TOOL-aSparedSpawn-17`'s erase on an executed red, runs on every run whatever its mode, because it
keeps the cache honest rather than sparing a leg.

**(b) The stamp distinguishes the two kinds.** Three counters: `reuses`, every reused leg;
`lineage_reuses`, origin's; and `cache_reuses`, this build's. The full-green preconditions are
`[ "$reuses" = "$lineage_reuses" ]` (origin's) AND `[ "$cache_reuses" = 0 ]`. The stamp writes
`reused` from `reuses`, as origin does, and `reused_cache` from `cache_reuses`. Predicate 9 reads
`reused_cache`; a stamp without that field and with `reused` above 0 forces FULL, the fail-safe
reading of a record that cannot say its kind. `read_green_file` gains `rec_reused_cache`, and the
inherited-green path reads the same pair.

**(c) `GATE_FULL` keeps meaning "no cache reuse".** Under it the cache modes never apply, exactly as
`TOOL-aSparedSpawn-13` S8 made it, and the boundary's lineage path is the one deliberate exception,
as `TOOL-aFrugalTurnstile-4` §4 records: its reused verdicts were earned by full runs on a clean
tree under an equal input key, which is why they may stamp.

**(d) When more than one could apply, one mode wins, by this table.**

| `GATE_FULL` | `REUSE_ASK_LINEAGE` | `REUSE_ASK_PUSH` valid | `REUSE_ASK_ENV` | Mode | Named as not used |
|---|---|---|---|---|---|
| set | set | any | any | `lineage` | `GATE_REUSE`, `GATE_REUSE_PUSH` when set |
| set | empty | any | any | `off` | `GATE_REUSE`, `GATE_REUSE_PUSH` when set (today's line) |
| empty | any | yes | any | `push` | `GATE_REUSE_LINEAGE` when set |
| empty | any | no | set | `env` | `GATE_REUSE_LINEAGE` when set |
| empty | any | no | empty | `off` | `GATE_REUSE_LINEAGE` when set |

The hook never sets two of them for one bar: `GATE_REUSE_LINEAGE` only on FULL, `GATE_REUSE_PUSH`
only on SCOPED, and it clears every inherited one first. The table governs a direct caller.

**(e) Each rule stated once.** The README section origin rewrote for its two ledger modes becomes one
section with three subsections, cache env, cache push and lineage, and one table, (d)'s. The
runner's mode block comment states (d) and points at the README for the rest; the reuse block keeps
both not-checked sentences, each beside the branch it describes. The hook's FULL branch comment
states lineage's rule, its SCOPED branch states the push mode's, and predicate 9's comment states
(b)'s reading. No comment restates another's rule.

**(f) What the merged code forces (rev-4).** Origin moved to 6e8f8b1da before the merge; the merge
takes that tip, and the conflict set is the same 16 files. Five points the merged code decides that
(a) to (e) do not name, each the narrowest reading that keeps both sides:

- Lineage's terms arrive as origin wrote them, read through this build's representations: origin's
  `impures[]` no longer exists, so "not declared `impure`" reads the manifest's legacy `impure` from
  `legreads`, as the cache block does; a `remote` leg with no observed remote is refused, the rule
  this build's runner states for every reuse of such a leg; and the key compares with the run's
  precomputed `INPUT_KEYS`, the one composition `input_key` also builds, rather than a spawn per leg.
- Predicate 9 moves into its own function, `check_green_reuse`, because origin's `check_green_record`
  signature gained a manifest path and a bar pair while this build's gained the reused field.
- The hook's `ls-remote` probe runs after origin's cover pass and post-merge red, and not under
  `--decide`, because a covered or decide-only push runs no bar and a post-merge red can turn the
  decision FULL.
- The reuse digest leaves out `GATE_TURNSTILE_HOLDER` beside `GATE_TURNSTILE_HELD`: origin's host
  turnstile exports the holder nonce to every bar before the digest is taken, which moved every key
  on every run and disabled the cache whenever the turnstile was on. This is a red the merge
  produced, fixed here; it is not the digest's view of the hook's environment, which stays
  `TOOL-aSparedSpawn-33`'s.
- Row 4 of (d)'s table governs where S7's "exactly as today" and the table disagree: a set but
  invalid `GATE_REUSE_PUSH` with `GATE_REUSE` set takes `env`, where today's block took `off`. The
  hook never sets both, so only a direct caller can reach it.

Not changed here, and recorded as owed: `tools/run-gates/post-merge.sh` and the unattended driver's
`_gknobs` scrub `GATE_REUSE` from the bars they run and not `GATE_REUSE_LINEAGE`, so an exported
lineage knob reaches a post-merge or close bar, which both run with the full flag.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `.githooks/pre-push`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/push-main.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/hooks/agent-cap.test.sh`
- `.githooks/pre-push.test.sh`
- `.memory-tree.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/backlog/TOOL.md`
- `memory/map/features/run-gates.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/project/fork-ceilings.txt`
- `memory/project/spawn-idiom-sites.txt`

### Alternatives rejected

- **Rebase the run branch onto origin.** It rewrites the build's recorded shas, which its ledgers,
  its review record and `RUN.md` cite.
- **Merge after the close's bar.** The bar would grade a tree that never lands, and the lander's
  own reconcile would meet these 16 conflicts with no unit to own them.
- **Take origin's side of the generated map files and re-render later.** The files would then
  describe neither parent until the re-render, and the map freshness leg grades every commit.

## 5. Production-readiness checklist

- security: the merged hook and runner keep both sides' scrubs and refusals; S1's two-parent diff is what shows none was dropped. S6 clears the new lineage knob for every bar, and S8 keeps predicate 9 refusing every cache-reused full stamp, reading an unlabelled one as cache.
- perf / scale: N/A — no new code path; a re-measured fork row records origin's cost, not a change of this unit's.
- error / empty / loading states: N/A — no behaviour change beyond reconciling.
- observability: the ledger records each conflicted file's resolution and its two-parent diff result.
- risks: a conflict resolved by picking a side drops a behaviour silently; S1's diff is the check, and a hunk both sides rewrote is the case to read twice. A full stamp written before the composition with `reused` above 0 forces one FULL push, which costs a bar and never a verdict.
- testing: the direct checks in AC6 at the merge; the suites and the bar run at the close.
- migration: N/A — no data or schema moves.
- user docs: `tools/run-gates/README.md` keeps both sides' sections, and its reuse section states the composed rules once each (S9).

## 6. Acceptance criteria

- **AC1** — When, for each conflicted product, suite or doc file F, every line
  `git diff 69e0ff0f5 37200355d -- F` adds is searched for in the merge result, each is present or
  carries a justification in the ledger. Red when: a line origin added is absent and unjustified.
- **AC2** — When the same search runs for every line `git diff 69e0ff0f5 fce4b707 -- F` adds, each
  is present or justified. Red when: a line this build added is absent and unjustified.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs on the merge commit, it exits 0,
  and `python tools/memory-tree/gen_build_index.py --write` leaves no diff. Red when: either reports
  a generated file stale, or a hand-merged one differs from its render.
- **AC4** — When `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` runs
  after the stamps commit, the audit stamp names the merge commit's sha. Red when: it still carries
  either parent's stamp.
- **AC5** — When `grep -c '^<<<<<<<\|^>>>>>>>' .memory-tree.conf memory/map/features/run-gates.md`
  runs, it counts 0 in each, and every key either parent's conf declares is declared in
  the result. Red when: a marker survives, or a key either side added is missing.
- **AC6** — When the merge commit is checked out, all of these exit 0:
  - `bash -n` on every conflicted shell file;
  - `python tools/govkit/govkit.py selfcheck`;
  - `python tools/memory-tree/check-arms.py --check`;
  - `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`;
  - `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg`, and
    the same with `--only run-gates-2leg`;
  - `python tools/codebase-map/gen_map.py --check`;
  - `python tools/check-spec-tokens.py`;
  - `bash tools/memory-tree/check-memory-hygiene.sh --staged`.

  Red when: any exits non-zero.
  figure: each fork count is DERIVED at observation; a row re-measured here records both readings.

Each of the six criteria below runs on a hand-built fixture: a scratch repository holding a copy of the merged
runner, hook and a two-leg manifest, with a local bare remote as `origin`, built as the evidence
suite's `ru_repo` and the pre-push suite's `run_rp_push` build theirs. Each is observed red against
the naive merge, both sides' bytes kept side by side, before the composition is written.

- **AC7** — When a fixture push reds on one leg, the leg is fixed, and the fix push runs FULL with
  `GATE_REUSE_LINEAGE` exported by the hook and stamps `gate-full-green` with `reused` above 0 and
  `reused_cache 0`, the next push of that sha takes no FULL decision from predicate 9: its decision
  line does not carry `reused`. Red when: the next push is forced FULL by the stamp's `reused`
  field, which the naive merge does.
- **AC8** — When a fixture's `gate-full-green` is planted with `reused_cache 1`, the push is forced
  FULL and its decision line names `reused`; with a planted stamp carrying `reused 2` and no
  `reused_cache` field, it is forced FULL too. Red when: either planted stamp is trusted.
- **AC9** — When a fixture bar earns an `ok` and a second bar runs with `GATE_REUSE=1`, the second
  prints `GATE reuse` for the leg and its run header records `reuse` as `env`. Red when: it executes
  the leg, which the naive merge does because origin's unset clears `GATE_REUSE` before this build's
  mode block reads it.
- **AC10** — When a fixture's cache holds an `ok` for a leg whose ledger row is not
  lineage-qualified, a bar with the full flag and `GATE_REUSE_LINEAGE=1` prints `GATE ok` for that
  leg, not `GATE reuse`, and its header records `reuse` as `lineage`. Red when: the lineage run
  reuses the cache's entry.
- **AC11** — When `grep -c 'WHAT LINEAGE REUSE DOES NOT CHECK' tools/run-gates/README.md` runs it
  prints 1, and the README's reuse section carries (d)'s precedence table once. Red when: a rule is
  stated twice or not at all.
- **AC12** — When a fixture bar runs with the full flag, `GATE_REUSE=1` and `GATE_REUSE_LINEAGE=1`,
  its header records `reuse` as `lineage` and stderr names `GATE_REUSE` as not used; without the full
  flag and with both set, the header records `env` and stderr names `GATE_REUSE_LINEAGE`. Red when:
  either run takes another mode, or names nothing.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` ·
`run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push self-test` ·
`pre-push bar self-test` · `pre-push run-log line` · `push-main self-test` · `branch-guard self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` ·
`transition-audit arms` · `straggler-guard arms` · `recall floor arms` · `recall floor` ·
`memory hygiene` · `codebase-map coverage + freshness` · `agent-cap self-test` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`harness arms (fail branches armed or pinned)` · `govkit selfcheck` · `manifest-check self-test` ·
`scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` ·
`hook destinations self-test` · `kit/dogfood doc parity`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC9 AC10 AC12 · the naive merge's unset before the mode block, a lineage run reading the cache, two knobs set at once · none
New arm: .githooks/pre-push.test.sh · covers AC7 AC8 · a lineage full stamp read by predicate 9, a planted cache-reused stamp · none

## 8. Open questions

- **F1 — How do origin's lineage reuse and this build's cache reuse coexist in the merged tree?**
  Kept side by side, origin's `unset GATE_REUSE` disables the cache's env mode, and predicate 9
  forces every push after a lineage green FULL. The options were to keep origin's lineage and retire
  the cache's env mode, to keep the cache and retire lineage, or to compose both.
  RESOLVED (owner, 2026-10-12): compose both reuse designs.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-12 · §4: the merge commit carries `Pass: none` and a pass commit after it carries the CLOSED header and the ledger, because `--check-commit` refused a trailered merge for staging `memory/DECISIONS.md`, a shared record no dispatch may declare, and `diff-tree` lists no paths for a merge commit.
- rev-3 · 2026-10-12 · §2 §3 §4 §5 §6 §7 §8 S6 S7 S8 S9 S10 AC7 AC8 AC9 AC10 AC11 AC12 · the merge pass
  aborted on the two reuse designs: origin's `unset GATE_REUSE` merged without a conflict above this
  build's mode block, and predicate 9 read a lineage stamp's `reused` as a cache reuse. The owner
  ruled to compose both (§8 F1). §4 states the composition: disjoint knobs read at one site, one
  mode per run by a precedence table, a `reused_cache` stamp field predicate 9 reads, `GATE_FULL`
  meaning no cache reuse with lineage the one exception, and each rule stated once. §3 names the
  digest's view of the hook environment as `TOOL-aSparedSpawn-33`.
- rev-4 · 2026-10-12 · §4 · the merge takes origin's moved tip 6e8f8b1da, and §4 (f) records five
  points the merged code decided that (a) to (e) did not name: lineage read through `legreads` and
  `INPUT_KEYS`, predicate 9 in its own function, the probe after the cover pass, the holder nonce left
  out of the digest, and (d)'s row 4 over S7; plus the post-merge and driver scrubs left owed.

## 10. Reuse audit

No existing seam fits: a reconcile is a git operation, and `tools/codebase-map/reuse_lookup.py`
indexes code symbols, not procedures. The precedent this unit follows is the build's own earlier
reconcile, b9b24646f (origin/main 69e0ff0f5 into aSparedSpawn), and aMeteredSweep's two,
345900823 and 2da5ad1d6, each a `--no-ff` merge with generated files re-rendered and stamps
re-taken after. The two-parent diff is the check the charter's §1 Landing rule names for the
auto-took class.

Recall terms used: reconcile merge origin/main auto-took two parents generated re-render
last-audit stamps merge exception conflict dossier additive
