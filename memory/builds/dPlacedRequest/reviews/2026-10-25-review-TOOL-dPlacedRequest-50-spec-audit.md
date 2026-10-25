**Serves:** spec-audit TOOL-dPlacedRequest-50@rev-1 TOOL-dPlacedRequest-51@rev-1 TOOL-dPlacedRequest-52@rev-2

# Tier-2 spec audit — build dPlacedRequest, the round-4 promotion specs TOOL-dPlacedRequest-50 to -52, ROUND 1

*This is an adversarial pre-code pass over the three specs that the round-4 spec audit promoted, dated 2026-10-25. Five lenses found defects, and five skeptic batches tried to refute each finding. This report is synthesised only from the findings that survived. Finders were gov-spec-reviewer, skeptic batches gov-skeptic, and synthesis gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md@76ef5ce13d88578d2aeceaa641bd78d589c73994, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md@bf81f62fccd9ae4adf606377ff85c1c5d0090510, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md@930dd0c1d4970f503f813610691c9d8c913564db

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker stands. Three highs do, and each must be fixed in the spec before its unit is built.
H1: 52's `flat | grep -c` criteria can never print 2.
H2: 52's oracle walks another build's landing merge when HEAD has no prepared merge.
H3: 52's oracle exits 0 when its `git log` walk dies.
By item, the tally is 19 items: 0 blocker, 3 high, 9 medium and 7 low.
By raw confirmed finding, it is 25: 0 blocker, 3 high, 12 medium and 10 low.
One defect, the `flat | grep -c` count, was reported by three lenses at two binding grades. It sits in H1 (id 1) and M1 (ids 7, 18), which name each other, and no finding is counted twice.

## Review shape

The review ran at intensity full: raw 26, confirmed 25, refuted 1, unverified 0 (0 uncertain), precision 0.96.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| failure-envelope | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

**Run integrity.**
- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 24 were judged sound and 1 was judged UNSOUND (id 13). 0 had no fix proposed, and 0 were NOT JUDGED.
- Severity on confirmed findings: 0 were UNGRADED and 2 were RE-GRADED by the skeptic (ids 7 and 16).
- Unverified findings: 0 were answered UNCERTAIN, and 0 had no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

Because every count above is zero where it should be, this run is complete.

- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and synthesis gov-synthesizer.
- Intent: 49 spec documents were supplied as `specs`, as sibling context.
- Checklist: 45 items, each assigned to exactly one of 5 lenses: coherence 9, grounding 9, reuse 9, blast-radius 9, failure-envelope 9.
- By design: 1 invariant came from the checklist's by-design block.
- Move check: no checked subject moved.

Every fix below was judged by a skeptic. Where a skeptic rejected the finder's fix, the skeptic's corrected fix is the one written here.

## High

### H1 — 52's `flat | grep -c` criteria can never print "at least 2" (id 1)

- **Where:** `TOOL-dPlacedRequest-52` §6, the `flat` definition (:278) and AC1 (:286), AC6 (:300) and AC9 (:308).
- **What is wrong:** `flat` is `sed '/^## 9\./,$d' <file> | tr -s '[:space:]' ' '`, which turns every newline into a space, so its output is one line. `grep -c` counts matching lines, so over `flat` it prints only 0 or 1. AC1 (48 names S25), AC6 (48 cites `43 S30`) and AC9 (43 names 48128) each require "at least 2".
- **Consequence:** the three criteria stay red however correctly S1, S6 and S9 are built. The builder is stuck or rewrites the check outside review. The "named in two places" property each criterion exists to check (for example S22 against AC22 in 43) is never decided.
- **Fix (judged sound):** count occurrences, not lines: `flat <file> | grep -o '<pat>' | wc -l` prints at least 2. Or grep the two named paragraphs separately with the awk extraction S15 already uses. Run each command on a hand-written two-occurrence sample and see it reach 2.
- **Gate:** a bug-class checklist entry: "a criterion that expects a count of N >= 2 over squeezed or single-line output counts occurrences (`grep -o | wc -l`), never lines (`grep -c`)". Same defect as M1.

### H2 — 52's oracle walks another build's landing merge when HEAD has no prepared merge (id 16)

- **Where:** `TOOL-dPlacedRequest-52` §2 S17 and S12, §4 "The oracle" (:190-199), §6 AC12, §8 F1.
- **What is wrong:** S17 copies only fact 1 of `check_prepared_merge`: `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD`. Every push-main landing leaves a merge on the default branch's first-parent line. On this build branch before `--prepare`, that command returns c63aabbb, dOrderedCharter's landing merge, and `$t^1..$t^2` walks its 2 commits. S12's "no prepared merge on HEAD" refusal is never reached. `check_prepared_merge` (push-main.sh:514-526) rejects such a merge only through fact 2 (first parent equals the advertised tip), which S17 drops. AC12's fixture has no merge at all, so the case the real tree always presents is never staged.
- **Consequence:** the oracle finds no `KIT_` line in the foreign commits and exits 0, S11's "clean build" answer. 34 AC59 is read "before the lander's mint" (34:544-546), 49 S3 points it at this oracle, and 52 S11 restates it as "header line, exit 0". AC59 therefore goes green at unit 34's pass without reading one dPlacedRequest commit.
- **Grade:** the finder graded blocker; the skeptic's binding grade is high, because the README close rule (:41) runs the oracle on the prepared merge, where it is correct. The vacuous pass is on the narrower pre-prepare path.
- **Fix (judged sound):** keep fact 1, then refuse with exit 2 (`version oracle: no prepared merge on HEAD`) unless `$t` is this build's merge. Either require that `git merge-base --is-ancestor $t c63aabbb` fails (the build's base is an ancestor of `$t^2`, not of `$t`), or require `$t`'s subject to begin `merge: dPlacedRequest — land onto`. Add an AC12 row whose fixture puts an older landed merge on HEAD's first-parent line under a plain branch commit and expects exit 2. Restate 34 AC59's timing so it runs on the prepared merge.
- **Gate:** a bug-class checklist entry: "a check that locates its subject by shape (the newest merge, the newest tag) proves the subject is this unit's own, and a fixture plants a foreign one of the same shape".

### H3 — 52's oracle exits 0 when its `git log` walk dies (id 22)

- **Where:** `TOOL-dPlacedRequest-52` §2 S11/S12, §4 "The oracle (S11 to S13, S17)" (:189-199).
- **What is wrong:** the verdict is `if git log … -p "$r" -- … | grep -E …; then exit 1; fi; exit 0`. There is no pipefail and nothing reads `git log`'s own status. `n` comes from `rev-list --count`, which needs no blobs, so it succeeds even when the walk will not.
- **Consequence:** when `git log -p` dies (a partial clone missing blobs offline, a bad object, a signal), grep matches nothing and the oracle exits 0, certifying "no version bump" over a walk it never read. S12 refuses a missing range so that it "never reads as an empty build", but a dead walk still does. AC11 to AC13 stage no walk failure.
- **Fix (judged sound):** S11 states that the walk's own status is checked. Capture the `git log` output to a file under the scratch directory, exit 2 with `version oracle: the walk failed` when git exits non-zero, and only then grep the file (or `set -o pipefail` and branch on `PIPESTATUS[0]`). Add a criterion: on a scratch copy with a PATH-stub `git` that answers `rev-list` and exits 128 on `log`, the oracle exits 2 and never 0.
- **Gate:** a bug-class checklist entry: "a check whose verdict is `producer | grep` checks the producer's status; a criterion stubs the producer to fail".

## Medium

### M1 — 52's `flat | grep -c` criteria, reported by the grounding and blast-radius lenses (ids 7, 18)

- **Where:** `TOOL-dPlacedRequest-52` §6 preamble (`flat`, :278) with AC1, AC6 and AC9.
- **What is wrong:** the same defect as H1. `flat` yields one line, so `grep -c` prints 0 or 1 and never the "at least 2" the three criteria need. Re-probed: `flat 43 | grep -c 'S2'` printed 1 while `grep -o 'S2' | wc -l` printed 51.
- **Consequence:** three criteria can never go green, and a count of 1 cannot tell "named in S1 and §5" from "named once", the distinction AC6 and AC9 exist to make.
- **Grade:** id 7's finder graded high; its skeptic re-graded it medium because nothing ships a wrong result. Id 18 is medium. Both bindings stand here. H1 carries id 1 at its binding high grade.
- **Fix (judged sound):** as H1: `flat <file> | grep -o '<pat>' | wc -l` for every "at least N" with N >= 2, or `grep -c` on the unsqueezed file before §9. Say once, under the `flat` definition, that `grep -c` over `flat` only answers present or absent.
- **Gate:** the H1 checklist entry.

### M2 — 52's race-arm retry keeps attempt 1's state, so AC4's "discard and pass" cannot happen (ids 2, 23)

- **Where:** `TOOL-dPlacedRequest-52` §2 S3/S4, §4 "The placed race, bounded" (:231-237), §6 AC4.
- **What is wrong:** between attempts the loop clears only `$h/once`, `$h/held` and `$h/release`. Two kinds of state survive.
  - The health log: S3 reads it for `node-lock-broken` without bounding the read to the current attempt, so attempt 1's break event also marks attempts 2 and 3 as overruns.
  - The fixture's writes: attempt 1 leaves the stored `requests/<key>.md`, the `.typed` lines and the pushed remote record (48 §4 uses one unit-19 clone and bare remote). On attempt 2, A meets a stored copy. Equal bytes send it down 30 S2's "already recorded" path, which never spawns the `requests/` `cp` (result "never placed"). Different bytes refuse it with `collision`.
  - The spec also does not say whether "never placed" inside an attempt discards or fails it, or what happens to an A that outlives its bound.
- **Consequence:** 48 AC1's asserts (A exits 0, `.typed` holds s1 alone, one remote record) cannot pass on attempt 2. AC4's "delay on the first attempt only, the arm discards it and passes" is unreachable, and the arm reports an overrun that did not happen. AC4's "no `--request` process remains" has no kill to rely on.
- **Fix (judged sound):** state the per-attempt reset whole in S4 and the §4 sketch.
  - Run each attempt on a fresh fixture (a new unit-19 clone and bare remote), or remove `requests/<key>.md` and `<key>.typed` and reset the remote's request ref.
  - Record the health log's line count at the hold and read only the lines past it.
  - "Never placed" fails at once (48 S3).
  - An A still running at its bound is killed (`kill`, then `wait`) before the next attempt.
  - Add an AC4 observation that attempt 2's `$h/held` appears and its asserts read only attempt 2's writes. Probe it by staging the 11 s delay on attempt 1 only.
- **Gate:** a bug-class checklist entry: "a retry loop in a test arm names every piece of state an attempt writes, and resets or recreates each before the next attempt".

### M3 — 50 and 48 both write `unattended.test.sh` at order 25, marked parallel (id 3)

- **Where:** `TOOL-dPlacedRequest-50` §4 Files touched, against `TOOL-dPlacedRequest-48` §4; build order README.md:213.
- **What is wrong:** order 25 is 44, 45, 48 and 50, marked "Parallel: yes". 48 writes the placed-race arm and 50 writes the AC4 rows in 47's arm, both in `tools/unattended/unattended.test.sh`. Neither spec carries the "runs in sequence" line that 44 and 48 carry for their shared write to spec 43.
- **Consequence:** under M6 `parallel-when-disjoint`, two delegated passes edit one suite file at once, and one arm can be lost or conflict. This is the class 49 AC24 gates.
- **Fix (judged sound):** add to 50 §4 Files touched, mirrored in 48 §4: "`TOOL-dPlacedRequest-48` writes this file at the same order, so the two passes run in sequence". Or move 50 to its own order.
- **Gate:** 49 AC24's gate already names this class. Run it over order 25 once 50 lands, and make the order-group check compare Files touched across every member of a parallel group.

### M4 — 52's oracle `rev-list --count` dies on a deep working directory on Windows (id 8)

- **Where:** `TOOL-dPlacedRequest-52` §4 "The oracle (S11 to S13, S17)", the `n=$(git rev-list … --count "$r")` line (:193), and its Evidence paragraph.
- **What is wrong:** the range `<40-hex>^1..<40-hex>^2` (86 chars) is passed without `--`. Git stats it as a possible filename. When the cwd path plus 86 chars passes MAX_PATH, the stat fails with "Filename too long" and git exits 128. Reproduced with a 197-char cwd on git 2.54.0.windows.1; a trailing `--` printed 2. The `git log` call at :196-197 does carry `--`. The Evidence measured only a short `%TEMP%` path.
- **Consequence:** `n` is empty, `[ "$n" -gt 0 ]` errors, and the oracle prints `walked no commit of the build` and exits 2. A clean or bump build run from a deep path (a test arm's scratch fixture under a long harness path) reads as an empty walk. AC11, AC14 and AC17 go red without cause there.
- **Fix (judged sound):** end the call with `--`: `git rev-list --no-merges --invert-grep --grep='^mint:' --count "$r" --`. Guard `n` with `case $n in ''|*[!0-9]*) echo 'version oracle: rev-list failed'; exit 2;; esac`. Add a criterion that runs the oracle from a fixture more than 180 chars deep.
- **Gate:** a bug-class checklist entry: "every git call that takes a revision range ends its revisions with `--`", checkable by grep over spec sketches and scripts.

### M5 — 52 AC19 stages the scratch-directory skip with an "unwritable" `CARD_DIR`, which chmod cannot make on NTFS (ids 9, 25)

- **Where:** `TOOL-dPlacedRequest-52` §6 AC19 (:336-339), the "with `CARD_DIR` unwritable" case, and the §7 manifest-check arm (:371).
- **What is wrong:** manifest-check.sh:653-654 skips only when `mkdir -p "$CARD_DIR" && mktemp -d "$CARD_DIR/.claims.XXXXXX"` fails. AC19 says "unwritable" and names no staging. Under Git Bash on NTFS, `chmod a-w` or `chmod 555` leaves the directory writable, and `mktemp -d` under it still succeeds.
- **Consequence:** built the obvious way, the skip is never reached on Windows nodes. The arm reds there and passes on POSIX, or the case is weakened or dropped, and S19's `no scratch directory` skip ships unobserved.
- **Fix (judged sound):** stage it in a way that fails everywhere: `: > "$s/f"; CARD_DIR="$s/f/sub"`, so `mkdir -p` fails with "Not a directory". Write that in AC19 instead of "unwritable". Have the arm assert the stage took effect (`mkdir -p "$CARD_DIR"` fails) before judging the cell.
- **Gate:** a bug-class checklist entry: "a criterion that stages a filesystem failure names its staging, never chmod, and asserts the stage took effect".

### M6 — 51 S2 re-types 44's fixture inline in 45 AC2, undoing the one-fixture rule (id 12)

- **Where:** `TOOL-dPlacedRequest-51` §2 S2 (:40-43), and `TOOL-dPlacedRequest-52` S14 (:100-104) and AC14 (:322-324), which cite it.
- **What is wrong:** 45 AC2 today reuses `TOOL-dPlacedRequest-44` AC2's fixture by reference (45:117). 51 S2 rewrites it to describe the fixture inline (base, two branch commits, 1.110 to 1.111 bump, one default-branch commit, `--no-ff` merge). The round-4 record's M6 named exactly this as a defect, and 52 S14 says "44 §6 defines its fixture once". 52 AC14 only checks that both texts say `two branch commits`.
- **Consequence:** the fixture is described in two places. Drift in the bump values, the default-branch commit or the merge subject passes AC14, so 45's re-measurement can run on a different repository from 44's oracle. The two copies agree today.
- **Fix (judged sound):** rewrite 51 S2 so 45 AC2 keeps the reference: "45 AC2 runs each row's command on `TOOL-dPlacedRequest-44` §6's fixture (the one 52 S14 defines, `· 2 commits`) and greps the record for each row". Drop the inline description. Point 52 S14's "as 51 S2 writes it" at that reference, and change AC14 to check that 45 names 44's fixture.
- **Gate:** the round-4 gate "a fixture reused across specs is defined once and cited by count" gains a check that the citing spec carries no second description (for example no `--no-ff` in 45 AC2).

### M7 — 52 retires the oracle's old exit and range but leaves 44 and 43 stating them (id 13)

- **Where:** `TOOL-dPlacedRequest-52` §2 S11, S13, S17 and §3 Edges (:178, consumes-from `TOOL-dPlacedRequest-44`).
- **What is wrong:** S11/S13/S17 restate only 44 S1, §4, AC1, AC3 and AC4. These places still state the old oracle:
  - 44 S2 (:42) and 44 §5 (:113) say the empty walk "exits 1", while 44 §4 per S11 exits 2 and exit 1 now means a found bump.
  - 44 §5 risks (:115) and §4 Evidence (:91-92) still name the merge-base form that S17 removes.
  - 43 AC24 (:300-301), which 44 S3 runs on this oracle, still reads "prints nothing", though the oracle now always prints a header.
  - 44 AC3 (:133) runs on the fixture's main tip. Under 52's oracle that tip is either the merge (a 2-commit walk) or has no merge (S12's refusal). It never prints `walked no commit`, so S13's restated AC3 cannot observe the empty walk; only 52 AC13's `commit-tree` merge reaches it.
- **Consequence:** a builder or closer reading 44 gets contradictory exit contracts for the one oracle the close runs.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** extend S11/S13/S17 and the Edges line to 44 so they restate, in 44:
  - S2 and the §5 error line: exit 2 on an empty walk.
  - §5 risks: no merge-base form; a missing merge exits 2.
  - The §4 Evidence observations.
  - The Alternatives bullet.
  - §8 F1, marked superseded by 52 F1.
  Also:
  - Restate 43 AC24 as: header line, exit 0, no `KIT_` line.
  - Move 44 AC3 onto AC13's `git commit-tree -p <tip> -p <base>` merge.
  - Add a criterion that greps `flat` of 44 for `merge-base` and for `exits 1` beside "walked no commit", expecting 0. It runs only after all of the above are amended.
- **Gate:** the existing class `retirement-inventory-misses-readers-by-value`: a spec that retires a value greps every sibling spec for the old value and lists each hit as a restated place or a named exception.

### M8 — 52 S9 sets unit 34's ceiling to 48128 without measuring 34 after its own edits (id 19)

- **Where:** `TOOL-dPlacedRequest-52` §2 S9 and S11, §6 AC9.
- **What is wrong:** S9 takes 48128 from 49 S13's rev-5 derivation. Unit 34 is already 47490 bytes at rev-7, 638 under the ceiling. Still pending: 49 S3 and 52 S11 both rewrite 34 AC59, each adds a §9 line (about 170 bytes), and each further record serving 34 adds a gen:spec-records row (about 250-300 bytes). A shorter AC59 saves roughly 90 bytes. 52 §4 Evidence holds no measurement of 34 after these edits.
- **Consequence:** AC9 is likely to go red at 52's own pass and force an unplanned cut of unit 34. The ceiling has already been raised once to fit.
- **Fix (judged sound):** in §4 Evidence, measure 34 with S11's AC59 text and both §9 lines applied after a `gen_build_index.py` render. Show the margin holds, or name the cut S9 makes in 34 (for example AC59's restated text becomes one line pointing at 44 AC1).
- **Gate:** a bug-class checklist entry: "a spec that sets a size ceiling measures the file with every pending edit and render applied, and records the margin in Evidence".

### M9 — 51 AC1 cannot see the stale row it exists to remove (id 24)

- **Where:** `TOOL-dPlacedRequest-51` §6 AC1 (:108-111), and §2 S1.
- **What is wrong:** AC1 counts that each of the three new row commands appears once and that the `-p` row reads `yes`. It never checks that 45 rev-2's bare row (`git log --first-parent <base>..HEAD` | "no — the default branch's line only", 45.md:72) is gone. That state is AC1's own Red-when. AC2 runs the commands and never reads the record. No criterion runs row 2's `--name-status` form.
- **Consequence:** a build that appends the split rows and keeps the old one is green on AC1 and AC2, and the record ships with contradicting rows, the defect the unit exists to remove.
- **Fix (judged sound):** add an absence check to AC1: `grep -cE 'git log --first-parent <base>\.\.HEAD` *\|' <record>` prints 0, or `grep -c 'default branch.s line only'` prints 0. Observe its Red-when by planting the rev-2 row beside the new rows in a scratch copy. Spell the presence greps `grep -cF -e '--first-parent …'` (see L2). Have AC2 also run the `--name-status` form and expect `M tools/unattended/unattended.sh` under the merge.
- **Gate:** a bug-class checklist entry: "a criterion for a replaced row asserts the old row's absence and observes its red by planting it".

## Low

### L1 — 51 S1 spells the second row differently from §4 and AC1 (ids 4, 20)

- **Where:** `TOOL-dPlacedRequest-51` §2 S1 (:36-38) against the §4 table (:65) and §6 AC1 (:107).
- **What is wrong:** S1 writes "`git log --first-parent <base>..HEAD` with `-p` or `--name-status`". §4 and AC1 write `git log --first-parent -p <base>..HEAD`, and AC1 greps that exact string. Id 20 also reports the `grep -cF` option parse, which L2 carries.
- **Consequence:** a row written from S1's text lacks the substring and AC1 prints 0 for it. §4 gives the exact table, so the effect is limited to wording.
- **Fix (judged sound):** restate S1's second row in §4's spelling: "`git log --first-parent -p <base>..HEAD`, or `--name-status`".
- **Gate:** the existing class `two-answers-to-one-question`: a string a criterion greps for appears in one spelling across S, §4 and §6.

### L2 — 51 AC1's `grep -cF` patterns begin with `--` and parse as options (ids 5, 10)

- **Where:** `TOOL-dPlacedRequest-51` §6 AC1 (:105-110).
- **What is wrong:** every pattern AC1 greps begins with `--`. `grep -cF '--first-parent --no-merges <base>..HEAD' <record>` prints "unknown option" and exits 2 without a count.
- **Consequence:** the criterion as written errors instead of measuring. The error is loud and `-e` cures it, but the criterion then works only by an unreviewed tweak.
- **Fix (judged sound):** write it `grep -cF -e '<row command>' memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md`, or `grep -cF -- '<pattern>' <file>`.
- **Gate:** a bug-class checklist entry: "a criterion's grep passes its pattern through `-e` or after `--`"; run each criterion's literal command once at spec time.

### L3 — 50's Evidence cites 47 at stale line numbers (ids 6, 11)

- **Where:** `TOOL-dPlacedRequest-50` §4 Evidence, first bullet (:78-79).
- **What is wrong:** it cites 47 S1 at `:33-35` and AC1 to AC3 at `:111-114`, `:115-117` and `:118-120`. Those match 47 at 18818d631. The commit that added 50, d0ea82ecc, also shifted 47, which now has S1 at :34-36 and AC1, AC2 and AC3 at :114-117, :118-120 and :121-123.
- **Consequence:** a reader lands on the fixture paragraph and the wrong criteria. No behavioural effect.
- **Fix (judged sound):** cite 47 by label (S1, AC1 to AC3), or by the current lines above.
- **Gate:** a bug-class checklist entry: "cross-spec evidence cites by item label, not line number".

### L4 — 52 F1 overturns 44 F1 without naming or amending it (id 14)

- **Where:** `TOOL-dPlacedRequest-52` §8 F1 (:375-383) and S17 (:112-116).
- **What is wrong:** 44 §8 F1 (:148-152) is RESOLVED as "`HEAD^1..HEAD^2` on the prepared merge and the merge-base form elsewhere" and rejects (b) on tracking-ref freshness. 52 F1 resolves the opposite way. Neither 52 F1 nor S17 names 44 §8; S17 lists only 44 S1, §4 and AC1.
- **Consequence:** 44 keeps a live resolution for a form that no longer exists, and the next reader may restore it. What gets built does not change.
- **Fix (judged sound):** have 52 F1 name 44 F1 as the decision it supersedes. Add to S17: "44 §8 F1's resolution is amended in place to (a') the lander's fact-1 derivation alone, refusing with exit 2, superseded by TOOL-dPlacedRequest-52 F1", with a §9 line in 44. Cover it in AC17 (`flat 44 | grep -c 'merge-base form elsewhere'` prints 0). Overlaps M7's corrected fix, which also marks 44 F1 superseded.
- **Gate:** a bug-class checklist entry: "a resolved fork that reverses a sibling's resolved fork names it and amends it in place".

### L5 — 52 AC21 re-plants 50's chain in 47's arm, with no edge between 50 and 52 (id 15)

- **Where:** `TOOL-dPlacedRequest-52` §6 AC21 (:343-345) and §3 Edges (:172-183).
- **What is wrong:** 50 S1 adds 47 AC4: a `renews: no` chain of a tip sighted a minute ago, an unsighted middle and a start sighted a minute ago, expected live, with an unset row and a `-` row. 50 §3 hands the malformed `seen-utc` case to 52. 52 AC21 specifies the same chain with a `2026-10-2` middle stamp but names "unit 26's chains for the walk" as its fixture. 52's Edges have no line to 50, and 50's have none to 52.
- **Consequence:** 47's arm gets two separately planted copies of one chain that can drift, and the torn-stamp case does not sit beside the unset and `-` rows it belongs with. No behavioural change.
- **Fix (judged sound):** restate 52 AC21's second clause as a third row of 47 AC4 (unit 50 S1's fixture): a middle commit whose `seen-utc` is `2026-10-2`, expected `live`. Add `consumes-from TOOL-dPlacedRequest-50 — 47 AC4's rows, which S21 extends with a torn-stamp row` to 52's Edges, mirrored as a hands-off in 50.
- **Gate:** a bug-class checklist entry: "a hand-off named in one spec's §3 has a matching edge in the receiving spec".

### L6 — 51 §5 claims the gotchas checklist line changes, but only the body does (id 21)

- **Where:** `TOOL-dPlacedRequest-51` §5 observability.
- **What is wrong:** §5 says the checklist line gotchas.py prints for a lander diff "now names the vacuous pair". gotchas.py (:278) prints only the front-matter `description`, and 51 S1 edits only the body table.
- **Consequence:** the readiness line claims an effect that will not occur. A reviewer sees the same text as before.
- **Fix (judged sound):** restate the line as "none: the description line is unchanged; the pair is named in the record body". Or, if the checklist is meant to name it, edit the front-matter description and regenerate memory/gotchas/INDEX.md.
- **Gate:** a bug-class checklist entry: "an observability claim names the command that shows it and was run once at spec time".

### L7 — 52 S26 does not say which `renews:` line wins when a commit carries two (id 26)

- **Where:** `TOOL-dPlacedRequest-52` §2 S26 (:148-151), §4 "The walk, per tail, merged".
- **What is wrong:** the walk reads "a line beginning `renews:`, its value trimmed" and says nothing about duplicates. The driver's claim reader (unattended.sh:2177-2178) splits on `": "` and keeps the first occurrence.
- **Consequence:** `renews: no` then `renews: -` could resolve differently, and `-` versus `no` decides whether a take-over is allowed. No writer emits a duplicate key and no other reader of `renews` exists today, so the ambiguity is unreachable now.
- **Fix (judged sound):** S26 states "the first `renews:` line wins, as `read_claims` keeps the first occurrence of every key". AC26 gains a row: a commit carrying `renews: no` then `renews: -` under a fresh tip over an old start, expecting `stale`.
- **Gate:** a bug-class checklist entry: "a new reader of a trailer key states its duplicate rule and matches the existing reader's".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=26 confirmed=25 refuted=1 unverified=0 blocker=0 high=3 medium=12 low=10 agents=11 out-tokens=141055

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6 AC1, AC6, AC9 (and the `flat` definition above AC1) | high | high | confirmed | 52:278 defines flat as `sed '/^## 9\./,$d' <file> \| tr -s '[:space:]' ' '`. That squeezes newlines, so its output is one line. AC1 (:286), AC6 (:300) and AC9 (:308) each require `flat … \| grep -c <pat>` to print 'at least 2'. grep -c counts matching lines, so on a single line it can only print 0 or 1. I re-ran the finder's sample: two occurrences squeezed to one line give a count of 1. The three criteria cannot pass on any build, however correct. | sound | - |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S4, section 4 'The placed race, bounded', section 6 AC4 | medium | medium | confirmed | The attempt loop in 52 §4 (:231-237) clears only $h/once, $h/held and $h/release, and S4 (:65-70) says only that the placement is re-run. Neither names a fresh fixture. 48 §4/:119 uses one unit-19 clone and bare remote, and its asserts are rcA=0, cmp of requests/<key>.md with a.md, .typed = s1 alone and one remote record. Under 30 S1/S2, a stored copy left by the overrun attempt sends attempt 2's A down the equal-bytes 'already recorded' path, which never spawns the requests/ cp, so the result is 'never placed'. If the stored bytes differ instead, A is refused with collision. Either way 52 AC4's 'discards the first and passes' cannot be reached as specified. | sound | - |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md:section 4 Files touched (against TOOL-dPlacedRequest-48 at the same order 25) | medium | medium | confirmed | README.md:213 shows order 25 as 44, 45, 48 and 50, marked Parallel yes. The Files touched sections show that 48 writes `tools/unattended/unattended.test.sh: the placed-race arm` and 50 writes `tools/unattended/unattended.test.sh: the AC4 rows in 47's arm`. Neither carries the 'runs in sequence' line that 44 and 48 both carry for their shared write to spec 43. Grepping 50 and 48 for 'in sequence' finds only the 43 note. | sound | - |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 2 S1 against section 4 table and section 6 AC1 | low | low | confirmed | 51:36 (S1) spells the second row as '`git log --first-parent <base>..HEAD` with `-p` or `--name-status`'. The §4 table at :65 and AC1 at :107 use `--first-parent -p <base>..HEAD`, and AC1 greps exactly that string. A row written from S1's wording would not contain the substring AC1 greps for. | sound | two-answers-to-one-question |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 6 AC1 | low | low | confirmed | 51 AC1 (:105-107) says to run `grep -cF` once per row pattern, and every pattern begins with `--`. I ran `grep -cF '--first-parent' <51>`: it printed 'grep: unknown option -- first-parent' and exited with rc=2. Composed as the criterion describes it, the command errors before it prints a count. | sound | - |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md:section 4 Evidence | low | low | confirmed | 50:78-79 cites 47 S1 at :33-35 and AC1, AC2 and AC3 at :111-114, :115-117 and :118-120. At HEAD, grep over 47 puts S1 at 34 and AC1, AC2 and AC3 at 114, 118 and 121. The citations are stale and only the citations are affected. | sound | - |
| 7 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6, the `flat` definition and AC1, AC6, AC9 | high | medium | confirmed | 52:278 defines flat as `sed '/^## 9\./,$d' <file> \| tr -s '[:space:]' ' '`. That turns every newline into a space, so the output is a single line and `grep -c` can only print 0 or 1. Re-run: `flat …-48.md \| grep -c 'S25'` printed 0. `flat …-43.md \| grep -o 48128 \| wc -l` printed 1. AC1 (:286), AC6 (:300) and AC9 (:308) each require 'at least 2' from `grep -c` over flat output, which cannot happen. The effect is three criteria that can never go green. That blocks the build or forces an unreviewed rewrite, but nothing ships a wrong result, so the grade is medium. | sound | - |
| 8 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 4 'The oracle (S11 to S13, S17)', the `n=$(git rev-list … --count "$r")` line, and its Evidence paragraph | medium | medium | confirmed | 52:193 reads `n=$(git rev-list --no-merges --invert-grep --grep='^mint:' --count "$r")` with no `--`. The `git log` call at :196-197 does carry `-- paths`. I reproduced it in verify-skeptic/r, with a cwd of 197 chars (pwd -W) and a two-branch-commit --no-ff fixture. `git rev-list --count "$t^1..$t^2"` printed `fatal: failed to stat '…^1..…^2': Filename too long`, rc=128. The same command with a trailing `--` printed 2. git 2.54.0.windows.1. With n empty, `[ "$n" -gt 0 ]` errors and the oracle takes the 'walked no commit' exit 2. That only happens on deep paths, so the effect is contained. | sound | - |
| 9 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6 AC19, the 'with `CARD_DIR` unwritable' case, and the section 7 manifest-check arm | medium | medium | confirmed | manifest-check.sh:653-654 skips only when `mkdir -p "$CARD_DIR" && mktemp -d "$CARD_DIR/.claims.XXXXXX"` fails. AC19 (52:338) and the §7 arm (:371) stage this as an 'unwritable CARD_DIR'. Re-probe in verify-skeptic: after `chmod a-w ro`, `ls -ld` still showed drwxr-xr-x and `mktemp -d ro/.claims.XXXXXX` succeeded. A chmod-staged case therefore never reaches the skip on this Windows node. The fix's staging does reproduce the skip: `: > cardfile; mkdir -p cardfile/sub` failed with 'Not a directory', rc=1. | sound | - |
| 10 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 6 AC1 | low | low | confirmed | 51 AC1 (:108-110) tells the builder to run `grep -cF` once per row command, and every pattern begins with `--`. Running `grep -cF '--first-parent --no-merges <base>..HEAD' memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md` printed `grep: unknown option -- first-parent --no-merges <base>..HEAD`, rc=2. The error is loud and adding `-e` cures it, so the grade is low. | sound | - |
| 11 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-50.md:section 4 Evidence, first bullet | low | low | confirmed | 50:78-79 cites 47 S1 at :33-35 and AC1/AC2/AC3 at :111-114/:115-117/:118-120. In the current tree, `grep -n` over 47 puts S1 at 34, AC1 at 114, AC2 at 118 and AC3 at 121. The cited numbers do match 47 as it stood at 18818d631 (S1:33, AC1:111, AC2:115, AC3:118). The same commit d0ea82ecc that added 50 then shifted 47, so the citations are stale against the tree they ship with. Cosmetic only. | sound | - |
| 12 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 2 S2 (and 52 S14, which cites it) | medium | medium | confirmed | 45:117 has AC2 reuse `TOOL-dPlacedRequest-44` AC2's fixture by reference. 51 S2 (:40-43) rewrites 45 AC2 in place to re-type that fixture inline (base, two branch commits, 1.110->1.111 bump, one default-branch commit, --no-ff merge). 52 S14 (:100-104) says 'One fixture, one count. 44 §6 defines its fixture once', and AC14 (:322-324) only checks that both say `two branch commits`. The round-4 record for M6 (reviews/…-44-spec-audit.md:118-124) names the defect as '44 and 45 describe the shared fixture two ways' and gates 'a fixture reused across specs is defined once … and cited by count'. As written, the shared fixture is described twice, and any drift outside the count passes AC14. The two copies agree today, so the effect is contained. | sound | - |
| 13 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S11, S13, S17 and section 3 Edges (consumes-from TOOL-dPlacedRequest-44) | medium | medium | confirmed | Re-read spec 44, which is pinned with spec 52's blob verified by hash-object. Several places still state the old oracle and nothing in 52 restates them. 44 S2 at :42 says 'walked no commit of the build' and 'exits 1'. 44 §5 at :113 says 'an empty walk exits 1'. 44 §5 risks at :115 still says 'takes the merge-base form'. 44 Evidence at :91-92 still says 'took the merge-base form ... exited 1'. 52 S11/S13/S17 (:89-116) restate only 44 S1, §4, AC1, AC3 and AC4, and the Edges line at :178 names only 'the oracle, its fixture and AC1, AC3 and AC4'. 44 AC3 at :133 runs on 'that fixture's main tip'. Under 52's oracle (:190-195), that tip either is the merge (a 2-commit walk, exit 0 or 1) or has no merge (S12's 'no prepared merge', exit 2). Either way it never prints 'walked no commit', so S13's restated AC3 cannot observe the empty walk. Only 52 AC13's commit-tree merge reaches that line. 43 AC24 at :300-301 still reads 'prints nothing'. The defect is real and contained to the spec text. | unsound | retirement-inventory-misses-readers-by-value |
| 14 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 8 F1 (and S17) | low | low | confirmed | 44:148-152 F1 is RESOLVED as (a), 'HEAD^1..HEAD^2 on the prepared merge and the merge-base form elsewhere'. It rejects (b) because it 'depends on a tracking ref's freshness'. 52 F1 (:375-383) resolves the opposite way: the fact-1 derivation alone, with no merge-base. Neither 52 F1 nor S17 (:112-116) names or amends 44 §8. S17 lists only '44 S1, §4 and AC1'. After 52 lands, 44 keeps a live resolution for a form that no longer exists. That misleads a reader but does not change what gets built. | sound | - |
| 15 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6 AC21 and section 3 Edges (no edge to TOOL-dPlacedRequest-50) | low | low | confirmed | 50 S1 (:34-40) adds 47 AC4. That is a three-commit `renews: no` chain: a tip sighted a minute ago, an unsighted middle and a start sighted a minute ago, expected live, with an unset row and a `-` row. 50 §3 (:51) hands the malformed `seen-utc` shape test to 52. 52 AC21 (:343-345) specifies the same chain with a `2026-10-2` middle stamp, and its stated fixture (:280) is 'unit 26's chains for the walk', not 47 AC4. 52's Edges (:172-183) have no line to 50, and 50's Edges (:55) have only 47. A grep of 52 for 'dPlacedRequest-50' matches only the records table. The result is a duplicated plant and a missing edge pair. It does not change behaviour. | sound | - |
| 16 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S17 and S12, section 4 'The oracle', section 6 AC12, section 8 F1 | blocker | high | confirmed | Re-ran the probe on this build branch. `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD` printed c63aabbb4a73d44315dd5dd1219ff1dac5055cf8. Its subject is 'merge: dOrderedCharter — land onto origin/main at cdfbd1cf'. The walk count `$t^1..$t^2` printed 2. So 52's §4 oracle (:190-199) never reaches the S12 refusal (:191) off this build's prepared merge. It walks another build's 2 commits and exits 0, which is S11's 'clean build' answer. push-main.sh:514-526 shows that check_prepared_merge rejects such a merge only through fact 2 (first parent equals the advertised tip), and S17 drops fact 2. 34 AC59 (:544-546) is read 'before the lander's mint'. 49 S3 points it at this oracle, and 52 S11 restates it as 'header line, exit 0'. Read at that time, it passes vacuously. AC12's fixture has no merge at all, so the real-tree case is never staged. I grade it high rather than blocker: the README close rule (:41) runs the oracle on the prepared merge, where it is correct. The vacuous pass happens on the narrower pre-prepare path. | sound | - |
| 17 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S11, S12, S13, S17; section 3 Edges line to TOOL-dPlacedRequest-44 | medium | - | refuted | duplicate of id=13. It reports the same un-restated 44 S2 (:42), §5 error line (:113) and §5 risks line (:115) against 52 S11/S13/S17 and the Edges line at :178, which I confirmed under id=13. It adds the Alternatives bullet (:104-105) and AC2's subject clause, which are further instances of the same gap. | unsound | amendment-leaves-its-other-half-standing |
| 18 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6 preamble ('flat') with AC1, AC6, AC9 | medium | medium | confirmed | 52 §6 (:278) defines `flat` as `sed ... \| tr -s '[:space:]' ' '`, which turns every newline into a space. Re-probed: `flat 43 \| wc -l` printed 0, so the output is one unterminated line. `flat 43 \| grep -c 'S2'` printed 1, while `grep -o 'S2' \| wc -l` printed 51. AC1 (:286), AC6 (:300-301) and AC9 (:308-309) each require `grep -c` over `flat` output to print 'at least 2'. That can never happen, so a correct build cannot meet these three criteria as written. | sound | - |
| 19 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S9 and S11, section 6 AC9 | medium | medium | confirmed | `wc -c` on 34.md printed 47490 at rev-7, which leaves 638 bytes under 52 AC9's 48128. Two edits to 34 are still pending: 49 S3 (49.md:56) and 52 S11 both rewrite AC59, and 34.md:544-546 still holds the `git diff c63aabbb..HEAD` form. Each spec that edits 34 adds a §9 line (rev-7's line runs about 170 bytes over two lines). 34's gen:spec-records rows run about 300 bytes each, and new rows have already appeared (the 50 promoted-fix return and brief), which is why 34 now sits above 43 AC22's current 47104 target. A shorter AC59 saves roughly 90 bytes. Two §9 lines plus one or two new record rows come close to the margin or exceed it. 52 §4 Evidence holds no measurement of 34 after its own edits, so the claim stands. The consequence is a criterion that is likely to go red at 52's own pass and force a cut, which is contained. | sound | - |
| 20 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 2 S1 vs section 4 table and section 6 AC1 | low | low | confirmed | 51.md:36-38 (S1) words the second row as `git log --first-parent <base>..HEAD` with `-p` or `--name-status`, while the §4 table and AC1 spell it `git log --first-parent -p <base>..HEAD`, or `--name-status`. Re-probed: `grep -cF '--first-parent --no-merges <base>..HEAD' <record>` printed `grep: unknown option -- first-parent ...` and exited 2. With `-e` the same grep runs (it printed 0, because the section is not built yet). §4 gives the exact table, so the impact is limited to wording and how the probe is typed. | sound | - |
| 21 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 5 observability | low | low | confirmed | Re-ran `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh`. The record's checklist entry printed only its name, the front-matter description and its path, with no body text. gotchas.py:278 takes only `description` from the front matter. 51 S1 edits only the body table and leaves the description untouched, so §5's observability line ('now names the vacuous pair') claims an effect that will not occur. Only a readiness note is wrong. | sound | - |
| 22 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S11/S12, section 4 'The oracle (S11 to S13, S17)' | high | high | confirmed | 52.md:189-199. The sketch sets no pipefail and never reads git log's own exit status. `n` comes from `rev-list --count`, which needs no blobs. The verdict is `if git log ... -p "$r" -- ... \| grep -E ...; then exit 1; fi; exit 0`. If the git log walk dies (for example a partial clone missing blobs while offline, or a bad object), grep receives no input or partial input and fails to match, and the oracle exits 0, certifying 'no version bump' over a walk it never finished. AC11 to AC13 stage no failure of the walk. The path is narrow, but on it a check certifies something it did not check, which makes it high under the rubric. | sound | - |
| 23 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S3/S4, section 4 'The placed race, bounded' | medium | medium | confirmed | 52.md:231-237. The sketch's only reset between attempts is `clear $h/once $h/held $h/release`. S3 (:62-64) reads 'the health log' for `node-lock-broken` without bounding the read to the current attempt, so a break event from attempt 1 also marks attempts 2 and 3. 48 S2 (48.md:40-45) has A complete its copy, leaving the stored `requests/<key>.md`, `.typed` and the remote record in place. Attempt 2's A then meets an existing request and may never reach the `cp` window, or it runs a race other than the one 48 S2 asserts. S4 says 'never placed' still touches release, but it does not say whether 'never placed' discards the attempt or fails it, and nothing kills an A that outlives its bound. As written, AC4's 'first attempt only ... discards and passes' case is not reliably reachable. The defect is confined to the test arm. | sound | - |
| 24 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-51.md:section 6 AC1 (and section 2 S1) | medium | medium | confirmed | 51.md:108-111. AC1 counts only the three new fixed strings (each must print 1) and checks that the `-p` row reads `yes`. The stale row from 45 rev-2 (45.md:72, `git log --first-parent <base>..HEAD` \| 'no — the default branch's line only') matches none of the three strings, so a build that keeps it next to the new rows passes AC1. AC1's own 'Red when' describes exactly that state, so AC1 as written cannot observe its own red. AC2 runs commands and never reads the record, and no criterion runs the `--name-status` form. The record could ship with contradicting rows, a contained documentation defect. | sound | - |
| 25 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 6 AC19 | medium | medium | confirmed | Spec 52 is at the pinned blob 930dd0c. Its AC19 (line 336-339) says only 'with `CARD_DIR` unwritable', and its §6 arm line (371) says only 'an unwritable `CARD_DIR`'. Neither says how to stage that. I re-ran the probe in my scratch dir: `mkdir -p ro && chmod 555 ro && mkdir -p ro/x && mktemp -d ro/x/.c.XXXX` printed `ro/x/.c.hcrz` and then WRITABLE. So on this Git Bash/NTFS platform chmod does not block the `sd=$(mkdir -p "$CARD_DIR" && mktemp -d …)` line at manifest-check.sh:653-654, and the skip is never reached. A file planted where the directory should be does make it fail: `: > ff; mkdir -p ff/sub` printed 'Not a directory'. The case reds for a staging reason rather than passing falsely, so the damage is contained: medium. | sound | - |
| 26 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-52.md:section 2 S26, section 4 'The walk, per tail, merged' | low | low | confirmed | Spec 52 S26 (lines 148-151) says the walk reads 'a line beginning `renews:`, its value trimmed'. It does not say which line wins when the key occurs twice. The cited reader at unattended.sh:2177-2178 splits on `": "` and keeps the first occurrence (`!(k in v)`), as the finding says. Two parts of the impact claim are weaker than stated. A grep of tools/ and skills/ for 'renews' finds no reader of the `renews` key today, so there is no 'other reader' to disagree with yet. And no writer emits a duplicate key. What remains is a real but unreachable ambiguity in the spec: low. | sound | - |
