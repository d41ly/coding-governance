# TOOL-dGatedProse-3 — the guide cap rises on both axes, with the reason recorded beside the figure

**Status:** CLOSED · rev-6 · 2026-09-22 · node d · Tier-2 · base bd44d3ff · streams tooling · order 4 · ratified 2026-09-21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md](../build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md) | research | TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-4 TOOL-dGatedProse-5 |
| [2026-09-22-build-TOOL-dGatedProse-3-1-acceptance-ledger.md](../build/2026-09-22-build-TOOL-dGatedProse-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md](../reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md) | spec-audit | TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-4 TOOL-dGatedProse-5 |
| [2026-09-22-review-TOOL-dGatedProse-1-closing-diff-review-round1.md](../reviews/2026-09-22-review-TOOL-dGatedProse-1-closing-diff-review-round1.md) | diff-review | TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-4 TOOL-dGatedProse-5 |

<!-- /gen:spec-records -->

## 1. Goal

Raise both declared guide-size caps together so the class has real headroom again, delete the debt row
that records the breach the raise removes, record the reason where a reader of the constant finds it,
and move the kit version once for the whole build, because the epoch rule puts that move here. The
owner ruled the raise on 2026-09-20 at `TOOL-dLoggedFlight-33` and named ONE key; the dry run measured
that moving that key alone is a raise in name only, because the line axis reds first, and this
build's research record carries that measurement at
`memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md:334`. Moving
two where the row names one is a divergence this unit discloses rather than absorbs: the row's own
wording is corrected at landing, by the route section 3 names. The owner ruled the pair on 2026-09-21
at 98304 bytes and 1200 lines, superseding the 81920 and 1000 ratified earlier that day once the
merged tree showed that pair buying about 32 days where about 49 had been weighed, so section 8's
first fork is closed by a decision and not by this unit's recommendation.

## 2. Scope (IN)

- **S1** — At `tools/memory-tree/check-memory-hygiene.sh:84`, both cap constants move together to the
  ratified pair of 98304 bytes and 1200 lines, with a dated reason block immediately above them
  naming the rulings, the measured growth rate and the headroom the figure buys. Observed by AC1,
  AC2 and AC14.
- **S2** — The four dogfood copies are REGENERATED from their templates and never hand-edited, after
  this unit's template edit in S4. The render is all-or-nothing over the four pairs, so this unit
  rewrites three live copies it has no edit in. Observed by AC4.
- **S3** — `tools/memory-tree/.memory-tree.conf.example:194` and the line below it move to the same
  pair as the engine, so a future adoption copies a conf that agrees with the default it overrides.
  Observed by AC5, on both keys.
- **S4** — Every live prose ASSERTION of the retired pair moves, by the route its record type allows.
  A template is edited and re-rendered. A mutable OPEN backlog row is corrected in place. The
  append-only decision rows, the CLOSED backlog rows and the one OPEN row that RECORDS a past
  measurement are left verbatim and superseded by one new decision row. Observed by AC6 and AC7.
- **S5** — `memory/project/curation-debt.txt` loses the `memory/guides/UNATTENDED-PROTOCOL.md` block
  at lines 55 to 69, and its header gains a drain line naming this unit and the new figure. Observed
  by AC8.
- **S6** — The self-test's guide fixture is regrown past the raised line cap, both of its check-6 arms
  are repaired in place, and the two fixture comments that spell the retired line cap in a fourth way
  move with them. No assertion is added, so this unit owes the suite no floor raise. Observed by AC9
  and AC10.
- **S7** — The `guides/*.md` row of the table at `memory/map/features/memory-tree-hygiene.md:51`
  carries the new figures, and stops calling the byte bound hardcoded. Observed by AC11.
- **S8** — The kit version. The value of `KIT_MEMORY_TREE_VERSION` at
  `tools/memory-tree/check-memory-hygiene.sh:20` is replaced by the next increment, ONCE for the whole
  build, in a commit of this unit's that lands at or after its engine commit — the placement the
  epoch rule requires and the reason this move is here rather than at order 2, in
  `TOOL-dGatedProse-1`. The marker
  `gov:kit memory-tree@` on that same line moves with it, as does every other carrier of the
  retired marker value, the population DERIVED by the grep in section 4 rather than listed. The four
  shipped templates are stamped on their line 1; the four dogfood copies are REGENERATED and never
  hand-stamped. Observed by AC3, AC4, AC12 and AC13.
  **Readers:** by name: `tools/memory-tree/kit.toml`, `tools/check-kit-versions.sh`,
  `tools/memory-tree/check-verdict-epoch.sh`, `tools/memory-tree/hygiene-parity.test.sh`.
  by value: `tools/check-kit-versions.sh`, `tools/memory-tree/check-verdict-epoch.sh`,
  `tools/memory-tree/hygiene-parity.test.sh`.
  Each of the four reads the constant's own spelling: `tools/memory-tree/kit.toml:6` names it as a
  `version_from` pattern, `tools/check-kit-versions.sh:130` greps it, and both
  `tools/memory-tree/check-verdict-epoch.sh:108` and `tools/memory-tree/hygiene-parity.test.sh:52`
  parse that line with a sed. Three of them then read the VALUE, and that is where this move is felt:
  `tools/check-kit-versions.sh:147` asserts the four template markers EQUAL it,
  `tools/memory-tree/check-verdict-epoch.sh:179` compares it at a commit against its parent, and
  `tools/memory-tree/hygiene-parity.test.sh:54` derives its baseline floor from whatever the current
  value is.

## 3. Non-goals (OUT)

**No second version move, and not the kit README's check count.** The build's rule is one move per
build; this unit owns it at S8, and `TOOL-dGatedProse-1` no longer performs it. What that unit keeps
is the `tools/memory-tree/README.md` check-count sentence, which it was coupling to the version at
rev-2: that sentence counts CHECKS, the marker grep never returns that file, and the unit that CHANGES
the number of checks is the unit that owes the count. This unit adds no check, so it does not touch
it.

**No re-wording of the ruling row by this unit's code.** `memory/backlog/TOOL.md:560` is
`TOOL-dLoggedFlight-33` and reads that `GUIDE_CAP_BYTES` is raised — one key, where this unit moves
two, and the Alternatives table below calls the one-key version the raise in name only. The row is a
mutable record whose status moves when the raise lands, so its correction is a build-level backlog
write at landing, in the same commit that closes it, and not a code change this unit makes. The
correction to write: both keys moved together, to 98304 and 1200, because the line axis binds first.
Unit 4 declares its own superseded row the same way, and this is that declaration.

**No rewrite of a landed or past-tense record.** `memory/DECISIONS.md:62` and `memory/DECISIONS.md:132`
are append-only. `memory/backlog/TOOL.md:368` is CLOSED, and both of its mentions narrate the state at
closure; `memory/backlog/TOOL.md:296` is CLOSED too, and narrates the guides' caps at the retired byte
value as they stood when it closed. `memory/backlog/TOOL.md:56` is OPEN but past-tense: it records what
three carriers measured when the pattern was found, which is the evidence the row exists to carry.
Rewriting any of them would rewrite a record rather than a claim, which is the discipline S4 is built
on.

**No repair of the dossier's own check-count disagreement.** `memory/map/features/memory-tree-hygiene.md:1`
calls the engine a 21-check gate and `:34` says 22 checks; both are wrong or one is, at base, before
this build touches anything. This unit edits that file's cap row and leaves the count alone: the unit
that CHANGES the number of checks is the unit that owes the count, and absorbing a sibling's line here
would put an author-facing correction in the hands of the unit whose rule it is not. Naming it is the
whole of what this unit owes it.

No structural remedy. A high-water ratchet that prices an addition, or a per-carrier eviction rule
that names what leaves when something arrives, is the answer to why every capped carrier in this tree
fills up. Both candidates stay parked at `TOOL-dFoldedVerdict-7`, uncosted, and this unit is the
stopgap the owner chose over them.

No split and no trim. The owner ruled against both on 2026-09-20. Trimming was never a local edit
anyway: `tools/unattended/adopt-unattended.sh:333` byte-compares the live guide against
`tools/unattended/PROTOCOL.template.md` and `:481` re-copies it, so cutting a sentence from the guide
means cutting it from the shipped kit.

No adopter migration. `tools/memory-tree/adopt-memory-tree.sh:59` copies the conf example verbatim, so
every EXISTING adopter's live conf already carries an explicit retired value and stays red after this
lands until they edit it themselves. S3 reaches future adoptions only. A release note or a conf
migration is owed and is not built here; it needs a backlog row of its own.

No parity gate over the prose restatements. Nothing compares any of the restatements to the constant
that owns the figure, and `tools/check-install-prefix.sh:15` deliberately drops `*.conf.example` from
its population, so S3's carrier is enforced by nothing either. That is a left-shift candidate and a
second mechanism; it gets a row, not this spec.

No repair of the dead key in the same dossier table. That table's last row at
`memory/map/features/memory-tree-hygiene.md:54` points at a cap key the engine never reads.
Correcting it reaches `.gitattributes:36` and the append-only row at `memory/DECISIONS.md:34` as
well, which is a wider population than this unit's mechanism. (The key is `ROW_DOC_CAP_BYTES`,
written here in a sentence of its own: unit 2's new join refuses a backticked dossier subject
governing a backticked SHOUTED object, and rev-1 put the two in exactly that relation.)

### Edges

- **consumes-from** `TOOL-dGatedProse-1` — that unit lands at order 2, before this one, and edits
  the same engine file and the same self-test. What it LEAVES this unit is four things, none of them
  asserted here. **The new check 25, live and grading this spec**, because the owner declared no
  `READER_INVENTORY_CUTOFF` on 2026-09-21, so its population is every live spec from that unit's
  commit; S8 carries a `**Readers:**` clause for that reason and section 7 lists the leg that grades
  it. **The suite's assertion floor**, raised by the count of assertions that unit ADDS, which AC10
  reads rather than pins. **The four dogfood pairs already rendered and in sync**, from its own
  catalog-entry edit, at the marker value of the pinned base. And **the line offsets**: that unit
  adds a fixture block to the self-test and its check-25 branches to the engine, and either can sit
  ABOVE coordinates this spec cites. Every `path:line` here is a base-`bd44d3ff` coordinate and is
  re-resolved by grepping its anchor string before the edit. Nothing gates that:
  `tools/check-spec-tokens.py:594` resolves a citation against the file's line COUNT and reds at
  `:600` only when the number is out of range, so a citation that slid four lines passes, which is
  the class section 10 records five prior instances of. What that unit NO LONGER does is the version
  move and the marker re-stamp: they were its rev-2 S9 and are this unit's S8, because the epoch
  rule is topological and that unit's commit is not the last one in this build to move a
  behaviour-bearing engine line. The constant it leaves therefore still reads the base value, which
  S8 moves and AC3 observes.
- **consumes-from** `TOOL-dGatedProse-2` — that unit changes `memory/TEMPLATE-SPEC.md`, which is one
  of the four dogfood copies S2 and S8 regenerate. Its change must live in
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, or the render deletes it. This is not advice: the
  render loop iterates the whole PAIRS table, so ANY unit that renders overwrites all four live
  copies from their templates, whichever one it edited. Its `claims` join is the second predicate
  the owner left without a cutoff, so it too grades this spec from its own commit.
- **hands-off** `TOOL-dGatedProse-4` — for the same reason, the render rewrites
  `memory/guides/BUILD-METHOD.md` from `tools/memory-tree/BUILD-METHOD.template.md`, so that unit's M4
  edit goes through the template, and it renders again after its own edit. The re-stamp half of that
  render is byte-neutral, and the arithmetic is now this unit's to state rather than a sibling's: both
  version spellings are four bytes, so S8 spends none of the headroom that guide has against its
  `tools/template-size-limits.txt:86` row. Two size bounds grade that guide, and neither couples the
  two units. This unit's guide-class pair is the loose one: the file is 27641 B and 352 lines at
  base, 28.1% and 29.3% of the ratified pair, and that unit's own figures after its edit, 27936 B and
  352 lines, stay under 30% of both halves. The per-subject row is the tight one, and it moves in
  that unit's budget raise, on the owner's ruling of 2026-09-21, together with M1's line figure,
  whose rise the owner ruled the same day. That raise is named here by what it does and not by its
  scope label, because at that unit's rev-3 the same label named a different item, the pointer
  repair to the review protocol that its rev-4 deleted. One file is written by both units: each
  appends one row to `memory/DECISIONS.md`, which is row-keyed and append-only, so the two rows land
  additively and neither supersedes the other.
- **consumes-from** external — the owner's rulings of 2026-09-20 and 2026-09-21, and the dry-run
  measurement recorded at
  `memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md`, whose
  Strand 5 carries every dry-run figure this spec cites: the growth rate at `:331`, the narrowing at
  `:334` and the two candidate pairs at `:337` to `:339`. The 2026-09-20 ruling authorizes the raise
  and the row removal. On 2026-09-21 the owner ratified 81920 and 1000 and, the same day, re-ruled
  the pair to 98304 and 1200, for the reason section 8 records; this unit grants itself neither
  figure. Both 2026-09-21 rulings reached this spec as the main loop's relay of the owner's own
  conversation, and no decision record carries either yet: the row AC7 reads, which the build pass
  writes citing both, is their first.
- **hands-off** external — three writes this unit does not make: the adopter migration and the
  prose-parity gate named above, each owed a backlog row this unit does not mint, and the re-wording
  of `memory/backlog/TOOL.md:560` at landing. One consequence it does not repair either: after S8,
  `tools/memory-tree/hygiene-parity.test.sh` has no legal baseline until the next engine rewrite, and
  section 4 records that its own header declares this.

## 4. Design

### Data model

Two constants on one line, and nothing else decides the verdict. Check 6 compares with
`b>cb || (cl>0 && l>cl)`, so the two axes are independent and either one alone reds a file.

| key | retired | ratified | why |
|---|---|---|---|
| `GUIDE_CAP_BYTES` | 61440 | 98304 | 96 KiB; 33365 B of headroom, which is 62.3 days at the measured rate |
| `GUIDE_CAP_LINES` | 750 | 1200 | 98304 divided by 81.92, so the per-line allowance is preserved exactly |

**Where the two figures come from.** 98304 is 96 KiB, and it is also exactly eight fifths of the
retired 61440; 1200 is exactly eight fifths of 750. The ratified pair is therefore the retired pair
under ONE scalar, which is why the allowance below survives by construction rather than by a second
calculation. The pair the owner first ratified, 81920 and 1000, is the same construction at four
thirds. The owner ruled this pair on 2026-09-21 over both that one and the conservative alternative,
so the figures are a decision and the arithmetic is only the derivation.

**The headroom each axis buys, at the measured rate.** 98304 minus the file's 64939 B leaves 33365 B,
which is 62.3 days at 535.4 B per day. 1200 minus its 704 lines leaves 496, which is 177.1 days at
2.80 lines per day. The byte axis therefore stays the binding one by a factor of about 2.8, which is
what the design wants: one axis should decide, and it should be the one whose remedy is
prose rather than reformatting.

**Where the rate comes from, and the rate that is deliberately not used.** Measured over this file's
own history on the rebased base: the last intervention is `dc9431f8` on 2026-09-01, which left it at
54231 B and 648 lines, and on 2026-09-21 it is 64939 B and 704 lines. That is 20 days, 10708 B and
56 lines, so 535.4 B per day and 2.80 lines per day. Part of that growth arrived through the
reconcile merge rather than on this branch, which is how this file has always grown: the debt row
itself records a merge-induced overflow. The all-history rate over the same probe is 1303 B per day,
and it is NOT the basis: it spans the guide's authoring era, where a contract was being written rather than
maintained. The post-intervention refill rate is the defensible one for a stopgap, because what this
figure has to survive is refilling, and it is the more conservative of the two for a raise as well.

**Why both.** Measured on this tree, `memory/guides/UNATTENDED-PROTOCOL.md` is 64939 B and 704 lines.
Against the retired pair that is 3499 B over on bytes and 46 lines free on lines. Those 46 lines are
the whole of the line axis's remaining life: at the measured 2.80 lines per day they are spent in 16
days, whatever the byte figure says. A byte-only raise therefore expires inside one build, which is
the failure it was meant to prevent. Where exactly it stops paying depends on which density you
assume, and the two defensible bases disagree by about 4.5 KB: at the file's average 92.24 B per line
the 46 lines cost 4243 B and the break-even is 69182 B, while at the marginal 191.2 B per line
observed over the growth window they cost 8796 B and it is near 73700 B. The choice between those
bases does not change the conclusion, so this spec states the range rather than picking one.

**Why the allowance is preserved.** 61440 divided by 750 is 81.92, and 98304 divided by 1200 is 81.92.
Moving one key without the other silently re-decides how many bytes a line of a guide may carry, and
the engine's own comment above these constants warns that an unvalidated change here reds everything
or nothing with no message.

**The cap still binds something.** Six of the seven guides sit between 7.8% and 45.0% of the retired
byte cap, so this cap has only ever bound one file. At the ratified figure the second-largest guide
moves to 28.1%. The raise does not relax a constraint any other guide was under, and it consumes none
of the headroom it grants: no guide gains a byte.

### Inventory, and the codebase-map obligation

This unit mints no identifier. Both cap keys and the version constant already exist, no leg is added,
no function is written. The only new tracked text is one appended row in `memory/DECISIONS.md`, the
dated comment block above the constants, and one changed version string.

**It claims no new inventory key of the codebase map, and here is why rather than only that.** The
map's enumerated key kinds are gate-legs, kits, git-hooks, workflow-scripts, skill-engines,
rendered-skills, gotcha-classes, guides, backlog-shards and lexicon-verbs, and this unit adds no
member of any of them — no leg, no kit, no hook, no script, no skill, no gotcha class, no guide, no
shard, no verb. The kit files it edits are already inside the dossier's own
`[paths]` globs, declared at `memory/map/features/memory-tree-hygiene.md:25`, so no glob moves either.
The appended decision row is not a claim: a dossier's `decisions` list is validated for ID GRAMMAR
alone, at `tools/codebase-map/map_lib.py:1032`, and never for completeness. What this unit does owe
the map is the prose in S7, which is a table cell and not a claim block, so no generated artifact
moves with it.

### The version move is this unit's, and the epoch rule is what places it here

Re-derived from source rather than from a ruling, because this is the one placement the build got
wrong once already. `tools/memory-tree/check-verdict-epoch.sh:16` states the rule and `:179`
implements it: let W be the NEWEST commit in `<base>..HEAD` that moves a behaviour-bearing line of the
scan set, and S the NEWEST commit in that range that actually CHANGES the constant's value; W must be
an ancestor of, or equal to, S. The scan set is declared at `:68` and `:69` — the engine plus six
delegate modules — and accumulated at `:71`; W is walked newest-first at `:129` over that whole set,
while S is searched at `:150` over the engine alone.

Verified against the build's five write sets, each read from that spec's own Files touched: S1 moves
two non-comment lines of the engine at order 4, `TOOL-dGatedProse-1` moves many more at order 2, and
NONE of the other three units touches any file in the scan set. Unit 5's set is the live specs it
writes clauses into, its census record under this build's build folder and the regenerated build
README. Unit 2's is `tools/check-spec-tokens.py` and its suite, the spec template
`tools/memory-tree/SPEC-TEMPLATE.template.md` with its render `memory/TEMPLATE-SPEC.md`, its
dossier, and `memory/backlog/TOOL.md`, whose row its landing re-words. Unit 4's is five paths: the build-method template and its render,
`tools/template-size-limits.txt`, the dossier `memory/map/features/build-method.md` and one appended
row in `memory/DECISIONS.md`. None of those is the engine or one of the six delegates named at
`tools/memory-tree/check-verdict-epoch.sh:69`. So this unit's engine commit is the LAST
behaviour-bearing scan-set change in the build, and every legal S is at or after it. A single move
at order 2 makes W a descendant of S, the ancestry test at `:179` fails, and the leg
— subject `repo`, guard `None`, so on every bar — reds from this unit's commit through the build's
tip. That is what the earlier ruling would have produced and it is why the move is here.

Two consequences worth stating rather than discovering. The bump commit DATES ITSELF: the constant
sits on a non-comment line of the engine, so a commit that changes only the version is itself a
behaviour-bearing scan-set change, which makes W and S the same commit and the ancestry test trivially
true. And the move may sit in this unit's engine commit or in a later one of its own; both satisfy the
rule, and the ruling's own-commit shape is the one specified here.

### The marker population, and why it is derived and not listed

The population is `git grep -lF "gov:kit memory-tree@$OLD"` with `$OLD` read from the constant at the
commit's parent, never a written list. At the retired base it returned the carriers — the engine,
the four shipped `tools/memory-tree/*.template.md` templates and the four rendered copies
`memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/ANNOTATION-STYLE.md` and
`memory/guides/BUILD-METHOD.md` — plus one build record, a sibling spec that spells the literal
marker in its own prose. At the rebased base, where the constant reads 2.82, it returns the same
carriers and no build record, because that spec spells a value the grep no longer asks for. So the
population is tracked files OUTSIDE the build-record class, for the same reason the cap passes below
exclude it: a spec is not a carrier, and a landed one is never rewritten. The two readings differ,
which is the argument: the exclusion is the rule and the build re-derives the set at the commit. This spec
deliberately does not spell that literal string, which is how a spec joins its own population.

Two shapes inside the population, each costing a step if missed. The constant and the marker share
ONE line at `tools/memory-tree/check-memory-hygiene.sh:20`, so an edit keyed on the key name alone
leaves the marker behind — AC3 greps both. And the four rendered copies are OUTSIDE the glob
`tools/check-kit-versions.sh:135` derives its population from, so a hand-stamped render would pass
that leg and red `kit/dogfood doc parity` instead. They are regenerated, not stamped.

### The render direction, and the number of renders this build runs

`sed -n 58p tools/memory-tree/kit-dogfood-parity.test.sh` prints the PAIRS table: which live copy
renders from which template. Its loop at `:100` iterates the whole table in every mode, so:

```bash
bash tools/memory-tree/kit-dogfood-parity.test.sh --render
```

rewrites ALL FOUR live copies from their templates, not only the HYGIENE pair this unit edits. That
is why both sibling edges bind, and it is the only way to know the renders must be produced by a
command rather than typed. The script's header states the direction plainly, template to live, and
the `kit/dogfood doc parity` leg byte-compares each pair afterwards.

This unit runs it ONCE PER COMMIT THAT MOVES A TEMPLATE, which is both of its commits: the cap commit
carries S4's template figure edit, and the S8 commit carries the marker re-stamp. Each commit
therefore leaves the four pairs byte-identical, rather than leaving an intermediate commit whose
template and render disagree.

### What the bump costs the parity harness, declared rather than discovered

`tools/memory-tree/hygiene-parity.test.sh:54` derives its baseline floor as the first commit
introducing the CURRENT version, and `:64` refuses any baseline older than that floor. After S8 the
only baseline at or after the floor is the bump commit itself, which trips that harness's own
same-bytes guard. This is not a break and not this unit's to repair: the harness's header says so at
`:26`, in those words, and `:10` records that it is deliberately NOT a gate leg, so no leg reds and
nothing on the bar moves. It is stated here because a reader who runs it next week will otherwise read
a refusal as a regression this unit caused.

### The population the FIGURE reaches, and how it is derived

This is a SEPARATE derivation from the marker grep above, and neither finds the other's carriers: the
passes below are keyed on the cap figure and would not return a version marker, and the marker grep
would not return a prose restatement of a byte cap.

Deriving this by the VALUE is wrong, and that is the whole lesson of `TOOL-dBriefedPass-8`:
`INDEX_CAP_BYTES` is numerically identical at 61440, which is exactly why a mis-attribution survived
every reading once already. A bare tree-wide search for the number returns `INDEX_CAP_BYTES` carriers
that must NOT move. Four passes, in this order:

```bash
X="-- . :!memory/archive/** :!memory/builds/**"
git grep -nE 'GUIDE_CAP_(BYTES|LINES)'             $X   # pass 1 — by key name
git grep -nE '60 KB'                               $X   # pass 2 — by the prose spelling
git grep -nE '61440 */ *750|61440B/750L|750 lines' $X   # pass 3 — by the pair, spelled three ways
# pass 4, SCOPED: the bare numbers, over ONLY the files passes 1-3 already implicated
git grep -nE '(^|[^0-9])(61440|750)([^0-9]|$)' -- $(
  { git grep -lE 'GUIDE_CAP_(BYTES|LINES)'             $X
    git grep -lE '60 KB'                               $X
    git grep -lE '61440 */ *750|61440B/750L|750 lines' $X ; } | sort -u )
```

The fourth pass is SCOPED to the files the first three return, and it is scoped both ways. Run not at
all it misses two live carriers inside a file this unit edits. Run tree-wide it returns the
`INDEX_CAP_BYTES` carriers the fourth non-goal keeps out. Even scoped it OVER-returns, by
construction — lines that spell one of the two bare numbers about something else — and those are
routed below rather than left for the observer to re-judge. The
exclusions on the first three are the frozen classes: `memory/archive/` is exempt from check 6 by
class, and a landed build record is never rewritten.

Each carrier takes the route its record type allows, and every line the four passes return is
accounted for here — including the ones with nothing to move, because an unlisted hit is
indistinguishable from an unnoticed one:

| carrier | route |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh:84` | the owner of the figure; edited |
| `tools/memory-tree/.memory-tree.conf.example:194` and `:195` | edited, both keys |
| `tools/memory-tree/HYGIENE.template.md:70` and `:164` | edited, then rendered through |
| `memory/HYGIENE.md:70` and `:164` | never hand-edited; produced by S2's render |
| `memory/map/features/memory-tree-hygiene.md:51` | edited |
| `memory/backlog/TOOL.md:233` | OPEN row asserting the line bound; corrected in place, with its comparative |
| `memory/backlog/TOOL.md:354` | OPEN row asserting a live percentage of the byte cap; re-measured in place |
| `memory/backlog/TOOL.md:560` | the ruling row; re-worded and closed at landing, not by this unit |
| `memory/backlog/TOOL.md:56` | OPEN row RECORDING a past measurement; left verbatim |
| `memory/backlog/TOOL.md:368` and `:296` | CLOSED rows; left verbatim |
| `memory/DECISIONS.md:62` and `:132` | append-only; left verbatim and superseded |
| `memory/project/curation-debt.txt:56`, `:57` and `:67` | inside the block S5 deletes |
| `tools/memory-tree/check-memory-hygiene.test.sh:1149` | an expected string; repaired with its arm |
| `tools/memory-tree/check-memory-hygiene.test.sh:547` and `:549` | fixture comments; moved with the fixture |
| `tools/memory-tree/check-memory-hygiene.sh:121` and `:733` | the key NAMES, no figure; nothing to move |
| `tools/memory-tree/check-memory-hygiene.test.sh:2057` and `:2103` | regions declaring their OWN caps; nothing to move |
| pass 4's over-returns | `INDEX_CAP_BYTES` carriers, per-fixture conf declarations and one unrelated count of 750 things; nothing to move, and the reason pass 4 is scoped |

**One carrier needs more than its figure changed.** `memory/backlog/TOOL.md:233` reads that the
hygiene cap for a guide is 750 lines, "ten times looser" than the 250 the build-method guide declared
for itself when the row was written. The multiplier is already wrong at base — 750 against 250 is
three times — and no multiplier survives this build. M1 states 350 lines at base, at
`memory/guides/BUILD-METHOD.md:8`, not 250, and `TOOL-dGatedProse-4` moves that figure to 370 at
order 5, one unit after this edit, on the owner's ruling of 2026-09-21 that the method's line half
rises with its byte cap. So the clause takes the figure 1200 and a comparative with no number in it,
far looser than the method's own line figure, which stays true across both moves. Changing the
number and leaving "ten times" would ship a corrected figure inside a sentence that is still false,
so both move, in the same clause and the same edit.

**The union is still incomplete, and the gap is worth naming rather than discovering.** The pair grep
misses `memory/map/features/memory-tree-hygiene.md:51` because that row is a markdown table cell whose
two figures sit in different columns, so only the `60 KB` pass reaches it. The third pass misses
`tools/memory-tree/check-memory-hygiene.test.sh:547` and `:549`, which spell the line cap as "the
guide cap of 750" and "whether the guide cap were 750" — reachable only by the fourth, scoped pass,
and live inside a file S6 edits. A carrier that spells the number in a FIFTH way is reachable by none
of the four. Nothing gates any of this, which is why the parity gate is a declared follow-up and not
a claim of coverage.

### Where the reason is recorded

Three homes, three different readers, and the primary one is beside the figure.

1. **Beside the figure.** A dated comment block immediately above
   `tools/memory-tree/check-memory-hygiene.sh:84`, naming the rulings, the merge-induced overflow, the
   measured growth rate, the headroom in days, and the fact that BOTH keys moved and why a byte-only
   raise would have been short-lived. This is what a reader of the constant sees, it ships to every
   adopter, and the sibling constants in the same block already carry their reasons this way. AC14
   reads it.
2. **The corpus answer to why.** One appended row in `memory/DECISIONS.md`. Both prior movements of
   this value are recorded there, at `memory/DECISIONS.md:62` and `:132`, and the second of those is
   itself a re-argument of the first. A third movement absent from that file leaves
   `TOOL-dSpentCeiling-3` as the newest word on a value it no longer describes.
3. **The registry's own narration.** A drain line in the header of `memory/project/curation-debt.txt`,
   in the shape line 9 already uses, naming this unit and the new figure. No gate enforces it and the
   file stops explaining itself without it.

### The debt row, and why its removal is not tidying

`memory/project/curation-debt.txt:69` lists the protocol today, so `derive_waived` moves the finding
out of the failing set and check 6 PASSES on this tree right now. The raise is not clearing a red; it
is exchanging a recorded waiver for a raised cap, and the row's deletion is the raise's only visible
effect on this tree. The stale-entry guard at `tools/memory-tree/check-memory-hygiene.sh:1944` then
reverses the obligation: a listed path that passes checks 6, 7 and 8 unwaived is a row that hides
nothing, and line 1955 fails check 6 telling you to delete the row rather than re-justify it. The
registry's own header declares this condition, and the row's last line at `:67` names its drain as
"the contract is split again or the cap is re-argued".

**One timing trap.** That guard is held under the staged selection by the condition at line 1944, so a
pre-commit run is green with the stale row still present while the full-tree run reds. A clean commit
is not clearance for this edit.

### The two self-test arms, and the floor they do not move

The suite builds a 761-line guide fixture at `tools/memory-tree/check-memory-hygiene.test.sh:544` and
asserts two things about it. Line 1143 asserts check 6 NAMES it; line 1149 asserts the message spells
both halves of the bound. At a 1200-line cap that fixture is silent, so both arms fail — the fixture
must be regrown past the new line cap and the expected string rewritten to the new pair. Its two
explanatory comments at `:547` and `:549` restate the retired cap in prose and move with it. The rest
of the check-6 arms survive: the region at `:2057` declares its own cap explicitly rather than reading
the default, and the green counterpart fixture at `:551` is 401 lines and stays between the two class
caps, which is the comparison that arm exists to make.

**The floor.** The build's convention is that a unit ADDING assertions to a suite raises that suite's
own floor by the count it adds, with the comment naming the unit, in the same commit. This unit adds
none: two arms are repaired in place and the fixture's row count changes, not the assertion count. So
it owes no raise, and the only movement the floor sees this build is `TOOL-dGatedProse-1`'s.

**This breakage is invisible on an ordinary bar.** `memory-hygiene self-test` is subject `kit`, chunk
`selftests`, guarded on `tools/lib/` and `tools/memory-tree/`, so it runs only under the kit-work
Definition of Done. A build can land this raise with two dead arms and a fully green bar. That is this
repo's own guarded-legs-hide-latent-failures class, and it is why AC9 observes the engine on the
fixture directly instead of trusting the suite's verdict.

### Alternatives rejected

| option | why not |
|---|---|
| move `GUIDE_CAP_BYTES` alone, as the ruling row's wording says | inert within about 16 days; the line axis reds first at 704 of 750 |
| a per-repo override in this repo's `.memory-tree.conf` | `tools/unattended/adopt-unattended.sh` installs a byte-identical protocol into every adopter of both kits, so a local override fixes this tree and leaves them red on install day |
| raise `INDEX_CAP_BYTES`, which is also 61440 | the wrong key; it gates row documents and not this file, and `TOOL-dBriefedPass-8` records this exact confusion surviving a full reading |
| 81920 and 1000, the pair first ratified | buys 16981 B, which is 31.7 days on the merged tree against the 48.9 weighed at the old base; superseded by the owner's re-ruling of 2026-09-21, and section 8 keeps it with both measurements |
| 73728 and 900, the conservative pair | buys 8789 B, which is 16.4 days on the merged tree; refused by the owner on 2026-09-21, and section 8 records it with the figures the first ruling weighed and their re-measurement |
| cap the bytes at the break-even and leave the lines | buys the shorter of the two lives and re-decides the per-line allowance by accident |
| the single version move at order 2, in `TOOL-dGatedProse-1`, one per build but placed before this unit | topologically illegal: W is then a descendant of S, the ancestry test at `tools/memory-tree/check-verdict-epoch.sh:179` fails, and an unguarded `repo` leg reds from this unit's commit through the tip |

### Files touched

DERIVED, not counted here. The set is the live carriers the four passes return, minus the ones the
route table marks "nothing to move", plus the marker population of S8, plus one appended decision row
and the live copies the two renders rewrite without editing. Re-run the passes and the marker grep at
build time; a count written beside a derived population is wrong on the next commit.

## 5. Production-readiness checklist

- security — N/A. No write path, no input boundary and no authorization surface. The edit is three
  integers, a comment and prose.
- perf / scale — no added cost on any bar, and this is structural rather than a timing claim. The
  raise moves two awk bindings inside a comparison check 6 already runs over the same population. No
  file is newly read, no process is newly spawned, no leg is added.
- error / empty / loading states — N/A for a constant. The engine already refuses a malformed or zero
  byte cap and validates each binding before awk sees it, and the arms for that live at
  `tools/memory-tree/check-memory-hygiene.test.sh:2103`.
- observability — the reason block at the constant and the drain line in the registry are the whole of
  it. A later reader who asks why the figure is 98304 finds the answer on the line above it.
- risks — four, and each is named where it bites. The version move must land at or after this unit's
  engine commit or `verdict epoch` reds through the build's tip, which AC12 observes and section 4
  derives from source. The render rewrites three live copies this unit has no edit in, so a sibling
  that hand-edited a render loses it. The two self-test arms break inside a held suite, so a green bar
  does not clear them. Existing adopters are unreachable by either cap edit and stay red until they
  edit their own conf. One non-risk, stated because it looks like one: the parity harness loses its
  baseline, by its own declared design, and no leg reads it.
- testing — the observations in section 6 run the checker directly, on this tree and on a scratch tree
  built from the conf example. Two existing arms are repaired; no arm is added and the floor does not
  move.
- migration — none for this repo. For an adopter, see the adopter-migration non-goal.
- user docs — N/A. No user-facing feature, so no `help/` page. The adopter-facing text is the conf
  example's own comment, which S3 moves with the value.

## 6. Acceptance criteria

- **AC1** — When `tools/memory-tree/check-memory-hygiene.sh` runs over this tree with the protocol's
  debt block already deleted, check 6 names no file under the guides directory.
  Red when: the block is deleted and the byte key keeps its retired value, so check 6 names
  `memory/guides/UNATTENDED-PROTOCOL.md` at its measured size against 61440 B. The line key is
  observed by AC5, whose fixture sits above the retired line cap.
  figure: DERIVED — the file's size is read at observation time, not taken from this spec.
- **AC2** — When the two constants at `tools/memory-tree/check-memory-hygiene.sh:84` are read and
  divided, the quotient is 81.92, the same per-line allowance the retired pair carried.
  Red when: one key moved and the other did not, which is the byte-only raise the ruling row's
  wording would have produced; the quotient then reads 131.07 or 51.2.
  figure: DERIVED — both constants are read from that line at observation time.
- **AC3** — When `grep -n 'KIT_MEMORY_TREE_VERSION=' tools/memory-tree/check-memory-hygiene.sh` runs
  at the build's tip, the value differs from the value at the pinned base, and a grep of that same
  line for the marker at the NEW value returns 1.
  Red when: the constant moves and the marker on that same line does not, which
  `tools/check-kit-versions.sh` cannot see at all because its population is the four templates.
  figure: DERIVED — both the old and the new value are read from the tree, never copied from this
  spec, so a build that lands at a different increment still observes correctly.
- **AC4** — When `tools/check-kit-versions.sh` runs, it prints no line about a
  `gov:kit memory-tree@` marker; and when the four live copies are compared against their templates
  rendered, each pair is byte-identical.
  Red when: a SHIPPED template's marker is not equal to the constant. That is the only half
  `tools/check-kit-versions.sh` can report: its population is set at `tools/check-kit-versions.sh:135`
  to the tracked `tools/memory-tree/*.template.md` files, four of them, and the comparison fails at
  `:147`. The four RENDERED copies are outside that glob, so a hand-edited or stale render cannot make
  that checker print anything — that half belongs to `kit/dogfood doc parity`, and it is the half the
  render can actually break.
  permission: the pair comparison is a kit suite, so it is named as a leg here rather than invoked as
  an observation.
- **AC5** — When `tools/memory-tree/check-memory-hygiene.sh` runs in a scratch tree whose
  `.memory-tree.conf` is a verbatim copy of `tools/memory-tree/.memory-tree.conf.example` and whose
  guides directory holds a fixture of 1100 lines and 90000 bytes, check 6 is silent.
  Red when: the example keeps EITHER retired value, or either half of the 81920 and 1000 the
  re-ruling superseded, so a copied conf overrides the raised engine default back down on that axis.
  The fixture sits above both stale pairs and within the ratified one, 1100 lines against 750, 1000
  and 1200 and 90000 B against 61440, 81920 and 98304, so each key alone reds it at either stale
  value. On the protocol itself, a retired byte key reds a fresh adopter of both kits on install day
  and a retired line key reds it at line 751.
  fixture: the scratch tree is built by the observation; this tree holds no such fixture today.
  cost: seconds.
- **AC6** — When the four passes of section 4 are re-run over tracked files outside the archive and
  build-record classes, every line that ASSERTS a current guide bound spells the ratified pair of
  98304 and 1200. The lines that RECORD a past measurement or a superseded ruling are unchanged and
  are exactly these: `memory/DECISIONS.md:62`, `memory/DECISIONS.md:132`,
  `memory/backlog/TOOL.md:56`, `memory/backlog/TOOL.md:296` and `memory/backlog/TOOL.md:368`.
  Red when: a live assertion is missed, or spells the 81920 and 1000 the re-ruling superseded, which
  pass 1 returns on every key-name line — or the exemption is stretched to cover
  `memory/backlog/TOOL.md:354`, which asserts a PRESENT-tense percentage of the byte cap, is already
  wrong at base, and so is a second stale claim rather than a preserved record. Red also when the
  four passes are replaced by a bare tree-wide search for the value, which reports `INDEX_CAP_BYTES`
  lines as carriers and reads the dossier's split table cell as clean.
  figure: DERIVED — the passes are re-run at observation time and no file count is pinned.
  scope: pass 4 over-returns, so the observation reads its output against the route table's
  over-return row and not as a finding list; an `INDEX_CAP_BYTES` carrier surfacing there is the
  derivation working, not a miss.
- **AC7** — When `memory/DECISIONS.md` is read, exactly one new row names this unit, the ratified
  pair, the measured growth rate and the headroom in days, and cites the owner's rulings of
  2026-09-21 that ratified a pair and then re-ruled it.
  Red when: the raise is recorded only in the engine comment, so the value's third movement is absent
  from the file carrying its first two and `TOOL-dSpentCeiling-3` stays the newest word on it; or the
  row states the superseded 81920 and 1000 as the pair.
- **AC8** — When `tools/memory-tree/check-memory-hygiene.sh` runs in full-tree mode, its curation-debt
  stale-entry guard names no path, and `memory/project/curation-debt.txt` holds four path rows and a
  header line naming this unit as the drain.
  Red when: the cap rises and the block stays, so the guard names
  `memory/guides/UNATTENDED-PROTOCOL.md` as a row that hides nothing.
  permission: the guard is held under the staged selection, so only the full-tree run observes this.
- **AC9** — When `tools/memory-tree/check-memory-hygiene.sh` runs over the guide fixture the suite
  builds at `tools/memory-tree/check-memory-hygiene.test.sh:544`, it names that fixture and prints
  both halves of the ratified pair.
  Red when: the fixture is left at its current row count, so at the raised line cap check 6 is silent
  and the arm at `tools/memory-tree/check-memory-hygiene.test.sh:1149` asserts a string the engine
  never prints.
- **AC10** — When the diff is read, it adds no assertion to the memory-hygiene fixture suite —
  written unbackticked here on purpose, because a bare suite path inside an acceptance bullet is what
  the bar join refuses — and the floor at
  `tools/memory-tree/check-memory-hygiene.test.sh:2478` is unchanged from the value
  `TOOL-dGatedProse-1` left.
  Red when: an arm is deleted rather than repaired and the floor is lowered to match, which is the
  green-by-absence shape that floor exists to catch.
  figure: DERIVED — the floor is READ from that line after unit 1 lands, never pinned here. It
  measured 374 at base `bd44d3ff`, and the build's convention raises it only by the count of
  assertions a unit ADDS, so unit 1's raise is the one movement it sees and this unit owes none.
- **AC11** — When `memory/map/features/memory-tree-hygiene.md:51` is read, its `guides/*.md` row
  spells the ratified byte and line bounds and no longer calls the byte bound hardcoded.
  Red when: the figures are corrected and the word stays, which asserts the conf cannot override a key
  that `tools/memory-tree/.memory-tree.conf.example:194` declares.
- **AC12** — When the marker grep of section 4 is re-run at the build's tip for the RETIRED value, it
  returns no tracked file outside the build-record class; and
  `bash tools/memory-tree/check-verdict-epoch.sh <the build's base>` exits 0 there.
  Red when: the value moves in a commit BEFORE this unit's engine commit, so W is a descendant of S
  and the leg reds from that commit through the tip; or a carrier is left behind, which the grep
  reports by name.
  liveness: this probe can return the other answer, and that is checked rather than assumed. Stage
  the bump ahead of the engine edit in a scratch clone and the leg prints both shas and exits 1; the
  checker's own header at `tools/memory-tree/check-verdict-epoch.sh:21` records its first cut — an
  endpoint comparison — being reproduced and refuted, so a reassuring `clean` is not the only verdict
  this mechanism can print.
  figure: DERIVED — `$OLD` is read from the constant at the commit's parent, so the grep cannot go
  stale against a different increment.
- **AC13** — When each name in S8's `**Readers:**` clause is opened, it reads the constant: the four
  in the by-name half name its spelling, and the three in the by-value half compare or derive from its
  VALUE. Neither escape spelling is used, because both halves are non-empty.
  Red when: a name is listed that merely MENTIONS the key. The measured instance is
  `tools/memory-tree/corpus_ids.py`, which a grep for the key name returns and which reads nothing:
  its line 67 records a version comparison that module deliberately does NOT make, on the measured
  ground that this engine went 2.41 to 2.46 in under two days. It is excluded for that reason, and a
  clause listing it would be a reader inventory that is wrong in the direction the check cannot see.
  permission: the standing observation is `TOOL-dGatedProse-1`'s check 25 on the `memory hygiene`
  leg, which grades this spec's own §2 items from that unit's commit because the owner declared no
  cutoff on 2026-09-21. This criterion is the author-time reading of the same clause.
- **AC14** — When the comment lines immediately above the `GUIDE_CAP_BYTES=` line of
  `tools/memory-tree/check-memory-hygiene.sh` are read, contiguous up to the first non-comment line,
  they form one block that carries a date, names `TOOL-dLoggedFlight-33`, names both
  `GUIDE_CAP_BYTES` and `GUIDE_CAP_LINES` as moved, and states a growth rate in bytes per day and the
  headroom the raise buys in days.
  Red when: the constants move with no block above them, or with a block that omits the ruling, names
  one key, or states no rate or no headroom. AC1, AC2, AC7 and AC8 all stay green on each of those,
  which is how the primary home of the reason went unobserved at rev-3.
  figure: DERIVED — the rate and the headroom are section 4's method re-run at the build's commit,
  not this spec's readings, because the file keeps growing between the two.

## 7. Gates

The legs this unit must keep green, with every guard READ from the manifest rather than assumed.
Six of them are subject `repo` and carry no guard at all, so they run on every bar: memory hygiene,
verdict epoch, kit version markers, testsuite counts, codebase-map coverage and freshness, and spec
tokens. Two of those six now arm on this unit's OWN edit rather than a sibling's, because S8 moved
here: kit version markers grades the four template stamps against the constant this unit changes, and
verdict epoch grades where that change sits. The seventh, kit/dogfood doc parity, is subject `repo`
too but DOES carry a guard — six paths, among them the live HYGIENE and TEMPLATE-SPEC copies, both
rendered guides, `tools/lib/` and `tools/memory-tree/` — and scope items S1, S2, S4, S6 and S8 each
touch one, so it arms on this unit's bar either way. Two more are subject `kit` and chunk
`selftests`, both guarded on `tools/lib/` and `tools/memory-tree/`, so both are held by default and
owed only by the kit-work Definition of Done: the memory-hygiene self-test, whose two check-6 arms
this unit repairs, and the verdict-epoch self-test, which rev-2 omitted and which belongs here now
that this unit moves the constant that checker reads. Leg names in this paragraph are deliberately
unbackticked prose; the graded list is the single line below, where each name is spelled as the
manifest spells it.

`memory hygiene` · `verdict epoch (kit version dates the engine)` · `kit version markers` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `verdict-epoch self-test` · `testsuite counts (every bar self-test prints one)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

One of those legs grades this SPEC and not only this unit's code. With no
`READER_INVENTORY_CUTOFF` and no `SPEC_CLAIMS_CUTOFF` declared, unit 1's check 25 and unit 2's
`claims` join both take every live spec as their population from their own commits, so this file is
inside both from order 2 and order 3 onwards. S8's `**Readers:**` clause is written for the first and
AC13 reads it; the second is why the dead-key non-goal above keeps a dossier path and a SHOUTED key
out of a subject-verb-object relation.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the guide fixture regrown past the raised
line cap, so check 6 names it and prints the new pair · none added, so no assertion-floor raise is
owed by this unit.

The dossier edit in S7 changes prose in a table, not a claim block, so no generated map artifact moves
with it. If `codebase-map coverage + freshness` disagrees, `python tools/codebase-map/gen_map.py
--write` runs in the same commit.

## 8. Open questions

### F1 — the ratified figure

RESOLVED (owner, 2026-09-21): 98304 and 1200. The owner ruled the ACT
on 2026-09-20 and named no number. On 2026-09-21 the owner first ratified 81920 and 1000, taking this
unit's recommendation, and re-ruled the pair the same day to 98304 and 1200, once the re-measurement
below showed the first pair buying 31.7 days on the merged tree where 48.9 had been weighed. Every
candidate and every figure each needed is kept below as it was weighed, because the record of what
was weighed is the reason the resolved figure can be re-argued later.

The first ruling weighed these two, measured at the retired base `fcbfba5f` from the dry run's
figures, which this build's research record carries: the rate at
`memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md:331` and
both pairs at `:337` to `:339`.

| pair | byte headroom | days at 402 B/day | line headroom | days at 2.65 L/day |
|---|---:|---:|---:|---:|
| 81920 and 1000 | 19650 B | 48.9 | 299 | 112.8 |
| 73728 and 900 | 11458 B | 28.5 | 199 | 75.1 |

Both preserve the 81.92 allowance and both keep bytes as the binding axis, which is what the design
wants. The argument that carried: the intervention this replaces is the `TOOL-dFoldedVerdict-5` split
at `dc9431f8`, which amputated a whole section, recovered 7209 B and lasted 20 days, so a stopgap
buying less than roughly twice that expires inside one build. That was left open at rev-2 rather than
taken, because "roughly twice the split's lifetime" is a judgment about how long a stopgap should last
and not an arithmetic result — 29 days against 49 is exactly the size of the judgment, and it was the
owner's to make.

**Re-measured at rev-4 on the rebased base `bd44d3ff`, and re-ruled.** The reconcile brought the
protocol to 64939 B and 704 lines and the refill rate to 535.4 B and 2.80 lines per day, so the two
pairs the first ruling weighed, and the pair the owner then ruled, buy:

| pair | byte headroom | days at 535.4 B/day | line headroom | days at 2.80 L/day |
|---|---:|---:|---:|---:|
| 98304 and 1200 | 33365 B | 62.3 | 496 | 177.1 |
| 81920 and 1000 | 16981 B | 31.7 | 296 | 105.7 |
| 73728 and 900 | 8789 B | 16.4 | 196 | 70.0 |

The first ruling's premise moved: 31.7 days is under the forty, roughly twice the split's twenty,
that the argument above rested on, and under the 48.9 the first table weighed. The owner raised the
pair to restore that headroom. 98304 and 1200 buy 62.3 days at the merged tree's rate and keep the
construction: eight fifths of the retired pair, the 81.92 allowance intact, and bytes binding by a
factor of about 2.8.

### F2 — where the build's single kit-version move has to SIT

RESOLVED (owner, 2026-09-21): here, in
this unit. Re-derived from source and not from the ruling, per the instruction to verify it:
`tools/memory-tree/check-verdict-epoch.sh:16` states the rule topologically and `:179` implements it
as an ancestry test — W, the newest commit in `<base>..HEAD` moving a behaviour-bearing line of the
scan set declared at `:68` and `:69`, must be an ancestor of or equal to S, the newest commit that
CHANGES the constant's value. S1 moves two non-comment lines of that scan set at order 4, and none of
units 2, 4 and 5 touches any file in it, so this unit's engine commit is the last W the build has.
The move at order 2, in `TOOL-dGatedProse-1`, would therefore have made W a descendant of S and
redded an unguarded `repo` leg
from this unit's commit through the build's tip. The resolution keeps the move singular and gives it
to this unit, in its own commit at or after the engine commit; section 4 records what was verified,
AC12 observes the verdict and carries the liveness assertion, and S8 carries the work.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft.
- rev-2 · 2026-09-21 · folded the four cross-reads and the build's four rulings. **Folded:** (1) the
  one-move-per-build ruling — rev-1's S2, the bump, and S3, the nine-carrier re-stamp, are DELETED,
  the surviving render work is the new S2, and rev-1's S4 to S8 shift down one to S3 to S7; AC3 now
  observes that this unit moves no version and the marker-population derivation is gone from section
  4. (2) AC4 overstated `tools/check-kit-versions.sh`; re-derived at `:135` and `:147` — its
  population is the four tracked templates and the four renders are outside the glob, so AC4 now
  splits the halves and names `kit/dogfood doc parity` as the one S2 can break. Unit 4's F2 was right
  and rev-1's AC4 was not. (3) `memory/backlog/TOOL.md:548` names one key where this unit moves two;
  routed as a landing-time build write, in the route table, a non-goal and a `hands-off external`
  edge. (4) the floor ruling — this unit adds no assertion, so it owes no raise, said in S6, AC10 and
  the `New arm:` line, and AC10's pinned 374 became a DERIVED read of what unit 1 left. (5) rev-1's
  section 7 called `kit/dogfood doc parity` unguarded; verified in `tools/gate-legs.json` that it
  carries a six-path guard, and section 7 now names the guard and which scope items arm it. (6) the
  line-number reflow unit 1 causes — the consumes-from edge now covers offsets as well as the version
  and the floor, and records that `tools/check-spec-tokens.py:396` grades a citation's RANGE at
  `:402` and never its content, so nothing gates a slid coordinate. (7) the union's live gap inside a
  file this unit edits — a fourth, SCOPED pass added, with
  `tools/memory-tree/check-memory-hygiene.test.sh:547` and `:549` in S6 and the route table. (8)
  AC6's exemption was narrower than the union it graded — the route table now carries all five
  `memory/backlog/TOOL.md` matches and AC6 distinguishes an ASSERTION of a current bound from a RECORD
  of a past measurement, with `:352` re-measured in place. (9) the map obligation is stated with its
  reason, verified against the dossier's globs at `memory/map/features/memory-tree-hygiene.md:25` and
  the grammar-only decisions check at `tools/codebase-map/map_lib.py:1032`. (10) the
  author-facing-rule ruling — this unit already wrote the figure into the template and produced the
  render, restated with the verified fact that the render is all-or-nothing over the four pairs, which
  is what makes both hands-off edges binding. (11) unit 4's claim that this spec owes it a mirror
  `hands-off` — it already carried one; kept, with the byte-neutrality claim re-grounded on unit 1's
  stamp rather than on a re-stamp this unit no longer makes. (12) unit 2's refused-shape edge — the
  dead-key non-goal was rewritten so a dossier path and a SHOUTED key are no longer in a
  subject-verb-object relation. **Refused:** (a) the dossier's own check-count disagreement at
  `memory/map/features/memory-tree-hygiene.md:1` against `:34` — pre-existing, not caused by this
  unit's row edit, and owed by the unit that CHANGES the count; named in a non-goal and nothing more.
  (b) re-litigating where the single move sits — conformed instead, with the verdict-epoch
  consequence recorded as F2 rather than argued. (c) rewriting `memory/backlog/TOOL.md:366`, `:54`,
  `memory/DECISIONS.md:62` and `:132` — refused on record-type grounds, which is the discipline S4 is
  built on. (d) the dead-key repair at `memory/map/features/memory-tree-hygiene.md:54` — refused
  unchanged from rev-1, on population width. **Re-derived and held:** every figure in the Data model,
  the F1 table and the Design prose was left as rev-1 had it; the cross-read verified each against
  source and finding nothing to churn is a result, not an omission.
- rev-3 · 2026-09-21 · folded the owner's ruling O1 and the main loop's correction R1-CORRECTED.
  **O1, the ratified pair of 81920 and 1000:** F1 is now `RESOLVED (owner, 2026-09-21)` with both
  candidates and their figures kept as the record of what was weighed rather than deleted; S1 names
  the pair as ruled; a new Data-model paragraph derives each figure — 81920 is 80 KiB and exactly four
  thirds of 61440, 1000 is four thirds of 750, so the 81.92 allowance survives under one scalar — and
  a second gives the headroom in days on both axes, 48.9 against 112.8, with the byte axis staying
  binding by a factor of about 2.25. A third paragraph derives the 402 B/day and 2.65 L/day rate from
  this file's own history, `dc9431f8` at 54231 B and 648 lines on 2026-09-01 against 62270 B and 701
  lines on 2026-09-21, and records the all-history 1239 B/day that is deliberately NOT the basis
  because it spans the guide's authoring era. The Alternatives row for 73728 and 900 now reads as
  refused by the ruling rather than pointing at an open fork.
  **R1-CORRECTED, the version move returned to this unit:** rev-2's "No kit-version move and no
  marker re-stamp" non-goal is DELETED rather than negated, and the work returns as a new S8 — the
  value replaced once for the build, its same-line marker with it, every other carrier re-stamped from
  a DERIVED population, the templates stamped and the renders regenerated. AC3 is rewritten from
  "this unit bumps nothing" to an observation of the move that reads both the old and the new value
  from the tree rather than pinning an increment. F2 is `RESOLVED (owner, 2026-09-21)` and the
  placement was re-verified at source before folding, not taken on the ruling's word:
  `tools/memory-tree/check-verdict-epoch.sh:16` states the rule and `:179` is the ancestry test, the
  scan set is `:68` and `:69`, W is walked at `:129` and S searched at `:150` over the engine alone,
  and units 2 and 4 touch no file in that set — so this unit's engine commit is the build's last W and
  every legal S is at or after it. Two new ACs: AC12 observes the derived population and the leg's
  exit status with a liveness assertion built on the checker's own refuted endpoint cut at `:21`, and
  AC13 reads S8's `**Readers:**` clause, excluding `tools/memory-tree/corpus_ids.py` with its
  measured reason. Section 7 gains `verdict-epoch self-test`, which rev-2 omitted under the same
  guard, and records that two unguarded `repo` legs now arm on this unit's own edit.
  **Folded alongside them:** (1) O2's no-cutoff ruling makes this SPEC a graded subject of both new
  predicates from order 1 and order 2, which section 7 states and both consumes-from edges carry;
  S8's clause is written to satisfy check 25 on the graded path rather than through either escape.
  (2) the marker grep's population is TEN files and not nine — the tenth is a sibling spec that
  spells the literal marker in prose, so the population is tracked files outside the build-record
  class, and this spec avoids that string for the same reason. (3) the render count: it runs once per
  commit that moves a template, which is both of this unit's commits, so neither leaves a template
  and its render disagreeing. (4) unit 1 keeps the `tools/memory-tree/README.md` check-count
  sentence, which it had coupled to the version at rev-2 — verified that the file carries no version
  string and the marker grep never returns it, so it belongs to the unit that changes the count. (5)
  `memory/backlog/TOOL.md:231` needs its comparative moved with its figure: "ten times looser" is
  already wrong at base against 750 over 250 and becomes differently wrong at 1000, so both move in
  one clause. (6) the bump's cost to `tools/memory-tree/hygiene-parity.test.sh` is declared in its own
  sub-section — its floor at `:54` moves to the bump commit and `:64` then refuses every older
  baseline, which its header states at `:26` and which reds nothing because `:10` records that it is
  deliberately not a gate leg. (7) the byte-neutrality claim in the unit-4 edge is re-grounded on this
  unit's own stamp, since the re-stamp is no longer a sibling's. **Held:** every figure rev-2
  re-derived was re-measured at rev-3 against the live tree — the seven guides' percentages, 62270 B
  and 701 lines, the 81.92 quotient, the four passes' carrier set and the self-test coordinates at
  544, 547, 549, 551, 1133, 1139 and 2460 — and all of them reproduce, so nothing else in sections 4
  and 6 was churned.
- rev-4 · 2026-09-21 · folded the round-1 spec audit's four items against this unit, recorded at
  `memory/builds/dGatedProse/reviews/2026-09-21-review-TOOL-dGatedProse-1-spec-audit-round1.md`, and
  re-derived every coordinate and measured figure on the rebased base `bd44d3ff`, the merge of
  `origin/main` into this build. **M9:** new AC14 reads the comment block immediately above the
  `GUIDE_CAP_BYTES=` line for a date, `TOOL-dLoggedFlight-33`, both keys named as moved, a rate and a
  headroom, with the figures derived at the build rather than pinned; S1 and the first reason home
  name it. **M10:** AC5's fixture is 800 lines and 65000 B, above both retired values and within both
  ratified ones, so either retired key in the example reds it and S3 says so; AC1's red-when names the
  byte key only and points at AC5 for the line key. The value-parity arm the record proposes is the
  candidate the prose-parity non-goal already routes to a row. **L3:** the unit-1 edge's claim that
  unit 1 adds a preset to the engine's cutoff cluster and a conf-example line is deleted; the offsets
  it names are the self-test fixture block and the engine's check-25 branches. **L4:** orders restated
  as unit 5 at 1, unit 1 at 2, unit 2 at 3, this unit at 4 and unit 4 at 5, in S8, the unit-1 edge,
  the epoch derivation, the Alternatives row, section 7 and F2; the derivation counts five write sets
  and names unit 5's as touching no scan-set file. **The rebase:** the base moves from `fcbfba5f` to
  `bd44d3ff`, which also stops AC3 passing on the merge's own movement of the constant. Engine anchors
  re-grepped: the check-6 awk binding is now `:733` and the stale-entry guard `:1944` and `:1955`,
  while `:20`, `:84` and `:121` hold. The self-test, conf-example, backlog, spec-tokens and adopter
  anchors are re-resolved in place. The protocol measures 64939 B and 704 lines there and the refill
  rate 535.4 B and 2.80 lines per day, so the Data-model figures and the Alternatives rows move with
  them and F1 gains a re-measurement beside the figures the ruling weighed; the ruled pair does not
  move, and the moved premise goes to the owner. The marker grep, re-run with the constant at 2.82,
  returns the carriers and no build record. Re-running the four passes found two lines the route table
  never accounted for, both present at the old base: the CLOSED row at `memory/backlog/TOOL.md:296`,
  which narrates the guide cap at closure and had been counted among pass 4's unrelated
  over-returns, now a left-verbatim record in the route table, a non-goal, S4 and AC6; and
  `memory/project/curation-debt.txt:67`, inside the block S5 deletes. The over-return count is deleted
  rather than corrected.
- rev-5 · 2026-09-21 · the cross-spec reconcile of the round-1 folds, run one unit at a time, this
  unit after unit 4's rev-5; every figure and anchor this entry touches was re-derived at `bd44d3ff`.
  **The owner's re-ruling of the guide cap pair, 2026-09-21:** 98304 bytes and 1200 lines replace the
  81920 and 1000 ratified earlier that day. The Goal, S1, the Data-model table, the derivation of the
  figures, the headroom paragraph, the allowance quotient, the observability line and the landing
  correction the `memory/backlog/TOOL.md:560` non-goal names all carry it. The pair is eight fifths
  of the retired one, where the first pair was four thirds, so 81.92 survives. On the merged tree it
  leaves 33365 B, 62.3 days at 535.4 B per day, and 496 lines, 177.1 days at 2.80, so bytes bind by
  a factor of about 2.8; the second-largest guide sits at 28.1% of the new byte cap. AC2's one-key
  quotients become 131.07 and 51.2. AC5's fixture moves from 800 lines and 65000 B to 1100 lines and
  90000 B, so it sits above the superseded pair as well as the retired one: a conf example left at
  81920 or 1000 reds it, which the old fixture could not see. AC6 and AC7 name the superseded pair as
  a red. F1 is RESOLVED at the new pair; the first ruling's table stays as weighed, the
  re-measurement table gains the ruled pair's row, and rev-4's sentences returning the moved premise
  to the owner are deleted, because the owner has ruled on it. The Alternatives table gains the
  first-ratified pair as a superseded row, and its conservative row loses "inside the owner's
  bracket", a bracket this spec stopped defining at rev-3. **Unit 4's write set, corrected:** rev-4's
  epoch derivation named three of its paths, and its Files touched lists five, adding
  `tools/template-size-limits.txt` and `memory/DECISIONS.md`. Neither is in the scan set, so the
  conclusion holds. Each sibling's set is now read from its own Files touched, and unit 2's names its
  template and render. **The `memory/backlog/TOOL.md:233` comparative:** M1 states 350 lines at base,
  not the 250 the row names, and unit 4 moves it to 370 at order 5 on the owner's line-half ruling of
  the same day, so the corrected clause carries no multiplier. **The unit-4 edge** names that unit's
  budget raise by what it does rather than by the label its rev-4 reused, places the guide under the
  new pair, and records that both units append one row to `memory/DECISIONS.md`. **The research
  record, M6:** the Goal, the external edge and F1 cite
  `memory/builds/dGatedProse/build/2026-09-21-build-TOOL-dGatedProse-1-dry-run-research.md` by path
  and line, and the external edge names both 2026-09-21 rulings as the main loop's relay, with AC7's
  row as their first record. S8 and its clause are untouched, which unit 5's AC7 grades; the trigger
  re-run over this file fires on S8 alone, and S4 and S6 still carry no backticked token.
- rev-6 · 2026-09-22 · §8 · the closing commit. The two forks open as `###` sub-heads rather than
  bold paragraphs, because the hygiene engine counts a §8 item as a bullet or a `###` sub-head and a
  terminal spec whose §8 holds neither refuses as hollow, which is what the sibling unit's closing
  commit met. Each mark keeps its word, resolver and date, and no fork's question or resolution
  moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "raise a declared size cap for the guides class and record
the reason beside the constant"` returned no seam for a cap raise as such — the ranked candidates are
name-token matches on `record` and `declar` across the runlog and govkit kits, none of them relevant.
Three hits are: `kit-dogfood-parity.PAIRS` on the `build-method` dossier, which IS the seam the
re-render uses; `check-template-size.sh` on the `playbook` dossier, which is the high-water mechanism
`TOOL-dFoldedVerdict-7` names as the structural alternative this unit declines; and the `gate-legs`
inventory keys `build-method size` and `charter size`, which are the sibling declared-ceiling legs.
The seam this unit extends is therefore `tools/memory-tree/check-memory-hygiene.sh:84`, check 6's
existing per-class cap table, and no new mechanism is written. S8 extends no seam either: the version
constant, its marker, the epoch checker and the kit-versions leg all exist, and the move is a value
change inside them. Two recall hits were STALE against
source and are recorded as such: `TOOL-dBriefedPass-8` and the `dFoldedVerdict` specs both cite the
constants at `tools/memory-tree/check-memory-hygiene.sh:63`, and they now sit at line 84 — which is
also why the consumes-from edge treats every coordinate here as a base-`bd44d3ff` reading to be
re-resolved rather than copied.

Recall terms used: `guide cap GUIDE_CAP_BYTES GUIDE_CAP_LINES check 6 curation-debt raise headroom
hygiene constant unattended protocol split`, passed to
`python tools/memory-recall/query.py "why was the guide size cap raised and where is the reason for a
cap figure recorded"`, which returned 40 hits over 1136 records. The five that bind this unit are
`TOOL-aWidenedGuide-1` for the class split that created the pair, `TOOL-dSpentCeiling-3` for the value
re-argued once already, `TOOL-dBriefedPass-8` for the split precedent and the wrong-key correction,
`TOOL-dFoldedVerdict-7` for the carriers-on-their-ceiling pattern, and `TOOL-aScouredKit-23` for the
sibling template that carries no ceiling at all.
