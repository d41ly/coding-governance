# TOOL-aMendedFleet-40 — the coverage gate refuses a `baseline.toml` that gained a key against its base

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 40 · closes TOOL-aHoistedPass-30 · advances TOOL-aProbedToolkit-8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`baseline.toml` is the map's backfill of keys no dossier claims yet, and every document describing it
says it only shrinks. Nothing enforces that: `compute_coverage` grades the baseline against the live
inventories and the claims, never against its own earlier self, so a new key appended to the baseline
passes the gate exactly as a claim would. The file's own header says so, and one rename already went
through it. This unit makes the codebase-map coverage gate compare the working baseline with the
baseline at the branch's base and red on any key the base did not carry, so the shrink-only rule is a
constraint rather than a convention.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_lib.py` gains `resolve_compare_base(root)`, which returns the sha
  the comparison reads and the reason, or no sha and the reason none resolves. The rule is the merge
  bar's own: the default branch named by `refs/remotes/origin/HEAD`, its merge-base with `HEAD` when
  that is a proper ancestor of `HEAD`, else the remote tip itself. It fetches nothing. Observed by
  AC1 and AC3.
- **S2** — `map_lib.py` gains `derive_baseline_additions(root, base)`, which reads the baseline at
  `base` with `git show`, parses it with `tomllib`, and returns, per inventory id of the working
  baseline, the keys the base did not carry. An inventory id absent at the base counts every key as
  added, so a new inventory cannot open with a baselined key. A baseline absent at the base returns
  no comparison rather than an empty one. Every subprocess call names `encoding="utf-8"`. Observed by
  AC2 and AC4.
- **S3** — `test_baseline_never_gains_a_key` joins `tools/codebase-map/test_codebase_map.template.py`
  and its byte-identical instance `tools/codebase-map/test_codebase_map.py`, and the standalone
  runner's list. It always prints one line naming the base it compared against and how many keys
  each side carried. With no resolvable base, or no baseline at the base, it prints `UNGRADED` and
  the reason, the shape `test_dossier_decisions_are_declining` already uses, and passes. Otherwise it
  asserts no addition, and its failure names each added key as `<inventory>: <key>` with the remedy:
  claim the key in a dossier or `FOUNDATION.md`. Observed by AC1, AC2 and AC3.
- **S4** — The prose follows the mechanism. The gate docstring's remedy line, the header of
  `render_baseline` and of `memory/map/baseline.toml`, and the kit README sentence calling the rule
  socially enforced each say the gate refuses an addition against the base. The baseline header's
  2026-08-16 exception paragraph stays as a record and loses the sentence saying nothing enforces the
  rule. The `codebase-map` dossier's baseline paragraph is refreshed. Observed by AC5.
  **Readers:** by name: `memory/map/baseline.toml`, `tools/codebase-map/README.md`,
  `tools/codebase-map/map_lib.py` and `memory/map/features/codebase-map.md` carry the sentence that
  goes.
  by value: NO VALUE READERS — the sentence is prose and no program parses it.
- **S5** — A kit selftest arm builds a fixture repository with a committed baseline, adds a key in the
  working tree, and asserts `derive_baseline_additions` names it, returns nothing for an unchanged
  file, and returns no comparison when the base has no baseline. NOT OBSERVED by a criterion here:
  the arm is a declaration in §7 and runs in the kit selftest at the close, while AC2 and AC4
  observe the same function's two outcomes directly on the real map.

## 3. Non-goals (OUT)

- An escape for a deliberate addition. Every addition has a remedy that is not an addition: claim the
  key in a dossier. §8 F1 records why.
- The digest's coverage figure, the other half of `TOOL-aProbedToolkit-8`; unit 39 §8 hands it to
  `TOOL-aMendedFleet-86`, which closes that ask after this unit lands.
- Gating the affordance grace list the same way. It is shrink-only too, and `map_diff.py
  --drop-affordance-exempt` already rewrites it downward; a growth assert there is its own unit.
- Adopters whose gate was copied before this unit. Their frozen copy lacks the new test until they
  re-copy it; `check_gate_coverage.py` compares artifacts, not tests, and says so.
- The codebase-map kit version bump, owed once at the build's close.

### Edges

- **hands-off** `TOOL-aMendedFleet-86` — the digest's coverage figure; that unit's `closes` on
  `TOOL-aProbedToolkit-8` rests on this unit's shrink assert having landed.
- **hands-off** external — the codebase-map kit version bump, owed once at the close.

## 4. Design

### Evidence

- `compute_coverage` in `tools/codebase-map/map_lib.py` carries four set asserts: unclaimed,
  stale claims, stale baseline and lazy baseline. None reads an earlier baseline. Read at base
  `7af5f564`.
- `memory/map/baseline.toml` states in its header that nothing enforces the rule, beside the
  2026-08-16 rename `TOOL-aSiftedPlaybook-1` took through it.
- `tools/run-gates/run-gates.sh` derives its base as the merge-base with the remote default branch
  when that is a proper ancestor of `HEAD`, else the remote tip; S1 copies that rule because this kit
  may not read a sibling kit.

### Flow

On the default branch before a push, `HEAD` is ahead of the remote tip and the merge-base IS the
remote tip, so the comparison covers every pushed commit. On a feature branch it is the branch point,
so a key `main` deleted after the branch opened is not misread as one the branch added. On the
remote CI job after landing, `HEAD` equals the tip, the comparison is the committed baseline against
itself, and the printed line says so. A clone with no `origin` prints `UNGRADED`.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `resolve_compare_base` | function in `map_lib.py` | `py.function`; `--suggest` answered OK |
| `derive_baseline_additions` | function in `map_lib.py` | `py.function`; `--suggest` answered OK |
| `test_baseline_never_gains_a_key` | gate test function | `py.function`; `--suggest` answered OK |

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/test_codebase_map.template.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `memory/map/baseline.toml`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- **A drift-audit signal over the file.** drift-audit already resolves a base ref, but its signals
  are report-only here and the shrink-only lists it watches are counted by lines, not keys; the rule
  belongs in the gate that already owns the baseline's four other asserts.
- **Comparing against the remote tip, as drift-audit does.** On a long-lived branch the tip may have
  deleted keys the branch still carries, which reads as the branch adding them.
- **Comparing key counts.** A rename keeps the count and adds a key, which is the one case this
  repo has on record.

## 5. Production-readiness checklist

- security — N/A — a read of a committed file at a sha the repository already holds.
- perf / scale — two `git` calls inside a leg whose ceiling is 300 seconds.
- error / empty / loading states — no `origin`, a shallow clone, a base with no baseline and an
  unparseable base baseline each print `UNGRADED` with the reason; a parse error in the WORKING
  baseline still raises through `load_map_tree` as today.
- observability — the gate prints the base sha and both key counts on every run, so a comparison
  that compared nothing is visible as such.
- risks — a branch cut before a key was claimed elsewhere and rebased later: the merge-base moves with
  the rebase, so the comparison stays the branch's own change.
- testing — S5's fixture arm at the close; AC2 to AC4 stage each outcome in a scratch clone.
- migration — N/A — the baseline only loses keys from here on.
- user docs — the kit README and the gate's docstring, per S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/test_codebase_map.py` runs at the worktree root after the
  unit's commit, it exits 0, prints `ok   test_baseline_never_gains_a_key`, and prints the base sha it
  compared against.
  Red when: the test is missing from the standalone runner, or it compared nothing without saying so.
- **AC2** — When a scratch clone under the TEMP root moves the claim `codebase-map kit selftest` out of
  the `codebase-map` dossier's `gate-legs` list and into the `gate-legs` list of
  `memory/map/baseline.toml`, `python tools/codebase-map/test_codebase_map.py` in it exits 1 naming
  `gate-legs: codebase-map kit selftest`, and every other test in that run passes.
  Red when: the gate passes, because the move keeps the four existing asserts clean.
- **AC3** — When the same scratch clone runs with its `origin` remote removed, `python
  tools/codebase-map/test_codebase_map.py` prints `UNGRADED` beside the new test's name and exits 0.
  Red when: an unresolvable base fails the gate or passes it silently.
- **AC4** — When the same scratch clone resets its remote-tracking default branch to the parent of
  the commit that added `memory/map/baseline.toml`, as `git log --diff-filter=A` names it, `python
  tools/codebase-map/test_codebase_map.py` prints `UNGRADED` beside the new test's name with a reason
  naming the absent baseline, and exits 0.
  Red when: a base with no baseline is read as an empty one, and every key reads as added.
- **AC5** — When `git grep -n -i -e "nothing enforces" -e "socially enforced" -- memory/map
  tools/codebase-map` runs after the unit's commit, it prints nothing.
  Red when: a document still says the rule is unenforced.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `kit epoch (shipped bytes move, the version moves)` · `encoding posture (text IO names its encoding)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · a fixture repository whose working baseline gains a key over its committed one, staged red by making `derive_baseline_additions` return an empty mapping · none

## 8. Open questions

- **F1 — Does the gate admit a deliberate addition?**
  Options: no escape; a comment line in the baseline naming the key and a decision id; an environment
  override. The one addition on record was a rename the owner took because no remedy existed, and
  today a dossier claim is that remedy for every key.
  RESOLVED (agent, 2026-10-04, delegated): no escape. It satisfies every criterion with the smallest
  surface, and an override would be the second channel this repo removes wherever it finds one.
- **F2 — Against which base?**
  Options: the remote tip; the merge-base; an explicit environment value.
  RESOLVED (agent, 2026-10-04, delegated): the merge bar's rule, merge-base when it is a proper
  ancestor and the remote tip otherwise, so this gate and the runner's guards agree on what a branch
  changed.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#49], `compute_coverage`, the
  runner's base rule and the baseline header at base.
- rev-2 · 2026-10-04 · §3 · the M2 cross-read: the digest-figure Non-goal said only that unit 39
  hands it on, while `TOOL-aMendedFleet-86` holds it and declares a consumes-from on this unit; the
  Non-goal and Edges now name it.

## 10. Reuse audit

The seams extended are `parse_baseline` and `compute_coverage` in `tools/codebase-map/map_lib.py`
and the `UNGRADED` reporting shape of `test_dossier_decisions_are_declining` in the gate template.
`python tools/codebase-map/reuse_lookup.py "compare a registry file against its copy at the base ref
and refuse an added entry"` returned name-stem neighbours, the process-monitor refusal classes and
`corpus_files` among them, none of which reads a file at a ref; the probe printed `unscanned layers:
.sh`, and the shell seam it cannot see is the runner's base derivation, which S1 copies by rule
because a kit may not read a sibling kit. `ratchet_findings` in `tools/drift-audit/drift_report.py`
reads a file at a base ref, but compares one scalar and sits in another kit. The recall probe
returned `TOOL-aHoistedPass-30`, which this closes, the baseline half of `TOOL-aProbedToolkit-8`, and
the record of the 2026-08-16 rename. Where the report and the tree disagree: nowhere; the four asserts
and the header sentence are unchanged at base.

Recall terms used: `python tools/memory-recall/query.py "how is the codebase-map baseline kept
shrink-only and was a key ever added to it" --terms "baseline.toml shrink-only ratchet backfill
compute_coverage lazy baseline stale baseline seed-baseline aSiftedPlaybook rename exception base ref"`
