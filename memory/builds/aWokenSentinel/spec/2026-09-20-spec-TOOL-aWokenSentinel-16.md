# TOOL-aWokenSentinel-16 — `--landed`'s check 34 accepts the `--no-ff` landing the charter mandates: the marker's commit contains the witness and sits on the remote default branch

**Status:** SPECCED · rev-2 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-prompt-TOOL-aWokenSentinel-16-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-16-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H1 (round 2, raw id 48): `TOOL-aWokenSentinel-8`'s loop closes only if the
re-run `--landed` reaches `LANDED`, and on the `--no-ff` landing charter §3 mandates it never does.
`tools/push-main.sh:127` writes the lander marker with the MERGE commit; the run worktree's HEAD is
that merge's second parent; check 34 at `tools/unattended/unattended.sh:2499` takes the remote arm
whenever HEAD is an ancestor of the advertised tip, sets the witness to HEAD, and refuses unless the
marker names it by string equality. That is OPEN `TOOL-dUnstalledConvoy-38`, worked around by
fast-forwarding the run branch onto the merge and re-running in the same worktree. Under unit 8's
row every such refusal ends a turn and spends one of the shared `STOP_GUARD_BLOCKS`; after the
budget the record sits at `LANDING` with its work on `main`, the pre-build wedge by a longer route.
This unit builds the predicate -38 asks for: the marker's commit must CONTAIN the witness and must be
reachable from the remote default branch the anchor observed. A fast-forward landing satisfies it
exactly as before, a `--no-ff` landing satisfies it from the run worktree, and a marker naming an
earlier landing — the pass-by-finding-anything shape the equality was written against — still
refuses, because an earlier commit does not contain a later witness.

## 2. Scope (IN)

- **S1** — In `verb_landed`'s remote arm, the string compare at `unattended.sh:2499` is replaced
  by three reads over the marker's first 40-hex token `msha`: it must resolve to a commit in this
  object store, `GIT merge-base --is-ancestor "$wit" "$msha"` must hold, and
  `GIT merge-base --is-ancestor "$msha" "$ASHA"` must hold, where `ASHA` is the tip
  `observe_anchor` read from the remote's own advertisement. Observed by AC1, AC2 and AC3.
- **S2** — Each failing read is its own `fail 34` sentence naming what it read: a marker line with
  no sha, a sha this clone does not hold, a commit that does not contain the witness (the earlier
  landing), and a commit the advertised default branch does not reach — four new sentences
  replacing the one at `:2500`, beside the three check-34 sentences that stay (`:1242`, `:2481`,
  `:2493`), seven branches of one check for `check-arms.py` to key. S3 arms the second and the
  third; `TOOL-aWokenSentinel-22` arms the first and the fourth, and the `harness arms` leg runs
  once at the close after both. The witness written to the record stays HEAD, exactly as the
  remote arm has it; the marker's commit is evidence, never the witness. Observed by AC2 and AC3.
- **S3** — The suite's marker arms move with the predicate: the all-zero marker arm at
  `unattended.test.sh:4541` reads the "does not hold" refusal, a new arm writes a marker naming the
  fixture's parent commit and reads the "does not contain the witness" refusal, and a new arm builds
  the `--no-ff` shape — `main` merged `--no-ff` from the run branch, pushed, the marker holding the
  merge, `--landed` run from the run branch — and reads `phase LANDED` with the witness equal to the
  run branch's HEAD; that last arm is observed RED first against the driver at this unit's base,
  where it refuses naming a different commit. Observed by AC1, AC2 and AC3.
- **S4** — The verb's comment above the check states the predicate, cites -38, and states what the
  predicate does NOT prove, in a sentence carrying the phrase `does not prove`: that the lander
  which wrote the marker is the one this project declares, and the concurrent-landing overwrite
  `TOOL-aUnblockedFleet-7` records, cited by id, which this predicate tolerates only when the later
  landing contains this one. Observed by AC4, which pins the two ids and the phrase.

## 3. Non-goals (OUT)

- **No change to the local arm.** It compares the run's own branch tip against the local default
  branch and never reads the marker; -38 is a remote-arm defect.
- **No change to the lander.** `push-main.sh` writes the pushed commit, which under `--no-ff` is
  the merge; that is the right thing to write, and the reader was wrong.
- **No per-run marker.** -7's candidate fix keys the marker per branch or per run; it stays OPEN
  and this unit's §4 says which ordering the new predicate tolerates and which it does not.
- **No change to unit 7's refusals.** Unit 7 reads the stop listing BEFORE `observe_anchor`; this
  check sits after the anchor and after the arms, where it always was.
- **No change to `--liveness`.** `FINISHED-UNSTAMPED` keeps unit 2's definition; this unit is why a
  session at that verdict can now stamp the record from where it stands.

### Edges

- **consumes-from** external — check 34 as it stands at `tools/unattended/unattended.sh:2476` to
  `:2503`, the `observe_anchor` read that supplies `ASHA` and `AREF`, `tools/push-main.sh:127`'s
  marker line, the suite's marker arms at `tools/unattended/unattended.test.sh:4514` to `:4556`
  and its local-arm `--no-ff` fixture at `:2576`, whose shape the new arm copies with the merge
  pushed.
- **hands-off** `TOOL-aWokenSentinel-8` — step 3 of the loop trace reaching `LANDED` on the
  mandated landing shape from the run worktree, so the row spends no block on a refusal the
  lander cannot cure; spec 8 cites this unit and both backlog rows.
- **hands-off** `TOOL-aWokenSentinel-22` — the arms for the two sentences S3 does not read: the
  marker with no 40-hex token and the marker naming a commit that contains the witness but was
  never pushed, each observed RED first against the driver at this unit's base.
- **hands-off** external — the per-run marker of `TOOL-aUnblockedFleet-7`, a backlog row that
  stays OPEN with the tolerated ordering recorded against it at the close.

## 4. Design

### The predicate, in place of the equality

```
_lm_line=$(tr -d '\r' < "$_lm_path" | head -1)
msha=$(printf '%s\n' "$_lm_line" | grep -oE '[0-9a-f]{40}' | head -1)
[ -n "$msha" ] || { fail 34 "the lander marker carries no commit sha, so it is a touched file and not evidence; fix what the lander writes. marker holds: $_lm_line"; return 1; }
GIT cat-file -e "$msha^{commit}" 2>/dev/null \
  || { fail 34 "the lander marker names a commit this clone does not hold, so nothing here can say whether it contains this landing; fetch the remote or re-run the lander. marker: $msha"; return 1; }
GIT merge-base --is-ancestor "$wit" "$msha" 2>/dev/null \
  || { fail 34 "the lander marker names a commit that does not contain the witness, so it is evidence of an EARLIER landing standing in for this one; re-run the lander or fix what it writes. wanted $wit reachable from the marker's $msha"; return 1; }
GIT merge-base --is-ancestor "$msha" "$ASHA" 2>/dev/null \
  || { fail 34 "the lander marker names a commit the remote default branch does not reach, so the landing it records is not the one $AREF advertises; re-run the lander. marker $msha against $AREF at $ASHA"; return 1; }
```

`is-ancestor` is reflexive, so the fast-forward landing — marker equal to HEAD — passes both reads,
which is the existing accepting arm at `unattended.test.sh:4551` unchanged. Under `--no-ff` the
marker is the merge `M`, HEAD is its second parent `T`, `T` is an ancestor of `M` and `M` is the
advertised tip, so both reads pass and the witness written is `T`, the commit the remote arm
validated. The all-zero marker of the existing refusal arm is not a commit anywhere, so it refuses
at the second read; a marker naming the fixture's parent commit is on the remote but does not
contain `T`, so it refuses at the third read — the pass-by-finding-anything class the equality was
written against, still refused.

### What the predicate tolerates, and what it does not, against -7

Two runs land close together and the clone-shared marker is overwritten. Run A pushes `M_A`, run B
merges `main` (which now holds `M_A`) and pushes `M_B`, the marker holds `M_B`: A's witness is an
ancestor of `M_B`, so A's `--landed` is accepted, correctly, because A's work is on the default
branch and a lander observed a push that carried it. The other ordering — B's marker written before
A's push, A then pushes and B overwrites nothing — cannot arise, since the marker is written only
inside the lander's push-succeeded branch. What stays open is a lander that pushed and then failed
to write, which is -7's own concern and not this unit's.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `msha` | a local in `verb_landed` | no cell; not a function |

No function, key, verb or file is minted. The `fail 34` number is reused: the four new sentences
are four refusals of one check, beside the three that stay at `:1242`, `:2481` and `:2493` — seven
branches, each armed by S3 or by unit 22, and none pinned.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.sh` | the predicate and its four sentences in `verb_landed`; the comment above the check |
| `tools/unattended/unattended.test.sh` | the all-zero arm's expected text; the parent-commit arm; the `--no-ff` remote arm |

### Alternatives rejected

- **Keep the equality and have unit 8's reason text name the fast-forward workaround.** The audit's
  own fix. It sends every session to run a git command the record then has to explain, keeps -38
  OPEN with a documented workaround as its remedy, and leaves the landing shape the charter mandates
  unreachable from the worktree the run lives in.
- **Compare the marker against `ASHA` only.** Any landing by anybody satisfies it; the witness
  containment is what makes the marker evidence about THIS run.
- **Have the lander write the second parent as well as the merge.** A second field in a file two
  scripts parse, to avoid a `merge-base` call the verb already spends elsewhere in the same arm.

## 5. Production-readiness checklist

- security — the check is an integrity read and stays one: a marker must still name a commit that
  contains the witness and that the remote's own advertisement reaches. No write moves.
- perf / scale — two `merge-base` calls and one `cat-file` per `--landed`, milliseconds.
- error / empty / loading states — an empty marker, a marker with no sha, an unknown sha, an earlier
  commit and an unadvertised commit each refuse with their own sentence; a missing marker keeps the
  existing refusal above.
- observability — every refusal prints the marker's sha and the witness, so "stale marker" and "HEAD
  moved since the push" are told apart, as the existing arm's comment asks.
- risks — a marker from a later landing that contains this one is accepted; §4 argues that is
  correct and names the ordering -7 keeps. A shallow clone that lacks the merge refuses at the
  `cat-file` read and says so.
- testing — §6; three arms over the suite's marker fixture, each in seconds.
- migration — N/A; the marker's bytes are unchanged and an old marker naming HEAD still passes.
- user docs — none; the verb's comment, and -38's row closes at the close with this unit cited.

## 6. Acceptance criteria

The fixture is the suite's marker fixture at `tools/unattended/unattended.test.sh:4514`: a scratch
clone with a fixture `origin`, `LANDER_MARKER="tmarker"` in the conf, the record at `LANDING`, and
the marker written by `printf` under the git common dir. The staged break for AC1 is the driver at
this unit's base.

- **AC1** — When `main` is checked out at the fixture's base, merged `--no-ff` from the run branch,
  pushed to the fixture `origin`, the marker written as `landed main at <merge sha> by push-main`,
  and the run branch checked out again, `bash tools/unattended/unattended.sh --landed tRun` prints
  `phase LANDED` and the record's `witness:` equals `git rev-parse HEAD` on the run branch; against
  the driver at this unit's base the same run prints `names a different commit`.
  Red when: the run worktree cannot stamp a `--no-ff` landing, which is -38 and the wedge H1 names;
  or the witness recorded is the merge, which is a commit this arm never validated.
  fixture: the suite's marker fixture plus the local-arm `--no-ff` shape at `:2576`, with the merge
  pushed rather than left local.
- **AC2** — When the marker names the run branch's parent commit, which the fixture `origin`
  advertises as reachable, the same invocation prints `does not contain the witness` and `wanted`
  followed by HEAD's sha; when it names forty zeros it prints `a commit this clone does not hold`.
  Red when: an earlier landing's marker is accepted, which is the pass-by-finding-anything class the
  equality was written against; or the two refusals share one sentence, which sends the reader at
  the wrong half.
- **AC3** — When the marker names HEAD itself, the existing accepting arm still prints `phase
  LANDED` with no `names a` refusal, and `grep -c 'phase: LANDED'` over the fixture record's
  `RUN.md` prints 1.
  Red when: the fast-forward landing regressed, which is every landing on a node whose lander
  fast-forwards.
- **AC4** — When `grep -c 'dUnstalledConvoy-38' tools/unattended/unattended.sh` and
  `grep -c 'aUnblockedFleet-7' tools/unattended/unattended.sh` run at the tip each prints at least
  1 and 0 at this unit's base; `grep -c 'does not prove' tools/unattended/unattended.sh` prints at
  least 1 at the tip; and `grep -c 'is-ancestor "\$wit"' tools/unattended/unattended.sh` and
  `grep -c 'is-ancestor "\$msha"' tools/unattended/unattended.sh` each print 1.
  Red when: the comment does not cite the row the predicate closes or the row whose ordering it
  tolerates, or states the predicate without its limit; or the containment read is absent and only
  the remote read remains, which accepts any landing by anybody; or the remote read is absent and
  only containment remains, which accepts a marker for a merge that was never pushed.
  figure: every count is DERIVED by the greps at observation, over the tip and over the file at
  `12513c25`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates`

These run once at `--close`. The pass runs none of them: it verifies with the driver invocations of
AC1 to AC3 over the fixture in a scratch clone and the greps of AC4. Under `harness arms`, four new
`fail 34` sentences replace one, and every one is a branch the suite's arms must read: S3 reads
the "does not hold" and "does not contain the witness" sentences, and unit 22 reads the other two
before the leg runs.

New arm: `tools/unattended/unattended.test.sh` · the `--no-ff` remote-arm fixture with the merge pushed and the marker holding it, the parent-commit marker, and the all-zero marker's moved text; the break is the driver at this unit's base; the no-sha and unpushed-commit arms are unit 22's · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the arms' executed count, region two

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · S2 · S4 · §3 · §4 · AC4 · §7 · §10 · folded spec-audit round 3: sibling
  agreement for the promoted `TOOL-aWokenSentinel-22` (H2, raw 5, 17, 27) — four new `fail 34`
  sentences beside three existing, seven branches, two armed here and two by unit 22, which §7
  and the Inventory now count rather than "the two new" and "the two existing"; the third read,
  `is-ancestor "$msha"`, is pinned by AC4 so a predicate that drops the remote read cannot pass
  AC1 to AC4; M4 (raw 6) — AC4 pins the `-7` citation and the `does not prove` phrase S4
  requires.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of H1 (raw id 48); takes the predicate `TOOL-dUnstalledConvoy-38` records rather than
  the audit's reason-text fix, per BUILD-METHOD M3's feature-rich rule.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "accept a lander marker whose commit contains the witness
on the remote default branch"` ranked `outcome_accepted` in `tools/govkit/govkit.py` and the
`.unattended.conf` affordance seam (`branch, land, mark, wit`), and reported `unscanned layers: .sh`;
no Python seam fits a shell verb. The seam, read at source, is check 34 itself at
`tools/unattended/unattended.sh:2476` to `:2503` — the marker path resolution against the git common
dir, the three check-34 sentences that stay (`:1242`, `:2481`, `:2493`), the one at `:2500` the
predicate replaces, and the `wit` the arm validated — and the `merge-base
--is-ancestor` the same verb already runs at `:2434` for the remote arm, which the new reads copy. The
recall probe's top hit is `TOOL-dUnstalledConvoy-38` itself, whose row states the predicate this unit
builds; its second is `TOOL-dScaffoldedMirror-22`, CLOSED, the write-before-check sibling found in
the same invocation, whose ordering fix `dSealedTally` built and this unit relies on: a refusal here
leaves the record untouched.

Recall terms used: `lander marker check 34 witness HEAD no-ff merge second parent remote default branch ancestor landed refuse`
