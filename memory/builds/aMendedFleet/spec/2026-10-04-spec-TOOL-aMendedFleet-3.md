# TOOL-aMendedFleet-3 — the lander refuses a merge that loses a definition a parent carried

**Status:** CLOSED · rev-4 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · order 3 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-3-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

Merge `01c22e155` resolved a conflict by taking one side and lost `write_ask_views`, the code of two
CLOSED units, from main; nothing at the push boundary noticed. This unit makes the push boundary
refuse such a merge at DEFINITION level, as the charter's §1 Landing rule (diff the merge against
BOTH parents, the "auto-took" class) already says in prose: `.githooks/pre-push` refuses it on a
default-branch push, and `tools/push-main.sh --prepare` refuses it before moving the run's branch,
unless the merge's own message carries `superseded: <name> -> <successor>`. Report `[B#11]`, Q3 rank 1.

This spec says LOSS where the report says "drop", for one mechanical reason: hygiene check 25 reads
the drop and delete verb family beside a backticked identifier in §2 as a retirement, and this unit
retires nothing.

## 2. Scope (IN)

- **S1** — `python tools/lexicon/lexicon.py --merge-losses <a>..<b>` grades every two-parent merge in
  `git rev-list --merges <a>..<b>`. For each merge it reads definitions, through the lexicon's own
  `extract_text` and the languages `.lexicon.conf` arms, in every armed path where the merge's tree
  differs from either parent, at the merge base, at both parents and at the merge. A LOSS is a
  `(path, name)` present in a parent and absent from the merge, UNLESS it is present at the merge
  base and absent from the other parent: the other side took it out, and git applied that.
  Observed by AC1, AC2, AC3, AC4.
- **S2** — Three dispositions clear a candidate loss, each counted and printed rather than silent:
  `masked` when the merge's tree defines the name at a NEW home, a path the carrying parent did not
  define it in (a move); `restored` when the tree at `<b>`, the range tip, defines it at the lost
  path or at such a new home (a later commit put it back); `superseded`
  when the merge's message carries a line `superseded: <name> -> <successor>` and `<successor>` is a
  definition in the merge's tree. A `superseded:` line whose successor names no definition there is
  itself reported, naming the successor. Observed by AC3, AC4.
- **S3** — Output and exit. One line per loss naming the merge sha8, the parent number, the path and
  the name, then the remedy: restore it in a new commit, or add the `superseded:` line to the merge.
  One summary line on every run: merges graded, merges skipped, paths read, losses, masked,
  restored, superseded, seconds. Exit 0 with no loss, 1 with any, 2 for a DEAD PROBE: no
  `.lexicon.conf`, no armed language, a git call that failed, or armed paths read and zero
  definitions found across all of them. An octopus merge and a merge with no merge base are skipped
  and named, never graded silently. Observed by AC1, AC5, AC10.
- **S4** — `.githooks/pre-push`, for the default-branch ref update whose remote sha is not all
  zeroes, runs S1 over `<remote sha>..<local sha>` immediately after the straggler-guard block and
  before the bar is vetted. Exit 1 refuses through `write_refusal` with the new token `merge-loss`
  and the run-log decision `refuse-merge-loss`. Exit 2 prints `DEAD PROBE` and allows. No usable
  python, or no lexicon kit under the pushing tree or beside the hook, prints one skip line naming
  the ref. A brand-new remote branch (all-zero remote sha) prints a skip line. Observed by AC6, AC7.
- **S5** — `tools/push-main.sh --prepare`, after its merge at the detached advertised tip and before
  the compare-and-swap `update-ref`, runs S1 over `<advertised tip>..<merge>`. Exit 1 checks the
  branch back out unmoved, prints the loss lines and returns 1, the same shape as its CONFLICT path.
  Exit 2 or an unresolvable kit prints and continues, since pre-push binds anyway. Observed by AC8.
- **S6** — The mode's docstring and the pre-push block's header each state what the check does NOT
  see. Observed by AC9.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new Python definitions.
  NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its
  check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- A line-level check. The report measured that shape flagging nine merges where three lost a
  definition, and demanding a 368-line list for one documented rewrite; its "Do not build" list
  names it. Node d's dUnstuckLanding ask 26 is worded line-level; its three accept cases are taken
  here, at definition level.
- Loss below definition level: a body that lost lines under a surviving name, a prose section, a
  record row, a conf key. The S6 header states it.
- Branch pushes. The refusal binds where the loss lands, the default branch; the straggler guard
  keeps the branch refs.
- Restoring `write_ask_views` (`TOOL-aMendedFleet-1`) and the census of past merges
  (`TOOL-aMendedFleet-2`). This unit grades merges a push carries, not history already on main.
- A merge-bar leg. The pushed range is known only at the push boundary; a bar leg over `BASE..HEAD`
  would re-grade history every run.
- Editing the charter. Its §1 Landing sentence already states the rule this mechanizes.

### Edges

- **consumes-from** external — the lexicon kit and a `.lexicon.conf` arming at least one language;
  without them the check announces a skip or a DEAD PROBE and allows, and the push proceeds.
- **hands-off** external — `tools/drift-audit/drift_report.py` keeps its own `_read_defs_at_sha`, a
  whole-tree reader over the same extractor; moving it onto the reader this unit adds is a
  separate mechanism, filed as an ask by this unit's build pass.
- **hands-off** `TOOL-aMendedFleet-65` — the python and kit resolution this unit adds to
  `tools/push-main.sh` for its merge-loss call, which unit 65's version minter reuses rather than
  adding a second resolver to the same script.

## 4. Design

### Evidence

Read at HEAD `af449c0b` (run BASE `7af5f564`), 2026-10-04:

- `01c22e155` has parents `5ac44b04e` and `ef1dcdb61`, merge base `1f9158708`.
  `git show <rev>:tools/unattended/unattended.sh | grep -c '^write_ask_views()'` reads 0, 1, 0, 0 at
  the first parent, second parent, base and merge. So the second parent added it and the merge lacks
  it. HEAD lacks it too.
- `git rev-list --merges ac65de998..35438ba0a` is one merge, `2cbb2f09c`. A line probe over its two
  parent diffs finds one changed definition line, `verb_review() { # slug · subject · …`, whose name
  survives at the merge with a longer comment. A line-level check reds on it; this one does not.
- `lexicon.extract_text(src, mode, pset)` is the one dispatch to the readers `.lexicon.conf` LANGS
  arms; here `py` is `python-ast:parser`, `sh` is `shell-tokens:parser` and `js` is
  `js-regex:probe`. `tools/drift-audit/drift_report.py` already reads definitions from git blobs at
  two shas through it, in `_read_defs_at_sha`, with ONE `git cat-file --batch`; its comment
  measures that read at 0.957 s cold for two whole trees on node `d` (PINNED, from that comment).
- `.githooks/pre-push`'s straggler-guard block is the precedent for a python check at push: it
  resolves a kit through `resolve_kit_dir`, treats exit 1 as refuse and exit 2 as a DEAD PROBE that
  prints and allows, and prints a skip line when no python or no kit resolves. It skips the default
  ref; this block grades only the default ref.
- `tools/push-main.sh`'s `derive_push_failure` reads any unknown refusal token through its `?*` arm
  ("pre-push refused the push (<token>)"), so the lander needs no change to report `merge-loss`.
- `cmd_prepare` in `tools/push-main.sh` already refuses a conflicting merge by checking the branch
  back out unmoved; S5 reuses that exit shape. The script carries no python resolver today.

### The rule, stated once

For merge `M` with parents `P1`, `P2` and base `B = merge-base(P1, P2)`, over the armed paths in
`git diff --name-only P1 M` and `git diff --name-only P2 M`:

```
candidate = { d in defs(Pi) : d not in defs(M) and not (d in defs(B) and d not in defs(Pj)) }
loss      = candidate - masked(name in defs(M) at a new home)
                      - restored(d in defs(<b>), or name in defs(<b>) at a new home)
                      - superseded(merge message names it, successor in defs(M))
```

`d` is `(path, name)`. A new home is a path the carrying parent (or parents) did not define the name
in. The whole-tree reads behind it are name-to-path indexes over every armed path of M, of the
carrying parent and of `<b>`, read only when a candidate exists, so a clean merge costs the changed
paths alone.

### Inventory

| Identifier | Where | Cell |
|---|---|---|
| `read_defs_at_sha` | `tools/lexicon/lexicon.py` | `py.function` |
| `read_superseded` | `tools/lexicon/lexicon.py` | `py.function` |
| `check_merge_losses` | `tools/lexicon/lexicon.py` | `py.function` |
| `check_merge_losses` | `tools/push-main.sh` | `sh.function` |
| `--merge-losses` | the lexicon CLI's mode set in `main` | flag |
| `merge-loss` | `.githooks/pre-push` refusal token | token |
| `refuse-merge-loss` | `.githooks/pre-push` run-log decision | token |

`lexicon.py --suggest` answered OK for each function name in its cell, 2026-10-04.
`tools/push-main.sh` also gains the `resolve_python` and `resolve_kit_dir` canonical-copy blocks,
byte-identical to their markers' sources, as `.githooks/pre-push` carries them.

### Rollout

Live at landing: there is no flag, because the check refuses only a merge that loses a definition,
and the remedy is one commit. It runs only over the pushed range, so history already on main is
never re-graded. Node d's dUnstuckLanding branch edits `.githooks/pre-push` only at its inherited-red
policy, far below the straggler-guard block, so the reconcile is two disjoint hunks.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`
- `tools/lexicon/selftest.py`
- `tools/lexicon/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `memory/map/generated/symbols.json`

Plus the lexicon kit's version carriers, whichever the kit-version legs name at build time. This
set shares `tools/lexicon/selftest.py` with `TOOL-aMendedFleet-6`, whose codec arm is a separate
insertion, and `tools/push-main.sh` with `TOOL-aMendedFleet-65`, which calls the resolver blocks
this unit adds rather than adding its own.

### Alternatives rejected

- **The checker as a new module beside the hook** (`.githooks/`). It would need its own resolver
  for the lexicon kit, then a declared row in the push-main deployer entry; the lexicon mode reads
  its own declaration in-process and ships where the definitions are defined.
- **A mode in `tools/drift-audit/drift_report.py`.** It reuses `_read_defs_at_sha` directly, but that
  script loads the drift project layer on every run and roots itself on its own file, so a
  push-main adopter without drift-audit would get a refusal-capable check that cannot start; it
  would also make a report-only kit refuse.
- **`git show --remerge-diff`.** It shows only how a resolution differs from git's own re-merge,
  which is line-level: the documented-rewrite merge would list every rewritten line.
- **Grading only names a parent ADDED**, the brief's wording. A resolution that takes out a function
  both parents carried from the base is the same loss and is invisible to it. The wider rule reads
  the same paths, so it costs nothing more.

## 5. Production-readiness checklist

- security — no new write path: the mode reads git objects and prints. The `superseded:` escape is
  a commit-message line, visible in history; it accepts only a successor that resolves at the merge.
- perf / scale — four blob reads per changed armed path per merge, one `cat-file --batch` per sha;
  AC10 holds a ceiling. The whole-tree name sets are read only when a candidate exists.
- error / empty / loading states — every can-not-answer state is exit 2 with a printed reason; no
  python and no kit each print a skip line; an octopus or base-less merge is named as skipped.
- observability — the summary line prints every count and the seconds; the refusal token and the
  run-log decision name the class.
- risks — a same-named definition at a path the carrying parent did not define it in masks a loss;
  the masked count is printed, and the S6 header names the case. A false red costs one `superseded:` line or one restore commit.
- testing — one arm each in the lexicon suite, the pre-push suite and the push-main suite, on the
  fixture §6 describes; each observed RED against the base hook or lander first.
- migration — none: the check grades only merges a push carries.
- user docs — the lexicon README's mode section and the pre-push block header.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --merge-losses 01c22e155~1..01c22e155` runs at the
  repository root, it exits 1 and a loss line names `01c22e15`, parent 2,
  `tools/unattended/unattended.sh` and `write_ask_views`.
  Red when: it exits 0, which is the incident this unit exists for passing again.
  figure: the parents and base are tracked history, read 2026-10-04 (§4 Evidence).
- **AC2** — When `python tools/lexicon/lexicon.py --merge-losses ac65de998..35438ba0a` runs, it exits
  0 and its summary line reads one merge graded and zero losses.
  Red when: it names `verb_review`, whose definition line changed and whose name survived.
  fixture: the range is tracked; its cleanness is inferred from a line probe at spec time and is
  first observed through the mode at build.
- **AC3** — When `python tools/lexicon/lexicon.py --merge-losses <range>` runs in a fixture
  repository under `%TEMP%` whose `.lexicon.conf` arms `sh`, over a merge that resolves a conflict in
  one file to side A and loses side B's added `fb`, it exits 1 naming `fb`; the same merge keeping
  both exits 0; with `superseded: fb -> fa` in its message it exits 0 and counts one superseded; with
  `superseded: fb -> nothere` it exits 1 naming `nothere`.
  Red when: any of the four reverses.
  fixture: built by the build pass; the tree holds none today.
- **AC4** — When the same `python tools/lexicon/lexicon.py --merge-losses <range>` runs per case in
  that fixture: a commit re-adding `fb` after the losing merge makes the range ending at that commit
  exit 0 and count one restored; a merge moving `fa` to a second file exits 0; a merge that takes out
  a function both parents carried from the base exits 1; a merge lacking a function one parent took
  out since the base exits 0.
  Red when: the restore does not clear it, or the both-sides loss passes.
- **AC5** — When the mode runs in a fixture whose `.lexicon.conf` declares every language `dark`, it
  exits 2 and prints `DEAD PROBE`.
  Red when: it exits 0, the reassuring zero of a reader that read nothing.
- **AC6** — When a raw `git push origin main` of AC3's losing merge runs from a fixture clone whose
  `core.hooksPath` is this tree's `.githooks`, the push is refused, `<git-dir>/pre-push-refusal`
  starts with `merge-loss`, and `git ls-remote origin main` is unchanged.
  Red when: the token is `raw-push` or the remote moved, which is the base hook's behaviour.
- **AC7** — When the same push carries the merge with a valid `superseded:` line, the refusal token
  is not `merge-loss` (the hook proceeds to its later `raw-push` refusal).
  Red when: `merge-loss` refuses a superseded merge.
- **AC8** — When `bash tools/push-main.sh --prepare --slug fx` runs in a fixture clone whose branch
  carries AC3's losing reconcile merge, it exits 1 naming `fb`, and `git rev-parse` of the branch
  equals its value before the call, with the branch checked out.
  Red when: the branch moved to the prepared merge, the base lander's behaviour.
- **AC9** — When `grep -n -i 'does not see' tools/lexicon/lexicon.py .githooks/pre-push` runs, each
  file shows the stated blind spots: body-level loss under a surviving name, unarmed languages, a
  loss masked by a same-named definition, octopus merges.
  Red when: either header is missing, so a green push reads as semantic coverage.
- **AC10** — When AC1's `python tools/lexicon/lexicon.py --merge-losses 01c22e155~1..01c22e155` runs,
  its summary line prints its seconds.
  Red when: the figure exceeds 30, the ceiling a push-time precondition may cost.
  figure: PINNED ceiling; the cost itself is derived per run by the summary line.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` · `lexicon selftest` · `lexicon naming predicates` · `pre-push self-test` · `push-main self-test` · `kit version markers` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/lexicon/selftest.py · a fixture merge resolving a conflict to one side, against the base lexicon with no such mode · none
New arm: .githooks/pre-push.test.sh · a raw default-branch push of that merge, against the base hook · none
New arm: tools/push-main.test.sh · --prepare over a branch carrying that merge, against the base lander · none

## 8. Open questions

- **F1 — What may `<successor>` name?** Options: any free text; a definition at the merge or the
  literal `none`; a definition at the merge only. Free text and `none` make the escape a paste.
  Recommendation: a definition at the merge only; a deliberate removal keeps the definition through
  the merge and takes it out in a following non-merge commit, whose diff shows the act.
  RESOLVED (agent, 2026-10-04, delegated): a definition in the merge's tree only.
- **F2 — Key a loss by `(path, name)` strictly, or clear a name defined elsewhere in the merge?**
  Strict catches a loss masked by a same-named definition and reds every move; clearing accepts
  moves and can mask a loss of a common name. Recommendation: clear, and print the masked count.
  RESOLVED (agent, 2026-10-04, delegated): clear by name, counted as masked and printed.
  Narrowed at rev-4 by veto 1, since the bare-name form fails AC1: the name clears only at a path
  the carrying parent did not define it in (§9).
- **F3 — Judge each merge alone, or clear a loss the range tip has restored?** Alone, a loss on a
  branch can be cleared only by rewriting the merge; with tip clearing, one restore commit is the
  remedy and the refusal loop terminates. Recommendation: clear at the tip, counted as restored.
  RESOLVED (agent, 2026-10-04, delegated): a name defined at the range tip clears, counted.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the report's `[B#11]` and Q3 rank 1, node d's ask 26
  read on its branch, and `01c22e155` re-observed at its parents.
- rev-2 · 2026-10-04 · §3 gains the hands-off edge to `TOOL-aMendedFleet-65`, which declares consuming this unit's resolver in `tools/push-main.sh` (check 12 edge join).
- rev-3 · 2026-10-04 · §4 · Files touched claimed disjointness from `TOOL-aMendedFleet-6`'s lexicon
  templates and `.gitattributes`; that unit's rev-1 touches neither and shares
  `tools/lexicon/selftest.py` with this one, so the line now names the shared files. S7 and §7: the
  three Python definitions move `memory/map/generated/symbols.json`, which the build's other
  Python-adding units declare with the coverage leg and this spec omitted.
- rev-4 · 2026-10-05 · build · S2, §4's rule, §5's risks line and §8 F2: `masked` and `restored` clear a name only at
  a path the carrying parent did not define it in, or at the lost path itself for `restored`. Built
  as rev-3 said, AC1 exited 0 with `masked=1`: the driver suite's stub `write_ask_views()` in
  `tools/unattended/unattended.test.sh`, present at the second parent and at the merge, masked the
  very loss this unit exists for. Also: `.githooks/pre-push.runlog.test.sh` joins the files touched,
  because its exit table must name the new `merge-loss` refusal site.

## 10. Reuse audit

The seams extended are `lexicon.extract_text` and `resolve_extractor` in `tools/lexicon/lexicon.py`
(the one definition reader), the straggler-guard block's resolve-then-run shape and `write_refusal`
in `.githooks/pre-push`, and `cmd_prepare`'s unmoved-branch refusal in `tools/push-main.sh`. The
batched blob read copies the pattern of `_read_defs_at_sha` in `tools/drift-audit/drift_report.py`
rather than importing it, for the reason §4 rejects that home; the extractor itself is shared.
`python tools/codebase-map/reuse_lookup.py "refuse a merge that drops a function definition one
parent added"` ranked name-stem neighbours only (`merge` in `merge-rows.py`, `read_merge_heads` in
`transition_audit.py`) and printed `unscanned layers: .sh`, so it cannot see either shell seam; both
were found by reading the hook and the lander. Where the brief and the tree disagree: the brief
calls node d's ask the same mechanism, and its text on `origin/branch/unattended-build-closing-f90fd9`
is line-level; node d built nothing for it, so there are no bytes to reuse.
`python tools/memory-recall/query.py` returned the charter's §1 Landing sentence ("diff the merge
against BOTH parents") in every archived template version, and no record of a merge-loss check.

Recall terms used: merge reconcile auto-took both parents dropped definition superseded pre-push lander refusal data loss
