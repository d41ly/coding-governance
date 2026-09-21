# TOOL-aWokenSentinel-20 — `resolve_sidecar_dir` lives in `lib-unattended.sh`: one derivation of the sidecar root for the driver and the tick, counted in code lines across the three files

**Status:** CLOSED · rev-2 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-20-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-20-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-20-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-20-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H6 (round 2, raw id 36): `TOOL-aWokenSentinel-11` §3 rested on "at this order
the count is 1 by unit 2's AC7", and spec 2 AC7 never pins the `rev-parse --git-dir` literal — it
counts `resolve_sidecar_dir` — so nothing asserts the premise. Worse, the check as specced counted
comment lines in a driver whose idiom is a prose header beside every function, so a header sentence
carrying the literal reads 2 on the unmodified driver at unit 11's order, and unit 11's "no driver
change" leaves no unit able to fix it. The disposal takes the ratified answer rather than the
narrower one: `tools/unattended/lib-unattended.sh`'s header (the lib header's pointer, dUnstalledConvoy seq 22) is where a
spelling two scripts must answer identically lives, spec 5 already has the tick source the lib, and
spec 5 S4 spelled the same root inline for the tick's resume log. This unit moves `resolve_sidecar_dir`
into the lib one order after unit 2 defines it, so the driver and the tick call one function; unit
11's check, folded at its rev-2, counts CODE lines across driver, lib and tick and requires exactly
one, in the lib, with at least one call in the driver — a premise this unit's own criteria assert.

## 2. Scope (IN)

- **S1** — `resolve_sidecar_dir` is moved verbatim from `tools/unattended/unattended.sh`, where
  unit 2 defines it, into `tools/unattended/lib-unattended.sh` under its own header, which states
  the rule: the sidecar root is the WORKTREE's git dir plus `/unattended`, derived here and
  nowhere else, and an empty `rev-parse` answer is a refusal under the caller's dead-probe rule.
  The driver sources the lib at `unattended.sh:78` before any verb runs, so every existing call
  resolves unchanged. "Verbatim" is a `diff` of the extracted body against unit 2's, and the
  `return 1` branch is exercised from a directory inside no repository. Observed by AC1 and AC2.
- **S2** — The code-line count of the literal `rev-parse --git-dir` is exactly 1 in the lib and 0
  in the driver at this unit's tip, measured with `grep -cE '^[^#]*rev-parse --git-dir'` per file,
  and the driver carries at least one call `$(resolve_sidecar_dir)`. Observed by AC1 and AC2.
- **S3** — The lib's TOP header — the comment region before the file's first code line, which
  lists what the file holds — gains the function by name, and `tools/unattended/kit.toml` needs
  no change because the lib is already a shipped file. Observed by AC3, whose grep is scoped to
  that region so the definition's own comment cannot satisfy it.
- **S4** — Three sibling folds, all landed with the disposal that authored this spec: spec 11 at
  its rev-2 to this population and predicate; spec 5 at its rev-3 so the tick's resume log at S4
  resolves through `$(resolve_sidecar_dir)` from the lib it sources rather than an inline
  `rev-parse`; spec 2 at its rev-3 to hand the move off and to pin the code-line count at its own
  tip. Observed by AC4, one needle per fold.

## 3. Non-goals (OUT)

- **No change to what the function prints.** The worktree's git dir, never the common dir; unit
  2's AC7 fixture is the proof and stays unit 2's.
- **No move of any other driver function.** The lib holds predicates two scripts share; the
  liveness verb's other helpers have one caller.
- **No check.** The count is unit 11's gate; this unit is the population that gate binds.
- **No hook change.** `stop-guard.js` and `stall-recorder.js` derive the git dir in JavaScript
  through unit 3's `deriveSidecarPath`; a shell function cannot be their spelling, and they are
  outside unit 11's population by that design.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-2` — `resolve_sidecar_dir` as unit 2 defines it in the
  driver, and the `--liveness` call site that reads `stall.<slug>.log` through it. Without the
  definition there is nothing to move.
- **hands-off** `TOOL-aWokenSentinel-11` — the check's population and predicate: code lines only,
  across driver, lib and tick, exactly one and in the lib; spec 11's §3 premise is this unit's S2.
- **hands-off** `TOOL-aWokenSentinel-5` — the tick's resume-log root through
  `$(resolve_sidecar_dir)` from the lib it already sources, in place of spec 5 S4's inline
  spelling; the tick is then inside unit 11's population and carries zero code-line spellings.
- **hands-off** external — nothing.

## 4. Design

### The move

The function's body is unit 2's, unchanged:

```
resolve_sidecar_dir() { # -> <worktree git dir>/unattended, the one derivation of the sidecar root
  local _sd; _sd=$(GIT rev-parse --git-dir 2>/dev/null) || _sd=""
  [ -n "$_sd" ] || return 1
  printf '%s/unattended\n' "$_sd"
}
```

It leaves `unattended.sh` and lands in `lib-unattended.sh` beside `GIT`, which it calls and which
the lib already defines; the driver sources the lib at `unattended.sh:78` and the tick at spec 5's
walk, so both callers find it. The comment above the definition carries the rule and the
does-not-hold-the-common-dir sentence that unit 2's spec states, moved with the code so the reader
of the lib is not sent to the driver for it.

### Why the lib and not a corrected predicate alone

Counting code lines in the driver alone closes the comment case and leaves the tick's inline
spelling — spec 5 S4 at its rev-2 — as a second bash derivation one file over, exempted from the
check by a reason the lib answers. The lib's header ratifies that two spellings of one rule is the
two-answers-to-one-question class and that the fix is one spelling in that file; the tick already
sources it for `read_bound_key`. One move satisfies H6, gives unit 11 a premise a criterion states,
and takes M9's exemption out of spec 11 by making it unnecessary.

### Inventory

No identifier is minted; `resolve_sidecar_dir` is unit 2's name, already graded in cell
`sh.function` with verb `resolve`, moved between two shipped files.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/lib-unattended.sh` | the function and its header, in |
| `tools/unattended/unattended.sh` | the function, out; the header comment above unit 2's call site points at the lib |

### Alternatives rejected

- **Fold spec 2 AC7 to pin the literal at exactly 1 comments-included.** The audit's first option.
  It forbids the driver's own idiom of a prose header naming the rule beside the function, and
  leaves the tick's spelling outside every count.
- **Count non-comment lines in the driver only.** The audit's second option; it is the predicate
  unit 11 now carries, over a population one file too narrow.
- **Define the function in both files.** Two copies is the defect.

## 5. Production-readiness checklist

- security — N/A; a function moves between two files the driver sources in one process.
- perf / scale — none; one `rev-parse` per call, as before.
- error / empty / loading states — an empty `rev-parse` answer returns 1, and the caller's
  dead-probe rule refuses, exactly as unit 2 has it.
- observability — none changes; the function prints a path.
- risks — a caller that sources the driver's functions without the lib would lose the name; no
  such caller exists, because the driver refuses at `unattended.sh:73` when the lib is missing.
- testing — §6; greps and one call through a bare shell that sources the lib.
- migration — N/A; the move is within one commit and one kit.
- user docs — none; the lib's header.

## 6. Acceptance criteria

- **AC1** — When `grep -cE '^[^#]*rev-parse --git-dir' tools/unattended/lib-unattended.sh` runs
  at the tip it prints 1 and `grep -cE '^[^#]*rev-parse --git-dir' tools/unattended/unattended.sh`
  prints 0; over the files at the tip of unit 2's pass — the commit whose subject carries
  `TOOL-aWokenSentinel-2`, one order before this unit — the two print 0 and 1. At `12513c25`, the
  sha this design was grounded against, both print 0, because unit 2 has not defined the function
  there, so no reading is taken at that sha.
  Red when: the driver keeps a copy, which is two spellings; or the lib has none, which is a
  reader with no derivation.
  figure: every count is DERIVED by the greps at observation, over the tip and over the files at
  the tip of unit 2's pass, never at the status header's `base`.
- **AC2** — When a bare `bash` sources `tools/unattended/lib-unattended.sh` inside a scratch
  repository and runs `resolve_sidecar_dir`, it prints the repository's git dir with `/unattended`
  appended and exits 0; in a linked worktree of that repository it prints the WORKTREE's git dir,
  not the common dir; from a directory inside no repository the same call prints nothing and exits
  non-zero, which is the `return 1` branch; `grep -cE '^[^#]*\$\(resolve_sidecar_dir\)' tools/unattended/unattended.sh`
  prints at least 1; and `diff` of the body extracted by `sed -n '/^resolve_sidecar_dir()/,/^}/p'`
  from `tools/unattended/unattended.sh` at the tip of unit 2's pass against the same extraction
  from `tools/unattended/lib-unattended.sh` at this unit's tip is empty.
  Red when: the moved function resolves the common dir, which is every worktree sharing one
  sidecar; or the driver no longer calls it; or the empty answer returns 0, which composes a
  sidecar path from an empty root — the liveness class charter §7 names and unit 2's AC8 stages
  through `stat`, not through an empty git-dir answer; or the body moved with an edit.
  fixture: a scratch repository under a short `%TEMP%` path with one `git worktree add`, and a
  plain directory outside any repository.
- **AC3** — When `sed -n '/^[^#]/q;p' tools/unattended/lib-unattended.sh | grep -c 'resolve_sidecar_dir'`
  runs at the tip it prints at least 1 — the leading comment region up to the file's first code
  line, which is the top header and cannot include the definition or the rule comment §4 places
  directly above it — and 0 at this unit's base; and `grep -c 'resolve_sidecar_dir'` over the
  whole file prints at least 2, the header and the definition.
  Red when: the lib's top header does not say the file holds it, which sends the next reader to
  the driver, and which the whole-file count alone cannot see because the definition and its own
  comment supply two hits with the header untouched.
  figure: the header's extent is DERIVED by the `sed` at observation, never typed as a line count.
- **AC4** — When `grep -ci 'code.line' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-11.md`
  runs it prints at least 1 (the landed rev-2 spells it `CODE lines` and `code-line`, never
  lowercase `code lines`, which the rev-1 needle printed 0 against);
  `grep -c "resume-log root is that function's answer" memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md`
  prints at least 1, which is the S4 sentence of that spec's rev-3 and nothing else; and
  `grep -c 'aWokenSentinel-20' memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-2.md`
  prints at least 1, the hand-off of that spec's rev-3. All three folds landed with the disposal
  that authored this spec, and all three greps were run at authoring time.
  Red when: a sibling still describes the driver-only count or the tick's inline root, or spec 2
  does not hand the move off, which is the two-spellings class re-entering by prose.
  figure: every count is DERIVED by the greps at observation; 11, 1 and 2 as read on 2026-09-20.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the greps of AC1, AC3 and
AC4 and the bare-shell call of AC2. Under `unattended kit gate`, unit 11's check is the arm that
reads this unit's population at the close.

New arm: none — the count is unit 11's check; this unit moves the population it counts

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · S1 · S3 · S4 · AC1 · AC2 · AC3 · AC4 · folded spec-audit round 3: M13
  (raw 14) — S4 named three folds and AC4 observed two with a count any mention satisfies, so AC4
  now carries one needle per fold, each the sentence the fold wrote; M14 (raw 21, 35) — AC4's
  `code lines` needle printed 0 over the landed spec 11, which spells it `CODE lines`, so the
  needle is case-insensitive and was run at authoring time; M15 (raw 34) — AC1's base-side
  figures were stated at `12513c25`, where both files print 0 because unit 2 has not defined the
  function, so they are read at the tip of unit 2's pass and the spec says the status-header base
  is not where they hold; L5 (raw 15) — AC2 exercises the `return 1` branch from outside any
  repository and diffs the extracted body against unit 2's, which is what "verbatim" means; L6
  (raw 16) — AC3's grep is scoped to the leading comment region so the definition and its rule
  comment cannot satisfy the header requirement.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of H6 (raw id 36); takes the lib home the lib header's pointer (dUnstalledConvoy seq 22) ratifies over the
  audit's two narrower options, per BUILD-METHOD M3's feature-rich rule.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive the sidecar root once in a shared shell library
sourced by the driver and the tick"` ranked `repo_root` (four Python kits' root resolver, fan-in 13)
and `map_root`, `read_roots` and `require_adopted_root` — Python root resolvers for other kits, not
reachable from bash — and reported `unscanned layers: .sh`; the seam is the shell library the map
cannot see. Read at source: `tools/unattended/lib-unattended.sh:1` to `:19`, whose header ratifies
that a rule two scripts share lives there and names the lib header's pointer (dUnstalledConvoy seq 22); its `GIT` wrapper
the function calls; the driver's sourcing of the lib at `tools/unattended/unattended.sh:73` to
`:78`; and spec 2 §4 item 9, which defines the function this unit moves. The recall probe returned
`TOOL-aPacedTurnstile-10`, this build's round-2 audit at the M9 paragraph, which names the lib as
the ratified home, and `TOOL-aCollapsedScan-7`; no prior record puts the sidecar root in the lib,
which is why this unit exists.

Recall terms used: `lib-unattended sourced two spellings one rule driver gate leg sidecar root rev-parse git-dir derivation tick`
