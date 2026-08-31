# TOOL-aProvenReuse-1 — hygiene check 12 grades §10's CONTENT, behind a declared cutoff

**Status:** SPECCED · rev-5 · 2026-08-31 · node a · Tier-2 · base 3bfc5e87 · streams tooling · order 1 · ratified 2026-08-31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aProvenReuse-1.md](../prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md) | research | TOOL-aProvenReuse-2 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round1.md) | diff-review | TOOL-aProvenReuse-2 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round2.md) | diff-review | TOOL-aProvenReuse-2 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-diff-review-round3.md) | diff-review | TOOL-aProvenReuse-2 TOOL-aProvenReuse-5 |
| [2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round1.md) | spec-audit | TOOL-aProvenReuse-2 |
| [2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aProvenReuse-1-spec-audit-round2.md) | spec-audit | TOOL-aProvenReuse-2 |

<!-- /gen:spec-records -->

## 1. Goal

Make a spec's §10 Reuse audit carry the two facts `memory/guides/BUILD-METHOD.md` M5 requires of
it — which probe was run and what it found, and the recall terms that were used — so that the
obligation stops being satisfiable by any non-empty prose. The evidence must be a TRACKED file, so
the check works in a clone the run never touched.

## 2. Scope (IN)

- **S1** — a new cutoff key `SPEC10_EVIDENCE_CUTOFF`, in THREE places and all three are required.
  A shell-side `SPEC10_EVIDENCE_CUTOFF=""` preset in `tools/memory-tree/check-memory-hygiene.sh`,
  beside its five siblings and ABOVE the conf source; a declaration in `.memory-tree.conf`; and a
  BLANK mirror in `tools/memory-tree/.memory-tree.conf.example`. **The preset is not optional, and
  rev-2 dropped it — round 2 caught that as blocker F2.** That script runs `set -u` at `:19` and
  presets `SPEC_FORMAT_CUTOFF`, `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF`, `FORK_MARK_CUTOFF` and
  `REVIEW_VERDICT_CUTOFF` at `:29-36`, above the conf source at `:62`, for exactly this reason.
  `adopt-memory-tree.sh:47-50` copies the example only when no conf exists and never back-fills one
  that does, so without the preset the gate ABORTS on an unbound variable in every adopter tree
  whose conf predates the key — a checker that fails to RUN rather than one that fails.
  Its semantics are `STREAMS_CUTOFF`'s, not
  `SPEC10_CUTOFF`'s: **blank means OFF**, guarded in the awk as `ecut != "" && fdate != "" && fdate
  >= ecut`, which is the shape `scut`, `wcut` and `fcut` already use three times in this same block.
  `SPEC10_CUTOFF` resolves blank FORWARD only because it SELECTS between two canons and must hold a
  value; this key switches an optional rule on, and an adopter who ships it blank means off.
- **S1a** — the value is `2026-09-01`, strictly AHEAD of every dated spec on every live branch, not
  this build's own date. Measured at fold time across `git for-each-ref refs/heads`: 21 Tier-2 specs
  dated `2026-08-31` sit on three sibling branches — 8 on `branch/unattended-kit-adversarial-review-6810dc`,
  7 on `branch/paired-lexer-followup-9c31a2`, 6 on `branch/gate-bar-tooling-review-020565` — and every
  one of them fails S3's arms. A cutoff at `2026-08-31` reds `memory hygiene` on `main` for three
  in-flight runs the moment either side merges, which is the build README's own "neither unit may red
  a landed spec" broken by the unit that wrote it.
- **S2** — an added assertion inside check 12's existing Tier-2 awk block in
  `tools/memory-tree/check-memory-hygiene.sh`: for a spec graded against the ten-section canon whose
  filename date is at or after `SPEC10_EVIDENCE_CUTOFF`, the §10 body must satisfy BOTH arms below.
- **S3** — the arms, matched case-insensitively as plain substrings (`index()`, never a regex, so no
  awk-dialect question arises), over TWO blobs:
  - **arm T (the recall terms)** — the whole §10 body contains `recall terms` or `--terms`.
  - **arm P (the probe result)** — the §10 body TRUNCATED AT THE FIRST TERMS MARKER contains
    `reuse_lookup`, `reuse-lookup`, `no existing seam`, `no seam fits`, or `reuse-first`. The probe
    fact must therefore be recorded BEFORE the terms.
  - **Why two blobs.** A terms list is 8-14 words of this corpus's jargon and those words routinely
    include a probe token, so a single blob let the terms line alone satisfy BOTH arms — all three
    of this build's own specs did exactly that, and the probe half could not fail. A per-LINE cut was
    the first repair and it leaked in turn: a terms list that WRAPS puts its tail on a line carrying
    no marker, and a probe token there bought the probe half. Both holes were reproduced against the
    shipped awk before either fix was written.
  - **The ordering is measured, not asserted.** Over the 264 Tier-2 post-`SPEC10_CUTOFF` specs here,
    132 record the probe token before the terms marker and 5 record it only after. All 5 are
    grandfathered, the template states the order, and the failure message names the missing fact.
- **S4** — the failure line names WHICH arm is missing and the cutoff that armed it, so the remedy
  is readable without opening the checker.
- **S5** — `tools/memory-tree/SPEC-TEMPLATE.template.md` §10 states the two required facts and names
  the cutoff key, replacing a paragraph that describes the obligation without stating what satisfies
  it. **The TEMPLATE is the authored source; `memory/TEMPLATE-SPEC.md` is a RENDER of it** and is
  regenerated by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Hand-editing the live
  copy reds the `kit/dogfood doc parity` leg, which is guarded on exactly that path and diffs the
  pair.
- **S6** — `tools/memory-tree/README.md` and the kit's `kit.toml` version move per the kit's own
  version discipline, and `bash tools/check-kit-versions.sh` is the authority on which carriers.
- **S7** — self-test arms in `tools/memory-tree/check-memory-hygiene.test.sh` covering: a
  post-cutoff spec missing arm T reds; one missing arm P reds; one satisfying both passes; a
  PRE-cutoff spec missing both passes; a Tier-1 post-cutoff spec missing both PASSES, which is the
  arm that pins N4; a §10 carrying the skeleton's REPLACE-this-paragraph sentence reds, which is what
  stops the instructional prose moving back inside the copyable fence — the fixture splices that one
  sentence rather than reading the template's bytes, so AC10 rather than this arm is what observes
  the real skeleton; and a WRAPPED terms list with a probe token on its
  continuation line reds, which is the arm that fails if the probe blob ever returns to a per-line
  cut. Arm T's fixture carries probe tokens INSIDE its terms value, so it also pins the two-blob
  split from the other side.
- **S9** — the §10 rules live ABOVE the skeleton fence in
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, not inside it. Every word that satisfies this
  predicate is a word an explanation of it must contain, so instructional prose inside the copyable
  skeleton passes the gate on its boilerplate alone and an author who never fills the section is
  never told — the could-not-fail class this unit exists to refuse, one level up.
- **S8** — the kickoff manifest's `last-audit` re-stamp. `memory/guides/SESSION-KICKOFF.md` watches
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, both edited here, and
  `kickoff-manifest ratchet` is the first leg in `tools/gate-legs.json`. Its C5 fails on a watched
  file changed with no re-stamp at or after the change, and it has a `--staged` arm, so the
  pre-commit hook catches it before the bar does.

## 3. Non-goals (OUT)

- **N1** — grading the QUALITY of what §10 records. A citation that is wrong is out of reach of any
  substring test, and pretending otherwise is the false-confidence class §7 of the charter names.
- **N2** — proving the probe actually ran. That is node-local evidence and belongs to
  `TOOL-aProvenReuse-2`; this unit's evidence is tracked and this unit claims only what tracked
  evidence can carry.
- **N3** — repairing the landed Tier-2 specs the predicate would red. 253 fail across BOTH tiers,
  but 65 of those are Tier-1 files check 12 never reaches, so the repairable population is the 188
  Tier-2 ones. The cutoff exists precisely so no landed spec goes retroactively red; a migration is
  a separate decision nobody has asked for.
- **N4** — extending the check to Tier-1 specs. `memory/TEMPLATE-SPEC.md` scopes the ten-section
  canon to Tier-2, and the existing awk cut already places the canon and the empty-body test on that
  side. This assertion rides the same cut rather than inventing a second scoping rule.
- **N5** — logging from `tools/codebase-map/reuse_lookup.py`. See the build README's third
  build-level rule.

## 4. Design

### Inventory

| Path | Change |
|---|---|
| `.memory-tree.conf` | S1/S1a — the new cutoff declaration, its value and its rationale |
| `tools/memory-tree/.memory-tree.conf.example` | S1 — the adopter-facing mirror, shipped BLANK |
| `tools/memory-tree/check-memory-hygiene.sh` | S1 the shipped preset AND the `-v ecut=` binding; S2–S4 the assertion |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S5 — §10's body. THE AUTHORED SOURCE |
| `memory/TEMPLATE-SPEC.md` | S5 — RENDERED from the row above, never hand-edited |
| `tools/memory-tree/README.md` | S6 — the check description and the kit version |
| `tools/memory-tree/check-memory-hygiene.test.sh` | S7 — five arms |
| `memory/guides/SESSION-KICKOFF.md` | S8 — the `last-audit` re-stamp |

The assertion is added after the empty-body loop, inside the Tier-2 region that begins at
`if (hdr ~ /Tier-1/) next` (`check-memory-hygiene.sh:1014`). **There is no enclosing `want ==
canon10` block to inherit a guard from.** Rev-2 claimed there was; round 2's F12 showed `want` is a
plain variable assigned at `:1019` and read only by the `wantn` ternary and the canon equality. The
arm therefore spells its whole guard explicitly: `want == canon10 && ecut != "" && fdate != "" &&
fdate >= ecut`. Keeping the `want == canon10` term is still worth its bytes — it is the canon
check 12 CHOSE by filename date, so the evidence arm can never grade a spec the section canon did
not. What it cannot do is stand in for the cutoff test, which is a separate conjunct.

The §10 body is collected by walking the same `body[]` array the empty-body loop walks, setting a
flag on the `## 10. Reuse audit` heading and clearing it on any later `## ` heading. §10 is canon
LAST, so in practice the flag runs to end of body; the clear-on-heading is written anyway because a
canon that grows a §11 must not silently widen this predicate's reach.

### Alternatives rejected

- **A new checker script.** Rejected: check 12 already reads, unfences and section-splits every
  spec in the tree, in one awk pass that replaced roughly thirteen forks per spec. A second reader
  of the same files would be a second answer to one question and would pay the walk twice.
- **A regex predicate.** Rejected: this file's own header records that interval expressions are
  spelled out character by character because a build that does not honour `{8}` would demand those
  literal bytes. `index()` on a `tolower()`ed body has no dialect surface at all.
- **Requiring a specific line grammar** (`**Reuse:** …`, in the shape of check 21's record
  bindings). Rejected: 156 landed specs already spell arm T as `Recall terms used:` and would have
  to be rewritten to match a new grammar they predate, and the grammar buys nothing a substring does
  not — nothing downstream PARSES §10, it is read by people and by M7's regrounding step.
- **Requiring arm P only.** Rejected: arm T is the arm with a named downstream consumer. M7 step 5
  says to re-run the recall probe with the terms recorded in §10, and that step is inert without it.
- **Blank resolving FORWARD, as `SPEC10_CUTOFF` does.** Rejected at round 1 (finding 26): that key
  must hold a value because it SELECTS between two canons, so blank-means-off would leave check 12
  with no canon to grade against. This key switches an optional rule on, which is
  `STREAMS_CUTOFF`'s situation exactly, and copying the wrong sibling's guard would arm a rule in
  every adopter tree that shipped the `.example` unedited.
- **Setting the cutoff to this build's date.** Rejected at round 1 (finding 21), measured: 21 Tier-2
  specs on three live sibling branches would red on merge. See S1a.

### The tier, and what it decides

Both units of this build are **Tier-2**, and the build README's earlier "authored by this run at
Tier 1" was wrong. The tier is load-bearing rather than bookkeeping: `check-memory-hygiene.sh` runs
`if (hdr ~ /Tier-1/) next` BEFORE the section canon and every body assertion, so a Tier-1 spec is
never reached by S2's arms at all. Under the Tier-1 reading this unit's own predicate would grade a
population of zero and AC4 would pass vacuously. Tier-2 is also what the manifest's tier rule
assigns — each unit changes a kit's contract, and the pair is cross-kit.

### Migration

None, and the dogfooding claim an earlier revision made here is WITHDRAWN. S1a puts the cutoff at
`2026-09-01`, which is strictly after this build's own specs, so **these two specs are NOT graded by
the predicate they introduce**. That is the cost of not redding three sibling branches, and it is
paid deliberately. The first file the predicate grades is the next Tier-2 spec anybody writes on or
after `2026-09-01`. Because the corpus therefore exercises NEITHER arm on day one, AC5 and S7 carry
the whole liveness burden — the same trade `STREAMS_CUTOFF`'s own declaration records, and for the
same reason.

### Rollout

One commit. The check is inert on every existing file by construction, so there is no dark-launch
question and nothing to flip.

## 5. Production-readiness checklist

- **Security** — N/A. No new write path, no new input from outside the repo; the checker reads
  tracked files it already reads.
- **Performance** — one extra pass over an already-loaded `body[]` array per Tier-2 spec, inside an
  awk invocation that already runs. No new process, no new file read. `memory hygiene` is an
  unguarded leg, so the cost lands on every bar and is measured in S7's own run rather than asserted.
- **Error states** — a blank `SPEC10_EVIDENCE_CUTOFF` means OFF, guarded by an explicit `ecut != ""`
  test rather than by a date comparison. That guard is not optional: an empty string compares
  EARLIER than every date, so `fdate >= ""` is true for every spec and a blank key without the
  non-empty test would arm the predicate over the whole corpus — the one outcome the cutoff
  mechanism exists to prevent. This is `STREAMS_CUTOFF`'s shape, at `:846`, and not
  `SPEC10_CUTOFF`'s forward resolution, for the reason §4 Alternatives records.
- **Observability** — the failure line names the file, the missing arm and the cutoff.
- **Testing** — S7.
- **Migration/rollback** — revert the commit; nothing is generated and nothing is stored.

## 6. Acceptance criteria

- **AC1** — a Tier-2 spec dated at or after the cutoff whose §10 omits arm T makes
  `bash tools/memory-tree/check-memory-hygiene.sh` exit non-zero, and the failure text names
  `§10` and the missing arm. Observed by staging the break, not asserted.
- **AC2** — the same, for a spec omitting arm P: `bash tools/memory-tree/check-memory-hygiene.sh`
  exits non-zero and its text names the probe-result arm.
- **AC3** — a spec dated BEFORE the cutoff whose §10 omits both arms leaves
  `bash tools/memory-tree/check-memory-hygiene.sh` at exit 0, proving the grandfathering is real
  rather than a comment.
- **AC3a** — a **Tier-1** spec dated at or after the cutoff whose §10 omits both arms also leaves it
  at exit 0. This is N4's observable: `if (hdr ~ /Tier-1/) next` fires before the assertion, and
  without this arm nothing distinguishes "N4 holds" from "no Tier-1 fixture was tried".
- **AC4** — on the tree as it stands, `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with
  the cutoff at its declared `2026-09-01`. Zero hits, because every tracked spec predates it.
- **AC5** — with `SPEC10_EVIDENCE_CUTOFF` temporarily set to `2026-08-04`, the same command reds and
  names the count RE-DERIVED at build time over the Tier-2 post-`2026-08-04` specs failing either
  arm. Measured 2026-08-31 that count is **188** against a population of 264, and the figure is
  evidence for the criterion rather than the criterion. This is the liveness assertion for AC4: a
  predicate that reds nothing at its declared cutoff must be shown capable of redding. Do not reach
  for **253** — that is the ALL-TIERS failure count over the 348 §10-bearing specs, and 65 of its
  members are Tier-1 files the arm never reaches. A criterion pinned to the wrong population fails a
  correct implementation.
- **AC5a** — the cutoff hazard is re-measured across `git for-each-ref refs/heads`, not just the
  worktree index, immediately before the value is pinned, and the declared value is strictly after
  every dated spec the enumeration returns.
- **AC6** — `bash tools/memory-tree/check-memory-hygiene.test.sh` passes with S7's arms present, and
  the assertion count the suite reports rises. Measured: 254 before this unit, 262 after its first
  five arms, and higher again once the skeleton and wrapped-terms arms landed.
- **AC10** — the copyable skeleton's own §10 body, fed to the predicate lifted from
  `tools/memory-tree/check-memory-hygiene.sh`, scores `hasT=0 hasP=0`. Observed directly against the
  shipped awk, not inferred from a fixture passing.
- **AC11** — a §10 whose terms list WRAPS with `reuse_lookup` on the continuation line scores
  `hasT=1 hasP=0`. Observed the same way, and it is the case the per-line repair got wrong.
- **AC7** — `bash tools/check-kit-versions.sh` exits 0 after the version move.
- **AC8** — `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, and the RENDERED
  `memory/TEMPLATE-SPEC.md` §10 names both required facts and the `SPEC10_EVIDENCE_CUTOFF` key.
- **AC9** — `bash skills/session-kickoff/manifest-check.sh` exits 0 after S8's re-stamp.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the full bar. Four of its legs are named here because this
unit reaches each of them and a builder should not discover the pairing from a failing run:
`kickoff-manifest ratchet` (S8), `memory hygiene` (unguarded), `memory-hygiene self-test` and
`kit/dogfood doc parity` (guarded on `memory/TEMPLATE-SPEC.md`, which S5 renders).
`bash tools/check-kit-versions.sh` for AC7, `bash skills/session-kickoff/manifest-check.sh` for AC9.
What no gate here checks: whether the two arms are the RIGHT two facts to demand — that is a design
question the spec audit owns, not a predicate. Nothing checks arm content either, which is N1.

## 8. Open questions

- **Q1 — should arm P accept `reuse-first` as a satisfying token?** It admits a §10 that names a
  waiver instead of a finding. **RESOLVED (agent, 2026-08-31, delegated):** yes. The kit's own Skill
  asks a waived run to NAME the waiver in §10 and has no way to make it, so accepting the token is
  what converts that request into a record. Rejecting it would instead make `reuse-first` effectively
  unwaivable for any post-cutoff spec, which is a rule change M3 veto 2 puts outside this run's
  authority.
- **Q2 — where does the cutoff sit?** **RESOLVED (agent, 2026-08-31, delegated):** `2026-09-01`,
  strictly ahead of every dated spec on every live branch. **This SUPERSEDES an earlier resolution of
  this same fork reading "this build's date, 2026-08-31", whose reasoning was that the landing day
  and the build day were identical.** That was sound about this branch and wrong about the fleet:
  round 1's blocker 21 enumerated 21 Tier-2 specs dated `2026-08-31` on three other live branches,
  every one of which fails the predicate, so a cutoff on this build's date reds `memory hygiene` on
  `main` for three in-flight runs the moment either side merges. Round 2's blocker F1 found the stale
  resolution still standing under the corrected §2 and §4 — a ratification vouching for the option
  §4 records as rejected. `UNITS_REGION_CUTOFF`'s declaration warns that a cutoff set after the
  landing re-opens the gap for the commits in between; that cost is one day, and it is smaller than
  three red branches.

## 9. Revision log

- rev-1 · 2026-08-31 · authored by the aProvenReuse run.
- rev-5 · 2026-08-31 · closing-diff-review round-3 fold, at the loop's NON-CONVERGENT exit. Round 3's
  blocker: the fold that replaced the per-line terms cut with a whole-section truncation left the
  spec template still describing the per-line behaviour, and three carriers claimed the template
  stated an ORDER it never stated. The template now states the order as a rule, says why the
  truncation exists, and DECLARES the one shape it cannot see. The failure message names the order
  when the probe arm is the missing one. S7's skeleton-arm claim was overstated: the fixture splices
  one sentence rather than reading the template's bytes, and AC10 is what observes the real skeleton.
- rev-4 · 2026-08-31 · closing-diff-review round-2 fold. Round 2 found this spec had NOT been
  folded after round 1 at all: it still specified a single-blob scan and five self-test arms while
  the code had neither. S3 now states the two-blob split and the measurement behind its ordering, S7
  names all seven arms, S9 records why the §10 rules sit above the skeleton fence, and AC10 and AC11
  are the two observations that were made against the shipped awk but never written down.
- rev-3 · 2026-08-31 · round-2 spec-audit fold, at the loop's NON-CONVERGENT exit. Blocker F2
  restored the shell-side `SPEC10_EVIDENCE_CUTOFF=""` preset the rev-2 edit had dropped; under
  `set -u` its absence aborts the gate in every adopter whose conf predates the key. Blocker F1
  superseded §8 Q2, which still ratified the cutoff §4 had already rejected. F12 corrected §4's
  placement paragraph, which described an enclosing block that does not exist. F8 restated AC5 as an
  observation with its measurement as evidence, F10 gave N3 its population, F7 dropped the
  conditional S5a, and F14 moved this header OPEN -> SPECCED to agree with the README roster.
- rev-2 · 2026-08-31 · round-1 spec-audit fold. Blocker 21 moved the cutoff to `2026-09-01` and
  withdrew the self-grading claim; findings 3 and 33 made the template the authored source and named
  the parity leg; findings 1 and 25 corrected AC5 from 253 to 188 and gave it its population;
  finding 26 replaced the forward-resolution guard with `STREAMS_CUTOFF`'s blank-means-off shape;
  finding 23 added S8, the kickoff-manifest re-stamp; findings 6 and 41 settled the tier at Tier-2
  against the build README. AC3a and AC5a are new observables the fold created.

## 10. Reuse audit

The seam this unit wires through is `tools/memory-tree/check-memory-hygiene.sh` check 12 — it
already reads, unfences and section-splits every spec in the tree, already grades §10's presence and
emptiness, and already carries the four-cutoff declaration idiom this unit adds a fifth member to.
No new script, no second reader.

`python tools/codebase-map/reuse_lookup.py "checking that a spec records a reuse audit before code
is written"` returned `check-memory-hygiene.sh`'s check family and the `memory-tree-hygiene`
affordance seam, plus `row_grammar.py`'s `cmd_check`. The row-grammar seam was inspected and
REJECTED: it grades table ROWS against a declared grammar, and §10 is free prose with 156 landed
files already spelling arm T their own way.

Recall terms used: `reuse-first reuse audit spec section 10 seam recall probe terms directive waiver
silent unchecked machine-checked prose`. That query surfaced `dFramedEntrypoint`'s round-1 finding
RECALL-1, which reproduced this defect on an eight-spec build, and `TOOL-dPromptedSeam-1`'s
observation that `check-memory-hygiene.sh:744` is already "the forcing function in as many words" —
both of which are evidence that the seam named above is the one the corpus already expects to hold
this rule.

Where a hit was STALE: none. The two claims about check 12's current behaviour above were re-read
against source at `tools/memory-tree/check-memory-hygiene.sh:1015-1047` rather than taken from the
records.
