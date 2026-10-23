# TOOL-dGroundRules-19 — the guard admits a regenerated mirror equal to its render, so an agent branch that edits the catalogue reaches a green bar

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-19-deviation-7.md](../build/2026-10-23-build-TOOL-dGroundRules-19-deviation-7.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 TOOL-dGroundRules-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 32 at HIGH**, item **H4**, which no other id shares. This unit is its
promotion. It repairs `TOOL-dGroundRules-6` and builds at order 4, one step after that unit.

A catalogue or policy edit on a branch stales the mirror. The bar's preflight then exits 2 and
prescribes `--regen` and a commit of what moved (`tools/run-gates/run-gates.sh:1449-1458`), and
`TOOL-dGroundRules-6` refuses an agent's commit of `.governance/policy.json` "even when it equals the
render". With the preflight skipped, `arm_mirror_parity` still reds. So every later build that adds
catalogue rows has no path to a green bar without the owner's terminal. This unit lets the guard
admit one more agent shape: a staged mirror whose bytes equal the render at HEAD, when nothing the
render reads is staged beside it.

## 2. Scope (IN)

- **S1** — The mirror shape. In `tools/policy/guard.py --staged`, after the parent rule and before
  the raise shape, `.governance/policy.json` leaves the touched set when both hold: the staged blobs
  of `.governance/policy.toml` and of the kit's `catalogue.toml` equal their blobs at HEAD, each
  absent on both sides counting as equal; and the staged mirror's bytes equal the stdout of
  `<python> <kit>/policy.py mirror --print`, the render at HEAD. Observed by AC1, AC2, AC3.
- **S2** — The render to stdout. `policy.py mirror --print` writes `render_mirror(repo, "HEAD")`'s
  bytes to stdout and writes no file; a refusal exits 2 as `mirror --write` does. Observed by AC1.
- **S3** — Each outcome named. An admitted mirror prints
  `policy-guard: admitted · .governance/policy.json · equals its render at HEAD`. A mirror staged
  beside a staged policy file or catalogue is refused with
  `the mirror renders HEAD: commit the policy file or catalogue first, then regenerate`; one that
  differs from the render is refused with `differs from its render at HEAD`, and its remedy line
  names `git restore --staged --worktree .governance/policy.json`, as today. Observed by AC2, AC3.
- **S4** — The cases `guard-mirror-render`, `guard-mirror-beside-catalogue` and
  `guard-mirror-branch-green` in `CASES` of `tools/policy/check_policy.py`. Observed by AC1 to AC4.
- **S5** — `help/policy.md`'s section "Who may change the policy file" gains the mirror shape and the
  two-commit order. Observed by AC5.

## 3. Non-goals (OUT)

- Grading the mirror only on the landing range, or untracking it on branches, the review's other two
  options (§8 F1).
- Any change to the raise shape, to the guarded paths, or to the owner's terminal proof.
- Rendering at the index. The render reads a revision (`TOOL-dGroundRules-5` §8 F3); requiring the
  render's inputs to equal HEAD's is what lets HEAD stand for the commit being made.

### Edges

- **consumes-from** `TOOL-dGroundRules-6` — `guard.py --staged`, its verdict order, its refusal and remedy lines, the hook block and the `guard-` cases, which this unit extends
- **consumes-from** `TOOL-dGroundRules-5` — `render_mirror`, the `mirror` verb that gains `--print`, and `mirror --check`
- **consumes-from** `TOOL-dGroundRules-65` — a render whose bytes do not name the commit that carries them; without it the admitted mirror is stale at its own commit
- **hands-off** `TOOL-dGroundRules-25` — the guard's mirror shape and `mirror --print`, whose recorded input set and byte write that unit pins (findings 7, 25, 42, 24)

## 4. Design

### Evidence

- `TOOL-dGroundRules-6` §4 "The verdict": "An agent's commit of `.governance/policy.json` is refused
  even when it equals the render", and its §8 F6 resolved that refusal on the clause's list of
  refused paths; its Alternatives rejected the render's admission only for the dependency on
  `TOOL-dGroundRules-5`, "which builds beside it". This unit builds after both.
- `TOOL-dGroundRules-5` §5 risks: "A branch carrying a policy change carries a stale mirror until it
  lands, so a bar run on that branch before its landing reds the parity arm".
- The preflight prescribes `bash $KITREL/run-gates.sh --regen`, "then commit what it moved"
  (`tools/run-gates/run-gates.sh:1456-1457`).
- `TOOL-dGroundRules-6` AC10 holds that the guard never imports the reader nor calls `resolve(`; a
  subprocess render keeps both greps empty.

### The order after this unit

1. The list, 2. the touched set, 3. the parent rule: unchanged.
4. **The mirror shape**: when `.governance/policy.json` is touched, compare
   `git rev-parse :<p>` with `git rev-parse HEAD:<p>` for the policy file and `<kit>/catalogue.toml`;
   on equality run `mirror --print` with the guard's own interpreter and compare its stdout with
   `git cat-file blob :.governance/policy.json`. Equal: the mirror leaves the set. An emptied set
   exits 0 with the admitted line.
5. The raise shape, 6. the record, 7. the verdict: unchanged, over what remains.

So the agent's path is two commits: the catalogue or policy change, then the regenerated mirror.
After `TOOL-dGroundRules-65` the render at HEAD equals the render at the commit that carries it,
because the inputs are equal and the reasons name no commit, so `mirror --check` and the preflight
are green there.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_mirror_render` | py.function | `tools/policy/guard.py` |
| `mirror --print` | CLI flag | `tools/policy/policy.py` |
| `guard-mirror-render`, `guard-mirror-beside-catalogue`, `guard-mirror-branch-green` | `CASES` entries | `tools/policy/check_policy.py` |

`check_mirror_render` leads with `check`: `lexicon.py --suggest` answered OK for it under
`py.function` on 2026-10-23.

### Files touched (estimate)

- `tools/policy/guard.py`
- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `help/policy.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Grade the mirror's `[[generated]]` row only on the landing range.** §8 F1.
- **Untrack the mirror on branches.** §8 F1.

## 5. Production-readiness checklist

- security — the admitted mirror is byte-equal to what the landing would render from inputs equal
  to HEAD's, so an agent can commit no value the reader would not answer; a hand-edited mirror still
  differs and is refused. The guard still reads neither `policy-file.guard` nor `policy-file.proof`.
- perf / scale — a commit staging the mirror adds one Python spawn rendering about 270 keys.
- error / empty / loading states — a render refusal leaves the mirror in the set, so the commit is
  refused and the render's line is printed.
- observability — each outcome is named on its own line, with the two-commit remedy.
- risks — the render cost on a slow node lands on the commit that stages the mirror only.
- testing — the three cases under `--fixture`, with AC1 to AC5.
- migration — none.
- user docs — `help/policy.md`, S5.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py`, `guard.py` and `policy.py`, and the help page as `policy.md` under `help/`, as
`TOOL-dGroundRules-6` §6 does.

- **AC1** — When `python check_policy.py --fixture guard-mirror-render` runs, which commits a
  catalogue row, regenerates the mirror and stages it alone, `guard.py --staged` exits 0 printing
  `equals its render at HEAD`.
  Red when: the guard refuses a mirror byte-equal to its render.
- **AC2** — When `--fixture guard-mirror-beside-catalogue` runs, which stages the catalogue row and
  the mirror rendered over the working tree together, `guard.py --staged` exits 1 printing
  `commit the policy file or catalogue first`.
  Red when: a mirror whose render inputs are staged beside it is admitted.
- **AC3** — When `TOOL-dGroundRules-6`'s `guard-other-paths` plant rewrites the mirror by hand and
  `guard.py --staged` runs, it exits 1 printing `differs from its render at HEAD`.
  Red when: a hand-edited mirror is admitted.
- **AC4** — When `--fixture guard-mirror-branch-green` runs, which commits a catalogue row on a
  branch, runs `policy.py mirror --write`, commits the mirror through `guard.py --staged`, then runs
  `policy.py mirror --check` at the new HEAD, the guard exits 0 and the check exits 0.
  Red when: an agent branch carrying a catalogue edit cannot reach a fresh mirror without the
  owner's terminal.
- **AC5** — When `grep -n "regenerate"` runs over `policy.md` under `help/`, it prints a line of the
  section "Who may change the policy file" naming the mirror.
  Red when: the page still says every agent change to the mirror is refused.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture guard-mirror-render guard-mirror-beside-catalogue guard-mirror-branch-green`) · covers AC1 AC2 AC4 · the mirror shape staged to skip the input-equality check, then staged out of the verdict · none

## 8. Open questions

- **F1 — How does an agent branch that edits the catalogue reach a green bar?** (a) The guard admits
  a staged mirror equal to its render at HEAD when the render's inputs equal HEAD's. (b) The
  mirror's `[[generated]]` row is graded only on the landing range, through a new `regen.py` flag.
  (c) The mirror is not tracked on branches. (b) changes the run-gates kit's preflight contract and
  leaves `arm_mirror_parity` red on the branch, so it fails AC4 (veto 1) and adds a flag to another
  kit (veto 2). (c) contradicts `TOOL-dGroundRules-5`'s committed mirror and its AC1 (veto 1).
  Recommendation (a), which supersedes `TOOL-dGroundRules-6` §8 F6's pick for the case that unit
  could not price, once its dependency has built. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). grants: PLAY-dClosedLoop-3 the guard's second agent
  shape over the mirror `cl-dClosedLoop-0012` guards · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 32 (HIGH, item H4) of the round-1 spec
  audit, from the review's option (a) and specs 5 and 6 read at their audited revisions.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-25`, the reciprocal of each
  promotion of the round-1 spec audit of units 13 to 21 that repairs this unit; no scope moved.
- rev-3 · 2026-10-23 · §3 §4 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-6`'s verdict order in `guard.py`, which gains a step rather
than a second guard, and `TOOL-dGroundRules-5`'s `render_mirror`, reached through the `mirror` verb so
the guard imports no reader. `python tools/codebase-map/reuse_lookup.py "admit a staged generated file
equal to its render in a pre-commit guard"` ranked name stems only (`pre`, `render`, `build_commit`,
`render_cards_md`), none of which judges a staged file, so no other seam fits. The recall probe
returned spec 5's header and F6, spec 6's design, the spec brief and this build's review, which agree
with what this unit changes; `TOOL-aTrimmedHook-8` concerns a hook's trim and does not bear on it.

Recall terms used: `python tools/memory-recall/query.py "how may an agent commit a regenerated mirror
past the policy guard" --terms "policy guard mirror regenerated agent commit refused render staged
pre-commit regen preflight"`
