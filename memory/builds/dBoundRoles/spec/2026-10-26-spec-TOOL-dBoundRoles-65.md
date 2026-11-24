# TOOL-dBoundRoles-65 — the observation worktree's cleanup check compares normalised paths under a named root, and a positive control proves it sees a leftover

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 37 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |
| [2026-10-26-build-TOOL-dBoundRoles-65-deviation-651.md](../build/2026-10-26-build-TOOL-dBoundRoles-65-deviation-651.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-65-round7-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-65-round7-fix-return.md) | research | TOOL-dBoundRoles-66 |
| [2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md](../build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md) | journal | TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-11-24-build-TOOL-dBoundRoles-65-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dBoundRoles-65-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-TOOL-dBoundRoles-65-deviation-652.md](../build/2026-11-24-build-TOOL-dBoundRoles-65-deviation-652.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-65-round7-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-65-round7-fix-brief.md) | research | TOOL-dBoundRoles-66 |
| [2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief.md) | journal | TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-spec-writer.md) | journal | — |
| [2026-11-24-prompt-TOOL-dBoundRoles-65-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dBoundRoles-65-build-brief.md) | journal | — |
| [2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-65-66-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-66 |
| [2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md](../reviews/2026-11-24-review-TOOL-dBoundRoles-1-closing-diff-review-round1.md) | diff-review | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 TOOL-dBoundRoles-81 TOOL-dBoundRoles-82 TOOL-dBoundRoles-83 TOOL-dBoundRoles-84 TOOL-dBoundRoles-85 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted spec 64
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-64-spec-audit-round1.md`) confirmed
finding **id 11 at HIGH**, report item **H1**. No other id shares the item. Id 23 has the same
slash-spelling root at MEDIUM, item M8, and is `TOOL-dBoundRoles-66`'s. The one half of it that this
comparison needs as an operand, a literal root, lands here in S2, because a comparison against a prefix
nobody named compares nothing (§8 F2).

Spec 64's S18 and AC13 and spec 63's S12 check that no observation worktree stays registered "under a
`%TEMP%` prefix". On this host `%TEMP%` is `C:\Users\d41ly\AppData\Local\Temp`, with backslashes, and
`git worktree list --porcelain` prints forward-slash paths such as `C:/projects/coding-governance`.
Neither spec says how to compare the two. A literal prefix check therefore never matches, so the check
passes even when a staged break or a failed import leaves a worktree behind. That is the one path the
check exists for.

This unit makes every such check compare normalised paths under a named root through the comparison
`tools/branch-reconcile/branch_reconcile.py` already ships, and proves with a positive control that the
check reports a worktree left there on purpose. It repairs `TOOL-dBoundRoles-64` and builds one step
after it (order 37).

## 2. Scope (IN)

- **S1** — The comparison. Spec 63's S12 states one comparison for every check of the registered
  worktrees against the observation's paths. The list comes from `git worktree list --porcelain -z` and
  is parsed by `parse_worktrees` in `tools/branch-reconcile/branch_reconcile.py`. An entry lies under
  the root when `check_under(os.path.realpath(entry), os.path.realpath(root))` holds. It is the run's
  own worktree when `derive_key(os.path.realpath(entry))` equals `derive_key(os.path.realpath(run_path))`.
  S12 refuses a raw string prefix test, a `grep` of the porcelain text and `os.path.commonpath`, which
  raises across drives. Observed by AC1.
- **S2** — The operand. Spec 63's S12 names the observation root literally as `<TEMP>/dbr63obs`.
  `<TEMP>` is `tempfile.gettempdir()` in Python, or `cygpath -m "$TEMP"` in bash. Each run's worktree is
  a direct child, `<root>/<epoch>-<pid>`, and the root holds nothing but that probe's worktrees. The
  phrase "a short `%TEMP%` path" leaves S12. Observed by AC1.
- **S3** — The readers. Spec 63's AC11 porcelain half, which unit 64's S18 wrote, and spec 64's S18 and
  AC13 name S12's comparison and S12's root wherever they now read `%TEMP%` or "S12's prefix". Spec 64's
  AC13 names the positive control of S4 as one of its halves. Observed by AC2.
- **S4** — The positive control. The pass makes a scratch repository under `%TEMP%/dbr65c` with one empty
  commit, and adds a detached worktree at `<scratch root>/1-1`, the scratch root being
  `%TEMP%/dbr65c/root`. S1's comparison, given the scratch root in the backslash spelling `cygpath -w`
  prints, reports that entry. A raw `startswith` over the same porcelain reports nothing. Once git's
  forced worktree removal has taken the entry away, the comparison reports nothing. The control runs
  inside its own repository, so it can neither see nor touch this repository's worktrees, and the
  scratch directory is cleared after. Observed by AC3.
- **S5** — The built tree. S1's comparison over this repository's worktree list, against S2's root,
  reports no entry. Where it reports one that an observation left, the pass takes that entry away by
  git's forced worktree removal and records the path in unit 64's ledger. This is safe only because
  S2's root holds nothing but the probe's worktrees. Observed by AC4.
- **S6** — The amendments. The pass bumps spec 63 and spec 64 FIRST, each with a §9 line naming this
  unit (BUILD-METHOD M2, READY). Unit 64's ledger answers AC13 as `amended rev-<n>`, rewriting the
  earlier answer in place by spec 64's §4 "How an item closes". Unit 63's ledger answers AC11 the same
  way where its block already holds an AC11 answer. Observed by AC5.

## 3. Non-goals (OUT)

- Id 23's other halves, the cleanup that can reach another session's worktree and the §5 pricing of it,
  and id 22's staged failed-import half. Both are `TOOL-dBoundRoles-66`'s.
- The report's left-shift checklist entry, "a path comparison across a Windows env var and git output
  normalises both sides, and its check carries a positive control". No clause of this build names it,
  and AC3 is this unit's regression.
- A shared comparison helper in a kit. The comparison is a criterion probe's, and it imports
  `branch_reconcile` rather than copying it. No shipped code reads the observation root.
- Every other reader of `git worktree list --porcelain` under `tools/`, such as
  `tools/unattended/resume-tick.sh@4a8a2169:430` and `tools/check-wiring.sh@49c697ec:2135`. None
  compares against a `%TEMP%` prefix.

### Edges

- **consumes-from** `TOOL-dBoundRoles-63` — S12, AC11 and the observation probe's worktree, which S1, S2, S3 and S5 restate or complete (id 11 of the round-1 audit of unit 64)
- **consumes-from** `TOOL-dBoundRoles-64` — S18, AC13 and the porcelain half its pass wrote into spec 63's AC11, which S3 restates and S4 completes (id 11 of the round-1 audit of unit 64)
- **hands-off** `TOOL-dBoundRoles-67` — S1's comparison, S2's root, S5 and AC4, which unit 67 restates with a second operand, the observation's signature, and the take-away it admits (id 1 of the round-1 audit of units 65 and 66)
- **hands-off** `TOOL-dBoundRoles-68` — S1's comparison, S2's root and AC4, which unit 68 qualifies by S7, green by construction over `dbr63obs` alone, and completes by AC6, the signature's positive control (id 14 of the round-1 audit of units 65 and 66)
- **hands-off** `TOOL-dBoundRoles-69` — S2, S3, S5, S6, AC1, AC2, AC4, AC5, §4 and §5, which unit 69 restates: one `TEMP` source, the printed root, S5 citing spec 63's cleanup rule, the full reader list and ledger criteria read through the revision list (ids 2, 13, 7, 21, 12, 16, 15, 9 and 11 of the round-1 audit of units 65 and 66)

## 4. Design

### The comparison

```python
import os, subprocess, sys
sys.path.insert(0, "tools/branch-reconcile")
import branch_reconcile as br

def registered_under(root):
    text = subprocess.run(["git", "worktree", "list", "--porcelain", "-z"],
                          capture_output=True, text=True, check=True).stdout
    r = os.path.realpath(root)
    return [w["path"] for w in br.parse_worktrees(text)
            if br.check_under(os.path.realpath(w["path"]), r)]
```

`tools/branch-reconcile/branch_reconcile.py#derive_key` folds case and separators through
`os.path.normcase(os.path.normpath(os.path.abspath(str(path))))`. `os.path.realpath` expands an 8.3 short name and resolves a junction, so a `%TEMP%` held in short form
still compares. `check_under` is strict, so the root itself never counts. The root is a directory, not a
name prefix, so a sibling such as `dbr63obs-x` is not under it. The block shows the design's shape; the
pass fits it to S12's probe and to S4's control.

### Evidence

Re-read at HEAD `29acd2d77` on 2026-11-22; each code line is pinned to the blob it was read at:

- `echo $TEMP` prints `C:\Users\d41ly\AppData\Local\Temp`. At `29acd2d77`, `git worktree list`
  `--porcelain` prints 64 `worktree` lines (PINNED, measured 2026-11-22 at `29acd2d77`), all with
  forward slashes. Two of them (PINNED, `29acd2d77`) lie under `%TEMP%`, at
  `C:/Users/d41ly/AppData/Local/Temp/dbr-base` and `.../Temp/dtr-base`, both detached and neither this
  build's: other runs' base checkouts, the entries a bare `%TEMP%` root would red on.
- `tools/branch-reconcile/branch_reconcile.py#derive_key` and `#check_under` are the comparison.
  `#derive_location` compares a worktree with `tempfile.gettempdir()` as
  `check_under(os.path.realpath(path), os.path.realpath(tempfile.gettempdir()))`
  (`branch_reconcile.py@4cbbe71c:183`). `#parse_worktrees` reads the `-z` form and keeps the `prunable`
  flag. Importing the module runs nothing: `branch_reconcile.py@4cbbe71c:1223` guards `main`. Since
  base the file moved only its kit version, so these lines did not shift.
- Measured in a scratch repository under `%TEMP%` on 2026-10-26: with a worktree at `<root>/1-1`, the
  comparison given the root as `C:\Users\d41ly\AppData\Local\Temp\dbr65c\root` reported
  `C:/Users/d41ly/AppData/Local/Temp/dbr65c/root/1-1`, a raw `startswith` reported nothing, and after
  `git worktree remove --force` the comparison reported nothing.
- `os.path.realpath("C:/PROGRA~1")` prints `C:\Program Files`, and `derive_key` of it folds the case to
  `c:\program files`.
- `memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-58-spec-audit-round1.md@c005c4aa:89`
  and `:253` record `os.path.commonpath` raising `ValueError` across drives on this host.
- At `29acd2d77`, spec 64's S18 and AC13 say "a short `%TEMP%` prefix" and "S12's prefix". Spec 63's
  S12 says "under a short `%TEMP%` path", and its §5 security line says the worktree "lives under
  `%TEMP%`". Each is cited by its label, because units 64 and 66 revise both specs before this pass.
- `tools/run-gates/lib-attribute.sh#add_scratch_worktree` and `#remove_scratch_worktree` are the
  worktree lifecycle, and `tools/run-gates/post-merge.sh@eb32abcc:819-820` pairs them with an EXIT
  trap. That is the lifecycle S12's probe may source. It holds no comparison.
- No other reader of the porcelain under `tools/` compares against a temp prefix. A grep for
  `gettempdir`, `$TEMP`, `%TEMP%` and `TMPDIR` over `tools/unattended/resume-tick.sh`,
  `tools/check-wiring.sh`, `tools/loop/loop_witness.py`, `tools/playbook/tag_index.py`,
  `tools/run-gates/run-gates.sh`, `tools/unattended/pass-tree.sh` and `tools/unattended/unattended.sh`
  finds only `TMPDIR` handling in the bar and the driver, none of it on a porcelain path.

### Inventory

Minted: none. `dbr63obs` and `dbr65c` are scratch directory names, not identifiers.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 37, after unit 64 at order 36. `TOOL-dBoundRoles-66` holds order 37, and its
Files touched names specs 63 and 64 and their ledgers too. The declared write sets intersect, so
`--dispatch` refuses the second pass while the first is open (M6 clause 1). Each unit states its own
clauses, and each criterion reads only its own unit's clauses, so either order lands both.

### Files touched (estimate)

- the specs of TOOL-dBoundRoles-63 and TOOL-dBoundRoles-64, rev bumps (S1 to S3, S6), named here for the
  dispatch write set
- the acceptance ledgers of units 63 and 64 and this unit's own, the AMENDED answers and the S5 record,
  named here for the dispatch write set

### Alternatives rejected

- **`cygpath -m` on the prefix alone.** It fixes the slashes on one side only. It folds no case and
  expands no 8.3 name, so a `c:/users/...` entry still misses.
- **`os.path.commonpath`.** It raises `ValueError` across drives (§4 Evidence), so a worktree on a second
  drive would crash the check instead of passing it.
- **A new comparison helper.** `branch_reconcile` already compares a worktree with the temp directory
  this way in `#derive_location`. A second copy would drift from it.
- **A bare `%TEMP%` as the root.** Other sessions' fixture clones and worktrees live under `%TEMP%`, so
  a normalised check against it reds on their entries. The cleanup clause would then reach entries this
  unit does not own, which is the hazard id 23 names.

## 5. Production-readiness checklist

- security — no new write path in shipped code. The control writes only its own scratch repository under
  `%TEMP%/dbr65c`, and S5 removes only entries under S2's root, which holds nothing else.
- perf / scale — one porcelain read per check, and one scratch repository with one worktree for the control.
- error / empty / loading states — a `git worktree list` that fails raises from `check=True`, so the check
  fails loudly rather than reading an empty list as clean.
- observability — the ledger records the control's three readings and any path S5 removed.
- risks — a junction inside `%TEMP%` could point outside it. `realpath` resolves both sides alike, so the
  comparison stays consistent.
- testing — AC1 and AC2 by extraction probes, AC3 by the scratch control, AC4 by the comparison over this
  repository, AC5 by a ledger probe. No suite arm.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe extracts spec 63's S12 bullet, joins its lines and collapses its
  whitespace, the text names `parse_worktrees`, `check_under`, `os.path.realpath` and `dbr63obs`, refuses
  `os.path.commonpath`, and holds no "a short `%TEMP%` path".
  Red when: S12 leaves the root unnamed or the comparison a raw string test, so a leftover never matches.
- **AC2** — When a `python -c` probe extracts spec 64's S18 and AC13 bullets and spec 63's AC11 bullet,
  joined in the same way, each names `check_under` or "S12's comparison" and names S12's root, none holds
  "S12's prefix", and spec 64's AC13 names `dbr65c`. Spec 63's and spec 64's §9 each hold a line naming
  `TOOL-dBoundRoles-65`.
  Red when: a reader of the check keeps the raw `%TEMP%` spelling.
- **AC3** — When the pass runs S4's control, the comparison prints exactly the one path under the scratch
  root, the raw `startswith` prints nothing, and after `git worktree remove --force` the comparison
  prints nothing.
  Red when: the comparison cannot see a leftover worktree whose root is spelled the other way.
  fixture: a scratch repository under `%TEMP%/dbr65c`, short-pathed and deleted after; the tree holds
  none today.
- **AC4** — When S1's comparison runs over this repository's `git worktree list --porcelain -z` against
  S2's root, it prints nothing.
  Red when: an observation left a worktree registered under the root.
  figure: DERIVED at observation time.
- **AC5** — When a `python -c` probe reads unit 64's `**Evidences:**` block, exactly one line answers
  AC13, and `LEDGER` of `tools/memory-tree/deviation_join.py` matches it at the spec-64 revision whose
  §9 line names `TOOL-dBoundRoles-65`. Where unit 63's block answers AC11, the same holds there for
  spec 63.
  Red when: a second line answers the criterion, or the one line names a stale revision.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

No suite arm moves. S4's control is a write probe, so the pass runs it and records its readings.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 64 carries no
  clause, so veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — The literal root: here, or in `TOOL-dBoundRoles-66` with id 23?** Options: (a) this unit names
  the root as S2, and 66's item for id 23 closes the cleanup and the §5 halves; (b) 66 names the root,
  and this unit compares against "S12's root". Under (b), whichever pass lands first meets a root that
  is not yet named, so AC4 has no operand and S5 has nothing it may safely remove. (b) also needs an
  edge between two units at one order, which a parallel group may not carry. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most feature-rich survivor; id 11's comparison is not stated
  without both operands. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of unit 64, id 11 (HIGH, item
  H1), on the report's fix, with branch_reconcile's comparison as the seam.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-67, TOOL-dBoundRoles-68 and TOOL-dBoundRoles-69, the two HIGH promotions and the minors batch of the round-1 audit of units 65 and 66; nothing else moved.
- rev-3 · 2026-11-22 · §3 · §4 · AC5 · §10 · re-grounded at HEAD `29acd2d77` by
  `2026-11-22-prompt-TOOL-dBoundRoles-65-reground-q-brief`. `branch_reconcile.py` moved only its kit
  version since base, so its symbols hold; they are cited as `#derive_key`, `#check_under`,
  `#derive_location` and `#parse_worktrees`, and the temp comparison is re-pointed from `:182` to
  `@4cbbe71c:183`, where it always sat. The porcelain census is re-measured: 64 `worktree` lines, two of
  them other runs' base checkouts under `%TEMP%`. `os.path.realpath("C:/PROGRA~1")` prints
  `C:\Program Files`, the case folded by `derive_key`. The dWitnessedBar-58 citation moves from `:238`,
  which never held it, to `@c005c4aa:89` and `:253`. `post-merge.sh`'s trap is at `@eb32abcc:819-820`,
  `check-wiring.sh`'s porcelain reader at `@49c697ec:2135`, and `LEDGER` is cited by symbol. Specs 63's
  and 64's clauses are cited by label, not line, since units 64 and 66 revise both before this pass.
  Nothing a criterion observes changed.

## 10. Reuse audit

The seam is `tools/branch-reconcile/branch_reconcile.py`: `parse_worktrees`, `derive_key` and
`check_under`, imported as `branch_reconcile.py#derive_location` already uses them for the temp
directory, rather than a second normaliser. `python tools/codebase-map/reuse_lookup.py "compare a windows temp path with git worktree list paths after normalising slashes and case"`
ranked `git`, `run_git`, `read_git_output`, `add_scratch_worktree` and `remove_scratch_worktree`. None
is a normalised comparison: the last two are the worktree lifecycle S12's probe may source. A
`git grep -n normcase -- tools` found the branch_reconcile comparison. The recall query's hits include
`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md@d2b648bd:267`,
which fixed the same class with forward slashes and a case-folded drive. They also include the
dWitnessedBar finding that `os.path.commonpath` raises across drives, and `TOOL-aProbedUnit-11`, the
short `%TEMP%` path rule a clone needs.

Recall terms used: `python tools/memory-recall/query.py "how is a path from a windows environment variable compared with git output paths" --terms "worktree porcelain normcase realpath backslash forward slash TEMP prefix cygpath case fold positive control"`
