**Serves:** diff-review TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

# Closing diff review — the cumulative dBriefedPass diff landing on main

*Node d, 2026-09-01, unattended prompt-mode run under a standing mandate. Five units shipped: the `plan_state` title-grading correction and its BUILD-METHOD M2 half, the `--brief` verb, the `--dispatch` refusal plus the new `pass-order history` merge-bar leg, the `unattended-build.js` harness, and the carrier edits that declare both. Finder lenses primed on the two classes the brief named as live over this range — a SECOND READER of `plan_state` sliced out of the driver, and FOURTEEN compressed passages of a BINDING contract — then batched skeptics prompted to REFUTE each finding against the source. Every citation below was re-derived against the tree by the author of this record before it was graded.*

**Reviewed range:** `269dacae79bd5001486de32b3277675a953d3483...HEAD` — nine commits, of which five are the unit builds (`ac4875fb`, `b9fb4fb0`, `ead1b820`, `021d29bd`, `0c1ce54b`). **ROUND 1.**

## Verdict: BLOCKED

Three blockers stand. Two are in the one file this build added to the merge bar: `tools/unattended/check-pass-order.sh` is the leg whose entire subject is a run that games its own records, and it can be silenced by the run it grades (B1) and reds honestly on a run that did everything right (B2). The third is worse in one respect — **the merge bar is RED right now, and has been since `b9fb4fb0`** (B3).

Twenty-five confirmed findings were filed against this range; they consolidate to **seventeen distinct defects** — several were the same defect reached from two or three sides, and the consolidation is shown in the table's `filed as` column rather than performed silently. **B3 was filed by nobody.** It was found by this synthesis pass running the merge bar against the tree rather than reading the diff, so it is the eighteenth defect and it does not appear in the shape numbers below. That a whole lens fan read this range and none of them ran the gate the range reds is worth more than the finding itself.

**Review shape.** Raw 32 · confirmed 25 · refuted 7 · unverified 0 · precision 0.78. Plus one defect (B3) found outside the fan, by execution rather than by reading.

## The findings

| # | Sev | Site | Defect | Filed as |
|---|---|---|---|---|
| B1 | blocker | `tools/unattended/check-pass-order.sh:60` | the leg sources its subject's own working-tree file into its own shell | 1 |
| B2 | blocker | `tools/unattended/check-pass-order.sh:142` | a SPEC commit is selected as the BUILD commit, so a conforming run reds | 25 |
| B3 | blocker | `memory/builds/dBriefedPass/README.md:8` | two negative-test ids in the authored roster — the bar is RED now | *none — found by execution* |
| H1 | high | `tools/unattended/.unattended.conf.example:215` | the adopter template ships this repo's landing date as a live cutoff | 4, 29 |
| H2 | high | `tools/workflows/unattended-build.js:262` | M4's blocker disposition is asserted by comment and implemented nowhere | 15, 6 |
| M1 | medium | `tools/unattended/check-pass-order.sh:110` | the grading cutoff is read from a field the graded run authors | 2 |
| M2 | medium | `tools/unattended/unattended.sh:4490` | a reader refusal is swallowed and reported to the agent as MISSING | 7 |
| M3 | medium | `tools/unattended/unattended.sh:4500` | the new order gate has no test arm and its failing case was never observed | 8, 28 |
| M4 | medium | `tools/unattended/unattended.test.sh:3996` | the anti-collapse arm cannot fail on the collapse it names | 9, 27 |
| M5 | medium | `tools/workflows/unattended-build.test.sh:1` | a 21-arm suite registered in no manifest, run by no bar | 10, 18 |
| M6 | medium | `tools/unattended/check-pass-order.sh:29` | a version constant nothing compares, under a comment saying it is paired | 16 |
| M7 | medium | `tools/unattended/run-unattended-gates.sh:172` | the kit's DECLARED compensating runner never runs the new leg or its suite | 17 |
| M8 | medium | `tools/workflows/unattended-build.js:246` | one sentence hands the agent two vocabularies for the gating field | 19 |
| M9 | medium | `.claude/skills/unattended/SKILL.md:93` | `passes-harnessed` points at M6, which states no such rule | 20 |
| M10 | medium | `tools/unattended/unattended.sh:4509` | two readers of the `order` verb, and the disagreement is a silent skip | 21, 26 |
| L1 | low | `.claude/skills/unattended/SKILL.md:503` | `--propose` prose now renders as `--brief` prose, in both halves of the pair | 11, 22, 32 |
| L2 | low | `memory/guides/UNATTENDED-PROTOCOL.md:1` | the render lands at exactly the cap, zero headroom | 12 |
| L3 | low | `tools/unattended/kit.toml:67` | "THE THREE LEGS BELOW STAY" now precedes four | 23 |

---

## B1 — BLOCKER — `tools/unattended/check-pass-order.sh:60` — the new merge-bar leg sources its subject's own working-tree file into its own shell

```sh
MEMORY_ROOT=""; PASS_ORDER_CUTOFF=""
# shellcheck disable=SC1090
. "$CONF"
```

`$CONF` is `$ROOT/.unattended.conf`, a **tracked** file the graded run commits. Sourcing it executes it. A one-line append is enough to end the leg, hijack it, or leave it printing its own failure while exiting green.

**Impact, reproduced.** On a fixture that reds honestly (`pass-order FAILED ... rc=1`):

- appending `exit 0` gives **rc=0 with zero bytes of output** — byte-indistinguishable from a clean tree, and `run-gates` records it as `GATE ok`;
- appending `trap 'exit 0' EXIT` is worse: the leg **PRINTS** `pass-order FAILED — a unit was BUILT before a conforming spec` and still exits 0, so the bar is green while the leg's own text says it failed;
- `MEMORY_ROOT=memoryy` yields `graded 0 ... rc=0`.

The conf is sourced at line 60, **after** `lib-unattended.sh` loads at line 47, so it can also redefine the pinned `GIT` wrapper that the file's own header spends nine lines insisting on — the wrapper that exists because a substituted object would flip exactly the ancestry answers this leg grades. The leg is registered in `tools/gate-legs.json` with `"subject": "repo"` and `"guard": []`, so it runs on every bar; the doctored conf travels with the push, so it also defeats §9's "what actually binds" — the same leg re-run in a clean clone.

**This is not the conceded cost.** PROTOCOL §1 cost 2 concedes that a leg reading the conf reads its subject's *answer* — value manipulation. It does not concede code execution that suppresses the leg's own return code and output.

**Both siblings already refuse this exact shape, with recorded incidents.** `check-unattended.sh:121-140` documents its round-8 (`exit 0`) and round-9 (`trap`, redefined `fail()`) blockers and imports the conf through a subshell with a NUL sentinel. `check-playbook.sh:74-86` records the same and uses a subshell `_conf_key`. Neither guard was carried into the new leg, and `check-pass-order.test.sh` has no hostile-conf arm.

**Fix.** Import rather than source: run `. "$CONF"` inside a subshell, hand the declared keys back as a NUL-delimited name/value stream terminated by a sentinel, exit 2 when the sentinel is absent, and assign only `[A-Z][A-Z0-9_]*` names. **Reuse `check-unattended.sh`'s block verbatim** — a third hand-written reader is the same class one level up. Separately, since the leg reads its subject's own answer, resolve `PASS_ORDER_CUTOFF` at the run's pinned BASE rather than from the working tree, or say in the header that it cannot be trusted from there.

**Left-shift gate.** A merge-bar leg that greps every `tools/**/check-*.sh` for a bare `^[[:space:]]*\. "\$CONF"` — or any `.`/`source` of a repo-root path outside a subshell — and reds on a hit. Three scripts now read this conf and two of them were hardened one incident at a time; the class is what needs the gate. Plus the two missing fixture arms in `check-pass-order.test.sh`: append `exit 0`, append `trap 'exit 0' EXIT`, assert non-zero exit in both.

---

## B2 — BLOCKER — `tools/unattended/check-pass-order.sh:142` — a SPEC commit is selected as the BUILD commit, so a conforming run reds at its own parent

STEP 1 picks the earliest commit in `BASE..HEAD` whose subject carries the unit id as a whole token and which touched a path **outside `$bdir/spec/` and `$bdir/reviews/`**. Those two prefixes are the whole exclusion. A spec pass legitimately writes more than that: the regenerated `memory/LIVE.md`, the build `README.md`, `RUN.md`, the month ledger. All four sit outside both prefixes, so a spec commit whose subject names the unit id wins the selection, and STEP 2 then grades that commit's parent — where, correctly, no spec exists yet.

**Impact, reproduced.** A fixture whose run authored the spec **before** the code exits 1 with:

```
pass-order FAILED — ARCH-tOrder-1 — BUILT at 29b1431 with NO tracked spec at that commit's parent ff11d7f; the spec was written after the code
```

which is the exact opposite of what happened.

**The shape is the corpus norm, not a corner.** `git log --format=%s` over this tree carries `spec(TOOL-aGradedDoorway-7): rev-3 ...`, `spec(aGroundedOrientation): TOOL-aGroundedOrientation-1 and -2 authored`, `spec(dTieredTribunal): TOOL-dTieredTribunal-1..3 ...`. Checked `96ae4f14` directly: it touched `memory/DECISIONS.md`, `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README and the ledger. **This build escaped only by luck** — its own spec commit `c5ceb93e` touched `memory/LIVE.md`, the build README, `RUN.md` and the ledger, and passed solely because its subject names the slug and no unit id.

The leg is `guard = []` with `red_after_land = true`. History is append-only. So the next conforming run whose spec commit names a unit id is **unlandable** short of `--no-verify` — and the run it punishes is the one that followed the method exactly.

**Fix.** Widen the exclusion to everything a spec pass legitimately writes: the build's whole folder (`^$bdir/`) plus the declared `GENERATED_INDEXES` paths, and treat a commit touching **only** those as not-a-build-commit.

**Left-shift gate.** Add the arm that proves it, in `check-pass-order.test.sh`: take the existing `spec-first` fixture, change the spec commit's subject to `spec(tOrder): ARCH-tOrder-1 authored`, add a `memory/LIVE.md` write to that same commit, and assert the leg stays GREEN. It currently goes RED — which is the failing case the charter requires to have been observed before this leg was landed.

---

## B3 — BLOCKER — `memory/builds/dBriefedPass/README.md:8` — the build's own negative-test ids were added to its authored roster, and the merge bar is RED now

```
ids: TOOL-dBriefedPass-1 ... TOOL-dBriefedPass-5 <slug>-77 <slug>-99
```

The `…-77` and `…-99` ids are not units. They are this build's **negative-test ids** — the deliberately non-existent ids its own live acceptance observations use to prove a refusal fires:

*A NOTE ON THIS SECTION'S OWN SPELLING, added by the fold. The two ids below are written with their
sequence detached — `…-77` rather than the full id-shaped token — because check 14 scans for that
shape and `gen_build_index.py` harvests it into the README's derived `ids:` roster. Spelled in full,
this record would REPRODUCE the very defect it reports, and the first draft of it did exactly that:
the review's own author caught a third orphan id introduced by a naming example. The finding is
unchanged; only the way the ids are written is.*


- `build/2026-09-01-build-TOOL-dBriefedPass-2-1-brief-verb.md:46` — AC2, `--brief --unit <slug>-99` must be refused as off-roster;
- `build/2026-09-01-build-TOOL-dBriefedPass-3-1-pass-order.md:37` — AC1, `--dispatch --pass <slug>-77` must be refused as MISSING.

They were then written into the build README's authored `ids:` front matter. `-99` entered at `b9fb4fb0` (unit 2), `-77` at `ead1b820` (unit 3). Both are in this range.

**Current state, measured.** `bash tools/memory-tree/check-memory-hygiene.sh` exits **1** on this tree:

```
HYGIENE check 14: id <slug>-77 is cited but never defined, and is not in memory/project/id-orphan-waiver.txt
HYGIENE check 14: id <slug>-99 is cited but never defined, and is not in memory/project/id-orphan-waiver.txt
```

The `memory hygiene` leg is `subject: repo` with **no guard**, so it runs on every bar, in every mode, from `b9fb4fb0` through to landing. This build cannot land.

**The waiver route is closed, and closed correctly.** `memory/project/id-orphan-waiver.txt` is EMPTY and shrink-only under `ORPHAN_ID_PIN` — its own header records the pin falling 5 → 0. Adding a row would red the pin. So the only repair is deleting the two ids, which is the right repair anyway.

**Why it is inert today rather than actively wrong, and why that is not reassuring.** Two readers consume two different id lists. `unit_ids_of` (`unattended.sh:1770`) derives the roster from the **generated `roster:units` region**, which carries only 1-5 — so the `--brief` and `--dispatch` off-roster refusals those acceptance criteria depend on still fire. Hygiene check 14 reads the **authored front matter**, and reds. The build put the ids in the one list that does not feed the refusals, so the evidence survives by accident of which reader looks where. Had it landed in the other list, this build's own AC2 and AC1 would have quietly stopped testing anything — an acceptance criterion certified by a value the same commit made invalid. That is `two-readers-of-one-config-one-re-derived` paying out in the build that shipped two more instances of it.

**Fix.** Delete the `…-77` and `…-99` ids from `memory/builds/dBriefedPass/README.md:8`, then `python tools/memory-tree/gen_build_index.py --write` (the value propagates into the `gen:build-index` region at :68 via `gen_build_index.py:673`). One line, and the bar goes green.

**Left-shift gate.** Check 14 already gates the class and did its job — nothing new is owed there. What is owed is upstream: a build record that cites an id in an acceptance observation should never be a reason to roster it, so **mint negative-test ids outside the live slug entirely** — the `tRun`-style fixture slug the driver suite already uses — rather than reaching for a high sequence number inside the build's own slug, where the id is well-formed, indistinguishable from a real unit, and one careless edit from being rostered. (This report tripped the same wire while drafting: an illustrative id spelled in this paragraph reddened check 14 on its first run, which is as good a demonstration of the class as the finding deserves.) A cheap mechanical form: red on any `<ROSTER>-<this-slug>-<n>` id appearing in a build's `build/` records but not in its generated units region — it is either an orphan or a fixture wearing the build's own name, and both want fixing. The deeper lesson is the one in the verdict paragraph: **run the bar before filing the review.** Twenty-five findings were read out of this diff by a fan that never executed the gate the diff reds.

---

## H1 — HIGH — `tools/unattended/.unattended.conf.example:215` — the adopter template ships this repo's landing date as a live cutoff

```
PASS_ORDER_CUTOFF="2026-09-01"
```

Every sibling cutoff in the same file ships blank: `UNITS_REGION_CUTOFF=""` (:160), `SPEC_THIN_CUTOFF=""` (:169), `LANDED_ANCHOR_CUTOFF=""` (:200). The comment block three lines above ends "Set to the day this landed" — gov-facing wording, byte-identical to `.unattended.conf`'s own block, where the `LANDED_ANCHOR_CUTOFF` block by contrast was rewritten to adopter voice and blanked.

**Impact.** An adopter who copies the example — `kit.toml:119` speaks of "the shipped conf example copied verbatim" — inherits **this repo's calendar** as their grandfather line. `check-pass-order.sh:114` then grades every build whose README `opened:` sorts at or after 2026-09-01, including builds that landed before they had the kit and whose commit order cannot be rewritten. That is precisely the failure the same comment block says the cutoff exists to prevent: "a build that landed before this leg existed cannot be rewritten, and a term that reds one is unlandable by any run." The repair is reachable (blank the key), so this is a red bar with an obvious edit rather than a wedged one — but the shipped defect stands, and the example's own header names this class: "A pin copied from another corpus is either vacuous or permanently red; this fleet tracks that as a named bug class."

Nothing catches it. The only test reading the example (`unattended.test.sh:1492ff`) iterates key NAMES, with value arms only for `CORE_FLOOR` and `DIRECTIVES_FLOOR`.

**Fix.** Ship `PASS_ORDER_CUTOFF=""` and reword the trailing line to the adopter voice its neighbours use: "Blank or absent grandfathers every build. Set it to the day you adopt this leg." Leave `.unattended.conf`'s `"2026-09-01"` as this repo's value.

**Left-shift gate.** Extend the existing example-vs-conf test to assert that **every** key matching `*_CUTOFF` in `.unattended.conf.example` is blank. That gates the class rather than this instance, and the next date-gated term is covered on arrival.

---

## H2 — HIGH — `tools/workflows/unattended-build.js:262` — M4's blocker disposition is asserted by comment and implemented nowhere

The comment at :262-265 states that on `NON-CONVERGENT` and `CEILING` "every standing blocker is PROMOTED to a unit rather than carried into code, which is what `BUILD-METHOD.md` M4 requires at the exit." Read the file whole: nothing does that. Control falls from the verdict gate (:266-285, a `CONVERGING`-only early return) straight into `phase('Build')` at :291 with `ordered` fixed at :123. The BUILD prompt (:293-308) never mentions `lastReport`, the blocker count, or promotion. `lastReport` is read only inside the `CONVERGING` return and echoed in the final return. `nextAction` — the only channel telling a caller what to do — exists solely on the `CONVERGING` path. Promoted units could not enter `ordered` anyway.

So on the two non-clean terminal verdicts the harness **builds a spec set with standing blockers**, and the report path it computed is discarded.

**The reporting half compounds it.** The run-integrity `note` at :334 tests `specRefused.length || unbuilt.length || verdict === 'CEILING'`. `NON-CONVERGENT` is omitted while its twin `CEILING` is flagged, and `NON-CONVERGENT` structurally guarantees standing blockers — `unattended.sh:3831-3833` returns `CONVERGED` only at a count of 0. Reproduced: an AUDIT returning `{"verdict":"NON-CONVERGENT","blockers":3}` with nothing refused and nothing unbuilt yields `note: "complete"`. The block immediately above invokes `memory/gotchas/degradation-known-but-unreported` by name, and then the harness computes the blocker count and reports the run as complete.

The obligation is real and cited correctly: `BUILD-METHOD.md:137` — "At the exit every blocker still standing is DISPOSED: FOLD ... PROMOTE one needing a mechanism this build lacks and audit it as a SPEC; never parked, waived or re-reviewed." `unattended.sh:3936`'s NON-CONVERGENT stdout repeats it imperatively. And it is reachable, not hypothetically: **this very build exited NON-CONVERGENT at round 3** (`1dc4f031`).

**Fix.** Either return before BUILD on `NON-CONVERGENT`/`CEILING` with a `nextAction` naming `lastReport` and requiring each standing blocker be promoted via `--rescope --act add` before re-invocation — the shape the `CONVERGING` branch already uses — or inject `lastReport` and the blocker count into the BUILD prompt with an explicit promote-before-building instruction. Either way include `verdict !== 'CONVERGED'` in the DEGRADED test at :334. If neither mechanism is intended, **delete the promotion sentence** rather than leave a claim the program does not make true.

**Left-shift gate.** An arm in `tools/workflows/unattended-build.test.sh` that stubs AUDIT to return `NON-CONVERGENT` with `blockers: 3` and asserts the return carries a non-`complete` note and a `nextAction` naming the disposition duty. Broader: this is the "gate satisfied by its own comment prose" shape §7 was ported from — a parity check that every `BUILD-METHOD.md M<n> requires` claim in a workflow script names a code path is the class-level version.

---

## M1 — MEDIUM — `tools/unattended/check-pass-order.sh:110` — the grading cutoff is read from a field the graded run authors

```sh
opened=$(sed -n 's/^opened:[[:space:]]*//p' "$readme" | head -1)
```

read from the **working tree**, and line 114's `sort -C` grades only builds with `opened >= PASS_ORDER_CUTOFF`. One character disables the leg for that build. Reproduced: a fixture that reds with `opened: 2026-06-01` prints `graded 0 closed unit(s) · 1 build(s) skipped by the 2026-01-01 cutoff` and rc=0 when the field is edited. The skip is counted — but a grandfathered build and an evaded one print the identical line, so the announcement carries no signal.

**The header's precedent claim is only half true.** It calls this "the same idiom `UNITS_REGION_CUTOFF` and `SPEC_THIN_CUTOFF` use". `SPEC_THIN_CUTOFF` does grade an authored value (the spec filename date, `unattended.sh:3327`) — but that is a **driver** term. The leg-side sibling, `UNITS_REGION_CUTOFF`, grades `GIT show -s --format=%cs "$base"` (`unattended.sh:1509`) — a commit date on a BASE pinned from the remote's own advertisement, which this run did not author and cannot restamp. So the one precedent that is itself a merge-bar input is git-anchored and outside the run's reach, and this one is not.

`opened:` is only format-validated: `gen_build_index.py:309` checks the ISO shape, and nothing anywhere compares it to git. On the second anchor the run may author its own build folder (`PROTOCOL.template.md:32`), so the run writes both the record and the field deciding whether the record is graded. The doctored value survives into a clean clone, which is the re-run §9 names as the thing that actually binds.

**Fix.** Grade on a git-derived date: `GIT log --diff-filter=A -1 --format=%cs -- "$readme"`, falling back to the pinned BASE's `%cs` as `UNITS_REGION_CUTOFF` already does. If `opened:` is kept for readability, red when it disagrees with the git-derived date rather than trusting it, and say in the header that this cutoff is graded on an authored value.

**Left-shift gate.** A fixture arm that back-dates `opened:` on a build the leg reds and asserts the leg still reds. The same arm shape covers any future cutoff read from authored front matter.

---

## M2 — MEDIUM — `tools/unattended/unattended.sh:4490` — a reader refusal is swallowed and reported to the agent as MISSING

```sh
load_spec_facts $(GIT ls-files -- "$MEMORY_ROOT/builds/$slug/spec/*.md" 2>/dev/null) >/dev/null 2>&1 || true
```

`load_spec_facts` returns non-zero specifically when `spec_facts` fails on a file it **could** open — the case its own header (`:1843-1853`) calls "not a state to paper over with an empty map", refusing because such a table "would look complete and name nothing". The sibling call site tests it: `build-complete` at :3319 announces "the spec-fact reader refused, so no unit could be graded". Here the status is discarded and the empty map falls through to the MISSING refusal at :4492 — which tells the agent this is "a unit no tracked spec under this build defines", whose documented M2 response is *author the spec*. Over a spec file that exists, and which would then FORK.

Worse: `load_spec_facts` fills its maps from the first `spec_facts` pass before re-running to test status (`:1836-1848`), so a failure leaves the maps **truncated**, not empty. The order gate below at :4513 then silently `continue`s past every earlier unit whose row was lost — the order term weakens with nothing said.

Mitigating, and why this is medium rather than higher: the path fails closed (`fail 49`, `return 1`), so no build proceeds, and awk being fatal on a readable file is rare. The swallowed status and the wrong diagnosis are real and one line from correct.

**Fix.** Mirror :3319 — `if ! load_spec_facts ...; then fail 49 "the spec-fact reader refused for this build, so no unit could be classified and --dispatch cannot tell MISSING from unreadable: $slug"; return 1; fi` before the `SPEC_PATH` lookup.

**Left-shift gate.** A repo grep leg for `load_spec_facts ... || true` — and, generally, `|| true` on any function whose header declares a refusal contract. Two call sites and two answers to one refusal is the class.

---

## M3 — MEDIUM — `tools/unattended/unattended.sh:4500` — the new order gate has no test arm anywhere, and its failing case has never been observed

`grep -rn 'declared order|order gate|out of the build' tools/unattended/*.test.sh tools/workflows/*.test.sh` returns nothing. `grep -n '· order [0-9]' tools/unattended/unattended.test.sh` returns nothing — **no fixture spec anywhere in the driver suite carries an `order` verb.** The three new dispatch arms at `unattended.test.sh:3924-3941` write a Status line of `SPECCED · rev-1 · 2026-08-20 · node a · Tier-2 · base 0123abcd` with no `· order N`, so `_d_ord` at :4510 is empty and the entire order-gate block is **skipped** in every existing arm — not passed, skipped. Even the "passing" arm short-circuits at the outer `[ -n "$_d_ord" ]`.

An out-of-order arm is not constructible against the current fixture: the `tRun` README's generated units region emits exactly one row, `ARCH-tRun-1`, `unit_ids_of` (`unattended.sh:1770`) derives the sibling roster from that region, and `--unit ARCH-tRun-99` is refused as off-roster (pinned at test :3971). Population of siblings: zero. `check-pass-order.test.sh` arms the separate history leg over a different input.

The sibling-blocking loop has real ways to be wrong: `SPEC_ST` is keyed by spec PATH not unit id, the dispatched-sibling grep interpolates the id into an ERE, and an unspecced earlier unit is silently skipped.

**Compounding: the build record claims coverage that does not exist.** `memory/builds/dBriefedPass/build/2026-09-01-build-TOOL-dBriefedPass-3-1-pass-order.md:44` cites `tools/unattended/unattended.test.sh` for the gate's equal-order (`[ "$_o_ord" -lt "$_d_ord" ] || continue`) and no-order (`[ -n "$_o_ord" ] || continue`) branches. No such arm exists. Live observation does not cover them either — all five dBriefedPass specs carry distinct orders 1-5. The record's disclosure section names the suite as unrun and says nothing about AC4, so the gap reads as covered.

**Fix.** Add a second unit to the `tRun` fixture roster with an `order` verb in both status headers, then arm both directions: dispatching the order-2 unit while order-1 is OPEN and undispatched must REFUSE naming the blocker; dispatching it after order-1 is dispatched, and again after order-1 is CLOSED, must PASS. Then either write the equal-order and no-order arms AC4 claims, or correct AC4 to say the branches are unexercised — the way the ledger's closing section already discloses the unrun suite.

**Left-shift gate.** The arms are the gate. Beyond them: `tools/check-arms.py`'s discovered population should reach `--dispatch`'s new refusal branches, so a `fail 49` site with no exercising arm reds rather than being certified by a build record.

---

## M4 — MEDIUM — `tools/unattended/unattended.test.sh:3996` — the anti-collapse arm cannot fail on the collapse it names

The arm's own comment (:3991-3993) says it exists because "the first cut of this reader lost its unit id to a heredoc-eaten back-reference and grouped every row under one key, which passes with one unit and drops rows with two." Both `--brief` calls then pass `--unit ARCH-tRun-1` (:3986 and :3996), because the `tRun` roster holds exactly one id and `verb_brief` refuses an off-roster one.

The reader (`unattended.sh:2786-2789`) is `last[u] = r` keyed on `u = substr($2, 6)`. With one distinct unit key, grouping by unit and grouping by a constant are **the same partition**. `last["ARCH-tRun-1"]` and the collapsed `last[""]` both resolve to the brief-2 row; both emit one path, one recomputed hash mismatch, `STALE briefs 1`. The arm passes byte-identically under the bug it was written to catch. Its comment — "passes with one unit and drops rows with two" — is a description of the fixture it was handed.

`fixture-passes-by-finding-nothing`, in the arm written to close that class, and doubly so in a suite that standing owner instruction leaves unexecuted.

**Fix.** Extend the `tRun` fixture's units region with a second rostered id and its spec, then order the arm so the STALE brief is recorded FIRST and a FRESH brief for the second unit LAST. The collapsed reader then reports 0 and the per-unit reader reports 1, which is the only ordering that discriminates.

**Left-shift gate.** Whenever an arm's comment names a specific broken implementation, the arm owes a discrimination proof. The cheapest mechanical form: keep the broken reader as a fixture and assert the arm fails against it. Applied here, the arm would have been rejected on arrival.

---

## M5 — MEDIUM — `tools/workflows/unattended-build.test.sh:1` — a 21-arm suite registered in no manifest, run by no bar

`grep -n unattended-build tools/gate-legs.json tools/workflows/kit.toml` returns nothing. The four sibling suites in that directory are all declared legs with matching `[[gate_leg]]` blocks: `check-verifier-fanout.test.sh` (gate-legs.json:468), `check-protocol-parity.test.sh` (:483), `tier2-review.test.sh` (:518), `check-review-join.test.sh` (:531). This one has neither, so **no bar mode reaches it** — not `GATE_FULL=1`, not `GATE_SELFTESTS=1`. I ran it by hand: 21 arms, exit 0. It works and never executes, which is exactly the state in which it rots.

Nothing else catches the omission. `map_extractors.py:100-101` defines `workflow-scripts` as `glob_inventory(ROOT/'tools'/'workflows', '*.js', ...)`, so a `.test.sh` is outside the enumerated set. `check-testsuite-counts.sh:35` derives its population from `*.test.sh` strings in the manifest, so the suite is graded for neither an executed-assertion count nor a floor — it prints `--- $n arms, exit $st` and declares no `FLOOR_ASSERTIONS`. `check-arms.py`'s population is shell gates defining `fail() {`, with `*.test.sh` excluded outright.

The 2026-08-23 ruling that took kit self-tests off the bar names the **`unattended`** kit, not `tools/workflows/`, whose four kit-subject self-test legs are still on the manifest. And unit 4's own dispatch row (`RUN.md:56`) declares writes to `tools/workflows/kit.toml` and `tools/gate-legs.json` that were never made. The build record documents the omission with a reason but names no compensating check — exemption-is-not-coverage, not a refutation.

**Fix.** Add a `[[gate_leg]]` to `tools/workflows/kit.toml` (`subject = "kit"`, `argv = ["bash", "{kit}/unattended-build.test.sh"]`, the `tools/workflows/` guard), mirror it into `tools/gate-legs.json` with `"chunk": "selftests"` and a ceiling, add the row to `tools/govkit/subject-pins.tsv`, and bring the suite up to the `PASS ($n assertions)` + `FLOOR_ASSERTIONS` shape `check-testsuite-counts.sh` will then require.

**Left-shift gate.** A declared-population assertion over `tools/workflows/*.test.sh` in both directions: every tracked suite is claimed by a `[[gate_leg]]`, and every claim names a file that exists. That is the charter's "deploy your own tooling as a DECLARED population" rule applied to the one kit that already satisfies it for four of five files.

---

## M6 — MEDIUM — `tools/unattended/check-pass-order.sh:29` — a version constant nothing compares, under a comment saying it is paired

```sh
KIT_UNATTENDED_VERSION=1.14   # gov:kit unattended@1.14 — must match unattended.sh; check-kit-versions.sh pairs them
```

`tools/check-kit-versions.sh:149` iterates a hardcoded two-element list — `tools/unattended/unattended.sh tools/unattended/check-unattended.sh` — so the third script carrying the constant is outside the population. **Staged the break directly**: set this file to `KIT_UNATTENDED_VERSION=9.99` with a matching `gov:kit unattended@9.99` marker, ran `bash tools/check-kit-versions.sh` → exit 0, then restored. A repo-wide grep for `KIT_UNATTENDED_VERSION` confirms `check-kit-versions.sh` is the only comparator.

At the next kit bump this leg silently keeps the old version while the driver moves, and the file's own line 29 tells the next reader the pairing exists. The block above the loop even says "ENUMERATED, NOT NAMED... The population is DERIVED" — true of the `*.template.md` arm below it, not of this list.

**Fix.** Replace the literal at :149 with a derived population — `git ls-files 'tools/unattended/*.sh'` filtered to files declaring `^KIT_UNATTENDED_VERSION=` — so the next script carrying the constant is covered on arrival.

**Left-shift gate.** The derivation is the gate. Add a self-test arm that stages a mismatched marker in a **third** file and observes RED; the current suite only ever stages the break in the two named ones, which is the "gate the CLASS, not the instance" rule.

---

## M7 — MEDIUM — `tools/unattended/run-unattended-gates.sh:172` — the kit's DECLARED compensating runner never runs the new leg or its suite

`tools/unattended/kit.toml:73-77` names `bash tools/unattended/run-unattended-gates.sh [--all]` as **the** compensating check for the 2026-08-23 ruling that took this kit's self-tests off the merge bar — the exemption's entire justification. Its leg list is hardcoded at :170-178 (three `checks`, five `selftests`) and gained nothing from this diff. A repo-wide grep for `check-pass-order.test.sh` returns only that file's own header line and build records: no gate leg, no kit descriptor entry, no runner.

So 155 lines of arms — including the matched spec-first/build-first pair and the sliced-classifier DEAD PROBE arm, the only evidence the leg reds at all — are dead plumbing. `--checks` also skips the new leg itself, so the kit's own runner cannot reproduce a red from it. `kit.toml` now declares FOUR `gate_leg`s against the runner's three checks, so `--all` no longer mirrors the kit's own declared legs. The runner's "A MISSING BUDGET IS ITSELF A FAILURE" ratchet is escaped by simply not being listed. `check-arms.py`'s discovered population (ten shell gates) excludes `check-pass-order.sh` too, so nothing else grades its branches. Spec 3 §7's "witnessed by running it directly, verdict owed in the landing report" is a one-time manual act, not a route the declared compensating check will ever take again.

**Fix.** Add `run_one "pass-order history" checks bash "$HERE/check-pass-order.sh"` beside :172 and `run_one "pass-order selftest" selftests bash "$HERE/check-pass-order.test.sh"` beside :178.

**Left-shift gate.** Make the runner **derive** its `checks` list from `kit.toml`'s `[[gate_leg]]` argv entries rather than restating them, and assert in the kit gate that every `*.test.sh` in the kit dir has a `run_one` row. The fifth leg is then covered on arrival, and the exemption's compensating check stops drifting away from what it compensates for.

---

## M8 — MEDIUM — `tools/workflows/unattended-build.js:246` — one sentence hands the agent two vocabularies for the gating field

The AUDIT prompt spells `--verdict <CLEAN|CLEAN WITH FIXES|BLOCKED>` and then, in the same sentence, says "return the driver own verdict token verbatim" — binding "verdict token" to the set it just spelled. `AUDIT_SCHEMA.verdict` (:173) enums the **disjoint** set `CONVERGING | CONVERGED | NON-CONVERGENT | CEILING`, which is `review_state`'s output (`unattended.sh:3828`), printed as the tail of the driver's stdout line and never called a "verdict". `REVIEW_VERDICTS` (`unattended.sh:461`) is what `--verdict` takes.

An agent following the sentence literally returns `CLEAN` and fails the enum. Nothing in the prompt says to parse the state token out of the driver's stdout, so the only channel for the field is unnamed — on the one stage whose absence this file treats as fatal (:249-257). Worse than a schema bounce: the state is computed by the driver from a count-shrink predicate over PRIOR rounds, which the stage agent cannot derive, so an agent mapping its own `CLEAN` onto `CONVERGED` would defeat the one gate this file exists to hold.

**Fix.** Name the channel and the set explicitly: "read the CONVERGENCE STATE token the driver prints at the end of that line — one of CONVERGING, CONVERGED, NON-CONVERGENT, CEILING — and return it as `verdict`; the CLEAN/CLEAN WITH FIXES/BLOCKED value you passed to `--verdict` is an input, not the return."

**Left-shift gate.** An arm that returns `"CLEAN"` and asserts the harness refuses rather than gating on it. Generally: a cheap parity leg comparing every `*_SCHEMA` enum against the literal alternation sets spelled in the same file's prompts, so a prompt naming a vocabulary its schema rejects reds.

---

## M9 — MEDIUM — `.claude/skills/unattended/SKILL.md:93` — `passes-harnessed` points at M6, which states no such rule

```
| `passes-harnessed` | the pass sequence a build runs, driven as one program | M6 | all | D13 |
```

The table's preamble (:73-76) says "Each NAMES a rule and points at the section that states it; none of them restates one", and step 0 says every directive "is a POINTER into a section of that file", meaning `BUILD-METHOD.md`. I read M6 whole: it covers what a PASS is, the commit boundary, parking, and the disjointness rule. Grep for `harness`, `driven`, `one program`, or a stage order across `BUILD-METHOD.md` returns only M4's `tier2-review` lines and two M8 review lines. **M6 was not touched by this diff.**

The rule the handle names is stated only in `UNATTENDED-PROTOCOL.md` §12 — a different document the directive table does not point at. The sibling `discoveries-adopted -> M10` resolves because M10 does name ADOPT. `check-unattended.sh:1492` only asserts the cited section EXISTS, so the mispointer is green: an agent that resolves the handle reads M6 and finds no rule, and a waiver recorded against the handle relaxes something no reader can locate. `unattended.sh:463`'s `DIRECTIVES_CORE` carries the same `passes-harnessed:M6`.

**Aggravating, and worth its own sentence.** The row's Scope is `all`, which the preamble defines as "binds every unattended run" — while §12 says "Recipe mode does not take it: its pieces are not specs." The scope grammar admits `prompt` and `recipe` but has no token for "all but recipe", so `all` is the closest available and §12 is the qualifier that narrows it. That is tolerable **only** while the pointer resolves to the section carrying the carve-out. It points at M6, which carries neither the rule nor the carve-out, so a recipe run reading its bound directives has no reachable statement that this one does not bind it.

**Fix.** Add the harness rule to `## M6` in `tools/memory-tree/BUILD-METHOD.template.md` and re-render `memory/guides/BUILD-METHOD.md` — **both halves of the byte-compared pair** — with one sentence pointing at `tools/workflows/unattended-build.js`, its two limits, and its mode scoping. Or point `passes-harnessed` at whichever M-section is made to carry it. Do not leave the rule reachable only from the protocol while the table claims otherwise.

**Left-shift gate.** Strengthen `check-unattended.sh`'s arm B from "the cited section exists" to "the cited section names this handle's subject" — cheapest honest form: require each directive handle's own token, or a declared keyword list per handle, to appear in the cited section. A pointer resolving to a section that says nothing is the shape the current check cannot see.

---

## M10 — MEDIUM — `tools/unattended/unattended.sh:4509` — two readers of the `order` verb, and the disagreement is a silent skip

The comment at :4505-4506 claims this and `gen_build_index.py` "cannot disagree about what step a unit is on". Probed both readers on the same headers:

| header | dispatch sed (:4509) | `gen_build_index` |
|---|---|---|
| `· order 3` | 3 | 3 |
| `·  order 3` (two spaces) | **EMPTY** | 3 |
| `·order 3` | **EMPTY** | 3 |
| `· order 2x` | **2** | `_parse_order` RAISES |
| `order 1 · order 5` | **5** (greedy `.*`) | RAISES, duplicate verb |

Four divergences, all reproduced. The two EMPTY cases are the live hazard: the generator renders the unit at step 3 while the driver treats it as unordered, and by its own rule an unordered unit "blocks nothing" — so the order gate **silently stops applying** with nothing red. `check-memory-hygiene.sh`'s check-12 header regex anchors only through `base <sha8>` with no end anchor, so the tail spacing that triggers it is ungated. The two RAISE cases are bounded, since the renderer refuses those headers so such a spec cannot land — but `--dispatch` enforces or waives a step number from a value the owning reader rejects, and `gen_build_index.py:2278-2291` pins both as refusals it was hardened against. Same defect on the sibling read at :4514.

Measured over all 401 tracked specs: **zero live divergences today.** Latent, not firing — and the failure mode is a silent skip, which is the class this repo gates against.

**Fix.** Take the order from the generated build-order region the units roster already renders, so there is one derivation instead of two. Failing that, mirror `ORDER_RE` exactly: allow `·[[:space:]]*order[[:space:]]+`, require the digits be followed by `·` or end of header, and refuse rather than `head -1` on a duplicate verb.

**Left-shift gate.** An arm with a two-space `·  order 2` header asserting the earlier unit still blocks. The class-level version: a leg that feeds a fixed table of adversarial Status headers through both readers and asserts they agree or both refuse. That is the "two readers of one config, one re-derived" gate, and this is the second place in this diff it would have paid.

---

## L1 — LOW — `.claude/skills/unattended/SKILL.md:503` — `--propose` prose now renders as `--brief` prose, in both halves of the pair

`git show b9fb4fb0` shows the eight-line `--brief` bullet inserted directly between the `--propose` code fence and its trailing two-space-indented paragraph:

> Nothing blocks on a proposal and `--status` counts them apart from the questions, so recording one costs the run nothing. The same amendment against two steps is two rows, because it is two edits.

Markdown attaches an indented paragraph to the enclosing list item, which is now `--brief`. That text is unambiguously `--propose` semantics — proposals, amendments, steps — and `--step` is a `--propose` argument `--brief` does not have. The second sentence is **false of `--brief`**: `verb_brief`'s identity is the exact line `brief · item <unit> · reason <hash> <path>` (`unattended.sh:4108-4113`), keyed on unit + hash + path with no notion of a step, so an unchanged re-brief prints `already recorded, unchanged` and a re-brief of an edited file is a new row. Meanwhile `--propose` is left with a bare fence and no statement of its own non-blocking or idempotence property.

Present byte-identically at `tools/unattended/SKILL.template.md:503-504`, so the render-pair byte compare is **green over a claim wrong in both halves** — misattributed instruction in an agent-facing Skill that no parity gate can see.

**Fix.** Move the `--brief` bullet below the trailing paragraph in `tools/unattended/SKILL.template.md`, re-render `.claude/skills/unattended/SKILL.md`, and give `--brief` its own closing sentence: it is a `history` kind, nothing blocks on it, an unchanged re-brief is a no-op, and `--status` grades the latest row as the live claim.

**Left-shift gate.** Structural, not prose: a check that every verb bullet in the Skill's verb list is followed by its own fence and that no continuation paragraph is separated from its bullet by another bullet's fence. Cheapest honest version — assert each verb bullet's block mentions only that verb's flags, so a `--step` sentence under `--brief` reds. A byte-compared render pair cannot catch a defect present in both halves, which is the general lesson here.

---

## L2 — LOW — `memory/guides/UNATTENDED-PROTOCOL.md:1` — the render lands at exactly the cap, zero headroom

`wc -c` reports **61440** for both `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`. `check-memory-hygiene.sh:63` sets `GUIDE_CAP_BYTES=61440` and the guides branch at :493 selects it; the comparison at :505 is `b[f]+0 > cb`, strictly greater, so it passes with **exactly zero bytes of headroom**. Line count 725 against `GUIDE_CAP_LINES=750` is not the binding constraint. Any single byte added to this BINDING contract — a typo fix, a clarification, the next verb — reds the merge bar with no repair short of another compression pass.

**The owner-facing record understates it, and that is the actual defect.** The parked decision at `RUN.md:48` tells the owner the file was 61353 with 87 bytes of headroom and that "the NEXT verb has 55 bytes to work with". After unit 5 added §12 that number is **0**. The record written specifically to hand the owner this structural question no longer describes the state it exists to surface.

**Fix.** Either land a deliberate margin (trim ~500 bytes so the next edit does not red the bar), or take the parked structural question to the owner now rather than at the next verb — and correct the headroom figure in the parked decision to what the tree shows.

**Left-shift gate.** A soft ceiling beneath the hard one: red at ~98% of `GUIDE_CAP_BYTES` with a distinct "approaching the cap" message. A gate whose only signal fires after the file is already unlandable gives no warning, and a governance carrier sitting at exactly its cap is a wedge waiting for the next commit.

---

## L3 — LOW — `tools/unattended/kit.toml:67` — "THE THREE LEGS BELOW STAY" now precedes four

The exemption block records the 2026-08-23 ruling by counting the legs it keeps and enumerating three subjects (run-state records, playbooks, skill wiring). `grep -n '\[\[gate_leg\]\]'` returns **four** blocks below it — at :83, :93, :100 and :107 — because this diff added `pass-order history`, whose subject matches none of the three. `git show ead1b820^:tools/unattended/kit.toml` confirms three before this build. The sentence is present-tense about the legs below, not a dated historical note, so an auditor checking whether the exemption still holds is told three and is wrong in the direction that hides a leg.

This is the charter's "NO count of a derived population is written in prose" rule, broken by the commit that grew the population.

**Fix.** Reword :67 to "THE LEGS BELOW STAY, and the difference is their subject" — dropping the number, exactly as the protocol's parked-entry passage dropped "of eight kinds" in this very diff.

**Left-shift gate.** A leg that greps the kit descriptors for an English cardinal (`TWO|THREE|FOUR|FIVE`) immediately preceding an enumerable block and reds when the count disagrees. Narrower and cheaper: assert the exemption paragraph contains no cardinal at all.

---

## Bug-class checklist — coverage over this range

The brief's fourteen classes, hunted individually. Where a class fired, the finding is named; where it did not, what was checked is named, because a class reported clean without saying what it looked at is the `fixture-passes-by-finding-nothing` shape one level up.

| Class | Result |
|---|---|
| `fixture-passes-by-finding-nothing` | **FIRED** — M4 (one-unit fixture cannot fail on the collapsed reader), M3 (order gate skipped in every arm, never passed) |
| `heredoc-escape-reaches-the-regex` | clean — checked the new awk programs in `check-pass-order.sh` and `verb_brief`; no heredoc-authored pattern in the diff. The class is what M4's arm was *written* for, which is why M4 matters |
| `staged-break-substitutes-a-synthetic-value` | clean on the arms that exist; I staged real breaks for B1, B2 and M6, and each reproduced against the real script rather than a stand-in |
| `two-answers-to-one-question` | **FIRED** — M10 (two `order` readers), M8 (two vocabularies, one field), M2 (two `load_spec_facts` call sites, two treatments of one refusal) |
| `amendment-leaves-its-other-half-standing` | **FIRED** — L3 (leg added, the count above it not), M7 (leg added, the compensating runner not), M5 (suite added, its declarations not), M9 (rule added to the protocol, not to the section the handle points at) |
| `bounded-through-a-pipe-is-unbounded` | clean — `unattended-build.js` spawns one agent per stage sequentially and fans out nothing; the AUDIT stage delegates to `tier2-review.js`, whose bound is unchanged by this diff |
| `containment-tested-one-way` | **FIRED** — B2 is exactly this: the build-commit filter was tested for "code commit selected" and never for "spec commit rejected" |
| `degradation-known-but-unreported` | **FIRED** — H2's reporting half computes the blocker count and reports `complete`; M1's cutoff skip counts an evasion and a grandfathering identically |
| `fixture-inherits-ambient-machine-state` | clean — `check-pass-order.test.sh` builds its own scratch repos and no arm reads the host tree. B1 is the inverse and worse: the *leg* inherits ambient tree state |
| `fold-text-is-unreviewed-surface` | see the compression audit below |
| `id-matched-as-a-substring` | clean, and handled well — `check-pass-order.sh:141` matches the id as a whole token via `tr -c`, and the dispatched-sibling grep anchors on ` · reason `. Both cite the class by name |
| `second-implementation-is-not-a-second-opinion` | clean by construction — the `plan_state` slice is a slice, not a re-implementation. See the slice audit below |
| `two-guards-one-question-two-answers` | **FIRED** — M10 (dispatch sed vs `ORDER_RE`), and M1 in the weaker form: two cutoff idioms, one git-anchored and one not, under one comment claiming they are the same |
| `two-readers-of-one-config-one-re-derived` | **FIRED, three times** — B3 (authored `ids:` front matter vs the generated units region: one reader reds, the other never sees it), B1 and M1 (the leg reading conf and README values the graded run authors), M6 (the version constant with three writers and one comparator) |

### The `plan_state` slice — verified, and it holds

The brief asked specifically whether the second reader can silently truncate. It cannot, and the design is right:

- the end line is **derived** from the first `^}` after `^plan_state()`, never a magic span (`:70-71`);
- a failed slice exits 2 with a message, and `declare -F plan_state` is asserted after the `eval` (`:73-76`), so a truncated body — which would not parse — cannot leave the leg grading nothing;
- the DEAD PROBE arm (`:83-88`) requires the sliced classifier to return one of `MISSING|THIN|FORKED|READY` on a real tracked spec before any verdict is trusted.

Confirmed against the live driver: `plan_state` spans lines 1650-1733, and the only column-0 `}` inside that span is the closing brace — every `}` in its embedded awk program is indented. If a future edit puts one at column 0, the slice truncates, the `eval` fails to define the function, and the `declare -F` guard catches it. **Not a finding.** It is the best-built thing in this diff, which is what makes B1 and B2 in the same file worth reading twice.

### The protocol compression — fourteen passages, no dropped or reversed claim

`memory/guides/UNATTENDED-PROTOCOL.md` and its template each changed 321 lines (158 removed, 165 added). I read the compression diff in full against the pre-image. **No claim was dropped or reversed.** Three passages deserve naming because they are where a reversal would have hidden:

- **§1 property 2**, the second-anchor weakening. "§9 still applies" was cut from the `SECOND_ANCHOR_MODES` sentence — but the immediately preceding sentence retains "neither is a verdict and §9 applies to both", so the claim survives in the adjacent clause rather than being lost. Tight, but correct.
- **§5 fact 3**, the parked kinds. "of eight kinds" was **removed** rather than bumped to nine, and `BRIEF` plus `--brief` were added to both the kind list and the writer list. That is the derived-count rule applied correctly by the commit that grew the population — and it is the direct counter-example to L3, which is the same situation handled the other way in the same build.
- **§7 `records-current` and `specs-audited`**, the two longest DoD cells. Both compressed heavily; every operative term survives — the exit-status reading, the whole-token id join, the `N..M` range expansion, the LOWER-bound disclaimer. The `reuse-probed` cell's five outcomes and its "cannot be a merge-bar leg" reasoning are intact.

The one cost of the compression is L2: the render now sits at exactly its cap.

## What this build got right, for the record

Three things, because a review that lists only defects mis-prices the diff. The `plan_state` slice is the correct answer to a second-reader problem and is guarded three ways. The `id-matched-as-a-substring` class is handled at both new join sites, each citing the gotcha by name. And the protocol compression preserved a binding contract across fourteen passages without a single reversal, which is not the usual outcome of a fold at that scale.

## Left-shift summary — the gates this review is asking for

Ranked by what they would have caught here:

0. **Run the merge bar before filing the review.** Not a gate — a procedure, and it belongs at the top because it is free and it is what found B3. The bar is red on this tree today and twenty-five findings were filed without anyone noticing.
1. **A conf-sourcing ban across `tools/**/check-*.sh`** — catches B1, and the two prior incidents that hardened its siblings one file at a time.
2. **A spec-commit arm in `check-pass-order.test.sh`** — catches B2, and is the failing case the charter required before the leg landed.
3. **A declared-population assertion over `tools/workflows/*.test.sh`** — catches M5, and covers the next suite on arrival.
4. **A derived population in `check-kit-versions.sh:149`** — catches M6, and the next script to carry the constant.
5. **`run-unattended-gates.sh` deriving its checks from `kit.toml`** — catches M7, and stops the declared compensating check drifting from what it compensates for.
6. **An adversarial Status-header table run through both `order` readers** — catches M10, and any future third reader.
7. **`check-unattended.sh` arm B asserting the cited section names the handle's subject** — catches M9.
8. **A soft ceiling under `GUIDE_CAP_BYTES`** — catches L2 before the file is unlandable rather than after.
9. **Negative-test ids minted outside the live slug's family** — catches B3, and stops an acceptance criterion from depending on a value the same build can invalidate.

The pattern across B1, B2, M5, M6, M7 and L3 is one thing said six ways: **this build knows how to write a carrier for a conf key and still does not know how to write one for a gate leg.** Round 3's spec audit said exactly that about the specs. It shipped anyway. The declarations a new leg owes — the kit descriptor, the manifest row, the version-pairing population, the compensating runner, the subject pin, its own hostile-input arms — are a checklist nobody holds, and the cheapest fix in this whole report is to write that checklist down as one gate rather than as six.
