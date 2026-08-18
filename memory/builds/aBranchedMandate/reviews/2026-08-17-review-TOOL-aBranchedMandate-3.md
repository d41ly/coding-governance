# Tier-2 review — the cumulative diff landing on main

**Serves:** diff-review TOOL-aBranchedMandate-3

**Reviewed range:** `eb09d6e7ee7ed6684d04ef80850f49446a0357dc...HEAD`

**Review shape:** raw 19 · confirmed 13 · refuted 6 · unverified 0 · precision 0.68

The 13 confirmed findings collapse to **7 distinct defects** — four of them were reported by more
than one reviewer (the check-9 fail-open three times, the remote-selection defect twice, the
`anchor-kind` drift twice, the dead `observe_branch` three times). Duplicates are merged below and
their originating ids listed, so nothing is lost and nothing is double-counted.

Counted as distinct defects: **1 blocker · 1 high · 4 medium · 1 low.**

Every defect in this report lives in the S6 unit — the rewrite that moved the BASE predicate off
local refs and onto the remote's own advertisement. That was the right direction; the landing of it
traded a check that always ran for one that runs only when the network answers, and picks its
endpoint with less discipline than the driver next door.

---

## BLOCKER

### D1 — check 9 fails OPEN when the remote advertises nothing

`tools/unattended/check-unattended.sh:338` (advertisement taken at `:213-220`; the comment it
contradicts at `:206-212`) — *ids 1, 10, 17*

The whole BASE body is wrapped in `if [ -n "$ADV_HEAD" ] || [ -n "$ADV_TIPS" ]; then`, and that `if`
has **no `else` and no `fail`**. When `git ls-remote` returns nothing — no remote configured, no
network, a proxy, or auth refused under the `GIT_TERMINAL_PROMPT=0` this leg itself exports — both
vars are empty and every BASE predicate silently vanishes:

- the not-a-commit refusal (`:347`)
- `is_published` (`:349`)
- ancestor-of-HEAD (`:351`)
- the phase-keyed `rb != HEAD` (`:365`)
- check 15's second half (`:383`)

Nothing else in the file re-asks any of them. The leg exits 0 with **no output at all** — the silent-skip
shape this file refuses by name elsewhere.

Reproduced twice independently. Clone the worktree, forge `memory/builds/aBranchedMandate/RUN.md`'s
`base:` to an orphan commit (`git commit-tree HEAD^{tree}`, published nowhere), commit: with origin
present the leg reds with *"a recorded BASE is not published on the remote"* and exits 1. After
`git remote remove origin` the identical tree exits 0, printing nothing.

The knock-on: check 13 (`:403`) is itself gated on `rb` resolving, so an unresolvable recorded base
skips the **mandate assertion** as well. A run-state file with `base: <garbage>` produces zero output
from the bar's only two authorization checks.

This is a regression in reach, not a pre-existing gap. `git show a2a6de4^` confirms the pre-S6 leg
read `refs/remotes/origin/$d`, which exists offline, and *did* fire on this same forgery. And the
block's own comment at `:206-212` states the opposite of what the code does — *"FAIL-CLOSED, decided
rather than left open… failing open would disarm the only BASE check on the bar"*. Two answers to one
question, and the code is the one that runs.

The leg deliberately does not carry the driver's check-22 environment guard (stated in its header at
`:25-30`), so the run's own process controls whether the advertisement succeeds — a bad
`GIT_SSH_COMMAND` or proxy var is a one-variable bypass of the authoritative `.githooks/pre-push`
run.

**Fix.** Make the empty advertisement a refusal, the way the driver's check 27 does. After the
advertisement block:

```sh
if [ "$POP" -gt 0 ] && [ -z "$ADV_HEAD" ] && [ -z "$ADV_TIPS" ]; then
  fail 9 "the remote did not answer, and check 9's predicate is an observation of it rather than of any local ref; a leg that cannot observe the remote cannot judge a recorded BASE at all: $adv_remote"
fi
```

then drop the `if [ -n "$ADV_HEAD" ] || [ -n "$ADV_TIPS" ]` wrapper at `:338` entirely, keeping the
separate `[ -n "$b" ]` guard at `:383` for the heads-but-no-HEAD-symref case.

**Left-shift gate.** Add an arm to `check-unattended.test.sh` that runs the leg with
`git remote set-url origin "$ORIGIN_DIR/nope.git"` over a *forged-base* fixture and asserts the
refusal, plus its restore-and-green control. The suite's comment at `test.sh:91-93` already
*acknowledges* the empty-`ADV_HEAD` disarm as a fixture requirement — that acknowledgement should
have been an arm. More generally: any `if` that guards a whole check body on an observation
succeeding wants a paired arm proving the observation's absence is loud.

---

## HIGH

### D2 — the leg picks its remote alphabetically, with none of the driver's endpoint discipline

`tools/unattended/check-unattended.sh:214` — *ids 2, 11*

```sh
adv_remote=$(GIT remote 2>/dev/null | head -1)
```

`git remote` sorts, so this takes the **alphabetically first** remote (verified empirically: with
remotes `aaa`/`origin`/`zzz`, `head -1` prints `aaa`). There is no count guard and no URL guard
anywhere in the file. The sibling driver refuses exactly these shapes — `unattended.sh` check 24
refuses `nrem != 1` (*"the anchor has to be the endpoint the landing push goes to, so the kit refuses
to pick one"*) and check 25 refuses fetch-URL ≠ push-URL. The project has already decided these
guards are necessary for the endpoint the anchor is observed from; the leg silently picks instead.

Both halves reproduced on a clone of this worktree with no other change:

- **False red.** Adding an unrelated non-empty bare repo as remote `aaa` makes the leg judge
  publication against it: 6 honest records red with *"a recorded BASE is not published on the
  remote"* (aBranchedMandate, aDeclaredCeiling, aSealedCaravan, aSiftedPlaybook, cBriefedPilot,
  dClosedLexicon) and the leg exits 1. It rides `.githooks/pre-push`, so that blocks **every** push.
  Any adopter clone with a second remote sorting before `origin` — `backup`, `fork`, `gh`, `mirror` —
  is in this state.
- **False green.** With `aaa` pointing at an *empty* bare repo the advertisement is blank and the
  whole check silently vanishes (D1's fail-open, exit 0).

And the forgery direction: `git remote add aaa /tmp/fake.git` against a local bare repo the run
authored, plus a push, makes `ADV_HEAD`/`ADV_TIPS` come from an endpoint the run controls —
`is_published` then blesses any commit, and check 9 is satisfiable entirely offline in two commands,
at the authoritative pre-push run, in the run's own clone.

The comment at `:326-328` claims the rewrite removed *"the last place this leg read … a `refs/remotes/*`
ref"* — i.e. run-writable state. That is overstated: remote names and URLs live in `.git/config` and
are equally run-writable. The rewrite moved which run-writable value is trusted; it did not remove
one.

**Fix.** Port the driver's two guards in before the advertisement:

```sh
nrem=$(GIT remote 2>/dev/null | grep -c . || true)
[ "$nrem" = 1 ] || fail 9 "this clone declares $nrem remotes, and the BASE predicate is an observation of ONE endpoint, so the leg would be choosing which one to believe"
[ "$(GIT ls-remote --get-url "$adv_remote")" = "$(GIT remote get-url --push "$adv_remote")" ] \
  || fail 9 "this remote fetches from one endpoint and pushes to another, so what it advertises is not what a landing would reach: $adv_remote"
```

One guard closes both this and part of D1. If multi-remote clones must be supported instead, union
the advertisements across all remotes and derive `b` from the remote whose HEAD symref resolves.

**Left-shift gate.** Two arms: a second remote sorting before `origin` (assert green, or assert the
new refusal), and a fetch/push URL split. Beyond that, the durable gate is **kit-internal parity**:
the driver and the leg both observe the same remote for the same reason, and the two lists of
endpoint refusals have now diverged. A small parity check — every `nrem`/URL refusal the driver
raises has a counterpart in the leg — would have caught this at write time, and belongs beside the
existing `check-protocol-parity.test.sh`.

---

## MEDIUM

### D3 — check 15 compares against an object this clone may not have, reding an honest LANDED record

`tools/unattended/check-unattended.sh:383` (advertisement `:213-220`) — *id 6*

`b="$ADV_HEAD"` is now the tip the remote advertises *right now*, not the last-fetched
`refs/remotes/origin/<d>` it replaced. There is **no test that this clone has that object**. If
origin's default branch moved since the last fetch — routine on a 4-node fleet — `$b` names a commit
that is not present locally, `git merge-base --is-ancestor "$w" "$b"` exits 128 (measured: *fatal:
Not a valid commit name*), the negation is true, and the leg reds with *"the work it says reached the
remote is not on the branch the remote calls its default"* on a witness that genuinely landed.

The `[ -n "$b" ]` guard added in this diff covers the empty case but not the absent-object case. The
witness gets a `rev-parse --verify` guard; `$b` gets only the emptiness test. The old `$b` was a
local `refs/remotes/*` ref, present by construction — the disposal comment at `:326-337` even calls
the advertised tip *"the same commit the old `$b` resolved to on an honest tree"*, which is exactly
the assumption that fails here. Three tracked LANDED records (aDeclaredCeiling, aSealedCaravan,
aSiftedPlaybook) would each red with a message blaming the run.

`is_published` (`:228-235`) has the same blind spot, softened by the `ADV_TIPS` fallback; it reds
identically once every advertised tip is unfetched (e.g. a landed run whose branch was deleted on the
remote). Check 15 consults `ADV_HEAD` only, so nothing softens it. The driver distinguishes exactly
this state — refusal 30, *"fetch and re-run"*. The leg blames the run instead.

**Fix.** Filter the advertisement down to objects this clone actually has when building
`ADV_HEAD`/`ADV_TIPS` (keep only shas passing `GIT rev-parse --verify --quiet "$sha^{commit}"`), and
when a tip is advertised but absent, refuse with the driver's own wording rather than letting
`--is-ancestor` misreport it as a failed ancestry.

**Left-shift gate.** A fixture that advances origin's default branch *without* fetching, then runs
the leg over a LANDED record and asserts green. This class — *comparing against a sha you did not
verify is present* — is worth a grep-shaped gate too: every `merge-base --is-ancestor` in the kit
whose right-hand operand comes from `ls-remote` output must be preceded by a presence check on that
operand.

### D4 — `anchor-kind` / `branch-ref` / `branch-sha` drift off the value they are evidence for

`tools/unattended/unattended.sh:1289` (and `:1291-1292`) — *ids 5, 13*

`base`, `anchor-ref`, `anchor-sha` and `anchor-url` are each pinned once (`[ -n "$(fact …)" ] ||`),
but `set_fact "$rel" anchor-kind` three lines later is **unconditional**, and `branch-ref`/`branch-sha`
are rewritten whenever `BREF` is non-empty and never cleared when it is empty.

`--preflight` is the documented resume verb after a compaction; `verb_preflight` only calls
`refuse_if_terminal` (`:1187`), so re-running it on a live record is expected, and the pin-once idiom
next door exists precisely because of it. Two reachable drifts:

- **Branch tip advances.** Under the second anchor `resolve_base` sets `RB_BASE="$BSHA"` (`:386`), so
  `base` and `branch-sha` are the same commit at pin time. A re-preflight after the tip moves rewrites
  `branch-sha` to the new tip while `base` stays pinned — the record's evidence no longer reproduces
  the pin.
- **The S12 scenario the code's own comment describes.** Once another node lands the build folder on
  the default branch mid-run, the first anchor fires, `ANCHOR_KIND` flips to `default-branch` with
  `BREF` empty, so `:1291-1292` never run and the stale pair survives. `trusted_base` still passes via
  the monotone `is-ancestor` clause. The record then simultaneously claims a default-branch anchor,
  carries second-anchor evidence, and pins a `base` that is not the merge-base.

`memory/guides/UNATTENDED-PROTOCOL.md` §2 states facts 10-11 are *"present only when the second anchor
fired"* and *"ABSENT on a default-branch run"*, and spec S12 opens with *"the anchor KIND is pinned at
preflight and does not change for the life of the run"*. This is precisely the class the adjacent
comment at `:1270-1274` says was just closed for the anchor triple: *"evidence for a pinned value that
moves is evidence for nothing."*

Nothing catches it: AC8 forbids `check-unattended.sh` from reading `anchor-kind` (grep confirms zero
hits), and the wrap-up **surfaces `anchor-kind` to the owner** — so the flip silently reports the
stronger anchor for a run the weaker one authorized.

**Fix.** Pin all three the way the triple is pinned:

```sh
[ -n "$(fact "$rel" anchor-kind)" ] || set_fact "$rel" anchor-kind "${ANCHOR_KIND:-default-branch}" || return 1
```

and the same guard on `branch-ref`/`branch-sha` inside the `[ -n "$BREF" ]` block.

**Left-shift gate.** An arm that runs `--preflight` twice with the branch tip advanced in between and
asserts every evidence fact is byte-identical across the two runs. That single arm covers the whole
pin-once family rather than one key, and it is the arm the anchor triple should have had when *it*
was fixed — the fix landed without one, which is why the sibling keys were missed.

### D5 — the LIFECYCLE green control no longer reproduces the state it was written to hold

`tools/unattended/check-unattended.test.sh:554` — *id 18*

```sh
git update-ref refs/remotes/origin/main "$(git rev-parse main)"
```

S6 removed `refs/remotes/*` from the leg's reads, so moving the tracking ref is now a no-op from the
leg's point of view: origin still advertises `ANCHOR0`, the recorded base equals it, and the arm no
longer reproduces *"the anchor advanced past the pinned base"* — the exact scenario it exists for.

Proven by mutation. Patching `is_published` to string equality instead of ancestry reds this arm
loudly on the pre-change suite (*"a LANDED run-state record leaves the bar green: expected [], got
[check 9 FAILED…]"*) and leaves it **silently green** on the post-change suite. A full run of the
suite against the mutated leg fails only on an unrelated arm (*"a tree whose waiver was taken at
preflight exits 0"*), so the one arm written to stop equality being reintroduced can no longer see
it. The ancestry-vs-equality decision is now held only incidentally.

Two sibling fixtures in the same file were converted from `update-ref` to `git push` **in this very
diff** (`test.sh:538-542`) with a comment giving precisely this reason. This third one, eight lines
later, was missed.

**Fix.** Publish the merge instead of moving the tracking ref: replace `:554` with
`git push -q -f origin main`, and restore `origin/main` to `$ANCHOR0` after the arm (`reset_tree`
only resets local refs). Re-run the equality mutation to confirm the arm reds again.

**Left-shift gate.** Two things. (a) When a unit removes a source of truth from an engine's reads,
grep the sibling test file for fixtures that *set* that source — a mechanical sweep that would have
caught this in the same commit that converted the other two. (b) The durable version: a
`grep -n 'update-ref refs/remotes' tools/unattended/*.test.sh` assertion on the bar, since the leg
provably reads no remote-tracking ref any more, so a fixture that writes one is by construction
setting up state the subject cannot see.

### D6 — `observe_branch` is dead code, and the arms floor now pins it in place

`tools/unattended/unattended.sh:326-339` (floor at `.memory-tree.conf:87`) — *ids 7, 12, 19*

`observe_branch` has **no caller anywhere in the repo** — grep over the whole tree excluding `.git`
returns only the definition at `:326` and a prose mention in the comment at `:289`. `resolve_base`
sets `BREF`/`BSHA` itself via `branch_tip_quiet` (`:377-379`), and `trusted_base` (`:416`) calls
`emit_branch_fail`. `git log -S` shows it was added by this branch's commit `a2a6de4`.

Its four `fail 31/32/30/33` sentences (`:333-336`) are **byte-identical** to `emit_branch_fail`'s live
copies (`:318-321`). `check-arms.py` marks a branch armed when its message signature appears in the
sibling test file (`check-arms.py:226`: `b['armed'] = any(b['sig'] in l for l in lines)`) — there is
no reachability notion at all — so the arms written for `emit_branch_fail`
(`unattended.test.sh:1503/1515/1523`) arm both sets. `check-arms.py --report` duly prints all four
dead branches as ARMED.

`ARMS_FLOORS` was bumped `tools/unattended/unattended.sh:71:70` → `83:80` in this diff, on a count
that includes them. The floors are shrink-only, so **deleting the dead function now reds the
meta-gate** unless `.memory-tree.conf` is edited in the same commit: the ratchet has pinned dead code
in place. And a future reword of one message in `emit_branch_fail` leaves a divergent twin that
nothing detects — a second, silently drifting refusal catalogue that still scores as armed.

*(One sub-claim from the raw findings overreaches and is dropped: deleting `emit_branch_fail`'s live
branches would drop the count to 79 and red the floor, so the meta-gate would not stay green in that
direction.)*

**Fix.** Delete `observe_branch` (`:326-339`), drop the stale reference in the comment at `:289`, and
lower `ARMS_FLOORS` for `tools/unattended/unattended.sh` to the re-measured `79:76`.

**Left-shift gate.** The real gap is that `check-arms.py` scores arming by message text with no
reachability notion, so duplicated refusal text inflates both counts silently. The cheap durable
gate is a **dead-function check** over the kit's shell sources — every `name() {` defined in
`tools/unattended/*.sh` is either called somewhere git can see or waived with a reason — which is a
smaller predicate than teaching `check-arms.py` reachability and catches the class that actually bit
here. Second-cheapest: refuse two `fail` call sites in the same file carrying identical message text,
since that is what defeats the arming heuristic.

---

## LOW

### D7 — two unconditional `ls-remote` round-trips in repos with no runs to check

`tools/unattended/check-unattended.sh:213-220` — *id 8*

`POP` is computed at `:147` and check 14 is already wrapped in `if [ "$POP" -gt 0 ]` at `:188`, but
the advertisement block sits outside any guard and there is no earlier exit for the zero-run case.
Every consumer of `ADV_HEAD`/`ADV_TIPS` is inside the per-record loop (`is_published` at `:228-233`,
the check 9/15 block at `:338-349`), so with `POP=0` both calls are pure waste.

Every adopter that installed the kit and has never started an unattended run now pays two network
round-trips on **every gate run**. `GIT_TERMINAL_PROMPT=0` prevents a credential hang but not a
transport timeout, so on an unreachable or slow endpoint each call blocks for the full TCP/SSH
timeout before returning empty — turning a leg whose own comment advertises *"ZERO network calls
before this unit"* into the slowest thing on the bar for repos that get nothing from it.

**Fix.** Wrap `:213-220` in `if [ "$POP" -gt 0 ]; then … fi`, matching the guard already used at
`:188`. Costs nothing and preserves the stated one-advertisement-per-run and fail-closed design.
(Note the interaction with D1: the refusal proposed there is already `POP`-guarded, so the two fixes
compose.)

**Left-shift gate.** A timing-shaped arm is overkill. The proportionate one is a leg-cost note in the
kit's own header contract plus an arm asserting that a tree with zero run-state files makes zero
network calls — cheaply observed by pointing `origin` at a path that does not exist and asserting the
leg still exits 0 promptly. That arm doubles as a regression test for D1's refusal being correctly
`POP`-guarded.

---

## Fix order

1. **D1** and **D2** together — they are one edit region (`:213-220` plus the `:338` wrapper), and
   D2's one-remote guard is part of what makes D1's refusal well-defined.
2. **D3**, same file, same block: filter the advertisement to present objects.
3. **D5** — the fixture fix, so the mutation test that holds the ancestry decision works again before
   anything else in this file moves.
4. **D4** in the driver.
5. **D6** and **D7** — cleanup; D6 needs the `.memory-tree.conf` floor edit in the same commit.

## The pattern under these

Five of the seven are the same shape: **an observation replaced a construction, and the code kept
treating it as one.** A local ref is present, resolvable, and always readable; a remote advertisement
is none of those. D1 (may be absent), D2 (may name the wrong endpoint), D3 (may name an object you do
not have), D5 (the fixture that wrote the old construction became inert), D7 (it costs a round trip)
are each that one substitution not being followed through. The unit's comments show the author
reasoning carefully about the *semantics* of the swap — the ancestry-vs-equality decision is
correct and well-argued — while the *failure modes* of the new source were handled in one place
(`[ -n "$b" ]` at `:383`) and not the others.

The single highest-leverage gate is therefore not any of the per-defect arms above: it is a rule that
**every value derived from `ls-remote` is unusable until it has been proved non-empty, single-sourced
and locally present**, applied at each of the three sites in this file. The driver already implements
that rule across its checks 24, 25, 27 and 30. The leg should not have needed to rediscover it.

## Fold — 2026-08-17, by the run that was reviewed

**All seven folded. Driver 311 assertions, leg 178, both 0 fail; check-arms green.**

- **D1 (blocker)** the advertisement block gained the `else` it never had. Armed, with a
  reachable-remote control beside it so the arm is not green for the fixture's reasons.
  Worth stating exactly: the code was fail-OPEN under a comment this run wrote claiming
  "FAIL-CLOSED, decided rather than left open". Every arm in the unit passed throughout because
  every fixture had a reachable remote — the `fixture-passes-by-finding-nothing` class the
  bug-class checklist had pre-selected for this diff, missed anyway.
- **D2 (high)** the leg now requires exactly one remote, matching the driver's check 24. `| head -1`
  blessed whichever name sorted first.
- **D3** `$b` is proved present locally before use; an absent tip disables the ancestry half only.
- **D4** `anchor-kind`/`branch-ref`/`branch-sha` are pinned once, as `base` already was.
- **D5** the lifecycle control PUSHES instead of moving a ref the leg stopped reading.
- **D6** `observe_branch` deleted. It went dead in the resolve_base refactor and its four `fail`
  branches were byte-identical twins of the live emitter's, scored ARMED. `ARMS_FLOORS` had been
  RAISED to 83:80 over that dead code — the inversion of what a ratchet is for — and now sits at
  79:76 measured, with the leg at 66:66.
- **D7** the advertisement is guarded on the population; it made two network round-trips per bar
  run with no run-state file present.

**The review's root-cause line is the accurate one** and is kept here rather than paraphrased: an
observation replaced a construction, and the new source's failure modes were handled at one site
out of three.

## Provenance — which BASE this review sits against

The run's pinned BASE is `401416faebff58c4527abef9f1a4ae80d244c4f2`. This review was scoped
`eb09d6e..HEAD` and the earlier one `3e5c6d4..HEAD`, so NEITHER range starts at that commit, and
saying so is the point of this section rather than a footnote to it.

Why the ranges differ from M8's "from the run's pinned BASE": `401416f..HEAD` spans two reconciles
that pulled in roughly 4,000 lines from five other builds — `dClosedLexicon`, `aWalkedCorpus`,
`aBoundedVerdict`, `aTetheredConvoy`, `cSettledDocket` — each already reviewed and gated by the run
that landed it. Reviewing them again would have produced findings about other people's landed code
and diluted the lenses across a diff ten times the size of this run's own work. The two ranges
together cover every line THIS run authored: `3e5c6d4..HEAD` for units 1 and 2, `eb09d6e..HEAD` for
unit 4.

What that costs, stated rather than implied: no adversarial pass examined the SEAM between the
merged-in work and this run's, beyond the gates. The merge conflicts were resolved by hand in
`memory/backlog/TOOL.md`, `memory/archive/TOOL.2026-08-17.md`, `tools/install-prefix-waivers.txt`
and the two generated indexes, and those resolutions are covered by the bar rather than by a review.
