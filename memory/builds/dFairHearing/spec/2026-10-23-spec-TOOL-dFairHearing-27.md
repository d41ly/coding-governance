# TOOL-dFairHearing-27 — the spec audit of units 20 to 23, its 31 minors: criteria a correct build can pass, refusals that name their cause, and the readers a move leaves behind

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 21 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-27-deviation-271.md](../build/2026-10-23-build-TOOL-dFairHearing-27-deviation-271.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-25-promoted-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-26 |
| [2026-10-23-prompt-TOOL-dFairHearing-27-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-27-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-27-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-27-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-4-edge-fix-brief.md) | research | TOOL-dFairHearing-4 TOOL-dFairHearing-18 TOOL-dFairHearing-25 |
| [2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md) | spec-audit | TOOL-dFairHearing-4 TOOL-dFairHearing-14 TOOL-dFairHearing-25 TOOL-dFairHearing-26 |

<!-- /gen:spec-records -->

## 1. Goal

One batch unit closes every MEDIUM and LOW finding that the spec audit of units 20 to 23 confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md`). That is
31 report ids: 24 MEDIUM, items M1 to M19, and 7 LOW, items L1 to L7. Each id is its own §2 item.
The minors land on four units, `TOOL-dFairHearing-20`, `-21`, `-22` and `-23`, so this unit builds
after every unit of the build. It does three things: makes each corrected statement true on the
code those units built, gives each refusal its named cause, and moves the readers that a rename or a
moved rule leaves stranded. A criterion this unit supersedes is named by the hands-off bullet in that
unit's §3, and that unit's acceptance ledger records it superseded here (`TOOL-dFairHearing-23` §8 F7's
form).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it. Where a report item merges ids, each id is its own item, and the later ids point at the first
one's mechanism.

- **S1** — id 5 (M1, unit 23, AC1). `tools/workflows/render_lenses.py --markers` prints only the lines
  that carry the `gov:lens-slots` marker. A `gov:lens-optins` literal (unit 23 S14) is outside the
  five-slot count, so a zero-row opt-in literal passes the fan-out leg. This supersedes unit 23 S35's
  "every line matching the renderer's own anchored marker regex".
- **S2** — id 27 (M1, unit 23, AC1). S1's defect from the blast-radius lens; S1 closes it.
- **S3** — id 11 (M2, unit 23, AC2). Unit 23 AC10's absence half reads command lines only. S17's
  warning against `git clone --branch` stays in the README.
- **S4** — id 12 (M3, unit 23, AC3). `tools/workflows/spec-audit-optin.test.sh` carries the
  `FOREIGN_PREFIX_PROBE` stop that its sibling suites carry. `tools/run-gates/foreign-prefix.gov.test.sh`
  holds no `WHOLE_RUN` row for `spec-audit opt-in pack self-test`. This supersedes unit 23 S26's
  `WHOLE_RUN` row and AC17's foreign-prefix half.
- **S5** — id 25 (M3, unit 23, AC3). S4's defect from the blast-radius lens; S4 closes it.
- **S6** — id 13 (M4, unit 23, AC4). `extract_tag_ref`'s no-tag row returns the integer
  `extract_section_ref` returns: a `§<n>`, a `section <n>`, or an S, AC or F item mapped to 2, 6 or 8
  (`tools/workflows/review_replay.py:68-70`, `:100-115`). Only a ref `extract_section_ref` itself
  rejects returns `None`. This supersedes the middle row of unit 23 §4's table.
- **S7** — id 14 (M5, unit 21, AC5). `check_held_out_frozen` normalises the `heldOut` path once, to its
  repo-relative POSIX form through `git ls-files --full-name -- <path>`, before any `<rev>:<path>`
  read. An untracked path refuses. Any git call that exits non-zero refuses with exit 2, naming the
  call and its stderr, and its stdout is never compared. This supersedes the verbatim `<path>` in
  unit 21 S2 and §4.
- **S8** — id 35 (M5, unit 21, AC5). S7's defect from the failure-envelope lens; S7 closes it.
- **S9** — id 15 (M6, unit 23, AC6). `check_gate_token` returns one of three states: resolved, unresolved
  because `legs is None`, or unresolved. `check_invariant` keeps its note on the middle state
  (`tools/memory-tree/gotchas.py:435-437`). `check_ungated` counts the middle state as ungated and
  announces it as a note. This supersedes unit 23 §4's "lifted unchanged".
- **S10** — id 20 (M6, unit 23, AC6). S9's defect from the reuse lens; S9 closes it.
- **S11** — id 39 (M6, unit 23, AC6). `check_ungated` reads tokens from a case-insensitive `gated by`,
  `gated in` or `gated at` match, wherever it falls, across wrapped lines, to the end of its sentence.
  A sentence ends at a full stop followed by whitespace or the end of the paragraph, never at a dot
  inside a backticked token. It also reads the body of a `## Gated by` section. This supersedes unit
  23 S21's single physical line.
- **S12** — id 17 (M7, unit 22, AC7). `tools/hooks/kit.toml` gains `marker_carriers =
  ["{prefix}/workflows/spec-audit-optin.js"]`, and the pack carries a `gov:kit agent-cap@` marker at
  agent-cap's version of that commit. A scoped `govkit update --kits agent-cap` then moves a claimed
  review kit with it (`tools/govkit/govkit.py:1034-1059`, `:9294-9312`). Unit 22's presence check
  stays, for hand copies and hooks-only adopters.
- **S13** — id 18 (M8, unit 22, AC8). The deny message names its remedy by receipt state. When
  `.governance/install.json`'s `kits` claims `review-harness`, the remedy is `govkit update --kits
  review-harness`. Otherwise, or with no receipt, it is `govkit apply --kits review-harness`, because
  `update` refuses a kit the receipt does not claim (`tools/govkit/govkit.py:9287-9293`). The
  hand-copy remedy stays. This supersedes unit 22 S2's fixed first remedy and AC1's string.
- **S14** — id 21 (M9, unit 23, AC9). `tools/workflows/check-verifier-fanout.sh` carries no
  `LENS_SLOTS` assignment, so the number keeps one home, `tools/workflows/check-verifier-fanout.js`
  (unit 23 S42). The shell constant that `TOOL-dFairHearing-13` §4 mints does not survive this unit.
- **S15** — id 23 (M10, unit 23, AC10). One version rule: no commit of this build changes the value of
  an existing version line. A new file's marker carries its kit's version at that commit. The check
  diffs from `git merge-base HEAD main`, never from a fixed sha, so a mint that main lands and a
  re-prepare merges is not read as a hand bump. This supersedes unit 23 S12's "restored to base
  `3708a705`'s value" and AC6's base.
- **S16** — id 24 (M11, unit 23, AC11). The readers of the old slot-count name follow it.
  `tools/check-playbook-parity.sh`'s `lens-array bound` pair reads `LENS_SLOTS` from
  `tools/workflows/check-verifier-fanout.js`, and its stated side is the README sentence on rule 2's
  array-literal bound (`tools/hooks/README.md:180` at base), read wherever unit 16 S7 places it. The
  plants in `tools/check-playbook-parity.test.sh` (:158, :279-281) follow. Both REVIEW-PROTOCOL copies
  at :224 name `LENS_SLOTS` in `check-verifier-fanout.js`.
- **S17** — id 26 (M12, unit 23, AC12). `tools/govkit/subject-pins.tsv` carries a row for
  `spec-audit opt-in pack self-test`, regenerated with `python tools/govkit/govkit.py selfcheck --write`
  once the leg is live (`tools/govkit/govkit.py:3019-3020`).
- **S18** — id 28 (M13, unit 23, AC13). The `gateManifest` name (unit 23 S44) reaches
  `tools/workflows/README.md`'s argument list (unit 8 S9) and the throw that unit 8 AC5's arm expects
  in `tools/workflows/tier2-review.test.sh`.
- **S19** — id 30 (M14, unit 21, AC14). Unit 21's arms raise `ARMS_DECLARED` in
  `tools/workflows/replay_scorer.py`'s runner by the number of arms added, as `review_replay.py:84`
  and `:604-606` hold it. This supersedes the floor field "none" on unit 21's `New arm:` line.
- **S20** — id 33 (M15, unit 22, AC15). `checkOptinPackPresent` resolves the pack in
  `resolve_kit_dir`'s order (`tools/check-kit-versions.sh:69-105`). First comes a
  `.governance/install.json` row whose `source` ends `workflows/spec-audit-optin.js` and whose `path`
  is a file inside the tree. Then comes `<hook dir>/../workflows/spec-audit-optin.js`. A receipt row
  whose `path` is missing denies, naming that path. No row and no probe hit denies as unit 22 S1
  does.
- **S21** — id 34 (M16, unit 22, AC16). The `agent-cap self-test` guard in `tools/gate-legs.json` gains
  `{prefix}/workflows/spec-audit-optin.js`. `memory/guides/SESSION-KICKOFF.md` is re-stamped after
  that edit to its watched file, as unit 23 S28 re-stamps it.
- **S22** — id 36 (M17, unit 23, AC17). The replay recipe in `tools/workflows/README.md` states its
  failure envelope. An existing `$TEMP/<name>` refuses. Every step's exit status is checked. The
  liveness check compares `git -C "$TEMP/<name>" rev-parse HEAD` with `git rev-parse <commit>`. An
  EXIT trap runs `git update-ref -d` on the transient `refs/replay/<name>`, so it is cleared even when
  `git bundle create` fails. This supersedes unit 23 S18's `rev-list --count` check.
- **S23** — id 37 (M18, unit 23, AC18). When `render_lenses.py --markers` exits non-zero, cannot be
  found beside the gate, or has no usable python, the fan-out leg exits 2 with `verifier-fanout: the
  marker predicate did not run (<reason>)`. It never reads that as an empty marker list. `--markers`
  shares the renderer's python floor, so a refusal from either is that named exit.
- **S24** — id 38 (M19, unit 23, AC19). The walker-slice cap of unit 23 S49 is checked on the slices
  that `deriveWalkSlices(items, scenarios, run)` returns for the call's own `run`, so a run-2 band
  over 200 cells throws before the first agent.
- **S25** — id 7 (L1, unit 20, AC20). Unit 20 AC2's absence half reads "no line matching
  `the walk table has [0-9]+ gap`", and AC1's gapped case carries one.
- **S26** — id 8 (L2, unit 20, AC21). The args-header half of unit 20 S4 is observed: the header of
  `tools/workflows/tier2-review.js` names the gap rule and the four null fields.
- **S27** — id 9 (L3, unit 23, AC22). Unit 23 AC20's base-sha half reads the three key-pinning arms'
  own lines, sliced by their labels, never a whole-file `grep -c`. Each of the three arms opens with a
  `// ---- ` header naming its unit and criterion (`TOOL-dFairHearing-2 AC4`, `TOOL-dFairHearing-3 AC5`,
  `TOOL-dFairHearing-9 AC7`), the header form the suite's arms carry
  (`tools/workflows/tier2-review.test.sh:481`).
- **S28** — id 16 (L4, units 21 and 23, AC23). The clone-path reason in unit 21 AC1 and unit 23 §6 is
  an UNVERIFIED platform claim: the audit measured clones succeeding under the scratchpad with
  `core.longpaths` true. Fixtures go under `%TEMP%` by the run mandate's own convention, and no
  product file records the unmeasured limit.
- **S29** — id 29 (L5, unit 23, AC24). `render()` in `tools/memory-tree/gotchas.py` (:447-460) and its
  output `memory/gotchas/INDEX.md` say that the harness acquires the checklist on the diff kind, and
  keep the command for a reader who wants it. Unit 23 AC36's path set includes both.
- **S30** — id 40 (L6, unit 23, AC25). `scan_pairing_sites` exits 2 by name when its `git ls-files`
  read fails or finds no `*.py`, never returning `[]`. Unit 23 AC16 gains a positive half.
- **S31** — id 41 (L7, unit 23, AC26). Unit 23 AC33's and AC35's absence checks read a view of the file
  with comments and string literals blanked, the view S42's count reads. So a rule-2 comment that
  names the old bound does not red a correct build.

## 3. Non-goals (OUT)

- No re-review, and no fold into units 20 to 23: each item makes the corrected statement true and
  reopens no severity.
- No HIGH finding: ids 1 and 10 are `TOOL-dFairHearing-25` and `TOOL-dFairHearing-26`.
- No new gate leg: every arm lands in a suite that exists or that an earlier unit adds.
- No govkit code change: S12 is one descriptor row and one marker line, read by the coupling govkit
  already has.
- No help page: `help/` covers neither the review harness, the scorer factory nor the hooks.

### Edges

- **consumes-from** `TOOL-dFairHearing-20` — `walkRed`'s BLOCKED sentence and the args header, which S25 and S26 observe
- **consumes-from** `TOOL-dFairHearing-21` — `check_held_out_frozen`'s two new checks and its runner arms, which S7, S19 and S28 correct
- **consumes-from** `TOOL-dFairHearing-22` — `checkOptinPackPresent` and its deny message, which S12, S13, S20 and S21 correct
- **consumes-from** `TOOL-dFairHearing-23` — the marker predicate, the recipe, the tag reader, `check_ungated`, `LENS_SLOTS`, `gateManifest`, the version rule and the criteria S1 to S31 correct
- **hands-off** `TOOL-dFairHearing-31` — finding id 34 (item H3) of the round-3 spec audit: the version-line check resolves the bar's base or refuses by name; S15's base sentence and AC10 are superseded by its S1 to S3 and AC1 to AC3, and S15's version rule stands
- **hands-off** `TOOL-dFairHearing-32` — the same audit's minors on this spec, ids 3, 8, 12, 16, 17, 20, 26, 27, 35, 37 and 38: its S22 to S32, each naming what it supersedes

## 4. Design

### Why one unit and not two

A split along the units would put unit 22's minors in one half and unit 23's in the other. M6's
clause 2 refuses it. S21 writes `tools/gate-legs.json`, and S17 regenerates `subject-pins.tsv` from
that same manifest. S13 and S20 reword `tools/hooks/README.md`, the stated side that S16's parity
pair reads. So one half writes a contract the other half reads.

### The fan-out leg's marker list (S1, S23)

```
render_lenses.py --markers <harness>   -> one line number per `gov:lens-slots` marker line, exit 0
                                          a `gov:lens-optins` line is never printed
leg: python unresolved | renderer absent | exit != 0  -> exit 2, "the marker predicate did not run (<reason>)"
```

### The freeze path (S7)

```
rel = git ls-files --full-name -- <path>        # empty -> exit 2, the path is not tracked
git log --format=%H -- <rel> ; git hash-object -- <rel> ; git rev-parse <freeze>:<rel>
any call exiting non-zero -> exit 2 naming the call and its stderr
```

### The ungated scope (S9, S11)

| `check_gate_token(t, tracked, legs)` | `check_invariant` | `check_ungated` |
|---|---|---|
| a tracked path or a directory over one | passes | gated |
| not tracked, `legs is None` | the note, as today | ungated, with a note |
| not tracked, not a leg | check 18 failure | ungated |

A class is gated when any token in its scope resolves. The scope is S11's sentence or a `## Gated by`
body, read from the body that `FM_RE` cuts.

### The pack's home (S12, S13, S20)

`checkOptinPackPresent` reads `.governance/install.json` once, from the root `resolve_kit_dir` finds
(the nearest directory holding `.git`). It takes the review kit's row first, then the probe beside
the hook. The same read gives S13 the receipt's `kits`, which picks the remedy. A receipt that is
absent or unreadable is not a failure: it is the hand-copy case, and the probe decides.

### The recipe's failure envelope (S22)

```bash
set -e
test ! -e "$TEMP/<name>" || { echo "replay: $TEMP/<name> exists"; exit 2; }
trap 'git update-ref -d refs/replay/<name> 2>/dev/null' EXIT
# ... the recipe's steps, unchanged ...
test "$(git -C "$TEMP/<name>" rev-parse HEAD)" = "$(git rev-parse <commit>)"
```

### Files touched (estimate)

- `tools/workflows/render_lenses.py`
- `tools/workflows/check-verifier-fanout.sh`
- `tools/workflows/check-verifier-fanout.js`
- `tools/workflows/check-verifier-fanout.test.sh`
- `tools/workflows/replay_scorer.py`
- `tools/workflows/spec-audit-optin.js`
- `tools/workflows/spec-audit-optin.test.sh`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/README.md`
- `tools/workflows/REVIEW-PROTOCOL.template.md`
- `memory/guides/REVIEW-PROTOCOL.md`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/hooks/kit.toml`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/check-playbook-parity.sh`
- `tools/check-playbook-parity.test.sh`
- `tools/memory-tree/gotchas.py`
- `memory/gotchas/INDEX.md`
- `memory/guides/SESSION-KICKOFF.md`

`tools/workflows/tier2-review.js`, `memory/guides/REVIEW-PROTOCOL.md` and `memory/gotchas/INDEX.md` are
renders. The spec files of units 20 to 23 are not touched: every correction is stated here.

### Alternatives rejected

- **Two batch units** — §4 "Why one unit and not two".
- **A govkit refusal of a split update (S12)** — unit 22 §8 F1 (c), still refused. A descriptor row
  reaches the same scope with no deployer change.
- **Hold the shell `LENS_SLOTS` beside the JS one with a parity arm (S14)** — two homes and a guard,
  where one home needs none.

## 5. Production-readiness checklist

- security — S20 reads the receipt only for a row whose `path` resolves inside the tree, as
  `resolve_kit_dir` does, and follows no `..` path. S13 and S20 keep the fail-closed deny. No new
  write path.
- perf / scale — one receipt read per spec-audit `Workflow` call, and one `git ls-files` per
  held-out path.
- error / empty / loading states — S7, S23 and S30 turn a failed helper call into a named exit 2,
  never an empty population. S22 refuses a stale clone directory.
- observability — each refusal names its call or its path. `check_ungated` announces the leg names it
  could not check.
- risks — S12's marker couples two kits' updates. That is the intent, and it is the only cross-kit
  marker the hooks kit declares.
- testing — scratch probes and fixtures per criterion. The §7 arms are observed RED then GREEN at the
  close.
- migration — adopters who claim both kits move them together on their next scoped update. Hooks-only
  adopters see the corrected remedy.
- user docs — `tools/workflows/README.md` (the recipe, the arguments), `tools/hooks/README.md` (the
  pack's home and remedy) and `memory/gotchas/INDEX.md`. There is no `help/` page (§3).

## 6. Acceptance criteria

`$SCRATCH` is the pass's scratch directory, and a clone or fixture repository goes under
`%TEMP%/<short name>` (S28). A bare script name is the workflows kit's file under `tools/workflows/`.

- **AC1** — When `python render_lenses.py --markers "$SCRATCH/h.js"` runs over a file holding a
  five-slot `gov:lens-slots` literal and a zero-row `gov:lens-optins` literal, it prints only the
  first literal's line, and `bash check-verifier-fanout.sh "$SCRATCH/h.js"` exits 0.
  Red when: the opt-in line is printed or counted, so the zero-row literal reds the leg.
- **AC2** — When `grep -cE '^\s*git clone .*--branch' tools/workflows/README.md` runs, it prints 0, and
  `grep -c "never .git clone --branch" tools/workflows/README.md` prints at least 1.
  Red when: the absence check matches the warning S17 requires.
- **AC3** — When `grep -c FOREIGN_PREFIX_PROBE spec-audit-optin.test.sh` runs, it prints at least 1, and
  `grep -c "spec-audit opt-in pack self-test" tools/run-gates/foreign-prefix.gov.test.sh` prints 0.
  Red when: the suite stops at the probe and is also declared a whole run, which the leg reds as stale.
- **AC4** — When a scratch python probe imports `replay_scorer.py`, `extract_tag_ref('x.md:AC3')`
  returns `('x.md', 6)`, `extract_tag_ref('x.md:S5 scope')` returns `('x.md', 2)`, and
  `extract_tag_ref('x.md:prose')` returns `None`. For each ref the section equals
  `review_replay.extract_section_ref`'s.
  Red when: an item-only ref returns `None`, so the two readers disagree.
- **AC5** — When the unit 21 AC3 manifest runs through `python replay_scorer.py --experiment` with the
  held-out path spelled with backslashes, and again spelled absolute, each prints `frozen at
  b6c828a92` first. A scratch copy whose `git rev-parse` is forced to exit 128 exits 2 naming the
  call and its stderr.
  Red when: a correctly frozen file spelled either way is refused as differing, or the echoed argument
  is printed as a blob id.
  figure: the sha is PINNED, unit 21 §4's measurement of 2026-10-23.
- **AC6** — When a scratch python probe imports `tools/memory-tree/gotchas.py`, `check_ungated` reads
  "Gated in\n`tools/check-wiring.sh`'s arm." and "The lock is gated by\n`tools/check-wiring.sh`." as
  gated. It reads a `## Gated by` body holding a tracked path as gated, and a body naming only
  `fixture leg` with `legs` None as ungated with a note. The selftest arm "a leg-name guard under a
  blank LEG_MANIFEST is announced and exits 0" still passes.
  Red when: a wrapped or heading-form gated class reads as ungated, or the blank-manifest note becomes
  a check-18 failure.
- **AC7** — When `grep -n marker_carriers tools/hooks/kit.toml` runs, it prints the pack's row. The
  value in `grep -o "gov:kit agent-cap@[0-9.]*" spec-audit-optin.js` equals `KIT_AGENT_CAP_VERSION` in
  `tools/hooks/agent-cap.js`. A scratch target whose receipt claims both kits, run with `python
  tools/govkit/govkit.py update --target "$TEMP/fhk" --kits agent-cap`, prints `scope: review-harness
  moves with agent-cap`.
  Red when: the scoped update lands the hook without the pack.
  fixture: the target under `%TEMP%/fhk`, made by `govkit.py apply --target "$TEMP/fhk" --kits agent-cap,review-harness`.
  cost: one apply and one update into a scratch target, under a minute.
- **AC8** — When a scratch copy of the hook runs a spec-audit payload with no pack, a receipt claiming
  `agent-cap` alone makes its stderr name `govkit apply --kits review-harness` and not `update --kits
  review-harness`. A receipt claiming both makes it name `govkit update --kits review-harness`.
  Red when: the unclaimed case is sent to a verb govkit refuses.
- **AC9** — When `grep -cE "LENS_SLOTS ?= ?[0-9]" check-verifier-fanout.sh` runs, it prints 0, and over
  `check-verifier-fanout.js` it prints 1.
  Red when: the shell constant survives beside the JS one.
- **AC10** — When `git diff -U0 "$(git merge-base HEAD main)" HEAD -- tools/hooks tools/roles .claude/skills/build tools/workflows | grep -E '^-.*(KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@)'`
  runs at this unit's commit, it prints nothing.
  Red when: a version line that existed is changed on the branch, a hand bump.
- **AC11** — When `git grep -n MAX_LENSES -- tools memory/guides ':!tools/workflows/check-verifier-fanout.js'`
  runs, it prints nothing. A scratch copy of `check-playbook-parity.sh` run over this tree extracts a
  non-empty value on both sides of the `lens-array bound` pair, equal to 5.
  Red when: the pair's sed extracts nothing, or a REVIEW-PROTOCOL copy names a constant that does not
  exist.
- **AC12** — When `grep -n "spec-audit opt-in pack self-test" tools/govkit/subject-pins.tsv` runs, it
  prints one row.
  Red when: the live leg has no pinned row, which govkit's selfcheck reds.
- **AC13** — When `grep -c legManifest tools/workflows/tier2-review.js tools/workflows/tier2-review.template.js tools/workflows/tier2-review.test.sh tools/workflows/README.md`
  runs, each of its four lines ends `:0`. When `grep -c gateManifest tools/workflows/README.md tools/workflows/tier2-review.test.sh`
  runs, neither line ends `:0`.
  Red when: the README or the arm keeps the old name, so a caller silently gets the default manifest.
- **AC14** — When `python replay_scorer.py --selftest` runs, it exits 0. A scratch copy with
  `ARMS_DECLARED` lowered by one exits non-zero, naming the ran and declared counts.
  Red when: unit 21's arms ran with the declared count unraised, so the runner reds.
- **AC15** — When a scratch layout holds the hook at `$SCRATCH/p/.claude/hooks/agent-cap.js`, the pack
  at `$SCRATCH/p/tools/workflows/spec-audit-optin.js`, a `.git` directory and a receipt row naming the
  pack in `$SCRATCH/p/.governance/install.json`, a spec-audit payload exits 0. With the row left out,
  it exits 2. With the row naming a missing path, it exits 2 naming that path.
  Red when: the pack under a per-kit prefix is denied though the receipt names it.
- **AC16** — When a python probe reads `tools/gate-legs.json`, the `agent-cap self-test` guard holds
  the pack's prefixed path that S21 names. The `last-audit:` sha of `memory/guides/SESSION-KICKOFF.md`
  is one after which `git log <sha>..HEAD -- tools/gate-legs.json` lists no commit.
  Red when: a change to the pack alone skips the leg that holds the hook's literal.
- **AC17** — When the README's recipe runs twice with `<name>` `fhr`, first at `3708a705` and then at
  `HEAD`, the second run exits 2 before any fetch. After `rm -rf "$TEMP/fhr"` it ends with `git -C
  "$TEMP/fhr" rev-parse HEAD` equal to `git rev-parse HEAD`. `git show-ref refs/replay/fhr` prints
  nothing after either run, a forced bundle failure included.
  Red when: the second run passes its liveness check at the first commit.
  fixture: the clone under `%TEMP%/fhr`, made by the probe.
- **AC18** — When a scratch gate copy runs explicit-file mode over a harness with no
  `render_lenses.py` beside it, and again with python made unresolvable, each exits 2 and prints
  `the marker predicate did not run`.
  Red when: a failed predicate call reads as no markers and the leg passes.
- **AC19** — When a scratch prelude probe passes a `run` 2 `walk` whose one step holds 30 items under 7
  scenarios, it throws before the first agent, naming the 210-cell slice. The same grid under `run` 1
  proceeds.
  Red when: only the run-1 deal is checked, so the run-2 band reaches a walker.
- **AC20** — When unit 20's complete-walk stub run builds its synthesis prompt, no line matches
  `the walk table has [0-9]+ gap`. The gapped run's prompt holds one.
  Red when: the absence check matches the static verdict list's `BLOCKED`.
- **AC21** — When `grep -n "roundState" tools/workflows/tier2-review.js` runs within the args header,
  it prints the sentence that nulls `blockers`, `highs`, `roundCount` and `roundState` on a gapped
  walk.
  Red when: the header ships without the sentence.
- **AC22** — When `awk '/\/\/ ---- /{arm=$0} /3708a705/{print arm}' tools/workflows/tier2-review.test.sh`
  runs, slicing the suite at each arm header, it prints no header naming `TOOL-dFairHearing-2 AC4`,
  `TOOL-dFairHearing-3 AC5` or `TOOL-dFairHearing-9 AC7`. The same probe with `REVIEW_SHAPE` in place
  of `3708a705` prints all three.
  Red when: an arm compares with base's harness.
- **AC23** — When `git grep -n "Windows path limit" -- tools` runs, it prints nothing.
  Red when: a product file records the unmeasured claim.
- **AC24** — When `git grep -n "Hand a reviewer the classes" -- tools/memory-tree/gotchas.py memory/gotchas/INDEX.md`
  runs, it prints nothing, and `INDEX.md` names the harness acquiring the checklist.
  Red when: the catalogue index still sends a reviewer to the by-hand lookup.
- **AC25** — When a scratch copy of the tree plants a module with the pairing comprehension (unit 12
  AC6's shape) under the copy's factory directory, `scan_pairing_sites` names it. The same module
  under the copy's `memory/` is not named. A copy where `git ls-files` fails makes the scan exit 2 by
  name.
  Red when: a failed or empty walk returns `[]` and passes.
- **AC26** — When a scratch node probe reads `check-verifier-fanout.js` through the literal-blanked
  view with comments blanked too, it finds no `MAX_LENSES` identifier and one `LENS_SLOTS`
  declaration. The same probe over `tier2-review.js` finds no `legManifest`.
  Red when: a comment naming the old bound reds a correct build, or a code reference survives.

## 7. Gates

`playbook parity selftest` · `playbook parity` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `agent-cap restatement` · `verifier fan-out self-test` · `verifier fan-out` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-replay selftest` · `gotchas selftest` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `foreign-prefix parity (every self-test at three prefixes)` · `review-protocol parity (kit vs dogfood)` · `kickoff-manifest ratchet` · `kit version markers` · `workflow script syntax` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/check-verifier-fanout.test.sh · covers AC1 AC18 · a zero-row opt-in literal, a gate copy without the renderer and an unresolvable python, staged against the gate at `TOOL-dFairHearing-23`'s commit · none
New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC4 AC5 AC25 · an item-only ref, a backslashed and an absolute held-out path, and a failed `git ls-files`, staged against the factory at `TOOL-dFairHearing-23`'s commit · that runner's `ARMS_DECLARED`, raised by the arms added
New arm: tools/memory-tree/gotchas.py (its selftest) · covers AC6 · a wrapped gate token, a `## Gated by` body and a leg name under a blank manifest, staged against `TOOL-dFairHearing-23`'s `check_ungated` · none
New arm: tools/hooks/agent-cap.test.sh · covers AC8 AC15 · an unclaimed receipt and a pack under a per-kit prefix, staged against the hook at `TOOL-dFairHearing-22`'s commit · none
New arm: tools/workflows/tier2-review.test.sh · covers AC19 AC20 · a run-2 band of 210 cells and a complete walk's prompt, staged against the harness at `TOOL-dFairHearing-23`'s commit · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, unit 22's minors
  and the rest. (b) fails M6's clause 2 on the two contract reads §4 names. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What remedy does the deny name for an adopter whose receipt does not claim the review kit
  (S13)?** Options: (a) `govkit apply --kits review-harness`, the verb that installs a kit; (b) the
  kit's name alone, with a pointer to govkit's documentation; (c) `--add-kits`, which govkit's refusal
  names but no verb parses (`tools/govkit/govkit.py:13719-13724`). (c) sends the adopter to a third
  refusal. (b) leaves the verb to a reader. (a) names a command that runs. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Does `--markers` need its own python floor (S23)?** Options: (a) it shares the renderer's, and
  any refusal is the named exit 2; (b) it runs below the renderer's version check, so an older python
  still answers. (b) adds a second entry path for one flag, and the leg's verdict is the same named
  refusal either way. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 24 MEDIUM and 7 LOW findings of the spec audit of
  units 20 to 23 as one batch.
- rev-2 · 2026-10-23 · §3 · the round-3 spec audit's disposal: hands-off edges to TOOL-dFairHearing-31
  (the version check's base, finding id 34) and TOOL-dFairHearing-32 (eleven minors).

## 10. Reuse audit

Every item extends a seam that an earlier unit mints or the base tree carries, and none adds a
module. The seams: govkit's `marker_carriers` coupling (`tools/govkit/govkit.py:1034-1059`, used today
by `tools/drift-audit/kit.toml:13`); `resolve_kit_dir`'s receipt-then-probe order
(`tools/check-kit-versions.sh:69-105`); `extract_section_ref`'s item fallback
(`tools/workflows/review_replay.py:100-115`); `check_invariant`'s token loop
(`tools/memory-tree/gotchas.py:432-440`); and the sibling suites' `FOREIGN_PREFIX_PROBE` stop.
`python tools/codebase-map/reuse_lookup.py "resolve a sibling kit file through the install receipt"`
ranked `resolve_kit_dir` and `kit_rel`. The Node hook runs neither, so S20 ports the two rungs it
needs. The coupling row, the item fallback and the probe stop came from the source read. The recall
query returned specs 21 and 22 and the round-1 audit, which this spec corrects.

Recall terms used: `python tools/memory-recall/query.py "spec audit minors on the opt-in pack presence check, freeze path normalisation and slot count" --terms "marker_carriers receipt resolve_kit_dir freeze hash-object normalise ungated wrapped LENS_SLOTS subject-pins foreign-prefix walk cap"`
