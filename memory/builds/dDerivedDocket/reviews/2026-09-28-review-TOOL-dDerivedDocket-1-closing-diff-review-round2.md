**Serves:** diff-review DEPL-dDerivedDocket-1 PLAY-dDerivedDocket-1 TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 TOOL-dDerivedDocket-61 TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-64 TOOL-dDerivedDocket-65

# Closing diff review round 2 (BUILD-METHOD M8): dDerivedDocket, a fold review of round 1's ten fixes

Node `d` · 2026-09-28 · Tier-2 · on `branch/backlog-maintenance-mechanics-10588f` · run phase VERIFYING · adversarial fan through `tools/workflows/tier2-review.js`, with 4 finder lenses, then 3 skeptic batches, then this synthesis. Round 1's confirmed set went in as `priorFindings`. The lenses were pointed at the fold text only: the new code, the new arms, and whether each fix closes its finding without opening a sibling hole. I re-read every confirmed finding at source at `265d344c`. I also re-executed the lander finding, as stated under it.

**Reviewed range:** `364278a8b104c6e42f250e68fb8d98fc210a1aa0...265d344cb8fb72d6a1be82bd4619316c2ba03586`, **ROUND 2**. The base is round 1's recorded tip, as M8 requires for a round above 1. The range is two commits and 83 files, +1504/−132. `a6cccc03` is round 1's record, a one-line review stamp on each of the 50 specs, and a 6-line `tools/runlog/record.py` schema fix. `265d344c` is the fold, 32 files, +1179/−130. The product share of the range, under `tools/`, `.githooks/` and `.memory-tree.conf`, is 25 files, +1145/−120. HEAD in this worktree is `62dec397`, two records-only ledger commits past the range, and neither touches a file cited here.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and nothing is HIGH or MEDIUM. Two LOW items survived, and the fold introduced both. The first is in the lander this build will itself land through. The fold replaced `tools/push-main.sh`'s resume-after-signal trap with traps that exit. Bash defers a trapped signal until the foreground `git push` returns, so a TERM to the lander during the bar now lets the push publish and then exits before the landing is recorded. That wedges an unattended run on a landing that did happen. It was raised three times, with one mechanism. The second is documentary. The fold stated round 1's F1 age rule correctly in code, in the function header, in the run-gates README and in its own arm. It stated the rule wrongly in the STOPS contract, in its template and in the run-gates dossier. The other eight fixes drew no confirmed finding. Each LOW is a few lines plus one arm, so I recommend folding both before the landing.

## Review shape

Raw **6** · confirmed **4** · refuted **2** · unverified **0** · precision **0.67**.

Precision is above the 0.5 floor §8 sets. The four confirmed findings collapse to **2 items**. Ids 2, 3 and 4 are one defect, the lander's signal trap, raised three times with the same mechanism and the same reproduction. Ids 3 and 4 each named the other as a duplicate. I merged all three here, at write time. The pipeline itself removed no duplicates.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 0 MEDIUM · 2 LOW** (2 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 0 MEDIUM · 4 LOW** (4 findings; ids 2, 3 and 4 all take the LOW of the item that holds them).

The two refuted findings are the ids absent from the confirmed set, 1 and 5. A skeptic refuted each one, and neither is carried here. No severity moved at adjudication.

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **3/3** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so the run is complete. A zero in this report is evidence of absence within what the lenses read. Four lenses over a fold of about 1,200 added lines is a much closer read than round 1's prioritised pass over 38k. It is still a read and not a proof.

**What this synthesis ran.** I re-read every cited line at `265d344c`. I reproduced the lander finding with a stand-in script in my scratchpad, described under F1. I ran `tools/memory-tree/gotchas.py --for-diff` over the full range `869209ed..265d344c`, as M8 requires on every round. It selected 84 classes, 78 by anchor plus 6 universal. Over the fold range alone it selects 59. I ran no suite and no bar leg. The unattended kit's own self-tests are not run on the owner's behalf, by standing owner ruling.

**Scope note on `a6cccc03`.** The brief pointed the lenses at the fold commit. The 6-line `tools/runlog/record.py` change is in the range too, so I read it at synthesis. It lets the record schema accept the pre-hold `excluded rows` template beside the full one, which is its stated purpose, and I raise nothing on it. One cost is stated here rather than filed. A record written after the change in the older shape would also validate, because the schema carries no date to choose between the two templates.

**Known and not re-reported**, per the brief. The fold agents reported these residues themselves, and they were excluded from the finding set:

- A REOPEN-only disposition row still reads as cover in `--plan` and in the asks-disposed F-half.
- `spec_ask_verbs` still reads status-header closes and advances through the tolerant `expand_id_runs`.
- The `--relocate` index filter cannot see a provenance row that sits only in the working tree, unstaged.
- `--write` resolves a relative `--signed` path against the repository root, while `--plan` and `--ingest` read it relative to the cwd.
- `unattended.sh` `read_backlog_mode` and three older `MEMORY_ROOT` readers keep the first-wins, no-export conf-reader shape.
- Two conf-carrying worktrees now recompute one shared delta-cache entry in turn.
- Thirteen older driver-suite arms red identically before and after the fold in the replica cuts, because `git clean` removed fixture state.

Also excluded: the unattended arms were replayed alone rather than run as suites, and kit versions move in a sweep after this round.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| F1 | LOW | 2, 3, 4 | `tools/push-main.sh:140` | The fold's exiting INT and TERM traps fire after a foreground `git push` that published, so a signal to the lander mid-bar lands the push and exits before `write_lander_marker`. |
| F2 | LOW | 6 | `memory/guides/UNATTENDED-STOPS.md:438` | STOPS, its template and the run-gates dossier say a no-`signature` leg red with different output reads `age unproven`. The code reads a superset red as `aged`, and the fold's own arm pins that. |

### F1 — LOW · a signal during the push lands the landing and drops its record (ids 2, 3, 4)

`tools/push-main.sh:140`, as the fold left it:

```bash
  *) trap 'rm -f "$marker"' EXIT; trap 'exit 130' INT; trap 'exit 143' TERM ;;
```

Both push sites run `git push` in the foreground, then read its status and write the record. On the `--land` path the push is at line 521, `rc=$?` at 522 and `write_lander_marker` at 525. On the attended path they are at 620, 621 and 624. The foreground push is where the whole bar runs, through `.githooks/pre-push`, before anything is published.

Bash runs a trapped signal's handler between commands. While it waits on a foreground child, it notes the signal and defers the handler until the child returns. A TERM or INT sent to the lander's pid alone therefore lets `git push` finish and publish. Then the handler exits 143 or 130 before `rc=$?` runs. The landing is on the remote. `write_lander_marker` never runs. Neither the `landed` line nor the "push SUCCEEDED and is not recorded" sentence that every other post-push failure prints is emitted.

The pre-fold handler was `trap 'rm -f "$marker"' EXIT INT TERM`. It returned into the script, and bash restores `$?` after a handler, so `rc=0` still reached `write_lander_marker`. That handler had its own defect, round 1's F5 class: a signal before the push cleaned up and resumed the landing. The fold fixed that half and opened this one. A correct handler needs both halves. It exits outside the push window, and it defers inside it.

**Consequence in this repo.** `.unattended.conf` declares `LANDER_MODE="in-place"` (line 23) and `LANDER_MARKER="unattended-landed"` (line 341). `unattended.sh --landed` then fails 34 at line 4508, because the project declares a lander marker and the lander wrote none. Re-running `--land` does not repair it. `check_prepared_merge` refuses, because the prepared merge's first parent is no longer the advertised tip; the advertised tip is now that merge. `--prepare` finds nothing to land. The only recovery is to hand-write the evidence the marker exists to keep machine-written.

**Reach.** It is narrow. A process-group signal kills `git push` too, so nothing lands and nothing is misrecorded. That covers a terminal Ctrl-C, `timeout`, and the kit reaper's tree kill (`taskkill /T /F` or a group kill). What reaches the defect is a plain `kill <pid>` of the lander during the bar. That is an ordinary way to stop a script, and the bar makes the window minutes long.

**Reproduction.** I ran a stand-in with the exact trap lines under node `d`'s Git Bash. Its foreground child performed the "remote write" after about 3 seconds, and TERM went to the script's pid alone about 1 second in. With the new traps the script exited 143, the remote file was written, and there was no lander marker and no `landed` line. With the old traps it exited 0, wrote the marker and printed the `landed` line. Each of the three skeptic verdicts records the same result, one of them with a native `ping.exe` as the child.

**Why no gate saw it.** No arm covers this edit. The fold's new `tools/push-main.test.sh` arms are F7a to F7d only. The fold's F5 source scan in `tools/run-gates/run-gates.test.sh:2173-2206` reads `$KITDIR/*.sh`, the run-gates kit alone, as its own header says. The fold commit's message says each finding was "fixed at its cause with an arm seen red". That holds for F5's own instance in `run-selftests.sh`. It does not hold for this sibling edit, which shipped with no arm at all.

**Fix.** Defer the signal across the push-and-record window, then exit with it. At each of the two sites:

```bash
pm_sig=""
trap 'pm_sig=130' INT; trap 'pm_sig=143' TERM
git push "$remote" "$ref" >&2          # $ref: HEAD:refs/heads/$def at 521, $def at 620
rc=$?
rm -f "$marker"
if [ "$rc" -eq 0 ]; then
  write_lander_marker || exit 1
  echo "push-main: landed $def on $remote." >&2
  [ -z "$pm_sig" ] || exit "$pm_sig"
  exit 0
fi
[ -z "$pm_sig" ] || exit "$pm_sig"     # a signalled lander never retries or re-prepares
trap 'exit 130' INT; trap 'exit 143' TERM
```

When a signal arrived, print one line saying that the push completed and is recorded before the exit. The failure branch must also exit on a deferred signal before the `race` class re-prepares and pushes again.

**Left-shift.** Add an arm to `tools/push-main.test.sh`, placed by announcement and not by a sleep:

1. A stub pre-push writes a ready file, then waits under a bound for a release file.
2. The test backgrounds the lander and polls for the ready file under a bound.
3. It asserts the lander is alive, TERMs the lander's pid alone, and releases the stub.
4. It asserts that the remote advanced, that the lander marker names the pushed commit, and that the lander exited 143.

Observe that arm red on the current line-140 shape before the fix. Then bring `tools/push-main.sh` under the trap-class scan from its own suite. The run-gates kit must not name it, since a kit file names nothing outside itself by literal. The scan's current rule reds any handler that does not `exit`. It would therefore red the deferring handler this fix installs, so the scan needs a sanctioned deferral shape: a handler that only assigns a variable the same file later exits with. Record the new half on `memory/gotchas/trapped-signal-waits-for-the-foreground-child.md` as a "where it bit" line. An exiting handler held behind a child that PUBLISHES runs after the publication and before its record. Classes: `trapped-signal-waits-for-the-foreground-child`, `signal-trap-runs-the-exit-handler-twice` (the sibling F5 class) and `fold-text-is-unreviewed-surface`. The arm's placement follows `fixed-sleep-does-not-place-a-signal`.

### F2 — LOW · STOPS states an age rule the code does not implement (id 6)

The fold added this clause to `memory/guides/UNATTENDED-STOPS.md:438-439`, and the same text to `tools/unattended/STOPS.template.md:438-439`. It follows "A probe that cannot answer reads `age unproven`":

> a leg with no `signature` whose far end is red with different output is one

`memory/map/features/run-gates.md:216` says the same: a no-`signature` leg red there with different output reads `age unproven`.

The code says otherwise. `tools/run-gates/run-gates.sh:2828-2833`, the no-signature tail of `check_red_at`, returns 0, which means aged, when every non-blank line of L's output appears in the far end's (the `comm -23` at 2831). A far end red with a superset of L's lines, which is plainly different output, therefore reads `aged`. The fold's own arm pins exactly that case. `tools/run-gates/run-gates.test.sh:2123` expects `moved superset` to read `aged at R~10`. The function's header at `run-gates.sh:2779-2783` and the run-gates README at `tools/run-gates/README.md:403-409` both state the subset rule correctly. The README says a no-signature leg is aged "only while its text holds still or shrinks toward L's". The rule therefore appears in seven places, counting the code and its arm, and three of them give the other answer.

**Impact.** It is documentary only. STOPS is the binding stop contract an operator reads on a hold. It predicts `age unproven` for a shrunk-but-older red that the bar reports as `aged`, so a correct hold reads as a defect. A later edit that aligns code to the contract would silently change a verdict the arm pins. No landing changes, because neither `aged` nor `age unproven` is a number. The README says at line 404 that only a number counts toward the inherited-green stamp.

**Fix.** Reword the template clause and the dossier line to the implemented rule. A no-`signature` leg red at the far end with every non-blank line of L's output, more or not, reads `aged`. One red with output that lacks any of L's lines cannot be answered and reads `age unproven`. Re-install the guide from the template through `tools/unattended/adopt-unattended.sh`, in the same commit. A pointer to the run-gates README would be the stronger fix, because it removes the second answer rather than realigning it. From the unattended template it must go through the render token a sibling kit takes, because a shipped kit file names no `tools/<kit>/` path by literal. The dossier is not a kit file and may point at the README directly.

**Left-shift.** A gate cannot grade the meaning of a prose restatement, so this class is a documented check. The class is `two-answers-to-one-question`, which is universal. Add a "where it bit" line to `memory/gotchas/two-answers-to-one-question.md` naming this instance: one verdict rule in seven places, three of them wrong, and the arm that pinned the code could not see the prose. Replacing the dossier's restatement with a pointer shrinks the population that check has to cover.

## The ten round-1 findings, as the fold left them

This table records what this round's lenses returned against each fix. "No finding survived" means the lenses read that fix and nothing they raised survived a skeptic. It is not a proof that the fix is complete. The residues are the fold agents' own reports, listed above and not re-raised.

| Round 1 | Sev | Fold outcome in this round |
|---------|-----|----------------------------|
| F1 age probe | MED | The code closes it, and its arm pins superset, count and inside. The prose in STOPS and the dossier misstates the rule, which is F2 here. |
| F2 asks: mandate | MED | No finding survived. Residue: `spec_ask_verbs` still reads through the tolerant `expand_id_runs`. |
| F3 SEV as cover | MED | No finding survived. Residue: a REOPEN-only row still reads as cover. |
| F4 rollback deletes | MED | No finding survived. |
| F5 attribution trap | MED | No finding survived for `run-selftests.sh`. The sibling edit to `push-main.sh` opened F1 here. |
| F6 conf reader | LOW | No finding survived. Residue: `read_backlog_mode` and three older readers keep the old shape. |
| F7 carry-set owner | LOW | No finding survived. |
| F8 S6 skip | LOW | No finding survived. |
| F9 `--relocate` | LOW | No finding survived. Residue: an unstaged provenance row is invisible to the index filter. |
| F10 cache key | LOW | No finding survived. Residue: two conf-carrying worktrees recompute one entry in turn. |

## Bug classes

`gotchas.py --for-diff 869209ed..265d344c` selected 84 classes, 78 by anchor plus 6 universal, over 445 changed files. The lens brief was primed with the classes the checklist selected. Confirmed live instances:

- `trapped-signal-waits-for-the-foreground-child`: F1, a new half of the class, in which the handler exits too late for its record rather than running too late for the kill.
- `signal-trap-runs-the-exit-handler-twice`: the F5 class whose sibling fix produced F1.
- `two-answers-to-one-question`: F2.
- `fold-text-is-unreviewed-surface`: both. Every confirmed finding in this round was written by the round-1 fold.

No confirmed finding fell in `fixture-passes-by-finding-nothing`, or in arms that grade a copy instead of the shipped code, the two classes the brief prioritised. Every stage returned, so that is the lenses' answer and not a hole, bounded as stated under Run integrity. One scope limit is worth naming, though it is disclosed and not a could-not-fail. The fold's F5 source scan has a liveness guard. Its population is one kit, and its header says so. A green from it therefore says nothing about `tools/push-main.sh`, which is where F1 sits.

## Next

Fold F1 and F2 before the landing, each with its left-shift, and observe F1's arm red first. M8 owes a re-review only after a blocker, and there is none. F1's fold, though, is a signal-handling edit in the landing path. This round found its defect in exactly such a sibling edit, which nobody had armed or reviewed. A round 3 over that fold alone is therefore advised, from this round's recorded tip `265d344c`, with this round's confirmed set as `priorFindings`. It will be a few dozen lines.

Retuning note: one defect took three of the six raw findings. For a fold of this size, fewer lenses with less overlap would likely return the same set.
