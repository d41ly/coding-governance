# TOOL-aWokenSentinel-22 — check 34's two refusal branches unit 16 leaves unarmed get their arms: the marker with no sha and the marker the remote default branch does not reach, each read RED first

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 830c46e8 · streams tooling · order 22

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H2 (round 3, raw ids 5, 17 and 27): `TOOL-aWokenSentinel-16` replaces the
string compare at `tools/unattended/unattended.sh:2500` with four `fail 34` sentences, arms two of
them in its S3 — the all-zero marker reads `a commit this clone does not hold`, the parent-commit
marker reads `does not contain the witness` — and lists `harness arms (fail branches armed or
pinned)` among its gates. `tools/memory-tree/check-arms.py` discovers `unattended.sh` (it defines
`fail() {` at `:390`), keys every `fail 34 "` call site as a branch, and its `--check` reds any
branch with no positive assertion naming its own failure text in `unattended.test.sh` and no row in
`memory/project/unarmed-branches.txt`, which is shrink-only and holds no check-34 row. As specced
the close's bar reds on the `carries no commit sha` and `does not reach` branches. Spec 16 is
folded at its rev-2 to seven branches of one check with its third read pinned; this unit arms the
two branches it does not, over the suite's marker fixture, each observed RED first against a driver
copy that still holds the equality compare, so every check-34 branch is armed before the close and
the leg spec 16 names is green rather than red on the unit that named it.

## 2. Scope (IN)

- **S1** — An arm in `tools/unattended/unattended.test.sh`'s marker region (`:4514` to `:4556` at
  this unit's base): the marker written as `landed main at nothing by push-main`, which carries no
  40-hex token, makes `--landed tRun` print `the lander marker carries no commit sha` and
  `marker holds:` followed by that line, and the record's `phase:` stays `LANDING`. Observed by
  AC1.
- **S2** — A second arm in the same region: one commit made on a scratch branch off the run
  branch's HEAD and never pushed, the marker naming it, makes `--landed tRun` print `the lander
  marker names a commit the remote default branch does not reach` with `marker <sha> against
  refs/heads/main`, and the record stays at `LANDING`; the same marker after `git push origin
  <scratch>:main` reads `phase LANDED`, because a later landing that contains this one is the
  ordering spec 16 §4 tolerates. Observed by AC2.
- **S3** — Each arm is observed RED first against a driver copy at `12513c25`, the sha spec 16
  grounded against, with `lib-unattended.sh` beside it, where both markers read `names a different
  commit` and neither new sentence prints. Observed by AC1 and AC2.
- **S4** — At the tip `python3 tools/memory-tree/check-arms.py --report` lists every check-34
  branch of `tools/unattended/unattended.sh` as armed and `memory/project/unarmed-branches.txt`
  carries no row for check 34. Observed by AC3.

## 3. Non-goals (OUT)

- **No change to the predicate.** The four reads and their sentences are unit 16's; this unit
  reads two of them and adds no sentence, so the branch count `check-arms.py` keys is unit 16's
  count.
- **No re-arm of the two sentences unit 16 arms.** S3 of spec 16 owns the all-zero arm and the
  parent-commit arm; a second assertion on the same text would be a duplicate the leg cannot tell
  from the first.
- **No pin.** `unarmed-branches.txt` is shrink-only and the two branches are armable in the fixture
  the suite already has; a pin here would be an exemption where coverage costs two arms.
- **No arm for the `is-ancestor "$msha" "$ASHA"` read's SUCCESS.** The accepting arm at `:4551`
  is that read passing; the refusal is S2's, and spec 16 AC4 pins the read's presence by grep.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-16` — the predicate at check 34 with its four sentences,
  the fixture `origin` the marker region pushes to, and the moved all-zero and parent-commit arms
  this unit's two sit beside. Without the predicate neither sentence exists to read.
- **consumes-from** external — `tools/memory-tree/check-arms.py`'s discovery and arming rule, and
  the suite's marker fixture at `tools/unattended/unattended.test.sh:4514` to `:4556`, whose
  `fixture` and `git push -q -f origin HEAD:main` lines put the run on the remote arm.
- **hands-off** external — nothing.

## 4. Design

### The two arms, beside the accepting one

```
# the marker carries NO sha — a touched file, not evidence
printf 'landed main at nothing by push-main\n' > "$GCD/tmarker"
out=$(run --landed tRun)
hit "$out" "the lander marker carries no commit sha, so it is a touched file and not evidence"
hit "$out" "marker holds: landed main at nothing by push-main"
same "no-sha marker leaves the record at LANDING" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"

# the marker names a commit that CONTAINS the witness but was never pushed
git branch -f tscratch HEAD; git checkout -q tscratch; fixture; _unpushed=$(git rev-parse HEAD); git checkout -q -
printf 'landed main at %s by push-main\n' "$_unpushed" > "$GCD/tmarker"
out=$(run --landed tRun)
hit "$out" "the lander marker names a commit the remote default branch does not reach"
hit "$out" "marker $_unpushed against refs/heads/main"
same "unpushed marker leaves the record at LANDING" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"
# ...and pushed, the same marker is a LATER landing that contains this one — accepted, spec 16 §4
git push -q -f origin tscratch:main 2>/dev/null
out=$(run --landed tRun)
miss "$out" "does not reach"
same "a later landing containing this one is accepted" "$(grep -c '^phase: LANDED' memory/builds/tRun/RUN.md)" "1"
```

`fixture` is the suite's own commit-making helper, which is how the scratch commit contains HEAD:
it is made on top of it. The first `hit` of each pair is the branch's own failure text, which is
what `check-arms.py` reads as an arm; the second pins the interpolated tail, so a sentence that
names the wrong sha is red. The `same` on `phase: LANDING` is the write-before-check property
`TOOL-dScaffoldedMirror-22` fixed and spec 16 §10 relies on: a refusal leaves the record untouched.
The pushed half of the second pair is the positive control that separates "not reachable" from "not
containing": the same marker, one push later, is accepted.

### The staged break

A driver copy read out of history — `git show 12513c25:tools/unattended/unattended.sh` into a
scratch kit dir with the lib beside it, the way the stripped-copy arm at `unattended.test.sh:2092`
carries the lib — and `SCRIPT` pointed at the copy for the two invocations. That driver holds the
equality compare, so the no-sha marker and the unpushed marker both read `names a different
commit` and neither `hit` above finds its text. The break is history rather than an edit because
at this unit's order the tree's driver already carries unit 16's predicate, and the reading that
proves the arms can fail is the one the predicate replaced.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `tscratch` | a branch name inside the fixture clone | no cell; fixture state |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.test.sh` | the two arms and the pushed control in the marker region, after the parent-commit arm spec 16 adds |

### Alternatives rejected

- **Fold the two arms into spec 16's S3.** The audit's own fix. Spec 16's rev-2 already re-agrees
  five sections; a unit that owns the predicate and seven branches and five arms is the two
  mechanisms in one spec BUILD-METHOD M2 makes unreviewable, and the closing diff could not tell
  which half a finding lands on.
- **Pin the two branches in `unarmed-branches.txt` with a reason.** Coverage was one fixture away;
  an exemption is not coverage (charter §7).
- **Read the no-sha branch through a marker that is an empty file.** `head -1` of an empty file is
  an empty line, `grep -oE '[0-9a-f]{40}'` prints nothing, and the sentence prints — but an empty
  marker is also what a lander that crashed mid-write leaves, and the arm should name the
  touched-file shape spec 16's sentence describes, which is a line with words and no sha.

## 5. Production-readiness checklist

- security — N/A; two suite arms over a scratch clone.
- perf / scale — two `--landed` runs and one push in a fixture already built, seconds.
- error / empty / loading states — the scratch branch is deleted with the fixture; a `hit` that
  finds no text prints the whole output, as the helper does.
- observability — each arm names the branch text and the sha it expected.
- risks — the region's fixture pushes `HEAD:main` with `-f`, so the pushed control leaves `origin
  main` at the scratch commit; the arm that follows in the region re-pushes `HEAD:main` before its
  own read, as every marker arm already does. A future sibling arm inserted between them inherits
  that state and must re-push, which the region's own comment says.
- testing — §6; the two arms and the control, and the copy at `12513c25`.
- migration — N/A.
- user docs — none.

## 6. Acceptance criteria

The fixture is the suite's marker fixture at `tools/unattended/unattended.test.sh:4514`: a scratch
clone with a fixture `origin`, `LANDER_MARKER="tmarker"` in the conf, the record at `LANDING`, HEAD
pushed to `origin main`, and the marker written by `printf` under the git common dir. The staged
break for AC1 and AC2 is the driver at `12513c25` with the lib beside it.

- **AC1** — When the marker holds `landed main at nothing by push-main`,
  `bash tools/unattended/unattended.sh --landed tRun` prints `carries no commit sha` and
  `marker holds: landed main at nothing`, and `grep -c '^phase: LANDING'` over the record prints 1;
  against the driver at `12513c25` the same run prints `names a different commit` and neither
  phrase.
  Red when: a marker with no sha is accepted or read as a stale sha, which is a touched file
  standing in for evidence; or the refusal writes the phase, which is the write-before-check class.
- **AC2** — When the marker names one commit made on a scratch branch off HEAD and never pushed,
  the same invocation prints `the remote default branch does not reach` and `marker` followed by
  that sha, and the record stays at `LANDING`; after `git push -q -f origin tscratch:main` the same
  marker reads `phase LANDED`; against the driver at `12513c25` the unpushed case prints `names a
  different commit`.
  Red when: an unpushed landing is accepted, which is a marker nothing observed; or the pushed
  control refuses, which is the containment read rejecting the ordering spec 16 §4 tolerates.
  fixture: the marker fixture plus one `fixture` commit on a scratch branch.
- **AC3** — When `python3 tools/memory-tree/check-arms.py --report` runs at the tip, its rows for
  `tools/unattended/unattended.sh` list every check-34 branch as armed, and
  `grep -c 'check 34' memory/project/unarmed-branches.txt` prints 0; at this unit's base the
  report lists the two branches of S1 and S2 as unarmed.
  Red when: a branch is unarmed, which the `harness arms (fail branches armed or pinned)` leg reds
  at the close; or a pin was written instead of an arm.
  figure: the branch count is DERIVED by the report at observation — seven after unit 16, by its
  rev-2 Inventory.
- **AC4** — When `grep -c 'carries no commit sha' tools/unattended/unattended.test.sh` and
  `grep -c 'default branch does not reach' tools/unattended/unattended.test.sh` run at the tip,
  each prints at least 1 and 0 at this unit's base.
  Red when: the arms exist under another text, which `check-arms.py` does not read as arming these
  branches.
  figure: both counts are DERIVED by the greps at observation over the tip and over the file at
  `830c46e8`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the driver invocations of
AC1 and AC2 over the fixture in a scratch clone, the report of AC3 and the greps of AC4. Under
`harness arms`, the two branches this unit arms are the count it moves.

New arm: `tools/unattended/unattended.test.sh` · the no-sha marker and the unpushed-commit marker with its pushed control, in the marker region; the break is the driver at `12513c25` beside the lib · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed count, region two

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 3 as the
  promotion of H2 (raw ids 5, 17, 27): the counts and the third read's grep are spec 16's rev-2
  fold, and the two arms are this unit.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "arm a refusal branch of a landing check against a
marker fixture"` ranked the `check` seam across nine kit self-tests and `armed` in
`tools/memory-tree/corpus_ids.py`, neither a shell arm, and reported `unscanned layers: .sh`; no
Python seam fits. The seam, read at source, is the marker region of the driver suite itself:
`tools/unattended/unattended.test.sh:4514` to `:4556`, whose `fixture`, `git push -q -f origin
HEAD:main` and `printf` into `$GCD/tmarker` are the three moves every arm here makes, and whose
all-zero arm at `:4541` is the shape the two new arms copy; `check-arms.py`'s `discover()` at
`:125`, which is why the arms carry the branch's own text; and the lib-beside-the-copy idiom at
`:2092`. The recall probe returned `TOOL-aFoldedQuarry-7` (every `fail` branch armed or pinned,
keyed on the call site), this build's round-3 audit at the H2 paragraph, and
`TOOL-aDeferredBar-13` (pins are keyed by ordinal, which is why this unit pins nothing); no prior
record arms these two branches, because the sentences do not exist before unit 16.

Recall terms used: `check-arms fail branch armed pinned unarmed-branches marker fixture landed check 34 harness arms positive assertion sibling test`
