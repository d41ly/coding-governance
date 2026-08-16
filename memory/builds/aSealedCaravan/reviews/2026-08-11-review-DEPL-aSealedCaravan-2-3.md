**Serves:** spec-audit DEPL-aSealedCaravan-2

## Verdict: BLOCKED

**Target:** `memory/builds/aSealedCaravan/spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md`
(`DEPL-aSealedCaravan-2`), rev-6, base `16aeb5ef`, before any code. This is the re-audit of the
rev-6 fold of review 2, which returned BLOCKED with seven blockers.

**Scope: this pass was scoped to the fold.** It audited what rev-6 CHANGED — the new and rewritten
material in section 4's data model and section 6's criteria — against three questions: are review
2's blockers actually closed, is the new model internally coherent, and is it still true of the
tree. It did not re-litigate the goal, the four-commit rollout, fork F1's location argument, the
two-phase `apply`, the probe-based outcome model, the three-valued baseline, or the bash-from-Python
remedy. Those held under review 2 and were not re-attacked.

**Shape:** raw 36, confirmed 9, refuted 27, unverified 0. Precision 0.25 — HALF review 2's 0.50 and
well under the floor `memory/guides/REVIEW-PROTOCOL.md` sets. Three lenses (blockers-actually-closed,
new-model-coherence, still-true-of-the-tree), five verifier batches over five agents total, inside
the protocol's at-most-5-total and at-most-5-concurrent budget. Every confirmed finding survived an
adversarial skeptic whose default was refutation, and each verdict had to reproduce against the spec
text or the running tree. There are no unverified carry-overs; nothing is outstanding for lack of a
verdict.

**Severity split:** 2 blockers, 4 high, 3 medium, 0 low.

**Measurements re-run at review time, at the current tip:**

- `git add` executes in exactly ONE of the six non-test `tools/*/adopt-*.sh`: `adopt-memory-tree.sh`
  at lines 135 and 172. The other two `git add` strings in adopters are operator instructions that
  never execute — `adopt-codebase-map.sh:215` inside an `echo`, `adopt-unattended.sh:154` inside a
  next-steps heredoc. No `git stage` and no `git update-index` anywhere in the six.
- `tools/gate-legs.json`: `.githooks/` guards THREE legs (branch-guard self-test, pre-push self-test,
  push-main self-test), `skills/session-kickoff/` guards ONE (manifest-check self-test), `.claude/`
  guards ONE (check-wiring self-test).
- `agent-cap.js` is tracked TWICE: `tools/hooks/agent-cap.js` (kit copy) and `.claude/hooks/agent-cap.js`
  (wired copy). `tools/hooks/agent-cap.test.sh` fails outright when the wired copy is absent.
- `adopt-memory-tree.sh:39-43` copies `.memory-tree.conf.example` to `.memory-tree.conf` at the repo
  root and exits 1 — the spec's own seed-and-stop outcome.
- `DEAD_PATH_PIN`, `ORPHAN_ID_PIN` and `READ_PATH_CEILING` are real keys, read at
  `tools/memory-tree/corpus_ids.py:74,90`.

---

## How to read this report

Ids are the raw ids from the verification pass, so they are sparse. Nine confirmed findings collapse
to **six distinct edits**; the three overlap clusters are named below and are one edit each. Every
finding names the section the correction lands in, the concrete fix, and a left-shift where one
exists.

| Cluster | Ids | One edit |
|---|---|---|
| The conf-example rule's role contradicts itself | 17, 11 | Give the role table a copied-on-first-apply column, retag the rule `seed`, say which side seeds |
| "three of the six stage their own writes" is false | 29, 14 | Restate as one of six (memory-tree), and DERIVE `mutates_index` instead of spelling it |
| The guard class table has no class for a verbatim repo-root path | 19, 32 | Add a fourth, identity-rendered class holding the hooks dir and the Claude Code dir |

**The through-line.** Rev-6 did the hard part: the population claims are gone, `[[hole]]` got a
runnable probe, `[[files]]` got destinations, and nine new criteria cover arms that had none. Every
one of review 2's seven blockers is addressed in substance. What survives is a narrower and later
class — rev-6's OWN new fields, argued into existence one at a time, were never audited against each
other. The role enum grew `seed` and nothing retagged the rule that needed it. `to` gained a
destination and the one entry needing TWO destinations still has no spelling. `red_after_land` was
added to make AC1 truthful and both of its consumers then exempt the leg permanently. The guard
class table was written from gov's layout without checking it against the destinations the same
section had just enumerated. Three of the six edits below are one-line consistency repairs between
two paragraphs rev-6 wrote in the same pass; two of those are blockers only because they land inside
rollout commit 1's own deliverable, where a builder has to guess rather than read.

The second, smaller through-line: one measured sentence in section 3 never reproduced. It is the
same false-measurement class rev-6 was folded to eliminate, surviving in a prose claim rather than in
a population count, so the anti-count rule does not shield it.

---

## Blockers (2)

### id=16 — `[[files]]` cannot express the one entry that needs two destinations

**Lands on:** section 4 Data model (`[[files]]` precedence and `to`) · section 6 AC10, AC11

Section 4 states the requirement twice. The registry prose: "one entry has TWO destinations for ONE
source file, because the agent-cap parity arm requires both the kit copy and the wired copy and fails
outright if the wired copy is absent." The `to` subsection restates it: the agent-cap hook "lands at a
Claude Code path outside any kit prefix AND a second time inside one." But `to` is a single string on
every rule shown, and the stated precedence — "later rules win, so exclusions are expressible" —
resolves two rules matching `agent-cap.js` to exactly one. No other spelling is defined anywhere: no
list-valued `to`, no second destination key, no second entry.

Verified in tree: `tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` are both tracked, and
`tools/hooks/agent-cap.test.sh` around lines 459-467 fails outright — "the wired copy
`.claude/hooks/agent-cap.js` is MISSING (parity must not be satisfiable by absence)" — when only one
exists. So under the model as written, exactly one destination survives and the parity arm reds in
every target that takes the kit.

This is the same class rev-6 fixed for the renamed and flat cases ("four registry entries could not be
written at all"), left unfixed for the dual-destination case. It bites in rollout commit 1, which is
"a `kit.toml` for every entry": the agent-cap descriptor cannot be written at all, and `plan` plus
AC11 promise a file set `apply` cannot produce.

**Fix:** make `to` accept a list, so one rule can name both the kit-relative default and the Claude
Code path — or state that precedence MERGES destinations rather than replacing rules. Whichever is
chosen, add to AC10 that a rule set producing two writes of one source is legal, while two rules
writing the SAME destination is a `selfcheck` refusal.

**Left-shift:** `selfcheck` should assert the destination SET per source file rather than a single
resolved destination, so the next entry needing a second home reds in commit 1 instead of surfacing
as a red parity arm in somebody else's repo.

### id=17 (with id=11) — `seed` and `project-owned` are the same role, and the example uses the wrong one

**Lands on:** section 4 Data model (the role table, the `kit.toml` example's last `[[files]]` rule)
· section 6 AC11

The role table's two operative columns are byte-identical strings for `project-owned` and `seed` —
"sha256 at install, then never compared" and "never rewritten". They differ only in the prose reason
column. So no column and no field answers the one question that actually separates them: is this file
copied out of gov on first apply? That is exactly the state `seed` was added at rev-6 to name, per its
own justification (the version gate, "copied verbatim reds immediately").

The example descriptor then compounds it. Its last `[[files]]` rule assigns `role = "project-owned"` —
annotated three rules above as "never copied FROM gov, never overwritten in the target" — to
`.memory-tree.conf.example` with `to = ".memory-tree.conf"`, a rule whose entire content is a
copy-from-gov-with-rename. Landing and never-copying-from-gov cannot both hold.

Measured: `tools/memory-tree/adopt-memory-tree.sh:39-42` runs under `set -eu` and copies
`.memory-tree.conf.example` from the INSTALLED kit dir to the repo root as `.memory-tree.conf`, then
exits 1. Under the stated precedence, the rule as written pulls the example out of the kit-relative
engine copy while its role forbids the copy to root, so a default-set install ends with neither the
kit-relative example nor the root conf — and the adopter then fails on a missing source.

`plan` (AC11: "lists every file it would write") cannot decide whether this rule produces a write, and
`apply` has two legal readings. The rule sits in the DEFAULT kit set, so rollout commit 1 cannot be
written without guessing, and the guess decides whether a default-set install yields a usable conf.

**Fix:** give the role table a "copied on first apply" column — true for `seed`, `engine` and
`rendered`, false for `project-owned` and `generated` — and retag the conf-example rule as
`role = "seed"`. If the two roles still coincide on every column after that, delete one.

**Left-shift:** `selfcheck` should refuse two roles whose operative columns are identical. A role enum
that grows a member indistinguishable from an existing one is the "two spellings of one fact with
nothing asserting they agree" class this unit exists to attack, appearing inside the unit's own model.

---

## High (4)

### id=11 — the same rule collides with its own descriptor's outcome map

**One edit with id=17 above; kept distinct because it names a second downstream break.**

**Lands on:** section 4 `kit.toml` example (the fifth `[[files]]` rule against the first `[[outcome]]`)

Read the id=17 rule the other way — govkit LANDS the conf during the land phase — and the collision
moves into the same descriptor's outcome map. `adopt-memory-tree.sh:39-41` seeds the conf and exits 1
telling the operator to edit it; that IS the `seed-and-stop` outcome the same `kit.toml`'s first
`[[outcome]]` probes for, with `must_exist = ".memory-tree.conf"` and the hygiene render absent. If
govkit has already landed the conf, that branch is unreachable, `--scaffold` proceeds against the
example's unedited `DISCIPLINES` and `FAMILIES` values — which the example itself marks "REPLACE the
example below" — and the install is the inherited-vacuous shape section 4 warns about. If govkit does
NOT land it, `to` is dead prose and section 4's "two conf examples land at the repo root renamed" is
false.

**Fix:** state which side seeds, in the `[adopt]` and `[[outcome]]` prose as well as in the rule, so
the two halves of one descriptor cannot disagree. Either govkit lands the seed and the descriptor
drops the `seed-and-stop` outcome, or the ADOPTER seeds it and the rule carries no destination at all.

### id=19 (with id=32) — the guard class table has no class for a verbatim repo-root path, and its stated reason is false for two of its own members

**Lands on:** section 4 "Guards, and why a deployed one is green by absence" (the three-class table)
· section 2 S12 · section 4 `to` · section 6 AC24

The table's third class is "gov-layout only — DROPPED, the path cannot exist in a target", and its
named members are the hooks directory, the kickoff engine's own tree, and `tools/lib/`. The SAME rev
deploys two of those three. Section 4's `to` subsection lists "the pre-push hook lands at a verbatim
repo-root path with no prefix" and "the agent-cap hook lands at a Claude Code path outside any kit
prefix" among the destinations the kit-relative default cannot express. S12 makes every path under the
hooks directory part of the asserted deployable surface. And the ratchet in S12's own population lands
flat and renamed under the install prefix.

The shipped runbook agrees with `to`, not with the table: `WIRE-INTO-PROJECT.md:435` copies the
pre-push hook in, `:441` installs agent-cap under the project's Claude Code hooks dir, and `:353`
lands the ratchet at a flat path under the install prefix.

Measured: three legs guard on the hooks directory, one on the kickoff engine's tree, one on the Claude
Code dir. "The hooks directory" is itself ambiguous between the git hooks dir and the deployable kit
dir `tools/hooks/`.

So the taxonomy has no class for a verbatim, unprefixed repo-root path, and none for a source path
deployed under a RENAME. The renderer has two options for the hooks dir and the Claude Code dir, and
both are wrong: kit-relative would prefix them into a path that cannot exist — the silent-skip failure
this subsection reproduced in the real runner — or dropped. AC24 ("no emitted guard names a path that
cannot exist there") is then graded against a taxonomy whose reason clause is false for its own
deployed members.

**Fix:** add a fourth class, "verbatim repo-root — emitted unchanged under the identity substitution",
holding the git hooks dir and the Claude Code dir. Move the kickoff engine's tree into kit-relative
with the ratchet's own destination as its rendering target, noting it travels flat and renamed. Restate
the DROPPED row to name only `tools/lib/` and the gate-runner pair, whose exemption section 3 actually
establishes, and disambiguate "the hooks directory" from the deployable `tools/hooks/` kit.

**Left-shift:** `selfcheck` should assert that every guard pathspec in gov's manifest falls into
exactly one declared class. A class table that does not partition its own input is how the emitter
gets a rule for the majority and no rule for the rest.

### id=20 — `red_after_land` is a temporal flag that both its consumers read as a permanent exemption

**Lands on:** section 6 AC1 · section 4 `red_after_land` and the three-valued baseline table

Section 4 defines it temporally: "true = this leg is red between land and configure, by design",
measured on the unattended kit as "red after land and green after adopt". Both consumers then exempt
the leg with no window and no expiry. AC1 excludes any leg carrying the flag from its exit-0 assertion
after a fixture that runs BOTH phases. The baseline table's `absent` row exempts it from failing the
install outright.

Nothing else picks the leg up. The `blocks_gate` exemption lifts on discharge ("no UNDISCHARGED
`blocks_gate` hole"); this one never does. AC5 covers only the `blocks_adopt` kit. AC17 asserts
execution, not verdict. So after land, configure and hole discharge, NO criterion asserts a
`red_after_land` leg green.

Section 4's measured instance is the unattended kit's two unguarded legs, and unattended is in the
`--all` set. A default `--all` install can therefore land that kit with both legs red forever and every
criterion pass — the deployed-leg-vacuously-green class section 7 names, reintroduced by the flag added
to prevent it.

**Fix:** split the window from the exemption. AC1 asserts a `red_after_land` leg exits 0 AFTER
configure, excluding it only from a land-phase check. The baseline `absent` row exempts it only for a
leg whose kit's configure phase was skipped by a `blocks_adopt` hole. If nothing actually checks
between land and configure, delete `red_after_land` and let `blocks_gate` carry the one remaining
exemption. The repair is a SCOPED assertion, not a loosening.

**Left-shift:** `selfcheck` should refuse a descriptor flag that no criterion in section 6 asserts
POSITIVELY — an exemption flag with only negative consumers is by construction unobservable.

### id=29 (with id=14) — section 3's measured staging claim never reproduced

**Lands on:** section 3 "Landing the install" (the sentence dated 2026-08-11) · section 4
`[adopt] mutates_index` · section 6 AC2

"three of the six stage their own writes" is false of the tree. Counting executed `git add` over the
six non-test `tools/*/adopt-*.sh`, only `adopt-memory-tree.sh` matches, twice, at lines 135 and 172.
The other five return zero. The two other `git add` strings in adopters never execute:
`adopt-codebase-map.sh:215` is inside an `echo` and `adopt-unattended.sh:154` is inside the closing
next-steps heredoc. Checked for other staging verbs across all six — none. So exactly ONE of six
stages: the denominator is right and the numerator is overstated threefold.

The claim was already false at `4838d3c`, so it is a measurement that never reproduced rather than
merge drift, and it carries an explicit measurement date in a spec whose whole discipline is that
measured claims are true.

**Fix:** restate as "one of the six (memory-tree) stages its own writes, twice". Then make the fact
DERIVED rather than spelled: add to AC10 that `selfcheck` asserts each descriptor's `mutates_index`
against a grep of that adopter for an executed `git add`, so it is never written in prose again.

**Left-shift:** this is rev-6's own anti-count rule one step short of its conclusion. The rule
currently covers population COUNTS; extend it to every measured claim about the tree — a number in
prose here is a defect in this document, whether or not it counts a population.

---

## Medium (3)

### id=14 — the same sentence is the stated ground for AC2's predicate and for per-kit descriptor data

**One edit with id=29 above; kept distinct because it names what the false number changes downstream.**

**Lands on:** section 4 `[adopt] mutates_index` · section 6 AC2 rationale

`mutates_index` is a per-kit boolean, and this sentence is the natural source a builder reads when
setting it across rollout commit 1's descriptors. Set true on three kits, it is wrong on two, and
`plan`'s promised file set then mis-predicts index effects for codebase-map and unattended. AC2's
rationale — "the adopters stage their own writes and a porcelain-empty tree would be satisfied by an
install that did nothing" — is overstated threefold.

The mitigation, and why this sits at medium rather than high: AC2's PREDICATE survives untouched. S5
has `apply` stage everything it writes, so a porcelain-empty tree is satisfied by a do-nothing install
regardless of what the adopters do. The example descriptor also sets `mutates_index = true` only on
memory-tree, the one kit it is true of. This is a factual and rationale defect that changes descriptor
data, not a criterion defect.

**Fix:** restate AC2's rationale as "at least one adopter stages its own writes, and S5 stages
everything else, so a porcelain-empty tree is satisfied by an install that did nothing" — a ground
that does not depend on the count.

### id=25 — `requires_if`'s condition keys are declared nowhere and gated by nothing

**Lands on:** section 4 `requires_if` and `when_any_key_set` · section 6 AC10

Review 2's id=18 asked for four things: real keys, a `[config]` declaration or a `conditional_keys`
list, a resolution namespace, and a re-evaluation rule. Rev-6 landed two. The keys are real —
`DEAD_PATH_PIN`, `ORPHAN_ID_PIN` and `READ_PATH_CEILING` are confirmed at `corpus_ids.py:74,90` — and
`apply --resume` re-evaluates the edge after a discharge. The `[config]` slot and the namespace did
not land.

The keys appear in none of `[config]`'s three key lists, so `intake` has nothing telling it these keys
exist and `deploy.toml` carries no answer slot for them. More decisively: AC10's enumerated assertion
list — descriptor existence, declared files, gate legs, `version_from` patterns, the version
cross-check, hole discharge tokens, neither-flag holes, the `--all` derivation, the S12 surface — has
no arm resolving a `requires_if` condition key. So a condition can name a key that never existed and
`selfcheck` stays green, which is the exact state rev-6 folded this section to fix: its own prose
diagnoses the rev-2 defect as leaving "`selfcheck` no key to resolve", and then gates nothing.

The intake half is the weaker half — the pins ship blank by design and are a declared hole, so they are
not an answer `intake` should be asking for. The AC10 gap alone changes what `selfcheck` is built to
assert.

**Fix:** add `conditional_keys` naming the three pins to the example `[config]` block, and add to AC10:
every `requires_if` condition key resolves in the named kit's `[config]` key lists, and the named kit
is a registry entry.

**Left-shift:** the general rule is that every field section 4 argues into existence needs a named arm
in AC10 before the fold is complete. Two of this pass's six edits are fields that gained prose and no
assertion; a fold checklist mapping each new field to its gating criterion would have caught both.

### id=32 — the DROPPED guard class is factually wrong about the hooks directory

**One edit with id=19 above; kept distinct because it measured the same contradiction from the
still-true-of-the-tree lens rather than the coherence lens.**

**Lands on:** section 4 guard class table · section 4 `to` · section 2 S12 · section 6 AC24

Same contradiction, verified from the tree side. If the pre-push hook deploys verbatim, the git hooks
directory demonstrably CAN exist in a target, so the class's stated reason for dropping is false for
that member. `WIRE-INTO-PROJECT.md:435` prescribes copying the lander, its self-test and the pre-push
hook, and `:402-408` prescribes copying the pre-commit branch-guard block into the project's own
pre-commit. Three legs carry that guard today.

Why medium rather than high on its own: dropping is FAIL-SAFE. AC24's unguarded fallback means the cost
is three legs running unnecessarily on every target commit, not a wrong verdict. But a builder
implements the classification FROM this table and would implement it wrongly for a whole class, and the
table supplies no rule at all for the class that renders as identity.

**Fix:** covered by id=19's fourth class. Note additionally that the kickoff engine's tree needs its own
treatment: the manifest ratchet DOES travel, but flat and renamed, so its guard cannot render under
either the identity or the kit-relative substitution.

---

## What must be folded, and what is advisory

**The verdict is BLOCKED. Two confirmed blockers stand, and both land inside rollout commit 1's own
deliverable** — `registry.toml` plus a `kit.toml` for every entry plus `selfcheck` — so a builder
starting today meets them in the first commit and has to invent a design answer mid-commit rather than
read one. The spec is NOT buildable as it stands. It is close: six edits, three of them one-line
consistency repairs between paragraphs rev-6 wrote in the same pass.

**Must be folded before the first line of code:**

- **id=16** — `to` must be able to carry two destinations for one source, or the agent-cap descriptor
  cannot be written at all and the parity arm reds in every target. Rollout commit 1.
- **id=17 / id=11** — the role table needs a copied-on-first-apply column and the conf-example rule
  needs retagging to `seed`, or `plan` cannot decide whether a default-set rule produces a write and
  `apply` has two legal readings of a DEFAULT kit. Rollout commit 1.
- **id=19 / id=32** — the guard class table needs a fourth, identity-rendered class, or the emitter has
  no rule for the git hooks dir or the Claude Code dir and AC24 is graded against a false taxonomy.
  This is high rather than blocker only because the wrong answer fails safe; fold it in the same pass,
  because the classification is implemented from this table.
- **id=20** — `red_after_land` must assert green AFTER configure, or an `--all` install lands the
  unattended kit with two legs red forever and every criterion passes. Fold before AC1 is implemented.
- **id=29 / id=14** — correct the staging measurement to one of six and DERIVE `mutates_index` in AC10.
  It is a two-word prose fix plus one AC10 clause, and it is the input a builder reads when setting a
  per-kit boolean across commit 1's descriptors.

**Advisory — real, but they do not gate the build start:**

- **id=25** — the `conditional_keys` declaration and AC10's `requires_if` resolution arm. The condition
  itself is correct and the re-evaluation rule landed; what is missing is the gate that stops it going
  stale. It changes what `selfcheck` asserts, so it wants to land with commit 1, but a builder who
  reads section 4 will write the right condition either way. Nothing downstream is unsatisfiable
  without it.

**Left-shift, in one sentence.** Every one of this pass's six edits is a disagreement between two
paragraphs of section 4 or between section 4 and section 6, and rev-6 wrote both sides of five of
them — so the missing step is not more review but a fold checklist that maps each newly argued field to
the criterion in section 6 that asserts it, and refuses the fold while any field has prose and no arm.
`selfcheck` is already the right home: it should refuse a role whose operative columns duplicate
another's, a guard pathspec matching no declared class, a descriptor flag no criterion asserts
positively, and a `requires_if` key absent from `[config]`. Four small arms retire this whole class.

**On the shape of this pass.** Precision fell from 0.50 to 0.25 across the two passes on the same
document, on a deliberately narrower scope. That is the surface hardening, not the review weakening:
three quarters of what the finders raised against rev-6 did not survive refutation, and the survivors
are consistency repairs rather than design gaps. Review 2's seven blockers are all addressed in
substance — the population claims are gone, `[[hole]]` has a runnable probe, `[[files]]` has
destinations, AC8 carves out the authorized re-run, the gate-runner write has a declaration and an
effect criterion, and the failure-policy knobs have keys and defaults. The protocol's own guidance
applies from here: once these six edits land, build rather than audit again. A seventh pass over this
document will find prose about the design, not defects in it.
