**Serves:** diff-review TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3

# aStagedLane — closing diff review, round 2

*Node `a`, 2026-09-05. Round **2**. Four primed lenses — security, correctness, seams, regressions —
a skeptic stage prompted to REFUTE each finding, and this synthesis pass. Per BUILD-METHOD M8 a round
N>1 reads from the previous round's recorded tip, so this review sees the FOLD and not the code round
1 already graded.*

**Range reviewed: `387d51e0e4d03554f2db8badd343d10e36394a1a...HEAD`** — three commits (`78b3fd46`,
`2213ebcb`, `d688054d`), 382 insertions across 11 files, of which two are product: 
`tools/unattended/check-pass-order.sh` and `tools/workflows/unattended-build.js`.

## Verdict: BLOCKED

One blocker, one high. Round 1's blocker was that unit 1's S6 hardened one read to the graded commit
and left two siblings on the working tree — "fixing two of three". The fold hardened all three. It
then left the line ABOVE them, which is the line that decides which builds those three reads run
over at all. The bypass is therefore not narrower than it was in round 1; it is wider, because the
population selector silences the whole leg for every build at once rather than emptying one build's
range. The class the fold's own comment claims to have closed — `gate the CLASS, not the instance` —
is still open, one more level up the same pipeline.

Shape: raw 15, confirmed 12, refuted 3, unverified 0, **precision 0.80**. Down from round 1's 0.88,
which is the expected direction for a second pass over an already-hardened surface (§8: over
hardened code a heavy fan manufactures refuted noise).

**The 12 confirmed findings are 5 distinct defects.** Four lenses converged hard: ids 2/4/8/12 are
one defect, ids 6/9/13 are one, ids 7/10/14 are one. Convergence is evidence of reachability, not of
count, so the table below is de-duplicated and the severities in it are the ones adjudicated here —
they are what the returned `blockers` and `highs` integers count.

**What the fold got right**, stated because a review that only lists defects misreports the diff.
All three record reads did move to `HEAD:` and I confirmed each at source (`opened:` :214, the
RUN.md `base:` blob :240, the CLOSED-units region :263), plus a fourth the brief did not mention —
the waiver registry at :182. The pre-anchor walk direction is genuinely fixed: `--reverse` is gone
from the probe call at :369 and the comment at :320-331 explains the actual mechanism (`--max-count`
applies during traversal and reverses after, so `--reverse` yielded the FAR end). The `_report`
hoist is correct: `_report` is a top-level function closing over `$violations`, `$waived_ids`,
`$waived_seen`, `$waived_n` and `$previews`, all plain globals assigned in the same shell — no
subshell, no pipeline, so the pre-anchor call site's mutations survive, and I confirmed the real-tree
run still reports both waived rows. And the filtered BUILD roster does not touch the unattended path:
`skippedDone` is populated only inside `if (attended)`, so `buildUnits` is identically `ordered` when
`attended` is false. Three of the four hunt questions came back clean.

---

## Findings

| # | Sev | Site | Defect | Raw ids |
|---|-----|------|--------|---------|
| 1 | **BLOCKER** | `check-pass-order.sh:207` | The build POPULATION is still enumerated from the INDEX while all four record reads inside the loop now come from HEAD | 2, 4, 8, 12 |
| 2 | **HIGH** | `check-pass-order.sh:200-202` | The new cap validation checks the alphabet, not the range — an all-digit out-of-range value still silently disables the pre-anchor class | 1 |
| 3 | MEDIUM | `unattended-build.js:766-775` | The new empty-roster early return hard-codes a clean `note`, bypassing the DEGRADED composition the main return performs | 6, 9, 13 |
| 4 | LOW | `check-pass-order.sh:335,348` | Truncation off-by-one: the relocated test dropped the `+1` that made it exact, so a COMPLETE walk of an exactly-cap-deep window reports TRUNCATED | 7, 10, 14 |
| 5 | LOW | `check-pass-order.sh:34,57-61,436,455` | Operator-facing text still describes working-tree reads the fold moved to HEAD | 11 |

---

### 1 — BLOCKER · `tools/unattended/check-pass-order.sh:207`

**The fold moved four reads to `HEAD:` and left the line that selects which builds those reads run
over on `git ls-files`, which reads the INDEX.**

```
207:  for readme in $(git ls-files "$MEMORY_ROOT/builds/*/README.md" 2>/dev/null); do
```

Everything inside that loop is keyed off `$readme` — `$bdir`, `$slug`, and all four HEAD reads. So
hardening the reads hardened what the leg grades and not WHICH builds it grades. An uncommitted
`git rm --cached memory/builds/<slug>/README.md` drops the build from `git ls-files` while
`HEAD:<path>` still resolves, the working-tree file is untouched, and the pushed tip is byte-identical.
Three lenses reproduced it independently on two different shipped fixtures: control `graded 1 closed
unit(s)` / rc 1 becomes `graded 0 closed unit(s)` / rc 0, every counter zero.

This is round 1's blocker one level earlier in the same pipeline, and strictly wider. Round 1's
version emptied ONE build's range via an untracked `RUN.md`; this one silences the leg for every
build simultaneously and produces output byte-indistinguishable from a repo with no closed units.
The vanished build is not counted in `skipped_cutoff` or `unbuilt` — the only trace is an aggregate
`graded` count nobody diffs. Reachable without malice: a `git rm -r memory/builds/<slug>` during a
folder move, run before the commit.

**One additional mechanism the finders did not reach, which I verified and which makes this worse.**
The leg's DEAD PROBE liveness check at :141 is enumerated the same way:

```
141:  _probe=$(git ls-files "$MEMORY_ROOT/builds/*/spec/*.md" 2>/dev/null | head -1)
142:  if [ -n "$_probe" ]; then
```

An empty `ls-files` result skips the probe silently. So the same index mutation that empties the
population ALSO disables the check whose stated job is to say "no verdict below would mean anything"
— and it reads `plan_state "$_probe"` off the filesystem rather than from the graded commit. The one
guard that exists to catch this leg grading nothing shares its input with the thing it guards, which
is §7's "a guard that shares a variable with the thing it guards is not a guard".

Nothing downstream catches any of it. `run-gates.sh:837`'s `TREE_CLEAN` only decides whether a green
stamp is RECORDED (:1426); the run still exits 0. `.githooks/pre-push` tests that HEAD equals the
pushed tip, not that the index is clean. `tools/gate-legs.json` runs this leg as bare
`bash tools/unattended/check-pass-order.sh` with `subject: repo` — no scratch clone, so it grades the
live index. And the freshness-leg mitigation one lens disclosed is real but only multi-step:
`gen_build_index.py` enumerates builds via `git ls-files` too (:1772, :1875), so regenerating against
the same mutated index leaves both legs green.

**Fix** — enumerate from the graded commit, through the pinned wrapper the file's own comment at :43
says every read uses:

```sh
for readme in $(GIT ls-tree -r --name-only HEAD -- "$MEMORY_ROOT/builds/" 2>/dev/null | grep '/README\.md$'); do
```

The file already uses `GIT ls-tree -r --name-only <rev>` at :390, so the idiom is in-file. Fix :141
the same way, or make an empty probe a refusal rather than a skip — an empty population on a repo
with builds is itself a DEAD PROBE condition.

**Left-shift gate** — add an arm beside the B1 pair at `check-pass-order.test.sh:477` that runs
`git rm -q --cached memory/builds/tOrder/README.md` on the fixture and asserts rc stays 1 and
`graded 1 closed unit` still prints. Observe it RED first (§7: a gate whose failing case has not been
observed is an assertion about nothing). The existing B1 arms cannot see this class because they
mutate file CONTENT with `sed -i`, which leaves the path listed in the index — that is precisely why
the fold's own new tests passed over an open blocker.

---

### 2 — HIGH · `tools/unattended/check-pass-order.sh:200-202`

**The new cap validation checks the character class only, so an all-digit out-of-range value still
produces the exact silent green the fix's own comment says it closes.**

```
199:  PREANCHOR_CAP="${PASS_ORDER_PREANCHOR_CAP:-400}"
200:  case "$PREANCHOR_CAP" in
201:    ''|*[!0-9]*) echo "... must be a non-negative integer ..."; exit 2 ;;
202:  esac
```

I verified the chain end to end on this machine:

1. `case` accepts `99999999999999999999` — it is all digits.
2. `git rev-list --max-count=99999999999999999999 HEAD` prints `fatal: '99999999999999999999': not an integer`, and :336 swallows that on `2>/dev/null`. The walk emits zero commits, so `_n` stays 0.
3. `[ 0 -ge 99999999999999999999 ]` prints `[: 99999999999999999999: integer expected` to stderr and evaluates **false**, so :348 never prints TRUNCATED.

`pre_c` is empty, control falls to `unbuilt=$((unbuilt+1))` at :381, and neither `unbuilt` nor
`truncated` affects exit status (only `violations` and `stale`, :452-460). The leg exits 0 while the
liveness line reports `0 pre-anchor violation(s) … 0 probe(s) truncated at the
99999999999999999999-commit cap`. That is verbatim the condition the H2 comment at :193-198 was
written against: "A non-numeric value also disabled the whole pre-anchor violation class while
reporting zero truncations, which is a silent green rather than a refusal."

The value is admitted from the same tracked `.unattended.conf` allow-list the comment cites (:75
blanks it, :106 evals it), so this is the identical trust boundary — the fix narrowed the alphabet
and left the range. `_cap=0` is loud by comparison, reporting TRUNCATED for every build; only
out-of-range is silent. The stale-waiver red does not rescue it: both rows in
`memory/project/pass-order-waiver.txt` are STEP-2 violations found in-range, not pre-anchor ones, so
they keep being reported and waived and no stale row fires.

**Fix** — bound the cap rather than its alphabet, and prefer the arm that gates the class:

```sh
GIT rev-list --max-count="$PREANCHOR_CAP" HEAD >/dev/null 2>&1 || {
  echo "pass-order: git refuses --max-count=$PREANCHOR_CAP, so the pre-anchor probe would walk nothing and report nothing"; exit 2; }
```

That is this file's own doctrine — a probe that cannot move says so — applied to the value that
decides whether it can move. The cheap alternative is a length arm on the existing case
(`''|*[!0-9]*|??????????*)`), which fixes the instance and not the class.

**Left-shift gate** — extend the H2 pair at `check-pass-order.test.sh:504-514` with a third arm
declaring an all-digit out-of-range cap and asserting rc 2. H2 currently covers `not-a-number` and
`1+1` only, which is why this survived.

---

### 3 — MEDIUM · `tools/workflows/unattended-build.js:766-775`

**The new all-terminal early return hard-codes a clean `note`, so a run whose SPEC stage refused
units reports itself complete.** This is `degradation-known-but-unreported` — the gotcha class this
same file names three times in the comments around this return, including the one three lines below
it calling these counts "part of the run-integrity report, not decoration".

The early return emits `note: 'complete for ATTENDED mode — every unit was already terminal…'`
unconditionally. The main return at :816-828 composes
`specRefused.length || unbuilt.length || verdict !== 'CONVERGED' ? 'DEGRADED — …'` from the same
state. Reproduced against the file's own runtime double: attended, both units `DONE`, spec writers
returning `refused:['A-tB-1','A-tB-2']` yields
`{… "specRefused":["A-tB-1","A-tB-2",…], "note":"complete for ATTENDED mode …"}`.

Reachable without agent misbehaviour: a dead spec-writer group pushes its units into
`specced.refused` (:418) while `liveWriters >= 1` keeps the all-dead throw from firing; those units,
terminal at entry and absent from `specced.authored`, all land in `skippedDone`, emptying
`buildUnits`. The run logs `spec stage: DEGRADED` and then returns `complete`.

One correction to the finders, adjudicated down: two of them claimed the verdict half is also
reachable. It is not. In attended mode the verdict token is CONVERGED/CONVERGING from the blocker
count alone (:589-591) and CONVERGING returns earlier, and `unbuilt` is `[]` on this path by
construction. `specRefused` is the only live term — which is why this is MEDIUM and not HIGH.

**Fix** — one conditional prefix, the same test the main return uses:

```js
note: (specRefused.length ? 'DEGRADED — ' + specRefused.length + ' spec(s) refused · ' : '') +
  'complete for ATTENDED mode — every unit was already terminal, so the BUILD stage was not spawned rather than handed an empty roster',
```

**Left-shift gate** — an arm beside the H4 pair at `unattended-build.test.sh:284` with all units
terminal and a non-empty `refused`, asserting the result carries `DEGRADED`. Grep finds zero hits for
`every unit was already terminal` or `nothing to build` in that suite, and AC11 was edited in this
same diff so its second unit is `READY` — which removed the only case that would have reached the
branch. A new branch shipped with no arm, in a diff whose own subject is closing review findings.

---

### 4 — LOW · `tools/unattended/check-pass-order.sh:335,348`

**Relocating the truncation test dropped the `+1` that made it exact.** The walk now enumerates
`--max-count=$_cap` (:335) and tests `[ "$_n" -ge "$_cap" ]` after the loop (:348). With
`--max-count=N` you cannot distinguish "exactly N existed" from "N shown, more behind", so a probe
that examined its entire window and found nothing reports TRUNCATED. The pre-fold shape
(`--max-count=$((_cap+1))` with the test at the loop top, visible in `78b3fd46`) could tell them
apart.

Reproduced on the `preanchor-record` fixture, whose pre-anchor window is 2 deep: cap=1 →
`1 probe(s) truncated` (correct), cap=2 → `1 probe(s) truncated` (the walk was COMPLETE), cap=3 → `0`.
Reachable at the default cap of 400 and trivially by declaration.

No verdict flips — both arms fall through to `unbuilt++` — so the damage is confined to the
`truncated` counter on the liveness line, which is exactly the counter whose own comment at :346-347
says it exists "so a probe that gave up and a probe that found nothing" do not print the same thing.
At `depth == cap` it prints the wrong one. Conservative direction (over-reports give-ups, never hides
a violation), hence LOW.

**Fix** — restore the extra element and compare strictly. Safe now that the cap is validated:

```sh
[ -n "$_cap" ] && _mc="--max-count=$((_cap+1))"          # :335
[ -n "$_cap" ] && [ "$_n" -gt "$_cap" ] && { printf 'TRUNCATED'; return 0; }   # :348
```

Newest-first, that still drops the far end, so the H1 fix is preserved.

**Left-shift gate** — the AC13 cap arm at `check-pass-order.test.sh:429-443` uses cap=1 against a
2-deep window, so it arms cap < depth only and passes either way. Add the boundary case: exactly
`PASS_ORDER_PREANCHOR_CAP` clean commits behind the anchor, asserting `0 probe(s) truncated`.

---

### 5 — LOW · `tools/unattended/check-pass-order.sh:34, 57-61, 436, 455`

**Operator-facing text still describes reads the fold moved to HEAD.** The liveness line at :436
prints `$waived_n waived by $WAIVER_FILE` as a bare working-tree path, and the FAILED stale-row
message at :455 repeats it, while `waived_ids` comes exclusively from `HEAD:$WAIVER_FILE` (:182-190).
An operator adding a waiver row to `memory/project/pass-order-waiver.txt` to unblock a red bar reruns
the leg, watches `waived` not move, and gets no explanation.

The suite corroborates that this is a real trap rather than a style note: three waiver arms
(`:399`, `:409`, `:414`) had to add `git add -A && git commit` to keep working, with a comment
saying "COMMITTED, because the registry is read from the graded commit". A human gets no such hint.

Same drift at :34 and :57-61, where `--preview` is documented as grading "the live tree" while
`opened:`, `base:`, the CLOSED region, the waiver and the parent spec now all come from `HEAD:` —
only the `git ls-files` population and the probe are live, which is the half finding 1 is about. The
diff corrected one stale comment (`d688054d`, the THREE COUNTS miscount) and left these three.

**Fix** — `… $waived_n waived by $WAIVER_FILE as committed at HEAD …`, and amend both `--preview`
comments to "grades the real repository AT HEAD".

**Left-shift gate** — none proposed. Comment-vs-code drift is not gateable here without a predicate
that would red on prose, and §7 says an ungateable class joins the documented checklist instead. The
durable form is §6's rule: this text states, in prose beside the source, a fact the source owns.
Fixing finding 1 removes half of it by making the claim true.

---

## Refuted (3)

Recorded for the corpus audit, not for action. The skeptic stage refuted three of fifteen raw
findings; the precision drop from 0.88 to 0.80 is consistent with a second pass over a surface the
first pass already hardened, which §8 predicts.

## Notes on the hunt

Every one of the four hunt questions was answered against source, and three came back clean:

- **Remaining working-tree reads on a path whose siblings now read HEAD** — YES, and it is the
  blocker. Not among the three the brief listed: the population selector at :207, plus the liveness
  probe at :141. The record reads themselves are all four correct.
- **Does the reversed pre-anchor walk still find violations, and is truncation still counted** —
  finding YES, counting off by one at the boundary (finding 4). H1's arm confirms a violation AT the
  anchor is now graded rather than eaten by the cap.
- **Does the filtered roster break the unattended path** — no. `skippedDone` is only ever populated
  inside `if (attended)`, so `buildUnits === ordered` unattended. The unattended path is unchanged.
- **Is the `_report` hoist correct w.r.t. what it closes over** — yes. Top-level function, plain
  globals, no subshell or pipeline at the call site, so `violations`/`waived_seen`/`waived_n`/
  `previews` all mutate as intended. Verified by reading the definition and both call sites; the
  pre-anchor site at :373 now calls it instead of duplicating the waiver bookkeeping inline.

**One claim in this report is NOT independently observed, and it is named rather than borrowed
silently.** The brief states the leg's real-tree verdict as 68 graded, 2 waived, rc 0. I started that
run and it had not returned after nine minutes, so I killed it rather than block this report; the
figure above is the brief's, not mine. What I did verify directly is the part the findings depend
on: `memory/project/pass-order-waiver.txt` holds exactly two rows, both `DEPL-dGaugedVintage-*`, and
both are described in the file as spec-and-product-code-in-one-commit — STEP-2 violations found
in-range, not pre-anchor ones. So neither finding 2 nor finding 4 can move the reported counts today,
and none of the five defects changes the leg's verdict on the current tree. All five are latent,
which is the point: four of the five are silent-green shapes rather than wrong answers, and a silent
green is invisible in exactly the run you would use to check for it.
