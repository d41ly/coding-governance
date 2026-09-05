# TOOL-aJoinedCanon-2 — the fold procedure gains a re-read set

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-1 · base 750ca0ca · streams tooling · order 2 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Folding a review correction is the corpus's most travelled route and its dominant defect source, and
the entire instruction for it is one clause that names no re-read set. Replace that clause with a
short procedure: a table keyed on the section you just edited, naming the sections that edit may have
invalidated.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/BUILD-METHOD.template.md` M4 gains a fold procedure. Its fold sentence
  today is `**Fold fixes into the spec** (rev bump + §9 line), then **STOP**`. It gains a re-read
  table keyed on the edited section, and a pointer at
  `memory/gotchas/fold-text-is-unreviewed-surface.md` for the content practices the table does not
  supply.
- **S2** — the re-read table has one row per section a fold actually lands in, and each row lists the
  sections to re-read before the rev is bumped. The four rows are §2, §4, §6 and §7; the sets are
  derived in §4 below from the finding's own round-level distribution and from `A5`'s amended-arm
  count, not invented.
- **S2b** — a FIFTH row, `§8`, whose set is §2, §4, §6 and every criterion naming an `F<n>` or a
  `Q<n>`. BOTH spellings, because the corpus uses both: ten of this build's eleven forks are labelled
  `F1`/`F2` and this spec's own is `Q1`, so an `F<n>`-only clause would have skipped the criteria of
  the very spec that wrote it. Measured at the rev-3 fold. It is
  listed separately from S2's four because it was not derived the same way: the four came from the
  measured round distribution, and this one came from RUNNING S2's table on a real fold and watching
  it miss. §8 is the section a fork resolution ALWAYS edits, so a table with no §8 row triggers no
  re-read at all on the most common fold there is. Evidence is this build's own rev-2 pass,
  recorded in §4. The block also states that the table fires for EVERY section the fold ends up
  editing, not only the one it started in: the rev-3 fold of THIS spec edited §8 and §2, and it is
  §2's row, not §8's, that reaches §3 — where the non-goal contradicted by the ruling was sitting.
- **S3** — `tools/memory-tree/SPEC-TEMPLATE.template.md:183` — `Review corrections fold in here; bump
  the header rev and log it in §9.` — becomes a POINTER at M4's procedure and restates no row of it.
  One text, one home.
- **S4** — both live copies are re-rendered from the two templates by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited, so
  `memory/guides/BUILD-METHOD.md` and `memory/TEMPLATE-SPEC.md` move in the same commit as their
  shipped twins.
- **S5** — the procedure ends at "log what moved per §9's own rule". It states no §9 grammar of its
  own, because `TOOL-aJoinedCanon-1` (order 1) owns that grammar and lands first.
- **S6** — `tools/workflows/tier2-review.js` is the THIRD carrier, and it is a pointer exactly as S3
  is. Its round-above-1 spec-audit priming reads, verified at HEAD, `- this is a FOLD review. Aim at
  the text the previous round's fixes introduced, which is the only text in these documents nobody
  has reviewed.` That is the one sentence of fold priming the gotcha record names. It gains a second
  sentence naming `memory/guides/BUILD-METHOD.md` M4's re-read table and telling the lens to check
  the neighbours that table names for each section the fold edited. It restates no row.
- **S7** — the pointer lands in the `isSpec` branch of that ternary ONLY. The table's rows are spec
  section numbers and a code diff has none, so the same sentence on the diff-review branch would name
  a set the reviewer cannot apply.
- **S8** — `memory/project/method-carriers.txt` gains one row for `tools/workflows/tier2-review.js`.
  The pointer spells `BUILD-METHOD.md`, and `tools/memory-tree/check-method-carriers.sh` selects
  every tracked file outside `memory/` carrying that string, so the row is not paperwork: it is the
  recorded decision that this carrier POINTS rather than restates, and it is what makes an existing
  leg guard the pointer from here on (§7).
- **S9** — the harness version moves `1.6` to `1.7` in all THREE tokens on the `meta.version` line of
  `tools/workflows/tier2-review.js` — the field itself and the `gov:kit tier2-review@` and
  `gov:kit review-harness@` markers beside it. `tools/check-kit-versions.sh` requires the three to
  agree, and `tools/workflows/kit.toml` DERIVES the kit version from that same field, so there is no
  fourth carrier to move.

## 3. Non-goals (OUT)

- **No new gate arm, and no new check-12 predicate.** §7 says why. Inventing an arm that grades a
  claim of re-reading would add a green that means nothing.
- **No priming for the fold ACT, because this harness dispatches no agent that folds.** Verified at
  HEAD: `tools/workflows/tier2-review.js` spawns finder lenses, batched skeptics and one synthesis
  pass, and the fold is performed by the run that called it and came back — `unattended-build.js`
  returns `CONVERGING` with "fold, then re-invoke" rather than folding anything itself. So S6 reaches
  the round that REVIEWS a fold, which is the nearest thing to a fold this harness dispatches. A run
  that delegates its own fold to sub-agents primes them itself, and what governs there is M4, which
  M7's regrounding step 3 reads whole at every pass boundary.
- **No cutoff key, and no `.memory-tree.conf` edit.** The build's dated-cutoff rule binds a change
  that makes a landed spec red. This one adds no required field to any spec and grades nothing, so
  there is no retrofit to guard against and a cutoff key would be a knob with no rule behind it.
- **No rewrite of the four practices in `memory/gotchas/fold-text-is-unreviewed-surface.md`.** M4
  points at that record; copying its practices into M4 is the paraphrase-beside-its-source class the
  charter refuses.
- **Not a re-measurement of B1.** Whether the procedure lowered the fold-created share is a later
  measurement over later builds, named as the compensating check in §5 and not performed here.

## 4. Design

### The evidence the table is derived from

Finding B1 measured the fold across nine round-level measurements in five builds, and every one found
the fold created the MAJORITY of the next round's confirmed findings: 65–72% on `dBriefedPass`, 69%
twice on `dTieredTribunal-1`, 88.9% wide and 61.1% narrow on `dTieredTribunal-11`, 42 of 62 on
`dFramedEntrypoint`, four of five blockers on `dRetiredFork` round 2, both blockers on
`aGradedMandate` round 2. Only 12.0% of specs are still at rev-1, so this is the ordinary path and
not an edge case.

B1's second number is what shapes the table: the confirmed-finding distribution does not migrate
across rounds. §2+§4+§6 is 63.5% at round 1, 59.1% at round 2 and 65.0% at round 3. The fold keeps
breaking the same three sections, so a fixed table keyed on the edited section is sufficient — a
derived or per-build set would be machinery bought for a distribution that does not move.

A worked instance, verified at HEAD:
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:534` logs `rev-3` as
"folded round 2, which found the rev-2 fold had not reached the whole spec: S6 still specified the leg
check over a round-count FACT the data model had deleted, and four further sites still described the
fact shape." That is a §4 edit that invalidated a §2 item and four more sites, found a round later.
It is the exact defect the §4 row exists to catch.

### The procedure

M4's fold sentence gains this, in M4's own voice:

> **A fold is not one edit.** The section you edited has neighbours the edit may have invalidated.
> Re-read them BEFORE bumping the rev, and log whatever moved per §9's own rule.
>
> | You edited | Re-read, in this order |
> |---|---|
> | §2 Scope | §3 Non-goals · §6 Acceptance |
> | §4 Design | §2 Scope · §6 Acceptance · §7 Gates |
> | §6 Acceptance | §2 Scope · §7 Gates |
> | §7 Gates | §6 Acceptance |
> | §8 Open questions | §2 Scope · §4 Design · §6 Acceptance · every criterion naming an `F<n>` or a `Q<n>` |
>
> Every section this fold ends up editing fires its own row, not just the one you started in. A fork
> resolution that widens scope edits §8 AND §2, and it is §2's row that reaches §3.
>
> The set says WHERE to look. What goes wrong there is
> `memory/gotchas/fold-text-is-unreviewed-surface.md`, which the fold round's own checklist already
> selects — read its four practices rather than trusting the table alone.

Each set is earned, not symmetric by taste. §4 carries three because it is the section corrections
land in and the one the worked instance broke outward from. §7 is in §4's set on A5's evidence: at
least four criteria were amended because the arm landed elsewhere than the spec said, and in one case
the misplacement surfaced only at the closing review after 42 of 85 legs had silently left every
profile. §3 sits only in §2's set, because a scope item moving is the one edit that moves a cut-line.
§5 and §9 are deliberately absent: §5 is a fixed row sweep a fold rarely invalidates, and §9 is
written by the fold itself.

**The §8 row was earned differently, and the difference matters.** The four rows above come from
B1's measured round-level distribution. The §8 row comes from RUNNING those four rows on a real fold
and watching them miss: this build's own rev-2 pass folded ten owner rulings across ten specs on
2026-09-05, and a fork resolution edits §8 and often nothing else, so a four-row table keyed on the
edited section fires no re-read at all on the single most common fold there is. Two stale clauses
were caught in that pass by the mechanic rather than by the table — `TOOL-aJoinedCanon-1`'s AC1
named a fixture whose date fell PRE-cutoff under the very cutoff the fold had just ratified, making
a gate's own failing-case criterion unable to fail; and `TOOL-aJoinedCanon-3`'s AC5 still branched
on the outcome of a fork that had just been decided. Both are criteria naming a fork id, which is
why that clause is in the row rather than a bare section list. A table derived from where defects
LAND cannot see the section a fold always TOUCHES, and only using it revealed that.

Running it once more, on this spec at rev-3, moved the clause again. Both spellings are live in one
build: ten of `aJoinedCanon`'s eleven forks are `F<n>` and this spec's is `Q1`, so the `F<n>`-only
clause of rev-2 selected nothing here — the row would have gone quiet on the only spec whose author
had read it. Hence `F<n>` or `Q<n>` in S2b. The same pass produced the transitivity sentence, for the
same reason: the ruling's contradiction sat in §3, which no §8 row reaches, and only §2's row does.

### The third carrier, and why three carriers are still one mechanism

Read at HEAD before writing this. `tools/workflows/tier2-review.js` dispatches agents at three sites
— the finder lenses, the batched skeptics, and one synthesis pass — and NONE of them folds. Its one
sentence of fold priming is the round-above-1 clause inside the `REVIEW ROUND:` line, and it primes a
REVIEWER of a fold, not a folder. That is what S6 widens, and §3 records what it therefore cannot buy.

The new sentence, in the harness's own voice and in the `isSpec` branch only:

> Read the re-read table in `memory/guides/BUILD-METHOD.md` M4 and check the neighbours it names for
> each section the fold edited — the fold's commonest defect is a correct edit whose neighbour was
> left standing.

**M2 says one mechanism per spec, and this unit ships one.** The mechanism is the re-read set. It has
ONE home, M4, which is the only place a row is written; every other site names that home and restates
nothing. S3 already treats `SPEC-TEMPLATE.template.md` that way and no reviewer has read it as a
second rule, because deleting a pointer changes no rule — it changes only who can reach the one that
exists. Three pointers to one table are three call sites, not three mechanisms, and a closing diff can
still say which half a finding lands on because there is only one half. The honest cost of the third
one is not ambiguity but blast radius: it lands in a program rather than a document, so it carries a
version bump (S9), a registry row (S8), and a self-test leg (§7). That cost is what the tier question
in §9 is decided against, and it is not an argument for a second unit.

**The pointer spells the path, and takes the registry row that costs.** `unattended-build.js` already
does exactly this — its stage prompt tells every agent to read `memory/guides/BUILD-METHOD.md` whole
before acting — and it holds a `method-carriers.txt` row whose reason is that it points and restates
nothing. The
recipient here is an AGENT with `Read`, not a human editing a spec, so the pathless `BUILD-METHOD M4`
spelling S3 uses would make the pointer a lookup the lens can silently skip. One row buys the path,
and the row is not a tax: check 4 of that leg reds if this file ever stops mentioning the method, so
the pointer gains regression coverage no new arm had to be written for.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | M4's fold sentence gains the procedure block |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | line 183's clause becomes a pointer at M4 |
| `memory/guides/BUILD-METHOD.md` | RENDERED, not hand-edited |
| `memory/TEMPLATE-SPEC.md` | RENDERED, not hand-edited |
| `tools/workflows/tier2-review.js` | the `isSpec` fold-review priming gains the pointer; version 1.6 -> 1.7 |
| `memory/project/method-carriers.txt` | one row declaring the harness a pointer |

The render direction is the parity test's own, stated in its header: `--render` writes TEMPLATE ->
LIVE, and hand-editing the live copy is what the leg exists to catch.

### Alternatives rejected

- **Put the procedure in `TEMPLATE-SPEC.md` instead of M4.** TEMPLATE-SPEC owns the section canon, so
  by subject it is the natural home. It is the wrong home by READER: the skeleton's §4 body is
  instructional prose the author replaces with real design, so the fold clause does not survive into
  the spec being folded, and a folding session is looking at the spec. M4 is what a run reads whole —
  M7's regrounding step 3 is `**This file, whole.**` at every pass boundary. The reader wins.
- **Spell the pointer as the repo-relative path `memory/guides/BUILD-METHOD.md`.** Verified cost:
  `tools/memory-tree/check-method-carriers.sh` selects carriers with `grep -lF -- "BUILD-METHOD.md"`
  over every tracked file outside `memory/`, excluding only `BUILD-METHOD.template.md` itself, and
  `tools/memory-tree/SPEC-TEMPLATE.template.md` is not in `memory/project/method-carriers.txt`. The
  path spelling would therefore red the `method carriers (every pointer declared)` leg until a
  registry row is added. Rejected in favour of the pathless `BUILD-METHOD M4` spelling the same file
  already uses at line 138 for M7 — zero new gate obligation. A builder who wants the path anyway
  owes the registry row and now knows it.
- **Restate the gotcha record's four practices in M4.** Two carriers of one rule is the shape that rot
  is measured in, and the gotcha's own fourth practice is about exactly that failure.
- **A derived per-build re-read set.** The distribution does not move across rounds, so a derivation
  would compute a constant at cost.
- **Restate the table's rows inside the harness prompt**, sparing the lens a `Read`. That is a fourth
  copy of the one text, in the carrier least likely to be re-rendered when M4 moves, and it would
  make the three-carriers-one-mechanism argument above false rather than merely arguable.
- **Ship the harness change as its own unit, as rev-2 recommended.** Overruled by the owner on
  2026-09-05; §8 records the pick and why.

## 5. Production-readiness checklist

- security — the third carrier makes this no longer a prose-only unit, so the row is real. The added
  text is a STATIC string literal in a prompt: it interpolates no caller value, reads no file at
  build time, and touches none of the harness's argument validation, so it opens no path by which
  `args` or a reviewed document could steer an agent that could not already steer it. The two
  documents remain prose with no execution path.
- perf / scale — N/A — prose plus one prompt literal. No leg's runtime changes, and a prompt two
  sentences longer does not move a review's cost against the documents it makes the lens read.
- a11y — N/A — no user interface.
- i18n — N/A — this repo's documents are English-only by construction.
- error / empty / loading states — N/A — no runtime.
- observability — the only signal is the §9 lines the procedure produces, which `TOOL-aJoinedCanon-1`
  makes structured; this unit adds no signal of its own.
- risks (concurrency, data-loss, rollback hazards) — the live copies are GENERATED. Hand-editing one
  instead of rendering is the single failure mode, and `kit/dogfood doc parity` catches it. The
  harness carries a second hazard of its own: a version bump that moves one of the three tokens and
  not the others, which `kit version markers` reds on. Rollback is a revert of one commit; nothing is
  stateful.
- testing + left-shift gates — still no NEW arm, and the argument is re-made for three carriers
  rather than inherited from two. Two of the three carriers hold prose whose obedience is an act
  nobody can observe, so §7's reasoning stands unchanged for them. The THIRD is different in kind: a
  pointer in a tracked program is an artifact, and S8's registry row hands it to an arm that already
  exists — `tools/memory-tree/check-method-carriers.sh` check 4 reds if this file ever stops
  mentioning the method. So the carrier most likely to be edited by someone with no interest in the
  fold rule is the one carrier that is guarded, at the cost of one row and no new code. The
  compensating check for the rest is unchanged: `memory/gotchas/fold-text-is-unreviewed-surface.md`
  is the standing documented check for this class, it is reached by
  `python tools/memory-tree/gotchas.py --for-diff` on any diff touching
  `memory/guides/BUILD-METHOD.md`, and the M4 spec-audit loop is the instrument that measures whether
  the procedure worked — B1's own numbers came from those review records. Re-running B1's by-kind
  split over the next builds is the verdict, and it is a later measurement, not a gate.
- migration / rollback — no corpus migration. Landed specs are untouched and no cutoff key is added,
  per §3.
- user docs — N/A — `help/` is for user-facing product features; this is an agent-facing rule, and its
  three carriers ARE the documentation.

## 6. Acceptance criteria

- **AC1** — When M4 of `memory/guides/BUILD-METHOD.md` is read at HEAD, its fold sentence is followed
  by a re-read table with one row each for `§2`, `§4`, `§6`, `§7` and `§8`; the §4 row lists §2, §6
  and §7; the §8 row lists §2, §4, §6 and criteria naming an `F<n>` OR a `Q<n>`; and the block
  states that every section the fold ends up editing fires its own row, not only the first.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs on the landing commit, it
  exits 0, proving both live copies were produced by `--render` from
  `tools/memory-tree/BUILD-METHOD.template.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`
  rather than hand-edited.
- **AC3** — When the fold clause at `memory/TEMPLATE-SPEC.md:183` is read, it names `BUILD-METHOD` M4
  and contains no row of the table, so `grep -c 'Re-read, in this order' memory/TEMPLATE-SPEC.md`
  returns 0 while the same grep over `memory/guides/BUILD-METHOD.md` returns 1.
- **AC4** — When `bash tools/memory-tree/check-method-carriers.sh` runs after the edit, it exits 0.
  The `SPEC-TEMPLATE.template.md` pointer adds no row, because it uses the pathless
  `BUILD-METHOD M4` spelling; `memory/project/method-carriers.txt` gains EXACTLY one row, for
  `tools/workflows/tier2-review.js`, whose pointer spells the path. Reverting that one row while
  keeping the harness edit reds the leg's check 3, which is the failing case this criterion is
  written against.
- **AC5** — When `python tools/memory-tree/gotchas.py --for-diff <base>..HEAD` is run over this unit's
  own diff, `fold-text-is-unreviewed-surface` appears in the checklist, because that record's derived
  anchors include `memory/guides/BUILD-METHOD.md`.
- **AC6** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs at the push
  boundary, `memory hygiene`, `kit version markers`, `kit/dogfood doc parity`,
  `method carriers (every pointer declared)`, `workflow script syntax` and `tier2-review self-test`
  are all green. The two environment variables are not decoration: `tier2-review self-test` is
  `chunk = selftests`, `subject = kit`, so a plain bar and even a `GATE_FULL=1` bar hold it, and this
  unit edits a kit.
- **AC7** — When `tools/workflows/tier2-review.js` is read at HEAD, its round-above-1 `isSpec`
  priming names `memory/guides/BUILD-METHOD.md` M4's re-read table and tells the lens to check the
  neighbours it names, while the `else` branch of that same ternary — the diff-review priming — is
  byte-identical to its rev-2 text.
- **AC8** — When `bash tools/check-kit-versions.sh` runs after the edit, it exits 0, and
  `grep -oE "1\.7" tools/workflows/tier2-review.js | wc -l` returns 3, so `meta.version` and both
  `gov:kit` markers moved together. Moving any one of the three alone reds that gate, which is the
  failing case.
- **AC9** — When `bash tools/workflows/tier2-review.test.sh` and
  `node tools/workflows/check-workflow-syntax.js` are run on the landing commit, both exit 0, proving
  the added prompt text neither broke the script's restricted-runtime parse nor moved an argument
  arm the suite pins.

## 7. Gates

Legs this unit must keep green, all named as they appear in `tools/gate-legs.json`:

- `kit/dogfood doc parity` — the leg that binds the two templates and their two rendered copies.
- `kit version markers` — two obligations now. Every `tools/memory-tree/*.template.md` must carry a
  `gov:kit memory-tree@` marker equal to `KIT_MEMORY_TREE_VERSION`, which this unit does not bump, so
  those markers stay as they are; and the three version tokens on `tools/workflows/tier2-review.js`'s
  `meta.version` line must agree with each other, which is what S9 and AC8 move together.
- `method carriers (every pointer declared)` — see AC4. It goes from "unchanged" to "one row added",
  and that row is also this unit's only regression coverage (§5).
- `workflow script syntax` — `subject = repo`, so it runs on every bar; it is what proves the added
  prompt text still parses in the restricted runtime.
- `tier2-review self-test` — `chunk = selftests`, `subject = kit`, guard `tools/workflows/`. It is
  held by a plain bar AND by `GATE_FULL=1`, so this unit's Definition of Done owes the
  `GATE_SELFTESTS=1` run named in AC6. That is the charter's "only for KIT work" case, and this is
  now kit work.
- `agent-cap restatement` — binds `tools/workflows/tier2-review.js` and is UNAFFECTED: the added
  sentence touches no restated cap value.
- `memory hygiene` — this spec is itself graded by check 12.

`line length` is deliberately NOT in that list, and rev-2 was wrong to claim it. Verified at HEAD:
`tools/check-line-length.sh` grades only the subjects declared in `tools/line-length-limits.txt`,
which today are `AGENTS.md` and `coding-governance-agents.template.md`. It reads none of this unit's
six files, so naming it as a leg this unit keeps green claimed a measurement that never happens. The
~100-column wrap in both documents is the writing rule from `memory/TEMPLATE-SPEC.md`, enforced by
review and not by that gate.

**This unit adds NO gate arm, deliberately, and the argument is re-made for three carriers.** For the
two DOCUMENT carriers it is unchanged: a re-read is an ACT, not an artifact, nothing in the tree
distinguishes "opened §6 and confirmed it still holds" from "never opened §6", and the only thing an
arm could grade is a §9 line CLAIMING a re-read — the liveness gap `TEMPLATE-SPEC.md` already names
for §10. A commit-level arm asserting "a rev bump touching §4 also names §2 or §6 in its §9 line"
would be worse, not better: it grades the same claim, it needs a git-replay checker where check 12 is
file-level, and it sits on top of a grammar `TOOL-aJoinedCanon-1` owns. The THIRD carrier does not
inherit that reasoning, because a pointer in a tracked program is an artifact and IS gradeable — so
it is graded, by an arm that already exists rather than by a new one, the moment S8's registry row
lands. The exemption's compensating check is recorded in §5's testing row, per charter §7.

## 8. Open questions

- **Q1 — does the procedure reach a fold performed by fan-out agents?** For a run that folds its own
  corrections, M4 reaches: M7's regrounding step 3 reads this file whole at every pass boundary. For a
  fold delegated to parallel sub-agents, only what the harness primes reaches, and
  `memory/gotchas/fold-text-is-unreviewed-surface.md` records that `tools/workflows/tier2-review.js`
  "carries exactly one sentence of fold priming today". That same record measured the parallel case on
  `dTieredTribunal`: round 1 folded by four agents, 20 fold-created findings of 29; round 2 folded by
  hand, 20 of 32 — the same absolute count, so author count is not the driver and a hand-fold does not
  escape this. **Recommendation:** land the two document carriers now, since they are where the rule
  belongs regardless, and treat the harness priming line as a separate unit the owner may decline.
  Adding it here would put a `.js` change inside a Tier-1 doc unit and make the tier wrong.
  RESOLVED (owner, 2026-09-05): WIDEN this unit to include the harness priming line. This goes
  AGAINST the recommendation immediately above, which loses and is kept verbatim as the record of
  what was weighed. The owner's reasoning carried on reach: the rule must arrive at every fold path
  in ONE landing, because a second unit may never be approved, and until it is, a delegated fold
  round keeps seeing the single sentence this record already measured as insufficient. The
  recommendation's own cost argument was weaker than it looked in two ways the fold checked. The
  tier objection reasoned from a file EXTENSION rather than from the project's tier rule, and §9
  records the re-examination that followed. The one-mechanism objection is answered in §4: the
  re-read set is one mechanism with one home and three pointers, which is what S3 already is. What
  survives of the recommendation is the cost, not the split — a version bump, a registry row and a
  self-test leg, all carried as S8, S9 and §7 rather than deferred to a unit that might not exist.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §2 · §4 · added S2b, the §8 row, after this build's own fold pass ran S2's
  four-row table against ten specs and measured it missing the §8 case. §8's fork remains OPEN.
- rev-3 · 2026-09-05 · §8 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · folded the owner's ruling on Q1:
  widen this unit to include the harness priming line, against the recommendation. §2 gained S6 to
  S9, the transitivity clause on S2b, and `Q<n>` beside `F<n>` in the §8 row after the fold measured
  the old clause selecting nothing on this spec; §3 lost the non-goal that forbade the harness
  change and gained the narrower one the harness's actual shape supports; §4 gained the design,
  the M2 one-mechanism argument and two rejected alternatives; §5 re-argued security and testing;
  §6 amended AC1, AC4 and AC6 and added AC7 to AC9; §7 gained four legs, corrected a false
  `line length` claim and re-made the no-new-arm case; §10 stopped calling the harness a
  non-candidate. TIER RE-EXAMINED, and it stays **Tier-1**. The rev-2 objection reasoned from
  the file extension, which is not the rule. Charter §8 makes a unit Tier-2 for a new write path, a
  migration, an auth/sanitization/egress surface, a shared-contract change or a cross-stream merge.
  The harness edit is a static string literal inside an existing prompt: it adds no write path, no
  migration, and no interpolation of caller data, so it widens no injection surface. The `args`
  schema and every return key are untouched, so no shared contract moves — the version bump moves a
  contract's VALUE, which is what that contract exists to carry, not its shape. One stream, one node,
  no merge. The unit stays mechanical and additive, so Tier-1 holds and the header is unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "folding a review correction back into a spec"` returned
`fold-text-is-unreviewed-surface.md [gotcha-classes]` as a direct hit, and that is the seam this unit
extends rather than a new one. That record already owns the fold as a named recurring class, already
declares "**No machine gate**, and this is a documented check rather than an unwritten one", and
already reaches a fold diff through `python tools/memory-tree/gotchas.py --for-diff` — verified live,
the command runs and prints an anchored checklist. What it does NOT hold is a SECTION closure: its
four practices are about the content a fold writes, and its nearest neighbour, "when a finding names
several carriers, edit all of them or record the refusal", covers carrier closure and not the
neighbouring sections of one document. This unit adds that half in M4 and points at the record for the
rest, so neither restates the other. The probe's other candidates were `REVIEW-PROTOCOL.md` and the
`gen_build_index.py` spec parsers, which read the header and not §4. Its third candidate,
`tools/workflows/tier2-review.js`, was filed here as fan-out shape rather than fold content — the
owner's Q1 ruling promoted it from a neighbour to this unit's third carrier, and §4 records what
reading the file at HEAD then established about what it does and does not dispatch.

Recall terms used: `python tools/memory-recall/query.py "why does the fold instruction name no
re-read set, and what decided the fold procedure's shape" --terms "fold rev bump revision log re-read
set spec audit round blocker disposition acceptance criteria scope item"`. It returned 40 hits over
909 records; the load-bearing one is
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:534`, quoted in §4, and
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md`,
which records a fold dropping the half of its own finding that made a criterion resolvable. Neither
record proposes a re-read set, so nothing prior is being re-invented.
