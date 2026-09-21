# TOOL-cMendedVintage-3 — `check-wiring.sh`'s boundary walk can produce the empty prefix it declares legal

**Status:** CLOSED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-TOOL-cMendedVintage-3-acceptance-ledger.md](../build/2026-09-17-build-TOOL-cMendedVintage-3-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-TOOL-cMendedVintage-3-2-build-brief.md](../prompts/2026-09-16-prompt-TOOL-cMendedVintage-3-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12 |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round3.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round3.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-5 DEPL-cMendedVintage-7 DEPL-cMendedVintage-16 DEPL-cMendedVintage-24 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-4 TOOL-cMendedVintage-12 |

<!-- /gen:spec-records -->

## 1. Goal

The `.git` boundary walk at `tools/check-wiring.sh:33-40` appends `basename "$_p"` to `KIT_REL`
BEFORE it tests `[ -e "$_parent/.git" ]`, so `$_p` itself is never tested as the repo root. At a ROOT
install the walk therefore runs past the repository, reaches the filesystem root, and hands every
`${KIT_REL:+…}` rung a prefix assembled out of directories ABOVE the tree. The comment at `:41-42`
says the empty prefix is legal; the derivation cannot produce it. Reorder the two steps so it can.

## 2. Scope (IN)

- **S1** The loop tests `$_p` for `.git` at the TOP of each iteration and appends
  `basename "$_p"` to `KIT_REL` only after that test fails. A root install then breaks on the first
  iteration with `KIT_REL` still empty, which is the state `:43` and its comment already declare
  legal. Observed by AC1.
- **S2** The `tools/` install and every deeper install keep the value they have today. The walk
  accumulates the same segments in the same order; only the ITERATION the break happens on moves.
  Observed by AC2 and AC3.
- **S3** The comment at `:41-42` is rewritten to state what the walk now does rather than what it
  intended, and it names the case it did not reach. A comment that described an unreachable state
  for the life of this file is the reason the defect survived a closing review. Observed by AC4.

## 3. Non-goals (OUT)

- No refusal, and no guard, on an empty `_KIT_ROOT`. Outside a git repository `--check` exits at its
  `skip — not a git repo` line before any `${KIT_REL:+…}` rung is read — observed live on
  2026-09-16 with a copy of this file placed outside any repository — so such a guard could never
  fire. A branch that cannot fire is the class this repo's own arms gate reds on.
- `_KIT_ROOT` is neither deleted nor given a reader. It carries the walk's success condition and is
  the break's subject; making it dead-code-clean is a separate judgement about legibility, not this
  defect.
- No change to any `${KIT_REL:+…}` rung. Every one of the seven is correct as written and is what
  makes the empty prefix meaningful; the bug is upstream of all of them.
- No replacement of the walk with `git rev-parse --show-prefix`. The comment at `:27-31` records why
  that call is wrong here: a junctioned worktree makes it answer with the junction's TARGET.
- No change to the three settings-merge remedies. That is `TOOL-cMendedVintage-4`, and it is
  sequenced after this unit because its correct spelling rests on this derivation.

### Edges

- **hands-off** `TOOL-cMendedVintage-4` — that unit spells the settings-merge rungs through
  `${KIT_REL:+$KIT_REL/}`, which resolves to a garbage prefix at a root install until this lands. It
  is sequenced after this unit for that reason.
- **consumes-from** external — nothing. The loop is self-contained and no unit in this build
  precedes it.

## 4. Design

### Data model

MEASURED on 2026-09-16 by lifting the loop from `tools/check-wiring.sh:33-40` verbatim into a probe
script and running it from three locations in a scratch git repository:

| case | script location | `_KIT_ROOT` today | `KIT_REL` today | `KIT_REL` wanted |
|---|---|---|---|---|
| A | `<repo>/tools/` | `<repo>` | `tools` | `tools` |
| B | `<repo>/` | empty | `tmp/kw3/repo` | empty |
| C | outside any repo | empty | `tmp/kw3` | unchanged — see rev-2 |

Case B is the live one: the same probe run through the REAL script in a scratch repo with the file
at the repo root printed `skip agent-cap — not adopted (no agent-cap.js at tmp/kw3/repo/hooks/ or
.claude/hooks/)`. That is a false skip over the concurrency hook, which is the one arm in this file
where a false skip has a security shape, and the file's own comment at `:369-375` records that
exact consequence being found once already — by the guard, not by the derivation the guard rests on.

The reordered loop was run over the same four locations before being written into this spec. It
returned `tools`, empty, the unchanged filesystem path and `a/b/c` for cases A, B, C and a
two-segment nested install, which is every case the file can meet.

**rev-2 rewrote the case C value in the sentence above and in the table's `wanted` cell. Both said
`empty` at rev-1, and the build pass that measured the RED disproved it.** A
reorder cannot empty case C, and did not: the walk outside a repository still runs to the filesystem
root and accumulates every segment on the way, so the probe returned `c/Temp/kw3` both before and
after, byte-identical. Only a `[ -n "$_KIT_ROOT" ] || KIT_REL=""` normalization would empty it, and
section 3 already rules that out as a branch whose effect nothing can observe — verified live at
BASE by running the real script outside any repository, which printed `skip — not a git repo` and
exited 0 before a single `${KIT_REL:+…}` rung was read. The reordered loop actually returns `tools`,
empty, `c/Temp/kw3` and `scripts/gov`. Cases A, B and D are what this unit is for; C is untouched by
construction and out of scope by section 3.

### Inventory

Minted by this unit: nothing. No new variable, no new flag, no new file. The change is the order of
two statements inside one loop and the comment above it.

### Rollout

Behaviour in THIS repo is unchanged — gov installs at `tools/` and case A is already correct — so
the landing is observable here only as an unchanged verdict. The behaviour that moves is an
adopter's, and no adopter in this fleet installs at the root today. That is why the failing case is
staged in a scratch repository rather than found in the tree, and why AC2 exists at all: the risk
this unit actually carries is breaking the case that works.

### Alternatives rejected

Testing `$_p` for `.git` after the append and stripping the last segment on a hit: arithmetic on an
accumulated string to undo work the loop should not have done, and it leaves the same off-by-one
readable in the source.

Leaving the walk and special-casing `KIT_REL` when it names a directory that is not under the repo:
that is a second derivation of the same fact, checked against the first.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/check-wiring.sh` | the loop's two statements swap order; the comment above `:43` is rewritten |

## 5. Production-readiness checklist

- security — the false skip this closes is over `agent-cap.js`, the fan-out guard. Nothing about the
  hook changes; what changes is whether the checker can find it at a root install.
- perf / scale — one comparison per iteration, and one FEWER iteration at a root install.
- error / empty / loading states — the empty prefix becomes reachable, which is the whole unit. The
  outside-a-repo case stays unreachable through `--check` and section 3 says so.
- observability — every `${KIT_REL:+…}` rung prints its resolved probe path in its own skip or
  UNWIRED message, so the derived value is visible in the run's output with no new printing.
- risks — the real risk is regressing case A, which is the only case any live node exercises. AC2 is
  written against it and is the criterion this unit would most plausibly fail.
- testing — AC1 to AC3 are three runs of the real script in scratch repositories at three install
  depths. The permanent arm is declared in section 7.
- migration — none. No adopter's files change; a root-installed adopter starts getting correct
  answers on the next run.
- user docs — none. `KIT_REL` is internal to this script and is documented by the comment S3
  rewrites.

## 6. Acceptance criteria

- **AC1** — When `tools/check-wiring.sh` is copied to the ROOT of a scratch git repository holding no
  `agent-cap.js` and run with `--check`, its agent-cap line reads `at hooks/`.
  Red when: the `.git` test still runs against `$_parent` after the append, so the repo root is never
  tested as itself and the line carries a filesystem-derived prefix — measured today as
  `at tmp/kw3/repo/hooks/`.
  fixture: a scratch git repository under this run's short fixture root, never inside the worktree.
- **AC2** — When `bash tools/check-wiring.sh --check` runs in this repo, every rung that prints a
  probe path still names it under `tools/`, and the run's exit status and severity lines are
  unchanged from BASE `859daa67`.
  Red when: the reorder drops the final segment, so `KIT_REL` is empty here and every rung silently
  falls back to its bare second spelling while still reporting `ok`.
- **AC3** — When the same file is placed at `<repo>/scripts/gov/` in a scratch repository and run
  with `--check`, its agent-cap line reads `at scripts/gov/hooks/`.
  Red when: the reorder breaks on the first `.git` found ANYWHERE rather than on the repository
  boundary, collapsing a two-segment prefix to one.
- **AC4** — When `sed -n '41,43p' tools/check-wiring.sh` is read, the comment states the case the old
  walk could not reach and cites this unit.
  Red when: the loop is fixed and the comment that described the unreachable state is left standing,
  which is how the defect survived one closing review already.

## 7. Gates

`check-wiring self-test` · `install-prefix (shipped surface)` · `hook destinations (every declared hook path ships)` · `govkit selfcheck` · `testsuite counts (every bar self-test prints one)`

New arm: `tools/check-wiring.test.sh` · a scratch repository with this file at the repo ROOT,
asserting the agent-cap probe path carries no prefix segment · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · section 4's case C was wrong in both directions and the build pass measuring
  the RED caught it: its `wanted` cell said `empty` and the paragraph beneath claimed the reordered
  loop had returned empty there. Neither is true — a reorder cannot empty a walk that runs to the
  filesystem root, and the lifted probe returned the same `c/Temp/kw3` before and after. The cell now
  reads `unchanged` and the paragraph records the measurement and why section 3 already wanted it
  that way. No acceptance criterion moved: none of AC1 to AC4 ever named case C.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the install prefix for a remedy string printed by
a wiring checker"` returned `resolve_root` in three Python kits and `resolve` in
`tools/memory-recall/recall_conf.py`, none of which is a `.git` boundary walk, and it reported `.sh`
as an unscanned layer — so every carrier of this idiom is invisible to the map by construction. No
existing seam fits, and the evidence is that the walk being repaired IS this repo's canonical copy of
it: `tools/check-wiring.sh:27-31` records that it was copied from the unattended adopter rather than
invented, and `tools/unattended/adopt-unattended.sh:116` derives `TOOL_ROOT` from the same `KIT_REL`.
The recall probe returned the record that already diagnosed this: `TOOL-dRetiredFork-32` in
`memory/backlog/TOOL.md`, CONFIRMED by that build's closing review with a lifted probe whose three
cases this spec re-ran at BASE and reproduced exactly.

Recall terms used: `--terms "check-install-prefix carried predicate KIT_REL boundary walk repo root
empty prefix settings-merge remedy adopter install prefix ratchet rebaseline PREDICATE_EPOCH
check-wiring"`, with the question "why do shipped kit files carry a literal tools/ prefix and what
predicate catches a carried prefix at a scripts install".
