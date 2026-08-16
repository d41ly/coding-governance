## Verdict: BLOCKED

**Target:** `memory/builds/aSealedCaravan/spec/2026-08-10-spec-DEPL-aSealedCaravan-2.md`
(`DEPL-aSealedCaravan-2`), rev-5, base `16aeb5ef`, before any code. This is the M4 spec-audit pass
that follows the rev-2 fold of review 1.

**Shape:** raw 50, confirmed 25, refuted 25, unverified 0. Precision 0.50 — at the floor
`memory/guides/REVIEW-PROTOCOL.md` sets, so the correct next move on this spec is tighter scope, not
more agents. Four lenses (underspecification, contradiction, assumptions, prior-art), five verifier
batches over five agents total — inside the protocol's at-most-5-total and at-most-5-concurrent
budget. Every confirmed finding survived an adversarial skeptic whose default was refutation, and
each verdict had to reproduce against the spec text or the running tree.

**Severity split:** 7 blockers, 14 high, 4 medium, 0 low.

**Measurements re-run at review time, at the current tip:** `git ls-tree -d HEAD tools/` = **11**
directories (base `16aeb5ef` = 10; `tools/unattended/` landed after grounding) · four adopters ship a
`--check` arm (`agent-instructions`, `drift-audit`, `memory-recall`, `unattended`), not three · six
`adopt-*.sh` under `tools/*/` · `MANIFEST-TEMPLATE.md` matches `grep -cE '\{\{[A-Z]'` on **33 lines**
(46 occurrences, 23 distinct) · `manifest-check.sh:87` is C1, `:58` is the exit-2 env error ·
`KIT_UNATTENDED_VERSION` is gated at `check-kit-versions.sh:54` · zero `KIT_*` constants under
`tools/agent-instructions/` and `tools/gate-lint/` · `KIT_CHECK_WIRING_VERSION=1.0` at
`tools/check-wiring.sh:13` · 33 `tools/lib/` mentions in `tools/gate-legs.json` guards.

---

## How to read this report

Ids are the raw ids from the verification pass, so they are sparse. Twenty-five confirmed findings
collapse to **nineteen distinct edits**; the overlap clusters are named below and are one edit each.
Every finding names the section the correction lands in, the concrete fix, and a left-shift where one
exists.

| Cluster | Ids | One edit |
|---|---|---|
| `tools/unattended/` is in no population | 6, 22, 33, 44 | Measure the kit, add its row and registry entry, re-derive every stale count |
| The kickoff-manifest leg cannot be green at AC1 | 17, 30 | A second hole flag for gate-red-by-design, rescope AC1 |
| Gate-runner and CI wiring is modelled nowhere | 2, 35 | A `[gate_runner]` declaration in the target descriptor plus an effect AC |
| The F4 baseline observes an empty population | 5, 19 | Three-valued baseline over the TARGET's own legs, added to S5's order |

**The through-line.** Rev-2 fixed this spec's data model where review 1 pointed and rev-5 closed the
fork set, but three structural gaps outlived both passes. First, `[[files]]` and `[[hole]]` are the
two fields the design leans on hardest and the two that were never given the treatment `[[outcome]]`
got at rev-2 — "code + PROBE, not code + meaning" was applied to the weakest state in the model and
withheld from the strongest. Second, `apply`'s hard order in S5 names three writes (`.gitattributes`
blocks, rendered artifacts, gate-runner and CI legs) that no `[[files]]` role, no receipt row and no
`deploy.toml` key can express, and AC4 asserts their ORDER while nothing asserts their EFFECT. Third,
the spec's population claims were measured at base and the tree moved underneath them; rollout commit
1's entire deliverable is that population, so the miss lands inside the first commit.

---

## Blockers (7)

### id=1 — `[[hole]]` has no discharge predicate and the outbox has no shape

**Lands on:** §2 S8 · §4 Data model (`[[hole]]`) · §6 AC6

The word "discharged" appears in S8, S9 and AC6 and is defined nowhere. The example `[[hole]]` carries
only `id`, `kind`, `blocks_adopt`, `why`. AC6's "`check` exits non-zero until each is discharged" and
AC5's resume trigger therefore have no evaluator, and the outbox has no stated location, file shape or
age field for S9's "outbox age" to read. A builder can satisfy AC6 by treating discharge as "the
operator deleted the order file" — which makes `check` green on a target whose pins are still
inherited-vacuous, the exact failure S8 exists to prevent. `kind = "authoring"` is an enum of one with
no other member and no behavioural effect.

The asymmetry is self-inflicted: rev-2 gave `[[outcome]]` a RUN probe on the argument "code + PROBE,
not code + meaning" and left `[[hole]]` — the state that gates `--resume` and reds `check` — asserted
rather than measured. §10 does supply a reusable predicate for two of the four default holes
(`manifest-check.sh` C1, C6), so the criterion is not wholly unobservable; but the schema has no field
to carry a per-hole predicate, which contradicts §4's own "four files carry all state, nothing is
inferred", and memory-tree's measured-pins hole has no predicate anywhere in the spec.

**Fix:** give `[[hole]]` a `discharge` probe in `[[outcome]]`'s shape (`must_exist` /
`must_not_exist` / a command that must exit 0). For `measured-pins` that is a non-blank pin in the
target's `.memory-tree.conf`; for `map_extractors.py` a non-empty `EXTRACTORS` dict; for the playbook a
no-surviving-placeholder grep. State where the outbox lives (e.g. `<target>/.governance/outbox/` with
one file per hole id), what one order contains, and which field carries the timestamp S9 reads.
Restate AC6 to assert the probe FIRES: an undischarged hole reds, and filling the artifact turns it
green.

**Left-shift:** `selfcheck` should refuse a `[[hole]]` with no `discharge` probe, the same way AC10
refuses a `version_from` that matches no line — the population check is already the right home.

### id=2 / id=35 — the last step of `apply`'s hard order has no artifact in the data model

**Lands on:** §2 S5 · §4 Data model (`deploy.toml`, `[[gate_leg]]`) · §6 AC1, AC4

S5 orders "gate-runner and CI legs last" and AC4 observes only that it IS last. Which file is edited,
in what syntax, and by what CI system are all unstated. `WIRE-INTO-PROJECT.md:261, 299, 483` shows what
is being mechanised — add the leg "to BOTH your CI config and your local gate runner, grep-guarded so a
re-run doesn't duplicate the leg", plus a mandatory `fetch-depth: 0` — a target-owned, target-specific,
idempotent text edit whose path and format only that target knows. `deploy.toml` carries `gov_source`,
`prefix`, kit ids, per-kit config answers and the failure-policy knobs, and nothing else;
`[[gate_leg]]` carries name/argv/guard/history_depth, which is what the leg IS, not where it lands.
Neither `tools/run-gates.sh` nor `tools/gate-legs.json` is a registry entry — §4 names exactly three
non-directory deployable surfaces (the playbook pair, `manifest-check.sh`, `settings-merge.py`).

`history_depth` exists solely to be emitted into a target's CI job (§7) and has no named consumer, no
output format and no AC. AC1's "each of their gate legs exits 0 in that fixture" is satisfiable by
executing the descriptor's `argv` directly, so the entire wiring step can be a no-op with every
criterion green — the deployed-leg-vacuously-green class §7 itself names. AC11 ("`plan` lists every
file it would write") and AC2 (path-and-hash over the receipt) cannot cover a write whose file, format
and idempotence rule are undefined, and AC15's fresh-empty-repo and non-Python arms have no gate runner
to wire into at all.

**Fix:** add a `[gate_runner]` table to `.governance/deploy.toml` declaring the target's runner kind
and file(s), its insertion grammar, its CI workflow path and job name — or an explicit
`none = "emit an outbox order instead"`. State that `history_depth` is consumed by the CI emitter and
how it renders. Give the wiring an anchored-block receipt role so AC2 can cover it. Add an AC that runs
the TARGET's own runner and asserts the newly wired leg executed, plus a shallow-checkout arm asserting
the emitted CI leg reds or names the degradation rather than passing. If the intent is to ship gov's
runner, name `run-gates.sh` + `gate-legs.json` as a fourth deployable surface with its own descriptor.

**Left-shift:** this is the same class as the run-gates canary's "a guard naming an untracked path
would skip forever" check — the acceptance matrix needs an arm that proves a deployed leg can go RED,
not just that it exists.

### id=3 — three of four failure-policy knobs are unnamed, and the landing flow they presuppose is unscoped

**Lands on:** §4 Data model (`deploy.toml` knobs) · §5 risks/rollback · §2

Only the pre-existing-red knob was given a default (F4). "On a diverged remote" and "on a push-scope
failure" imply `apply` fetches and pushes; §5 asserts "landing is by branch and PR", bounds the
half-applied-install risk on it ("a crash leaves an abandoned branch"), and defines rollback as deleting
the branch — yet S5's two phases end at `git add` and no S-item mentions creating a branch, committing,
pushing or opening a PR. A builder cannot tell whether `apply` runs `git commit`/`git push` at all,
which is the difference between a tool that stages files and a tool that writes to a remote unattended.

The hook-block knob is sharper still and survived every refutation: AC15 requires the "pre-commit hook
blocks" fixture arm to assert "a specific message or on-disk effect", and the spec never says what
`apply` should DO when a hook blocks — so that arm can only assert whatever the code happens to print,
which is a test written after the fact against itself.

**Fix:** add a §4 sub-section naming each knob's key, allowed values and default. Then either scope the
landing flow as an S-item (branch-name derivation, whether it commits, whether it pushes, whether it
opens a PR, and what an unattended run is permitted to do) or state in §3 that `apply` writes and stages
only and the operator lands — and correct §5's risk and rollback lines to match. Give AC15's hook-block
arm a stated expected outcome.

**Left-shift:** the unattended kit already binds "a run that will merge and push with no owner turn"
to a committed standing mandate; if `apply --unattended` can push, it inherits that protocol rather
than inventing a second answer — cite `memory/guides/UNATTENDED-PROTOCOL.md` in §4 and let its leg
carry the constraint.

### id=16 — AC8's detection predicate refuses every re-run the spec designs for

**Lands on:** §6 AC8 (against AC2, AC5, AC7, §2 S3)

AC8's predicate is stated without qualification: refuse when "any registry entry's version constant
resolves in the target, **or** `.governance/install.json` exists". After the first apply BOTH disjuncts
are true. So AC2 ("when that `apply` runs a second time" — the idempotency criterion, required on both
POSIX and Git-Bash by S11), AC5's `apply --resume`, AC7's re-apply, and S3's "standing authorization for
an unattended re-run" are each refused before writing. AC2 and AC5 have no satisfying assignment.

§3's non-goal excludes converging a repo that already carries kits, which explains why a FOREIGN kit
refuses — but nothing in the spec distinguishes a foreign install from govkit's own receipt inside the
predicate. The builder must guess which criterion is authoritative, and the committed descriptor's whole
purpose is contradicted by the refusal it triggers.

**Fix:** carve the authorized re-run out of AC8. Refuse when a registry entry's version constant
resolves at EITHER prefix and `.governance/install.json` does NOT claim it; proceed when this target's
own receipt claims it. State that `--resume` and a re-apply are receipt-authorized paths, and name in
the refusal which kit resolved and which claim was missing.

**Left-shift:** AC16 already requires every refusal message to be asserted by name in the matrix; add
the mirror obligation — every refusal branch needs a matrix arm proving it does NOT fire on the
authorized path. A refusal with no negative arm is the guard-that-always-fires twin of the guard that
never can.

### id=17 / id=30 — AC1 is unsatisfiable for the kickoff-manifest kit

**Lands on:** §6 AC1 · §4 Inventory table (kickoff-manifest row) · §4 `[[hole]]`

Verified in source. `manifest-check.sh:87` defines C1 as `grep -nE '\{\{[A-Z]'` over the manifest, and
`MANIFEST-TEMPLATE.md` matches on 33 lines — `{{LAYOUT}}`, `{{REMOTE}}`, `{{DEFAULT_BRANCH}}`,
`{{BRANCH_CONVENTIONS}}`, `{{AREA_1}}` and the audit values `{{AUDIT_DATETIME}}`, `{{AUDIT_SHA}}`,
`{{WATCH_PATHSPECS}}`, `{{VERIFY_PATHS}}` (which C3/C4/C6 also grade). The template carries the
`kickoff-manifest: v1.1` marker, so the ratchet does NOT take its unmanaged-manifest exit-0 escape.
Landing the ratchet with no manifest scaffolded fares no better: `manifest-check.sh:58` exits 2 with a
`MANIFEST env ERROR`. `kickoff-manifest ratchet` is a real leg at `tools/gate-legs.json:10`.

§4's inventory puts the kickoff manifest in the DEFAULT set with its "manifest section B" hole marked
`Blocking: no` and `Config: none`, so nothing in the descriptor renders those placeholders, and AC6
keeps the hole undischarged at the moment AC1 grades. AC1 demands "each of their gate legs exits 0 in
that fixture" and excludes only codebase-map. AC1 and AC6 therefore point in opposite directions for
this one kit. This is the identical class rev-2 fixed for codebase-map and left open here, and
`blocks_adopt` cannot express it — it models ADOPTER failure, not a leg red until a non-blocking hole
is filled.

**Fix:** split the hole taxonomy. Keep `blocks_adopt` for a hole that makes the adopter fail; add
`blocks_gate` for a hole that leaves the kit's own leg red until discharged. Mark the manifest
section-B hole with it, reword AC1 to "each gate leg of a kit with no undischarged hole exits 0", and
name the kickoff-manifest leg alongside codebase-map's as red-by-design until `apply --resume` — with
the manifest's green state observed after discharge exactly as AC5 does for codebase-map.

**Left-shift:** `selfcheck` should assert that every kit whose default-set install leaves a gate leg
red carries a hole flag saying so. Otherwise the third instance of this class arrives the same way the
first two did — discovered when the acceptance matrix is written, in rollout commit 3.

### id=44 (with 6, 22, 33) — `tools/unattended/` exists on `main` and appears nowhere in this spec

**Lands on:** §4 Data model (registry prose) · §4 Inventory table · §2 S6 · §6 AC10 · §10

Verified: `git ls-tree -d HEAD tools/` lists **eleven** directories; base `16aeb5ef` lists ten.
`tools/unattended/` landed after grounding and the spec still reached rev-5 saying "`tools/` holds ten
directories". It carries every marker the spec itself uses to define a kit: `adopt-unattended.sh` with a
`--check` render-parity arm (plus its adopter e2e), a committed project-owned `.unattended.conf` whose
shipped example carries literal placeholder holes, a rendered `.claude/skills/unattended/SKILL.md`, a
BINDING protocol, five legs in `tools/gate-legs.json`, and `KIT_UNATTENDED_VERSION` already gated at
`check-kit-versions.sh:54`. `tools/govkit/` will be a twelfth directory with neither entry nor exemption.

This lands INSIDE rollout commit 1, whose entire deliverable is `registry.toml` plus `selfcheck`: AC10's
both-direction assertion ("every `tools/*` directory is either an entry or an exemption with a reason")
reds on day one on two directories, and the §4 inventory row for unattended — config keys, holes,
blocking verdict, adopt command, outcome map, five gate legs — has never been measured. Because S6's
`--all` list is hand-enumerated prose with no AC tying it to the registry, unattended can land as an
entry `--all` never selects: a silently undeployable kit. Its required-key set is also a second
`blocks_adopt` candidate — a conf declaring nothing renders a Skill carrying `{{KEEPALIVE_CREATE}}`, and
`adopt-unattended.sh --check` now fails on a surviving placeholder — which falsifies §4's "exactly one
of which blocks" as a general claim about the two-phase design.

Three derived counts are stale with it: "measured by running all eight adoption entrypoints" (there are
six `adopt-*.sh` under `tools/*/` today and the entrypoint set is larger than the spec's eight), Files
touched's "1 + 12" descriptors, and §10's "THREE adopters ship a `--check` render-parity arm" — it is
four, and that count is what `check`'s fan-out design is sized against.

**Fix:** re-run the entrypoint inventory at the current tip. Add an `unattended` row to §4's table
measured the way the other rows were (run `adopt-unattended.sh` end to end in a throwaway repo), with
its `[config]` keys, its holes, its blocking verdict, its adopt argv, its outcome map and its five gate
legs. Correct the registry prose to eleven, declare `tools/govkit/` a self-exemption with its reason
(it runs on the deployer, is never deployed), place unattended in `--all`, re-cost Files touched, and
correct §10 to four adopters naming `adopt-unattended.sh`. Add an AC asserting `--all` selects exactly
the non-exempt registry entries, so a future kit cannot be an entry no selection reaches. State the
directory count as DERIVED by `selfcheck` rather than as a literal in prose.

**Left-shift:** this is the codebase-map coverage gate's own thesis applied to the registry — a new
moving part must red until a declaration claims it. Make `selfcheck` the ratchet and never spell a
population count in prose again; that single change retires this whole cluster permanently.

---

## High (14)

### id=5 (with 19) — the F4 baseline has no defined value for a leg that is not installed yet

**Lands on:** §4 Data model (F4 baseline) · §2 S5 · §6 AC4, AC8, AC15

F4 baselines "every selected kit's gate legs BEFORE it writes anything", but AC8 guarantees the target
carries no kit, so at first install those legs do not exist — `argv` is `["bash", "{kit}/…"]` and
`{kit}` is not there. Under the stated rule ("fail only on a leg green in the baseline and red after")
`apply` can never fail on a gate leg in the main path. Read the other way (absent counts as green) it
fails on every leg a fresh install leaves red by design, including codebase-map's, which AC5 REQUIRES
to be red. The two readings give opposite behaviour and the third state is undefined.

§4's claim that "AC15's pre-existing-red fixture arm is the observation that this holds" is false
against AC15's text: in a target with no kits, a pre-existing red gate is by construction the TARGET's
own, which a selected-kit-leg baseline never observes, and AC15 only requires the arm to assert "a
specific message or on-disk effect". The baseline is also a write-free step appearing in neither S5's
declared two phases nor AC4's ordering, which starts at `.gitattributes`.

**Fix:** state the three-valued baseline explicitly — `green` / `red` / `absent` — and what each does
(absent implies the leg is expected to become green, and a red one fails the install, except where a
hole flag declares it red-by-design). Baseline the TARGET's own gate runner rather than the kit's legs,
and treat each newly installed leg's first run as a separate class. Add the baseline step to S5's hard
order and to AC4's log assertion. Restate AC15's arm as the observation F4 claims: a target leg red
before the install is reported and does not fail it; a leg green before and red after fails it, naming
the leg.

### id=6, 22, 33 — folded into the id=44 cluster above

Kept as distinct verdicts because each measured the same omission from a different lens
(underspecification, contradiction, stale-assumption) and each names a different downstream count. One
edit.

### id=8 — three of `check`'s five arms are observed by no criterion

**Lands on:** §2 S9 · §6

`check` appears in §6 only inside AC5 (reports inert), AC6 (reds until holes discharge) and AC7 (reports
project-owned rather than drift). Nothing corrupts a receipt-covered engine file and requires `check` to
name it; nothing mutates the recorded commit or an installed byte and requires the provenance arm to
fire — AC3 proves provenance at APPLY time via `git show`, which is the harness observing, not `check`;
nothing asserts `check` invokes `adopt-*.sh --check` for the four kits that have one. S9 makes `check`
"the leg a target repo runs in its own CI", so its negative arms are the whole product, and it can ship
as a receipt-parser that verifies nothing while all sixteen criteria pass — a green-by-empty-population
gate in the unit whose thesis is that those are the enemy. This repo's own evidence is that such a
verifier goes vacuous in good faith: drift-audit's Skill named two nonexistent files while its `--check`
reported in sync.

"Outbox age" compounds it — S4 enumerates the per-file receipt as role, sha256, kit id and version, and
source commit, with no timestamp for an age to be computed from. (Weaker sub-point: a receipt-LEVEL
timestamp outside that per-file list would supply the origin, so the age half is inference; the
unobserved-arms half is not.)

**Fix:** add ACs mirroring the arms — (1) modify one `engine`-roled file in an installed fixture and
require `check` to exit non-zero naming the path and the expected hash; (2) point the receipt at a
commit whose bytes differ and require the provenance arm to name it; (3) break a kit whose adopter has
a `--check` arm (e.g. edit the rendered `.claude/skills/memory-recall/SKILL.md`) and require `check` to
surface that adopter's refusal; (4) add the timestamp field the age check reads, or drop "outbox age"
from S9.

**Left-shift:** `check-arms.py`'s rule — every fail branch armed by a positive assertion naming its own
failure text — is exactly this, and F3 deliberately kept it shell-only. AC16 applies that rule to
refusals; extend AC16 to cover `check`'s findings, not just `govkit.py`'s refusals.

### id=18 — `requires_if`'s condition names a key that does not exist

**Lands on:** §4 Data model (`requires_if`)

`when = "pins.corpus_ids_enabled"` names a config key present nowhere in the tree. The real arming
condition is any of `DEAD_PATH_PIN` / `ORPHAN_ID_PIN` / `READ_PATH_CEILING` being non-blank, which the
raise site itself spells out, and the raise is at `corpus_ids.py:105-109`, not the `:44` the `why`
cites (`:44` is `HYGIENE = …`; `GRAMMAR_DIR` is `:45`). The same descriptor's `[config] required_keys`
lists only `MEMORY_ROOT`/`DISCIPLINES`/`FAMILIES`, so the key is undeclared there too, and `when`'s
resolution namespace — conf key, `deploy.toml` answer, or computed predicate — is left undefined.

This is not a cosmetic slip in an illustrative block: `requires_if` is one of the four fields §4 argues
into existence, AC9's "names the missing key" has no key to name, and AC10's `selfcheck` has no key to
resolve. Worse, the real condition cannot be evaluated at apply time under this design at all — §4's own
inventory declares memory-tree's measured pins a `[[hole]]`, so the pins are blank during `apply` and are
filled later by an outbox discharge, at which point nothing re-evaluates the edge. The kit either
silently ships without memory-recall (checks 13-16 hard-fail) or pulls it in unconditionally: the two
failures §4 says the field prevents.

**Fix:** spell the condition against real keys — a `when_any_key_set` over the three pins — add them to
`[config]` (or a `conditional_keys` list), correct the `why` citation to the raise site, define `when`'s
resolution namespace, and say what re-evaluates a conditional edge after a hole is discharged.

**Left-shift:** the same class rev-2 already folded (the `gate-legs.json` "two keys, actually three"
correction). A gotcha row for "a spec's illustrative config block is graded as spec text, not as
decoration" would catch the next one at review time.

### id=19 — folded into the id=5 cluster above

### id=21 — `[[files]]` cannot express a destination, and four registry entries need one

**Lands on:** §4 Data model (`[[files]]`) · §6 AC10, AC11

`[[files]]` carries `include` and `role` only, with no destination expression anywhere in §4, so every
file lands at `<prefix>/<kit>/<relpath>`. That cannot describe four of the registry's own declared
entries. The CLOSED sibling `TOOL-aSealedCaravan-1` S2 fixes `manifest-check.sh` at a flat
`tools/manifest-check.sh` from source `skills/session-kickoff/manifest-check.sh` — a rename across
trees, which `WIRE-INTO-PROJECT.md:353` confirms post-S2; `.claude/hooks/agent-cap.js` installs outside
any kit prefix; `settings-merge.py` is a flat `tools/` file; and the playbook with its two companions
are root files landing at an owner-chosen instantiation path. §4 acknowledges those surfaces are "not
`tools/*` directories at all" but never says how a descriptor spells where their bytes land.

Rollout commit 1 is "a `kit.toml` for every entry" and cannot be written for any of the four. AC10 grades
source-side existence only; AC11 ("`plan` lists every file it would write … `apply` produces exactly that
file set") presumes a destination the model does not carry.

**Fix:** add a destination to `[[files]]` — a `to =` per rule, defaulting to `<prefix>/<kit>/<relpath>`,
plus a `flat = true` form for a single-file entry — and spell the destination in §4 for the four
non-`tools/<kit>/` entries, citing `TOOL-aSealedCaravan-1` S2 for the two it already fixed.

### id=31 — rendered artifacts have no gov-blob provenance, so AC3 is false for them

**Lands on:** §4 Data model (`install.json`, `[[files]]` roles) · §6 AC3

`tools/memory-tree/adopt-memory-tree.sh:64-69` renders `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and
`memory/guides/BUILD-METHOD.md` through `render_doc` (a sed over `{{KIT_DIR}}`/`{{TOOL_ROOT}}`), and
memory-recall, drift-audit and unattended each render a `.claude/skills/*/SKILL.md`. S5 names "rendered
artifacts" as their own step in `apply`'s hard order and AC4 asserts that ordering, so govkit itself
writes them. Yet the receipt records "the gov source commit the bytes came from" per file, AC3 quantifies
over EVERY file named in the receipt, and a rendered file's bytes equal no `git show <commit>:<path>`.
The role enum (`engine | project-owned | generated`) has no slot that both records provenance-by-render
and exempts byte equality.

Either horn is a design change: AC3 reds on every install, or the committed rule-set documents an adopter
actually receives sit outside the receipt and outside `install.sums` — so `check`'s integrity arm never
sees the files most likely to be hand-edited, and §10 already concedes memory-tree ships no `--check`
arm, so nothing else covers them. This is the class the sibling unit's install-prefix gate was built for:
a rendered artifact stranding an adopter while a gate exits 0.

**Fix:** add a `rendered` role whose receipt row carries the template path, the substitution inputs and
the output sha256 instead of a source commit; scope AC3's byte-equality predicate to `role = "engine"`;
and add an AC that a rendered file re-renders byte-identically from the recorded inputs.

**Left-shift:** four adopters already ship exactly that assertion as their `--check` arm. `check`'s
fan-out is the reuse; state it in §10 rather than re-deriving it.

### id=34 — deployed `guard` pathspecs name gov-tree paths that cannot exist in a target

**Lands on:** §4 Data model (`[[gate_leg]]` `guard`) · §6 AC10

Every guarded leg's pathspecs in `tools/gate-legs.json` are gov-tree literals, and each kit leg names
`tools/lib/` (33 mentions) — the directory §4 declares a permanent exemption on the stated ground that
"nothing under `tools/lib/` ever needs to travel". Others name `memory/HYGIENE.md`,
`memory/TEMPLATE-SPEC.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `skills/session-kickoff/`,
`.githooks/`, `.claude/` — all MEMORY_ROOT- or gov-layout-relative. §4 gives `argv` a `{kit}`
interpolation and probes a `{memory_root}` one, but gives `guard` neither, and AC10 pins the descriptor's
guard to MATCH gov's, which forecloses translation at the descriptor level.

The consequence is the one `tools/run-gates.test.sh` already records verbatim: `git diff --quiet BASE --
does/not/exist` reports no difference, so the leg would skip forever, printing a reassuring GATE skip. A
deployed guarded leg is green-by-absence — and if the canary is deployed too, the target's bar reds
instead.

**Fix:** state that guard pathspecs are RENDERED against the target's install prefix and MEMORY_ROOT,
forbid a rendered guard from naming an exempt path (`tools/lib/`), and change AC10's predicate from "a
matching guard" to "the descriptor's guard renders to gov's guard under the identity substitution".

**Left-shift:** the run-gates canary already refuses a guard naming an untracked path. The deployed
runner needs the same canary, or the refusal exists only on the deployer.

### id=35 — folded into the id=2 cluster above

### id=36 — no role expresses a file that is part gov and part target

**Lands on:** §4 Data model (`[[files]]` roles) · §2 S5 · §6 AC2, AC7

S5's FIRST land step writes "`.gitattributes` blocks" into a file the target owns. Gov's own
`.gitattributes` pins are prefix- and MEMORY_ROOT-relative (`memory/**/*.md`,
`memory/DECISIONS.md merge=rows`, `.claude/skills/*/SKILL.md`, `tools/gate-legs.json`,
`tools/memory-tree/.memory-tree.conf.example`), so the block must be RENDERED per target, not copied.
`[[files]]` is an include-glob plus three whole-file ownership classes, none of which expresses a file
that is part gov-written block and part target content. Marking it `project-owned` contradicts S5 (AC7
says a project-owned file is not rewritten); any other role makes AC2's whole-file hash treat any target
edit as drift and makes the second apply's append non-idempotent. Same shape for `.claude/settings.json`
(`settings-merge.py` is a registry entry whose entire job is merging into a target-owned file) and for
the `CLAUDE.md` pointer `adopt-agent-instructions.sh` writes beside the target's own `AGENTS.md`.

**Fix:** add a `merged` role with an anchored begin/end marker; hash the BLOCK rather than the file in
the receipt and in AC2's predicate; and state that `.gitattributes` blocks are rendered against the
target's prefix and MEMORY_ROOT rather than copied.

### id=45 — `version_from` is unfillable for two selectable kits and duplicates an existing table

**Lands on:** §4 Data model (`kit.toml` `version_from`) · §6 AC8, AC10

Verified: zero `KIT_*` constants and zero `gov:kit` markers under `tools/agent-instructions/` and
`tools/gate-lint/`, and `check-kit-versions.sh` has no `need` call for either. Both are `--all`-selectable
per S6, so S2's "version constant location" and AC10's "every `version_from` pattern matches exactly one
line in its named file" are unfillable for two entries, and AC8's detection predicate ("any registry
entry's version constant resolves in the target") is structurally blind to both — `apply` will happily
re-land agent-instructions over an existing install.

The dual-spelling half is grounded too: `check-kit-versions.sh`'s own header declares it "the govkit
Phase-0 contract gate … every kit carries a well-formed version constant a deployer can grep in a target
repo", and it is already a hardcoded `{label, file, pattern}` table over the kits that do. With
`version_from` in the registry AND `need` calls in that script, the repo carries two independent
spellings of one fact with nothing asserting they agree — the second-population drift class
`TOOL-aSealedCaravan-1` F2 rejects by name.

**Fix:** state in §4 that `check-kit-versions.sh` is the prior art, and make the descriptor the single
source — have `selfcheck` assert registry `version_from` against `check-kit-versions.sh` in both
directions, or scope in converting that script to read the registry. For agent-instructions and gate-lint
either add a marker in the same commit or give `version_from` an explicit `none = "<reason>"` form, and
correct AC8 to name what its predicate does for a kit with no constant.

### id=47 — the registry's completeness claim covers only directories

**Lands on:** §4 Data model (registry.toml) · §6 AC10

AC10 asserts "every `tools/*` **directory** is either an entry or an exemption with a reason", and §4
names exactly three non-directory deployables. But `WIRE-INTO-PROJECT.md` already prescribes copying
`tools/check-wiring.sh` (+`.test.sh`, at `:412`/`:420`), `tools/push-main.sh` (+`.test.sh`, at
`:422`/`:425`) and `tools/check-kit-versions.sh` (`:430`) into a target, and S5 itself installs the gate
runner (`run-gates.sh` + `gate-legs.json`) and `.githooks/`. Six-plus tracked single-file deployables sit
in no population at all, so `selfcheck` is green while the registry is incomplete, and a new single-file
gate added under `tools/` is outside the ratchet forever. `tools/check-wiring.sh:13` even carries
`KIT_CHECK_WIRING_VERSION=1.0` — version-detectable, unrepresented, and absent from
`check-kit-versions.sh`'s need list.

**Fix:** make AC10's both-direction assertion quantify over the tracked `tools/` SURFACE, not `tools/*`
directories: every depth-1 file under `tools/` must be an entry, a member of an entry's `[[files]]`, or an
enumerated exemption with a reason — and the same for `.githooks/`. Add a §4 line stating where the
gate-runner pair and the two single-file gates live in the registry.

**Left-shift:** this is the green-by-absence class the registry exists to close, and it is exactly what
`map_extractors._tool_kits()`'s docstring (which §4 cites as its authority) warns about. Quantifying over
the tracked surface makes `selfcheck` the ratchet the coverage gate already is.

---

## Medium (4)

### id=10 — `--kits` and `--all` have no acceptance criterion

**Lands on:** §2 S6 · §6

S6 declares three selection modes and every selection-dependent criterion in §6 (AC1, AC2, AC5, AC6) is
scoped to the default set. So S8's "union of holes over the SELECTED kits" is never observed varying,
`requires_if` only matters for a selection that omits memory-recall and no arm makes one, and the failure
§4 calls "the more dangerous of the two" — drift-audit seeding empty product globs and unmeasured pins
while its own `--check` passes on existence alone — belongs to an `--all`-only kit, so the case the design
reasons hardest about is reachable by no criterion. AC6's hole set is the default four, so
`drift_signals.py` and the pytest `pyproject.toml` knobs are declared holes no arm ever derives an order
for. The five `--all` kits can land broken with the matrix green.

Partial mitigation exists — AC10's `selfcheck` statically validates every registry entry including the
`--all` kits, and AC15's matrix is stated as a minimum — so this is a matrix gap rather than a design
contradiction, which is why it sits at medium. Closing it still changes the deliverable.

**Fix:** add an AC over a non-default selection — `--kits memory-tree,memory-recall` produces an outbox
holding exactly that pair's hole ids and no others, and `--all` lands the extra kits with drift-audit
reported by `check` as incompletely adopted despite its adopter exiting 0 and its own `--check` passing.

### id=12 — `scope = "machine"` declares a class with no action

**Lands on:** §4 Data model (`scope`)

§4 justifies the class only by naming two behaviours `apply` must NOT have ("try to commit a junction or
silently skip the one component `/session-kickoff` needs") and never states the behaviour it does have:
junction, symlink, an outbox order, or a refusal. Nothing else closes it. S6's default set and `--all`
list together enumerate exactly the ten rows of §4's inventory table and contain no machine-scoped entry,
yet Files touched's "1 + 12" implies twelve entries. S4's receipt is per-file and repo-relative with no
machine section, so a re-deploy has nothing to no-op against. §5 scopes the deployer's writes to "a
repository the operator names", which a user-level junction is not. And the sibling
`TOOL-aSealedCaravan-1` F1 settles that the kickoff ENGINE is a per-machine junction and never lands in
the target, while §4 insists `apply` must not skip it. AC1's "lands AND configures" has no meaning for
such an entry.

**Fix:** state the action — most likely never written by `apply`, represented as a `[[hole]]` whose order
carries the per-machine junction command and the client restart, with `check` reporting it undischargeable
from inside the repo. Say whether the kickoff engine is a registry entry at all, and exclude
machine-scoped entries from AC1's "lands AND configures" in the criterion text.

### id=40 — memory-tree's adoption needs a per-clone git config the model cannot express

**Lands on:** §4 Data model (`[adopt]`)

`.gitattributes` declares `memory/DECISIONS.md merge=rows` and `memory/backlog/*.md merge=rows`, and the
ONLY thing that sets the driver is `tools/check-wiring.sh` (`git config merge.rows.driver` under `--fix`,
around `:453`), whose own unwired message states the consequence: paths declare `merge=rows` but the
driver is unset, so git falls back to a line merge that can duplicate a row. `check-wiring.sh` is a root
`tools/*.sh` and is not among §4's three non-directory deployable surfaces, so no target receives it —
while S5 lands `.gitattributes` blocks and memory-tree is in the default set, so the attribute travels
and the driver does not. `[adopt] argv` is one command (`adopt-memory-tree.sh --scaffold`, which sets no
config) and `scope = repo|machine` classifies the KIT, not an action. §4 already treats
`merge.rows.driver` as load-bearing in the `tools/lib/` exemption reason, which makes this a gap rather
than a scoping decision, and no `check` arm covers git config.

**Fix:** add a `[[wiring]]` block to the descriptor (machine-scoped, idempotent, with its own `--check`
predicate) and put `tools/check-wiring.sh` in the registry as the wiring step memory-tree's entry invokes,
so `check`'s three-state report can distinguish "landed and adopted" from "wired".

**Left-shift:** a gotcha class for "an attribute deployed without its driver degrades silently and no gate
reads git config" — this repo has the failure mode written down in `check-wiring.sh`'s own message and
nowhere a reviewer would meet it.

### id=48 — the reuse audit misses the closest existing seam and undercounts an adopter class

**Lands on:** §10 Reuse audit

`.unattended.conf` + `check-unattended.sh` is already this repo's "committed declarations the tooling
READS and never restates" mechanism: an explicit required-vs-optional key split (the conf annotates
`KEEPALIVE_INTERVAL` as deliberately outside the gate's required-key loop), a leg that reds when a script
respells a declaration, a rendered Skill graded for `{{`-placeholder completeness, and a
shipped-equals-installed parity check. Those map one-to-one onto §4's `[config] required_keys`, AC9's
named-missing-key refusal, S10's rendered Skill and AC14's parity gate, all of which are designed as if no
precedent existed. And four adopters ship a `--check` render-parity arm — agent-instructions, drift-audit,
memory-recall and unattended — not the "THREE" §10 states, which under-scopes what `check` must carry
itself.

**Fix:** add `.unattended.conf`/`check-unattended.sh` to §10 as the reused seam for the declaration layer
and for S10's rendered Skill, naming which of its behaviours `govkit check` composes rather than restates.
Correct the count to four, and list which kits still have no `--check` arm (codebase-map, memory-tree).

---

## What must be folded, and what is advisory

**Must be folded before the first line of code — all seven blockers plus the population and model
edits.** Rollout commit 1 is `registry.toml` + every `kit.toml` + `selfcheck`, so the builder meets four
of these inside the FIRST deliverable and would have to invent design answers mid-commit:

- **id=44 / 6 / 22 / 33** — the eleventh directory. AC10 reds on day one; the inventory row was never
  measured; three derived counts are stale. Re-run the enumeration at the current tip.
- **id=21** — `[[files]]` has no destination, so four of twelve descriptors cannot be written at all.
- **id=45** — `version_from` is unfillable for two `--all` entries, and AC10 grades it.
- **id=47** — AC10's completeness predicate must quantify over the tracked surface, not directories.
- **id=1** — `[[hole]]` needs a discharge probe and the outbox needs a stated location and file shape;
  without them AC5 and AC6 have no evaluator and `--resume` has no trigger.
- **id=17 / 30** — the hole taxonomy needs a `blocks_gate` flag and AC1 needs rescoping, or the headline
  acceptance criterion is unsatisfiable for a default-set kit.
- **id=16** — AC8's predicate must carve out the receipt-authorized re-run, or AC2 and AC5 have no
  satisfying assignment.
- **id=2 / 35** — the gate-runner and CI write needs a declaration, a receipt role and an effect AC.
- **id=3** — the failure-policy knobs need key names, values and defaults, and the landing flow needs
  either an S-item or an explicit §3 exclusion with §5 corrected to match.

**Fold in the same pass, cheaply — the model and criteria repairs (high).** id=5/19 (three-valued
baseline, target-scoped, added to S5 and AC4), id=8 (`check`'s three unobserved arms get ACs), id=18
(`requires_if` against real keys), id=31 (`rendered` role, AC3 scoped to engine), id=34 (guards are
rendered, AC10's predicate restated), id=36 (`merged` role with block-level hashing).

**Advisory — real, but they do not gate the build start.** id=10 (a non-default-selection AC; the matrix
is stated as a minimum and `selfcheck` covers the `--all` entries statically, so this can land with
rollout commit 3), id=12 (`scope = "machine"` — decide it before the entry is written, but it touches one
row), id=40 (`[[wiring]]` for the merge driver — a correctness gap in the deployed target, not in the
deployer's own commit 1), id=48 (§10 reuse audit — a count correction plus one named seam; costs nothing
and improves what commit 2 reuses).

**Left-shift, in one sentence.** Five of the seven blockers are population or predicate claims spelled in
prose that the tree then moved underneath, and this spec has now paid for that class twice (review 1's
"ten directories" measurement and this pass's eleven). Make `selfcheck` the ratchet for every count the
spec states — directories, descriptors, adopters with `--check`, holes with probes, kits whose fresh
install leaves a leg red — and never spell one of those numbers in §4 prose again.

**On the shape of this pass.** Precision landed exactly at 0.50, the floor. Half the raw findings did not
survive refutation, and the survivors cluster tightly in §4's data model and §6's criteria — the two
sections review 1 also sent back. The goal, the four-commit rollout, fork F1's location argument, the
two-phase `apply`, the probe-based outcome model and the bash-from-Python remedy all held under attack
and are not re-litigated here. This is a rev-6 design pass over §4 and §6, not a re-spec.
