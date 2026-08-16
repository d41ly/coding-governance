# review-dClosedLexicon-1 — adversarial pass over the spec at rev-2

**Subject:** `spec/2026-08-16-spec-dClosedLexicon-1.md` at rev-2 · base a9bd87d5 · node d · 2026-08-16

Single-reviewer pass, not a Tier-2 multi-agent run. Nine findings, ordered by severity. Findings R7,
R4, R3 and R5 change the shape of the work; the rest are gaps in an otherwise sound shape. Every
claim below was checked against source at review time.

## R7 — the spec files a decided question as an open one, and §1 already decided it

`§8 F5` asks the owner whether rev-2 made the unit too big to land as one. §1 does not leave that to
taste: a unit is "one stream/owner, no cross-stream contract change, reviewable as one Tier-1 diff —
else split." At rev-2 the unit adds a kit, edits `map_extractors.py`, edits `drift_signals.py`, edits
`gate-legs.json`, and edits three shipped playbook files. That is a cross-stream contract change by
the playbook's own definition, and a spec amending the governance should not be the document that
treats it as advisory.

FIX: demote F5 from a fork to a §3 non-goal plus a named follow-up build. Unit A is `tools/lexicon/`
with S12 and the playbook edits; unit B is S6 and S14, the integration. The split also fixes R2,
because unit B is where the coupling instruction belongs.

## R4 — S15 blocks real progress in every `probe`-mode language

S15 says a pin may not be LOWERED while any contributing language is in `probe` mode. Fixing ten
real Go violations under a regex extractor then produces a measured population of ten fewer, and the
guard refuses to bank it. The rule as written makes every `probe` language permanently
ratcheted-shut, which is the opposite of the shrink-only doctrine it was modelled on: `ORPHAN_ID_PIN`
is shrink-only precisely so that repair is recordable.

The intent is right — an under-matching pattern must not launder its blindness into a lower pin —
but the predicate is wrong. What distinguishes a real drain from a coverage regression is whether the
offender set SHRANK by named members or the population itself shrank.

FIX: guard on the offender IDENTITIES, not the count. A lower is admissible when every departed
offender is individually accounted for, and refused when the definition population itself fell in the
same edit. That is checkable and does not punish repair.

## R3 — S15's guard needs machinery this repo has never built, and the spec spends one sentence on it

To know a pin was lowered, `--check` must compare against the PREVIOUS value, which the conf does not
carry. The only sources are git history or a stamped baseline. `TOOL-aNumeralWarden-3` records
exactly this hole from the other side: a drift-audit pin RAISE is indistinguishable from a population
drain to every gate leg, because `--check` compares only `value > pin`. S15 therefore asserts a
capability the tree has an OPEN row saying it lacks, and AC15 is written as though the mechanism
exists.

FIX: either design the baseline read in §4 (a `git show HEAD:.lexicon.conf` comparison, with the
behaviour on a first commit and in a detached worktree both stated), or cut S15 and AC15 and file the
pin-direction guard as the shared follow-up it really is — it would serve `drift-audit` and
`memory-tree` at the same time, which is a better argument for building it than this kit is.

## R5 — the portability fix is not portable

S5 vendors `map_lib.subtokens()` and byte-gates the copy "the way `tools/lib/resolve-python.sh`
already is". The analogy does not hold. `resolve-python.sh` lives in `tools/lib/`, which AGENTS.md
states is gov-internal and ships nothing, so its parity gate always has both sides present in the
governing repo. The lexicon's parity gate compares against `tools/codebase-map/map_lib.py`, which an
adopter taking the lexicon WITHOUT codebase-map does not have. AC16 then holds only in this repo,
and in an adopter tree the leg either reds forever or is silently skipped — and a silently skipped
parity leg is the drift the gate exists to catch.

FIX: state the source-of-truth direction. Either the splitter moves to a shipped shared location both
kits vendor from, or the parity leg is declared conditional on codebase-map's presence and prints
`NOT ARMED` rather than passing, per the S3 precedent already in this spec.

## R2 — S14 leaves an orphan when the lexicon is removed

`map_extractors.py` is per-adopter project-owned code, which the spec gets right. The extractor it
gains will read `.lexicon.conf`. An adopter who later drops the lexicon leaves an extractor whose
source is gone, and `all_inventories()` raises rather than degrading — so removing an OPTIONAL kit
reds a DIFFERENT optional kit's gate. Nothing in §2 or §6 covers the teardown direction.

FIX: `adopt-lexicon.sh --check` detects an orphaned `lexicon-verbs` extractor and names it, and the
uninstall path is written down. An inventory that cannot be removed is a kit that cannot be opted out
of, which contradicts F-A5's whole conclusion.

## R8 — no acceptance criterion covers S13, the lockstep the marker exists to enforce

S13 lands edits across three shipped files that carry `<!-- governance-template: vN.N -->` and are
re-pulled in lockstep. AC11 asserts only that the template is under 32768 bytes. Nothing asserts the
three markers read the same version after the edit, which is precisely the failure the marker was
introduced to make visible, and `customize.md` says so in its own words.

FIX: add an AC asserting all three markers agree at v2.8, checked by a command. `check-placeholders.sh`
is the natural home since it already opens both shipped files.

## R1 — §4 oversells the map ratchet in one direction and undersells it in the other

The "How this rides the existing kits" table calls the `EXTRACTORS` ratchet "the only pressure a
closed table has against growth". For an inventory of code keys a claim requires describing a real
moving part; for a hand-authored verb the claim is a one-line dossier edit by the same author who
added the verb in the same commit. The addition direction makes growth VISIBLE in a diff, not costly.

The deletion direction is the valuable half and goes unmentioned: a claim naming a verb since removed
reds, which catches the table drifting behind the code. AC14 covers both directions; the prose should
match it.

## R9 — the byte ledger has an unattributed placeholder

§4 Migration says `customize.md` gets "the `{{LEXICON_CONF}}` tally move", but no section says which
of the two SHIPPED files carries `{{LEXICON_CONF}}`. `customize.md` is a catalogue, not a shipped
placeholder host. If the placeholder lands in the template it costs bytes the F-A6 ledger does not
count, against roughly 17 B of headroom. If it lands in the companion it is free.

FIX: name the host file. The companion is the right one — the lexicon rules live there, and the
template's §12 stub only needs to route.

## R6 — the day-one seed for S6's verb-liveness signal will be non-zero and the spec does not say so

"Verbs declared but never used" is measured against a table that `--scaffold` derived by frequency
and a human then edited, and curation adds aspirational verbs. The seed pin will not be 0, so the
signal ships slack, in the same shape as `non_terminal_specs_cited_by_product_source: 2`. That is
defensible and the drift-audit pins carry that precedent openly, but the spec should say the seed is
expected non-zero so an implementer does not read a non-zero measurement as a failed build.

## What holds up

The three coverage modes are the right answer to the fail-closed law and are stated in a form an
implementer can build. The split of vacuity into a corpus-side signal (S6) and a kit-side sentinel
(S11) is correct and the reasoning is sound — the corpus arm really is defeated by an empty corpus.
§3's rejection of a pre-emptive gotcha class is right and cites the rule it obeys. F-A11's admission
that rev-1's reuse audit was wrong about its own novelty is the kind of thing a revision log usually
launders, and it is recorded plainly.
