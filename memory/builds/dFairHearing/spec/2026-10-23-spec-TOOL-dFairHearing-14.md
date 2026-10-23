# TOOL-dFairHearing-14 — the experiment shape's method, enforced or recorded by the scorer factory

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0081@3ad56b8f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-12 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

aScoutedSeam's figures held because of how they were measured: cases with objective evidence, a
held-out set frozen before any tuning and never read to change a prompt, one variable per arm, parsed
replies counted before any score is read, one blind judge per case with labels rotated, and the arms'
union read as one system, its held-out cases joining the benchmark's replay (night pass two, point
2). This unit makes each of those a rule the scorer factory `tools/workflows/replay_scorer.py`
enforces where committed outputs can show it, and records where they cannot, in the factory's module
and never a second one. An experiment declares itself once, in a committed manifest beside its raw
outputs, and the factory refuses one that breaks a rule it can check.

## 2. Scope (IN)

- **S1** — `check_experiment(manifest, repo)` and the CLI `replay_scorer.py --experiment <src>`, in
  `tools/workflows/replay_scorer.py`. The manifest is JSON read through `read_raw_output`, so it may
  open with `// **Serves:**` lines; §4 gives its shape. Every rule below runs before the first
  figure line, and a refusal exits 2 naming the rule, the arm or case, and the value. Observed by AC4
  and AC7.
- **S2** — Cases with objective evidence. Each instance in `INSTANCES` declares `case_evidence(case)`,
  and a case for which it returns nothing is refused by id. `scouted-seam` reads the case's `sha` and
  every `ground_truth` item's `path` and `why`; `review-replay` reads the known item's ref and the
  record it came from. An instance registered without the hook refuses at load. Observed by AC1.
- **S3** — A held-out set frozen before any tuning. A manifest naming `heldOut` names a working-tree
  path. `git log --format=%H -- <path>` must list exactly one commit, the freeze, printed on the first
  line; and no held-out case id may also be a tuning case id. "Never read to change a prompt" is
  printed as a recorded line, not checked. Observed by AC2.
- **S4** — One variable per arm. Each arm declares `settings`, and an arm naming a `base` must
  differ from that base's settings in exactly one key; zero keys or two or more is refused, naming
  them. An arm with no base declares no variable and is printed as a base. Observed by AC3.
- **S5** — Parsed replies counted before any score is read. Each arm declares `dispatched`; the
  factory prints `parsed <arm>: <n> of <dispatched>` for every arm, `n` the cases holding a parsed
  result row, before any figure line. An arm with no `dispatched`, or with `n` above it, is refused.
  Observed by AC4.
- **S6** — One blind judge per case, labels rotated. A manifest naming `judge.key` names the
  committed label key, `{<case>: {<label>: <arm>}}`. Each case must give each judged arm one label,
  and with two or more arms and two or more cases no arm may hold one label on every case. With no
  key the factory prints the rule as recorded, not checked, and why. Observed by AC5.
- **S7** — The arms' union read as one system, its held-out cases joining the replay. A manifest
  naming `union` names, per set, the arms read as one system; a case counts as covered when any of
  them covered its primary in the judge's verdicts, as aScoutedSeam's system reading does
  (`memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-13-system.py:315-331`).
  With `heldOut` declared the union is printed for tuning, held-out and the pooled population, so the
  held-out cases join the score instead of standing beside it. Observed by AC6.
- **S8** — The rules' arms run in the factory's runner, `replay_scorer.run_selftest`, which
  `review-replay selftest` already calls. Observed by AC7.

## 3. Non-goals (OUT)

- Judging whether a prompt was changed after reading a held-out case. No committed output shows it;
  S3 records it.
- Generating judge packets or rotating labels. The factory reads outputs and spawns nothing; the
  label key is an input it checks.
- A second module, a manifest schema file, or a manifest writer: the shape is §4's and the reader is
  `check_experiment`.
- Retrofitting manifests for past experiments. The proof's manifest lives in the arm and in AC6's
  probe, never as a new record under `memory/builds/aScoutedSeam/`.

### Edges

- **consumes-from** `TOOL-dFairHearing-12` — `replay_scorer.py`, `read_raw_output`, `derive_paired_cases` and `INSTANCES`; without the factory there is no module to hold the rules
- **hands-off** `TOOL-dFairHearing-1` — its replays declare a manifest and score through `check_experiment`
- **hands-off** `TOOL-dFairHearing-15` — its with-and-without replay declares its two arms in a manifest, one variable apart
- **hands-off** `TOOL-dFairHearing-18` — the whole-design walk's recall runs declare their manifest the same way
- **hands-off** `TOOL-dFairHearing-21` — finding id 39 (item H2) of the round-1 spec audit: the freeze check hashes the working-tree bytes against the freeze's blob and refuses a shallow history, which S3 does not
- **hands-off** `TOOL-dFairHearing-23` — finding id 2 of the round-1 spec audit: the review-replay manifest defined whole, its case, `dispatched`, `parsed` and `matched` (its S4, AC2)

## 4. Design

### Evidence

Measured 2026-10-23 at `3dca04036`, PINNED.

- The held-out file `memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json`
  has one commit in its history, `b6c828a92` ("freeze the held-out set"), and the same blob,
  `078445c2…`, at `5f8ef021d` and at HEAD. It is absent at `b0fe68f30`.
- `system.py system` over the tuning cases and the results at `5f8ef021d` (blob `219cf9a2…`), arms
  `m1cA@medium t1r@medium`, prints `# system m1cA@medium + t1r@medium: 21/23`; over the held-out
  cases with `m1c@medium t1r@medium` it prints `12/12`. The record states 33 of 35 pooled
  (`2026-10-18-build-TOOL-aScoutedSeam-3-1-system-and-held-out.md:82`).
- `system.py` changed in `5f8ef021d`, after the freeze; a rule that refused any prompt source
  touched after the freeze would refuse the experiment the method came from (§8 F2).
- `git log --all -- '*judge-key*'` lists nothing: aScoutedSeam's label keys were never committed, so
  its rotation can be recorded and not checked (§8 F3).

### The manifest

```json
{
  "instance": "scouted-seam",
  "cases": "<src>",
  "heldOut": "<working-tree path>",
  "results": "<src>",
  "arms": [
    {"name": "<arm>", "base": null, "settings": {"<key>": "<value>"}, "dispatched": 30},
    {"name": "<arm>", "base": "<arm>", "settings": {"<key>": "<value>"}, "dispatched": 30}
  ],
  "judge": {"verdicts": "<results key>", "key": "<src> or null"},
  "union": {"tuning": ["<arm>", "<arm>"], "heldOut": ["<arm>", "<arm>"]}
}
```

`heldOut`, `judge` and `union` are optional; every other key is required, and an unknown key is
refused so a misspelt rule is never skipped. `settings` values are compared as JSON values. The
`review-replay` instance takes `known` and `candidates` in place of `cases` and `results`.

### Output order

1. `held-out: frozen at <sha> · <n> case(s) · never read to change a prompt — recorded, not checked`
2. One `arm <name>: base` or `arm <name>: varies <key> from <base>` line per arm.
3. One `parsed <arm>: <n> of <dispatched>` line per arm.
4. The judge line: checked, or recorded with its reason.
5. Figures: paired through `derive_paired_cases`, then the union per set and pooled.

Lines 1 to 4 print before any figure, so a reader meets the counts before a score, as S5 requires.

### What the rules do not check

S4 compares declared settings, so a variable nobody declared is invisible. S3 proves the file was
written once and its ids are disjoint, never that a prompt author did not read it. S6 proves the key
rotates; that one judge read each case is the spawn's to show, and the key cannot. S2 proves evidence
is present, never that it is right.

### Inventory

| Identifier | Kind | Lexicon verb |
|---|---|---|
| `check_experiment` | function | check |
| `check_held_out_frozen` | function | check |
| `check_one_variable` | function | check |
| `measure_parsed` | function | measure |
| `check_judge_rotation` | function | check |
| `measure_union` | function | measure |
| `case_evidence` | instance hook | — |

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`

### Alternatives rejected

- **Flags on the CLI instead of a manifest.** Arms, settings and dispatched counts are per-arm data;
  flags would be typed beside the outputs they describe and lost with the shell history.
  aScoutedSeam's own rule is that instruments and result rows are committed beside the record
  (`PLAY-aMendedFleet-2`).
- **A second module for the method.** The clause forbids it, and the rules read the same instances
  and pairing the factory owns.

## 5. Production-readiness checklist

- security — no write path; `git log` runs with argv on a path the manifest names, refused when it
  opens `-` or leaves the repository.
- perf / scale — one `git log` per held-out path; the rest is in memory.
- error / empty / loading states — each broken rule exits 2 by name; a manifest with no arm refuses.
- observability — the four lines before the figures say what was checked and what was only recorded.
- risks — a rule too strict for a real experiment; AC6 runs the method's own experiment through it.
- testing — AC1 to AC7 as probes and fixtures; the arms run in `review-replay selftest`.
- migration — none; past experiments are untouched.
- user docs — the kit README's factory paragraph names `--experiment`; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When the factory `replay_scorer.py` runs `--experiment <m>` over a scratch manifest
  whose cases file is the tuning corpus with one positive case's `sha` blanked, it exits 2 naming
  that case and `case_evidence`.
  Red when: a case without evidence is graded.
- **AC2** — When the manifest's `heldOut` names the real held-out file, the first line reads
  `frozen at b6c828a92…` and the run proceeds; in a scratch fixture repository where the held-out file
  has two commits, `--experiment` exits 2 naming the second; and with one held-out id copied into the
  tuning cases it exits 2 naming that id.
  Red when: the freeze reads only the newest commit, or the overlap passes.
  fixture: the scratch repository goes under `%TEMP%/<short-name>`, since a clone path under the
  session scratchpad exceeds the Windows path limit.
- **AC3** — When two arms share `settings` but for `effort`, the run prints `arm m1b@medium: varies
  effort from m1b`; with `effort` and `model` both changed it exits 2 naming both keys; with no key
  changed it exits 2 naming the arm.
  Red when: an arm two variables from its base is scored.
- **AC4** — When a valid manifest runs, every `parsed` line precedes the first figure line in stdout;
  an arm without `dispatched` exits 2 naming it; an arm whose parsed count exceeds `dispatched`
  exits 2 naming both numbers.
  Red when: a figure prints before its arm's parsed count, or an undeclared dispatch count reads as
  zero.
- **AC5** — When `judge.key` names a scratch key rotating two arms over three cases, the judge line
  reads checked; with one arm holding `ARM-A` on every case it exits 2 naming that arm; with
  `judge.key` null it prints `labels rotated — recorded, not checked: no committed key`.
  Red when: a constant label passes, or an absent key prints as checked.
- **AC6** — When a probe runs `--experiment` over a manifest reading the cases and results at
  `5f8ef021d`, the held-out file, `judge.verdicts` `judge2`, and `union` tuning `m1cA@medium
  t1r@medium` and held-out `m1c@medium t1r@medium`, it prints `system tuning 21/23`, `system held-out
  12/12` and `system pooled 33/35`, equal to what `system.py system` prints over the same blobs in the
  same probe.
  Red when: the union counts a case only one arm was judged on as a miss, or the held-out cases stay
  outside the pooled figure.
  figure: DERIVED, `system.py`'s own output in the same probe; the literals are PINNED at `5f8ef021d`.
- **AC7** — When a probe walks every tracked `*.py` under `tools/` with `ast`, `check_experiment`
  and the five rule functions of §4's inventory are defined in the factory `replay_scorer.py` and
  nowhere else, and calling `replay_scorer.run_selftest()` prints a count line naming its declared
  total.
  Red when: a rule lands in a second module.

## 7. Gates

`review-replay selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC1 AC2 AC3 AC4 AC5 AC6 · the factory at `TOOL-dFairHearing-12`'s commit, which reads no manifest; then planted manifests breaking each rule in turn · none

## 8. Open questions

- **F1 — How is "one variable per arm" observable?** (a) Arms declare `settings` and the factory
  diffs each against its base. (b) Inferred from arm names such as `m1b@medium`. (b) reads a naming
  habit, and aScoutedSeam's own names do not follow one (`m1cA@medium`, `t1r@medium`). Both survive
  the vetoes; (a) checks every declared arm. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — What does "frozen before any tuning" refuse?** (a) A held-out file with more than one
  commit, or ids shared with the tuning set; the "never read" half recorded. (b) Also any commit to a
  prompt source after the freeze. (b) refuses aScoutedSeam's own experiment, whose `system.py` changed
  after the freeze (§4 Evidence), failing AC6 (veto 1). Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — With no committed label key, is the judge rule refused or recorded?** (a) Recorded, with
  its reason printed; checked whenever a key is named. (b) Refused. (b) refuses every past experiment,
  aScoutedSeam's included, since no key was ever committed (§4 Evidence), failing AC6 (veto 1).
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none ·
  relaxes: none
- **F4 — Where does an experiment declare its arms?** (a) A committed JSON manifest beside its raw
  outputs, read through `read_raw_output`. (b) CLI flags. §4 Alternatives says why (a). Both survive
  the vetoes; (a) serves every rule from one record. Recommendation (a). Rung 3. RESOLVED (agent,
  2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-21 and TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "check an experiment held out set frozen one
variable per arm blind judge labels rotated"` ranked generic name stems (`check`, `arm`, `frozen` in
`check-unattended.test.sh`), none an experiment rule. No existing seam fits outside the factory
`TOOL-dFairHearing-12` builds, `tools/workflows/replay_scorer.py`, which this unit extends in place;
the union rule is ported from aScoutedSeam's `system.py` (`run_system`, :315-331) and the label key's
shape from `bench.py`'s `cmd_judge_packets` (:573-607), both read, neither edited. The recall query
returned the night pass two's point 2 and its instruments, which state the method in the clause's own
words, and `PLAY-aMendedFleet-2`, the rule that instruments and result rows are committed beside
their record, which F4 follows. `TOOL-aWeighedCompass-19`'s `union.py` scores retrieval ensembles
live, not committed arms, so it is not this union.

Recall terms used: `python tools/memory-recall/query.py "how must a benchmark experiment be run held
out set blind judge one variable" --terms "held-out frozen tuning blind judge rotated labels one
variable per arm parsed replies union aScoutedSeam experiment shape"`
