# TOOL-dDeclaredLoop-93 — 92 AC16 states the push-merge-tree-fatal plant's exit as 1, the code every sibling states

**Status:** INPROGRESS · rev-3 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 47 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-93-deviation-931.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-93-deviation-931.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-93-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-93-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-93-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-93-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-93-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-93-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-93-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-94 |

<!-- /gen:spec-records -->

## 1. Goal

The round-10 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-91-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**. The grounding lens found the same contradiction as
id 11, kept at MEDIUM as item M9; that id is a scope item of `TOOL-dDeclaredLoop-94`, the round's minors
batch, and is not this unit's.

At rev-2, `TOOL-dDeclaredLoop-92` AC16 gave the `push-merge-tree-fatal` plant of `guard.py --fixture`
exit 0, while 81 AC3, 83 S2 and 88 gave it 1, its refusal verdict. No build satisfied both.

At rev-3 the restatement is written: 92's rev-5 re-ground states AC16 with exit 1, so S1 is settled
(§3). What this unit still owes is the observation that the agreement holds once 92 is built: the
plant exits 1 with 92 S17's `OSError()` row in its output (S2), and every exit code the build's specs
state for that command is 1 (S3). The pass writes no file of the tree. It builds immediately after 92,
at order 47, and closes on AC1 to AC3.

## 2. Scope (IN)

- **S2** — The built plant exits 1. At this unit's pass, after 92 S17 is built,
  `python guard.py --fixture --plant push-merge-tree-fatal` in `tools/loop/` exits 1 and prints both
  `the clean re-merge failed: 128`, 81 AC3's row, and `the clean re-merge failed: start failed: OSError`,
  92 S17's `start failed, no message` row. The plant exits 1 at HEAD, and 92 AC16 itself owes exit 1,
  so no code moves in this pass. Observed by AC2.
- **S3** — Every exit code that a spec of this build states for that command is 1. The claim population
  is the probe in §4 "The exit-claim probe", run over `memory/builds/dDeclaredLoop/spec/`; 92 AC16's own
  range is the claim the high named. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- **S1, settled at HEAD.** Rev-2's S1 ordered 92 AC16 restated to exit 1 in a rev bump of 92. The 92
  spec at rev-5 already reads `python guard.py --fixture --plant push-merge-tree-fatal` in `tools/loop/`
  exits 1, with its `start failed, no message` row naming `the clean re-merge failed: start failed: OSError`
  (§4 Evidence), and its hands-off bullet to this unit says so. This unit writes no rev bump of 92, and
  AC1 keeps observing the range.
- Id 11, the same defect at MEDIUM: `TOOL-dDeclaredLoop-94` names 88 S18 and AC18 in 92 S17.
- The report's left-shift gate, a `tools/check-spec-tokens.py` join that fails when one command carries
  two exit codes across a build's specs. That is a second mechanism in a governance tool outside the
  loop kit (BUILD-METHOD M2). The class is recorded at the close, and AC3 is this instance's probe.
- AC16's other halves: the `build_failure_detail` arguments and the multi-line detail (ids 13 and 29) are
  `TOOL-dDeclaredLoop-94`'s.
- The plant's other rows: the rc-128 rows 81 and 86 own and the signal row 86 S22 owns. This unit reads
  the rc-128 line and changes neither.
- Any code edit to `tools/loop/guard.py`. Rev-2 restored exit 1 there only where 92's pass had left the
  plant exiting 0; 92 AC16 at rev-5 owes exit 1, so 92 cannot close in that state.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-92` — AC16 as rev-5 states it with the plant's exit 1, and the `OSError()` row of the `push-merge-tree-fatal` plant that S17 builds, which S2 observes (the round-10 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-94` — 92 AC16 as 92 rev-5 states it, whose `build_failure_detail` calls and range greps that unit completes (the round-10 spec audit's ids 4, 11, 13, 20, 29)
- **hands-off** `TOOL-dDeclaredLoop-96` — §4's exit-claim probe, AC1 and AC3, which that unit restates (the round-11 spec audit's ids 3, 4, 12)

## 4. Design

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every read is of
`branch/unattended-declared-loop-d56bf0` at `af5996d3d`, its tree written by `git archive` into the run's
scratch directory, since this worktree is cut from main, which lacks the loop kit. The plant ran in that
extracted tree after a scratch `git init` and one commit, since `guard.py` reads its own repository.

- 92 rev-5 AC16 states the plant exits 1 and names its `start failed, no message` row
  (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md`, §6 AC16). AC1's two greps
  over its range print 0 for `exits 0` and 1 for `exits 1`.
- 81 AC3 (CLOSED) states the plant exits 1 printing `the clean re-merge failed: 128 fatal: fx stand-in`.
  83 S2, 86 AC22, and claims in 75, 82, 84 and 85, each CLOSED, state exit 1. 88 at rev-6 (CLOSED) holds
  S18 as a settled row naming exit 1 in `run_selftest`'s owed map, and holds no AC7 or AC18; its S6 and
  S7 row says `guard.py --fixture` takes exactly one `--plant` and `tools/loop/guard.py#main` refuses it
  bare.
- `tools/loop/guard.py#run_selftest` owes 1 for `push-merge-tree-fatal`.
  `tools/loop/guard.py#run_guard_plant` grades its `graded` row on `128 fatal: fx stand-in` and its
  `start failed` row on an `OSError("fx stand-in")`.
  `tools/loop/guard.py#build_failure_detail` spells an `OSError` as `start failed: %s` of the exception.
- `python guard.py --fixture --plant push-merge-tree-fatal` in `tools/loop/` exited 1, printed
  `6 of 6 scenario(s) held · all held` and `the clean re-merge failed: 128 fatal: fx stand-in`, and took
  8.2 s PINNED wall time. It printed no `start failed: OSError`: that row is 92 S17's, unbuilt at HEAD.
- The probe below, run over the spec folder with rev-2 of this spec in it, found 14 PINNED claims: one
  each in 75, 81, 82, 85, 86 and 92, two each in 83 and 84, and four in this spec. It printed the set
  `{1}`. With rev-3 in the folder it found 13 PINNED claims, three of them this spec's, and the same
  set.

### The exit-claim probe

```
claim = re.compile(r"--plant push-merge-tree-fatal`((?:(?!--plant|\. |; ).){0,60}?)\bexits (\d+)")
for each *.md under memory/builds/dDeclaredLoop/spec/:
    text = the file with every whitespace run squeezed to one space
    collect m.group(2) for every claim.finditer(text)
print the number of claims and the set of codes
```

The plant name must be followed by its closing backtick, so `push-merge-tree-fatal-unparseable-parent`
is not counted. A claim ends at a sentence end or at a second `--plant`, so an exit stated for another
plant later in the same sentence is not counted.

### Write set

None under `tools/` and no spec. The pass runs AC1 to AC3; the close's records and the build README's
regions are the main loop's and the generator's. The pass mints no public module-level `def`, so
`memory/map/generated/symbols.json` does not move.

### Files touched (estimate)

None under `tools/`.

### Alternatives rejected

- **Naming no exit code in AC16, as the report's other option.** The exit code is the plant's refusal
  verdict. Leaving it out of AC16 drops an observation without closing the defect class. 92 rev-5 states
  1, and AC1 and AC3 observe it.
- **Flipping 81 AC3, 83 S2 and 88's row to exit 0.** A refusing plant that exits 0 reads as a pass to
  the `loop guard fixtures` leg, and every CLOSED claim would move to agree with one wrong one. Each of
  them is frozen besides.
- **Settling S2 and S3 with S1 and closing the unit unbuilt (F3 option b).** The `start failed: OSError`
  line S2 observes does not exist until 92 S17 is built, so HEAD cannot show it.

## 5. Production-readiness checklist

- security — keeps the plant's refusal visible as a non-zero exit, so a merge the guard refuses is never
  read as clean.
- perf / scale — one plant run, about 8 s PINNED 2026-11-17, and a probe of one folder.
- error / empty / loading states — the `OSError()` row keeps 92 S17's non-empty detail.
- observability — the plant's refusal lines are 92's and 81's; this pass reads them.
- risks — `TOOL-dDeclaredLoop-94` and `TOOL-dDeclaredLoop-96` rewrite AC16, the probe and AC3 after this
  unit; each keeps exit 1, and AC3 re-runs at their passes. The sweep below names every reader.
- testing — AC1 to AC3 as a grep, a plant run and a probe over the spec folder.
- migration — none: no stored data.
- user docs — none: `grep -rln "push-merge-tree-fatal" help/` prints nothing at HEAD, and no verb, flag
  or usage row is added.

### The sweep

The pass writes no file, so no function, constant or fixture moves. The readers below read this spec's
text, which the re-ground commit lands. Each count is DERIVED by the command beside it, run on the
branch tip.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| this spec's claims in the probe's population | the probe of §4, `python -I` over `memory/builds/dDeclaredLoop/spec/` | each claim this spec states is exit 1; the set stays `{1}` |
| AC1 and AC3, by number | 94 AC10, which re-runs 93 AC3's probe; 96 S2, S3, AC2 and AC3, which restate the probe and AC3 and have 94 AC10 re-run 93 AC1's grep; `grep -n "93 AC1\|93 AC3" memory/builds/dDeclaredLoop/spec/*.md` | both ids and the probe's text are kept |
| the probe's section | 96 AC2's ranges `### The exit-claim probe` to `### Write set` and AC3's range to `## 7` over this spec | both headings are kept; the probe's range holds no `non-zero` and AC3's range no `exit code of 0`, as 96 AC2 baselines |
| the probe's population | 96 AC2 owes a claim from 88; 88 at rev-6 holds none in the probe's form | 96's own re-ground answers it; this unit writes neither spec |
| 83 §4 Evidence's citation of this spec's probe | 83 is CLOSED and frozen | the probe and the `{1}` set it cites are kept |
| the edge with 92 | 92 rev-5's hands-off bullet to this unit | the consumes-from bullet above mirrors it |
| this spec's positional row | `memory/project/positional-refs.txt`, one row naming this spec, `grep -c "dDeclaredLoop-93.md" memory/project/positional-refs.txt` | its value `BUILD-METHOD M2` is kept in §3 |
| the build README's units row | `memory/builds/dDeclaredLoop/README.md`, which renders rev-2 | the dispatcher's index regeneration renders rev-3 |
| the `loop guard fixtures` leg | `tools/gate-legs.json`, whose argv runs `guard.py --selftest`, its 300 s PINNED ceiling and the 140 s PINNED row of `tools/run-gates/selftest-budgets.txt` | the pass writes neither and adds no plant row |
| the lexicon offender pin | `tools/lexicon/lexicon.py` | no new function or constant name |
| refusal ceilings and families | `tools/memory-tree/check-arms.py` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | it names no path under `memory/builds/` or `tools/loop/` |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps, help anchors and usage rows | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no shipped file, leg, step, verb or flag |

Order: this unit reads 92 S17's code, built at order 46, and 92 AC16 as 92 rev-5 states it. Unit 91,
building at order 45, writes `tools/loop/loop_lib.py`, which this pass neither reads nor writes. Units
94 at order 48 and 96 after it read this spec's probe and criteria as rev-3 states them.

## 6. Acceptance criteria

- **AC1** — When `awk '/^- \*\*AC16\*\*/,/^## 7/'` over
  `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-92.md` is piped to
  `grep -c "exits 0"`, it prints 0. Piped to `grep -c "exits 1"`, it prints at least 1.
  Red when: AC16 requires exit 0 again, staged by restoring `exits 0` in a scratch copy of the 92 spec.
  figure: the first grep prints 0 and the second 1 at HEAD, PINNED 2026-11-17.
- **AC2** — When `python guard.py --fixture --plant push-merge-tree-fatal` runs in `tools/loop/`, it exits 1,
  and its output holds `the clean re-merge failed: 128` and
  `the clean re-merge failed: start failed: OSError`.
  Red when: 92 S17's `OSError()` row is absent, as at HEAD, or the plant's refusal exits other than 1.
  figure: at HEAD it exits 1 and holds the first line and not the second, PINNED 2026-11-17.
  fixture: the second line exists only once 92 S17 is built, at order 46.
- **AC3** — When a `python -c` probe runs §4's exit-claim pattern over every `*.md` under
  `memory/builds/dDeclaredLoop/spec/`, it counts at least five claims and prints the set `{1}`.
  Red when: any spec of the build states another exit code for the command, staged by restoring
  `exits 0` in a scratch copy of the 92 spec.
  figure: 13 PINNED claims and the set `{1}` with rev-3 in the folder, 2026-11-17. The count at
  observation time is DERIVED from the folder.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop guard fixtures`, which runs `guard.py --selftest`, every plant, `push-merge-tree-fatal`
among them. This pass adds and moves no arm: the plant's exit 1 is 81's arm, its `OSError()` row 92's,
and S2 only observes them.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — State exit 1 in AC16, or name no exit code (id 1)?** (a) exit 1, as 81 AC3 states; (b) the
  `OSError()` row's line alone. The report judged both sound. (a) keeps the refusal verdict observed and
  satisfies every criterion (b) would; 92 rev-5 wrote (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F3 — With S1 settled at HEAD, does the unit still build?** (a) yes, as an observation pass at order
  47 that writes no file and closes on AC1 to AC3; (b) settle S2 and S3 with S1 and close the unit
  unbuilt. The `start failed: OSError` line of S2 exists only once 92 S17 is built, and the run keeps
  this unit's order and status. Recommendation: (a).
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-10 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-96, written by the round-11 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 AC1 AC2 AC3 · re-grounded on the code at
  `branch/unattended-declared-loop-d56bf0` by the 2026-11-17 re-ground: S1 settled by 92 rev-5's AC16;
  S2 an observation with no code write; S3 names AC1; §4 Evidence re-read, the probe's note re-worded
  off 88's former AC7; §5's sweep added; AC1 to AC3 figures re-pinned; F3 added and every fork re-marked.

## 10. Reuse audit

The seam is 92 AC16 and 81's `push-merge-tree-fatal` plant of `tools/loop/guard.py`, observed in place.
No second plant and no new checker is minted.
`python tools/codebase-map/reuse_lookup.py "collect every exit code a spec states for one command and compare them"`,
re-run on the branch tip 2026-11-17, ranked `resolve_compare_base`, `parse_spec_h1`, `read_spec_revisions`
and `build_spec_path_re` first, none of which reads an exit claim from a spec's prose, so no existing seam
fits the probe and it stays a criterion's `python -c` rather than a tool. The memory-recall query at
rev-1 returned the round-10 report's H1, 81's AC1 and 92's checklist.

Recall terms used: push-merge-tree-fatal exits AC16 guard plant exit code sibling criteria two-answers-to-one-question refusal convention
