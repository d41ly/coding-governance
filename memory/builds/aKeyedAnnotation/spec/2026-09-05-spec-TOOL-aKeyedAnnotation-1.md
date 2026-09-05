# TOOL-aKeyedAnnotation-1 — the annotation convention, written once, and the citation it repairs

**Status:** CLOSED · rev-7 · 2026-09-05 · node a · Tier-2 · base 0d7d9414 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-acceptance.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-acceptance.md) | journal | — |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py) | research | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md](../build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md) | research | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-2-3-4-closing-diff-round1.md) | diff-review | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round1.md) | spec-audit | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |
| [2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md](../reviews/2026-09-05-review-TOOL-aKeyedAnnotation-1-round2.md) | spec-audit | TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4 |

<!-- /gen:spec-records -->

## 1. Goal

Write this repo's code-annotation convention down once, as a memory-tree guide the kit renders into
adopters, and demonstrate it by repairing the two source citations that resolve to no record.
Every later unit writes comments that must obey it, so it lands first.

## 2. Scope (IN)

- **S1** A new annotation-style guide beside `memory/guides/BUILD-METHOD.md`, rendered by the
  memory-tree kit from a template beside that guide's own, and wired into
  `tools/memory-tree/adopt-memory-tree.sh` at the same seam that renders the build method. The two
  new filenames are deliberately NOT backticked anywhere in this spec: the spec-token leg grades a
  backticked path against `git ls-files`, and its waiver registry is shrink-only, so a spec cannot
  name the file its own unit creates without redding a leg nobody may waive. Choose the names at
  build time, mirroring the build-method pair.
  **The new TEMPLATE must not contain the literal build-method filename anywhere.** Two files keep a
  hand-written exclusion list over exactly that literal — the seeder block in
  `tools/memory-tree/adopt-memory-tree.sh` and the gate `tools/memory-tree/check-method-carriers.sh`,
  which is `subject = repo` with no guard and therefore runs on every bar in every adopting tree.
  Spelling the literal would need a skip case in BOTH, which is the same rule in two hand-kept
  spellings; not spelling it needs neither.
- **S2** The guide carries exactly four things and nothing else: the MUST / MAY / MUST NOT list; the
  three dispositions under which a number is safe in a comment (frozen by its conditions, gated by a
  pin, pointed at its owner); the delete-the-id test; and the statement that annotation is voluntary,
  with the reason — the shipped-evidence oracle discriminates only because citation is sparse.
- **S3** The guide POINTS at what other files own and restates none of it: the id grammar belongs to
  the recall extractor, the charter owns the derived-count ban, and the design pass record owns the
  measurements. Each is named, none is copied.
- **S4** Repair both dangling citations — in `tools/unattended/lib-unattended.sh` and in
  `tools/unattended/unattended.test.sh` — by rewriting each block so its evidence is named in the
  comment and the id is a trailing pointer. Each block must read completely with its id deleted.
  The ids belong to another node's build and its records were never written, so this unit repairs
  the PROSE and files the missing records as a backlog row rather than inventing them.
  **THAT ROW MAY SPELL NO ID OF THE FOREIGN BUILD, ANYWHERE, AND THE CONSTRAINT IS NOT STYLISTIC.**
  A backlog row's head is an ANCHOR under the recall extractor's dash rule, so an id there DEFINES
  it — which resolves it, and unit 3's report-only signal needs it to resolve to nothing, so the row
  would quietly delete that unit's only real finding. An id in the row's BODY is a bare citation
  instead, and the memory-tree orphan check counts cited-never-defined against a pin sitting at zero
  with a waiver file empty by its own declaration, so the bar reds; raising that pin trips the
  shrink-only ratchet row that marks it. AC6's green bar cannot hold either way. The only escape the
  design pass measured is to name the foreign BUILD and its SEQ RANGE in prose, which no grammar
  matches. The row is minted under one of this build's own reserved ids.
- **S5** Delete the mechanism prose that a bug-class record absorbed verbatim from a call-site
  comment, leaving the record its class name, its frozen incident and its reach. **AMENDED at build
  time, because both of this item's factual claims were wrong and the build measured them rather
  than inheriting them.** It said TWO records and said the design pass names both; that record names
  no bug-class file at all, and the measurement finds exactly ONE, carrying a run absorbed from
  `tools/check-wiring.sh`. Method, so the next reader can re-run it rather than trust this sentence:
  split every record into sentences, squeeze whitespace and comment markers, and look for each run
  of 60 characters or more inside tracked source. One record hits at 60 and the same one at 90, so
  the count is not an artefact of the threshold. There is NO direction to establish: `git log -S`
  over the shared run returns the SAME commit for the record and for the call site, so the two
  copies were born together rather than one absorbing the other. This item claimed git established a
  direction; git refutes that as well. The disposition is unchanged and the reason is better — one
  fact in one place, and the call site is where the decision it describes is acted on.
- **S6** Register the guide as a method carrier if and only if the kit's carrier registry demands it;
  read `tools/memory-tree/adopt-memory-tree.sh` for whether a second guide joins that population.
- **S7** A rendered memory-tree guide is declared in FOUR carriers beyond the render line, and all
  four are in scope. An earlier revision of this item said three and missed the one that SHIPS.
  (i) A `[[files]] role = "rendered"` stanza in `tools/memory-tree/kit.toml` carrying `to` and
  `placeholders` — without it the template falls to the catch-all `role = "engine"` and reaches
  adopters with no render destination. (ii) A fourth row in the hand-kept `PAIRS` literal in
  `tools/memory-tree/kit-dogfood-parity.test.sh` — without it the dogfood copy may diverge from its
  template forever while the leg prints green. (iii) The new rendered path in that leg's `guard`
  list in `tools/gate-legs.json`, which today names the three existing rendered paths explicitly.
  (iv) The `[[gate_leg]]` block's OWN `guard` list inside `tools/memory-tree/kit.toml`, which is a
  separate carrier from (i) and from (iii): the deployer copies a descriptor's declared guard
  verbatim into a target, so patching this repo's manifest alone leaves the half that ships open and
  EXPORTS the hole rather than fixing it. The comment under that guard says exactly this, and it is
  the comment this item cites as its precedent — which is how an earlier revision came to repeat,
  in its own text, the failure it was quoting.
- **S8** The two new files this unit lands both fall under GLOB-DERIVED codebase-map inventories —
  the rendered guide under the guides inventory, and S5's bug-class record under the gotcha-class
  one — so each mints an inventory key that a dossier must claim, and the coverage leg reds until it
  does. `memory/map/baseline.toml` is not the escape: its own header says it only ever shrinks and
  that new keys belong in a dossier. `memory/map/features/build-method.md` is the precedent and the
  shape to copy — it already claims the build method's guides key and covers the template and the
  rendered copy as one pair. This unit claims both new keys the same way and regenerates the map
  artifacts under `memory/map/generated/` in the same commit.

## 3. Non-goals (OUT)

- **No line in the charter template.** Measured at this base: it is 8 bytes under its gate ceiling,
  so even a one-line pointer needs a trim or an owner ceiling decision. §8 carries the fork; the unit
  ships without it and the guide is reachable from the kickoff manifest instead.
- **No annotation grammar, marker kind, or scanner.** The design pass refuses all three.
- **No sweep over the corpus rewriting comments to the new style.** The convention is forward-looking
  and the two named repairs are its demonstration, not the start of a pass.
- **No change to any consumer.** Units 2 to 4 own those.

## 4. Design

### Data model

The guide is prose. It has no schema, no parser and no gate, deliberately: a style convention that a
machine could grade would be a rule, and every rule this pass considered was refused on measurement.
What makes it stick is that it is short, rendered into adopters with the kit, and reachable from the
one document a session already loads.

### Rollout

The kit's adopter script renders the build-method guide from a template beside it. The annotation
guide rides that seam — one template file and one render line — plus the four declaration carriers
S7 names and the map claims S8 names. Nothing beyond THOSE. This sentence has now been wrong twice
in the same direction: it first said "nothing else in the kit changes", which was false in three
places, and its repair then bounded the unit to three carriers and no dossier claim, which forbade
the very thing AC6's green bar requires. Both were the assert-over-derive shape the round-1 audit
found running through this set, and the second was written while repairing the first. The bound now
points at the enumerations rather than restating a number.

### Alternatives rejected

Putting the convention in `memory/HYGIENE.md` was rejected: that file grades RECORDS, and a
code-comment convention filed under a record-hygiene gate reads as gated when it is not. Putting it
in the charter was rejected on the measured 8 bytes. Putting it in a gotcha record was rejected
because a gotcha is a bug class selected per-diff, and this is a writing convention that applies
everywhere.

## 5. Production-readiness checklist

- security — N/A: prose, no execution path.
- perf / scale — N/A: no runtime.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the render is observable by the kit's own adopter run; a missing render shows as an
  absent file, which the adopter script's existing conditional already tolerates.
- risks — the real risk is drift: the guide restating something the charter or the extractor owns.
  S3 is the control, and §6 asserts it by name.
- testing + left-shift gates — no new leg. The existing memory-hygiene, kit-version and codebase-map
  coverage legs grade the files this unit touches; the third is load-bearing because S8's two new
  inventory keys are what it counts, and it was not named here until the round-2 audit found the
  scope bound forbidding the claim that satisfies it. A new leg for a prose guide would be the
  structural-check-reads-as-semantic shape the charter warns about. Two left-shifts the round-1 audit named and this unit owns: extend
  the existing dangling-citation gotcha record with the backlog-row disposition — head defines, body
  orphans, prose escapes — so the class is SELECTED before such a row is written rather than after
  the bar reds; and add a bug-class row for the criterion shape this audit found five times, that an
  acceptance criterion stating a numeral over a derived population must name the command deriving it,
  must assert on the field that command actually moves, and must not hold unchanged when its scope
  item is skipped.
- migration / rollback — the guide is additive; deleting it restores the prior state exactly. The
  record deletion is an ordinary revert.
- user docs — the guide IS the doc.

## 6. Acceptance criteria

- **AC1** When `bash tools/memory-tree/adopt-memory-tree.sh` is run against a scratch clone, the
  target tree holds the rendered annotation-style guide beside its rendered
  `memory/guides/BUILD-METHOD.md`, byte-identical to a render of its template.
- **AC2** When the rendered guide beside `memory/guides/BUILD-METHOD.md` is read, it carries all
  four of the MUST/MAY/MUST-NOT list, the three
  number dispositions, the delete-the-id test, and the voluntary-annotation statement with its
  reason — and nothing that duplicates the charter's derived-count ban beyond naming it.
- **AC3** When `python memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-citation-census.py`
  is run after this unit, each repaired block reads completely with its id removed, and the census
  reports no unresolvable id that was not present at this base.
- **AC4** When each repaired block in `tools/unattended/lib-unattended.sh` and
  `tools/unattended/unattended.test.sh` is read with its trailing id removed, its evidence is still named
  and the paragraph still states the incident it records.
- **AC5** When the edited bug-class record is read after this unit, the specific mechanism prose
  S5 names is ABSENT — named sentence by sentence in the unit's acceptance ledger, so the
  criterion observes the removal rather than the residue — while the record still carries its class
  name, its frozen incident and its reach. `python tools/memory-tree/gotchas.py --check` exits 0,
  which is an invariant across the change and is therefore recorded as a guard, never as the proof.
- **AC6** When `bash tools/run-gates/run-gates.sh` is run on this unit's commit it is green.
- **AC7** When `bash tools/memory-tree/kit-dogfood-parity.test.sh` is run after this unit it reports
  one more pair than it does at this base — a count the test already prints — and editing the
  rendered guide away from its template REDS it. Both observed.
- **AC8** When `bash tools/memory-tree/check-method-carriers.sh` is run after this unit it is green,
  with no skip case added to either of the two files that keep an exclusion list.
- **AC8b** The `PAIRS` carrier is OBSERVED both ways, and it is the only one of the four that can
  be: with the row present, a rendered guide edited away from its template REDS
  `kit-dogfood-parity.test.sh`; with the row deleted and the same divergence in place, that leg
  reports GREEN over one pair fewer. Stage the divergence, take both readings, restore.
- **AC8c** **The other three carriers have NO mechanism that reds on their absence, and this
  criterion RECORDS that rather than asserting one.** An earlier revision of AC8b demanded that
  deleting the descriptor's `[[files]]` stanza make a deployer run REFUSE. It does not — measured,
  `govkit.py selfcheck` exits 0 with the stanza and exits 0 without it, because the deployer walks
  rows already declared `rendered` and an absent stanza declares nothing. AC1 cannot see it either,
  since the adopter script renders from a hardcoded line. The two `guard` rows are worse still: they
  change only which legs a SCOPED run selects, so observing them costs a full bar on a
  single-file diff. So the disposition is the one the charter asks for when a check cannot be
  mechanised — the exemption is documented together with its compensating manual check. The
  compensating check is the four-carrier enumeration in S7, read whenever a rendered guide is added,
  and the gap is recorded in this feature's map dossier. The permanent close is deriving the pair
  list and both guards from the descriptor's rendered stanzas, filed as a backlog row rather than
  built here because deriving kit parity is outside this build's goal.
- **AC8d** When the codebase-map coverage check is run after this unit it is clean, with both new
  inventory keys claimed by a dossier and none added to `memory/map/baseline.toml`, and the
  generated map artifacts reproduce from the tree at that commit.
- **AC9** S4's constraint has TWO failure modes and they need two observations, because one number
  covers neither. HEAD case: when the set of ids of the foreign build appearing anywhere under the
  memory root is enumerated with `git grep` and sorted, it is byte-identical before and after the row
  lands. An id in a row's head ANCHORS, so it lands in the definitions set and the orphan count stays
  0 — the earlier form of this criterion named the orphan count alone and was therefore green on
  exactly the violation it exists to catch. BODY case: `python tools/memory-tree/corpus_ids.py
  --report` shows an orphan count of 0, which is what catches a bare citation. The criterion names
  which clause catches which mode; it does not assert on a per-build definitions set, because that
  command prints none.

## 7. Gates

Existing legs that must stay green: the full bar. Load-bearing here are the memory-hygiene leg, the
kit-version leg, the codebase-map coverage and freshness leg, the drift-audit records leg, and
whichever legs `tools/gate-legs.json` guards on `tools/memory-tree/`. Read the manifest for the
names; none is typed here. An earlier revision typed four of them under that very sentence and got
one wrong, which is the sentence's own point made the expensive way. No new leg.

## 8. Open questions

- **F1 — the charter pointer.** The template is 8 bytes under its gate ceiling at this base, so a
  one-line pointer to the guide does not fit without a trim or a ceiling raise, and the manifest
  records that raising it is an owner decision rather than an edit. Options: (a) ship without a
  charter pointer and reach the guide from the kickoff manifest's §B, which is not byte-gated;
  (b) trim non-instructional prose elsewhere in the template to buy the line; (c) ask the owner to
  raise the ceiling. Recommendation: (a) now, and let a later unit that is already trimming the
  template carry the pointer for free. RESOLVED (agent, 2026-09-05, delegated): (a).
  Options (b) and (c) both change the governance template, which M3's veto 2 reserves to
  the owner, so neither survives to be picked. (a) is what is left standing, and it is also
  the option costing no acceptance criterion.
- **F2 — carrier registration.** Whether a second rendered guide must join the kit's method-carrier
  registry is a fact the adopter script decides, not a judgement. FACT-QUESTION · read
  `tools/memory-tree/adopt-memory-tree.sh` at the carrier-registry block and follow what it demands. RESOLVED (agent, 2026-09-05,
  delegated): the probe was run, and the answer falls out of it in two halves. That block
  seeds `memory/project/method-carriers.txt` by grepping every file OUTSIDE the memory root
  for a literal reference to the build method, so the RENDERED guide lands inside that root
  and never joins the registry — no registration is demanded. The half it does demand is the
  TEMPLATE, which lands in the kit dir where the seed does look. Liveness: the probe can
  return no obligation, and on the first half it did.
  AMENDED by the round-1 spec audit, which found this resolution incomplete in both directions.
  The exclusion list exists in TWO files, not one: the seeder block the probe read, and the gate
  `tools/memory-tree/check-method-carriers.sh`, which is `subject = repo` with no guard and so runs
  on every bar in every adopting tree — a seeder-only patch would leave gov red on the new template
  and a fresh adopter red at install. Rather than patch both, which is one rule in two hand-kept
  spellings, S1 now bans the literal from the template outright, and AC8 observes the gate green
  with no skip case added anywhere. The skip-case route is withdrawn, not merely unused.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the `aKeyedAnnotation` design pass.
- rev-2 · 2026-09-05 · §8 forks resolved under the standing mandate; no scope change.
- rev-3 · 2026-09-05 · round-1 spec-audit fixes folded in.
- rev-4 · 2026-09-05 · §8 F2's withdrawn skip-case route closed behind S1's ban.
- rev-5 · 2026-09-05 · round-2 fixes folded: the map claim, four carriers, and an AC9 that can fail.
- rev-6 · 2026-09-05 · S5 corrected at build time: one record, not two, and measured rather than cited.
- rev-7 · 2026-09-05 · AC8b demanded a deployer refusal that measurement shows does not exist.

## 10. Reuse audit

Probe result: `python tools/codebase-map/reuse_lookup.py "scanning source code comments for build ids
and spec references"` returned no seam for a comment-convention document — the ranked candidates were
id and index builders (`inventory_ids`, `build_reference_index`, `build_form_index`), none of which a
prose guide extends. The seam this unit actually rides is the adopter script's existing
`BUILD-METHOD.template.md` render line, found by reading `tools/memory-tree/adopt-memory-tree.sh`,
and it is extended rather than duplicated. No existing seam fits for the guide's CONTENT, which is
correct for a documentation-shaped unit.

Recall terms used: annotation comment docstring slug spec id orientation reuse-audit codebase-map
memory-recall marker keying.
