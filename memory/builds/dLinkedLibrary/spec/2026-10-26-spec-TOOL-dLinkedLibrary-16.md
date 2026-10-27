# TOOL-dLinkedLibrary-16 — the code replay: a unit's files read and its lookups counted with the `code` slot and without, scored by the scorer factory against the seed alone

**Status:** DEFERRED · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 19 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0253@22d88118 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md) | research | TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-27-build-TOOL-dLinkedLibrary-16-deviation-161.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-16-deviation-161.md) | deviation | — |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-20 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-20 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

The night pass made the per-item `code` slot core on one probe: on the unit dispatch 102 replayed,
the seed's one-hop neighbourhood and kit siblings held 16 of the 20 files its spec writer read where
the seed alone held 5 (research-code-orientation.md:91). That was one unit, read from its old
transcripts. This unit replays builds with the `code` slot handed and without it, counts each run's
files read and lookups, and scores them through dFairHearing's scorer factory on the losing test the
code research committed before its probe: the slot loses if its recall of the files the unit then
read is no better than its seed's alone (night pass point 3).

## 2. Scope (IN)

The scorer is TOOL-dFairHearing-12's factory `tools/workflows/replay_scorer.py` (S1: `INSTANCES`,
`derive_paired_cases`, `read_raw_output`), its manifest check `check_experiment` (TOOL-dFairHearing-23
S4) and its run procedure TOOL-dFairHearing-30 S1 to S3 (one fresh clone per case, arm and attempt,
clean before the call). The transcript counts are TOOL-dTotalRecall-17 S1's `count_existence_searches`
over runlog's `resolve_session_tree`, `read_records` and `extract_segments`
(`tools/runlog/extract.py:266`, `:308`, `:372`, verified at base). The record is TOOL-dTotalRecall-8's,
derived at a past tree by `code_record.py --tree <rev>`. All but runlog are DEFERRED at base
`5fede642` and are a build-run precondition.

- **S1** — The `code-replay` instance (shared interface I19), a fourth row of the factory's
  `INSTANCES` beside `review-replay`, `scouted-seam` and TOOL-dTotalRecall-17's `map-replay`:
  `replay_scorer.py --instance code-replay --manifest <src>`. It pairs cases and arms only through
  `derive_paired_cases`, so the factory's conformance arm `scan_pairing_sites` reads it clean.
  Observed by AC4 and AC7.
- **S2** — The corpus, derived before any run: `replay_scorer.py --instance code-replay --corpus`
  prints TOOL-dRedressedBar-24, the unit the research replayed (its build commit `73b80ed31`), and
  the two most recent CLOSED Tier-2 units at the pass base whose build commit changes at least five
  files of the population P (§4 "The counts") in at least two kits, each with its build commit, its
  spec and its brief at that commit's parent. The pass commits the manifest holding them before the
  first run. Observed by AC5.
- **S3** — The seed and the slot. A unit's seed is the build's declared write set: the backticked
  paths under its spec's `### Files touched (estimate)`, read by `extract_files_touched`
  (`tools/check-spec-tokens.py:564`) loaded by path from the repository scored, kept where they are
  in P. `render_code_slot(record, seed)` renders the research's candidate B: the seed files with each
  definition's key and range, then the files one `calls`, `tests`, `invokes` or `registers` edge away
  from a seed definition in either direction, through TOOL-dLinkedLibrary-14's `derive_callers`,
  `derive_callees` and `derive_tests`, then the seed files' kit siblings, as paths and ranges, never
  bodies. It stops adding lines at 16 KiB (NP-8's answer, PINNED), and the manifest records the last
  file it named. Observed by AC2.
- **S4** — The runs. For each corpus unit, two arms, `without` and `with`, two runs each: one fresh
  clone per unit, arm and attempt at the build commit's parent, run as TOOL-dFairHearing-30 S1 to S3
  say, each one `Workflow` call of `tools/workflows/unattended-unit.js` building the unit from its
  spec and brief. The `with` arm's brief is the unit's brief with one `### task:code` section
  appended holding the slot, written outside the clone, so the clean check still holds. Observed by
  AC6.
- **S5** — The counts, per run, from the builder's transcript: `read_files`, the files of P the run
  read (§4 "The counts"), and `lookups`, `count_existence_searches`'s figure. Observed by AC1.
- **S6** — The verdict, `derive_code_verdict(manifest)`: R is, per unit, the union of the `without`
  arm's `read_files`; the slot's recall is the files of R the rendered slot names, and the seed's the
  files of R the seed names, each summed over the corpus and divided by R's summed size. The slot
  loses when its recall is no better than the seed's. The `with` and `without` arms' median `lookups`
  and `read_files` are reported beside it and decide nothing. Observed by AC3.
- **S7** — The record,
  `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-16-code-replay-verdict.md`,
  opening `**Serves:** research TOOL-dLinkedLibrary-16`, carrying `**Verdict:** win` or
  `**Verdict:** lose`, both recalls, the reported medians, the manifest's path, and each clone's
  name, `HEAD` and status before its call; the manifest beside it,
  `<date>-build-TOOL-dLinkedLibrary-16-code-replay-manifest.json`. Observed by AC6.
- **S8** — The fixture, `replay_scorer.py --instance code-replay --fixture --plant <case>`: a scratch
  repository with a derived record, a spec carrying a Files touched estimate, and canned builder
  transcripts under a private projects root. The plants are §6's. Observed by AC1 to AC5 and AC7.

## 3. Non-goals (OUT)

- The per-item `code` slot as a product, its budget key and its roles: dBoundRoles' (§8 F1's ask);
  S3's render is this experiment's arm and is never handed to a work order.
- A spec-writer replay: a past spec writer's seed, its scope paths, has no declared source at the
  corpus units' bases, while a builder's write set is its spec's estimate (§8 F2).
- Editing the factory's other instances, its pairing or the run procedure: TOOL-dFairHearing-12, -23
  and -30's, called here.
- The map's replay: TOOL-dTotalRecall-17's `map-replay`, whose transcript readers this unit shares.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-14` — `gov_code.py`, its `derive_callers`, `derive_callees` and `derive_tests`, from which S3 renders the slot's one hop
- **consumes-from** external — TOOL-dFairHearing-12 S1 and S6, TOOL-dFairHearing-23 S4 and TOOL-dFairHearing-30 S1 to S3 (the factory, its manifest check and its clone procedure), TOOL-dTotalRecall-17 S1 (`count_existence_searches`) and TOOL-dTotalRecall-8 (the record at a past tree), DEFERRED at base and built before this unit's pass
- **hands-off** external — dBoundRoles, whose per-item `code` slot no spec carries: the verdict record of S7 is the input §8 F1's ask names
- **hands-off** `TOOL-dLinkedLibrary-52` — `measure_read_files`, which unit 52 re-points at the one shell-read definition (id 42)

## 4. Design

### Evidence

- The losing test, committed before its probe: candidate B loses when "not better than its own seed
  on recall of the feature files the agent then read (procedure tools excluded)"
  (research-code-orientation.md:91, the B column's losing-test row).
- The research's unit: TOOL-dRedressedBar-24, its spec read from `5b30e4b47` and its build from
  `73b80ed31`, which changed 22 files (`git show --stat 73b80ed31`, verified at base); its spec's
  Files touched names 16 paths (`memory/builds/dRedressedBar/spec/2026-10-15-spec-TOOL-dRedressedBar-24.md`).
- No dBoundRoles spec names a `code` slot: `git grep -l "code slot\|memory.code-budget\|code-roles"
  -- memory/builds/dBoundRoles/spec/` prints nothing at base, as scout C found.

### The counts

- **P, the population.** The paths of the record's `code_file` rows at the clone's commit, outside
  `memory/`, not ending `.md`, and not a skipped row: the "feature files", with records, guides,
  specs and prompts, the procedure's own reading, left out.
- **read_files.** The paths of P a run opened: the `file_path` of each `Read` call, and each
  operand of a shell segment whose program is `cat`, `head`, `tail`, `sed`, `awk`, `less` or `wc`
  that names a path of P, read by `extract_segments`. Each path counts once per run.
- **lookups.** `count_existence_searches`: `Grep` and `Glob` calls and shell segments whose program
  is `grep`, `rg`, `find`, `ls`, `git grep` or `git ls-files` (TOOL-dTotalRecall-17 §4 "The terms").

### The runs

| Corpus unit | Arms | Runs per arm | Clone names |
|---|---|---|---|
| the research's unit, TOOL-dRedressedBar-24, and its two S2 derives | `without`, `with` | 2 | `k<u><a><n>`, `<u>` 1 to 3, `<a>` `o` or `w`, `<n>` the attempt from 1 |

Twelve builder runs. A run whose clone is not clean before its call, or whose builder dies, takes the
next attempt in a new clone, as TOOL-dFairHearing-30 S2 and S3 say; every attempt is in the record.

### Inventory

Minted: the instance key `code-replay`; `render_code_slot`, `measure_read_files`,
`derive_code_verdict` and `derive_code_corpus` in `replay_scorer.py`; the flags `--corpus`,
`--fixture` and `--plant` of the instance; the verdict record and its manifest. Naming cells: each
function asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None.

### Rollout

The runs happen once, at this unit's pass in the build run.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`: the `code-replay` instance
- `tools/workflows/README.md`: the factory paragraph names the fourth instance
- `tools/workflows/tier2-review.template.js`: the workflows kit's version line, moved with its shipped bytes
- `tools/workflows/tier2-review.js`: its render
- `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-16-code-replay-verdict.md` (new)
- `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-16-code-replay-manifest.json` (new)

### Alternatives rejected

- **Score the research's old transcripts only.** They are one unit, read on one node, and carry no
  `with` arm; the clause asks for the slot handed and not.
- **Wait for dBoundRoles' slot.** No spec carries it, so the clause's test would wait on a build
  this one cannot schedule (§8 F1).
- **A scorer beside the factory.** TOOL-dFairHearing-12's conformance arm reds a second pairing site.

## 5. Production-readiness checklist

- security — every run is in a throwaway clone under `%TEMP%`, never the working repository; the
  slot is rendered from tracked text and handed as a brief section, not as a tool grant.
- perf / scale — twelve builder runs, the cost of one build pass each; the scoring itself reads
  transcripts and the record once.
- error / empty / loading states — an unpaired case, a missing transcript, an absent
  `check-spec-tokens.py` or an empty R is a refusal naming it, never a score.
- observability — the record names every clone, its status and both recalls.
- risks — a corpus of three units is small; the verdict is the clause's test as the research wrote
  it, and the record states the corpus size beside the result.
- testing — the plants of S8.
- migration — none.
- user docs — none: `help/` covers neither the scorer factory nor the replays, as
  TOOL-dFairHearing-30 records.

## 6. Acceptance criteria

- **AC1** — When `python replay_scorer.py --instance code-replay --fixture --plant counts` reads a
  canned transcript with three `Read` calls (two of P, one a spec), one `sed -n` segment over a file
  of P, and two `Grep` calls, it reports `read_files` 3 and `lookups` 2.
  Red when: a spec or record read is counted, or a shell read is missed.
- **AC2** — When the plant `slot` renders the slot for a seed of one file whose function is called
  from a second kit's file and tested by a third, the render names the seed with its ranges, then the
  caller and the test, then the seed's kit siblings, and holds no body text; with the cap set below
  the render, the manifest names the last file kept.
  Red when: a one-hop file is missed, a body line appears, or a cut is unrecorded.
- **AC3** — When the plant `verdict` scores a manifest whose `without` runs read a file only the
  slot's one hop names, the verdict is `win`; with that file removed from every run's reads, the two
  recalls are equal and the verdict is `lose`.
  Red when: equal recalls read as `win`, or the `with` arm's counts move the verdict.
- **AC4** — When the plant `unpaired` scores a manifest in which one arm answered a case the other did
  not, `derive_paired_cases` refuses naming the case; with a transcript path that does not exist, the
  instance refuses naming the path.
  Red when: a partial population is scored.
- **AC5** — When `replay_scorer.py --instance code-replay --corpus` runs at the pass base, it prints
  three units, TOOL-dRedressedBar-24 first with `73b80ed31`, each with its build commit, spec and
  brief path.
  Red when: the research's unit is missing or a unit with fewer than five files of P is chosen.
  figure: the two derived units are DERIVED at the pass base; `73b80ed31` is PINNED.
- **AC6** — When the pass runs the twelve builds and writes S7's record, the record carries a
  `**Verdict:**` line, both recalls, and for every attempt its clone name, `HEAD` and an empty status
  before its call.
  Red when: an attempt is missing from the record, or a status before a call is not empty.
  cost: twelve builder runs and their clones, the price of twelve build passes.
- **AC7** — When the factory's conformance arm `scan_pairing_sites` walks the tool root at the pass
  tip, it names no site in the `code-replay` instance.
  Red when: the instance pairs arms with cases outside `derive_paired_cases`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `review-replay selftest` · `kit epoch (shipped bytes move, the version moves)` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms`

New arm: tools/workflows/replay_scorer.py · covers AC1 AC2 AC3 AC4 AC5 AC7 · the `code-replay` plants run inside the `review-replay selftest` leg's factory arms, its failing case staged by a verdict that compares the `with` arm's reads · that leg's declared factory total, raised by the plants

## 8. Open questions

- **F1 — The slot under test has no spec: no dBoundRoles spec carries the per-item `code` slot.**
  Options: (a) render the slot here from the code record by the research's candidate B rule, as this
  experiment's arm, and ask dBoundRoles to spec the product slot from the verdict; (b) wait for
  dBoundRoles' spec; (c) spec the product slot in this unit. (b) leaves the clause's test unrun;
  (c) builds another build's surface. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. The ask,
  for the main loop to file once: target dBoundRoles' `BACKLOG.md`, "THE PER-ITEM `code` SLOT HAS NO
  SPEC. v2 and TOOL-dTotalRecall-8 §3 give the `code` slot to dBoundRoles and no dBoundRoles spec
  carries it; TOOL-dLinkedLibrary-16 replays candidate B's render against its seed", accept "a
  dBoundRoles spec carries the per-item `code` slot, its seed, budget and roles, taking its render
  rule from TOOL-dLinkedLibrary-16's verdict record, or holding the slot unrendered on a `lose`".
  widens: none · relaxes: none
- **F2 — Which role is replayed?** Options: (a) the builder, seeded by its spec's Files touched
  estimate; (b) the builder and the spec writer, the spec writer seeded by its scope paths; (c) the
  spec writer only. A spec writer's scope paths have no machine-readable source at a past unit's
  base, so (b) and (c) would type a seed by hand, which the clause's "seed" does not admit.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the role whose seed is declared; the
  research's spec-writer figure stays its own record. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 16, night pass point 3,
  research-code-orientation.md:79-92 and :123, TOOL-dFairHearing-12, -23 and -30,
  TOOL-dTotalRecall-17 S1 and §4, and scout C's row for cl-0253.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.
- rev-3 · 2026-10-27 · §4 · "The runs" table's corpus-unit cell cites TOOL-dRedressedBar-24 after its
  opening words, so hygiene check 13 no longer reads the foreign id as defined here; nothing else moved.

## 10. Reuse audit

The seams extended: TOOL-dFairHearing-12's scorer factory, a fourth `INSTANCES` row pairing only
through `derive_paired_cases`; TOOL-dTotalRecall-17's `count_existence_searches` and its runlog
readers, shared rather than copied; TOOL-dFairHearing-30's clone procedure; TOOL-dLinkedLibrary-14's
edge readers for the one hop; and `extract_files_touched` (`tools/check-spec-tokens.py:564`) for the
seed. `python tools/codebase-map/reuse_lookup.py "score recall of files read in a replay with and
without a context slot"` ranked name stems (`read`, `read_text`, `score` in
`tools/memory-recall/bench.py`); `bench.py`'s `score` ranks a live retrieval per query and pairs no
committed population, which TOOL-dFairHearing-12 §3 records too, so no existing seam fits beyond the
factory. Scout C's runlog lines agreed with source at base. The recall query returned scout C's row
and TOOL-dTotalRecall-17's scout row, which names the same transcript readers.

Recall terms used: `python tools/memory-recall/query.py "how is the code slot scored against its seed by replaying a unit's file reads" --terms "code slot replay losing test seed one hop kit siblings recall files read scorer factory code-replay"`
