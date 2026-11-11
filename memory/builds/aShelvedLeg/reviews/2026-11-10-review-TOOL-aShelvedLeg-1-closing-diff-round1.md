**Serves:** diff-review TOOL-aShelvedLeg-1

# Closing diff review, round 1: aShelvedLeg unit 1, the unattended kit gate held off every automatic bar

2026-11-10 · Tier-2 · on `branch/clever-babbage-44839c` · adversarial fan through `tier2-review.js`: 5 finder lenses (gov-diff-reviewer), 4 skeptic batches (gov-skeptic), then this synthesis (gov-synthesizer). The subject is the cumulative diff landing on main.

**Reviewed range:** `b904a0f913957b13bfda3dc00e5d8f77bd3cffb7...3203e2ac4e6c6e6ea64197bd24bc05e094bcf8cc`. **ROUND 1.**

## Verdict: BLOCKED

One blocker stops the landing. The new `unattended kit gate` budget row reds `run-selftests.sh --check`, which is an unguarded bar leg, so every bar run fails after this diff. The other seven confirmed findings are LOW and fall into five items:

- Two items are prose the diff made false, in two files.
- One is a miscount in a comment the diff rewrote.
- One is a missing sentence about `GATE_SELFTESTS=changed`.
- One is a budget row the `--rank` reader cannot parse.

Fold all of them before the close.

## Review shape

Intensity full, raw 8, confirmed 8, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, counted two ways:

- By item: 6 items, 1 BLOCKER and 5 LOW.
- By raw confirmed finding: 8 findings, 1 blocker, 0 high, 0 medium and 7 low.

Items 2 and 3 each hold two findings that name the same stale sentences.

### Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified. 0 orphaned duplicate refutations demoted to unverified. 0 duplicate refutations counted as merged confirmations. 0 spurious verdicts discarded. 0 duplicates.
- Fixes on confirmed findings: 5 judged SOUND, 0 judged UNSOUND, 3 judged INSTANCE-ONLY, 0 with no fix proposed, 0 NOT JUDGED. An INSTANCE-ONLY fix cures the cited instance and leaves its class standing.
- Severity on confirmed findings: 0 UNGRADED by the skeptic. 1 RE-GRADED by the skeptic: id 1, from medium to low.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: neither `specs` nor `context` was supplied. The lenses had only the range's commit messages and what they read from the tree.
- Checklist: 31 items, acquired by the harness from `--for-diff b904a0f913957b13bfda3dc00e5d8f77bd3cffb7..HEAD`. Each went to exactly one lens: security 7, correctness 6, seams 6, verification 6, intent 6.
- By design: none supplied, with no caller byDesign and a block of 0.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twins are flagged.
- Dispositions: unclassed refused. 31 class slugs were handed, and 149 leg names were read from `tools/gate-legs.json`.

Every integrity count is zero and no lens or batch died, so this run is complete.

## Items

### 1. BLOCKER: the new budget row reds the trailer arm of `run-selftests.sh --check` on the bar (id 3)

- **Where:** the row is at `tools/run-gates/selftest-budgets.txt:141`. The trailer arm that grades it is in `tools/run-gates/run-selftests.sh` at lines 1088-1107. The pooled-kit declaration is at `tools/run-gates/selftest-pooled-evidence.txt:30`.
- **What is wrong:**
  - The new `unattended kit gate` row has an empty argv column. `read_population` (run-selftests.sh ~703-707) therefore takes the argv from the manifest leg of the same name at `gate-legs.json:1083`. That argv resolves to `tools/unattended/check-unattended.sh`.
  - That path falls under `# pooled-kit: {prefix}/unattended`, so the trailer arm grades the row.
  - The script prints nothing that matches `SWEEP_TRAILER_RX` (`PASS \(|assertions executed|this leg ran shard`). It ends with a bare `exit "$status"`.
  - The row is not declared `# no-trailer:`. The only two declarations are `brief-recorded` and `pass-order`.
- **Consequence:** `--check` runs as the bar leg `every held leg is budgeted, every budget row resolves` (`gate-legs.json:1926`), which is repo-subject and unguarded. That leg now fails on every bar run, on this branch and on main, and it blocks every later landing. This diff introduced the fault. At the base no budget row named the kit gate, because the gate was a bar leg and not held.
- **Fix (judged SOUND by the skeptic):**
  - Add `# no-trailer: unattended kit gate` beside the two existing no-trailer declarations in `tools/run-gates/selftest-pooled-evidence.txt`.
  - Note there that this is a checker, not a self-test, so a completed run is read from its exit code plus the count of `^FAIL` lines.
  - The alternative is to have `check-unattended.sh` print a trailer on every run.
  - Either way, the main session then runs `bash tools/run-gates/run-selftests.sh --check` and confirms that the trailer-arm fault naming `unattended kit gate` is gone.
- **Left-shift gate:** the leg `every held leg is budgeted, every budget row resolves` already catches this. Any change that holds a leg should run `run-selftests.sh --check` before it commits.

### 2. LOW: `run-unattended-gates.sh` still calls the whole `--checks` half "repository checks and merge-bar legs" (ids 1, 7)

- **Where:** `tools/unattended/run-unattended-gates.sh:46-47`, in the header comment, and `:434`, in the `--attribute` text that `--help` prints.
- **What is wrong:**
  - Both lines give "those are repository checks and merge-bar legs" as the reason the `--checks` half is not attributed.
  - The `--checks` half runs `check-unattended.sh` as its first row (`:549`/`:551`). This diff moved that leg to subject=kit and held it off every bar.
  - The diff reworded `:8`, `:419-420` and `:559` of the same file but missed these two lines.
  - Spec S5 asks for every sentence in the unattended kit that calls this leg a merge-bar leg to be corrected. AC6's grep checks three other phrases and misses this wording.
- **Consequence:** only comment and help text change, and behaviour does not. The `--help` output now contradicts the corrected `--checks` line a few lines above it. The stated reason for not attributing `--checks` is now false for the kit gate. That gate runs only through `--checks` or `GATE_SELFTESTS=1`, and neither route attributes a failure to a baseline.
- **Grades:** id 1 is low. The finder graded it medium. The skeptic regraded it low because only comment and help text change, and I keep that grade. Id 7 is low.
- **Fix:**
  - Id 1's fix was judged INSTANCE-ONLY. The skeptic's class-level fix has two parts:
    - Rewrite every stale claim that the kit gate (`check-unattended.sh`) is a merge-bar leg. Those claims are at `run-unattended-gates.sh:46-47` and `:434`, `check-unattended.sh:2`, `:435` and `:3809`, and `check-unattended.test.sh:3330`.
    - Add an AC-style grep check over `tools/unattended/` that fails when "merge-bar leg" appears next to check-unattended or the kit gate.
  - The finder's proposal for id 1 cures only the cited instance. It amends lines 46-47 and 434 to name the held kit gate as the exception, or extends `--attribute` to the kit gate.
  - Id 7's fix was judged SOUND. Reword lines 47 and 434 the way lines 420 and 561 were reworded. Add the phrase "repository checks and merge-bar legs" to AC6's grep.
- **Left-shift gate:** the grep check over `tools/unattended/` described above, which fails on merge-bar wording tied to the kit gate. Also widen AC6's list of phrases.

### 3. LOW: `check-unattended.sh` still calls itself the merge-bar leg (ids 2, 8)

- **Where:** `tools/unattended/check-unattended.sh:2`, `:435` and `:3809`. The diff did not touch this file.
- **What is wrong:**
  - Line 2 reads `# check-unattended.sh - the merge-bar leg for the unattended-run kit`. Lines 435 and 3809 say "an unguarded merge-bar leg".
  - The diff held this exact leg off every automatic bar by giving it subject=kit in `gate-legs.json` and `kit.toml`, so these lines are now false.
  - They contradict the ruling comment in kit.toml and the README.
  - S5's general clause covers these lines, although its explicit list of lines leaves this file out.
- **Consequence:** only comments are affected. The script's own header gives a second answer to whether the leg is on the bar. Two readers will take the wrong one: the next person who edits the leg, and an adopter told at `adopt-unattended.sh:1178` to wire it in.
- **Fix:**
  - Both fixes were judged INSTANCE-ONLY.
  - The skeptic's class-level fix for id 8, which covers id 2's instance, has two parts:
    - Reword every sentence that calls `check-unattended.sh` a merge-bar leg or says it runs on the merge bar. That covers `check-unattended.sh` lines 2, 73, 435 and 3809. It also covers `check-unattended.test.sh` line 2485 ("It runs on the merge bar") and line 3330 ("on an unguarded merge-bar leg"). Each sentence should say the leg is held off every automatic bar by the 2026-11-10 ruling (TOOL-aShelvedLeg-1) and runs through `run-unattended-gates.sh --checks` or `GATE_SELFTESTS=1`.
    - Widen AC6's grep to cover "merge-bar leg" and "on the merge bar" in `check-unattended.sh` and its test file.
  - The class-level fix for id 2 also adds `run-unattended-gates.sh:46-47` and `:434` (item 2) and the same grep check over `tools/unattended/`.
  - The finders' proposals cure only the cited instances: they reword the header and the two inline comments.
  - Edit `check-unattended.sh` in binary mode, because it carries raw CR bytes.
- **Left-shift gate:** the same grep check over `tools/unattended/` as item 2, with AC6 widened to `check-unattended.sh` and `check-unattended.test.sh`.

### 4. LOW: the rewritten `--checks` comment says "those four" about five rows (id 4)

- **Where:** `tools/unattended/run-unattended-gates.sh:561`.
- **What is wrong:**
  - The sentence now reads "those four are REPOSITORY checks, bar legs but for the held kit gate".
  - The `--checks` half (lines 551-555) runs five rows, and the kit gate is the first.
  - "Four" was already wrong at the base. This diff rewrote the sentence and added the kit-gate exception, which places the kit gate among the four.
- **Consequence:** only a comment is affected, and behaviour does not change.
- **Fix (judged SOUND by the skeptic):** write "those five are REPOSITORY checks, bar legs except the held kit gate". Better, drop the count. The file has its own rule against hand-typed population sizes.
- **Left-shift gate:** add a checklist entry: prose must not type a count of a population that the code enumerates, and should name the population instead.

### 5. LOW: the kit docs do not say that `GATE_SELFTESTS=changed` can skip this leg after a records-only change (id 5)

- **Where:** the HELD block at `tools/unattended/kit.toml:256-262` and the paragraph at `tools/unattended/README.md:422-424`. The selection behaviour is in `run-gates.sh:3070-3200`.
- **What is wrong:**
  - Under `GATE_SELFTESTS=changed`, the held-select program picks a kit-subject leg using only two inputs: the leg's argv suite files and the owning kit's `govkit.py shipped --epoch` sources. It never reads a leg's `doc_reads`.
  - The `unattended kit gate` is now the only kit-subject leg with `doc_reads`: `memory/builds/`, `memory/guides/` and `memory/archive/`. A probe of the kit's shipped sources printed 47 unattended paths and none under `memory/`.
  - A change that touches only records therefore leaves this leg held for up to the 10-commit lag bound. Records-only drift is exactly what this leg exists to catch.
  - The spec names this risk at spec line 162. The new kit.toml and README sentences name only `--checks` and `GATE_SELFTESTS=1`.
- **Consequence:** the effect is contained, because the bar prints `GATE held`, not a pass. Even so, someone reading the kit could take a green `changed` run as having graded this leg.
- **Fix (judged SOUND by the skeptic):**
  - Add one sentence to the HELD block in kit.toml and to the README paragraph. It should say that `GATE_SELFTESTS=changed` selects this leg by kit source only, so it does not re-run the leg when only records move, and that `=1` or `--checks` should be used after a records change.
  - The alternative is to add the leg's `doc_reads` to its selection set in the held-select program in run-gates.sh.
  - To probe, run with `GATE_SELFTESTS=changed` on a tree with a fresh last-run record where only a `memory/builds` file changed. Confirm the leg prints `GATE held`.
- **Left-shift gate:** add a new class entry. A kit-subject leg that declares `doc_reads` must include them in its changed-mode selection set, or its descriptor must state the skip. A check over `gate-legs.json` can flag every kit-subject leg whose `doc_reads` is non-empty.

### 6. LOW: the new budget row spells its reading in a form `--rank` cannot parse (id 6)

- **Where:** the row is at `tools/run-gates/selftest-budgets.txt:141`. Its reader is `run-selftests.sh --rank`, at lines 550-555.
- **What is wrong:**
  - The row reads `worst of 5 retained gate-run readings on node a 2026-11-10, 3147s ...`.
  - `--rank` recognises only two forms, `worst of (\d+) readings (\d+)s` and `measured (\d+)s`, and the row matches neither.
  - The spec (section 4, "The budget") asks for the row to take the shape of the other rows, and no check enforces that.
- **Consequence:** the effect is contained. `--rank` lists the row among the rows whose reading it does not recognise, and it computes no share for it. The row is now the largest unranked one, at 4721 s. At the base 21 rows already failed the patterns, so `--rank` was refusing before this diff.
- **Fix (judged SOUND by the skeptic):** respell the row as `worst of 5 readings 3147s on node a 2026-11-10 (retained gate-run windows), beside six foreign gate processes, x1.5. TOOL-aShelvedLeg-1 held it by owner ruling`. The main session then runs `run-selftests.sh --rank` and confirms this row is no longer listed among the unbacked rows.
- **Left-shift gate:** add an arm to `run-selftests.sh --check` that fails any budget row whose reading column matches neither `--rank` pattern. The 21 rows that already fail must be respelled first.

review-shape kind=diff-review round=1 intensity=full at=synth raw=8 confirmed=8 refuted=0 merged=0 unverified=0 blocker=1 high=0 medium=0 low=7 agents=10 out-tokens=42168
review-round round=1 limit=- prior=- count=1 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/run-unattended-gates.sh:434 | medium | low | confirmed | At 3203e2ac, run-unattended-gates.sh:46-47 still says 'The `--checks` half is NOT attributed, because those are repository checks and merge-bar legs', and the help echo at :434 says the same. The diff flipped the `unattended kit gate` row to subject=kit in gate-legs.json:1090 and kit.toml, and the `--checks` half still runs check-unattended.sh as its first row (:549). So this rationale is now false for one of the checks it covers. Spec S5 asks for 'each sentence in the unattended kit saying this leg is a merge-bar leg' to be corrected, and the diff fixed :8, :419 and :559 but missed these two lines. Before the diff the sentence was true, so this change introduced the defect. The consequence is limited to a stale comment and help text. No behaviour changes: --checks was never attributed, and the bar never attributed this leg either. Graded low. | instance | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 2 | security | tools/unattended/check-unattended.sh:2 | low | low | confirmed | At 3203e2ac, `sed -n 2p tools/unattended/check-unattended.sh` prints '# check-unattended.sh - the merge-bar leg for the unattended-run kit', and lines 435 and 3809 say 'an unguarded merge-bar leg'. The file is untouched by the diff (it is not in the --stat), but the diff made these sentences false when it moved the leg to subject=kit. Spec S5's general clause says every sentence in the unattended kit calling this leg a merge-bar leg is corrected, and these were missed. Only comments are affected, so graded low. | instance | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 3 | correctness | tools/run-gates/selftest-budgets.txt:141 | blocker | blocker | confirmed | The new selftest-budgets.txt row 'unattended kit gate' has an empty argv column. read_population (run-selftests.sh ~703-707) therefore takes the argv from the manifest leg of the same name in gate-legs.json:1083, which is `bash {prefix}/unattended/check-unattended.sh`, and resolves it to tools/unattended/check-unattended.sh. selftest-pooled-evidence.txt:30 declares `# pooled-kit: {prefix}/unattended`, so tr_in=1 in the trailer arm (run-selftests.sh 1088-1107). The only no-trailer declarations, at lines 22-23, are brief-recorded and pass-order, so the row is graded. A grep of check-unattended.sh for SWEEP_TRAILER_RX (line 388) counts 0 matches, and the script ends `exit "$status"`, so tr_faults gets the row and fails=1 is set. That --check is the bar leg 'every held leg is budgeted, every budget row resolves' (gate-legs.json:1926, subject repo), so the bar reds on every run. At the base no budget row named the kit gate, because it was a bar leg and not held, so this diff introduced the fault. | sound | - | gate:every held leg is budgeted, every budget row resolves |
| 4 | correctness | tools/unattended/run-unattended-gates.sh:561 | low | low | confirmed | Lines 551-555 hold five run_one rows under --checks, the kit gate first. The word 'four' was already wrong at the base, which had the same five rows. But this diff rewrote the sentence and added 'bar legs but for the held kit gate'. The sentence now counts the kit gate among 'those four', so the miscount is in a line this diff wrote. It is a comment only and changes no behaviour. | sound | - | new:hand-typed-count-of-an-enumerated-population |
| 5 | seams | tools/unattended/kit.toml:262 | low | low | confirmed | I confirmed this against run-gates.sh:3070-3200. Under GATE_SELFTESTS=changed, the held-select program picks a kit-subject leg using two inputs only: its argv suite files and the owning kit's `govkit.py shipped --epoch` sources. A leg's doc_reads are never consulted. gate-legs.json now gives `unattended kit gate` subject=kit and doc_reads memory/builds/, memory/guides/ and memory/archive/. It is the only kit-subject leg with doc_reads. So a change that touches only records holds the leg (prints GATE held) until the 10-commit lag bound runs out. At the base the leg was subject=repo and ran on every bar, so this diff made the path reachable. The spec names the risk in its section 5 risks bullet. The new kit.toml HELD block (lines 256-262) and README lines 422-424 name only --checks and GATE_SELFTESTS=1 and say nothing about `changed`. The effect is contained, so I grade it low. The bar's output says the leg was held, not that it passed, and run-gates.sh's own 'WHAT THIS DOES NOT CHECK' comment states the general class. | sound | - | new:changed-mode-selection-ignores-doc-reads |
| 6 | verification | tools/run-gates/selftest-budgets.txt:141 | low | low | confirmed | selftest-budgets.txt:141 reads `worst of 5 retained gate-run readings on node a 2026-11-10, 3147s ...`. The rank reader in run-selftests.sh (lines 550-555) has two condition patterns. `worst of (\d+) readings (\d+)s` does not match, because `retained gate-run` sits between the 5 and `readings`, and the seconds come later. `measured (\d+)s` does not match either, because the row has no `measured`. So the for/else falls through and the row lands in `unbacked`, and --rank exits 1 with no share computed. The other rows, for example lines 50-59, use the matching spelling `worst of N readings Ns`, which goes against the spec's 'in the shape of the other rows'. Other rows at the base already fail the patterns, for example line 53 (`worst of 4 readings alone 105s`), so --rank was already refusing before this diff. The harm is contained: low. | sound | a-spelling-change-strands-its-readers | class:a-spelling-change-strands-its-readers |
| 7 | intent | tools/unattended/run-unattended-gates.sh:434 | low | low | confirmed | At 3203e2ac, tools/unattended/run-unattended-gates.sh:47 still reads 'The `--checks` half is NOT attributed, because those are repository checks and merge-bar legs.' Line 434 still echoes 'those are repository checks and merge-bar legs.' in --help. The --checks half runs the 'kit gate' (check-unattended.sh, line 551), and this diff makes that leg subject kit and holds it off the bar. It also rewrote lines 8, 420 and 559 of the same file to say 'except the kit gate', so the diff itself made lines 47 and 434 false and inconsistent with the new wording. S5's stated goal is 'Each sentence in the unattended kit saying this leg is a merge-bar leg is corrected'. AC6's grep only matches three other phrases, so it misses this wording. Behaviour is unchanged: the help text is wrong, nothing else. | sound | - | class:amendment-leaves-its-other-half-standing |
| 8 | intent | tools/unattended/check-unattended.sh:2 | low | low | confirmed | tools/unattended/check-unattended.sh:2 reads '# check-unattended.sh - the merge-bar leg for the unattended-run kit', and lines 435 and 3809 say 'an unguarded merge-bar leg'. The diff leaves this file untouched, but it holds this exact leg off every automatic bar (subject kit, in gate-legs.json and kit.toml), so it made these lines false. They now contradict the kit.toml ruling comment and the README. This is S5's own goal ('each sentence in the unattended kit saying this leg is a merge-bar leg'), even though S5's explicit line list leaves this file out. The effect is limited to comments. | instance | - | class:amendment-leaves-its-other-half-standing |
