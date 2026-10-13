# TOOL-dRedressedBar-7 — records, the regenerated index and the kit versions, measured over the fixed tree

**Status:** SPECCED · rev-1 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dRedressedBar-1-brief.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

At `ebce889c7` the regen preflight refused, and three legs read red, on a stale generated index and
an undeclared carrier rather than on code: `memory hygiene` check 17, `push-main self-test` arms 28
and 29, and `method carriers (every pointer declared)` check 3. The bytes units 1 to 6 move owe kit
version bumps, and possibly a kickoff manifest re-stamp. This unit brings each one back to what its
own checker measures, over the tree the other six units leave. It runs last because every figure it
writes is read off that tree.

Tier-2 by the README's tier rule: the version constants it moves are shipped engine bytes, across
four or more kits.

## 2. Scope (IN)

- **S1** — The bug-class index. Merge `ebce889c7` resolved `memory/gotchas/INDEX.md` with the
  `merge=ours` driver that `.gitattributes:86` declares. The index kept local main's copy and lost
  the rows for two class files tracked at `ebce889c7`:
  `a-gate-that-walks-the-repo-root-reads-other-worktrees` and
  `a-merge-of-the-default-branch-read-as-additions`. The pass runs
  `python tools/run-gates/regen.py --write` as its last write, so the index and every other declared
  output are fresh over the unit's tree. Observed by AC1 and AC2.
- **S2** — The method carrier. `.claude/agents/gov-reuse-scout.md:31` mentions
  `memory/guides/BUILD-METHOD.md` through its rendered charter block. It has no row in
  `memory/project/method-carriers.txt`, so `tools/memory-tree/check-method-carriers.sh` check 3
  reds (lines 112-115). One row is added beside the eight sibling agent rows. Observed by AC3.
- **S3** — Kit versions. Every kit whose shipped bytes moved over `ebce889c7..HEAD` gets its next
  version from `python tools/govkit/govkit.py mint --base ebce889c7`. That includes every carrier the
  minter writes and every `[[regenerate]]` render it runs. Observed by AC4 and AC5.
- **S4** — The kickoff manifest stamp. A commit in `ebce889c7..HEAD` may touch a path on the
  `watch:` line of `memory/guides/SESSION-KICKOFF.md`. If one does, a follow-up records commit
  re-stamps `last-audit:` at HEAD, in the shape of `2e187ee8b`. If none does, nothing is written.
  Observed by AC6.

## 3. Non-goals (OUT)

- No edit to `tools/run-gates/run-gates.sh`, which is a brief non-goal. The run-gates version
  constant sits in that file at line 36. If the pre-mint epoch names `run-gates`, the pass stops
  before minting and returns to the main loop (§4).
- No version number is typed by hand. The minter computes every value.
- No pin, ceiling or registry row is raised to absorb a red that a code change can fix.
- No carrier row other than those check 3 names over this unit's tree. A carrier that a sibling unit
  introduces goes back to that unit.
- No hygiene red other than check 17. Another check that reds at this unit's tip goes back to the
  unit whose write caused it.
- No generated output is edited by hand. No regeneration runs outside `regen.py --write` and the
  minter.
- The run-gates canary, and `GATE_REGEN_CHECK` reaching nested runners, as the brief says.
- No merge to local main and no push.

### Edges

- **consumes-from** `TOOL-dRedressedBar-1` — its re-armed suites are part of the tree that S1 and S2
  measure. Its `.githooks/pre-push.test.sh` edit moves a push-main byte, and the epoch reads push-main
  as `skip` because that kit declares no version.
- **consumes-from** `TOOL-dRedressedBar-2` — its rename in `tools/unattended/gate-guard.js` moves the
  unattended kit's shipped bytes, which S3 bumps.
- **consumes-from** `TOOL-dRedressedBar-3` — the root-cause fixes to the govkit selftest may move
  bytes in any kit. S3's kit set is read only after this unit lands.
- **consumes-from** `TOOL-dRedressedBar-4` — its `tools/hooks/format-guard.js` edit moves the
  agent-cap kit, which S3 bumps.
- **consumes-from** `TOOL-dRedressedBar-5` — its conversions in
  `tools/branch-reconcile/adopt-branch-reconcile.sh` and `tools/roles/adopt-roles.sh` move the
  branch-reconcile and roles kits, which S3 bumps.
- **consumes-from** `TOOL-dRedressedBar-6` — the last edit to the roles adopter's suite before the
  measure. The roles re-render that S3 triggers runs the adopter whose exits that unit arms.
- **hands-off** external — a closing-review fold that moves shipped bytes after this unit owes
  another bump. The lander's mint writes it at the push, as TOOL-aMendedFleet-65 states.
- **hands-off** external — push-main self-test arms 28 and 29 clone HEAD's bug-class index. The main
  loop observes them at the close.

## 4. Design

Every item is a record, a declaration or a value an existing tool writes. No product logic moves.
Each figure is read off its own checker over this unit's tree and never copied from the bar log at
`ebce889c7`.

### Sequence within the pass

1. **Baseline, read-only.** Run the two probes below and keep their output for the acceptance
   ledger. The first is the liveness half of AC4. The second is the liveness half of AC2: at
   `f079464e2` it read `12 declared · 11 fresh · 1 stale`, naming the index (PINNED, 2026-10-14).

   ```bash
   python tools/govkit/govkit.py epoch --base ebce889c7
   python tools/run-gates/regen.py --check
   ```

   If the epoch prints a `FAILED` line for `run-gates`, stop here and return to the main loop.
   Minting that kit writes `KIT_RUN_GATES_VERSION` into `tools/run-gates/run-gates.sh`, which the
   brief's non-goal forbids. The lander's mint would date it at the push instead.
2. **S3, mint.** Run `python tools/govkit/govkit.py mint --base ebce889c7`. `cmd_mint`
   (`tools/govkit/govkit.py:13110`) asks `derive_epoch_state` (`:12976`) for each entry's verdict,
   the same function the `epoch` verb calls. It adds one to the last dotted component of each moved
   kit's value. `write_version_carriers` (`:798`) then moves every carrier, and each minted kit's
   `[[regenerate]]` argv runs. It stages and commits nothing. The kits expected from the briefed
   write sets, with the version source each descriptor declares, are below. The set is DERIVED by
   step 1's output, and unit 3 may add to it.

   | Kit | Moved by | Version source |
   |---|---|---|
   | agent-cap | unit 4, `tools/hooks/format-guard.js` | `tools/hooks/kit.toml:6`, in `agent-cap.js` |
   | branch-reconcile | unit 5 | `tools/branch-reconcile/kit.toml:10`, in `branch_reconcile.py` |
   | roles | unit 5, `tools/roles/adopt-roles.sh` | `tools/roles/kit.toml:22`, in `roles_lib.py` |
   | unattended | unit 2, `tools/unattended/gate-guard.js` | `tools/unattended/kit.toml:6`, in `unattended.sh` |
   | push-main | unit 1, `.githooks/pre-push.test.sh` | none (`tools/govkit/entries/push-main.kit.toml:7`), so `skip` |

   The renders this runs rewrite files outside those kits. The roles render
   `bash tools/roles/adopt-roles.sh --scaffold` (`tools/roles/kit.toml:72-73`) rewrites the
   `.claude/agents/gov-*.md` files and `.claude/roles.json`. The unattended render
   (`tools/unattended/kit.toml:193-194`) rewrites `memory/guides/UNATTENDED-PROTOCOL.md` and
   `.claude/skills/unattended/SKILL.md`.
3. **S2, carrier row.** Measure after the mint, because the roles render rewrites the agent file.
   The probe mirrors the checker's population (`tools/memory-tree/check-method-carriers.sh:63-71`)
   and its checks 3 and 4, without running the leg.

   ```bash
   git grep -lF BUILD-METHOD.md -- . ':!memory/' ':!*.test.sh' \
     ':!tools/memory-tree/BUILD-METHOD.template.md' ':!tools/memory-tree/check-method-carriers.sh'
   grep -vE '^\s*(#|$)' memory/project/method-carriers.txt | sed 's/ *·.*//;s/[[:space:]]*$//'
   ```

   On 2026-10-14 at `f079464e2`, the first list held exactly one path the second lacks:
   `.claude/agents/gov-reuse-scout.md`. The second held none that the first lacks. The row goes
   between the `gov-researcher.md` and `gov-skeptic.md` rows:

   ```
   .claude/agents/gov-reuse-scout.md · rendered role agent; its rendered charter block's protocol line points a build of more than one pass at the method, and it restates none of it
   ```

   This carrier was handed off to aOrientedCast by `TOOL-aSweptBar-6` §3. That landing rendered the
   agent and wrote no row.
4. **S1, regenerate.** Run `python tools/run-gates/regen.py --write`, the one command the lander
   runs over a tree it pushes (`tools/push-main.sh:35-42`). Its memory-tree item for the index is
   the declared pair `gotchas.py --write` / `gotchas.py --check` (`tools/memory-tree/kit.toml:487-490`).
   The expected move is the two rows S1 names. The commit body names any other path the command
   moves, because a sibling unit or step 2's renders left it stale.
5. **Probe and commit.** Run AC1 to AC5 and commit with the unit id in the subject.
6. **S4, stamp.** Run the AC6 probe. If it prints a commit, follow `manifest-check.sh`'s C5
   remedy (`skills/session-kickoff/manifest-check.sh:1450-1475`). Re-read the §B claims derived
   from each touched watch path, and re-stamp `last-audit:` as `<ISO time> @ <HEAD sha>`, which is
   `STAMP_SHA_RULE` (`:1343`). Commit it as a follow-up whose message carries a `manifest-audit:`
   line, in the shape of `2e187ee8b`. The stamp cannot name the commit that carries it, which is why
   it is a second commit. A watch path moves only if the minter bumped a kit that carries one, such
   as memory-tree's marker in `memory/guides/BUILD-METHOD.md` (TOOL-aMendedFleet-108).

### Why one unit

The README's roster gives this unit three records and the version values. None of them is designed
here: each is the output of a tool that already exists, run over the tree the other six units leave.
`TOOL-aSweptBar-6` had the same shape and closed. A split would add order steps and no reviewable
seam, because no record here reads another's output except the carrier row, which reads the mint's
render, and the sequence above orders that.

### Alternatives rejected

- **Bump each version by hand.** The minter derives the same set as the epoch leg and writes every
  carrier in the basis. A hand bump misses carriers. DEPL-aHoistedPass-10 records an unattended
  carrier outside the populations that `tools/check-kit-versions.sh` reads.
- **Leave every bump to the lander's mint.** `tools/push-main.sh:26-31` states that a branch owes no
  bump. The brief makes the bump this unit's work, and the owner said go on it. The lander's mint
  stays the backstop for a later move.
- **Run `gotchas.py --write` alone.** That fixes the one stale output known today. It does not fix
  an output that a sibling unit or step 2's renders leave stale. The README's goal is a fresh regen
  preflight with no knob.

### Files touched (estimate)

- `memory/gotchas/INDEX.md`
- `memory/project/method-carriers.txt`
- `tools/hooks/agent-cap.js`
- `tools/branch-reconcile/branch_reconcile.py`
- `tools/roles/roles_lib.py`
- `tools/unattended/unattended.sh`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Production-readiness checklist

- security — No new write path. The minter and `regen.py` write only declared files in the working
  tree, and stage nothing. The carrier row is one registry line. No secret, credential or egress is
  involved.
- perf / scale — `regen.py --check` took 16 s on node d at `f079464e2` (PINNED 2026-10-14), and
  `--write` runs the same twelve items. The minter makes a few git reads per registry entry and
  runs the renders of the kits it moves.
- error / empty / loading states — The minter exits 1 on a broken entry or a failed render, and the
  pass stops there (`cmd_mint` docstring). `regen.py --write` stops after a failing stage
  (`tools/run-gates/regen.py:409-411`). An epoch with no `FAILED` line means the minter writes
  nothing, and the commit body says so. A `run-gates` hit stops the pass before any write.
- observability — The minter prints one line per entry and `regen.py` one per item, plus a
  summary. The commit body names each kit with its old and new value.
- risks — A closing-review fold that moves bytes after this unit leaves a bump undated until the
  lander's mint. The roles render rewrites every agent file, which is why S2 is measured after
  step 2. A minted memory-tree marker moves a watched path, which is why S4 exists.
- testing — The direct probes of §6 in the pass. The unit adds no arm. The close's bar observes the
  §7 legs, including push-main self-test arms 28 and 29.
- migration — None. Version values move forward, and an adopter reads them through
  `govkit.py update`.
- user docs — N/A — no `help/` page states a kit version or a carrier; checked with `git grep` over
  `help/` on 2026-10-14.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --check` runs at the unit's tip, it prints no
  `HYGIENE check 17` line. `git diff ebce889c7 -- memory/gotchas/INDEX.md` adds a row linking each of
  the two class files S1 names, and every other row it adds or changes links a class file tracked at
  the tip.
  Red when: either class has no row, or a byte of the index differs from what `--write` renders.
- **AC2** — When `python tools/run-gates/regen.py --check` runs at the unit's tip, every item reads
  `fresh` and the summary line reads `0 stale`.
  Red when: any declared output is stale over the unit's tree, the index included.
  figure: the declared count is DERIVED by the command; 12 is its PINNED reading at `f079464e2`.
- **AC3** — When the two lists from §4 step 3 are compared at the unit's tip, neither holds a path
  the other lacks. `grep -lE '^## M[0-9]+' .claude/agents/gov-reuse-scout.md` prints nothing.
  Red when: the agent file has no row in `memory/project/method-carriers.txt`, a row names a file
  that no longer mentions the method, or the agent file holds a copied method heading.
- **AC4** — When `python tools/govkit/govkit.py epoch --base ebce889c7` runs before the mint, it
  prints a `FAILED` line for each kit that units 1 to 6 moved. When the same command runs at the
  unit's tip, it prints no `FAILED` line and exits 0.
  Red when: a moved kit keeps its value, or its bump precedes a later move of its bytes.
  figure: the kit set is DERIVED by the pre-mint run; §4's table is the expectation from the brief.
- **AC5** — For each kit the minter moved from value `<old>`, `git grep -nF "gov:kit <kit>@<old>"`
  prints nothing at the unit's tip. The minted commit's diff of the kit's version source shows
  `<old>` becoming the next value.
  Red when: a carrier keeps the old marker, or a value moves by more than its last component.
- **AC6** — When `git log --format=%H ebce889c7..HEAD -- <each path on the watch: line>` runs over
  `memory/guides/SESSION-KICKOFF.md`'s watch list, it prints nothing. If it prints commits, the
  newest one is an ancestor of, or equal to, the newest commit that moved the `last-audit:` value.
  Red when: a watched path moved after the last stamp, the C5 condition at
  `skills/session-kickoff/manifest-check.sh:1468`.

## 7. Gates

`memory hygiene` · `method carriers (every pointer declared)` · `kickoff-manifest ratchet` · `push-main self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `govkit selfcheck` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `branch-reconcile selftest` · `recall floor` · `recall floor arms`

The close runs these in its one bar. Its push-main self-test is where arms 28 and 29 go green: their
fixture clones HEAD, and HEAD's index is fresh after this unit. The unit adds no arm.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft from the build brief, with every attribution and figure re-verified against the tree at `f079464e2`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "regenerate a stale generated index and bump the version
of every kit whose shipped bytes moved"` returned only name-token neighbours. Examples are
`resolve_kit_dir`, `resolve_generated_indexes` and `write_version_carriers`, and none is a new seam to
build beside. No new code is written, so no existing seam fits a new mechanism. The unit extends
three existing commands: the lander's minter `cmd_mint` in `tools/govkit/govkit.py`, the declared
generated-output runner `tools/run-gates/regen.py`, and the per-repo carrier registry
`memory/project/method-carriers.txt`. Recall surfaced the rules followed here. TOOL-aMendedFleet-65
says the lander mints, so a branch owes none. TOOL-aPrimedIndex-4 says the lander regenerates the
`merge=ours` indexes. TOOL-aMendedFleet-108 says a minted watched carrier reds C5. The precedent unit
is TOOL-aSweptBar-6.

Recall terms used: `python tools/memory-recall/query.py "how does a build bump the kit versions its
units moved and refresh a merge=ours generated index before the bar" --terms "govkit mint epoch kit
version bump regen gotchas INDEX merge=ours method-carriers lander"`
