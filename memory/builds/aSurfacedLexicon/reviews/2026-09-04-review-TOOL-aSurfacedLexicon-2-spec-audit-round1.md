**Serves:** spec-audit TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4

# Spec audit — one scope item cannot be built at all, and six acceptance criteria cannot fail

Tier-2 adversarial spec audit · 2026-09-04 · node `a` · build `aSurfacedLexicon` · streams tooling ·
designs only, no code exists yet.

**Reviewed subjects**, each pinned at the blob it was read at:
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-2.md@35194bd816138aa57daac4c70103adbb146def12` ·
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-3.md@f641116ab24b1b133ea034a87ab417c03e7cf84b` ·
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-4.md@f47cbe3586d92f9cd810b3c6540e3ef828cf2e5a`.
**ROUND: 1.** Build orders 1 (units 2 and 3) and 2 (unit 4). No code exists yet, so every finding
below is a design defect, not an implementation one.

## Verdict: BLOCKED

**Review shape:** raw 45 · confirmed 22 · refuted 23 · unverified 0 · precision 0.49. The 22
confirmed findings deduplicate to **16 rows** below: three lenses landed the govkit blocker from
three sides, two landed the `verdict_pass` name, two landed the two-carrier guard, and three landed
the same generated-artifact staleness once per spec. Merged rows name every address they cover.

One blocker, ten highs, four mediums, one low. The blocker is not a judgement call: `TOOL-aSurfacedLexicon-4` S8
directs an edit that reds an unguarded merge-bar leg on every bar, and the kit's own descriptor
records that this exact edit was considered and refused in writing. The ten highs are dominated by a
single shape — an acceptance criterion whose command cannot produce the failure it exists to
observe. Six of them pass no matter what the implementer builds.

**What is right, and it is most of the design.** The three units are correctly ordered and their
seams are real. Unit 2's core argument is measured and holds: `python tools/lexicon/lexicon.py --check`
does print `lexicon: P3 layer graded=557 offenders=0 waived=0`, the pin has never held any value but
`"0"`, and replacing 164 engine lines with one refusal over a population the kit can actually reach
is the right trade. Unit 3's three armed-but-unreachable confessions are all still in the source at
`tools/lexicon/lexicon.py:624-632`, `:654-663` and `:738-745`, so the two-pass split is grounded in
this file's own failure history rather than in taste. Unit 4's Inventory section — running every
identifier it mints through `--suggest` before minting it — is the single best practice in the set,
and finding H4 exists only because its two siblings did not copy it. The anti-mirror rule is honoured
throughout: no predicate in any of the three takes its standard from the graded population.

## Findings

| # | Sev | Subject | Address | One line |
|---|-----|---------|---------|----------|
| B1 | blocker | spec 4 | §2 S8, §6 AC7, §5, §7 | The guard widening reds `govkit selfcheck`, and the kit descriptor already refused it in writing |
| H1 | high | spec 4 | §2 S8, §4 Files touched | That guard has two carriers; S8 names one, and no check compares them |
| H2 | high | spec 4 | §6 AC5, §8 | The standing arm merges a fixture it wrote itself, so it cannot fail on the tracked conf |
| H3 | high | spec 4 | §6 AC8 | The neighbour-contract command has no CLI and prints nothing whatever the count is |
| H4 | high | spec 3 | §2 S5, §4 Data model, §6 AC2, §7 | `verdict_pass` is a name this build's own gate refuses, on this unit's own commit |
| H5 | high | spec 3 | §6 AC8 | The `--brief` residue grep does not run as written, and its answer is wrong by 34 hits |
| H6 | high | spec 3 | §6 AC1/AC2, §3 | Byte-identity is unsatisfiable — the deleted functions are themselves graded corpus |
| H7 | high | specs 2, 3, 4 | §4 Files touched, §7 | Three units move symbols in a generated artifact an unguarded leg re-derives |
| H8 | high | spec 4 | §6 AC10, §2 S9 | AC10's load-bearing premise states the reverse of what its four carriers say |
| H9 | high | spec 2 | §2 S9, §4 Files touched | The codebase map's own dossier for this feature keeps describing the deleted predicate |
| H10 | high | spec 3 | §4 Alternatives rejected | The ground for deleting `--brief` is refuted by two CLOSED units it never cites |
| M1 | medium | spec 3 | §6 AC9 | The one-walk claim is observed by a fixed-string grep that misses a target and counts survivors |
| M2 | medium | spec 2 | §4 Data model, §6 | The refusal's placement against the `--measure` return is unpinned — this file's own repeat defect |
| M3 | medium | spec 4 | §2 S2 | S2 preserves a `LAYERS` dispatch arm that does not exist and that unit 2 deletes first |
| M4 | medium | spec 2 | §4 Data model, §6 | The replacement refusal inherits no liveness assertion from the thing it replaces |
| L1 | low | spec 2 | §4 Migration | The dead-path carrier count does not reproduce under the command that names it |

---

### B1 — blocker — the guard widening reds `govkit selfcheck`, and the descriptor already refused it

**Address:** `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-4.md` §2 S8 and §6 AC7,
contradicting §5's risk paragraph and §7's leg enumeration. Covers confirmed ids 1, 15, 24.

S8 adds `.lexicon.conf` to the `lexicon naming predicates` guard in `tools/gate-legs.json`.
Check 7c at `tools/govkit/govkit.py:1355-1382` partitions every guard pathspec in that manifest into
exactly one of five declared classes — `memory/`-prefixed, verbatim repo-root (`.githooks/`,
`.claude/`), renamed (`skills/session-kickoff/`), registry-exempt, or kit-relative (`tools/<kit>/`,
`tools/`) — and calls `r.fail` when the count is not 1. A root-level conf matches zero.

Staged and observed:

```
$ python tools/govkit/govkit.py selfcheck
guard pathspec '.lexicon.conf' (leg 'lexicon naming predicates') falls into 0 declared classes [], not exactly one
rc=1
```

`govkit selfcheck` carries no `guard` key, chunk `declarations`, subject `repo`, so it runs on every
bar including the push boundary. AC7 is therefore satisfiable only by an edit that reds the merge
bar, and §5's claim that S8 "changes when a leg runs and not what runs" is false.

The design never saw this because §10 never probed govkit — but the refusal is also recorded in
prose in a file this unit edits. `tools/lexicon/kit.toml:60-65`:

> The conf itself is deliberately NOT a guard pathspec. govkit partitions every guard into declared
> classes … and a root-level conf falls into none of them, so declaring one reds `selfcheck` rather
> than scoping anything. Widening that taxonomy is a change to a different kit's contract. The cost
> of the narrower guard is an early signal on a conf-only diff, never a merge verdict: the pre-push
> hook sets `GATE_FULL=1`, which bypasses every guard, so the authoritative run stays total.

**Fix.** Drop S8 and AC7. Move the `kit.toml:60-65` ruling into §3 Non-goals with its own
compensating note (the authoritative run is already total, so what is lost is early signal on a
conf-only diff and nothing else), and record it in §4 Alternatives rejected as prior art. If the
early signal is genuinely wanted, S8 has to become a two-part scope item that first widens govkit's
guard taxonomy — a second kit's contract, which the descriptor comment already prices — or routes
`.lexicon.conf` through `tools/govkit/registry.toml`'s `[[exempt]]`, with its own red-then-green
observation on `govkit selfcheck` before the guard edit lands.

**Left-shift.** The gate that caught this already exists and is unguarded; what failed is the design
pass. Add one hygiene check: a Tier-2 spec whose §4 Files-touched table names a path under
`tools/<kit>/` must show that kit's `kit.toml` among §10's verbatim retrieval terms. Cheap, and it
would have surfaced the refusal before the spec was ratified.

---

### H1 — the widened guard has two carriers and S8 names one

**Address:** spec 4 §2 S8 and §4 Files touched. Covers confirmed ids 2, 23.

`tools/lexicon/kit.toml:66-70` declares `[[gate_leg]] name = "lexicon naming predicates"` with
`guard = ["tools/", "skills/session-kickoff/", ".githooks/", ".claude/"]` — byte-identical to the
array in `tools/gate-legs.json`. S8 and the §4 table name `tools/gate-legs.json` alone, and no §6
criterion reads the descriptor.

The descriptor-vs-manifest parity check compares leg NAME and SUBJECT and never `guard`. A
one-carrier widening therefore diverges silently, adopters keep the narrow guard, and gov's bar reads
the wide one — which is the exact failure mode spec 2 §8 used to veto its own option B, and which
spec 2 §4 Alternatives leans on when it says the three lexicon legs keep "their names, argv, guards
and ceilings".

**Fix.** Moot if B1 is taken and S8 is dropped. If any part of S8 survives, name both carriers in S8,
add `tools/lexicon/kit.toml` to the §4 table, and add a criterion asserting the two guard arrays are
equal — since no shipped check compares them.

**Left-shift.** Extend govkit's descriptor-vs-manifest parity arm to compare the `guard` array in
both directions, alongside name and subject. Small, and it closes a divergence class the build has
now identified twice from opposite sides without anyone gating it.

---

### H2 — AC5's standing arm merges a fixture it wrote itself

**Address:** spec 4 §6 AC5, with §8's residual paragraph. Confirmed id 3.

AC5 states both halves and they contradict: "a standing selftest arm … so an edit that removes the
separation F1 chose reds it", against "the arm and every figure behind it run over a SYNTHESIZED
block". An arm that writes its own separated `PINS` fixture merges clean regardless of how dense the
tracked `.lexicon.conf` has become, so it cannot red on the hazard it is named for.

§8 attributes AC5's blindness solely to `lexicon selftest` being chunk `selftests` with guard
`["tools/lexicon/"]`, and offers the DoD's explicit `GATE_SELFTESTS=1` run as the compensating check.
That run reaches the arm, but the arm still never reads the real declaration, so the compensation is
inert. Once unit 7 pastes a real `PINS` block, the ratified F1 separation property has no observation
at all.

**Fix.** Add a scope row and a criterion for a textual invariant over the tracked declaration — no
two `PINS` rows adjacent — evaluated where a conf edit is actually read, which is the unguarded
`lexicon naming predicates` leg rather than the guarded selftest. Restate §8's compensating-check
paragraph to name the fixture-vs-tree gap rather than only the leg gating.

**Left-shift.** Add to the spec-review checklist: an acceptance criterion whose input is synthesized
by the arm itself cannot observe a property of a tracked file, and must say which tracked-file arm
does.

---

### H3 — AC8's neighbour-contract command prints nothing

**Address:** spec 4 §6 AC8. Confirmed id 5.

AC8 names `python tools/codebase-map/map_extractors.py` as the observation for "still yields 23
lexicon-verbs inventory keys". Verified on this tree: that module has zero `__main__` blocks and no
CLI — it exposes `inventory_ids()` / `all_inventories()` as library calls — so the command exits 0
printing nothing whether the count is 23, 0, or the dict is empty.

That half of AC8 is the only criterion protecting `tools/codebase-map/map_extractors.py:139-168`'s
read of the widened `VERBS` block, and §7 leans on AC8 to make the neighbour contracts "observable
from this unit rather than at some later push".

**Fix.** Replace the command with one that prints the number —
`python -c "import sys; sys.path.insert(0,'tools/codebase-map'); import map_extractors; print(len(map_extractors.all_inventories()['lexicon-verbs']))"` —
and state the expected `23` beside the command that produced it.

**Left-shift.** Laziest durable fix: give `map_extractors.py` a three-line `__main__` that prints each
inventory name and its key count. One edit turns a whole class of unfalsifiable neighbour-contract
criteria into real observations, in this build and every later one.

---

### H4 — `verdict_pass` is a name this build's own gate refuses

**Address:** spec 3 §2 S5 and §4 Data model (the two-passes paragraph), contradicting §6 AC2 and §7.
Covers confirmed ids 16, 26.

```
$ python tools/lexicon/lexicon.py --suggest verdict_pass
`verdict` is not in the declared table, and no row bans it by name. Declared verbs: add arm build
check cmd derive extract init load main measure parse print read remove render resolve run scan
seed set test write
```

`tools/lexicon/lexicon.py` is itself graded corpus. `.lexicon.conf:164` holds
`VERB_OFFENDER_PIN="461"` and the measured count is 461, so a new module-level `verdict_pass` takes it
to 462 and `tools/lexicon/lexicon.py:697` (`if len(unwaived) > pin:`) reds `lexicon naming
predicates` — the first leg in this unit's own §7 — on the unit's own commit. Nothing offsets it: all
five functions this unit deletes lead with already-declared verbs. AC2 fails independently too, since
`--measure` prints the measured count, so the pin line moves from 461 to 462 and cannot be
byte-identical. The unit's other two names, `scan_corpus` and `measure_pass`, are clean.

**Fix.** Rename to a declared verb — `check_verdict` and `run_verdict` both resolve — or add the
`.lexicon.conf` VERBS row or the waiver row to §2 and rewrite AC2 to expect the moved pin line. Add
an Inventory table to §4 naming each minted identifier with its `--suggest` verdict.

**Left-shift.** Make `TOOL-aSurfacedLexicon-4`'s §4 Inventory table a spec-template requirement: every
identifier a Tier-2 spec mints carries its `--suggest` verdict. That is exactly the ask the lexicon
Skill exists to answer, and unit 4 already proves it costs one table.

---

### H5 — the `--brief` residue grep does not run, and its answer is wrong by 34 hits

**Address:** spec 3 §6 AC8, contradicting §4 Migration. Confirmed id 19.

`grep -rn -- "--brief" --include=*.py --include=*.sh --include=*.md .` puts the options after `--`, so
grep reads them as filenames: run verbatim it errors three times with "No such file or directory".
Run correctly and excluding `memory/`, the carriers that SURVIVE this unit — which touches none of
`tools/unattended/` — are 35 hits across six files: `tools/unattended/unattended.test.sh` 21,
`tools/unattended/unattended.sh` 9, `tools/unattended/PROTOCOL.template.md` 2,
`tools/unattended/SKILL.template.md` 1, `tools/unattended/VERBS.template.md` 1,
`.claude/skills/unattended/SKILL.md` 1. AC8 claims a single hit. The criterion also greps `.`
including `memory/`, where this spec itself carries nine occurrences.

§4 Migration's carrier list is correct and lexicon-scoped. AC8 contradicts it, and taken at face
value points a builder at the unattended kit.

**Fix.** Scope AC8 to the carriers this unit owns — `tools/lexicon/`, `tools/codebase-map/`,
`.claude/skills/lexicon/` — move `--include` before the `--`, and state the unattended residue as an
expected set of six files rather than an expected single line.

**Left-shift.** Extend the build's MEASURE, NEVER ESTIMATE rule from figures to COMMANDS: every shell
command written into a §6 criterion is run at spec time and its output pasted. Four of this round's
findings (H3, H5, M1, L1) are one habit.

---

### H6 — byte-identity is unsatisfiable because the deleted functions are graded corpus

**Address:** spec 3 §6 AC1 and AC2, restated as a §3 non-goal. Confirmed id 25.

Staged and measured. Baseline `python tools/lexicon/lexicon.py --check` prints
`lexicon: P1 verb   graded=1045 offenders=461 waived=0`. After staging S1+S2's five top-level
deletions from `tools/lexicon/lexicon.py` (`read_object_state:881`, `read_token_is_live:899`,
`read_object:906`, `run_brief:916`, `run_probe:1053`) the same command prints `graded=1040`, offenders
unchanged. Only the `P3 layer` row was carved out of the comparison, not the `graded=` figures.

So AC1's "every surviving line is byte-identical" and §3's identically-worded non-goal are both false,
and the unit's primary safety argument evaporates with them. One overshoot worth recording: AC2
survives on its own terms, because `--measure` emits only the three pin scalars and offenders stay at
461 — until H4's `verdict_pass` moves them.

**Fix.** Rewrite AC1 to compare the lines whose invariance the unit actually claims — the offender
counts, the coverage line, the `lexicon OK` line, the pin lines — and state the expected `graded=`
delta as a figure derived at build time rather than typed. Correct §3's non-goal to "no predicate's
VERDICT changes".

**Left-shift.** Checklist entry: a unit that edits a file its own tool grades may not assert
byte-identity of that tool's output; it states the expected delta and the command that derives it.

---

### H7 — three units move symbols in a generated artifact an unguarded leg re-derives

**Address:** three specs, three separate edits. Covers confirmed ids 28, 29, 30.

- `spec-…-2.md` §4 Files touched ("Thirteen files, one of them a deletion"), §7 Gates, §6 AC9.
- `spec-…-3.md` §4 Files touched ("Ten files, no deletions and no additions"), §7 Gates, §6 AC9.
- `spec-…-4.md` §4 Files touched, §7 Gates.

`tools/codebase-map/map_lib.py:316-349` indexes every public module-level def/class into
`memory/map/generated/symbols.json`, and `tools/codebase-map/test_codebase_map.py:138-147`
byte-compares that committed artifact against a live re-derivation. The leg `codebase-map coverage +
freshness` carries **no** `guard` key, chunk `declarations`, subject `repo` — it runs on every bar
including the push boundary.

Verified present in `symbols.json` with `file: tools/lexicon/lexicon.py`: `build_module_index`,
`check_layer_violation`, `resolve_import`, `scan_unselective_rules` (unit 2's deletions) and
`run_brief`, `run_probe`, `read_object`, `read_object_state` (unit 3's). Unit 3 also ADDS a row with
`scan_corpus`. Staged unit 3's deletions and observed
`FAIL test_generated_artifacts_are_fresh` / `STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write`.

Unit 4's exposure is real but narrower than its finding claimed, and I checked rather than took it: of
the seven identifiers §4's Inventory mints, `_parse_rows`, `_parse_cells` and `_parse_pins` are
excluded as leading-underscore and `SURFACES`, `CONVENTIONS`, `PIN_PREDICATES` as plain assignments —
`lexicon_conf.py` has no `__all__`. `check_declaration` alone lands, and one new public def is enough
to red the leg.

Naming this leg when a unit moves map-visible keys is house convention, not an omission every spec
makes: `aBoundedVerdict-11/-13/-14`, `aClosedDocket-2`, `aFusedCharter-1/-2/-3` and `aMendedLedger-1`
all do it.

**Fix.** In each of the three specs: add `memory/map/generated/*` to §4 Files touched (correcting the
hard counts and, in spec 3, the "no deletions and no additions" clause), add a scope item running
`python tools/codebase-map/gen_map.py --write` in the same commit, and name `codebase-map coverage +
freshness` in §7. Extend spec 2's and spec 3's AC9 to enumerate it alongside `dead-path carriers` and
`testsuite counts`.

**Left-shift.** Add a hygiene check: a spec whose §2 adds or deletes a public module-level def in a
tracked `.py` file must name `codebase-map coverage + freshness` in §7. The predicate is cheap — the
scope prose already says "delete" and the path is right there — and it fires on the class rather than
on these three instances.

---

### H8 — AC10's premise states the reverse of what its four carriers say

**Address:** spec 4 §6 AC10 and §2 S9's carrier list. Confirmed id 38.

AC10's load-bearing sentence is that "the ratchet the conf and all three waiver headers claim does not
exist in any line of Python". Verified against source, it is false as written. `.lexicon.conf:29`
reads "Shrink-only: the count may fall, never rise"; all three
`tools/lexicon/lexicon-*-waivers.txt:2` headers read "SHRINK-ONLY: the count may fall, never rise";
and `tools/lexicon/lexicon.py:697` is `if len(unwaived) > pin:` — which is that rule, implemented.
What does not exist is a guard on a FALL, which is the opposite claim.

§4's files-touched table lists `lexicon_conf.py`, `lexicon.py`, `selftest.py`, `gate-legs.json`,
`.gitattributes` (marked untouched) and `README.md` — no `.lexicon.conf` and no waiver headers. So
AC10 can be met in full while four tracked carriers state a rule the shipped engine contradicts, and
three of them are kit files every adopter receives on the next `govkit update`.

**Fix.** Rewrite AC10's premise to say the fall direction is unguarded. Add a scope item amending
`.lexicon.conf:29` and the three waiver headers to the two-sided wording, and list all four files in
§4 Files touched.

**Left-shift.** Once the pin is two-sided, add a selftest arm that stages a pin ABOVE its measured
value and confirms RED — the failing case for the new half, per build rule 3, which is otherwise
unobserved for the direction this unit adds.

---

### H9 — the map dossier keeps describing the deleted predicate

**Address:** spec 2 §2 S9 (carrier list) and §4 Files touched (the thirteen-file list). Confirmed id 41.

`memory/map/features/lexicon.md` is a P3 prose carrier the scope omits, in four places this unit
falsifies: the front-matter title ("Three naming predicates over a per-repo DECLARATION"), `:90` (the
unselective-LAYERS rule), `:93-98` ("What P3's correctness rests on is `resolve_import`"), `:109-110`
("An empty `LAYERS` reports `NOT ARMED` and exits non-zero"), and `:171-181` (P3's resolver limits and
the `_glob_match` adversarial rounds).

S9's carrier list names `README.md`, `LEXICON.md`, `scaffold_lexicon.py`, `AGENTS.md` and the
template. No sibling picks the dossier up either — spec 12's files-touched table names it only for
"the BLOCKED claim about the map wiring". AGENTS.md §1 DoD requires "dossier prose refreshed on
touch", so the unit as specced lands with the codebase map's own dossier documenting a predicate that
no longer exists.

One correction to the finding as received: the `codebase-map coverage + freshness` leg would NOT
catch this. It grades claimed keys, not prose. Nothing catches it today.

**Fix.** Add a scope item for `memory/map/features/lexicon.md` naming those ranges, and add the file
to §4 Files touched (fourteen files).

**Left-shift.** This is the hand-kept-inventory-disagrees-with-source class the drift audit exists
for, and the cheapest real gate is a drift signal rather than a bar leg: have
`tools/drift-audit/drift_report.py` grep `memory/map/features/*.md` for backticked identifiers absent
from `memory/map/generated/symbols.json` and report them. Seconds, stdlib, no agents, and it catches
stale dossier prose for every feature rather than this one.

---

### H10 — the ground for deleting `--brief` is refuted by prior art it never cites

**Address:** spec 3 §4 Alternatives rejected, the "Keep `--brief` and only collapse the walks"
paragraph, with §3's understatement of the loss. Confirmed id 43.

The stated ground — that `--brief` is "the corpus-as-authority direction the canon exists to close" —
is contradicted by the shipped surface and by the records that built it, neither of which the spec
cites. `tools/lexicon/SKILL.template.md:34` says `--brief` "prints what the corpus DOES, never what it
should do, and it decides nothing", and `:37` "Neither verb can exit 1 and neither prints a pin. They
are reports, structurally." `TOOL-dScaffoldedMirror-8` draws the anti-mirror line at SELECTION, not
reporting: "the corpus is admitted as evidence for exactly one thing — which spellings become debt
rows. The corpus votes to EXCLUDE, never to select." Flagging objects spelled more than one way is
that admitted use. `TOOL-dScaffoldedMirror-10`, which built `--brief` per-object on a measured
rationale, is CLOSED and was called "the highest-VALUE unit in the build", and `run_brief`'s own
comment near `tools/lexicon/lexicon.py:983` calls `--brief` on an uncommitted file "the lexicon
Skill's PRIMARY path".

§3 understates the loss as "one of its two routes" when the route lost is the one the source names
primary, and §8's replacement (`scaffold_lexicon.py <path-outside-the-repo>`) answers `--probe`'s
pre-adoption question, not `--brief`'s name-this-object question. Nothing in the spec replaces it.

**Fix.** Cite `TOOL-dScaffoldedMirror-8` and `TOOL-dScaffoldedMirror-10` by id in §4 and either refute
the debt-reporting reading against the anti-mirror rule's own wording, or re-ground the deletion on
cost alone — which is a defensible ground and does not need the canon. Name in §3 which later unit
restores the Skill's primary path, since §3 already concedes the gap is only "for the units between".

**Left-shift.** Extend TEMPLATE-SPEC's §10 retrieval-terms requirement to §4 Alternatives: a rejection
ground that contradicts a CLOSED unit cites it by id, and the memory-recall terms used to look are
recorded. §10 already forces this discipline for seams; rejections are where it is actually being
skipped.

---

### M1 — the one-walk claim is observed by a grep that misses a target and counts survivors

**Address:** spec 3 §6 AC9. Confirmed id 8.

AC9 observes "`scan_corpus` is the only corpus walk left" with `grep -c "for rel in files"` and states
no expected value. Measured, that fixed string matches six sites — `tools/lexicon/lexicon.py:170`
(`scan_definition_carriers`), `:355` (`build_module_index`), `:550` (`run`), `:1076` (`run_probe`),
`tools/lexicon/scaffold_lexicon.py:70` and `:124` — while §4's fifth named walk, `lexicon.py:994` in
`run_brief`, is spelled `for f in tracked_files(root):` and does not match at all. The criterion counts
two survivors it never meant to name, misses one of its own five targets, and passes for any new walk
spelled differently. The unit's central structural claim has no observation that could fail.

**Fix.** Restate AC9 as an enumeration with a number: every `extract`/`tracked_files` call site in the
two files resolves inside `scan_corpus`, expected caller count stated and derived by a named command
at build time.

**Left-shift.** Same habit as H5 — run the criterion's command at spec time and paste its output. A
`grep -c` with no expected value beside it is not an observation.

---

### M2 — the refusal's placement against the `--measure` return is unpinned

**Address:** spec 2 §4 Data model (the three binding conditions, repeated verbatim in §8's
ratification) and §6. Confirmed id 31.

`run()` has two returns that matter: the NOT ADOPTED return at `tools/lexicon/lexicon.py:478-480` and
the `measure_mode` return at `:669-680`. The three binding conditions pin the first and say nothing
about the second, while S6 says only "add the self-containment refusal … to the `run()` check path" —
which reads equally as the `--check` branch below `:680`. A refusal written there is reachable from
`--check` and not from `--measure`: the armed-but-unreachable class this file confesses to three
separate times, at `:624-632`, `:654-663` and `:738-745`, and the class its sibling at the same build
order is building a differential arm to close.

Nothing in §6 would catch it. AC1-AC3 and AC5-AC9 are `--check`-side, and AC4's only `--measure`
assertion counts pin lines. The established repair in this file is to append to `problems` above the
measure return, and the spec never says `problems`.

**Fix.** Make it a fourth binding condition: the refusal enters the shared `problems` list above the
`measure_mode` return at `:669`, so both modes see the same refusal set. Add an AC that
`python tools/lexicon/lexicon.py --measure` exits 1 with the refusal when AC2's `import map_lib` break
is staged.

**Left-shift.** The differential arm the sibling unit is already building — assert `--check` and
`--measure` produce the same refusal set for every staged break — is the gate for this class. Make it
a named dependency of this unit rather than a coincidence of ordering.

---

### M3 — S2 preserves a `LAYERS` dispatch arm that does not exist and that unit 2 deletes first

**Address:** spec 4 §2 S2. Confirmed id 32.

Both halves are wrong against the tree. `_parse_block` at `tools/lexicon/lexicon_conf.py:99-119` tests
only `if key == "VERBS"`; the glob-pair code at `:110-119`, with the arrow refusals at `:112-113` and
`:116-117`, is the unconditional fall-through DEFAULT, not a keyed arm. So S2's "dispatch stays keyed
on the block name … `LAYERS` keeps its arrow refusal at `:113-117`" describes a shape the module does
not have, and an implementer adding a generic default would have to CREATE a `LAYERS` arm to honour
it. And the order-independence claim is false: `TOOL-aSurfacedLexicon-2` is order 1 to this unit's
order 2, and its S5 removes `LAYERS` from `BLOCK_KEYS` at `:32` and deletes that branch. Spec 4's
line 144 ("the unit that deletes `LAYERS` owns that breakage, which is why this one does not touch
it") does not rescue S2, because S2 names `LAYERS` as a branch to preserve.

**Fix.** Rewrite S2 for both orderings: state that `_parse_block` today has one keyed arm (`VERBS`)
plus a `LAYERS` fall-through, that after unit 2 the fall-through is gone, and that this unit's job is
a keyed `CELLS`/`PINS` dispatch with `_parse_rows` as the default. Drop the order-independence claim
or restate it with its stated difference, and cross-reference `TOOL-aSurfacedLexicon-2` S5 by id.

**Left-shift.** Hygiene check: a spec asserting order-independence from a sibling must name that
sibling's unit id. Currently the claim is unattributable, which is why it went unchecked.

---

### M4 — the replacement refusal inherits no liveness assertion

**Address:** spec 2 §4 Data model and §6. Confirmed id 42.

The thing S3 deletes existed to buy exactly one liveness assertion. `tools/lexicon/kit.toml:107`,
deleted by S3, reads: "An empty declaration makes the engine report NOT ARMED and red rather than
green: an unarmed predicate that exits 0 is indistinguishable from a satisfied one, and this is the
hole where that distinction is bought." The dossier repeats it at `:109`.

The replacement gets no arm that fails on an empty population. §5's observability bullet only PRINTS
the population, and AC3 pins the shape of that line while explicitly disclaiming its value as
gov-scoped — so a zero greens. That is the DEAD PROBE class `TOOL-dScaffoldedMirror-2` closed, and the
charter §7 rule that a probe which cannot move says so. The finding's secondary claim is wrong and I
am recording that: `Path(__file__).resolve().parent` and a tracked-file walk compose fine through the
`tracked_files` seam §10 names, so §4's two descriptions of the walk are not incompatible. The missing
liveness arm stands on its own.

**Fix.** Add an acceptance criterion that a zero-population self-containment run REDS rather than
printing a zero, and say in §4 which source the population comes from.

**Left-shift.** The kit already refuses on DEAD PROBE and DEAD SNIFFER. Route the new refusal through
the same shape rather than inventing a second one — no new gate needed, just reuse of the one the
engine ships.

---

### L1 — the dead-path carrier count does not reproduce

**Address:** spec 2 §4 Migration, the dead-path paragraph. Confirmed id 36.

"`grep -rn lexicon-layer-waivers` finds five carriers outside `memory/`" does not reproduce. Ran it:
seven lines across four files — `tools/govkit/fixtures/incms-2cff5855.receipt.json:128,129,597,600`,
`tools/lexicon/kit.toml:26`, `tools/lexicon/selftest.py:84`, and `tools/lexicon/lexicon.py:93` (the
`WAIVER_FILES["layer"]` row, which the sentence never names). No reading reconciles to five: not
lines, not files, and not spellings, since S10 itself calls the receipt hits "four spellings". S2 does
cover `:93`, so nothing is left unfixed — but this paragraph is the implementer's checklist for the
unguarded `dead-path carriers` leg, and it states a figure the command it names contradicts.

**Fix.** Re-run the grep, paste the derived count with its command, and list `tools/lexicon/lexicon.py:93`
alongside `kit.toml:26` and `selftest.py:84` as the three engine carriers S2/S3/S7 edit, with the four
receipt spellings S10 waives.

**Left-shift.** Covered by H5's rule — commands as well as figures get run and pasted. This is the
charter's "a number typed beside the thing it counts" ban, in a spec rather than in code.

---

## Notes on the round

**Precision was 0.49**, at the low end of the useful band. Twenty-three of forty-five raw findings
were refuted, and the refuted set clustered on lenses re-deriving the specs' own reasoning rather than
checking it against the tree. The confirmed set has the opposite property: nearly every survivor was
confirmed by RUNNING something — `govkit selfcheck` on a staged guard, `--suggest` on a minted name,
`--check` on a staged deletion, the map freshness assert on five removed symbols. For round 2, prime
finders to reach for the interpreter before the argument.

**Two findings were narrowed rather than dropped**, and the narrowing is recorded above so a later
reader is not misled: H7's unit-4 arm covers one identifier, not the seven its raw finding listed, and
H9 does not fire the coverage leg. Both conclusions survive; their enumerations did not.

**Three cross-cutting habits would have prevented eleven of the sixteen rows.** Run every command a
spec writes into §6 and paste the output (H3, H5, M1, L1). Run every minted identifier through
`--suggest` and table the verdict, as unit 4 already does (H4). Read the `kit.toml` of every kit a
unit touches during §10, since the descriptors in this repo carry refusals in prose that no gate
restates (B1, H1, M4).
