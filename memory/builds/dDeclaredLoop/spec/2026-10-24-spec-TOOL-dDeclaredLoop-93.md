# TOOL-dDeclaredLoop-93 — 92 AC16 states the push-merge-tree-fatal plant's exit as 1, the code every sibling states

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 47 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-93-deviation-931.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-93-deviation-931.md) | deviation | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-94 |

<!-- /gen:spec-records -->

## 1. Goal

The round-10 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**. The grounding lens found the same contradiction as
id 11, kept at MEDIUM as item M9; that id is a scope item of `TOOL-dDeclaredLoop-94`, the round's minors
batch, and is not this unit's.

`TOOL-dDeclaredLoop-92` AC16 gives the `push-merge-tree-fatal` plant of `guard.py --fixture` an exit
code of 0. 81 AC3, 83 S2, 88 S18 and 88 AC18 give it 1, its refusal verdict. No build satisfies both, and
a builder who makes AC16 pass flips the refusal that the other four observe.

This unit restates AC16 to exit 1, keeps the built plant at exit 1, and proves the agreement with a probe
that collects every exit code the build's specs state for that command. It builds immediately after 92
and repairs `TOOL-dDeclaredLoop-92`.

## 2. Scope (IN)

- **S1** — 92 AC16 reads: `python guard.py --fixture --plant push-merge-tree-fatal` exits 1, as 81 AC3
  states, and its `OSError()` row prints `the clean re-merge failed: start failed: OSError`. The words
  `exits 0` leave AC16, in this unit's rev bump of 92 with its §9 line. Observed by AC1.
- **S2** — The built plant exits 1. `python guard.py --fixture --plant push-merge-tree-fatal` in
  `tools/loop/` exits 1 and prints both `the clean re-merge failed: 128`, 81 AC3's row, and
  `the clean re-merge failed: start failed: OSError`, 92 S17's row. Where 92's pass left the plant
  exiting 0 to meet the old AC16, this pass restores exit 1 in `tools/loop/guard.py`. Where the plant
  already exits 1, nothing in the code moves. Observed by AC2.
- **S3** — Every exit code that a spec of this build states for that command is 1. The claim population
  is the probe in §4 "The exit-claim probe", run over `memory/builds/dDeclaredLoop/spec/`. Observed by
  AC3.

## 3. Non-goals (OUT)

- Id 11, the same defect at MEDIUM: `TOOL-dDeclaredLoop-94` names 88 S18 and AC18 in 92 S17.
- The report's left-shift gate, a `tools/check-spec-tokens.py` join that fails when one command carries
  two exit codes across a build's specs. That is a second mechanism in a governance tool outside the
  loop kit (BUILD-METHOD M2). The class is recorded at the close, and AC3 is this instance's probe.
- AC16's other halves: the `build_failure_detail` arguments and the multi-line detail (ids 13 and 29) are
  `TOOL-dDeclaredLoop-94`'s.
- The plant's other rows, the rc-128 and rc -9 rows that 81 and 88 own. This unit reads the rc-128 line
  and changes neither.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-92` — AC16 and the `OSError()` row of the `push-merge-tree-fatal` plant that S17 builds, which S1 restates to exit 1 (the round-10 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-94` — 92 AC16 as S1 restates it, whose `build_failure_detail` calls and range greps that unit completes (the round-10 spec audit's ids 4, 11, 13, 20, 29)
- **hands-off** `TOOL-dDeclaredLoop-96` — §4's exit-claim probe, AC1 and AC3, which that unit restates (the round-11 spec audit's ids 3, 4, 12)

## 4. Design

### Evidence

Read or probed 2026-10-24 at the worktree tip on node `d`: PINNED, that date.

- 92 AC16 says the plant `exits 0` (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md`,
  §6 AC16).
- 81 AC3 says `--plant push-merge-tree-fatal` exits 1 printing `the clean re-merge failed: 128`. 83 S2
  says it still exits 1. 88 S18 and 88 AC18 say it exits 1. 88 AC7 gives exit 0 to the bare
  `guard.py --fixture` with no plant, the convention that a named guard plant exits 1 on its refusal.
- 86 AC22 and 90 AC21 observe the plant's `OSError` row and name no exit code.
- `tools/loop/` is absent at base, so `guard.py` and its plant are sibling-minted, by 81 and 88.
- The probe below, run over the spec folder with this spec in it, found nine claims: one each in 81, 83
  and 92, two in 88 and four in this spec, each of this spec's stating 1. It printed the set `{0, 1}`, the
  0 being 92 AC16's.

### The exit-claim probe

```
claim = re.compile(r"--plant push-merge-tree-fatal`((?:(?!--plant|\. |; ).){0,60}?)\bexits (\d+)")
for each *.md under memory/builds/dDeclaredLoop/spec/:
    text = the file with every whitespace run squeezed to one space
    collect m.group(2) for every claim.finditer(text)
print the number of claims and the set of codes
```

The plant name must be followed by its closing backtick, so `push-merge-tree-fatal-unparseable-parent`
is not counted. A claim ends at a sentence end or at a second `--plant`, so the `exits 0` of 88 AC7's
bare run is not counted.

### Write set

This pass writes the 92 spec as a rev bump with its §9 line, and `tools/loop/guard.py` only where S2
finds the plant exiting 0. The build README's regions are the generator's render. The pass mints no
public module-level `def`, so `memory/map/generated/symbols.json` does not move.

### Files touched (estimate)

- `tools/loop/guard.py`
- `memory/builds/dDeclaredLoop/spec/`
- `memory/builds/dDeclaredLoop/README.md`

### Alternatives rejected

- **Naming no exit code in AC16, as 86 AC22 and 90 AC21 do (the report's other option).** The exit code is
  the plant's refusal verdict. Leaving it out of AC16 drops an observation without removing the defect
  class. Stating 1 satisfies every criterion that the omission would, and AC3 observes it.
- **Flipping 81 AC3, 83 S2 and 88 S18 and AC18 to exit 0.** A refusing plant that exits 0 reads as a pass to
  the `loop guard fixtures` leg, and four criteria would move to agree with one wrong one.

## 5. Production-readiness checklist

- security — keeps the plant's refusal visible as a non-zero exit, so a merge the guard refuses is never
  read as clean.
- perf / scale — none: one spec line, and a probe of one folder.
- error / empty / loading states — the `OSError()` row keeps 92 S17's non-empty detail.
- observability — the plant's refusal lines are unchanged; only the stated exit code moves.
- risks — `TOOL-dDeclaredLoop-94` rewrites AC16 again after this unit. Its items keep exit 1, and AC3 re-runs
  at its pass.
- testing — AC1 to AC3 as a grep, a plant run and a probe over the spec folder.
- migration — none: `tools/loop/` is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `awk '/^- \*\*AC16\*\*/,/^## 7/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md` is piped to
  `grep -c "exits 0"`, it prints 0. Piped to `grep -c "exits 1"`, it prints at least 1.
  Red when: AC16 still requires exit 0 from a plant four siblings require to exit 1.
  figure: the first grep prints 1 and the second 0 at HEAD, PINNED 2026-10-24.
- **AC2** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs in `tools/loop/`, it exits 1,
  and its output holds `the clean re-merge failed: 128` and
  `the clean re-merge failed: start failed: OSError`.
  Red when: the plant was flipped to exit 0 to satisfy the old AC16, staged by setting its exit to 0.
- **AC3** — When a `python -c` probe runs §4's exit-claim pattern over every `*.md` under
  `memory/builds/dDeclaredLoop/spec/`, it counts at least five claims and prints the set `{1}`.
  Red when: any spec of the build states another exit code for the command, staged by restoring
  `exits 0` in a scratch copy of the 92 spec.
  figure: nine claims and the set `{0, 1}` with this spec in the folder, PINNED 2026-10-24. The count
  at observation time is DERIVED from the folder.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The sibling-minted leg this pass keeps green, outside the base manifest and declared by the unit that
mints it: `loop guard fixtures`, which runs `guard.py --fixture`; it is no leg at HEAD. This pass adds and
moves no arm: the plant's exit 1 is 81's arm, and S2 only keeps it.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — State exit 1 in AC16, or name no exit code (id 1)?** (a) exit 1, as 81 AC3 states; (b) the
  `OSError()` row's line alone. The report judged both sound. (a) keeps the refusal verdict observed and
  satisfies every criterion (b) would. RESOLVED (agent, 2026-10-24, delegated): (a), S1.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-10 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 92 AC16 and 81's `push-merge-tree-fatal` plant of `tools/loop/guard.py`, restated and kept in
place. No second plant and no new checker is minted.
`python tools/codebase-map/reuse_lookup.py "collect every exit code a spec states for one command and compare them"`
ranked `read_spec_revisions`, `parse_spec_h1`, `build_spec_path_re` and `resolve_compare_base`, none of which
reads an exit claim from a spec's prose, so no existing seam fits the probe and it stays a criterion's
`python -c` rather than a tool. The memory-recall query returned the round-10 report's H1, 81's AC1 and
92's checklist.

Recall terms used: push-merge-tree-fatal exits AC16 guard plant exit code sibling criteria two-answers-to-one-question refusal convention
