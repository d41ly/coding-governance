**Serves:** spec-audit TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20

# dDerivedDocket — spec audit of topic group G3, ask-driven unattended runs, round 1

*Node `d`, 2026-09-14. A Tier-2 adversarial pass over the six specs of topic group G3. They are the
ask envelope, READY and the new-build scaffold (unit 15); the driver's ask-awareness (16); the
`asks-disposed` Definition-of-Done item and its freeze (17); the leg's second opinions (18);
authority grants (19); and the unattended carriers with the two-key refusal (20). Four primed finder
lenses ran, then a skeptic stage prompted to REFUTE each finding in five batches, then this
synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md` (sections 19,
"19 fixes", 20 and 21.4 U16 most of all), the owner mandate
`memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`, and
the spec brief's roster and edge tables. Sibling specs outside G3 were read wherever an edge or an
interface named them: units 1, 2, 3, 4, 6, 7, 22, 34 and 35, because contradiction between specs is
in scope. The G1 and G2 round-1 reports were read too, because three of their entries overlap this
group's. Every high below was re-checked against source at `abac6d59` before it was written down
here, and the sites read are named in each entry. H4's premise was also re-measured against this
repository's own refs today.*

**Round: 1.** Range at base `abac6d59`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md@dd47ecb6a242c91cd1c4d59d52ba7c7b2d7db707`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md@2ec36fa404f1b19fa2eebed738e1ebf7b8d4afdc`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-17.md@dd6f2277ae953f8dda0ef2fb225460843ee7bc96`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md@ff90db54ab2bf9a81a9d7d7504f58f280e1e0808`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md@8580ad069903832de9d70769b8bedf91493a7d57`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-20.md@87a8e8f1584cef0ce0bdab5595209cc0b1215e35`

## Verdict: CLEAN WITH FIXES

No confirmed finding is adjudicated a blocker, so the verdict is CLEAN WITH FIXES by the blocker
count. That does not mean the set is close to done. Eleven HIGH defects stand, carried by 19
confirmed findings. Each is a defect in a document this round read, so the disposition
`memory/guides/BUILD-METHOD.md` M4 prescribes is FOLD for all of them. None of them, folded, needs a
mechanism that no spec in the set carries, and that is half of the line this build's reports draw
for a blocker. H1 and H2 come closest on the other half. As specified, the first real `ASKS_CMD`
call after unit 35 arms gov is a parse refusal. Every mandated preflight then refuses as a DEAD
PROBE, and every close with a non-empty scope is UNMET on T2, this build's own close included. Their
fold is a clause in unit 15 and one stdout rule in unit 7, not a missing mechanism.

The highs cluster in three places.

- **The seam between the `--tsv` producer and its two consumers cannot carry a real row** (H1, H2,
  H3). The consumer suites stub `ASKS_CMD`, so every fixture stays green.
- **The authority and scope properties the ask path exists for are not delivered where they are
  claimed** (H5, H6, H7). In gov the D12-a route prints a push instruction instead of the scaffold
  recipe. The driver pins a run-authored mandate that the leg refuses only after the build. And the
  owner's own D12-j channel reds the leg permanently.
- **Two probes cannot move in gov** (H4, H8). The live-build set cannot contain an in-flight run,
  and the freeze-presence arm grades a phase that gov's lander mode never records.

H9 and H10 are units that cannot pass as written. H11 is the allow-list of the one surface that
executes a filer's bytes.

Four folds change a ratified design point or the reach of a ruling. Each should be decided rather
than folded silently, and each takes a §9 line.

- H4 replaces the mechanism of design fix F5.
- H7, together with M1, restates fix F4's "T4's range is `m-base..HEAD`" for in-place landing.
- H8 picks which of units 18 and 22 owns the derived-LANDED population. It must follow whatever
  G1's B2 fold decides for rotation, or the same population gets folded twice, two ways.
- M8 either widens the scope of owner ruling TOOL-aPromptedMandate-4 or records that its premise
  does not reach scaffolded builds. The widening is the owner's call.

The folded text is unreviewed surface (`memory/gotchas/fold-text-is-unreviewed-surface.md`). M4's
loop re-arms only on a blocker count, so re-reading the fold is a choice rather than an obligation.
This report recommends it for units 15, 16, 17 and 19, whose folds are the largest.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

Every counter that could make this run incomplete is zero, so the finding set is complete for what
the four lenses were primed to hunt. That is not a claim that G3 holds no other defect. It is a claim
that nothing was lost between the lenses and this page. The pipeline's duplicate count of 0 comes
from its own exact-match dedupe. On reading, five groups of confirmed findings each describe one
defect from several lenses: 8/50, 10/35, 15/36/60, 22/34 and 25/38/66/71. Each group is folded into
one entry below, and every count on this page stays per finding id.

## Review shape

Raw 78, confirmed 50, refuted 28, unverified 0, precision 0.64. The 50 confirmed ids collapse to 42
distinct defects.

| Severity | Finding ids | Distinct defects |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 19 | 11 |
| MEDIUM | 25 | 25 |
| LOW | 6 | 6 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 and G2
reports used, so the three groups' counts compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert, or which refuses a state an owner ruling sanctions, while its suite reads
  green. In each case the fold is local to one or two specs, or needs one decision.
- MEDIUM covers three things: a contradiction between specs with a bounded consequence, a
  declaration or edge a spec owes, and a rule whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, three findings move up and three move down.

- Up, from medium to HIGH: 8, which is H10 together with 50; 10, which is H6 together with 35; and
  71, which is H7 together with 25, 38 and 66.
- Down, from high to MEDIUM: 1 and 16, which are the criterion-gap class that G1 and G2 put at
  MEDIUM. 16's wrong direction is also loud, an UNMET at first use rather than a silent pass.
- Down, from high to MEDIUM: 53, because it depends on a slot-body shape the spec leaves to the
  implementer and reds loudly at the owner's push. H10's failure, by contrast, is certain.

Precision at 0.64 sits above the ~0.5 floor that `AGENTS.md` section 8 sets. The dominant class is
the one G1 and G2 named, `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`.
Ids 1, 4, 5, 6, 9, 12, 13, 16, 18, 21, 23, 24, 26, 28, 29, 30 and 43 are that class outright, which
is 17 of the 50, and ids 2 and 8 each have it as one half. Six of those criteria carry a `Red when:`
that cannot turn them red: 1, 4, 5, 23, 29 and 43. This group's lenses were primed with the gotcha's
skip test, as G1 asked, and the class still survived spec authoring at about the same rate.

The second cluster is new to G3: a consumer graded against a stand-in for its producer or its
configuration. Units 16 and 17 fake `ASKS_CMD` in every fixture (H1, H2, M2). AC1 and AC2 of unit
16 run under the kit default `ANCHOR_SCOPE`, while gov declares `published` (H5). Unit 18's AC7 uses
a primary-mode record, while gov runs in-place (H8). AC14 keeps a foreign run's record in the same
tree as the preflight (H4). Each fixture is green over a shape the real system never produces.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---|---|
| 51 | HIGH | H1 | 15 | §4 The machine projection (S6); §6 AC7 |
| 3 | HIGH | H2 | 15 | §4 The machine projection |
| 15 | HIGH | H3 | 17 | §4 Data model; §6 |
| 36 | HIGH | H3 | 17 | §4 Data model and The terms, T0 and T2; §6 AC3 |
| 60 | HIGH | H3 | 17 | §4 Data model |
| 55 | HIGH | H4 | 16 | §4 The live-build set (S5); §6 AC14 |
| 57 | HIGH | H5 | 16 | §2 S6; §4 Ids-shaped invocations |
| 10 | HIGH | H6 | 16 | §2 S2, the absent item; §6 |
| 35 | HIGH | H6 | 16 | §2 S2 and S3, against §1 and unit 18 S5 |
| 25 | HIGH | H7 | 19 | §2 S4 third arm; §4 The cross-run arm; §6 AC6 |
| 38 | HIGH | H7 | 19 | §4 The cross-run arm, against unit 2 S1 |
| 66 | HIGH | H7 | 19 | §4 The cross-run arm |
| 71 | HIGH | H7 | 19 | §4 The cross-run arm; §6 AC6; §3 Edges |
| 22 | HIGH | H8 | 18 | §3 fourth bullet; §2 S4 |
| 34 | HIGH | H8 | 18 | §3, against unit 22 §4 and unit 3 S1 |
| 37 | HIGH | H9 | 16, 17, 18 | AC13, AC12 and AC10; §3 Edges |
| 8 | HIGH | H10 | 15 | §2 S8; §4 The scaffold; §6 AC10 |
| 50 | HIGH | H10 | 15 | §4 The scaffold (S8) |
| 2 | HIGH | H11 | 15 | §2 S7; §4 The probe runner; §6 AC9 |
| 19 | MEDIUM | M1 | 17 | §4 The terms, T4 |
| 44 | MEDIUM | M2 | 16 | §2 S1; §4 The ASKS_CMD contract |
| 75 | MEDIUM | M3 | 16 | §2 S7 and S8; §6 AC7 |
| 40 | MEDIUM | M4 | 20 | §2 S3 and S4, against unit 18 S3 |
| 41 | MEDIUM | M5 | 19, 20 | unit 19 §5 and AC1; unit 20 §4 |
| 42 | MEDIUM | M6 | 20 | §3 Edges and §8 F1, against unit 34 AC8 |
| 68 | MEDIUM | M7 | 20 | §2 S1; §4 The two-key refusal |
| 73 | MEDIUM | M8 | 16 | §2 and §3, the absent item |
| 77 | MEDIUM | M9 | 18 | §1 Goal; §2 S4; §3 |
| 43 | MEDIUM | M10 | 16 | §6 AC14 |
| 53 | MEDIUM | M11 | 15 | §4 The scaffold, the generated slot bodies |
| 61 | MEDIUM | M12 | 17 | §6 AC8 |
| 62 | MEDIUM | M13 | 17 | §6 AC9 |
| 1 | MEDIUM | M14 | 15 | §2 S5 and S9; §6 AC5, AC6 and AC12 |
| 4 | MEDIUM | M15 | 15 | §6 AC7 |
| 5 | MEDIUM | M16 | 15 | §6 AC1 |
| 6 | MEDIUM | M17 | 15 | §2 S4; §6 AC4 |
| 12 | MEDIUM | M18 | 16 | §2 S8; §4 Plan, next and rank; §6 AC9 |
| 13 | MEDIUM | M19 | 16 | §2 S5; §4 The ASKS_CMD contract |
| 16 | MEDIUM | M20 | 17 | §6 AC4 to AC6 |
| 18 | MEDIUM | M21 | 17 | §4 The terms and the F3 hardening; §6 |
| 23 | MEDIUM | M22 | 18 | §6 AC4 |
| 26 | MEDIUM | M23 | 19 | §2 S7; §4 Budgets; §6 AC9 |
| 29 | MEDIUM | M24 | 20 | §6 AC1; §7 |
| 30 | MEDIUM | M25 | 20 | §2 S3 and S4; §6 AC3 and AC4 |
| 9 | LOW | L1 | 15 | §2 S2; §4 The probe runner |
| 21 | LOW | L2 | 17 | §2 S3; §6 AC8 |
| 24 | LOW | L3 | 18 | §2 S4; §6 AC7 |
| 28 | LOW | L4 | 19 | §2 S2 and S3; §6 AC2 and AC3 |
| 49 | LOW | L5 | 20 | §2 S7, the M9 row |
| 69 | LOW | L6 | 20 | §6 AC4 |

Every spec path below is `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-<n>.md`,
named by its unit number.

## Blockers

None. The two candidates nearest the line were weighed and put at HIGH. H1 with H2 would leave the
ask path refusing every mandated run once armed, but its fold is local spec text. H4 needs a
decision, but a run still proceeds under it, and the harm is a possible double claim rather than an
outcome the build cannot reach.

## High

### H1 — `--tsv` does not own its stdout, so every real `ASKS_CMD` call is a parse refusal (51)

**Where.** Unit 15 §4 "The machine projection" (S6) and §6 AC7. These are read against unit 16 §4
"The ASKS_CMD contract", unit 17 §4 "Data model", and unit 7 §2 S11 and S12.

**Defect.** §4 specifies `--tsv` as exactly eleven-field rows plus one `examined` line. It never says
the mode owns stdout. `--asks` needs `collect()` for the spec index and the build statuses (unit 7
S1). At BASE, `collect()` prints `build-index: N header(s) tolerated by waiver` to stdout
"UNCONDITIONALLY, including at zero", by its ratified F2 (`tools/memory-tree/gen_build_index.py:819-822`,
re-read for this report). Unit 7 S11 adds a liveness line "on every run" and names no stream. The
consumers refuse anything else. Unit 16 §4 says "Anything else is a parse refusal rather than a row",
and unit 17 §4 refuses any line whose first field is not `ask`.

**Impact.** Every real `ASKS_CMD` call reads as a DEAD PROBE. Once unit 35 sets gov's `ASKS_CMD`,
preflight refuses every README carrying `asks:`, and T2 is UNMET on every close with a non-empty
scope. That includes this build's own close, which unit 35 S9 grades "T3 over F" with `ASKS_CMD`
set. Every fixture stays green, because unit 16 AC6 and unit 17 AC3 fake `ASKS_CMD`. This is the TSV
twin of G2's M4, whose fix text reads "Under `--asks`, stdout carries only the table or the JSON".
That wording does not name `--tsv`.

**Fix.** State one rule in unit 7, which owns the `--asks` print path: under `--asks`, every output
mode, `--tsv` included, writes only its value to stdout, and the waiver line and the liveness line
go to stderr. State the same property in unit 15 §4 for `--tsv`. Make AC7 assert that stdout is
exactly n+1 lines. Fold it with G2's M4 as one rule, so the two groups' folds cannot disagree.

**Left-shift.** A unit 15 selftest arm that runs `--asks --tsv` over a fixture holding one
tolerated-by-waiver header, and asserts the line count of the whole of stdout. Stage it RED by
re-adding the print. The consumer-side gate is class item 1 below.

### H2 — the eleven fields' values are unpinned, and an empty field collapses under the kit's read (3)

**Where.** Unit 15 §4 "The machine projection". It is read against unit 6 §4 "The fold" and "Decided
by", and unit 17 §3 Edges and §4 terms T4 and T5.

**Defect.** §4 pins a format for `missing`, `holds` and `closers` only, each `-` when empty. The
other fields are open:

- `decided-by` is empty for an OPEN ask, by unit 6's own rule ("R7 nothing"). It names "the closing
  evidence" in the singular, although `closing(A)` is a set that can hold a spec and a `by` sha.
- `sev` has no value for an unlabelled ask, and `grant` and `home` have no stated value set.
- `closers` does not say whether it lists CLOSED specs, which T5 needs to read.

The kit reads TAB records with `IFS=$'\t' read` (`tools/unattended/lib-unattended.sh:168`,
`tools/unattended/unattended.sh:1872`). Tab is IFS whitespace, so a run of tabs collapses, as
`memory/gotchas/empty-field-collapses-unless-it-is-last.md` records.

**Impact.** A correct row for an OPEN, unlabelled ask carries two empty fields in its middle. Read
the kit's way it has nine fields, which is unit 17's parse refusal: a DEAD PROBE on the commonest row.
T4 needs a sha from `decided-by` and finds none when the producer names a spec there. T5 cannot tell
whether a CLOSED spec of this build closed the ask. Both verdicts depend on a choice nobody pinned.
Whether units 16 and 17 parse with `read` or with `awk -F'\t'` is itself unpinned, so the collapse is
likely rather than certain. The unpinned values are certain.

**Fix.** Specify each field's value set, and a non-empty placeholder `-` for every field that can be
empty. Make `decided-by` a comma list of every member of `closing(A)` or `declining(A)`, rather than
one member picked (`memory/gotchas/one-value-field-records-a-mixed-outcome.md`). State whether
`closers` carries CLOSED specs, and with what token. Pin all of it with an AC7 fixture holding an
unlabelled OPEN ask and an ask closed by two records.

**Left-shift.** Class item 1 below: a consumer arm that parses the real producer's output for exactly
this fixture.

### H3 — F is defined by the witness it scopes (15, 36, 60)

**Where.** Unit 17 §4 "Data model", the terms table (T0's second row, T2, T3) and "The freeze"; §2
S3; and §6, which has no arm over F. These are read against unit 16 §4 "The ASKS_CMD contract" and
unit 35 §2 S9 and §4 "This build's own close".

**Defect.** F is "every ask whose `home` field in the witness is this build's slug". The witness is
"one invocation of `ASKS_CMD` over M ∪ F". The definition is circular: F must exist before the call
that defines it. The one declared invocation (unit 16 §4) passes ids through `--ready`. Unit 15 never
says `--tsv` composes with unit 7's `--build` or `--all`. T0's second row, "F empty", cannot be
decided before the witness runs. If F is read back from the witness, T2's count check cannot notice
a witness that omits an F ask, because the omission shrinks F to match.

**Impact.** T3's second clause, the freeze's F population and S3's "whose build filed asks" have no
implementable input. A producer that drops a self-filed, undisposed ask lets T3 pass vacuously,
which is `memory/gotchas/inputs-inside-the-subjects-reach.md`. No criterion stages an F ask, so the
break is never seen. This build is the first real subject. It carries no `asks:` fact, and unit 35
S9 grades its own close as T3 over F.

**Fix.** Enumerate F before the call and independently of it. Use the P5 line matcher unit 16 puts
in `tools/unattended/lib-unattended.sh`, matching `^- <ID> · filed ` in this build's own
`BACKLOG.md` at HEAD; filing is not status, as unit 16 S7 already argues for `unit` asks. Pass
M ∪ F through `--ready`, and compare T2's counts against that set. Add three ACs:

- an F ask with no disposition reds T3;
- a witness that omits an F ask reds T2 as a DEAD PROBE naming it;
- `--landed` on a no-mandate record whose build filed an ask writes the freeze.

**Left-shift.** Those arms. The class is item 3 below.

### H4 — the live-build set cannot contain an in-flight run (55)

**Where.** Unit 16 §4 "The live-build set" (S5) and §6 AC14. Also unit 15 §4 READY, the `stale:`
rule, and §8 F2. These are read against design "19 fixes" F5.

**Defect.** The driver derives the set from every tracked `memory/builds/*/RUN.md` in the preflighting
tree. A live run's record exists only on that run's own branch. `check_branch` refuses a run on the
default branch (`tools/unattended/unattended.sh:1086-1090`), and preflight stages the record on the
run branch. A foreign run's record reaches the preflighting tree only after that run lands.

Re-measured for this report: `memory/builds/dDerivedDocket/` is absent from both local `main` and
`origin/main` while this run is live. A preflight anywhere else today would therefore not list this
build as live. By construction, the set derived this way holds the landed-but-unrotated records and
little else. Design F5's premise, that "a foreign live spec grades `no` only when its build has a
non-terminal RUN.md", assumed that record is visible where READY is evaluated.

**Impact.** Take a foreign build whose specs are already on main while a second run on it is in
flight. It is missing from the set, so R2 admits its SPECCED closing spec as `stale:` and grades the
ask `yes`. Two builds then answer one ask. That is design K7's measured failure, the one
TOOL-aProvenReuse-4 records, and exactly what AC6 and AC14 exist to stop. §4's "conservative
direction" holds for the landed-but-unrotated case only. AC14's fixture keeps the foreign `RUN.md` in
the same tree, so it reads green. Unit 15 calls omitting `--live-builds` the conservative reading,
and the driver chooses the other reading with an input that cannot be complete.

**Fix.** This needs a decision, because it replaces F5's mechanism. Choose one:

- (a) Observe live runs where they live: read `RUN.md` at each advertised run-branch tip under
  `ANCHOR_SCOPE=published`, bounded, and state what a branch nobody pushed cannot show.
- (b) Pass no `--live-builds`, so every foreign live spec counts as a claim, and state the residual:
  a stale claim costs an ask this run could have taken, and the ask is parked for the owner.

Either way, add an AC whose foreign `RUN.md` exists only on an unmerged branch. The choice changes
unit 15 §8 F2's and unit 16 §8 F2's resolutions, so each takes a §9 line. M9 depends on the answer.

**Left-shift.** That AC. The classes are items 3 and 4 below.

### H5 — in gov, the ids and filing-home refusals never reach code 6 (57)

**Where.** Unit 16 §2 S6, §4 "Ids-shaped invocations", and §6 AC1 and AC2. These are read against
`.unattended.conf:110`, `resolve_base` (`tools/unattended/unattended.sh:887-917`),
`emit_branch_fail` (`:859-866`) and `verb_preflight` (`:2610-2613`).

**Defect.** Code 6 is raised inside `check_authorization`, and `verb_preflight` reaches that
function only after `trusted_base` succeeds. Gov sets `ANCHOR_SCOPE="published"`. For an id value or
a filing-home slug, the README is absent at the merge-base, so `resolve_base` widens to the second
anchor (`:903-915`). An unpushed branch then refuses with fail 32, "push the branch first" (`:863`).
The filing-home test reads "the folder at BASE", and at that point there is no BASE to read.

Re-checked for this report: a value carrying whitespace, which §4 also routes to code 6, is refused
earlier still. `check_slug` answers it with fail 1, "the slug is not a build-folder name"
(`:1060-1070`), before any anchor work.

**Impact.** In gov, `/unattended <ids>` and `/unattended <filing-home>` print a push instruction or a
slug-grammar refusal, never the scaffold recipe. Owner ruling D12-a says each "print the E3 recipe
and stop without writing anything". Following the printed instruction writes to the remote. Unit
20 S5's Skill relays "the scaffold recipe its refusal prints", and fail 32 carries none. AC1 and AC2
run under the kit default `ANCHOR_SCOPE`, so both read green.

**Fix.** Run the id-shape test before `check_slug` and before any anchor work, since it needs no
tree. Run the filing-home test against the first anchor's merge-base, `merge-base(ASHA, HEAD)`,
before `trusted_base`. Add AC1 and AC2 arms under `ANCHOR_SCOPE=published` with an unpushed branch,
and one with a two-token value.

**Left-shift.** Those arms. The class is item 4 below.

### H6 — preflight pins a mandate in the modes where the run wrote the README (10, 35)

**Where.** Unit 16 §2 S2 to S4, against its own §1 Goal. Also unit 18 §2 S5 and AC8, unit 19 §2 S2
and AC2, and `SECOND_ANCHOR_MODES="prompt recipe"` (`tools/unattended/unattended.sh:497`).

**Defect.** S3 pins `asks:`, `asks-ready:` and `m-base:` for any README carrying `asks:`, whatever
the resolved mode. The only related refusal, in S2, is a blank `ASKS_CMD`. `prompt` and `recipe` are
second-anchor modes, so their README can be run-written. Unit 18 S5 and AC8 red a record carrying
`asks:` with mode `prompt`, citing D12-a's single authorization path. Unit 19 S2 refuses the sibling
`may:` at preflight for exactly this reason.

**Impact.** A run on the prompt path can write `asks:` into the README it authored at the second
anchor. Preflight pins that self-chosen mandate, the run builds against it, and unit 17's F3
hardening keys on grades from it. The violation surfaces when check 19 reds at the post-build bar,
after the whole build. §4's "a run cannot satisfy P5 by construction" still holds, because P5 reads
rows at `m-base:`. But choosing WHICH filed asks is exactly what D12-a took from the run, and the
Goal names that property.

**Fix.** Add to S2 a preflight refusal, under a new driver code and writing nothing, for any README
carrying `asks:` whose resolved mode is not `slug`. Add an AC with a `prompt`-mode fixture and one in
`recipe` mode, mirroring unit 19 S2 and AC2. L4 asks for the same `recipe` arm there.

**Left-shift.** Those arms. The class is item 5 below: a leg arm refusing a record shape owes a
driver twin refusing it at preflight, or a stated reason why not.

### H7 — the cross-run arm walks every default-branch commit since BASE (25, 38, 66, 71)

**Where.** Unit 19 §2 S4's third arm, §4 "The cross-run arm", §6 AC6 and §3 Edges, which has no edge
to unit 2. These are read against unit 2 §2 S1 and S3 and §4, unit 3 §2 S1, the witness write at
`tools/unattended/unattended.sh:2375-2376`, and the leg's population at
`tools/unattended/check-unattended.sh:717-726`.

**Defect.** The arm walks `BASE..witness` for a terminal record and `BASE..HEAD` for a live one. It
reds any commit that adds or changes a `may:` line in any `memory/builds/*/README.md`. §4 says it
"does not see a grant typed by a person on the default branch". That is false in both lander modes.

- Under in-place landing, which unit 3 S1 sets for gov, unit 2's prepared merge T has the
  advertised tip R as its first parent. From T, `BASE..HEAD` holds every default-branch commit
  landed since BASE.
- Under the primary lander, `--landed` records the default branch's HEAD after the `--no-ff`
  landing as the witness (`wit="$head"`, `:2375`). `BASE..witness` again holds every main-line
  commit between BASE and the landing.

The spec never defines "its witness". Under in-place, unit 22 S7 makes `--landed` write nothing, so
a gov record may carry no witness fact at all.

**Impact.** Suppose the owner hand-types `may:` into any build README while a run is in flight,
which is the one channel D12-j keeps open. That run's check 19 then reds at its prepared merge, so it
cannot land. The leg grades archived records on every bar (`check-unattended.sh:717-726`), and no
verb rewrites a terminal record, so the red is permanent. The property the arm closes is real:
TOOL-aStandingWrit-1 records that "a run that lands a new build README authorizes" the next. As
specified, the arm closes it by also closing the owner's channel.

**Fix.** Walk only the run's own commits: those reachable from the run branch and not from the
landing merge's first parent. For a landing merge W that is `git rev-list W ^W^1`. Define the
endpoint per lander mode and per recorded state. Under in-place, that endpoint is the landing commit
unit 22's `landing_commit_of` finds, not a witness fact. Put the walk in
`tools/unattended/lib-unattended.sh` as one function that M1's fold also calls. Add consumes-from
TOOL-dDerivedDocket-2. Add a negative AC6 arm: an owner commit after BASE adds `may:` on the default
branch, arrives through the prepared merge, and does not red. This restates the range in design fix
F4's letter for both units, so it takes a §9 line.

**Left-shift.** That negative arm, staged RED against the plain range. The class is item 2 below.
The first observation under "Outside the confirmed set" extends this entry to in-place records read
as live.

### H8 — the freeze-presence arm grades a phase gov never records (22, 34)

**Where.** Unit 18 §2 S4, §3's fourth bullet and §6 AC7. These are read against unit 22 §4 "The
readers" (the check 15 row), §2 S4, S6 and S7, and §3 Edges; unit 3 §2 S1; and unit 17 §3 Edges,
its hands-off to 22.

**Defect.** S4 grades only records whose recorded phase is LANDED. §3 says unit 22 "extends S4 to a
derived-LANDED record in the same commit that moves the freeze". Unit 22 carries no such scope item
and no edge with unit 18. Its readers table says the opposite: "the leg's check 15 and S10 | no |
they grade what a record SAYS it is, and a derived record says LANDING". S4 reports under check 15.
Unit 3 S1 sets gov to `LANDER_MODE=in-place`. There, unit 22 S7 makes `--landed` write nothing, and
S4 rotates a record with its `phase: LANDING` line kept. So no gov record written after this build
carries a recorded phase of LANDED.

**Impact.** In gov the arm's population is empty for every mandated run, so the freeze-presence
second opinion never fires. AC7's fixture is a primary-mode LANDED record, so it reads green. That is
`memory/gotchas/armed-but-unreachable-rule.md`. Under in-place the freeze is written at `--close`
(unit 22 S6), so a LANDING record could already be graded. G1's M16 noted the same population from
unit 22's side. G1's B2 is choosing whether rotation writes `phase: LANDED`, and this fold must
follow that choice.

**Fix.** Choose one owner for the gap, and write the choice into both specs.

- (a) Unit 18 S4 grades every record past `--close` under in-place: a recorded LANDING under
  `LANDER_MODE=in-place`, plus whatever archived form G1's B2 fold leaves. Add an in-place fixture
  AC.
- (b) Unit 22 takes the extension as an S-item, changes its readers-table row for check 15, and both
  specs declare the edge.

The first observation under "Outside the confirmed set" belongs to this same fold.

**Left-shift.** An AC7 arm over an in-place fixture record. The classes are items 3 and 4 below.

### H9 — three units accept on a verdict their named command cannot print (37)

**Where.** Unit 16 §6 AC13 and §3 Edges, unit 17 §6 AC12, and unit 18 §6 AC10. These are read
against unit 1 §2 S1, S5 and S6 and its §3 Edges, and design 21.4 U16's "Order".

**Defect.** Each criterion requires "no failure is NEW against unit 1's baseline", and each names
`bash tools/unattended/run-unattended-gates.sh --selftests`. At BASE that script takes
`--selftests`, `--checks` or `--all` and nothing else (`tools/unattended/run-unattended-gates.sh:121-128`).
Unit 1 S5 keeps the no-flag output unchanged, and the NEW, INHERITED and FIXED sets exist only under
`--attribute <R>` (S1, S6). Siblings 3, 4, 5, 22, 24, 27, 28 and 30 name `--attribute <BASE>`. Unit
1's hands-off list names units 2, 3, 4, 5, 23 and 30, not 16 to 18, and none of the three declares
consumes-from unit 1. Design U16 orders unit 1 "First, and before U11-U13", because those units run
suites that TOOL-aHoistedPass-36 records red at BASE.

**Impact.** The single run D12-h sanctions prints a red suite carrying inherited failures and no
split. The three Tier-2 units' criterion is then decided by eye, or the units cannot close. That is
the failure unit 1 exists to remove.

**Fix.** Change AC13, AC12 and AC10 to
`bash tools/unattended/run-unattended-gates.sh --attribute <BASE>`. Add consumes-from
TOOL-dDerivedDocket-1 to units 16, 17 and 18, and the matching hands-off lines to unit 1.

**Left-shift.** Class item 6 below: an AC that says "no NEW failure" must name `--attribute`. Units
16, 17 and 18 are live hits.

### H10 — the scaffold's key list omits two keys the generator requires (8, 50)

**Where.** Unit 15 §2 S8, §4 "The scaffold" and §6 AC10. These are read against
`tools/memory-tree/gen_build_index.py:174`, `:369-372`, `:635-648`, `:1054-1070` and `:1352-1361`.

**Defect.** §4's front-matter list is `slug`, `node`, `opened`, `streams`, `roster`,
`authorized-by: slug` and `asks:`. Two keys the generator needs are missing.

- `ids` is in `REQUIRED_KEYS` (`:174`). `parse_front_matter` raises `StaleHeader` without it
  (`:369-372`), and `apply_front_matter_ids` refuses a front matter with no `ids:` line to rewrite
  (`:1054-1070`).
- `status:` is required by `derive_status` for a build whose specs carry no parseable status header
  (`:635-641`), and a freshly scaffolded build has no specs at all.

Once the first spec lands, an authored `status:` becomes the "two answers" Problem (`:643-648`).
Deleting it in the run's first spec commit is existing practice: this build's own README carried
`status: OPEN` and `ids:` until `c6cb6951` deleted the status line, re-checked for this report. §4
does not say the run owes that edit. Two further gaps sit in AC10. It observes `asks:`, the contract
row and `--check-format`, and none of those reads `authorized-by:`. And `--check-format`'s reverse
registry check reds a row naming an untracked README (`:1359-1361`), while AC10 does not say its
fixture stages the scaffold's output.

**Impact.** The scaffold's own `--write` render refuses the README it has just written. D12-a's one
owner command therefore cannot produce a README the bar accepts, which is AC10's own Red-when. A
scaffold that writes `authorized-by: prompt` passes AC10, and units 16, 18 and 19 would then treat
that README as run-writable.

**Fix.** Add `ids:`, left empty for `--write` to fill, and `status: OPEN` to §4's key list. State
that the run deletes `status:` in its first spec commit. Make AC10 assert `authorized-by: slug`, and
run `gen_build_index.py --check` and `--check-format` after the scaffold's files are staged.

**Left-shift.** An AC10 arm that drives the scaffold end to end in a scratch repository: scaffold,
stage, `--write`, `--check`, `--check-format`. Stage it RED by dropping `ids` from the key list.

### H11 — the probe allow-list's match rule is unpinned, and its grammar admits only whole interpreters (2)

**Where.** Unit 15 §2 S7, §4 "The probe runner", §5 security and §6 AC9.

**Defect.** AC9 covers three cases: `PROBE_ALLOW` blank, a matching prefix, and a `;` in the command.
No arm sets a non-blank `PROBE_ALLOW` that does not match. §4 says the command runs "only when those
argv tokens begin with one of the whitespace-separated prefixes". It does not say whether matching
is whole-token equality or string prefix. A whitespace-separated list also splits a multi-token
prefix such as `python3 tools/foo.py` into two entries. The newline refusal and the bound are
unobserved.

**Impact.** A runner that executes any command once `PROBE_ALLOW` is non-blank passes AC9. So does
one where `tools/` string-prefixes `tools/../x`, or `python3` admits `python3x`. And because an entry
can only be one token, every entry an adopter can declare admits a whole interpreter or directory:
`python3` admits `python3 -c` followed by anything, whatever the match rule. §5's security claim
rests on this check. It guards the only place the kit executes a filer's bytes (charter §9). Gov
ships the key blank, so nothing in gov is exposed by this build. Adopters receive the key.

**Fix.** Pin the grammar and the match. Entries are separated by `|`, and each entry is a sequence
of whole argv tokens compared by equality against the command's leading tokens. State that a
single-token interpreter entry admits arbitrary code. Add AC9 arms:

- a non-matching prefix refuses and names the key;
- `python3x` against `python3` refuses;
- a two-token entry admits its own two-token prefix and nothing shorter;
- a newline refuses before splitting;
- a command past the bound is killed and reported.

**Left-shift.** Those arms, staged RED by a string-prefix comparison. The classes are
`memory/gotchas/id-matched-as-a-substring.md` and
`memory/gotchas/structured-record-split-on-whitespace.md`.

## Medium

The first thirteen entries are contradictions between specs or with BASE, an edge or declaration a
spec owes, or a decision the fold needs. The last twelve are gaps in what the acceptance criteria can
observe.

### M1 — T4 counts every default-branch commit since `m-base:` as the run's own (19)

**Where.** Unit 17 §4 "The terms", the T4 row, and design "19 fixes" F4. These are read against unit
16 §4, unit 3 §2 S3 to S5, and unit 2 §2 S3.

**Defect.** T4 grades shas in `m-base..HEAD`. Under in-place landing the DoD runs at `--close` on the
prepared merge, whose first parent is the advertised tip. The range therefore holds every
default-branch commit landed since `m-base:`. The driver reads no foreign build's file, so it cannot
recognise a foreign unit's build commit.

**Impact.** A foreign build that lands `CLOSED · <a mandated ask> · by <its own sha>` during the run
makes T4 red, naming a sha this run never wrote. The run then needs the D12-b override. The design's
"Why T4" scopes the rule to the run's own commit, and T5 already owns "closed with someone else's
evidence".

**Fix.** Define T4's range as the run's own commits, the same set H7's fold defines. Add an AC with a
foreign in-range closing sha that T4 does not name. This restates F4's letter, so it takes a §9 line.

**Left-shift.** That AC. The class is item 2 below.

### M2 — the `ASKS_CMD` contract names one call, and the specs make three (44)

**Where.** Unit 16 §2 S1 and §4 "The ASKS_CMD contract", against §4 "Ids-shaped invocations". Also
unit 17 §4 "Data model" and "The freeze", and unit 20 §2 S5.

**Defect.** S1 makes the contract "the `--asks` invocation of §4", one fixed argument list ending
`--at <m-base>`. The filing-home recipe must list that folder's live asks "as the
`--asks --build <slug>` print mode reports them at BASE". That is a shape the contract omits, and the
kit can reach it only through `ASKS_CMD`, because a kit file cannot name the generator by literal.
Unit 17 calls the witness "at HEAD over M ∪ F" and names no arguments. Nothing says what the
filing-home refusal prints while `ASKS_CMD` is blank, which is the kit default and gov's state until
unit 35. Unit 16 declares no edge to unit 7, whose `--build` mode it uses.

**Impact.** An adopter implementing the documented contract has no promise of supporting the other
two calls. Unit 17's T2 and freeze calls are unspecified. Unit 20's Skill relays a filing-home recipe
that cannot list asks in gov between units 20 and 35.

**Fix.** Enumerate every call shape in unit 16 §4 and in the protocol §8 row: READY at `m-base:`
for preflight, the status witness at HEAD for close and the freeze, and the filing-home listing at
BASE. State what the filing-home refusal prints while `ASKS_CMD` is blank. Have unit 17 name its
appended arguments. Add consumes-from TOOL-dDerivedDocket-7.

**Left-shift.** Class item 1 below, run once per declared call shape.

### M3 — code 19 refuses the state every scaffolded build starts in (75)

**Where.** Unit 16 §2 S7 and S8 and §6 AC7. These are read against unit 15 §4 "The scaffold",
design §19.4 and `tools/unattended/unattended.sh:2058-2061`.

**Defect.** S7 keeps code 19 for an empty roster with zero specs. Unit 15's scaffold writes the units
roster pair empty, and the new folder files no `unit` ask. So every build D12-a's route produces
starts in exactly that state. At BASE, fail 19 fires before any row prints.

**Impact.** On every E3 build, `--plan` and `--plan --asks` refuse at the moment S8's UNDECIDED
`next:` shape is designed for, and `--status` and `--resume` read the same next. The Skill routes on
that output (unit 20 S5 and S6). A run can work around it by writing roster rows before orienting,
which is the order the design reverses.

**Fix.** Count a pinned `asks:` mandate as plan input, so code 19 fires only when the roster, the
specs and the mandate are all empty. On a mandate-only build, `--plan --asks` prints the ASK rows and
`next: <id> (UNDECIDED …)`. Add an AC over a scaffold-shaped fixture: an empty roster, no spec and an
`asks:` line.

**Left-shift.** That AC, fed from unit 15's real scaffold output rather than a hand-written README.

### M4 — the leg enforces a folder-wide anchor ban that no carrier states (40)

**Where.** Unit 20 §2 S3 and S4, and §4 "Wording that is true in both modes". These are read against
unit 18 §2 S3, `memory/guides/UNATTENDED-PROTOCOL.md:246-251` and design §19.7 layer 1.

**Defect.** Unit 18 S3 reds a foreign-slug anchor in any tracked file under a mandated run's folder.
The protocol's anchor ban scopes the rule to the run-state file's authored rows. Design §19.7 layer 1
states the carrier change as the ban "widened from `RUN.md` to the whole folder". Unit 20 edits only
the ban's planned-unit sentence, and its guide carries §19.2 to §19.6, not §19.7. Unit 18 writes no
user docs.

**Impact.** A run following the protocol types resolution tables under `prompts/` and `build/`, which
is K9's population, 24 of its 31 anchor lines. It meets the rule only when the leg reds.

**Fix.** Extend unit 20 S3 so the ban's paragraph covers every tracked file under the run's build
folder, and names the link-wrapped `--asks --ready` paste as the sanctioned way to cite a foreign
ask. Add that sentence to AC3 and to S9's sweep.

**Left-shift.** Class item 7 below.

### M5 — units 19 and 20 name a stage that never runs their arms (41)

**Where.** Unit 19 §5 "testing" and §6 AC1's permission line, and unit 20 §4 "Fail codes and
self-tests". These are read against `tools/gate-legs.json` and the build README's rule "Unattended
self-tests run only in units 1, 3, 4, 5, 16, 17, 18, 22, 24, 27, 28 and 30".

**Defect.** Both specs say the unattended suites run "at the build's one post-build bar".
`tools/gate-legs.json` carries no leg for `unattended.test.sh` or `check-unattended.test.sh`, because
those suites left the bar by owner ruling on 2026-08-23. `run-gates.sh` runs only manifest legs, so
even `GATE_FULL=1 GATE_SELFTESTS=1` does not run them.

**Impact.** Unit 19's AC1, "Proven in `tools/unattended/unattended.test.sh`", and unit 20's two new
arms are executed only incidentally, by a later unit's attribution run that neither spec names.

**Fix.** Name the run that executes them. The next self-test-permitted unit is 22, whose
`run-unattended-gates.sh --attribute <BASE>` run would carry them, with an edge to it. Otherwise
name the landing's compensating check from unit 1 S8.

**Left-shift.** Class item 6 below.

### M6 — unit 34's AC8 reads unit 20's check, and neither spec declares the edge (42)

**Where.** Unit 20 §3 Edges, §8 F1 and §4 "The two-key refusal". Also unit 34 §6 AC8 and §3 Edges.

**Defect.** Unit 34 AC8 requires `check-unattended.sh` to report no path declared under both keys.
That check exists only as unit 20's S1, and unit 20's F1 names "spec 34's AC8" as its reader. Neither
spec declares the edge, although the brief says an edge found is added and never dropped.

**Impact.** The reciprocity and ordering arms cannot see the dependency. If unit 20's check is
absent or later retired, unit 34 AC8 passes by absence, because a check that does not exist reports
nothing.

**Fix.** Add hands-off TOOL-dDerivedDocket-34 to unit 20, naming the two-key refusal the
switch-over's AC8 reads, and the matching consumes-from to unit 34.

**Left-shift.** G2's class item 1c: a spec whose AC invokes a check another spec adds must declare
consumes-from that spec. This is a live hit.

### M7 — the leg's half of the two-key refusal compares two empty sets (68)

**Where.** Unit 20 §2 S1, §4 "The two-key refusal" and §5 error states. These are read against
`tools/unattended/check-unattended.sh:116-120` and `:181-186`, and
`tools/unattended/unattended.sh:290` and `:328`.

**Defect.** The leg imports conf keys only through its allow-list, and neither `SHARED_RECORDS` nor
`GENERATED_INDEXES` is on it. The driver resolves an undeclared `SHARED_RECORDS` to
`$MEMORY_ROOT/DECISIONS.md $MEMORY_ROOT/backlog` through a `__kit-default__` sentinel. The leg
sources only `lib-unattended.sh`, and §5 says blank keys compare as empty sets.

**Impact.** As specified, the leg's half compares two empty sets and is silent on every tree. With
the import widened, a different gap remains. An adopter who relies on the default and adds a
`GENERATED_INDEXES` pair over `memory/backlog` is refused by the driver and passed by the bar. That
is the half edit §4 says this check exists to catch, and the outcome F1 rejected as option (b). AC1
declares both keys explicitly, so it cannot see this.

**Fix.** Widen the leg's initialiser and allow-list for both keys in this unit. Move the default
resolution into `lib-unattended.sh` beside the predicate, so both callers share it. Add an arm to
AC1 with `SHARED_RECORDS` undeclared.

**Left-shift.** Class item 5 below. The gotcha is
`memory/gotchas/two-readers-of-one-config-one-re-derived.md`.

### M8 — runs pointed at asks silently lose the M12 directives (73)

**Where.** Unit 16 §2 and §3, where no such item exists. This is read against `DIRECTIVES_CORE`
(`tools/unattended/unattended.sh:473`), the TOOL-aPromptedMandate-4 row at `memory/DECISIONS.md:35`,
`memory/guides/BUILD-METHOD.md:312`, and unit 15 §4 "The scaffold".

**Defect.** `DIRECTIVES_CORE` scopes `researched:M12:prompt` and `solution-tested:M12:prompt` to
prompt-authorized runs. The owner ruling behind that rests on a slug-mode build whose solution "was
already chosen". Under D12-a every ask-driven run starts from unit 15's scaffold, which writes
`authorized-by: slug`, no specs and no authored prose. M12's own trigger, "nobody has chosen yet",
holds, and neither directive binds. No G3 spec mentions this.

**Impact.** Runs pointed at asks drop the research and solution-test obligations with no waiver and
no record. That includes `legacy` asks, which carry no acceptance at all.

**Fix.** This needs a decision. Either widen both directives to bind a record that pins `asks:`, with
an arm; that changes the scope of an owner ruling, so it is the owner's call. Or record a DECISIONS
row that the ruling's premise does not reach scaffolded builds, and name what replaces M12 there.
Unit 20's per-ask orientation is the obvious candidate.

**Left-shift.** A documented check: a spec that adds a new way to reach an authorization mode lists
the mode-scoped directives and states which of them bind.

### M9 — no second opinion reaches `asks-ready:`, or the freeze's content (77)

**Where.** Unit 18 §1 Goal, §2 S4, §3's second bullet and §4's table. These are read against unit 16
§4's table, unit 17 §4 "The F3 hardening", `tools/unattended/unattended.sh:2731-2734`, and the
TOOL-aUnmannedHelm-6 row at `memory/DECISIONS.md:47`.

**Defect.** The Goal promises the leg its own reading of "each mandate fact". `asks-ready:` gets no
arm, because §3 excludes re-deriving READY, and `asks-at-landing:` is checked for presence only. The
driver's own comment says a pinned authorization fact exists "so the leg has a recorded answer to
SECOND-OPINION". Re-running `ASKS_CMD` at the recorded `m-base:` is the natural second opinion. As
specified it is impossible, because unit 16 does not pin the `--live-builds` set the grade was
computed with.

**Impact.** F3 admits a self-filed hold only for a `no` or `legacy` ask. A run that edits its own
record from `yes` to `no` takes the laxer path, and no arm notices. A forged freeze passes S4.
TOOL-aUnmannedHelm-6 records that checking a claim's paperwork without the claim is a second
signature, not a second opinion.

**Fix.** Have unit 16 pin the live-build set beside `asks-ready:`. Add a unit 18 arm that re-runs
`ASKS_CMD` at the recorded `m-base:` with that set and requires the result to equal `asks-ready:`.
Re-derive `asks-at-landing:` with `--at` set to the landing commit. Otherwise, state in the Goal, in
S4 and in the leg header that both facts go unverified. H4's answer decides what the set is.

**Left-shift.** Class item 3 below. The gotcha is `memory/gotchas/inputs-inside-the-subjects-reach.md`.

### M10 — AC14's Red-when cannot happen at unit 16's order (43)

**Where.** Unit 16 §6 AC14. This is read against unit 4 §2 S1 and S8, and its §3 non-goal that "the
derived-terminal unit adds that derivation".

**Defect.** AC14 reds when the live-build set is read from a recorded phase string instead of
`derived_phase()`, "so a HELD run reads as abandoned". At unit 16's order, `derived_phase()` returns
the recorded phase unchanged. The first derivation that differs, LANDED from the tip, arrives with
unit 22, which is ordered later. HELD is non-terminal under either reading.

**Impact.** The named break produces identical fixture results, so the criterion certifies a
property it cannot distinguish.

**Fix.** Name a break the criterion can observe. One is a live-set reader that hard-codes a phase
list omitting HELD, so a HELD fixture reads as abandoned. Another is a direct phase-fact read, which
unit 4's structural arm catches. Or move the derived-against-recorded arm after unit 22, with a
derived-LANDED fixture and the edge.

**Left-shift.** Class item 8 below.

### M11 — the scaffold's generated slot bodies may anchor the ids they name (53)

**Where.** Unit 15 §4 "The scaffold". This is read against `SLOT_CANON`
(`tools/memory-tree/gen_build_index.py:107-113`) and the anchor shapes at
`tools/memory-recall/extract.py:117-121`.

**Defect.** The generated slot bodies "name the asks". `SLOT_CANON` makes "Expected improvements"
and "Detriments if this is not built" bullet slots that may not be empty. `A_BOLD_LI`, `A_DASH` and
`A_TABLE` anchor an id that leads a bullet or a row. §4 guards anchoring elsewhere, through the
one-line `asks:` and the link-wrapped first cell, and states no constraint for these bodies.

**Impact.** A natural bullet of the form `- EXMP-aFoo-3 — …` makes the new build a second claimant of
a foreign id. Check 13 then reds the owner's scaffold commit at push, and unit 18 S3 reds the run.
This is MEDIUM rather than HIGH because it depends on a shape the implementer chooses, and it reds
loudly.

**Fix.** State in §4 that generated bodies mention asks inside prose, never as a bullet's or a row's
first token. Add an AC10 arm asserting that `anchor_at` returns nothing for every line the scaffold
writes.

**Left-shift.** That arm. The gotcha is
`memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md`.

### M12 — AC8 asserts a line position `set_fact` does not produce (61)

**Where.** Unit 17 §6 AC8, against §2 S3, §4 "The freeze" and `set_fact`
(`tools/unattended/unattended.sh:2776-2787`).

**Defect.** `set_fact` inserts a new key directly under the `## Run facts` heading, so a record reads
newest-first. A key written after `units-at-landing` lands on the line BEFORE it. AC8 expects it "on
the line after".

**Impact.** The criterion fails against the seam §4 names. Meeting it as written would mean changing
`set_fact`'s placement for every fact, and every arm that reads fact positions. G1's M16 fix text
repeats the same "on the line after" wording for unit 22's in-place close, so the two folds should
share one assertion.

**Fix.** Assert that the fact is present, and that it is written before the terminal writes, rather
than its adjacency.

**Left-shift.** Class item 6 below.

### M13 — AC9 names check 1 for a red that check 3 raises (62)

**Where.** Unit 17 §6 AC9. This is read against `tools/unattended/check-unattended.sh:663-676` and
`:692-694`.

**Defect.** The DoD shrink-only pin is `fail 3`, "CORE Definition-of-Done set has shrunk below its
floor". Check 1 fires only when `CORE_FLOOR` is undeclared or malformed.

**Impact.** The arm staged for AC9 observes check 3, so the criterion reads as failed, or gets
"fixed" by asserting the wrong code.

**Fix.** Name check 3 in AC9.

**Left-shift.** Class item 6 below: an AC naming a leg check number resolves it against the
checker's own fail sites.

### M14 — most of READY's rules have no failing case (1)

**Where.** Unit 15 §2 S5 and S9, and §6 AC5, AC6 and AC12.

**Defect.** No criterion makes R1, R4 or R6 fail. R2's terminal branch, R2's `unit`-ask branch and
a passing R3, a hold inside M, are not observed either. AC8 fails R1 only through the no-row case.
AC5's Red-when is "legacy granted with R4 and R5 both failing", but AC5's only legacy fixture
carries a pointer, so R4 holds and the Red-when cannot occur. AC12 grades only the arms that exist,
so S9's "arms for every verdict, grade and refusal" is not measured.

**Impact.** Several wrong graders pass every criterion. One ignores R1's exactly-one and home tests,
one ignores R4's path-present test, and one ignores R6's data-clause test. Another grants `legacy` on
R1 to R3, R6 and `filed` before the cutoff alone, which is what design fix F6 forbids. Units 16 and
17 key preflight and the F3 hardening on these grades.

**Fix.** Add fixtures to AC5 and AC6, each naming its expected `missing` value:

- an id with no ask row, and one with two (R1);
- an ask filed in a foreign folder (R1's home test);
- a pointer whose path is absent from the tree (R4);
- an external locator with no `data` clause (R6);
- a terminal ask, and a `unit` ask of the `--target` folder (R2);
- a hold whose target is inside M (R3 passes);
- a pre-cutoff ask with neither pointer nor acceptance, which must grade `no`.

**Left-shift.** Those fixtures. The class is item 8 below.

### M15 — AC7 counts fields and cannot see a reorder (4)

**Where.** Unit 15 §6 AC7.

**Defect.** AC7 observes the field count, the leading `ask` and the examined line. Its Red-when
names a reordered field, and a reordered row still has eleven fields.

**Impact.** Swapping `status` and `ready`, or `decided-by` and `home`, passes. Units 16 and 17 parse
by position, and their own tests drive a fixture `ASKS_CMD`, so no criterion anywhere pins the order.

**Fix.** Assert the value at every position for a fixture whose values are distinct and known: field
3 `OPEN`, field 7 `yes`, field 11 `stale:` and an id. Have the consumers validate each field's value
set, so a reorder reads as a parse refusal.

**Left-shift.** That fixture, shared with class item 1's consumer arm.

### M16 — AC1's Red-when cannot occur in AC1's fixture (5)

**Where.** Unit 15 §6 AC1.

**Defect.** AC1's Red-when is a left-to-right read in which a TEXT containing ` · out ` swallows the
real clauses. The §4 example's TEXT contains no ` · <label> ` segment, so both read directions split
it identically. The example also holds three clauses, not the four AC1 claims.

**Impact.** A left-to-right parser passes AC1, so §4's claim that a collision "is loud" rests on a
read direction no criterion tests.

**Fix.** Add a fixture row whose TEXT contains ` · out ` before the real `seen` and `accept` clauses.
Assert the parsed clause values and the V13 verdict that the misread produces. Correct "four" to
three, or add the fourth clause.

**Left-shift.** That row. The class is item 8 below.

### M17 — V14 has no passing arm on or after the cutoff (6)

**Where.** Unit 15 §2 S4 and §6 AC4.

**Defect.** AC4's arms are an ask on the cutoff with no clauses, which reds, and one filed the day
before, which passes. No arm shows an ask on or after the cutoff passing because it carries `accept`,
or a `seen` with `run`. S4 says the ask "must carry" them, while R5 reads "the merged clauses", so
whether a SCOPE row can make a new ask V14-clean is left open.

**Impact.** A V14 that reds every ask filed on or after `ASK_CUTOFF` passes AC4. Unit 24's
auto-filed asks and the Skill's filing step depend on the SCOPE answer.

**Fix.** Add AC4 arms: a cutoff-day ask with `accept` passes, one with `seen … run` passes, and one
with a bare `seen` reds. Decide whether a SCOPE row's `accept` satisfies V14, and arm the decision.

**Left-shift.** Those arms.

### M18 — S8's rank, duplicate-closer refusal and shared next have no criterion (12)

**Where.** Unit 16 §2 S8, §4 "Plan, next and rank" and §6 AC9.

**Defect.** AC9 observes the three-field ASK row, the UNDECIDED next and check 30. Four S8 behaviours
are unobserved: the rank order, the refusal row for two live units closing one ask, `--status` and
`--resume` reading the same next, and ASK rows for live asks filed in the folder but not mandated.
§4 never names the three `--paths` fields. Design §19.4 gives `ASK`, the id and a `k=v;…` summary,
with no keys (design line 1365).

**Impact.** A plan that ranks by listing order, omits the duplicate-closer refusal, or lets
`--status` print the old terminal next passes. Unit 20's Skill routes on `--plan --asks` output whose
machine fields are undefined.

**Fix.** Pin the three fields and the summary keys in §4. Add criteria: two held asks rank by hold
edge rather than listing order; `-2` sorts before `-10`; two live units closing one ask print the
refusal row; `--status` and `--resume` print the same UNDECIDED next.

**Left-shift.** Those criteria.

### M19 — READY at `m-base:` is unobserved, and so are the bound, the exit and a malformed row (13)

**Where.** Unit 16 §2 S5, §4 "The ASKS_CMD contract", and §6 AC6 and AC14.

**Defect.** Only the short-witness case has a criterion. A bound breach, which §4 says is named
"never answered", a non-zero exit and a malformed row are not observed. Nothing observes that the
call carries `--at <m-base>`.

**Impact.** Two wrong drivers pass AC6 and AC14. One treats a bound breach as a red. The other omits
`--at`, so READY grades the working tree, where a row filed after the run began counts as filed and
an unpushed SCOPE row moves the pinned `asks-ready:`.

**Fix.** Add AC6 arms. A stub `ASKS_CMD` that sleeps past the bound prints "never answered". One that
exits 1 refuses and names the exit. A stub that records its argv shows `--at` equal to the pinned
`m-base:`.

**Left-shift.** Those arms.

### M20 — the item's success path, closed by this build's unit, has no criterion (16)

**Where.** Unit 17 §6 AC4 to AC8.

**Defect.** The criteria show MET only for a BLOCKED ask with a decision park row and for KEEP with
an advancing spec. In both the ask stays live. AC5 shows only T4's UNMET side. No criterion shows the
item MET for a mandated ask derived CLOSED by a CLOSED spec of this build, or for an in-range CLOSED
whose sha is a CLOSED unit's build commit.

**Impact.** An arm that reds every CLOSED mandated ask passes every criterion, although closing by
this build's unit is the item's main success path. Every legitimate ask-driven run would then need
the override. Gov's `ASKS_CMD` stays blank until unit 35, so nothing else runs this path first.

**Fix.** Add a criterion: the item is MET for a fixture in which this build's CLOSED spec `closes`
the mandated ask. Add one in which a CLOSED row's sha is that unit's `build_commit` result, and T4
admits it.

**Left-shift.** Those criteria.

### M21 — T0's second row, T1, T2's other halves, T5 alone and two F3 rules have no criterion (18)

**Where.** Unit 17 §4 "The terms" and "The F3 hardening", and §6.

**Defect.** §7's gate line names a fixture per term, so T0 to T5 each have a named arm, but no
criterion with a Red-when observes T0's second row, T1, T2's examined-count mismatch and bound
breach, or T5 in isolation, including the `rescope` owed class. Two F3 rules are named nowhere: a
decision park row's reason must spell `veto 2` or `veto 3`, and a self-filed owner-call hold is
admitted only for a `no` or `legacy` ask. AC4's MET fixture states neither the ask's grade nor the
park row's reason.

**Impact.** Each of these branches can be omitted or inverted with every criterion green. That
includes the two F3 restrictions, which exist to stop a run meeting the item with no delivered work.

**Fix.** Add one fixture per branch:

- `ASKS_CMD` set with no mandate: MET, announced "nothing to dispose";
- an `asks:` fact with `ASKS_CMD` blank: UNMET;
- a BLOCKED `legacy` ask with no park row (T5 UNMET), and with a rescope-retire park row (MET);
- a `yes` ask held with a decision park row whose reason lacks `veto`: UNMET;
- a self-filed owner-call hold on a `yes` ask: UNMET.

**Left-shift.** Those fixtures.

### M22 — unit 18's AC4 cannot tell the anchor-derived arm from a `base:`-derived one (23)

**Where.** Unit 18 §6 AC4. This is read against `resolve_base` (`tools/unattended/unattended.sh:887-898`),
the degenerate path (`:952-957`) and the `anchor-sha` write (`:2713`).

**Defect.** For a slug-mode record, `base:` equals `merge-base(anchor-sha, HEAD at preflight)` by
construction, which is exactly `m-base:`. The degenerate path sets `base:` to HEAD only where the
merge-base is HEAD anyway. S5 requires slug mode, and AC4 forges only `m-base:`.

**Impact.** The correct arm and the forbidden one both red, so an arm that compares `m-base:` against
`base:` passes AC4, and fix F4's requirement is not measured.

**Fix.** Forge `base:` and `m-base:` together to the same older ancestor of `anchor-sha`. Only the
anchor-derived arm then reds.

**Left-shift.** That fixture. The class is item 8 below.

### M23 — unit 19's carrier content and budgets have no criterion (26)

**Where.** Unit 19 §2 S7, §4 "Budgets" and §6 AC9.

**Defect.** AC9 observes byte parity and the BUILD-METHOD size cap only. Nothing observes what
protocol §1 must state: where a grant is honoured, what it lifts, and that ask-row and SCOPE-row
clauses honour nothing. Nothing observes that M3 gains exactly one pointing sentence, or the budgets
of at most 300 B on BUILD-METHOD and 600 B on the protocol.

**Impact.** An empty edit passes, and so does one over budget but under the shared caps. The latter
spends the headroom that units 20 and 31 were priced against (unit 20 §4).

**Fix.** Add criteria: a grep over both protocol copies for the rule sentence; a
`git diff --numstat` against this unit's parent showing at most 300 B on BUILD-METHOD and 600 B on
the protocol; and a count of the M3 sentences naming protocol §1.

**Left-shift.** Class item 7 below.

### M24 — unit 20's AC1 fixture is caught by an equality test too (29)

**Where.** Unit 20 §6 AC1 and the first §7 arm.

**Defect.** AC1's fixture and the §7 arm both declare the identical string `memory/backlog` in both
keys, which string equality also refuses. AC1's Red-when, equality letting `memory` and
`memory/LIVE.md` pass, is never staged.

**Impact.** A predicate written as string equality passes both the criterion and the arm. The
switch-over's half edit is then caught only when the two paths match exactly.

**Fix.** Add a fixture pairing `memory` in `SHARED_RECORDS` with `memory/LIVE.md:<generator>` in
`GENERATED_INDEXES`, plus the reverse nesting, and assert the refusal for both.

**Left-shift.** That fixture. The gotcha is `memory/gotchas/containment-tested-one-way.md`.

### M25 — unit 20's protocol edits and guide content have no criterion (30)

**Where.** Unit 20 §2 S3 and S4, and §6 AC3 and AC4.

**Defect.** AC3 observes parity and growth, and AC4 observes installation and byte equality. Nothing
observes the content S3 requires: the §2 anchor-ban sentence, the §11 declined disposition, the
own-folder paragraph and the guide pointer. Nothing observes the guide sections §4 lists.

**Impact.** An empty guide passes every criterion, and so do protocol edits that leave "a planned
unit is minted as a backlog row" in place. The guide is where unit 17 hands off the T0 to T5 text,
the override route and the KEEP rule.

**Fix.** Add greps for the retired protocol sentences, expecting count 0, and for the new ones,
expecting one per copy. Add a criterion listing the guide's required headings.

**Left-shift.** Class item 7 below.

## Low

### L1 — the clause merge rules have no criterion, and two `seen … run` values are ambiguous (9)

**Where.** Unit 15 §2 S2 and §4 "The probe runner".

**Defect.** AC2's SCOPE row adds `accept` to an ask that has none, so replace-per-label and conjoin
give the same result. The conjoin rule and the union absorbing `none` are unobserved. With `seen`
conjoined, two rows can each carry `run`, and §4 still says `--probe` takes "the merged `seen`
command", in the singular.

**Impact.** A SCOPE row that replaces the ask's value passes AC2. A triager's SCOPE `seen … run`
could become the command `--probe` executes for someone else's ask.

**Fix.** Add an AC2 arm in which the ask and a SCOPE row both carry `accept`, and both values print.
State that `--probe` refuses as ambiguous when two `seen` values carry `run`.

**Left-shift.** That arm.

### L2 — the freeze has no no-mandate arm and no sort arm (21)

**Where.** Unit 17 §2 S3 and §6 AC8.

**Defect.** AC8 has only a mandated-fixture arm. Nothing shows that a record with no mandate and no
filed ask gains no line, and nothing observes the numeric sort that S3 and §4 require.

**Impact.** A freeze written onto every record, or sorted as strings, passes, and the rollout claim
that no existing record changes is not measured.

**Fix.** Add a no-mandate `--landed` arm asserting that no line is written, and a fixture holding
`-2` and `-10` asserting numeric order.

**Left-shift.** Those arms.

### L3 — the freeze's "every mandated id" is unobserved (24)

**Where.** Unit 18 §2 S4 and §6 AC7.

**Defect.** S4 requires the freeze to name every mandated id. AC7 observes only whether the fact is
present.

**Impact.** A freeze missing one mandated id passes, and that ask's frozen answer is lost. M9 is the
larger half of the same gap.

**Fix.** Add an AC7 arm in which `asks-at-landing:` omits one id of `asks:`, and check 15 names it.

**Left-shift.** That arm.

### L4 — no `recipe`-mode arm, and the grant token grammar is undefined (28)

**Where.** Unit 19 §2 S2 and S3, and §6 AC2 and AC3.

**Defect.** AC2 exercises `prompt` mode only, although S2 refuses `recipe` too. S3's "path-shaped"
is undefined, including whether a grant is backticked, as unit 15's `GRANT` is, which §3 says an
owner copies by hand.

**Impact.** A refusal keyed on `prompt` alone passes. An owner who copies an ask-row proposal
verbatim is either refused or pinned with backticks the leg then compares.

**Fix.** Add a `recipe`-mode arm to AC2. Pin the token grammar, backticked or bare, with an AC3 arm
for each form.

**Left-shift.** Those arms. H6 asks for the same `recipe` arm in unit 16.

### L5 — the new M9 row names a command that never lists a terminal ask (49)

**Where.** Unit 20 §2 S7, the M9 row. This is read against unit 7 §2 S12.

**Defect.** The row reads "asks filed and disposed", derived from
`gen_build_index.py --asks --build <slug>`. Unit 7 S12 defines that table form as listing live asks
only, and every ask only with `--all`. Unit 20 declares no edge to unit 7.

**Impact.** A reader deriving the wrap-up count from the named command gets only undisposed asks, so
the derivation table misstates what the build disposed.

**Fix.** Name `--asks --build <slug> --all` in the row, and add consumes-from TOOL-dDerivedDocket-7
with the matching hands-off.

**Left-shift.** None beyond the fix. A derivation row's command is read once, by M9.

### L6 — AC4's pair count is three where a correct tree holds four (69)

**Where.** Unit 20 §2 S4 and §6 AC4. This is read against unit 4 §2 S10 and AC11, and the pair loop
at `tools/unattended/check-unattended.sh:1583-1620`.

**Defect.** Unit 4, ordered earlier, adds `UNATTENDED-STOPS.md` as a companion guide that the leg
byte-compares to its template. Check 10 therefore already carries the protocol, verbs and stops
pairs before this unit adds a fourth. S4 says "third pair" and AC4 expects "three pairs".

**Impact.** The criterion reads as failed against a correct tree, or invites dropping a pair to make
the count match.

**Fix.** Assert that the ASKS pair is present rather than a fixed total, or state four and derive it
from the pair list.

**Left-shift.** None beyond the fix. A count of a derived population is not written in prose
(charter §7).

## Left-shift, by class

1. **The seam between the `--tsv` producer and its consumers is graded only against a stand-in**
   (H1, H2, H3, M2, M3, M15, M19). Units 16 and 17 fake `ASKS_CMD` in every fixture. A stub cannot
   carry the waiver line, an empty field, or a call shape the contract forgot, so every one of those
   defects is green. Give each consumer suite one arm that runs the REAL producer,
   `gen_build_index.py --asks --tsv`, over a builds-mode fixture tree, and parses its stdout with the
   driver's own parse. The tree should hold an OPEN unlabelled ask, an ask closed by two records and
   a tolerated-by-waiver header. Stage it RED twice: by adding one print to the producer's stdout,
   and by emptying `sev`. The gotchas are `memory/gotchas/staged-break-substitutes-a-synthetic-value.md`
   and `memory/gotchas/empty-field-collapses-unless-it-is-last.md`.
2. **"The run's own commits" spelled as a plain range across a landing merge** (H7, M1). One function
   in `tools/unattended/lib-unattended.sh` answers it for every arm that grades authorship, excluding
   commits reachable from the landing merge's first parent. Each suite gets a fixture in which an
   owner commit on the default branch lands inside the window through the prepared merge. The
   documented check: every S-item that says "the run's range" states what it means under in-place
   landing.
3. **A population the subject supplies, or one located where the subject cannot be** (H3, H4, H8,
   M9). F is read from the witness it scopes. The live-build set is read from a tree that holds no
   live run's record. The freeze-presence arm grades a phase gov never records. Each arm that
   quantifies over a population should print its size and its source, as the leg's PRE and POP
   guard already does (`tools/unattended/check-unattended.sh:712-730`). The documented check: for
   every "every X" in an S-item, the spec names where X is enumerated and shows that the enumeration
   reads nothing the subject writes or returns. The gotchas are
   `memory/gotchas/inputs-inside-the-subjects-reach.md` and
   `memory/gotchas/armed-but-unreachable-rule.md`.
4. **A fixture configured as the kit default where the shipping repository differs** (H4, H5, H8).
   Every ask-path arm in `tools/unattended/unattended.test.sh` and `check-unattended.test.sh` runs
   under the kit default AND under gov's declared `ANCHOR_SCOPE="published"` and
   `LANDER_MODE=in-place`. The documented check: an AC's fixture names the conf values it runs under
   whenever gov's value differs from the kit default.
5. **The driver admits what the leg refuses, or the two halves read one rule from different inputs**
   (H6, M7). For every leg S-item that reds a record shape, the driver spec either refuses that shape
   at preflight or states why not. A conf key both halves read has its default resolved in
   `lib-unattended.sh`, once. Unit 18 S5 against unit 16 S2 is a live hit, and so are the two-key
   defaults.
6. **An AC naming a stage, a command or a check that cannot produce its verdict** (H9, M5, M12, M13).
   Three joins fit `tools/check-spec-tokens.py`, over inputs already in the tree. Run each over this
   build first and print hits and near-misses before wiring it, per charter §7.
   - (a) An AC that says "no NEW failure" names `--attribute`. Live hits: units 16, 17 and 18.
   - (b) An AC or §5 line saying a suite runs "at the post-build bar" names a leg that
     `tools/gate-legs.json` resolves, or a unit on the build README's self-test list. Live hits:
     units 19 and 20.
   - (c) An AC naming "check <n>" of a leg resolves `<n>` against that checker's `fail <n>` sites
     and the phrase the AC quotes. Live hit: unit 17 AC9.
7. **A rule the leg enforces that no carrier states, and carrier text no criterion reads** (M4,
   M23, M25). The documented check: unit 20's S9 sweep gains a column listing every leg rule this
   build adds, with the carrier sentence that states it. A carrier edit's criterion greps for the
   sentence it adds and for the sentence it retires.
8. **An S-item whose Observed-by criteria survive its deletion** (M10, M14 to M25, L1 to L4, and half
   of H10 and H11), per `criterion-asserts-what-its-own-command-cannot-show`. This is the third group
   in a row where it leads, at 17 outright of 50. G1 and G2 proposed a `check-spec-tokens.py`
   near-miss printer. This group adds one narrower, mechanical form: a `Red when:` whose break the
   AC's own fixture cannot produce. Six live hits (1, 4, 5, 23, 29 and 43) share one shape. Each
   Red-when names an input value, and that value is absent from the fixture the AC names. The fold
   should write, beside each S-item's "Observed by", the mutation that deletes the item and the AC
   that reds on it.

## Outside the confirmed set

Two observations came out of re-checking the highs. Neither was put to a skeptic, so neither is
counted above. Both were read at `abac6d59`.

**In-place records read as live to unit 18's and unit 19's arms.** Under `LANDER_MODE=in-place` a
landed record keeps `phase: LANDING` (unit 22 S4 and S7). LANDING is not in `PHASES_TERMINAL`
(`tools/unattended/unattended.sh:338`), and unit 22's readers table says check 19 reads the recorded
phase. Two consequences follow, and both fall inside H7's and H8's folds.

- Unit 18 S1's HEAD half ("for a non-terminal record it also requires the README at HEAD to carry
  the same bytes") grades every landed, unrotated gov record carrying `asks:`. Design §19.2's route
  for a follow-up run is "ONE line, `asks: …`, added to an existing README". An owner who edits that
  line to start one pushes a commit on which check 19 reds the old record, and the pre-push bar
  blocks the push. The preflight that would rotate the record needs the edit already on the default
  branch. AC2's own Red-when names this outcome for terminal records, and under in-place it arrives
  through a non-terminal one.
- Unit 19's cross-run arm walks `BASE..HEAD` for a record it reads as live. For such a record HEAD is
  the tip of whatever tree is being graded, which grows forever. Every later `may:` grant anywhere
  on the default branch then reds it.

If G1's B2 fold keeps the archived phase at LANDING, archived records stay non-terminal to both
readers as well.

**Unit 35's staged RED for `asks-disposed` passes for the wrong reason while H1 or H2 stands.** Unit
35 S4 expects `--close` to refuse "naming `asks-disposed` and the ask among its unmet items". A T2
DEAD PROBE names the missing ask id, which satisfies that expectation. So the arming unit cannot
tell the intended T3 refusal from a parse refusal. Its S4 should assert the term label, T3, and that
the witness returned one row per scoped id.

## What this round did not cover

- Units outside G3 were read only where an edge or an interface named them: units 1, 2, 3, 4, 6, 7,
  22, 34 and 35. Nothing here clears units 1 to 14 or 21 to 36, PLAY-dDerivedDocket-1 or
  DEPL-dDerivedDocket-1. Entries H8, H9, M5, M6, M10, M12 and L6 name defects that also live in
  units 1, 4, 22 and 34. The fold for each must land in both specs at once.
- Three entries overlap other groups' round-1 entries, and the group folds must agree: H1 with G2's
  M4, H8 with G1's M16 and B2, and M12 with G1's M16 fix text.
- Whether units 16 and 17 will parse the TSV with `read` or with `awk` was not settled, because
  neither spec says. H2's field collapse depends on that. Its unpinned values do not.
- The design record's measured figures were not re-derived. The exceptions are the live-build-set
  premise (this build's folder is absent from `main` and `origin/main` while it runs) and the
  `status:` and `ids:` precedent in this build's own README history, both checked for this report.
- This round raised two questions and did not answer them.
  - Under in-place landing, where does a terminal record's endpoint come from for unit 19's walk and
    unit 18's arms, given that unit 22 S7 writes nothing at `--landed`?
  - Does the Skill's E3 route (unit 20 S5) need `--preflight` at all, once H5's fold puts the
    refusal ahead of every anchor read?
- The 28 refuted findings are not reproduced here. They were refuted, not lost, as the run-integrity
  counters show.
