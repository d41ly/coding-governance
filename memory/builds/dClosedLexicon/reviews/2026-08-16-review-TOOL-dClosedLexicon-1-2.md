# review-dClosedLexicon-2 — M4 spec audit of TOOL-dClosedLexicon-1 rev-5 and TOOL-dClosedLexicon-2 rev-2

**Serves:** spec-audit TOOL-dClosedLexicon-1 TOOL-dClosedLexicon-2  <!-- inferred: its H1 names both specs and their revs -->

## Verdict: BLOCKED

**Subject:** `spec/2026-08-16-spec-dClosedLexicon-1.md` at rev-5 and
`spec/2026-08-16-spec-dClosedLexicon-2.md` at rev-2 · base a9bd87d5 · node d · 2026-08-16

M4 multi-agent audit: independent finder passes, an adversarial skeptic pass over every finding, then
this synthesis. Forty-nine raised findings resolved to nine confirmed and twenty-eight refuted; none
went unjudged. Two confirmed blockers make a unit unbuildable as written — unit 1's S12 specifies a
gate whose first assertion is permanently false in this repo, and unit 2's S3 specifies a signal in a
file that cannot declare one. The next act is an unattended build with no owner turn, so both must
fold into a rev bump before it starts.

Findings the by-design list covers — unit 1's folded R1-R9, the cut pin-direction guard (F-A14),
unit 2's open F1, `PLAY-dClosedLexicon-1`'s ceiling block, and the kit's deliberate opt-in
unmeasurability (F-A5) — are not re-reported. R5 below is the one exception the brief allows: it
names precisely where a rev-3 fold imported a wrong premise from the review it folded.

## R1 — `check-placeholders.sh` asserts something permanently false of this repo's own tracked files

**What it is.** S12 specifies `tools/check-placeholders.sh` "asserting three things over the shipped
playbook files", the first being that "no `{{`-shaped placeholder survives". AC10 makes that
explicit: "When any `{{`-shaped placeholder survives in either shipped file,
`tools/check-placeholders.sh` reds." §7 puts `bash tools/check-placeholders.sh` on this repo's merge
bar as a new leg, invoked bare with no argument. But in gov the shipped playbook files ARE the
un-instantiated template sources: they carry placeholders permanently and by design, and S13 in the
same spec deliberately adds another one. The spec never states whether the gate's subject is gov's
source, an adopter's rendered tree, or a fixture, and those readings produce different scripts.

**Evidence verified.** Measured in the tree: `parallel-coding-governance.template.md` carries 23
distinct `{{…}}` placeholders, `parallel-coding-governance.domain-rules.md` 14,
`parallel-coding-governance.customize.md` 36 — none filled, and no filled instantiation is tracked
(`AGENTS.md` is bespoke, not a render). AC9 presupposes the opposite state — "When `{{MEMORY_ROOT}}`
is filled with different values in the two shipped files" — and `{{MEMORY_ROOT}}` is unfilled in
both, which also makes S12's second assertion vacuous on gov's tree. Every existing implementation of
this predicate in the tree is render-side and says so: `tools/govkit/entries/playbook.kit.toml:28-34`
is already this exact check, `[[hole]] id = "playbook-placeholders"`, discharged as
`! grep -qE '\{\{[A-Z]' "$1" "$2"` over `{playbook_path}` and the DEPLOYED companion;
`tools/unattended/adopt-unattended.sh:131` greps the RENDERED skill;
`tools/memory-tree/kit-dogfood-parity.test.sh:91` greps `render "$ship"`.
`parallel-coding-governance.customize.md` states the intended target in its own words — run the grep
over "both **written** files". §10's closing claim, "No existing seam covers the three predicates
themselves", is false against the govkit hole.

**Consequence.** The new leg reds on its own landing commit and can never go green here, so AC14
("every new leg appears in the green line by name") is unsatisfiable and `bash tools/run-gates.sh` is
red. An unattended builder either lands red or silently guts the assertion to reach green, shipping a
placeholder gate that asserts nothing.

**FIX.** In unit 1 §2 S12, replace the three-assertion sentence with an explicit subject split:
(a) the gov-side leg asserts only what is true of the SOURCES — that the `{{X}}` union over
`parallel-coding-governance.template.md` and `parallel-coding-governance.domain-rules.md` is exactly
the set catalogued in `parallel-coding-governance.customize.md`, that the catalogue's per-file tally
matches the measurement, and that a placeholder appearing in BOTH files is declared as shared rather
than as disjoint (`{{MEMORY_ROOT}}` is in both today, which is the live falsehood §4 Migration's
"corrected disjointness sentence" is reaching for); and (b) the no-surviving-placeholder assertion
becomes a `--check <target> <target>` mode exercised only by fixtures in
`tools/check-placeholders.test.sh`, never over the tracked sources. Rewrite AC9 and AC10 to name the
fixture rather than "either shipped file". In §10, delete "No existing seam covers the three
predicates themselves" and cite `tools/govkit/entries/playbook.kit.toml`'s `playbook-placeholders`
hole as the render-side owner of the survival predicate, plus
`memory/builds/aCandidStub/reviews/2026-08-10-review-aCandidStub-1.md:51` ("Gate A1 —
placeholder-coverage check"), which already designed the source-side gate this unit should build.

## R2 — unit 2's S3 declares drift signals in a file that cannot declare one

**What it is.** S3 specifies "two `drift-audit` signals in `tools/drift-audit/drift_signals.py`, each
seeded at a MEASURED pin", and §4 Data model says "S3's pins live beside the existing ones in
`drift_signals.py:PINS`". `drift_signals.py` is the project-owned DATA layer. The signal set is a
hardcoded list of engine functions, and `PINS` is keyed by the name the ENGINE emits, so a `PINS` key
naming a project-invented signal is silently inert. The only project-layer extension hook is
`HANDKEPT`, and every row folds into ONE signal with ONE shared pin.

**Evidence verified.** `tools/drift-audit/drift_report.py:488`
`SIGNALS = [signal_ledger, signal_spec_status, signal_shrink_only, signal_handkept,
signal_dangling_pointers, signal_closed_specs_untraceable]` — a module-level list in the engine;
`:117` the project layer is validated for exactly `("PRODUCT_GLOBS", "SHRINK_ONLY", "HANDKEPT",
"PINS")`; `:584-586` `out = [s(ctx) for s in SIGNALS]` then `s["pin"] = ctx.pins.get(s["signal"],
s["tolerance"])`; `:322-355` `signal_handkept` sums `gap += max(0, actual - claims)` across ALL
`HANDKEPT` rows into one value under `handkept_inventories_disagreeing_with_source`, pinned at
`drift_signals.py:177` to `0` with the comment "DRAINED to 0". Measured live today:
`handkept_inventories_disagreeing_with_source  0  55  ok (pin 0)`. `drift_signals.template.py`
exposes no signal-declaration hook — the project surface is `{record, source, probe}` rows only.
Unit 2 §4 Files touched names `drift_signals.py` and `selftest.py` but NOT `drift_report.py`: it
edits the shipped kit's test while excluding the shipped kit's engine.

**Consequence.** AC3, AC4 and AC5 all assert a mechanism no S<n> constructs. A builder following S3
literally adds two probe functions nothing calls — inert, with a green gate, which is the dead-
instrument class this kit exists to prevent. A builder routing them through `HANDKEPT` gets no
per-signal pin, so AC3's "above the seeded pin" and AC4 are unobservable, and §4's own prediction
that "the day-one seed will not be zero" then forces the SHARED pin off its drained 0 — blinding the
charter-completeness ratchet that rides the same signal (see R4). A builder who does it correctly
edits a shipped generic engine, coupling `drift-audit` to an optional kit for every adopter who takes
it without the lexicon: the exact failure this spec's own §4 Alternatives rejects for
`map_extractors.template.py`.

**FIX.** Take the ENGINE route and write it down. In unit 2 §2, restate S3 as two new signal
functions appended to `tools/drift-audit/drift_report.py:SIGNALS`, each with its own `PINS` key in
`drift_signals.py`, and each reporting `gateable: False` with a "not asked" reason when
`.lexicon.conf` is absent — the shape `signal_closed_specs_untraceable` already uses at
`drift_report.py:420-426` — so no adopter without the lexicon inherits a DEAD gateable signal. Add
`tools/drift-audit/drift_report.py`, `tools/drift-audit/README.md` and the `drift-audit` kit-version
bump (the `KIT_DRIFT_AUDIT_VERSION` constant, every `gov:kit drift-audit@` marker, and both
`tools/workflows/drift-audit-{code,state}.js` `meta.versions`) to §4 Files touched, and add a §3
sentence saying why coupling the shipped engine is acceptable here when it was rejected for
`map_extractors.template.py`. If the author prefers the project-layer route instead, S3 must say
explicitly that both questions become `HANDKEPT` rows sharing
`handkept_inventories_disagreeing_with_source`, drop "each seeded at a MEASURED pin", rewrite AC3 and
AC4 against that one signal, and carry the written justification `drift_signals.py:148-149` demands
for raising a pin the tree just drained to 0.

## R3 — the landing commit cannot be green: `LAYERS` is never stated and the "predicates OFF" rollout has no mechanism

**What it is.** S3 makes an un-declared `LAYERS` a hard RED ("With no `LAYERS` declaration the
predicate reports `NOT ARMED` and the run reds, never passes green over an absent declaration"), AC3
repeats it, and §3 removes the escape route ("A `--scaffold` proposal for P3. The layer map is
hand-declared in this unit"). No section — §2, §4 Data model, Migration, Rollout or Inventory —
states what this repo's forbidden-import direction map is. `.lexicon.conf` appears in NO Files
touched list in either unit, although it is a new tracked root file two gates must read. §4 Rollout
says to "Land the kit with its predicates OFF for this repo … then arm the legs in a second commit"
and names no OFF mechanism.

**Evidence verified.** §4 Data model gives only the shape: "`LAYERS` | `<glob> -> <glob>` pairs naming
a FORBIDDEN import direction; empty means `NOT ARMED`". AC7 requires `bash
tools/lexicon/adopt-lexicon.sh --check` to red on an empty `ratified` key, and §4 Rollout requires
ratifying the derived table — both of which read a `.lexicon.conf` the spec never budgets. AC14
requires every new leg green "on the landing commit". With the legs in `tools/gate-legs.json` and no
ratified conf, the run reds by AC3 and AC7; with the legs absent they cannot appear in the green line
at all.

**Consequence.** The builder must author this repo's governance layer map with zero specification —
unreviewed policy invented by an unattended run — or disarm P3 in a way S3 forbids. Either way AC14
fails.

**FIX.** Three concrete edits to unit 1. (1) In §4 Data model, state gov's own `LAYERS` value. The
spec already contains one true forbidden direction: S5 requires the lexicon to be self-contained and
to import nothing from `codebase-map`, so seed `LAYERS` with `tools/lexicon/* -> tools/codebase-map/*`
and say that this is the declaration the landing commit ratifies. (2) Add `.lexicon.conf` to §4 Files
touched in unit 1, naming it as a new tracked root file. (3) Make §4 Rollout mechanical rather than
narrative: commit 1 lands `tools/lexicon/` with NO leg rows in `tools/gate-legs.json`; commit 2 adds
the leg rows, `.lexicon.conf` with the measured pins, the `LAYERS` value and the `ratified` stamp
together, and its message carries the measured numbers. Reword AC14 to name the ARMING commit as the
one it observes.

## R4 — five new legs, no charter edit: the `drift-audit records` leg reds on the landing commit

**What it is.** Unit 1 adds five gate legs and edits neither `AGENTS.md` nor any drift pin. This repo
runs a gateable signal, pinned at 0, that counts legs in `tools/gate-legs.json` whose argv SCRIPT PATH
the charter's `## The gate suite` section does not cite.

**Evidence verified.** `tools/drift-audit/drift_signals.py:104-136` `_charter_mentions_every_leg`
reads `tools/gate-legs.json`, extracts each leg's argv script path, and counts how many appear inside
`re.search(r"^##\s+The gate suite.*?$(.*?)^##\s", charter)`; `drift_report.py:322-330` scores it as a
magnitude; `drift_signals.py:177` pins `handkept_inventories_disagreeing_with_source: 0`, commented
"DRAINED to 0: … the charter now names them in one bullet, so every leg on the bar is spelled there";
`drift_report.py:601` reds a gateable signal on `value > pin`. Measured live: `0 of 55 · ok (pin 0)`.
The `drift-audit records` leg — `{"name": "drift-audit records", "argv": ["python",
"tools/drift-audit/drift_report.py", "--check"]}` — carries NO `guard`, verified against the
manifest, so it runs on every invocation including the authoritative pre-push one. Unit 1 §7 adds
five legs, all with a `/`-bearing script path. §4 Files touched lists no `AGENTS.md`; the §4 Inventory
table, whose stated contract is "A new `tools/<kit>/` in this repo lands red without all of the
following", has no row for it; and §7's "Existing legs that must stay green" omits
`drift_report.py --check` entirely, which reads as closed.

**Consequence.** The signal goes 0 → 5 over a pin of 0 and the bar is red on the landing commit, for
a constraint neither spec records. AC14 fails, and the remedy is an edit to a file the spec never
names.

**FIX.** Add `AGENTS.md` to unit 1 §4 Files touched with the explicit requirement that the
`## The gate suite` section spell the SCRIPT PATH of each new leg —
`tools/lexicon/lexicon.py`, `tools/lexicon/selftest.py`, `tools/lexicon/adopt-lexicon.sh`,
`tools/check-placeholders.sh`, `tools/check-placeholders.test.sh`, plus the gov-internal splitter
parity leg. Add an §4 Inventory row: `charter gate-suite bullet | AGENTS.md | the drift-audit handkept
signal is pinned at 0 over leg argv paths`. Add `python tools/drift-audit/drift_report.py --check` to
§7's must-stay-green list, and add an AC observing it green after the charter edit. While editing §4
Files touched, add `memory/map/generated/` as a re-render — unit 2 lists it and unit 1 omits it for
the same gate.

## R5 — S12 and AC11 assert three `governance-template` markers; only two exist

**What it is.** S12 says "the three `governance-template: vN.N` markers agree" and AC11 tests "the
three shipped files". Only TWO files carry the marker. `parallel-coding-governance.customize.md`
carries none — and is explicitly not shipped. This is the one place a rev-3 fold is demonstrably
wrong rather than merely incomplete: R8 of `reviews/2026-08-16-review-dClosedLexicon-1.md` introduced
the miscount ("three shipped files that carry `<!-- governance-template: vN.N -->`") and rev-3 folded
it verbatim.

**Evidence verified.** Grep over the tracked tree returns exactly two markers:
`parallel-coding-governance.template.md:12` and `parallel-coding-governance.domain-rules.md:3`, both
`<!-- governance-template: v2.7 -->`. `parallel-coding-governance.customize.md`'s only hit is prose at
`:80` — "Both files carry `<!-- governance-template: vN.N -->`, and they are re-pulled **in
lockstep**" — which both fails to be a marker and declares the population is TWO; its line 7 reads
"**TWO files deploy together, and both carry placeholders:**". `tools/govkit/registry.toml:165-167`
exempts it from the shipped surface: "the deploy-time placeholder catalog. The runbook's own words
are 'read it, don't ship it'." `tools/govkit/entries/playbook.kit.toml:9` records the identical
lesson: "TWO files, not three. … counting it is how the spec over-stated this entry for four
revisions." §4 Migration assigns the marker bump to two files only — `customize.md` gets "the new
conditional-section row, the corrected disjointness sentence, and the placeholder tally", no marker.
§6 also contradicts itself: AC9 says "the two shipped files", AC10 "either shipped file", AC11 "the
three".

**Consequence.** A gate built to AC11 reds forever — a grep for the marker matches customize.md's
literal `vN.N`, which can never equal `v2.7` — or the implementer stamps a marker into the one
playbook file the deploy chain never ships, contradicting that file's own prose, the govkit
exemption, and §4 Migration's edit list, and adding a fourth thing to keep in lockstep at every
playbook bump.

**FIX.** In unit 1, change S12's third assertion and AC11 to name TWO marker-carrying files
explicitly — `parallel-coding-governance.template.md` and
`parallel-coding-governance.domain-rules.md` — matching AC9's "two shipped files", which becomes the
canonical population. In §4 Migration, change "The three shipped files move together or the lockstep
marker lies" to name the two marker carriers and to say separately that `customize.md` is the
deploy-time catalogue that is edited but carries no marker, citing
`tools/govkit/registry.toml:165-167`, so no later revision re-adds the third. This is the shape
`memory/builds/aCandidStub/reviews/2026-08-10-review-aCandidStub-1.md:52` already specified as
"Gate A2 — version-marker parity".

## R6 — the govkit chassis row is short by a descriptor and by two depth-1 files

**What it is.** §4 Inventory's registry row names only `tools/govkit/registry.toml` and frames the
failure as "an unregistered dir". Two things are missing. (a) A registry entry is two artifacts — the
`[[entry]]` row AND a `descriptor` file with a validated schema. (b) The declared surface is `tools/*`
at DEPTH 1 including FILES, so S12's `tools/check-placeholders.sh` and
`tools/check-placeholders.test.sh` are two new unclaimed surface paths needing their own entry or
exemption.

**Evidence verified.** `tools/govkit/registry.toml:25-31` `[surface] globs = ["tools/*", …]`;
`tools/govkit/govkit.py:97` `surface_paths` docstring: "`tools/*` means depth-1 entries under tools/
— a FILE at depth 1, or the directory a deeper tracked path sits in"; `govkit.py:516-519` fails per
unowned path: "tracked path '…' is in the declared surface but is neither an entry member nor an
exemption". Every `[[entry]]` in `registry.toml` carries a `descriptor`, and `govkit.py:load_toml`
raises `Refusal("no such descriptor: …")` when it is absent; `govkit.py:339-364` makes `version_from`
mandatory and single-match. Flat single-file gates have a live precedent —
`tools/govkit/entries/check-install-prefix.kit.toml`, whose `[[files]].claims` names both
`tools/check-install-prefix.sh` and its `.test.sh` — and an exemption precedent at
`registry.toml:149-151` for `tools/check-template-size.sh`. Unit 1 §4 Files touched names only
`registry.toml`; the unenumerated "twelve new files under `tools/lexicon/`" never names a descriptor.

**Consequence.** `python tools/govkit/govkit.py selfcheck` — an existing bar leg and AC13's own
observation — reds three ways the spec does not anticipate: a missing descriptor is a hard refusal,
and each unclaimed depth-1 file is its own failure. AC13 would be "satisfied" in wording while the leg
is red.

**FIX.** Split the §4 Inventory registry row into three rows and add all three artifacts to §4 Files
touched: (1) `tools/lexicon/kit.toml` — the kit descriptor, carrying `id`, `home`, `scope`,
`version_from` resolving to exactly one line, `[[files]]`, `[adopt]`, `[check]` and `[[gate_leg]]`
with guards; (2) the `[[entry]]` row in `tools/govkit/registry.toml` pointing at it; (3)
`tools/govkit/entries/check-placeholders.kit.toml`, a flat entry on the
`check-install-prefix.kit.toml` model whose `[[files]].claims` names both
`tools/check-placeholders.sh` and `tools/check-placeholders.test.sh` — or an `[[exempt]]` row per
file carrying a written reason.

## R7 — unit 2's teardown promise is unachievable with the mechanism S2 chose, and AC6 tests a weaker property

**What it is.** S4 states an absolute requirement — "Removing an optional kit must not red a
different optional kit's gate" — while S2 makes it unachievable, and AC6 observes a strictly weaker
property that can pass while the requirement fails.

**Evidence verified.** S2 (ratified to the dossier route at rev-2) has a dossier claiming the
`lexicon-verbs` keys under the both-directions ratchet. All three degradation routes red the map leg:
if the extractor returns `[]`, every dossier claim becomes stale and
`tools/codebase-map/test_codebase_map.py:79` `test_every_inventory_key_is_claimed_or_baselined` fails
on `cov.stale_claims` (`:87` "STALE CLAIMS (a dossier names a key that no longer exists)"); if the
extractor is removed from `EXTRACTORS`, the dossier's `[claims]` table names an id outside
`inventory_ids()` and `tools/codebase-map/map_lib.py:769` raises `MapError(f"{source}: unknown
inventory keys …")` — `map_lib.py:716-722` requires a dossier's claims to be exactly the project's
inventory ids; and `test_generated_artifacts_are_fresh` byte-compares a render that also moves. AC6
asks only that the map test "does not raise an unhandled `MapError`", which the degrade-to-empty
route satisfies while the leg is red on a plain assert.

**Consequence.** The teardown story ships broken while its acceptance criterion reports success, and
the failure surfaces in an adopter's tree at uninstall time as a red leg belonging to a kit they did
not touch — the exact scenario R2 raised and this unit was split out to fix. Note the rev-2 F2
resolution introduced this: the `baseline.toml` route it discarded produces no stale claims.

**FIX.** In unit 2 §2, state S4's uninstall as an ORDERED procedure rather than a goal: remove the
dossier's `lexicon-verbs` claims block first, then the `EXTRACTORS` entry, then re-render
`memory/map/generated/`, then delete `.lexicon.conf` — and require
`tools/lexicon/README.md` to carry that order verbatim. Rewrite AC6 to observe the property S4
promises: "When the documented uninstall order is followed to completion, `python
tools/codebase-map/test_codebase_map.py` exits 0 and `bash tools/lexicon/adopt-lexicon.sh --check` is
silent." Keep the existing `MapError` clause as a separate AC covering the mid-teardown safety arm,
where `bash tools/lexicon/adopt-lexicon.sh --check` names the orphan.

## R8 — `.lexicon.conf` has no declared grammar and three readers in two languages

**What it is.** §4 Data model places `.lexicon.conf` "at the repo root beside `.memory-tree.conf` and
`.codebase-map.conf`" and gives each key's value shape, but never the container grammar. The one
grammar it gestures at cannot carry the load-bearing key, and three separate readers must parse the
file from two specs.

**Evidence verified.** `.codebase-map.conf:2-4` documents the sibling grammar: "RESTRICTED grammar —
sourced by bash AND parsed by `map_lib.load_conf()`: plain KEY=VALUE, a value with spaces MUST be
double-quoted, no inline comments after a value, no `export`", and `map_lib.py:180-202` confirms
`load_conf` is strictly line-based with no multi-line support. §4 Data model specifies `VERBS` as "One
row per verb, `<verb>: <meaning>`, negative definitions included" — a multi-row block that grammar
cannot hold, and whose prose meanings contain spaces, defeating the nearest single-line house idiom
(`.memory-tree.conf:87`'s `ARMS_FLOORS`). Readers required: `tools/lexicon/lexicon.py` (S1),
`tools/lexicon/adopt-lexicon.sh` in bash (S9), and unit 2 S1's `map_extractors.py`, whose natural
seam is exactly `load_conf` — and no spec names an alternative seam.

**Consequence.** The implementer invents the format, and unit 2 must then match it by inspection
rather than by contract: two or three hand-written parsers for one file, authored from two specs, with
a disagreement between them silent.

**FIX.** In unit 1 §4 Data model, add a fenced example of a complete `.lexicon.conf` showing the
multi-row `VERBS` block, and name the SINGLE reader both units use: a `tools/lexicon/lexicon_conf.py`
the kit owns, with a `--print-verbs` mode for the bash side so `adopt-lexicon.sh` does not
reimplement it. In unit 2 §2 S1, state how `map_extractors.py` reaches that reader — an explicit
`sys.path` insert against the install prefix, or a subprocess call — and note the gated-copy
precedent at `tools/drift-audit/drift_report.py:79-88` if a second parser is chosen instead.

## R9 — unit 2's §8 cannot go terminal: neither fork carries `RESOLVED` on its bullet line

**What it is.** The hygiene gate grades only the FIRST line of each §8 item. Neither of unit 2's two
bullets carries `RESOLVED` there. F2 IS owner-resolved and the mark still will not count, because it
sits three physical lines down; F1 is open by design, and the spec never says how it discharges §8 at
close.

**Evidence verified.** `tools/memory-tree/check-memory-hygiene.sh:696-702`: for a terminal header an
ITEM is a line matching `/^[[:space:]]*[-*][[:space:]]/` or `/^###[[:space:]]/`, and `resolved`
increments only `if (rng[i] ~ /RESOLVED/)` on that SAME line; continuation lines are not items and are
never scanned for the mark. The gate then fires unless `items > 0 && items == resolved`. Unit 2's two
bullet first lines are `- **F1 — should \`codebase-map\` consume a lexicon-owned definition census?**
\`map_lib.python_symbols\`` and `- **F2 — dossier or baseline for S2?** A dossier makes each verb
claimable in prose and costs a real` — items = 2, resolved = 0. Sibling unit 1 puts `RESOLVED` on all
five bullet first lines, so this is a within-build divergence from the house shape.
`memory/TEMPLATE-SPEC.md` states the rule: "§8 must read `none` or be fully RESOLVED before the status
may go CLOSED/WONTDO (machine-checked)" — and its "the hygiene gate reads only §8's first non-blank
line" actively misleads here.

**Consequence.** The unattended run builds unit 2, sets the header to CLOSED at wrap-up, and
`bash tools/memory-tree/check-memory-hygiene.sh` reds with "(terminal Status with unresolved §8 Open
questions)". The bar blocks the landing with no owner turn available to resolve it.

**FIX.** Two edits to unit 2 §8, made now rather than discovered at wrap-up. (1) Move F2's resolution
onto its bullet's first line: `- **F2 — dossier or baseline for S2?** RESOLVED (owner, 2026-08-16):
dossier. A dossier makes each verb claimable in prose …`. (2) Give F1 its discharge in writing: state
in the bullet that at close it is marked in place as `RESOLVED (agent, <date>, delegated): deferred
pending a measured corpus, tracked as <TOOL backlog id>`, with the row filed in
`memory/backlog/TOOL.md` in the same commit. The mark must land on the bullet's first line.

## Refuted

Twenty-eight findings were raised and dismissed; several were raised in more than one framing, and the
count in parentheses says how many.

- **`ARMS_FLOORS` row states the chassis wrongly** (×3) — the code facts hold (`check-arms.py`
  discovers only tracked `*.sh` defining `fail() {`; a floor is optional; a floor naming an
  undiscovered gate hard-fails), but nothing in the spec directs adding `lexicon.py` to
  `ARMS_FLOORS`, and 6 of 7 shipped adopters define no `fail()` helper. An imprecise rationale column,
  not a fork an implementer must invent.
- **The gov-internal splitter-parity leg is constructed by nothing** (×3) — the leg is mandated by
  S5, by the §4 Inventory row and by AC15, and its location is named twice ("the way `tools/lib/` is
  gov-internal and ships nothing"; §10's `tools/lib/resolve-python.sh` precedent). Its absence from
  §7's enumeration is a completeness nit.
- **No corpus-scope key (`CORPUS_GLOBS`, exclusions, tracked-vs-filesystem)** — S4's "an extension
  present in the corpus with no declaration reds by name" only parses if the corpus is the whole
  tracked tree, which is a stricter contract than a globs key; every gate here reads tracked files.
- **Which languages ship a pattern set is never enumerated** (×2) — coverage is DECLARED per adopter
  by design (F-A12 deleted rev-1's nine-language list on a law this repo already wrote down), and AC5
  is proportional rather than vacuous: with no regex set there is no set that can go inert, and the
  corpus-side arm (S6/AC4) is armed regardless.
- **§4 Rollout's "predicates OFF" contradicts S3/AC3's hard red on an absent declaration** — the two
  govern different inputs: S3 covers a PRESENT conf with an empty `LAYERS`; §5's rollback covers an
  ABSENT conf, i.e. the kit uninstalled. (The genuinely unspecified half — the OFF mechanism and the
  missing `LAYERS` value — is confirmed as R3.)
- **Teardown reds the map gate regardless of how the extractor degrades** (×3, incl. "forbids the only
  two behaviours the map kit allows") — S4's documented uninstall ORDER is the mechanism, and AC6's
  narrow `MapError` wording deliberately targets review R2's complaint. The sharper form — that AC6
  tests a weaker property than S4 promises — survives as R7.
- **The §4 Inventory codebase-map row names only the `kits` inventory, omitting five `gate-legs` keys
  and the `memory/map/generated/` re-render** (×3) — a dossier's `[claims]` block spans every
  inventory at once (`memory/map/features/agent-cap.md` claims four `gate-legs` keys and one `kits`
  key in one block), so "one codebase-map dossier" is the correct vehicle, and the freshness assert
  prints its own regen command. (The re-render omission is folded into R4's fix as a one-line
  addition.)
- **The registry row omits the descriptor and the two depth-1 files** (medium framing) — refuted only
  in its weaker form, on the argument that an implementer driving AC13 to green would arrive at the
  right declaration. The stronger framing is confirmed as R6, which governs.
- **`LEXICON.md` is named with no path and the `HYGIENE.md` analogy points at a memory-root the gate
  rejects** — §4 Files touched enumerates every new file, and `LEXICON.md` fits no named slot except
  the twelve under `tools/lexicon/`; the analogy is invoked for the doc's SHAPE, not its destination.
- **AC14 and AC15 name observations no command produces** — verified that `check-kit-versions.sh`
  exits 0 silently, so AC14's "reports the pair" is loose phrasing, but its operative half is
  decidable and AC15's self-containment follows by construction from S5.
- **S12's `PLAY-aSealedCaravan-1` funding claim leaves `WIRE-INTO-PROJECT.md:98` carrying the same
  wrong tally** (×2) — the row is already fully funded by the in-flight sibling
  `memory/builds/aSiftedPlaybook/spec/2026-08-16-spec-PLAY-aSiftedPlaybook-4.md`, whose S4 corrects
  both carriers by name and whose AC5 greps both to 0.
- **Unit 2 §3's "Anything in `tools/lexicon/` itself" forbids the work S4 requires** — specific scope
  beats a blanket non-goal: S4 names the two files, AC6 makes the behaviour observable, §4 Files
  touched lists both, and review R2's FIX put that work in this unit by name.
- **Unit 2's header carries no `ratified` pointer** (×2) — nothing machine-checks it, the resolution
  is recorded in place, and F1 is open by design; a one-token records nit.
- **Unit 2 §9's rev-2 line says unit 1 "moves to DEFERRED", which rev-5 undid** (×2) — §9 entries are
  dated historical records; unit 1 WAS deferred when rev-2 was written, and rewriting a landed log
  line would corrupt the append-only history. A resuming session reads status from the sibling's own
  header and the generated build index.
- **Adding a tenth inventory makes `AGENTS.md`'s "nine inventories" wrong, and `AGENTS.md` is not in
  unit 2's Files touched** — prose staleness with no gate behind it; no signal reads an inventory
  count. (`AGENTS.md` does enter unit 1's Files touched for a different and gated reason — R4.)
- **`.lexicon.conf` gets three parsers with no declared grammar** (medium framings, ×2) — refuted in
  the form that leaned on `drift_report.py:79-88` as a ban on second parsers, which in fact
  establishes the gated-copy pattern. The grammar gap itself is confirmed as R8.
- **The R5 fold requires a leg that "must not ship" but places no file** — S5 and the Inventory row
  state the constraint twice and §10 names the precedent directory; placing it where
  `include = "**"` ships it would violate an explicit instruction.
- **§10's reuse audit omits `check-unattended.sh`, the seam its own query ranks first** — the seam
  prose was already present at the spec's base, and `check-unattended.sh` checks a declared PHASE
  vocabulary over run-state files, not the three predicates; the recorded lesson the finding invoked
  (a core-set floor is a shrink-only COUNT) is already obeyed by S7.

## What holds up

- **The coverage-mode framework (S4, §4 Coverage modes).** `parser`/`probe`/`dark` is the right answer
  to the fail-closed law at `map_extractors.py:134`, it is stated in a form an implementer can build,
  and F-A12's deletion of rev-1's nine-language list rather than its replacement is the law being
  obeyed rather than argued with.
- **The two-sided vacuity arming (S6 + S11, F-A15).** The reasoning is correct — the corpus-side arm
  really is defeated by an empty corpus — and rev-3's re-scoping of S6 back inside `lexicon.py`, on
  the grounds that a gate which cannot read its corpus must not pass green, is the right split.
- **S5's inversion to lexicon-owned with a gov-internal parity leg.** The R5 fold is sound: it names
  the `tools/lib/` precedent, states the direction of truth, and keeps the shipped kit self-contained.
- **F-A14's honesty about the cut guard.** The spec records what the cut costs instead of hiding it,
  names the two independent defects, and files the shared follow-up — the record a later session needs
  to act without re-arguing.
- **F-A6's byte arithmetic kept after it stopped binding.** Measured 32,682 against the present 32,768
  ceiling, both re-verified here; keeping the ledger as the proof that this unit never needed the raise
  is exactly right, and it is what lets rev-5 drop the predecessor cleanly.
- **Unit 2 §4's correction of the ratchet claim.** Separating the ADDITION direction (visibility, not
  cost) from the DELETION direction (the load-bearing half) is a genuine improvement on unit 1's
  oversold sentence, and "The day-one seed will not be zero" is the honest pin discipline this repo
  already practises at `non_terminal_specs_cited_by_product_source: 2`.
- **Unit 2 §2 S5.** Recording the `EXTRACTORS`-versus-`SYMBOL_EXTRACTORS` choice where an implementer
  reads it, with the reason (`map_extractors.py:129` — a new symbol there never fails CI), is the
  right form for a decision that would otherwise be re-litigated silently.
