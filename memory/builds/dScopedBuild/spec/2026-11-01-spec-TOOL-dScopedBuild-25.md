# TOOL-dScopedBuild-25 — unit 4's `review.build.when` read spelled `policy.py get`, so the reader-coverage arm counts it

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 15 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-28 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, report item **H1**. `TOOL-dScopedBuild-4` S7 spells its read
`"$py" "$ROOT/$cli" get review.build.when`. The policy kit's `.sh` reader shape needs the literal
`policy.py` immediately before `get` (`tools/policy/check_policy.py:433-434`), so that line yields no
key, and unit 4 AC8 only greps for the text `get review.build.when`, which the line passes anyway.
Once every unit is terminal the reader-coverage arm reds an owned key with no counted reader, at the
build's close.

This unit spells both of unit 4's policy reads in the counted shape and replaces AC8's text grep with
the arm's own reader. It repairs `TOOL-dScopedBuild-4` and builds one step after it (order 15).

## 2. Scope (IN)

- **S1** — The kit directory, not the file. `resolve_policy_cli` (unit 4 S7, in
  `tools/unattended/lib-unattended.sh`) prints the policy kit's DIRECTORY, repo-relative, `.` at a
  root install, as `resolve_kit_dir` prints it (`lib-unattended.sh:131-132`), and exits 1 with
  nothing printed where the kit does not resolve. Observed by AC2.
- **S2** — The two reads, spelled with the file name before `get`. Unit 4 S7's read is
  `"$py" "$ROOT/$_pk/policy.py" get review.build.when` and unit 4 S8's is
  `"$py" "$ROOT/$_pk/policy.py" get decisions.major`, `$_pk` S1's answer, each key a literal at the
  call and each call on a line that does not open `#`. This supersedes unit 4 S7's
  `"$py" "$ROOT/$cli" get review.build.when`; unit 4's outcomes per value are unchanged. Observed by
  AC1 and AC2.
- **S3** — Unit 4 AC8's third clause, `git grep -c 'get review.build.when' --
  tools/unattended/unattended.sh` prints at least 1, is superseded by AC1, which asks the arm that
  grades the key. AC8's first two clauses stand. Unit 4's acceptance ledger answers its AC8 with a
  note naming `TOOL-dScopedBuild-25 S3`. Observed by AC1.

## 3. Non-goals (OUT)

- What a refused `get` or an out-of-set value does to the exit. That is id 48 of the same audit, a
  MEDIUM, and `TOOL-dScopedBuild-35` S30 grades it over the spelling S2 gives.
- The left-shift gate the report names, a spec-lint rule that every criterion certifying a policy-key
  reader asserts `scan_reader_keys`. No clause of this build names it.
- Rewording unit 4's spec text. Each clause is superseded by name and answered in its ledger.
- A new reader shape in `tools/policy/check_policy.py`. The read moves to the shape the arm counts.

### Edges

- **consumes-from** `TOOL-dScopedBuild-4` — S7's `resolve_policy_cli` and its `review.build.when` read, S8's `decisions.major` read, and AC8's grep clause, which S1 to S3 respell and supersede (id 1)
- **hands-off** `TOOL-dScopedBuild-35` — the two reads S2 spells, whose refused `get` and out-of-set value that unit's S30 makes a refusal of the exit (id 48)

## 4. Design

### Evidence

- `READER_SHAPES` in `tools/policy/check_policy.py:423-435`: the `.sh` row matches
  `policy\.py["']?[ \t]+get[ \t]+<key>`, so the file name must be spelled on the line, directly
  before `get`. A path held whole in a variable, `"$ROOT/$cli"`, matches nothing.
- `scan_reader_keys(repo)` (`:479`) reads every tracked code file outside the memory root and `help/`,
  skips `*.test.sh` and lines opening `#` or `//`, and returns the set of keys spelled. Unit 3 AC7 and
  unit 8 AC1 already observe their keys through it.
- `resolve_index_generator` (`tools/unattended/lib-unattended.sh:188-198`) is the model unit 4 S7
  cites; it prints `<dir>/gen_build_index.py`, or the bare file name at a root install, so a caller
  holding its answer whole spells no file name. S1 prints the directory so that S2 can.

### The read, after this unit

```
_pk=$(resolve_policy_cli) || { echo "review.build.when: per-build — the policy kit is not installed"; ... }
_when=$("$py" "$ROOT/$_pk/policy.py" get review.build.when)      # counted by READER_SHAPES' .sh row
_major=$("$py" "$ROOT/$_pk/policy.py" get decisions.major)
```

### Inventory

Minted: nothing. `resolve_policy_cli` is unit 4's; S1 fixes what it prints. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 15, one step after unit 4 (order 14), so its reads are respelled before the close
runs the policy check.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Spell `"$ROOT/${cli%/*}/policy.py"`.** At a root install `resolve_policy_cli` would print the
  bare file name, `${cli%/*}` keeps it whole, and the path doubles the file name. S1's directory
  answer has no such case.
- **Add a reader shape for `"$ROOT/$cli" get`.** It widens the arm to count any variable followed by
  `get`, a reader of keys the arm cannot see are policy keys; the read moves to the shape instead.

## 5. Production-readiness checklist

- security — no new write path; the reads are unit 4's, at the landed revision.
- perf / scale — unchanged: the same two `get` calls.
- error / empty / loading states — S1's exit 1 keeps unit 4's not-installed line.
- observability — unchanged lines; the coverage arm now sees the key.
- risks — a builder who keeps the path in one variable passes a text grep and fails AC1, which is
  why AC1 asks the arm.
- testing — AC1 by probe over the built tree, AC2 by a sliced function in the driver suite.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy;
  k = check_policy.scan_reader_keys('.'); print('review.build.when' in k, 'decisions.major' in k)"`
  runs on the built tree, it prints `True True`.
  Red when: a read keeps the path whole in a variable, or a comment line carries the only spelling.
  figure: DERIVED at observation; at base `f4597719` it prints `False` for `review.build.when`.
- **AC2** — When `resolve_policy_cli` is sliced from `lib-unattended.sh` and run in a fixture whose
  policy kit sits at the root, it prints `.`, and `"$py" "$ROOT/./policy.py" get review.build.when`
  built from it prints `per-build` with no policy file; with no kit it exits 1 printing nothing.
  Red when: the answer is a file path, or a root install joins to a path that does not exist.
  fixture: the driver suite's slug fixture with the policy kit copied to its root.

## 7. Gates

`unattended kit gate` · `routed-commits selftest` · `policy check` · `policy fixtures` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 · reader coverage over `review.build.when` once dScopedBuild lands, staged by respelling the read `"$ROOT/$cli" get` · none

New arm: tools/unattended/unattended.test.sh · covers AC2 · the sliced `resolve_policy_cli` over a root-installed kit and a missing one, staged by printing the file path · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause.
  (b) splits cl-dClosedLoop-0402, which unit 4 carries whole, and the packet's coverage would read a
  second carrier. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the precedent
  `TOOL-dWitnessedBar-91` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 1
  (HIGH, item H1).

## 10. Reuse audit

The seam is the reader-coverage arm's own `.sh` shape (`tools/policy/check_policy.py:433-434`) and
`resolve_kit_dir` (`tools/unattended/lib-unattended.sh:132`), whose directory answer S1 keeps.
`python tools/codebase-map/reuse_lookup.py "read a policy key from a shell script in the shape the
reader coverage arm counts"` ranked `read`, `read_text`, `key`, `counts` and `keys`, name-token hits
and none a shell policy reader, so no existing seam fits beyond the shape and the resolver named
above. The recall probe surfaced TOOL-dPlacedRequest-73 and TOOL-dRankedPlan-7, which met the same
shape for `read_card_policy`; this unit moves the read to the shape rather than adding a row.

Recall terms used: `python tools/memory-recall/query.py "how is a policy key read so the reader coverage arm counts it" --terms "policy.py get reader coverage READER_SHAPES scan_reader_keys literal key shell python call"`
