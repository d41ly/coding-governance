# TOOL-aWokenSentinel-22 — check 34's two refusal branches unit 16 leaves unarmed get their arms: the marker with no sha and the marker the remote default branch does not reach, each read RED first

**Status:** CLOSED · rev-3 · 2026-09-21 · node a · Tier-2 · base 830c46e8 · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-22-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-22-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-22-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-22-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-21-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 |

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
  this unit's base), entered with the record at a COMMITTED `LANDING`, the tree clean and HEAD
  pushed to the fixture's `origin main`, which is the state the region's own setup leaves: the
  marker written as `landed main at nothing by push-main`, which carries no 40-hex token, makes
  `--landed tRun` print the branch's whole signature, `the lander marker carries no commit sha, so
  it is a touched file and not evidence; fix what the lander writes. marker holds`, followed by
  that line, and the record's `phase:` stays `LANDING`. Observed by AC1.
- **S2** — A second arm in the same region: one commit made on a scratch branch off the run
  branch's HEAD over a tracked write and never pushed, the marker naming it, makes `--landed tRun`
  print the branch's whole signature, `the lander marker names a commit the remote default branch
  does not reach, so the landing it records is not the one`, with `marker <sha> against
  refs/heads/main`, and the record stays at `LANDING`; the same marker after `git push origin
  <scratch>:main` reads `phase LANDED`, because a later landing that contains this one is the
  run-B-overwrites-run-A ordering `TOOL-aUnblockedFleet-7` records and spec 16 §4 tolerates. The
  control then RESTORES the state it consumed — the record back to `LANDING`, committed, and HEAD
  re-pushed to `origin main` — so the accepting arm below it enters the state it needs. Observed by
  AC2.
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
- **hands-off** `TOOL-aWokenSentinel-26` — the accepting arm's own entry-state guard: this unit
  restores what its control consumed, and that unit makes the accepting arm assert it, so the next
  insertion above it reds there rather than passing on an inherited record.
- **hands-off** external — nothing.

## 4. Design

### The two arms, beside the accepting one

```
# the marker carries NO sha — a touched file, not evidence
printf 'landed main at nothing by push-main\n' > "$GCD/tmarker"
out=$(run --landed tRun)
hit "$out" "the lander marker carries no commit sha, so it is a touched file and not evidence; fix what the lander writes. marker holds"
hit "$out" "marker holds: landed main at nothing by push-main"
same "no-sha marker leaves the record at LANDING" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"

# the marker names a commit that CONTAINS the witness but was never pushed. The scratch commit is
# made over a TRACKED write: fixture() is `git add -A && git commit`, and on a clean tree it commits
# nothing, exits 1 under set -u without set -e, and leaves HEAD where origin main already is.
git branch -f tscratch HEAD; git checkout -q tscratch; printf 'scratch\n' > tscratch.txt; fixture; _unpushed=$(git rev-parse HEAD); git checkout -q -
same "the scratch commit is not the run branch HEAD" "$([ "$_unpushed" != "$(git rev-parse HEAD)" ] && echo distinct)" "distinct"
printf 'landed main at %s by push-main\n' "$_unpushed" > "$GCD/tmarker"
out=$(run --landed tRun)
hit "$out" "the lander marker names a commit the remote default branch does not reach, so the landing it records is not the one"
hit "$out" "marker $_unpushed against refs/heads/main"
same "unpushed marker leaves the record at LANDING" "$(grep -c '^phase: LANDING' memory/builds/tRun/RUN.md)" "1"
# ...and pushed, the same marker is a LATER landing that contains this one — accepted: the
# run-B-overwrites-run-A ordering TOOL-aUnblockedFleet-7 records, which spec 16 §4 tolerates.
git push -q -f origin tscratch:main 2>/dev/null
out=$(run --landed tRun)
miss "$out" "does not reach"
same "a later landing containing this one is accepted" "$(grep -c '^phase: LANDED' memory/builds/tRun/RUN.md)" "1"
# THE CONTROL CONSUMED THE STATE: the record is LANDED and origin main is the scratch commit. The
# accepting arm below establishes nothing of its own (TOOL-aWokenSentinel-26 makes it assert this),
# so restore what the region's setup left — a committed LANDING, a clean tree, HEAD advertised.
sed -i 's/^phase: .*/phase: LANDING/' memory/builds/tRun/RUN.md; fixture; git push -q -f origin HEAD:main 2>/dev/null
```

`fixture` is the suite's own commit-making helper, `git add -A >/dev/null && git commit -q -m
fixture --no-verify` at `unattended.test.sh:363`, and every one of its call sites writes a tracked
file first because a clean tree makes it a no-op that changes no sha; the `tscratch.txt` write is
that file here, and the `same` that follows names a no-op commit as such rather than letting it
reach the marker as the run branch's own HEAD, which `origin main` holds and the driver accepts.
The first `hit` of each pair quotes the branch's WHOLE signature as `check-arms.py`'s
`signature()` derives it — the longest literal run before the first interpolation, which runs past
the sentence to `marker holds` and to `is not the one`, 123 and 115 characters — because
`classify()` arms a branch only when a test line contains that entire run, and a readable prefix
reads as UNARMED (`memory/gotchas/arm-literal-strands-on-message-edit.md`). The two literals were
computed by running `signature()` over spec 16 rev-2's sentences at the disposal; at this unit's
order `--report` still prints its rows truncated at 72 characters, so the row is not the thing to
copy until `TOOL-aWokenSentinel-25` lands, and the pass copies from here. The second `hit` pins the
interpolated tail, so a sentence that names the wrong sha is red. The `same` on `phase: LANDING`
is the write-before-check property `TOOL-dScaffoldedMirror-22` fixed and spec 16 §10 relies on: a
refusal leaves the record untouched. The pushed half of the second pair is the positive control
that separates "not reachable" from "not containing": the same marker, one push later, is
accepted — and the three lines after it put the region back where the accepting arm expects it.

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
| `tools/unattended/unattended.test.sh` | the two arms, the pushed control and its three restoration lines in the marker region, after the parent-commit arm spec 16 adds and before the accepting arm |

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
- risks — the pushed control lands the record and leaves `origin main` at the scratch commit, and
  the accepting arm that follows in the region has NO setup of its own (the all-zero arm at `:4541`
  does not re-push either; only the MISSING-marker arm at `:4556` rebuilds its state), so without
  the three restoration lines it would run `--landed` on a LANDED record, pass its three `miss`
  lines on check 26's unrelated refusal and read the control's `phase: LANDED` as its own — green
  by absence. The restoration is this unit's; the assertion that it happened is unit 26's.
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
- **AC2** — When the marker names one commit made on a scratch branch off HEAD over the tracked
  write `tscratch.txt` and never pushed — a sha the arm asserts differs from the run branch's HEAD
  — the same invocation prints `the remote default branch does not reach` and `marker` followed by
  that sha, and the record stays at `LANDING`; after `git push -q -f origin tscratch:main` the same
  marker reads `phase LANDED`; after the control's three restoration lines,
  `grep -c '^phase: LANDING'` over the fixture's record prints 1, `git status --porcelain` prints
  nothing and `git rev-parse HEAD` equals the sha `git ls-remote -q origin refs/heads/main`
  advertises; against the driver at `12513c25` the unpushed case prints `names a different commit`.
  Red when: an unpushed landing is accepted, which is a marker nothing observed — or `_unpushed`
  equals the run branch's HEAD, which is `fixture` committing nothing on a clean tree and the
  driver accepting a sha `origin main` already holds; or the pushed control refuses, which is the
  containment read rejecting the ordering `TOOL-aUnblockedFleet-7` records; or the state after the
  control is not the state the accepting arm needs, which is that arm going green on this unit's
  write.
  fixture: the marker fixture plus one `fixture` commit over `tscratch.txt` on a scratch branch.
- **AC3** — When `python3 tools/memory-tree/check-arms.py --report` runs at the tip, its rows for
  `tools/unattended/unattended.sh` list every check-34 branch as armed, and
  `grep -c $'^tools/unattended/unattended.sh\t34\t' memory/project/unarmed-branches.txt`
  prints 0 while the same grep keyed `\t9\t` prints at least 1, because the file is tab-keyed by
  file, check and branch and never spells `check 34`, so a selector on those words matches nothing
  on every tree; at the tip of unit 16's pass
  — the commit whose subject carries `TOOL-aWokenSentinel-16`, not `830c46e8`, where the two
  sentences do not exist and the report keys only the four pre-predicate `fail 34` sites — the
  report lists the two branches of S1 and S2 as unarmed.
  Red when: a branch is unarmed, which the `harness arms (fail branches armed or pinned)` leg reds
  at the close; or a pin was written instead of an arm; or the RED-first reading is taken at a
  commit where the branches do not exist, which lists nothing and cannot red.
  figure: the branch count is DERIVED by the report at observation — seven after unit 16, by its
  rev-2 Inventory.
- **AC4** — When `grep -cF 'the lander marker carries no commit sha, so it is a touched file and not evidence; fix what the lander writes. marker holds' tools/unattended/unattended.test.sh`
  and `grep -cF 'the lander marker names a commit the remote default branch does not reach, so the landing it records is not the one' tools/unattended/unattended.test.sh`
  run at the tip, each prints at least 1 and 0 at this unit's base.
  Red when: the arms exist under a prefix or another text, which `check-arms.py` does not read as
  arming these branches — the fragment greps of rev-1 passed on exactly that prefix.
  figure: both counts are DERIVED by the greps at observation over the tip and over the file at
  `830c46e8`; the two literals are PINNED as `signature()` returned them on 2026-09-20 over spec
  16 rev-2's sentences, and a reworded sentence moves them.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)`

These run once at `--close`. The pass runs none of them: it verifies with the driver invocations of
AC1 and AC2 over the fixture in a scratch clone, the report of AC3 and the greps of AC4. Under
`harness arms`, the two branches this unit arms are the count it moves.

New arm: `tools/unattended/unattended.test.sh` · the no-sha marker and the unpushed-commit marker with its pushed control and restoration, in the marker region; the break is the driver at `12513c25` beside the lib · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed count, region two

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-09-21 · AC3 · folded at the pass from the bug-class checklist
  (`fixture-passes-by-finding-nothing`): `unarmed-branches.txt` is tab-keyed by file, check and
  branch and never spells `check 34`, so rev-2's `grep -c 'check 34'` printed 0 on every tree; the
  selector is keyed on the file's own columns and its liveness is the pinned check-9 row.
- rev-2 · 2026-09-20 · S1 · S2 · §3 · §4 · §5 · AC2 · AC3 · AC4 · §7 · folded spec-audit round 4:
  sibling agreement for the promoted `TOOL-aWokenSentinel-25` (H1, raw 12, 22, 33) — the first
  `hit` of each pair quotes the whole signature `signature()` derives, 123 and 115 characters,
  and AC4 greps those literals with `-F` so a prefix reds; sibling agreement for the promoted
  `TOOL-aWokenSentinel-26` (H2, raw 1, 23) — the pushed control restores a committed `LANDING`
  with HEAD re-pushed, S1 states the entry state, AC2 observes the after-state, §5 says which arm
  inherits it and why the rev-1 risk line was false; M1 (raw 4, 21) — the scratch commit is made
  over the tracked write `tscratch.txt` and the arm asserts `_unpushed` differs from HEAD; M2
  (raw 3, 13) — AC3's RED-first reading is at the tip of unit 16's pass, not `830c46e8`; L2 (raw
  34) — `TOOL-aUnblockedFleet-7` cited in S2, the comment and AC2 beside the spec 16 §4 pointer.
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
