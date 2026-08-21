**Serves:** research TOOL-dScriptedRepeat-1

*Research record · lens 4 of the dScriptedRepeat design pass · in-repo prior art and the reuse audit
(M5) · 2026-08-20 · node d · base `0d88d5f2` · streams tooling.*

*The question this lens was given: what does this repo already know about templates, declared
populations, and gating a document — and for each piece of NEW machinery playbook mode proposes,
what is the strongest case that an existing seam already does the job?*

---

## 0 · How to read this, and what is measured

Every claim below is either MEASURED — a `file:line`, a quoted byte, or a command whose output is
reproduced — or marked **INFERENCE**. Line numbers are against `0d88d5f2`.

Four commands produced most of the evidence and can be re-run:

```bash
python tools/govkit/govkit.py selfcheck            # the declared-population verdict, with its counts
python tools/codebase-map/reuse_lookup.py "<behaviour phrase>"
python tools/memory-recall/query.py "<question>" --terms "<8-14 words>"
python tools/memory-tree/corpus_ids.py --measure   # the read-path budget, live
```

**Recall terms used**, recorded so M7 does not have to re-compose them:

- `template render placeholder rendered artifact byte-compare parity marker region adopt drift shipped installed copy`
- `declared population registry descriptor unclaimed surface exemption stale both directions selfcheck claims inventory ratchet`
- `closed vocabulary verb table derived seed curated frozen prescriptive mirror of the code ratified scaffold lexicon`
- `park parked decision register backlog row proposal surfaced close override waiver blocks improvement`

**The headline.** Nine of the ten behaviours playbook mode needs already have a seam here, and two of
the seven owner-ruled forks are in tension with a machine-checked contract they did not know about.
The single most useful thing in this record is not a seam — it is `TOOL-aMouldedFolio-1`'s finding
that this repo's template to render to byte-parity mechanism is **green over documents that are
false**, because it grades sameness rather than truth. A PLAYBOOK TEMPLATE under that mechanism
inherits exactly that blind spot, and the spec has to say so in the gate's own header.

---

## 1 · The reuse verdict, one row per behaviour

This is §10's answer for the unit set, derived from the two probes above plus source reading. Verdict
vocabulary: **REUSE** (wire through it unchanged) · **EXTEND** (the seam grows by data, not by
plumbing) · **NEW** (no seam fits, evidence below).

| # | Behaviour playbook mode needs | Existing seam | Verdict |
|---|---|---|---|
| 1 | a third authorization discipline, refused outside a closed set | `check_authorization` · `tools/unattended/unattended.sh:794-798` | **EXTEND** — one `case` arm, plus four carriers that restate the set (§8.1) |
| 2 | directives that bind only playbook runs | `scope_of` · `unattended.sh:120-129`; `check_waiver_scope` · `:656-668` | **EXTEND**, and the gate's scope reader BLOCKS it as written (§8.2) |
| 3 | a PLAYBOOK TEMPLATE rendered into a target and gated | `render_playbook.py`; `kit-dogfood-parity.test.sh` `PAIRS`; the three `adopt-*.sh --check` legs | **REUSE** the mechanism, **and state its blindness** (§2) |
| 4 | every step tagged `GATE <leg>`, every leg runnable | `tools/gate-legs.json` names + govkit's `[[gate_leg]]` join at `tools/govkit/govkit.py:859-905` | **REUSE** — gov has the runnability oracle the reference playbook's own checker lacks (§8.5) |
| 5 | declared OUTPUT PATHS, refuse a diff outside them | `registry.toml`'s `[surface] globs` + both-directions assertion; gate-leg `guard` pathspecs | **EXTEND** the SHAPE; no code to import (§3, §8.3) |
| 6 | derive the template from a corpus, then freeze it human-curated | `.lexicon.conf`'s `ratified=` key + `adopt-lexicon.sh --scaffold`'s `PROPOSED` mark | **REUSE** the discipline verbatim (§4) |
| 7 | an improvement register that does not block the close | `park()` · `unattended.sh:1891-1893`, whose KIND is already an argument | **EXTEND** by one kind — a new register is waste (§7) |
| 8 | count produced pieces against a requested N | none — `reuse_lookup.py "count produced artifacts against a requested number"` returns no seam | **NEW** (§8.6) |
| 9 | gate a document against a required-section canon | hygiene check 12 · `tools/memory-tree/check-memory-hygiene.sh:662-925` | **REUSE** the whole shape, including its grandfathering (§2.2) |
| 10 | a generated index over N per-record files | `tools/memory-tree/gotchas.py` — front-matter contract, rendered `INDEX.md`, per-diff checklist | **REUSE** (§6) |

---

## 2 · Template machinery — what exists, and the one thing it cannot do

### 2.1 The mechanism runs five times already, and it is truth-blind

`memory/builds/aMouldedFolio/build/2026-08-11-build-TOOL-aMouldedFolio-1-doc-template-census.md:40-44`,
a 13-agent census with 92 confirmed and 17 refuted claims:

> This repo runs the template→render→byte-parity mechanism **five** times already (four claimed in
> `AGENTS.md`, plus `adopt-drift-audit.sh`, which the census initially missed and a skeptic caught).
> The mechanism works. It is also **green over documents that are false**, because it grades
> *sameness*, not *truth*.

Its Exhibit A is a shipped rule set stating a measured falsehood under a green gate
(`memory/HYGIENE.md:218` byte-identical to its template, both claiming "30 of 30 branches across
both gates are armed" while `ARMS_FLOORS` then named four gates). Exhibit B is a generator laundering
an authored error into a machine-verified artifact.

`:158-166` is the instrument table, and it is the most directly reusable page in the corpus:

| Shape | Catches | **Cannot catch** |
|---|---|---|
| Byte-parity (render then `diff`) | live copy edited away from template | a false sentence in **both** |
| Freshness (regenerate then compare) | artifact stale vs its source | a wrong **input** to the render |
| Ratchet (re-attest + watch-pathspec) | a watched input moved with no re-audit | anything unwatched |
| Shrink-only pin | omission; drains one at a time | falsehood *inside* what it counts |

**Consequence for this build.** The playbook-validity gate (fork 5) is a *shape* gate. It will
confirm that every step carries a tag and that every named leg exists. It cannot confirm that the
step is correct, that the leg is the RIGHT leg, or that following the playbook produces an acceptable
piece. `AGENTS.md` already requires a gate's own header to say what it does not check; this is the
sentence that header owes.

### 2.2 Hygiene check 12 is the required-sections gate, already built

`tools/memory-tree/check-memory-hygiene.sh:662-925` is a complete worked implementation of "a
document must conform to a template", and every part of it is a decision playbook mode will face:

- **Canon as EXACT EQUALITY of the `##` line sequence** (`:672-681`, `:872-879`). Two canons, nine and
  ten sections, selected by the file's own FILENAME date against `SPEC10_CUTOFF`.
- **Empty section bodies are rejected** (`:889-896`) — "an absent or hollow section is
  indistinguishable from a forgotten one" (`memory/TEMPLATE-SPEC.md`, writing rules).
- **Skeleton placeholders are rejected** (`:747`): any body line matching `<FAMILY-slug-seq>` or
  `YYYY-MM-DD`. The kickoff manifest records the trap this creates —
  `memory/guides/SESSION-KICKOFF.md:201-203`: quoting a stale artifact containing one of those shapes
  reds the spec.
- **Grandfathering is by FILENAME DATE and is TOTAL EXEMPTION, not relaxation.** Measured by the
  census (`:185-190`): a pre-cutoff spec is dropped from the selection entirely, and because the
  canon is exact equality, **a grandfathered file is FORBIDDEN to conform early** — 0 of 11
  grandfathered specs carry §10, while `streams`, whose rule is validated-when-present, drained
  voluntarily in 15 of 33. **If the playbook canon is a hard equality, no existing playbook can adopt
  it incrementally.** For a mode whose second verb is "updates and tweaks EXISTING playbooks", that
  is a design-changing property, and the soft shape is the one this corpus has measured draining.
- **Anti-vacuity is a first-class helper.** `pop_guard` (`:178-183`) compares the check's own
  segmented population against an UN-SEGMENTED precondition and reports a mis-segmented selector. Its
  known blind spot is recorded rather than hidden: `pop_guard` is blind to DATE vacuity, because it
  measures before the date filter (census `:196-198`).

### 2.3 The renderer, the placeholder classes, and the refusal posture

`tools/playbook/render_playbook.py:1-56` declares three placeholder classes — `derived` (a named
probe; a probe returning nothing REFUSES rather than defaulting), `asked` (from `deploy.toml`; absent
is a refusal NAMING the key), `defaulted` (and the render RECORDS that it defaulted). Both fence
namespaces refuse rather than skip, and `drop_blocks` is membership rather than truthiness because
govkit writes every answer as a quoted string, so a key "answered false" arrives as the truthy string
`false` (`:22-32`).

The declaration itself lives in `tools/govkit/entries/playbook.kit.toml:70-215` and carries the rule
this build must obey verbatim (`:74-76`):

> NO COUNT APPEARS HERE. `render_playbook.py` quantifies over what the template actually holds and
> refuses on a placeholder no row declares, so the population is derived on every run. Two revisions
> of the spec stated a figure and both were wrong when read.

**Two questions, not one.** `tools/playbook/README.md` and `TOOL-aUnmannedHelm-7` (the top recall hit
for the template question) both state it: region parity and placeholder completeness fail with
different messages, because a target whose descriptor declares nothing for a key renders a region
that is perfectly in sync and still tells the agent to invoke a placeholder's name as a tool. The
survival predicate is `tools/check-placeholders.sh --check <a> <b>` (`:31-43`), grepping
`\{\{[A-Z][A-Z0-9_]*\}\}`, and it is deliberately **fixture-only** in gov because the shipped
template legitimately carries placeholders forever (`:16-24`).

### 2.4 The census's own verdict on templating the playbook, re-tested

`aMouldedFolio` census `:293-299`, under "Explicitly NOT recommended": *"any templating of the
playbook template or its companions"* — because the file sat 148 bytes from a strict byte cap and "a
generated region inside a byte-capped file makes the cap non-deterministic".

**That objection is now half-retired and should be re-tested rather than inherited.** Measured today:
`tools/template-size-limits.txt` declares 49152 for the charter template and
`tools/template-size-highwater.txt` records 48163 — 989 bytes of headroom, not 148 — and the ceiling
moved once, on owner order. The *deterministic-cap* half still stands for any file carrying both a
byte cap and a generated region. **INFERENCE:** a PLAYBOOK TEMPLATE that is a new file with no byte
cap inherits neither half; the objection was about gov's charter, not about the class.

---

## 3 · Declared-population gates — govkit is the model for "a playbook declares its paths"

`tools/govkit/registry.toml:1-30` states the thesis fork 2 needs:

> EVERY tracked path in the asserted surface is an ENTRY, a member of exactly one entry's
> `[[files]]`, or an EXEMPT row with a non-empty reason. `selfcheck` asserts that in both directions
> and reds on an exemption whose path no longer exists.

And two paragraphs up: *"NO COUNT APPEARS IN THIS FILE OR IN THE SPEC. `selfcheck` derives every
population figure over the tracked surface. The spec stated two counts across its life and both were
true when measured and false when read."*

**Measured today**, `python tools/govkit/govkit.py selfcheck`:

```
govkit: legs: 88 in the manifest · 71 claimed · 17 exempt
govkit: surface 56 tracked path(s) · 25 entr(y|ies) · 16 exemption(s) · 0 unclaimed
```

The four properties worth porting, each with its enforcement site:

1. **A new moving part reds until a declaration claims it** — `govkit.py:901-903`: *"a new leg must
   red until a declaration says whether an adopter receives it"*.
2. **An exemption naming a dead path reds too** — `govkit.py:894-895`: *"a stale [exemption] silently
   widens the surface it was written to narrow"*.
3. **Both-and is a refusal** — `govkit.py:896-899`: a leg exempted AND claimed is an error, not a
   tolerated duplicate.
4. **The surface is DECLARED, not listed** — `registry.toml:33-41`'s `[surface] globs`, whose header
   explains why no directory listing equals the deployable set.

**The playbook analogue, and its one asymmetry.** A playbook declaring `output_paths`, plus a checker
asserting "every path this diff touched is under a declared output path or is one of the run's own
records", is the same predicate with the quantifier flipped. The asymmetry: govkit's surface is a
tracked-tree glob set, while a playbook-mode run's population is a DIFF. The nearest live precedent
for a diff-scoped pathspec population is the gate-leg `guard` field —
`tools/run-gates/run-gates.sh:659-672` evaluates guards serially and up front as a read-only
`git diff` per guarded leg, and `govkit.py:743-763` refuses a guard pathspec falling outside the
kit's own home. `AGENTS.md` records the companion rule: *"A guard naming an untracked path would skip
forever and silently, so the run-gates canary refuses one."* An output-path declaration naming a path
nothing produces has exactly that failure mode.

**One open row lands here.** `TOOL-aPacedTurnstile-12` (`memory/backlog/TOOL.md:128`): govkit joins a
descriptor's `[[gate_leg]]` rows to the manifest **by NAME only and never compares the declared
GUARDS**. Whatever fork 2 builds, it should not add a second declaration nothing joins.

---

## 4 · The lexicon kit — fork 4's precedent, and it is exact

Fork 4 rules that the PLAYBOOK TEMPLATE is corpus-derived plus external research, then frozen and
marked human-curated. `tools/lexicon/` already implements that sequence, and the reasoning is
recorded because the reasoning is the argument for curating.

`tools/lexicon/README.md:60-67`:

> `--scaffold` derives a verb table from your own corpus by leading-token frequency and marks it
> `PROPOSED`. **Curate it before ratifying.** A derived table is a mirror of the code, which is the
> one shape a naming gate must not have […] `--check` reds while `ratified` is empty, so an uncurated
> seed cannot reach the merge bar disguised as a vocabulary.

`memory/map/features/lexicon.md:59` states the same thing as a property: *"A prescriptive verb table
is the inverse and is safe — but `--scaffold` derives its proposal from the adopter's corpus, so for
one moment it IS the banned shape. The resolution is procedural: mark it `PROPOSED`, leave `ratified`
empty, and red until a human stamps it."*

`.lexicon.conf:92` is the frozen stamp: `ratified="2026-08-16 node d"`. And `:8-14` records the
derivation that justifies curating at all — 25 rows proposed, ten of which were not verbs (`t`, `do`,
`git`, `kit`, `signal`, `bounded`, `all`, `repo`, `is`, `no`).

**Three transferable rules, all measured:**

- **Coverage modes per language, and an undeclared one is a NAMED REFUSAL, never a silent skip.**
  `.lexicon.conf:22-24` declares `LANGS` with `parser` / `probe` / `dark`, and `sh` is dark on
  purpose. The playbook analogue is a step kind with no runnable gate: it must be a declared
  `CHECK <why>`, never an omission.
- **An unarmed predicate REDS.** `README.md:20-21`: *"P3 with an empty `LAYERS` reports `NOT ARMED`
  and **reds**. It never passes green over an absent declaration."*
- **Pins are MEASURED against the adopting corpus and never inherited** — *"a pin copied from a
  larger tree is either vacuous or permanently red"* (`README.md:69-70`), a class
  `memory/gotchas/pin-copied-from-another-corpus.md` owns.

**A caution the fork should absorb.**
`memory/builds/dClosedLexicon/reviews/2026-08-16-review-TOOL-dClosedLexicon-1-3.md:269` records that
the offender pin is a HAND re-measurement because the tool offers none, and `adopt-lexicon.sh:93-97`
refuses to re-scaffold over an existing conf. **A derive-then-freeze artifact with no re-derivation
mode is a one-way door.** Fork 4's template will need a re-derivation path for its second version, or
the freeze becomes a wall — and "updates and tweaks existing playbooks" is half the feature.

---

## 5 · Gate construction — how a leg is added here, and what it trips

### 5.1 The obligation set is FIVE, not six, and the sixth is retired

`aMouldedFolio` census `:303-305` priced a new gate leg at six obligations, one of which was an
`AGENTS.md` gate-suite bullet against a pin at tolerance 0. **That one is retired**, measured:
`tools/drift-audit/drift_signals.py:143-152` leaves `_charter_mentions_every_leg` defined and
unreferenced with `HANDKEPT: list[dict] = []`, noting *"RETIRED 2026-08-18 […] the charter's
gate-suite section is deleted against an admission test, so the charter stops CLAIMING to name every
leg."* `PINS["handkept_inventories_disagreeing_with_source"]` is `0` and drained.

The live, measured version is `memory/guides/SESSION-KICKOFF.md:206-209`:

> Adding ONE gate leg trips a SET of meta-gates that GROWS as new ones land — run the full bar, not
> this list. MEASURED 2026-08-18: map freshness, the kickoff ratchet, govkit selfcheck + selftest (a
> leg needs a `[[gate_leg]]` in its kit's `kit.toml`, else an `[[exempt_leg]]` row). The coverage
> assert and handkept signal did NOT fire; this line claimed both and neither govkit gate.

Adding to that, from source rather than from the manifest:

- **The leg name is a codebase-map INVENTORY KEY.** `tools/codebase-map/map_extractors.py:71-93`
  registers `gate-legs` as an inventory derived from `tools/gate-legs.json`, and a leg with no name
  raises rather than dropping a key. A new leg is a new key; an unclaimed key reds the map.
- **A new `*.sh` defining `fail()` joins `check-arms.py`'s DISCOVERED population** and needs an
  `ARMS_FLOORS` row. `.memory-tree.conf:178` declares seven gates today. `check-arms.py:38`: floors
  are per-gate deliberately, because an aggregate lets one gate's deleted guard be masked by
  another's added one.
- **A new `*.test.sh` on the bar must print an assertion count against a non-zero FLOOR and compare
  the two.** `tools/check-testsuite-counts.sh:50-63` derives its population from the manifest and
  asserts the emitting line is ANCHORED, that `FLOOR_ASSERTIONS=0` is not a floor, and that the
  script actually reads `$FLOOR_ASSERTIONS`.

### 5.2 The cheaper route, stated by the manifest itself

`SESSION-KICKOFF.md:250-253`:

> A new CHECK inside the hygiene gate is far cheaper than a new gate LEG: the codebase-map coverage
> assert and drift-audit's leg signal both key on `tools/gate-legs.json`, so neither moves. It still
> costs `ARMS_FLOORS`, an arm per `fail` call site (not per check number), and the leg's own name if
> that name states a count.

**Playbook mode has at least three new predicates** — playbook validity, output-path scope, piece
count. As numbered checks inside `tools/unattended/check-unattended.sh` they cost `ARMS_FLOORS` bumps
and no manifest rows; as three legs they cost three of everything in §5.1.

**One in-passing defect this route hits.** `check-unattended.sh:2` reads *"the merge-bar leg for the
unattended-run kit. TWENTY-ONE checks over the tree."* That is a count of a derived population
written in prose, in a gate header — the class `AGENTS.md` bans by name. Every new check either edits
that sentence or leaves it false. The clean move is to DRAIN the number rather than re-stamp it,
which is what `check-arms.py:23-25` did with its own overlap count.

### 5.3 The arms rules that will cost this build cycles

Four traps, each already paid for and recorded at `SESSION-KICKOFF.md:224-234`:

- an arm must contain the branch's ENTIRE literal signature, and a literal word between the sentence
  and the first interpolation is part of it;
- adding branches RENUMBERS per-check ordinals, invalidating `unarmed-branches.txt` rows below the
  insertion point;
- a bare positional in a `fail` message CANNOT be armed — bind it to a name and put it last;
- hygiene checks 13-19 are OFF unless a pin is armed, so a fixture tree written without pins arms
  nothing in that range.

And the rule the whole regime rests on, `AGENTS.md` §7: **a new gate is not landed until its failing
case has been observed** — stage the break, confirm RED, unstage.

---

## 6 · Content-shaped prior art — "render N things from one source"

`reuse_lookup.py "render N repeated artifacts from one declared source"` ranks
`render_playbook.render` (fan-in 5, SEAM) and the `map_lib.render_*` trio (fan-in 3 each) at the top.
The established shape, one sentence per instance:

- **`tools/memory-tree/gen_build_index.py`** — the canonical form. `:12-22`: *"THREE SOURCES, NOTHING
  ELSE"*, and *"a source the renderer does not read cannot make the render drift; a source the
  renderer WRITES must not also be read, or a wrong value defends itself forever."* It renders the
  build index, the LIVE index, per-month ledger shards, and the order / edges / docs regions from
  build front matter plus every spec status header. **It is the exemplar for a per-piece status table
  derived from the pieces themselves.**
- **`tools/memory-tree/gotchas.py`** — N per-record files with a front-matter contract, rendering one
  `INDEX.md` between `<!-- BEGIN GENERATED -->` markers, plus `--for-diff`, whose *"STDOUT IS THE
  CHECKLIST"* (`:13-16`). Its anchor derivation is declared recall-biased and over-selecting, and a
  record naming no path is **REPORTED as unanchored rather than silently never firing** (`:19-23`).
  This is the closest existing thing to a playbook REGISTRY, and its `--for-diff` shape is the
  closest existing thing to "hand the producer the steps their piece can actually hit".
- **`apply_region` / `region`** — the marker-splice primitive. It exists in at least four
  implementations (`gen_build_index.py`, `gotchas.py`'s dead twin, `unattended.sh:169-177`,
  `check-unattended.sh`), which the census flagged as measurably disagreeing in both directions
  (census `:288-292`), and `unattended.sh:164-168` records that a transposed marker pair once
  **deleted authored data**. Unifying them is `aMouldedFolio` step 5 and is still open. **Playbook
  mode must not add a fifth.**

**The generated/authored split is already this kit's idiom.** The run-state file carries a GENERATED
region asserted EMPTY (`check-unattended.sh:328-331`) precisely so the unit list is derived at read
time and lives in no second place. A per-run PIECES table should follow that: derived from the pieces
on disk, never copied into the run-state file.

---

## 7 · Park versus propose (fork 6) — the adversarial case, and what survives it

### 7.1 The fork's premise is not what the driver implements

Fork 6 says *"a park blocks the close; a proposal must not"*. **Measured: a park does not block the
close.** `unattended.sh:1878-1880`:

```
    parked-decisions-surfaced)
      grep -qE '^parked-surfaced: (yes|true)' "$rel" ;;
```

`parked-decisions-surfaced` is an AGENT-attested item (`DOD_CORE`, `unattended.sh:93`) written by
`verb_attest` (`:1911-1932`), and `verb_close`'s DoD loop (`:1650-1680`) blocks on the missing
ATTESTATION whether the run parked zero entries or nine. The count comparison that
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-5.md:145` describes — *"the
same grep, plus a close-verb refusal when the attested COUNT does not equal the DECISION-kind parked
[count]"* — **is not in the shipped driver**; the only decision-kind read is the duplicate guard at
`:1967-1975`. **INFERENCE:** either the spec item was descoped or it regressed. Either way, the
asymmetry fork 6 asks for already holds in the direction it wants, and the fork's stated
justification for a separate register does not hold up against source.

### 7.2 The strongest case that no new machinery is needed

`park()` has taken its KIND as an argument since `TOOL-cSettledDocket-1` S11
(`unattended.sh:1886-1893`):

```
park() { # file · kind · item · reason
  printf '\n%s %s · item %s · reason %s\n' "$(date -u …)" "$2" "$3" "$4" >> "$1"
}
```

Four kinds exist — `decision`, `abort`, `override`, `waiver`. Adding a fifth, `proposal`, costs: one
alternation in `verb_status`'s count regex (`:1566`), one verb wrapper modelled byte-for-byte on
`verb_park` (`:1934-1976`, whose refusals — no run-state file, no `--item`, no `--reason`, no
newline, no ` · ` inside the item, no bypass-flag spelling — are exactly the ones a proposal needs),
and one row in the protocol's §2 kind list. **Check 17 joins only the `waiver` kind**
(`check-unattended.sh:489-492`: *"the other three legitimately arrive late […] so joining them to the
first blob would red every honest run"*), so a fifth kind needs no gate work at all.

Surfacing is free: `memory/guides/BUILD-METHOD.md:224` derives the wrap-up's *open / parked* row from
*"every parked entry in the authored record (M6) with question, options and reason, plus any recorded
DoD override or directive waiver"*.

### 7.3 The strongest case that the BACKLOG is the register — and why it loses

The backlog is a real candidate and deserves to be named as the strongest alternative.
`memory/backlog/<FAMILY>.md` rows already have a machine grammar (`tools/memory-tree/row_grammar.py`),
a row-keyed merge driver (`merge-rows.py`), archive rotation, and 136 of 136 rows conforming with
zero migration cost (census `:214`). An improvement proposal is a backlog row in every respect but
one.

**It loses on the mid-run reachability argument, and that argument is recorded in source.**
`unattended.sh:1899-1901`:

> DECISION — the kind §2 names first […] — had no writer at all, so an agent that refused a decision
> at pass four had nowhere to put it that any gate reads. Hit during cBriefedPilot's own fold, where
> the workaround was a backlog row: **a different document, read by different people, at a later
> time.**

That is this fleet's own measured verdict on the backlog as a mid-run register, from the very build
that added `--park` because of it.

**Verdict: reject a separate register, accept a fifth `park()` kind.** The fork's ruling is satisfied
— distinct kind, distinct rows, distinct DoD treatment (none) — at roughly a tenth of the cost, with
no second file for the wrap-up derivation to read and no new document class for hygiene to gate.

**One genuine cost to price.** `TOOL-aBoundedVerdict-6` (`memory/backlog/TOOL.md:100`) is OPEN and
lands squarely here: *"the run-state authored region's 8 KB spill rule becomes load-bearing once
`--park` makes parking cheap: parks are rare hand-edits today, so the spill has never fired, and
crossing the cap mid-flight reds the bar and blocks `--close`."* A mode designed to emit proposals
across a run of N pieces makes that spill likely rather than hypothetical. **Whichever way fork 6 is
implemented, this row is a prerequisite, not a follow-up.**

---

## 8 · Fork by fork — what already exists, and what breaks

### 8.1 Fork 1 — a third `authorized-by:` member, and the fifth uncompared vocabulary

The closed set is spelled in FOUR places and **nothing joins them**:

| Carrier | Site | Bytes |
|---|---|---|
| driver `case` arm | `unattended.sh:795` | `prompt\|slug) ;;` |
| the refusal message | `unattended.sh:796` | *"outside the closed set of prompt and slug"* |
| the protocol | `memory/guides/UNATTENDED-PROTOCOL.md` §1 | *"over the closed set `prompt` / `slug`"* |
| the Skill | `tools/unattended/SKILL.template.md:127-186` | the whole prompt-path section |

Compare the treatment the kit gives its other vocabularies. `PHASES_CORE`, `DOD_CORE`,
`DIRECTIVES_CORE` and `PHASES_PASSKIND` are all read out of the driver by `core_of`
(`check-unattended.sh:63-82`) and joined BOTH WAYS to the protocol's tables (`:794-825`) — *including
the count sentence above the DoD table*, because (`:819-822`) *"the table grew to eight rows while
the sentence directly above it still said six, in BOTH copies, so the parity leg was green over a
document contradicting itself."*

**The mode set is the fifth vocabulary and the only uncompared one.** Adding a third member is the
moment to add the join, or playbook mode ships the exact drift shape four other joins exist to
prevent. This is a cheap, high-value unit and it is not in the fork list.

### 8.2 Fork 1 + 2 — the directive SCOPE cell is hard-closed at two values (BLOCKER-CLASS)

`tools/unattended/check-unattended.sh:709`, inside the arm joining the registry's scope field to the
Skill's table:

```
          if (cell == "all" || cell == "prompt") sc = cell
```

A directive declared `researched:M12:playbook` would produce `sc == ""` for its row, that row would
be dropped from `tblscope`, and the `corescope != tblscope` comparison at `:723` would red with a
message about *scopes disagreeing* — not about an unknown scope value. The refusal text at `:714`
also spells the closed pair: *"the cell it looks for holds exactly all or prompt"*.

The driver side has the same shape: `check_waiver_scope` (`unattended.sh:661`) tests
`[ "$sc" = prompt ]` literally, so a `playbook`-scoped directive would be **waivable by any run of
any mode** — the refusal simply would not fire.

**This is the single most concrete thing this lens found.** Fork 1's ruling is workable, but it is
not "one `case` arm": it requires the scope vocabulary to become derived like every other set in this
kit. **INFERENCE:** adding a third literal makes it three hardcodes instead of two and guarantees a
fourth.

### 8.3 Fork 2 — output paths, and where they must live

**The declaration cannot live in `.unattended.conf`.** `UNATTENDED-PROTOCOL.md` §1, cost 2, states
the rule: *"The key gates the DRIVER and cannot gate the leg: the conf is a working-tree file the run
can commit, so a leg reading it would be reading its subject's answer."* A playbook-mode run that can
edit its own output-path declaration has no output-path restriction. The declaration therefore
belongs in the PLAYBOOK, at the pinned BASE, where `check_authorization` already reads a blob it
cannot have written (`unattended.sh:763-770`, `GIT show "$base:$rel"`).

**The honest framing already exists and should be reused in spirit.** `check-unattended.sh:497-500`:

> HONEST LIMIT, in source rather than in a document read at a different time […] run locally this
> proves little, because the run writes BOTH sides […] What changes is that the same leg re-run in a
> clone the run never touched now has something to catch here. This is not an authorization verdict
> and does not claim to be.

That paragraph is the model for the stated CHECK fork 2 owes: a code change landing *inside* a
declared output path is invisible to the path gate, and the gate's header must say so.

### 8.4 Fork 3 — "pieces are PASSES" collides with a closed, machine-joined set

`memory/guides/BUILD-METHOD.md:133-134`:

> **A PASS is exactly one of:** a spec authored · a spec reviewed · a review's fixes folded in · a
> unit built · the closing diff review. **Nothing else is a pass.**

That set is not just prose. `unattended.sh:100` publishes the phase subset named for it —
`PHASES_PASSKIND="SPECCING REVIEWING FOLDING BUILDING"` — with the comment *"published so the
protocol's claim about it can be JOINED rather than believed"*, and `check-unattended.sh:794-803`
joins it to the protocol in both directions AND asserts every pass-kind phase is in the core
vocabulary.

M12 faced exactly this and chose the other answer (`BUILD-METHOD.md:261-264`): *"**This adds no PASS
kind.** M6's set is closed and neither research nor testing is in it. The work happens INSIDE the
passes that set does name […] and under a mandate the run occupies the `RESEARCHING` and `TESTING`
positions while doing it."*

**Three routes, and only one is cheap:**

1. A piece is *"a unit built"* and its phase is `BUILDING` — M12's precedent exactly, no method edit,
   no vocabulary edit. **INFERENCE: this is what fork 3 means, loosely worded, and it is the route
   the existing contract admits.**
2. A new phase (e.g. `PRODUCING`) in `PHASES_CORE`, joined to the protocol, `CORE_FLOOR` raised
   12:8 → 13:8. Cheap mechanically — but if it is *also* published as a pass kind, it edits M6.
3. Editing M6's closed set. **This is an OWNER TURN by M3 veto 2** — *"a change to a governance
   carrier"* (`BUILD-METHOD.md:73-76`).

**A correction to the build README's constraint claim.** It is accurate about the numbers and
imprecise about the enforcement: measured, `memory/guides/BUILD-METHOD.md` is 20,567 B / 283 lines,
and its stated *"Budget: ≤22 KB, ≤290 lines"* (`:8`) is a LOCAL, SELF-STATED constraint. The hygiene
gate's guide class is 61,440 B / 750 lines (`check-memory-hygiene.sh:42`), so **nothing machine-checks
the 22 KB.** It binds through M3 veto 2 and the owner, not through a leg — which makes it more
binding, not less, but for a different reason than "the gate will stop you".

### 8.5 Fork 5 — "every named leg is runnable" is stronger than the reference achieves

**Out-of-repo evidence, read at the terminal.** The reference playbook's own I21 invariant
(`C:/projects/nicocares/main/scripts/check_content_plan.py:2408-2500`) is the closest existing
implementation of fork 5, and it is worth knowing exactly how far it gets:

- the step selector is `^\*\*([A-Z]\d+(?:\.\d+)?)\.` and was widened from `[A-D]` after a review found
  `## Checklist E` structurally invisible — *"`[A-Z]` gates the class rather than today's instance"*;
- the tag window **stops at the next step or heading**, after a fixed lookahead let `D4` borrow
  `D5`'s tag — *"caught by staging the break"*;
- a bare `GATE` naming nothing is a finding, via `LEG_RE` (`:402-406`) — but `LEG_RE` is a
  **project-specific SHAPE regex** (`I\d+|C\d+[a-z]?|check_[a-z_]+\.py|check-[a-z-]+\.sh|…`). Only
  the `I\d+` half is genuinely joined, against ids harvested from the checker's own source
  (`:2474-2489`), and that harvest carries its own anti-vacuity floor (`len(known_ids) < 15`);
- the compound-tag bug is recorded: the lazy non-overlapping form checked only the FIRST id, so
  `GATE check_content_plan.py I2/I99` exited green while `… I99` alone red;
- the selector has an anti-vacuity floor: `steps < 50` reds as I20;
- duplicate step ids are a finding, because *"a duplicate id merges two passes into one wherever a
  record joins on it"*;
- and a prose count is machine-compared: `REQUIRED_FIELDS is <n>` against `len(REQUIRED_FIELDS)`.

**Measured over the reference playbook** (1290 lines): 86 `GATE ` occurrences, 95 `CHECK`
occurrences, 103 lines matching the bold-step shape, 35 distinct `GATE <leg>` strings. These differ
from this build's README (92 / 95 / 110) because the selectors differ, and neither set is the
checker's own. **Whichever number the spec set uses must be DERIVED by a program, not typed** — the
disagreement between two hand-selectors over one file is itself the argument.

**The gov-shaped answer fork 5 can actually have.** `tools/gate-legs.json` is a declared leg manifest
with 88 named legs, and govkit already joins descriptor-declared legs to it by name in both
directions (`govkit.py:859-905`). So "every named leg is runnable" degrades cleanly:

- adopter HAS a leg manifest → the predicate is set membership, and it is real;
- adopter has NO leg manifest → the predicate must be a **declared coverage mode** in the lexicon's
  sense, or a **named refusal**. A shape regex that quietly matches anything is precisely what
  `tools/lexicon/README.md:24-27` refuses on behalf of shell.

### 8.6 Fork 3 + 5 — the piece-count DoD item

Nothing in this tree counts produced artifacts against a requested number:
`reuse_lookup.py "count produced artifacts against a requested number"` returns only
`json_artifact_inventory`, `check_entry_producer` and `scan_produced_destinations`, none of which
compares against a requested N. **This is the build's one genuine "no existing seam fits".**

`build-complete` (`unattended.sh:1746-1800`) is the model to copy: FIVE terms, evaluated SEQUENTIALLY
so each can say which one failed, after `TOOL-aBoundedVerdict-12` S3 found all four printing the same
sentence and `--override build-complete` becoming the natural next move for a reader who could not
tell a missing spec from an unfinished unit. Its first term names the missing marker pair BY NAME and
prints the repair command.

**Cost, measured:** `DOD_CORE` holds 8 members; `.unattended.conf` declares `CORE_FLOOR="12:8"`; the
floor is shrink-only, so adding an item is free at the floor. But the protocol's §4 table AND the
count sentence above it are both joined (`check-unattended.sh:810-825`), so both move in the same
commit. For reference: `PHASES_CORE` holds 12, `DIRECTIVES_CORE` holds 13 against
`DIRECTIVES_FLOOR="13"`.

### 8.7 Fork 7 — producer agnosticism has a precedent to copy

`tools/memory-tree/check-method-carriers.sh` is the shape: *"every file that POINTS AT the build
method is declared, and points rather than copies"* (`:1-2`), with the honest limit in its own header
(`:11-14`) — *"It does not read prose and judge whether a file restates M3 […] A fluent paraphrase
that invents its own headings passes here."* Its motivating history is exactly playbook mode's risk
(`:7-9`): *"this repo grew FOUR spellings of its unattended rules […] one well-meaning summary at a
time, none of them wrong on the day it was written."*

If the kit stays agnostic, this is the gate that keeps it agnostic: a playbook is a carrier, and a
carrier that starts restating kit rules is the drift. Its registry lives per-repo under
`<MEMORY_ROOT>/project/` and the kit ships none, *"because gov's rows would otherwise travel to an
adopter whose tree does not contain those paths, and every adopter would red on install"* (`:16-19`)
— the same reason a playbook registry must be adopter-authored.

---

## 9 · The decision records that BIND this work

Retrieved with the term sets in §0. Ids, and what each constrains here:

| Record | What it binds |
|---|---|
| id `TOOL-aPromptedMandate-1` | the `authorized-by:` key, the closed mode set, mode as EVIDENCE never an input |
| id `TOOL-aPromptedMandate-2` | `PHASES_PASSKIND` published so the protocol's claim can be JOINED; `CORE_FLOOR` 10:8 → 12:8 |
| id `TOOL-aPromptedMandate-4` | the three-field directive entry `<handle>:<section>[:<scope>]`; scope is KIT-owned, never a project knob |
| id `TOOL-cSettledDocket-1` | `--park` as a verb, `park()`'s kind argument, and why a backlog row failed as the mid-run register |
| id `TOOL-aBoundedVerdict-5` | parking as a verb; the parked-kind taxonomy so review rounds cannot inflate the surfaced count |
| id `TOOL-aBoundedVerdict-6` | **OPEN** — the run-state 8 KB spill becomes load-bearing once parking is cheap |
| id `TOOL-aBoundedVerdict-11` / `-12` | the generated units region as the frozen scope; sequential DoD messages |
| id `TOOL-aMouldedFolio-1` | the doc-template census: four enforcement shapes, parity is truth-blind, "do not template the playbook" |
| id `TOOL-aUnmannedHelm-7` | template parity and placeholder completeness are two questions about one render |
| id `TOOL-dClosedLexicon-1` | derive-then-freeze, `ratified` reds while empty, coverage modes, unarmed-predicate-reds |
| id `TOOL-aSealedCaravan-1` / `DEPL-aSealedCaravan-2` | registry + descriptor, the both-directions surface assertion, never a count in prose |
| id `TOOL-aTetheredConvoy-1` | **OPEN** — the playbook template reached `origin/main` with unresolved conflict markers and both gates over it passed |
| id `TOOL-aDeclaredCeiling-1` | **OPEN** — make a template ceiling a DECLARED pin, not a shell constant |
| id `TOOL-aPacedTurnstile-12` | **OPEN** — govkit joins `[[gate_leg]]` to the manifest by NAME only and never compares declared GUARDS |
| id `TOOL-aBranchedMandate-5` | **OPEN** — `adopt-drift-audit.sh` diffs its render with no `[ -s ]` test, so empty-vs-empty PASSES |

`TOOL-aTetheredConvoy-1` deserves a second look from this build specifically: it is the recorded
proof that **both existing gates over a playbook-shaped product document are blind to conflict
markers**. A PLAYBOOK TEMPLATE is the same class of artifact, and `TOOL-aBranchedMandate-5` is the
matching proof that an adopter check can pass by comparing nothing to nothing.

---

## 10 · Budget and gate facts this build must not trip

- **Read-path budget, live:** `python tools/memory-tree/corpus_ids.py --measure` reports 106,288 B
  measured against `READ_PATH_CEILING="112987"` (`.memory-tree.conf:113`) — **6,699 B of margin**.
  The population is files the CHARTER cites under `memory/` (`corpus_ids.py:336-360`), derived
  through three token arms, so *this record does not count* unless `AGENTS.md` cites it. A new
  `memory/guides/` document that the charter points at DOES.
- **The template ceiling** is 49,152 with 48,163 recorded — 989 B free — and the high-water ratchet
  prices every growth (`tools/template-size-limits.txt`, `tools/template-size-highwater.txt`).
  `AGENTS.md` is capped at 64,512 with 60,930 recorded.
- **`RECORD_UNBOUND_PIN="9"`** (`.memory-tree.conf:215`) bounds records carrying `**Serves:** none`.
- **Line length**: only `AGENTS.md` and the charter template carry rows in
  `tools/line-length-limits.txt` (450 each); everything else takes the 450 default.
- **This record's own binding reds check 21 today, MEASURED rather than predicted.** The mandated
  first line `**Serves:** TOOL-dScriptedRepeat-1` omits the closed `<kind>` token the grammar at
  `memory/HYGIENE.md:249` requires. Run
  `python tools/memory-tree/gen_build_index.py --print-bindings` after staging:

  ```
  A  …-in-repo-prior-art.md  first token TOOL-dScriptedRepeat-1 is not one of
     spec-audit diff-review journal research, and the line is not the none form
  ```

  That is branch **A** of check 21 (`check-memory-hygiene.sh:607-609`, *"records […] whose head
  carries no conformant Serves line"*), not branch B as one might expect — **the parser rejects the
  missing kind before it ever tries to resolve the id**, so the "no spec defines this id yet" problem
  is masked and will surface only once the kind is added. Both lens records in this build's `build/`
  folder carry the same defect, so it is systematic to the brief rather than to one agent. **The fix
  is one word per record — `**Serves:** research TOOL-dScriptedRepeat-1` — and it should be applied
  when the record set is folded, together with the spec that DEFINES the id.**

---

## 11 · What this lens did NOT check

Stated so a green reading of this record is not mistaken for coverage:

- **No gate was written or run against a candidate predicate.** Nothing here has been staged-broken
  and observed RED, which is the standard `AGENTS.md` §7 sets for a gate.
- **The full bar was not run.** Only `govkit selfcheck`, `corpus_ids.py --measure`, `reuse_lookup.py`
  and `query.py` were executed.
- **No adopter tree was inspected.** Every claim about what an adopter receives is read from
  descriptors and exemption rows, not observed in an install.
- **The external half of fork 4** — checklist and instruction-design literature — is another lens's
  job and nothing here substitutes for it.
- **The reference playbooks were read, not audited.** The counts in §8.5 are my selectors over their
  bytes; the authoritative population is whatever the spec's own checker derives.
- **`memory/map/features/*.md` prose is ungated** — `memory/map/features/unattended.md:119-122` says
  so about itself: *"Dossier prose is ungated — only the claims tables above are — so this section
  rots silently."* Where dossier prose is cited above, the claim was re-derived from source.
