# TOOL-aRoutedQuill-11 — check-wiring takes the write gate's armed verdict from the gate itself

**Status:** SPECCED · rev-1 · 2026-10-10 · node a · Tier-2 · base 5a836bf0 · streams tooling · order 9 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-10-prompt-TOOL-aRoutedQuill-11-spec-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-11-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`check_routed` in `tools/check-wiring.sh` prints `ok routed` for a `.memory-tree.conf` that
carries no `MEMORY_ROOT`, while the gate it reports on refuses every write under that conf. This
unit makes the arm take the armed-or-unarmed verdict from the gate's own reader, so the session
reporter and the gate give one answer, and pins that agreement with a parity arm.

## 2. Scope (IN)

- **S1** — `tools/hooks/scratch-guard.js` exports `checkUnarmed` beside the `readConfKey` it
  already exports, with no change to either function's body. Observed by AC3.
- **S2** — `check_routed` reads `MEMORY_ROOT`, `ROUTED_PATHS` and `ROUTED_COMMIT_CUTOFF` with one
  `node -e` call that requires the gate file the settings dispatch, reads each key through
  `readConfKey`, and returns `checkUnarmed`'s verdict with the two values. The arm sources nothing
  and defaults nothing. Observed by AC1, AC2 and AC6.
- **S3** — When `checkUnarmed` returns a reason, the arm prints that reason byte for byte as
  `UNWIRED  routed    — <reason> in <conf>, so the write gate is UNARMED ...` and counts it. The
  shape rules the gate grades (absolute, `..`-climbing, covering `MEMORY_ROOT`) are answered by the
  gate's verdict alone. Observed by AC1 and AC2.
- **S4** — On an armed gate verdict the arm keeps grading the ownership leg's two extra rules, the
  cutoff as an ISO date and each entry naming something tracked, over the values `readConfKey`
  returned, and words those lines as the leg's refusal rather than the gate's. Observed by AC2.
- **S5** — When the verdict cannot be read (no `node` on PATH, no resolvable gate file, or a gate
  copy that exports no `checkUnarmed`), the arm prints one `skip     routed    — <cause> ...` line
  naming the cause and counts nothing (F1). Observed by AC4.
- **S6** — `tools/check-wiring.test.sh` adds `MEMORY_ROOT=memory` to the three routed fixtures
  that lack it, adds an arm for a conf with no `MEMORY_ROOT`, and adds the parity arm: one set of
  confs fed to both `checkUnarmed` and the checker, asserting the checker's line carries the gate's
  reason exactly when the gate gives one. Observed by AC5.
- **S7** — The header comment above `check_routed` states that the gate half is the gate's own
  verdict, and that the ownership leg reads `MEMORY_ROOT` with a default the gate does not apply.
  NOT OBSERVED — a comment is prose, and no criterion can grade its truth beyond its presence.

## 3. Non-goals (OUT)

- M4 and L2 of the round-1 closing review: which `scratch-guard` group counts as "the write gate is
  wired", and the wording of the no-conf branch. Both stay as they are here.
- The other `MEMORY_ROOT` readers: `read_memory_root` in the kickoff engine (M1) and the ownership
  leg's `tree_lib.parse_conf_line`. Their grammar is the minors batch's question.
- Any change to the gate's verdict, its reasons or its evaluation order. The gate is the reference
  this unit reads, never a thing it edits beyond one export.
- A shell fallback reader for the no-`node` case (F1 says why).

### Edges

- **hands-off** `TOOL-aRoutedQuill-12` — M4 and L2, the two remaining defects in `check_routed`:
  the any-group `gated` reading and the no-conf wording. That unit edits the function this one
  rewrites, so it builds on this unit's shape.

## 4. Design

### Data model

Code references are at HEAD 4edeb467 on the build branch. Today the arm sources the conf in a
subshell and reads `${MEMORY_ROOT:-memory}` (`tools/check-wiring.sh:1455`), then re-implements the
absolute, `..` and covers rules in shell (`:1468-1480`). The gate reads the same keys with
`readConfKey` (`tools/hooks/scratch-guard.js:770`) and refuses through `checkUnarmed`
(`:868`), whose first rule is `MEMORY_ROOT is blank or absent`. Two readers, two answers.

`checkUnarmed` is NOT exported today: `module.exports` at `scratch-guard.js:1115` carries
`readConfKey` and not `checkUnarmed`, measured 2026-10-10 by a `node -e` probe that failed with
`g.checkUnarmed is not a function`. S1 adds the one name.

### The one reader

The arm resolves the gate file the way `check_scratch_guard` does: the hooks kit's
`scratch-guard.fragment.json` through the receipt and then the kit prefix (`first_of` over
`resolve_receipt_path` and `resolve_kit_file`), and its `hook_path` through
`resolve_fragment_hook`. That is the copy the settings dispatch, which in an adopter is the wired
copy and not the kit copy. No sibling kit is named by literal.

One call, run from the repo root:

```bash
node -e '<require path.resolve(argv[1]); read argv[2] as utf8; print reason \037 routed \037 cutoff>' \
  "$hookjs" "$conf"
```

`null` from `readConfKey` prints as empty. A value cannot hold `\037` or a newline, because
`readConfKey` reads one line per assignment. A non-zero exit, or output with no `\037`, is the S5
skip and names the cause from stderr's first line.

Then, in order:

1. A non-empty reason is the S3 line. Nothing else is graded, because an unarmed gate makes the
   leg's rules moot for this report.
2. Otherwise the cutoff: blank, then not an ISO date, as today, worded for the leg.
3. Otherwise each `ROUTED_PATHS` entry, split on whitespace as the gate splits it, normalised as
   today, must name something tracked, as today, worded for the leg.
4. Otherwise `ok routed`, unchanged.

The absolute, `..` and covers rules in shell are not carried forward: an armed verdict from
`checkUnarmed` already means none of them holds, so keeping them would be the second reader this
unit exists to end.

### Line shapes

| case | line |
|---|---|
| gate unarmed | `UNWIRED  routed    — <reason> in <conf>, so the write gate is UNARMED and refuses every Edit, Write, MultiEdit or NotebookEdit here except to that file. Fix: <as today>` |
| leg rule | `UNWIRED  routed    — <why> in <conf>, so the ownership leg refuses. Fix: <as today>` |
| unreadable | `skip     routed    — <cause>, so the gate's own armed verdict cannot be read here` |

The two `UNWIRED` prefixes keep the bytes the existing fixtures grep, `ROUTED_PATHS is blank` and
`ROUTED_PATHS entry <e> `, so those arms keep their meaning.

### Inventory

No identifier is minted. The arm stays one function, so neither the lexicon's verb table nor the
codebase map gains a symbol. The export adds no name: `checkUnarmed` already exists in the file.
The new test arms carry the label prefix `RQ11`.

### Files touched (estimate)

`tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `tools/hooks/scratch-guard.js`

### Rollout

Touching `tools/hooks/scratch-guard.js` moves shipped bytes, so the hooks kit's version moves in
every carrier the `kit epoch` leg and the `kit version markers` leg name, once, after the last edit.
If `tools/codebase-map/gen_map.py --check` reports the map stale, regenerate it in the same commit.

### Alternatives rejected

- **Read `${MEMORY_ROOT-}` in shell and refuse it blank** (the corrected M2 fix). It closes the one
  case and keeps two readers. A conf spelling the shell and `readConfKey` read differently, for
  example a value built from a variable, still splits them. Rejected for the brief's one-reader
  mechanism, which closes the class.
- **Call the exported `checkRouted` with a synthetic payload.** Its step 5 returns `null` for the
  conf target and a deny for any other, so the reason is only recoverable by parsing deny prose.
  Rejected: it couples the checker to the deny's wording and to the card.
- **Default `MEMORY_ROOT` to `memory` in the gate** (finding 16's proposal). Judged UNSOUND by the
  skeptic, and TOOL-aRoutedQuill-2 §4 rejects it on purpose.

## 5. Production-readiness checklist

- security — the arm stops sourcing the conf, so a conf line is no longer executed by this check.
  The `node -e` program is a fixed literal and both inputs are passed as argv, never interpolated.
- perf / scale — one `node` start per run, about 0.5 s on node a (PINNED, measured 2026-10-10), on a
  checker that took 82 s whole on this tree the same day.
- error / empty / loading states — every failure of the call is the S5 skip naming its cause; an
  absent conf keeps today's branch untouched.
- observability — the gate's reason is printed verbatim, so a reader can grep one string across the
  gate's deny and the checker's line.
- risks — an adopter running the hooks kit's checker with no `node` loses the leg-half grading too,
  since the keys are read only through the gate. Accepted in F1: the gate itself cannot run there.
- testing — S6's arms in `tools/check-wiring.test.sh`, the parity arm included; run at the close.
- migration — N/A — no data or conf shape changes; a conf that was armed stays armed.
- user docs — N/A — check-wiring's lines are operator output with no `help/` page.

## 6. Acceptance criteria

Each criterion runs in a frozen clone of the branch tip at the end of the build pass, made with
`git clone --local -q "$PWD" "$TEMP/rq11"` from the worktree root, with the conf edited there and
never in the worktree. `$TEMP/rq11` is removed afterwards.

- **AC1** — When `.memory-tree.conf` in `$TEMP/rq11` has its `MEMORY_ROOT=` line deleted and
  `bash tools/check-wiring.sh --check` runs there, the routed line reads
  `UNWIRED  routed    — MEMORY_ROOT is blank or absent in .memory-tree.conf, so the write gate is UNARMED`
  and the exit code is 1.
  Red when: the arm still defaults the key to `memory` and prints `ok       routed`.
  cost: about 80 s per checker run on node a.
- **AC2** — When three confs are written in turn to `$TEMP/rq11/.memory-tree.conf`, namely
  `MEMORY_ROOT=""`, then `export MEMORY_ROOT=memory` with `ROUTED_PATHS="memory/"`, then the
  repo's own conf unchanged, and for each one both
  `node -e "const g=require(require('path').resolve(process.argv[1])),b=require('fs').readFileSync(process.argv[2],'utf8');console.log(g.checkUnarmed(g.readConfKey(b,'MEMORY_ROOT'),g.readConfKey(b,'ROUTED_PATHS')))" tools/hooks/scratch-guard.js .memory-tree.conf`
  and `bash tools/check-wiring.sh --check` run, the routed line carries the node line verbatim
  when it is non-empty, and reads `ok       routed` when it is empty.
  Red when: any of the three pairs disagrees, or the third case is not `ok` (the liveness half).
  cost: three checker runs, about 4 min on node a.
- **AC3** — When `node -e "process.exit(typeof require(require('path').resolve(process.argv[1])).checkUnarmed === 'function' ? 0 : 1)" tools/hooks/scratch-guard.js`
  runs at the worktree root, it exits 0.
  Red when: `checkUnarmed` is missing from `module.exports`.
- **AC4** — When `bash tools/check-wiring.sh --check` runs in `$TEMP/rq11` with `PATH` rebuilt
  without every directory holding a `node` executable, the routed line starts
  `skip     routed    — ` and names `node`, and no `UNWIRED  routed` line is printed.
  Red when: the arm prints `ok`, an `UNWIRED` line, or nothing for the routed arm.
  cost: one checker run, about 80 s on node a.
- **AC5** — When `grep -c 'RQ11' tools/check-wiring.test.sh` runs, it prints at least 2, and
  `grep -c 'MEMORY_ROOT=memory' tools/check-wiring.test.sh` prints at least 3.
  Red when: the parity arm or the absent-key arm is missing, or a routed fixture still lacks the key.
  The arms' verdicts are the close's, under `New arm:` in §7; this criterion grades their presence.
- **AC6** — When `sed -n '/^check_routed()/,/^}/p' tools/check-wiring.sh | grep -cE 'MEMORY_ROOT:-|^[[:space:]]*vals=\$\( \. '`
  runs, it prints 0.
  Red when: the arm still defaults the key or still sources the conf.

## 7. Gates

`check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `hook destinations (every declared hook path ships)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-wiring.test.sh · covers AC1 AC2 · a conf with no MEMORY_ROOT, and the parity set fed to checkUnarmed and to the checker · none

## 8. Open questions

- **F1** — When the gate's verdict cannot be read, what does the arm print?
  Options: (a) a `skip` line naming the cause; (b) an `UNWIRED` line; (c) fall back to reading the
  keys in shell. (c) restores the second reader this unit removes, which is the defect's class.
  (b) counts a state the operator may not be able to change and calls the gate unarmed when no
  verdict was read. (a) announces itself, as the charter's §7 requires of a skip, and is honest
  because a gate with no `node`, or no gate file, refuses nothing.
  RESOLVED (agent, 2026-10-10, delegated): (a), a `skip` line naming the cause.

## 9. Revision log

- rev-1 · 2026-10-10 · initial draft, from the spec brief and H2 and M2 of the round-1 closing
  review, with the skeptic's corrected fix for finding 16.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "checker takes the write gate's armed verdict from the gate's own conf reader"`
ranked name-token neighbours only (`read_text`, `load_conf`, `parse_conf`, `read_conf`), none of
them the gate's reader, so the probe found no seam by name. The seam this unit extends is the
gate's own pair, `readConfKey` and `checkUnarmed` in `tools/hooks/scratch-guard.js`, already
required from outside the file by `tools/hooks/agent-cap.js:1865` for `readConfKey`. The gate
file is located with `resolve_fragment_hook` in `tools/check-wiring.sh`, the resolver the
scratch arm already uses. Where the probe and the source disagreed: the review's fix says to
require `checkUnarmed`, and source showed it is not exported, which is S1.

Recall terms used: `--terms "scratch-guard check-wiring checkUnarmed readConfKey MEMORY_ROOT ROUTED_PATHS armed unarmed one-reader parity conf-grammar routed"` with the question
"how should a checker read the write gate armed verdict so it agrees with scratch-guard", which
surfaced the round-1 review's H2, TOOL-aRoutedQuill-2 and TOOL-aRoutedQuill-4.
