**Serves:** diff-review DEPL-cMendedVintage-1 DEPL-cMendedVintage-5 DEPL-cMendedVintage-7 DEPL-cMendedVintage-16 DEPL-cMendedVintage-24 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-12

# cMendedVintage — closing diff review, ROUND 3

*Node `c`, 2026-09-21. **Round 3.** A Tier-2 adversarial pass over the work done AFTER round 2: a
parallel fan of primed finder lenses, a skeptic stage prompted to REFUTE each finding, one
synthesis. Round 1 returned BLOCKED with three blockers
([record](2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md)); round 2 returned BLOCKED
with one blocker and two highs
([record](2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md)). Every finding of both is
adjudicated and disposed, and **none of them is re-reported here.** Every citation a surviving
finding rests on was re-opened in this worktree at `0ab9f708` before this record was written.*

**Reviewed range:** `4877af81c05b54b1b995f44adf5396e947ccb73a...HEAD`.

## Verdict: BLOCKED

No finding this round is BLOCKER-severity. The verdict is BLOCKED on one HIGH, and on a run that
came back short of its own fan.

The HIGH is a **behaviour regression against origin/main**, introduced by a hand resolution in this
branch rather than by anything upstream: `tools/memory-tree/kit.toml:132` narrowed an `ok = true`
outcome row with a presence term that holds on only one of the two states the adopter exits 3 on,
so a target with no `memory/HYGIENE.md` — which is the kit's OWN declared seed-and-stop steady
state, pinned nine lines above at `kit.toml:108` with the comment "Every correct first install ends
here" — now gets a hard `govkit update` failure with writes left staged. Before `a2bb07f2` that stop
was accepted unconditionally. It is reproduced against the merged engine, not argued. A build whose
whole subject is `govkit update` rollbacks for adopters should not land a change that wedges the
first `update` an adopter runs.

Second reason, and it is independent of the findings: **one of four lenses DIED.** The finding set
is INCOMPLETE as delivered, so no zero anywhere in this record is evidence of absence.

The asymmetry rounds 1 and 2 both named still holds. `gov` does not dogfood `govkit`; `.governance/`
carries a `deploy.toml` and no `install.json`. A green bar on this tree is therefore **not** evidence
against H1, which lands on the first adopter target that takes this vintage.

**Review shape.** Raw 8, confirmed 8, refuted 0, unverified 0, precision 1.00. Precision of 1.00 over
eight raw findings is not a boast about the fan — three of the eight are the same defect and two more
are a second same defect, so the fan agreed with itself twice. Adjudicated counts, stated both ways
so the table below and the returned ids agree: **by item, HIGH 1 · MEDIUM 1 · LOW 3, five items**;
**by raw confirmed finding, HIGH 2 · MEDIUM 1 · LOW 5, eight findings.**

**Run integrity.** Lenses **3/4 returned, 1 DIED**. Skeptic batches 4/4 returned, 0 DIED. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates reported by
the harness. **This run is NOT complete.** The harness did not name which lens died, so the blind
spot cannot even be localised to a territory — it could be the security lens, the integration-seams
lens or any other. Where this record says "checked and found nothing", that phrase covers the
spot checks named in the last section, which are mine, and nothing else.

**Consolidation, stated so the arithmetic is checkable.** The 8 confirmed findings describe **5
distinct defects**. The harness reported 0 duplicates; that is a delivery fact and it is wrong as an
adjudication. Three lenses independently found the same dead `TOOL_ROOT` store in
`adopt-process-monitor.sh` (delivered 1, 5, 8) and two independently found the same outcome-probe
narrowing in `memory-tree/kit.toml` (delivered 2, 7). Nothing was dropped in the merge — every one of
the 8 is represented below and each entry names the delivered ids it carries. Two rows are graded
away from their delivered severity, and both moves are stated at the row.

**Scope, and it is the point of the round.** The 317 upstream commits that arrived in `e7752bcc` and
`4fab2724` from `dLoggedFlight`, `aBlindedTrial`, `aProbedToolkit`, `aHonedRuleset` and
`aWokenSentinel` are already reviewed and landed on `origin/main`, and were NOT read. What was read:
the nine branch commits `5fdb0f5b fb955322 92e3bab9 a2bb07f2 0383ac7f 48d7a13c 70681e9d 5028f05e
4ac33d5c` plus `0ab9f708`, and the 34 hand resolutions inside the two merges. Every finding below
sits in a hand resolution or in a branch commit.

**The binding line is twelve ids, not round 2's forty**, and the difference is the scope above rather
than a narrower reading. These are the units whose product this diff touches: the dirty-path guard
and the write scanner repaired in `5fdb0f5b` (`DEPL-24`, `DEPL-26`, `DEPL-28`), the regenerate
declarations and their `GOVKIT_RERENDER` prose reworded in `a2bb07f2` (`DEPL-5`, `DEPL-7`), the
acceptance-matrix arm that same commit fed (`DEPL-16`), the dead-path fixture literals declared in
`92e3bab9` (`DEPL-27`), the `--render` verb whose exit-1 marker refusal was removed (`TOOL-1`), the
two settings-merge units whose files were resolved by hand (`TOOL-3`, `TOOL-4`), the grandchild
write-end class repaired across four more loops (`TOOL-12`), and `DEPL-1`, whose subject — no
rollback over a render step this run declined — is exactly what H1 breaks.

| | Severity | Where | What |
|---|---|---|---|
| **H1** | HIGH | `tools/memory-tree/kit.toml:132` | An accepted stop narrowed to half its condition, so a seeded-but-unscaffolded target hard-fails `govkit update` |
| **M1** | MEDIUM | `memory/guides/SESSION-KICKOFF.md:127` | The CR-bytes bullet had its own control bytes eaten; it now says a newline becomes a newline |
| **L1** | LOW | `tools/process-monitor/adopt-process-monitor.sh:92` | The merge kept both sides' `TOOL_ROOT` derivation; the first is dead and the two disagree on a trailing slash |
| **L2** | LOW | `tools/memory-tree/kit.toml:100` | The `NO [[outcome]] PAIR` rationale describes an exit code `--render` can no longer produce, and one live exit-1 path is now mislabelled |
| **L3** | LOW | `tools/govkit/govkit.py:5129` | Round 2's H2 guard made the fold's `else None` fallback unreachable |

---

## H1 — the accepted exit-3 stop was narrowed to half the condition the adopter exits 3 on

*Delivered ids 2 and 7. Delivered at medium and high; adjudicated **HIGH**, on the higher of the two,
because the second reading reached the state the first did not: the unclassified half is not an
exotic target, it is the kit's own declared first-install steady state.*

**`tools/memory-tree/kit.toml:132`** — `probe = { must_exist = "{memory_root}/HYGIENE.md" }`, added by
`a2bb07f2` to the `code = 3` / `means = "not-rendered-here"` block.

`tools/memory-tree/adopt-memory-tree.sh:79-84` exits 3 on a **disjunction**:

```sh
if [ ! -f "$MEMORY_ROOT/HYGIENE.md" ] || ! grep -q 'gov:kit memory-tree@' "$MEMORY_ROOT/HYGIENE.md"; then
```

The probe can only ever match the second half. Exit 3 occurs nowhere else in that script, so
narrowing buys nothing and costs the first half outright.

Reproduced twice, and neither is an argument:

- Over the shipped descriptor, through the merged engine's own functions: with `memory/HYGIENE.md`
  present, `classify_outcome(...)` returns `not-rendered-here` and `outcome_accepted(3, …)` is True;
  with it absent, `classify_outcome` returns `None` and `outcome_accepted(3, None, True)` is **False**.
- In a scratch git repo holding nothing but a seeded `.memory-tree.conf` and the kit, `--render`
  exits 3 with `HYGIENE.md` absent. That is the unclassified half arriving in the wild.

Reachability through `update` is not theoretical. `_rerender_on` is ON by default
(`tools/govkit/govkit.py:8558`; only `GOVKIT_RERENDER=0` disables it), the regenerate loop at
`govkit.py:8617-8656` skips only inert kits, and a seed-and-stop install is stamped `adopted` by
`_cmd_apply` (`govkit.py:3655-3657`, `ok = true`), so such a target IS in the receipt and DOES get
the argv run. The result is `r.fail("the declared re-render/regenerate argv exited 3 and no declared
outcome accepts that, so the receipt is not re-stamped")` with writes staged and no rollback, for a
kit whose check cannot see the render.

The state that now fails is the one the kit declares as correct. `kit.toml:106-114` pins
`must_exist = ".memory-tree.conf", must_not_exist = "{memory_root}/HYGIENE.md"` as the accepted
seed-and-stop, with the comment "Every correct first install ends here". After `a2bb07f2` the
descriptor holds two `ok = true` rows that **contradict each other on one path**: one is accepted
only when `HYGIENE.md` is absent, the other only when it is present. And it is verbatim the wedge the
exit-3 row's own comment at `kit.toml:121-127` says the row exists to remove — "read the refusal as a
wedge and told the operator to repair by hand a render that should never have run".

**Fix.** `probe = { must_exist = ".memory-tree.conf" }`. The term cannot simply be deleted:
`tools/govkit/matrix.py:157-165` REQUIRES a `must_exist` on every `ok = true` block, which is
`DEPL-cMendedVintage-16`'s arm and is the reason `a2bb07f2` added one at all. The conf satisfies that
arm, it holds on BOTH halves of the branch, it cannot be satisfied by a run that died before writing
(the adopter refuses and seeds it long before line 79), and it is already the sibling row's
discriminator, so the two stay consistent. If the marker-less-but-present state is wanted as its own
classified outcome, it needs its own `[[outcome]]` block rather than a narrowing of this one. Fix L2
in the same pass — same file, same commit, same reading.

**Left-shift gate.** Extend `check_outcome_probes` in `tools/govkit/matrix.py`, which already owns
this class and already has every descriptor parsed: within one descriptor, two `ok = true` outcome
rows must not disagree about a single path, one declaring `must_exist` where the other declares
`must_not_exist`. Six lines, no argv analysis, and it reds exactly this. Run the predicate over the
three shipped descriptors before wiring it and print near-misses — a descriptor could legitimately
discriminate two accepted stops by one file, and if one does it takes a named exemption rather than
a silent widening. The fuller gate, if the cheap one proves too blunt: for each `[[regenerate]]`, run
the argv in a scratch target seeded to each of that kit's own declared accepted steady states and
assert `outcome_accepted` is True for each — derived rather than declared, at the cost of a scratch
run per kit. Either way, stage the break and confirm RED before landing it.

## M1 — the CR-bytes bullet had its own control bytes eaten, twice

*Delivered id 3, at medium. Adjudicated **MEDIUM**, unchanged.*

**`memory/guides/SESSION-KICKOFF.md:125-131`.** The bullet reads, on bytes:

```
  lone `<LF>` into `<LF>`, which leaves `sub(/` with a newline inside the regex …
```

Both sides of the "turns X into Y" are literal newlines. The sentence now asserts that a text-mode
read turns a newline into a newline, and the one fact the bullet exists to carry — CR `0x0D` becomes
LF `0x0A` — is gone. The file contains zero CR bytes. An LF inside a code span also renders as a
space, so no reader recovers it from the rendered page either, and the column-0 continuation lines
break the list item's rendering on top of that.

This is the second attempt at the same sentence. `48d7a13c` wrote it carrying the raw CR on the left
side; `70681e9d` "repaired" it by substituting a newline for the CR. One correction to the delivered
finding, which does not change the verdict: it attributed the empty span to `48d7a13c`, and the
diffs say `48d7a13c` had the byte and `70681e9d` removed it.

The cost is not cosmetic. A session front-loading this manifest learns nothing about the trap, which
is precisely how this build re-broke `check-unattended.sh`'s four CR bytes in the first place — the
bullet's own stated motivation, in the bullet that no longer states it.

**Fix.** Never put a raw control byte in the manifest; it is the document most likely to be rewritten
by a text-mode tool, which is the whole subject of the bullet. Spell them by name: "turns a lone CR
(0x0D) into LF (0x0A), which leaves `sub(/` with a newline inside the regex".

**Left-shift gate.** Two lines in `skills/session-kickoff/manifest-check.sh`, both derived, neither
naming this bullet: (a) the manifest carries no `0x0D` byte; (b) no line of the manifest carries an
odd number of backticks, which is what a code span split across a line break looks like and what
catches this defect by its shape rather than by its text. Lines 127 and 129 both red under (b) today.
Stage the break, confirm RED, unstage.

## L1 — the merge kept both sides' `TOOL_ROOT` derivation, and they disagree

*Delivered ids 1, 5 and 8, at low, low and medium. Adjudicated **LOW**, down from the one medium: the
sole live consumer re-adds the separator itself, so there is no wrong output today, and the medium
reading's own skeptic called that severity generous.*

**`tools/process-monitor/adopt-process-monitor.sh:92`.** Both routes survived the reconcile:

- line 92 derives `TOOL_ROOT`, line 93 appends a trailing slash ("trailing slash so a root install
  renders clean") — this branch's side, `TOOL-cMendedVintage-4`;
- line 100 re-derives the same value WITHOUT the slash — origin/main's side;
- line 101 is `SMERGE_REL="${TOOL_ROOT:+$TOOL_ROOT/}settings-merge.py"`, which supplies its own
  separator.

`grep -n` returns `TOOL_ROOT` at exactly 92, 93, 100, 101 and `SMERGE_REL` at 101 and 234. Between
lines 93 and 100 sit a blank, `PY=$(resolve_python …)` and a four-line comment — nothing reads
`TOOL_ROOT`, so lines 92-93 are a pure dead store. The script is `set -u` without `set -e`, so the
`&&` on a false test is harmless. Merge-introduced as claimed: `grep -c '^TOOL_ROOT='` is 1 at both
parents (`92e3bab9`, `0e61932d`) and 2 at HEAD.

No live wrong path today. What makes it worth a row is that the file now holds two answers to one
question with **opposite conventions**, and the comment sitting on top of the dead one — line 91,
"One file, one route, two answers. TOOL-cMendedVintage-4" — condemns the exact state the merge
re-created underneath it. Any line inserted between 93 and 100 reads the slashed value; anything
after 100 reads the slash-less one. The arithmetic of the trap: with `TOOL_ROOT="tools"`,
`${TOOL_ROOT}settings-merge.py` renders `toolssettings-merge.py`.

**Fix.** Delete lines 87-93 and fold the `TOOL-cMendedVintage-4` provenance sentence into the
surviving comment at 96-99, leaving one derivation at line 100 consumed only through `SMERGE_REL`.

**Left-shift gate.** This is the "kept both sides" merge class, and a static shell gate for dead
stores in general is not worth its own maintenance. Two cheap things instead, in this order: register
the class as a gotcha so `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` prints it
into the bug-class checklist of every future reconcile — the repo's own mechanism for a class no gate
fits; and, if a gate is wanted, the narrow derivable one is an awk pass over tracked `.sh` files
flagging the same name assigned twice at column 0 with no read between, run over the whole tree first
to see what it reds before anyone wires it.

## L2 — the descriptor's `NO [[outcome]] PAIR` rationale names an exit code `--render` can no longer produce

*Delivered id 6, at low. Adjudicated **LOW**, unchanged.*

**`tools/memory-tree/kit.toml:100-102`** says `--render` "exits 1 only on a tree already carrying
`{memory_root}/HYGIENE.md` without the marker — the state `refused-foreign-tree` below already
classifies". After `a2bb07f2` removed the exit-1 marker refusal from the adopter, that state exits
**3**, not 1. `kit.toml:89` ("requires the `gov:kit memory-tree@` marker instead") and
`adopt-memory-tree.sh:132` ("--render then refuses for a missing marker") are stale in the same
direction but more weakly — the marker is still read, it just no longer refuses.

The half that is more than prose: the exit-1 paths that ARE still reachable under `--render` on an
adopted tree are the blank-`READINESS_ROWS` refusal (`adopt-memory-tree.sh:88-90`, which sits AFTER
the marker gate, so an adopted tree reaches it) and the missing-template refusal inside `render_all`
(returned to `render_all || exit 1`). Both exit 1 with `{memory_root}/HYGIENE.md` present, so the
`code = 1` probe at `kit.toml:116-119` matches and labels them **`refused-foreign-tree`** — the wrong
`means` for either. Outcome rows are not step-scoped; the `code = 3` row's own comment says the
regenerate step reads them, which is why that row was added at all. The blast radius is a misleading
label on a stop that stays a failure either way, which is why this is LOW and not MEDIUM.

**Fix.** Rewrite `kit.toml:89` and `100-102` to the post-merge truth: `--render` answers the marker
question at exit 3 as an accepted stop, and its remaining exit-1 states are the `READINESS_ROWS`
refusal and the incomplete-render-set refusal. Either give those a `code = 1` row of their own, or say
in the comment that `refused-foreign-tree` will mislabel them. Fix `adopt-memory-tree.sh:132` in the
same pass, and H1 with it.

**Left-shift gate.** The engine already gates descriptor prose — the regenerate-prose rule that
demands any sentence naming `update` and a re-render also name `GOVKIT_RERENDER` is what turned three
of this reconcile's kit files red in the first place. Extend that family with one derived rule: an
exit code named in a descriptor's prose or in an `[[outcome]]` comment must be a code the declared
argv's script can actually produce, derived by scanning that script for `exit N`. It is a grep of a
file the descriptor already names, it cannot go stale, and it reds `kit.toml:100` today.

## L3 — round 2's H2 guard left a dead `else None` in the fold beneath it

*Delivered id 4, at low. Adjudicated **LOW**, unchanged.*

**`tools/govkit/govkit.py:5129`.** `check_region_only` now guards unconditionally at line 5120 with
`if not (target / path).is_file(): return False`, and the ternary at 5128-5129 re-tests the same
predicate: `derive_outside_region((target / path).read_bytes() if (target / path).is_file() else
None, om, cm)`. Between the two sit only `index_read` and `index_blob`, both read-only git calls, so
no deterministic execution reaches the `else None` arm. Only an external concurrent deletion during
those subprocesses could, and no comment claims that intent, so it is not defensible as deliberate
TOCTOU handling.

It is the same dead-branch shape the reconcile itself already found and removed in
`adopt-memory-tree.sh`, one file over. The risk is a reader concluding the fold still covers the
absent-worktree case — the case the round-2 H2 guard now refuses — and re-opening that hole by
deleting the guard. Plus one redundant `stat`.

**Fix.** Collapse to `derive_outside_region((target / path).read_bytes(), om, cm)` and let the guard
above own the absence. If the ternary is kept deliberately, say so beside it and say why.

**Left-shift gate.** None earns its cost. An AST rule for "a ternary re-tests a predicate an earlier
`return` already settled" is more machinery than the defect, and this class is already what §10 asks
a Tier-2 reader to look for. Documented check instead, in the recurring-bug-class list: **a guard
added above a fold makes the fold's own fallback dead — collapse it or state why it stays.** Two
instances in two files in one diff is enough of this repo's own evidence to earn the line.

---

## What this round spot-checked and did not find

These are mine, run against the tip while adjudicating. They are not lens coverage, and with one lens
dead none of them is evidence that the territory is clean.

- **Version markers.** Every `unattended@` marker in `tools/unattended/` reads 1.27 — nineteen sites
  across the four gated `.sh` files, the `.js` courtesy markers including the three that arrived with
  `aWokenSentinel`, and every template. `KIT_CHECK_WIRING_VERSION` is 1.5 at `tools/check-wiring.sh:23`
  and the entry descriptor reads it from that same pattern. No 1.25 or 1.26 left behind.
- **The four raw CR bytes in `tools/unattended/check-unattended.sh`.** Still four, at lines 948, 1508,
  2144 and 2145, inside the `sub(/…$/,"")` awk regexes and the `tr -d` at 1508. The byte-level
  re-resolution held. M1 is about the manifest bullet that documents them, not about these.
- **`BRANCH_PIN` at 255 against a measured 264.** Sound. `tools/govkit/refusal_join.py:233` is
  `if len(branches) < BRANCH_PIN`, a floor and not an equality, and the file's own line 44 says so.
  Not a finding. Worth one sentence anyway: a floor left nine below the measurement is nine branches
  of slack, so the pin will not notice the first nine refusals anyone deletes.

## What this round did not cover, stated so a green line is not misread

- **One lens of four DIED.** The finding set is incomplete and the gap is unlocalised.
- **The 317 upstream commits were not read**, by instruction. Their review is on `origin/main`.
- **The merge bar is GREEN at 54/54 on this tip**, and that says nothing about H1: `gov` does not
  dogfood `govkit`, so no leg on this bar executes the adopter path H1 breaks.
- **The deployer suite reports 34 failures, unchanged from before the merge.** Unchanged *count* is
  weaker than unchanged *set*, and the sets were not compared. A regression that swapped one failing
  arm for another is invisible to the comparison actually performed.
- **`resume-tick.test.sh` reports 162 passed, 1 failed, byte-identical to `origin/main` unrepaired.**
  The one failure is a wall-clock threshold on a loaded box. Byte-identical to the upstream result is
  good evidence the four loop repairs changed no behaviour, and it is not evidence that the scratch
  files they now write are cleaned up on every error path — that arm went unexercised.
