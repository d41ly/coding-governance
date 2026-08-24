# dScaffoldedMirror spec set — synthesis review

**Serves:** spec-audit TOOL-dScaffoldedMirror-2
**Commissions:** TOOL-dScaffoldedMirror-2

Fourteen specs (`-2` through `-15`), two convergence passes, four refutation lenses, one synthesis.
Spec dir: `memory/builds/dScaffoldedMirror/spec/`. Tree read at `af4de2d5` (899 tracked files);
every spec header declares `base 9ddcc5c9` (896 tracked files).

Everything below marked **[verified here]** was re-executed by this pass against the tree, not
inherited from a lens report. Where two lenses disagreed I picked a side and say why.

---

## 1. CONVERGENCE VERDICT

### CONVERGES WITH FIXES — mechanically, on 14 of 14. The plan does not converge with its own diagnosis.

The two convergence agents agreed (C1: "converges with fixes"; C2: "converges with fixes") and I
concur on the narrow question they were asked. These are one build: the mandatory spec mechanics are
clean in all fourteen (filenames, H1s, byte-exact status headers, all ten sections in order, all ten
§5 rows, zero AC bullets missing a backticked witness, at least one conforming `RESOLVED` mark per
§8, no fabricated §10 seam), M3 vocabulary is uniform with no invented synonyms, M4 holds — not one
spec re-opens a WHAT-NOT-TO-BUILD decision except as a quoted refusal — and the single highest-risk
shared mechanism, the `-19` structural exemption, is specced **once**, in `-11`, rather than three
times. That is a better result than a fourteen-way parallel authoring pass usually produces.

What stops it converging outright is not prose quality. It is **nine mechanisms handed between
units under two definitions**, and **five units whose central mechanism does not work as specced**
— verified against the code, not argued. `-5`'s repair returns the value it exists to compare
against. `-3` reads a receipt file that exists in neither repo on Earth. `-2`'s only legal escape
from its own landing-day red needs a conf grammar `-2` says it does not add. `-15` ships a leg whose
script, registry and subject are all declared un-shippable. `-9` seeds gov's 459-row debt file into
every adopter and deletes the declaration that would have explained the resulting red.

And one level up, the answer is different. **The plan is over-built by roughly half, and the
over-built half is the half the research pass told you not to build.** I answer that head-on in §5
and I do not soften it.

### Where the convergence agents disagreed with the refutation lenses, and who wins

| question | C1 / C2 said | R-lens said | **verdict** |
|---|---|---|---|
| does `-6`'s floor red an incms adoption? | yes, 15.7 points under (C1 #2, C2 #2) | no — 48.8% under `-6`'s own denominator (R2 A4) | **R2.** [verified here] incms is 3,401 md of 6,171 tracked; markdown does not enter a definition-carrying denominator. C1/C2 both compared 19.3% (tracked-file denominator) against a floor `-6` §4 explicitly defines over definition-carrying files. Wrong denominator, twice. Severity drops HIGH → MEDIUM and becomes bookkeeping. |
| `-7`'s pin move 463 → 464 | a sequencing collision to be ordered (C1 #3, C2 #9, R3 #4) | the premise is false; two `SIGNALS` entries already lead with `build` (R1 F3) | **R1.** [verified here] `drift_report.py:1038-1041` ends `build_live_backlog_rows, build_readme_mechanism_drift`. `build` is row 1 of the table. `-7` should rename, not raise. This dissolves a three-way collision into a two-way. |
| `-5` lands clean | "REFUTED as a hazard — all eleven rows resolve at HEAD" (R3) | the S3 repair is a no-op (R1 F1) | **R1**, and R3 answered a different question. [verified here] against `drift_report.py:198-221` and `-5` §4:100-102. R3 checked whether `-5` reds; R1 checked whether it works. It does not. |
| `-15`'s defect | missing subject-pin row, one command (R2 L5) | S3's adopter direction is structurally impossible (R1 F2) | **R1.** [verified here] `registry.toml:219` exempts `tools/govkit` as "never installed into a target"; `check_runbook_parity.py:32-39` hardcodes `ROOT` off its own location and reads that same registry. |
| is the plan right-sized? | not asked | over-built by ~half (R4) | **R4, substantially.** See §5. I depart from R4 on three units and say where. |

---

## 2. BLOCKING DEFECTS

Ordered by blocking-ness: B1 stops the specs being committed at all; B2–B6 are units whose central
mechanism does not work as written; B7–B10 are landing-day reds and machine-checked wrong literals.

### B1 — the spec set cannot be committed. The memory-hygiene gate reds on staging. [reproduced twice, independently]

**Spec:** none — this is a generator defect the spec set triggers.
**Where:** `tools/memory-tree/gen_build_index.py:673` and `:678`.

Staged in a throwaway clone, `python tools/memory-tree/gen_build_index.py --write` regenerates
`memory/builds/dScaffoldedMirror/README.md` with lines at **352** and **399** characters against
`BUILD_README_ENTRY_CAP_CHARS=350` [verified here at `check-memory-hygiene.sh:54`]. Check 9 fires
first (build-index DRIFT), then check 7 on the regenerated file. `EXIT=1`. Both C1 and R2 B1
reproduced this in separate clones.

Both offending lines are **generated, not authored**: `Ids no record names: <join>` at `:673` and
the `spec-audit` sentence at `:678`. Each joins every unrecorded id into one unwrapped line. Going
from one unit to fourteen is the first time this build's roster overflows. [verified here] the
current README already carries a 196-char entry line with a single id; thirteen more ids at 25 bytes
each overflows by construction.

**Exact fix:** apply `_wrap_ids()` — which already exists at `gen_build_index.py:686` with
`IDS_WRAP = 300`, and which the generator already uses for the `ids …` roster lines — to the two
sentences at `:673` and `:678`. **Do not raise the cap and do not edit a spec.** This is a generator
gap the spec set merely exposed, and it blocks the landing regardless of ownership.

### B2 — `-5`'s repair returns `now` as `was`. The unit's whole product is a no-op, and its acceptance criterion tests a different code path. [verified here]

**Spec:** `-5` §2 S3–S4, §4:100-107, §6 AC2 and AC5. **Severity: BLOCKING.**

`-5` §4 publishes the derivation verbatim at lines 100-102: on `was is None and now is not None`,
walk `git rev-list <base>..HEAD -- <file>` newest-first and take the first `_scalar_at` hit.

Run against the real caller [verified here, `drift_report.py:198-221`]: `was` comes from
`git show <base_ref>:<path>`, and the guard is `if now is None or was is None or now == was: continue`.
So **the S3 branch fires only when the key is absent at the base** — i.e. the deletion happened at or
before `base_ref`, outside the window. The pre-deletion value therefore does not exist anywhere in
`base..HEAD` and no walk of that range can recover it. What the walk *does* find, newest-first, is
the commit that re-added the key — inside the window, carrying the new value. So `was = now`, the
caller's `now == was` guard continues, and the run is silent. **The repair returns the value it was
written to compare against.**

Two consequences, both defects:

- **S4 is unreachable.** Its "nothing found" branch needs no commit in the window to carry the key,
  while `now is not None` needs HEAD to carry it, and any commit that introduced it is in the window.
  AC5 stages a state the algorithm cannot produce.
- **AC2 does not test S3 at all.** Its scenario (base holds `SUFFIX_OFFENDER_PIN="0"`, HEAD holds
  `"900"`) gives `was=0`, `now=900`, `weakens: "up"`, unjustified → a finding, through code that
  exists today. S1's three `RATCHETS` rows alone satisfy AC2. The arm that would expose S3 tests S1.

**Exact fix:** derive from the file's **full** history, not `base..HEAD` — walk newest-first past the
contiguous present-run ending at HEAD and take the value at the newest commit where the key was
present before it vanished, which is outside the window by construction. Restage AC2 with the
deletion commit **before** the base, the only shape that reaches the branch. If §5's cut is applied
and `-5`'s three `RATCHETS` rows go, this repair still needs fixing before it is re-filed — it
covers eight existing rows belonging to two other kits.

### B3 — `-3` specs a reader for `.governance/install.json`, a file that exists in neither gov nor incms, and then refuses `--scaffold` without it. [verified here]

**Spec:** `-3` §2 S1/S5, §4 (receipt reading), §8 F2. **Severity: BLOCKING for the unit; see §5, I recommend cutting it.**

[verified here] `git ls-files .governance/` in gov returns **`deploy.toml` and nothing else**.
`ls C:/projects/incms/main/.governance/` returns **`install.index`, `kits.json`, `row-count.txt`** —
**no `install.json`**. R2 A5 established that `-3` §4's adopter measurement (92 rows, 60 `engine` +
16 `diverged` = 76, 13 `project-owned`, 3 `seed`) reproduces exactly — **from `install.index`**,
which `-3` F2 explicitly refuses to read. The spec measured the receipt it declines to support, then
specced a reader for a spelling that exists nowhere.

Consequences, each measured rather than argued. `bash tools/lexicon/adopt-lexicon.sh --scaffold`
exits 1 on **gov and on incms** under S5, so the kit's adoption verb becomes inoperable on 100% of
live repos — in a build commissioned because nobody adopts the kit. The 25% cap, the stale-row
refusal and the malformed-receipt refusal are exercised only by fixtures: a selector with a provably
empty population everywhere, in the kit that ships `UNSELECTIVE LAYERS RULE` and cites
`vacuous-selector-empty-population.md`.

**Exact fix if `-3` survives:** read both spellings behind one role-normalising adapter, and drop
S5's `--scaffold` refusal until a receipt exists to refuse against. **Recommended: cut `-3`** (§5).

### B4 — `-2` AC2's escape hatch needs a conf grammar `-2` §4 says it does not add, and the only cheap alternative is a 45-offender absorbing move with a green bar. [verified here]

**Spec:** `-2` §2 S2, §4 (Files touched), §6 AC2. **Severity: BLOCKING.**

[verified here] 10 tracked `.js` files, **zero** carrying a class definition. `.js` is declared
`js-regex:probe` and is present in the corpus, so `(.js, P2)` has an empty population and S2's new
`DEAD PREDICATE` refusal reds on the landing commit. A real failing case needing no staging — which
is the spec's strength. The problem is the discharge. `lexicon_conf.py:120-132` enforces a strict
three-part `<ext>:<pattern-set-id>:<mode>` triple with `mode ∈ {parser,probe,dark}`; there is **no
spelling for a pair-level dark declaration**, and `-2` §4 states "No conf grammar change, so
`lexicon_conf.py` and `subtokens.py` are untouched." AC2 is unsatisfiable as written.

R2 measured the three real routes. Widening the grammar contradicts §4. Shipping a JS `class` fixture
means adding a class to hook and workflow scripts to satisfy a gate. Declaring `.js` dark measures at
**pin 463 → 418, `lexicon OK`, exit 0** — a 45-offender absorbing move with a green bar, in the build
commissioned because absorbing moves were invisible. Dropping `js` from `LANGS` is not available:
`UNDECLARED EXTENSIONS: js`, exit 1.

**Exact fix:** `-2` takes the `LANGS` pair-level grammar widening into its own scope and deletes the
"no conf grammar change" sentence, **and** `-6`'s mode ratchet (S5) lands with or before `-2` S2 so
the cheap escape is visible if anyone takes it. Both halves, not one. This same gap strands `-11`'s
P6 (B10).

### B5 — `-9` seeds gov's 459-row grandfather file into every adopter, and deletes the declaration hole that explained the resulting red. [verified here]

**Spec:** `-9` §2 S2/S5, §4 Migration. **Severity: BLOCKING for adoptability.**

[verified here] `tools/lexicon/kit.toml:16-18` is `[[files]] include = "**"` / `role = "engine"`, so
every new file in the kit deploys. `-9` S2 makes `lexicon-grandfathered.txt` `role = "seed"`, and
`govkit.py:2461` writes a seed's bytes on first apply, skipping only if the destination exists. The
three existing waiver registries dodge this by being **empty in gov** — `kit.toml:25-28` says so and
cites the pin-copied-from-a-larger-tree class. `-9`'s file **cannot be empty in gov**, because gov's
own 459 rows are its whole point.

A fresh adopter therefore receives 459 rows naming gov paths against a `.lexicon.conf` the scaffold
just wrote. Assert E (the sha resolves) fires → `DEAD PROBE` → red; if a `FREEZE_SHA` is present it
is gov's, unresolvable in the adopter's object store → same red; assert B independently reds all 459
because none is an offender there. And S5 **deletes the `lexicon-pins` hole from `kit.toml` and
declares no replacement** — that hole was the declaration telling an adopter why their first gate run
reds and how to discharge it. After `-9`, the equivalent red has no hole behind it at all.

**Exact fix:** the shipped seed must be empty; gov's set lives at a path the `**` rule does not deploy
(an explicit later `[[files]]` row, matching the waiver-registry precedent); a `lexicon-freeze` hole
replaces `lexicon-pins`. None of the three is in scope today.

### B6 — `-15` S3 ships a leg whose script, registry and subject are all declared un-shippable, and AC6 observes gov to certify a target. [verified here]

**Spec:** `-15` §2 S3, §6 AC6. **Severity: BLOCKING for S3; S1/S2/S4 are sound.**

[verified here] `check_runbook_parity.py:32-39` sets `HERE = pathlib.Path(__file__).resolve().parent`,
`ROOT = HERE.parents[1]`, `RUNBOOK = ROOT / "WIRE-INTO-PROJECT.md"`, and `main()` reads
`ROOT/"tools"/"govkit"/"registry.toml"`. And `registry.toml:218-220` carries
`[[exempt]] path = "tools/govkit"` with the reason *"the deployer itself. It runs on the deployer
machine and is never installed into a target, so it is an entry of nothing."*

So S3's "declare the leg in the govkit descriptor so an ADOPTER receives it" produces, in every
adopter tree, a leg whose argv names an absent script — and if it somehow ran, an unguarded
`.read_text()` on an absent registry (traceback) or `RUNBOOK.is_file()` → `return 1`. `-15` F2
refuses "a guard that never matches would skip forever and silently" for gov, then ships exactly that
shape outward. **AC6** is the automatic finding the brief names: a green `govkit.py selfcheck` on gov
is evidence about gov and cannot observe a target at all.

**Exact fix:** drop S3 and AC6; the leg stays gov-only and §1's adopter argument goes with it. A
target-side runbook-parity gate is a different gate over a different population and a different unit.

### B7 — `-9` deletes three pin keys; after `-11` there are four, and `-11` says so while `-9` does not.

**Spec:** `-9` H1, §2 S5, §3, §4:148, §6 AC9. **Severity: BLOCKING (its own AC catches it at build time).**

`-11` F3 states the obligation verbatim: *"the edge is NEW and `-9` must delete four keys, not
three."* `-9` says three in three places and never mentions `SHORTNAME_OFFENDER_PIN`. An M2 violation
on the one edge both specs already declare blocking (`-9` §3: *"`-11` lands first, and this is not a
preference"*). `-9`'s AC9 (`grep -rn "OFFENDER_PIN"` returns nothing) catches the fourth key at build
time, against a migration written for a three-key list.

**Exact fix:** `-9` §3, S5 and §4 Migration all say four, conditional on `-11` landing. H1 stays —
the title is about the three that exist today.

### B8 — `-10` reds three gate legs its own §7 lists as green, and adds two unclaimed map inventory keys. [R2 staged each in isolation]

**Spec:** `-10` §4 Files touched, §7. **Severity: BLOCKING for the landing commit.**

R2 staged each independently:

- `gate-legs.json += "lexicon skill wiring"` → `FAIL test_every_inventory_key_is_claimed_or_baselined`,
  `UNCLAIMED {'gate-legs': ['lexicon skill wiring']}`, plus `FAIL test_generated_artifacts_are_fresh`,
  plus `govkit selfcheck rc=1: "gate leg 'lexicon skill wiring' has no row in
  tools/govkit/subject-pins.tsv — a NEW leg reds until its subject is on the record"`.
- `.claude/skills/lexicon/SKILL.md` → `UNCLAIMED {'rendered-skills': ['lexicon']}`.

`-10` §7 names `govkit selfcheck` as green and omits `codebase-map coverage + freshness` entirely;
its thirteen-path Files-touched list has no map dossier and no `subject-pins.tsv`. `-15` S4 does this
correctly and is the only spec in the set that does.

**Exact fix:** `-10` claims both keys in the lexicon dossier in the same commit, adds the
`subject-pins.tsv` row, adds `gen_map.py --write` and `govkit.py selfcheck --write` to its rollout,
and names `codebase-map coverage + freshness` in §7.

### B9 — `-10` AC9 asserts byte literals wrong by two, in the one unit whose entire argument is arithmetic. [verified here, to the byte]

**Spec:** `-10` §4:151/168, §6 AC9. **Severity: BLOCKING (a machine-checked AC that fails on a correct build).**

| | `-10` says | **measured here** |
|---|---|---|
| §12 bullet bytes | 391 · 344 · 237 · 396 · **358** | 391 · 344 · 237 · 396 · **357** |
| third bullet | table says 237, arithmetic uses **236** | **237** |
| published replacement | **201** | **204** (two lines, 100 and 102 columns) |
| delta | **−35** | **−33** |
| `AGENTS.md` after | **64,359** of 64,512 | **64,361** of 64,512 (151 free) |
| template after | **48,792** of 49,152 | **48,794** of 49,152 (358 free) |

`AGENTS.md` today is 64,394 and the template 48,827 [verified here]. **M6 holds** — net-negative, 151
bytes free after. But AC9 is machine-checked against a wrong literal, and the builder's reflex on
failure will be to edit the AC — precisely the wrong reflex to train in the unit whose purpose is
deleting a number stated in prose beside the source that owns it.

**Exact fix:** AC9 asserts **64,361** and **48,794**; §4's bullet table says 357 and its arithmetic
uses 237. (The replacement's second line is 102 columns; [verified here] `tools/line-length-limits.txt`
grades both charter subjects at the 450 default, so no gate reds — it breaks only the spec set's own
100-column house style, inside a fenced block.)

### B10 — `-11`'s P6 lands a Python-only predicate into `-2`'s liveness law and answers the refusal with a comment. [verified here]

**Spec:** `-11` §3, §5; interacts with `-2` S2. **Severity: BLOCKING, one phase after B4.**

[verified here] zero `.js` classes; `.js` declared `probe` and present. `-11` §3 states P6 grades
Python only, "in the gate header rather than left for a reader to discover". `-2`'s mechanism reads a
declaration, not a header. `(.js, P6)` is a `DEAD PREDICATE` red on `-11`'s landing commit, and by
Phase 3 the `.js`-dark escape costs 45 offenders already in the grandfather set.

**Exact fix:** B4's grammar widening, applied to P6 — or P6 registers outside `-2`'s roll-up with its
liveness stated another way. Same decision, one owner.
---

## 3. CONFIRMED FINDINGS

Non-blocking findings that survive, grouped by spec. Anything a lens raised and another refuted is
**dropped** unless I re-establish it and say so; the drop list is at the end of this section.
Severity: **HIGH** = wrong on landing or wrong in a way a later reader will act on;
**MED** = a defect a builder will hit; **LOW** = craft.

### `-2` (per-predicate reporting and the liveness law)

- **HIGH — S4's four-condition inventory names one condition the path cannot reach and omits three it
  can.** [verified here] `problems.append` fires at `lexicon.py:416` (UNDECLARED EXTENSIONS), `:422`
  (P3 NOT ARMED), `:429` (UNSELECTIVE LAYERS RULE), `:445` (pattern set not shipped), `:450`
  (declared-parser file does not parse), `:491` (DEAD PROBE) — and `:528` (STALE WAIVERS) plus `:535`
  (non-integer pin), both **after** `if measure_mode:` returns at `:503`. So STALE WAIVERS has never
  ridden in `--measure`, and three conditions that do reach it are missing from S4's list. A hand-typed
  enumeration of a derived population, in the spec whose §7 rule forbids exactly that.
  **Fix:** S4 says "every member of `problems` at the point of return" and names none of them.
- **MED — AC6 cites a gate that cannot observe the change.** [verified here] `adopt-lexicon.sh` never
  invokes `lexicon.py`: it shells to `lexicon_conf.py --print-verbs` at `:83` and `:99` and to
  `scaffold_lexicon.py` at `:115`. `-2` changes `lexicon.py` reporting and exit codes exclusively.
  AC6 cannot fail. **Fix:** delete AC6; §7's `lexicon wiring` mention inherits the same emptiness and
  should be dropped from the keeps-green claim or justified.
- **LOW — §3's `.ts`/`.tsx` bullet is a bare pointer with no cut argument**, the thinnest non-goal in
  the set.

### `-3` (corpus scoping) — see B3; recommended for cutting

- **HIGH — the 25% cap is a selector over an empty population on the only repo that runs it, with no
  liveness assertion and no remedy when it trips honestly.** [verified here] gov excludes zero files.
  An adopter whose vendored `engine`/`diverged` rows carry >25% of graded definitions gets an
  unclearable RED: the receipt is generated by `govkit apply`, the adopter cannot edit it, the cap is
  a kit constant §4 refuses to expose, and no §5 row names an escape. S3 applies the zero-match law to
  receipt *rows* two scope items earlier and S4 gets no equivalent.
- **MED — three dependency edges owed to `-3` and written on neither side** (`-8` F3's soft probe-corpus
  edge; `-9` F3's assert-C edge, which has teeth — excluding a path makes its grandfathered rows
  underivable and assert C reds them, so `-3`'s scoping commit must delete them; and `-8`'s reciprocal).
  `-3` is the most-depended-on unit in the build and carries **zero** downstream edges.

### `-4` (waiver keying)

- **HIGH — S6 adds a `signal_`-led offender, does not move the pin, and §7 claims the leg stays green.**
  [verified here] `signal` is not among the 22 declared verbs; `lexicon.py:537` is `if len(unwaived) > pin`.
  One new off-table definition at pin 463 reds `lexicon naming predicates` on the landing commit.
  `-7` proves this shape costs a pin move and pays it; `-4` performs the same act and pays nothing.
  **Fix:** rename `signal_lexicon_waiver_rows` → `build_lexicon_waiver_rows`, matching the
  `build_live_backlog_rows` precedent `-4` §4 already cites. Then §7 becomes true and no pin moves.
- **MED — `load_waivers` is rewritten by two units four phases apart.** `-4` §4 claims it explicitly;
  `-9` F2 generalises it to `load_keyset(path, reason=False)` while `-9` §3 says "No waiver redesign".
  Neither names the other on this point.

### `-5` (RATCHETS rows and the repair) — see B2

- **MED — `-7` is a third user of `-5`'s marker mechanism and is missing from §4:129's enumeration**,
  which reads as the complete list ("Two new edges, neither in the build's declared set" — naming only
  `-4` and `-6`). If R1 F3's rename is applied (see `-7` below), this finding disappears with it.
- **MED — S2's vanish arm and `-9`'s new "a `RATCHETS` row names a live key" assert are two mechanisms
  for one condition**, and neither spec says which fires first.
- **LOW — `-5` correctly carries the `-9`-deletes-me reciprocal four times.** `-9` §4's claim that
  "the reciprocal is owed there" is false. Fix `-9`, not `-5`.

### `-6` (coverage floor and mode ratchet)

- **HIGH — S5 is a second base-versus-HEAD comparison in the file that already holds one, and AC4's
  second half is false.** `signal_lexicon_ratified_stale` (`drift_report.py:726-761`) already reads
  `.lexicon.conf` base-versus-HEAD for `LANGS` movement via `-G "LANGS="` and returns
  `"gateable": True`. A `py: parser → dark` flip is a `LANGS=` edit; the signal fires with or without
  `-6`'s marker, so AC4's *"with the marker present it reports nothing"* cannot pass. `-6` §4 argues
  at length against a second base comparison and then adds one **in the same file as the first**.
- **HIGH — `TOOL-dUnstalledConvoy-35` (`memory/backlog/TOOL.md:190`) proposes to blind the existing
  signal to precisely `-6`'s move** — *"a `dark` declaration … cannot invalidate a curation … widen it
  to ignore dark-only surface changes."* `-6`'s own measurement (`py→dark` collapses armed coverage
  42.9% → 7.9%) is the refutation of that row, and `-6` cites neither. **Fix:** `-6` §4 names which
  mechanism owns the LANGS-weakening question and supersedes that backlog row in writing, or blocks
  on it.
- **MED — S6's liveness assertion covers only the half of the denominator whose failure is safe.**
  If the sniffer under-counts *armed* files the denominator falls, coverage **rises**, and S6 passes
  untouched because `.sh` still yields hits. AC6 stages the total break, the one failure S6 already
  catches. **Fix:** assert that every file an armed extractor found a definition in is also seen by
  the sniffer — exogenous, cheap, and it stages by deleting one pattern.
- **MED — the floor's denominator dispute with `-13`.** Downgraded from both convergence passes:
  [verified here] incms is 3,401 `.md` of 6,171 tracked files, so R2's measurement of **48.8%** (wide
  sniffer) / **55.1%** (narrow) under `-6`'s definition-carrying denominator is structurally sound and
  the floor of 35 is safe for the one real adopter. What survives is that **`-13` AC5 instructs `-6`
  to cite 19.3%, a figure computed under a denominator `-6` §4 explicitly rejects**, and neither spec
  states the other's denominator. **Fix:** `-13` AC5 cites 48.8% or is withdrawn; `-6` §4 states in
  one sentence what its shipped default does to an incms-shaped adopter. No floor movement needed.
- **LOW — `-6` §3 routes the `.ts` question to `-13` as a consumer while `-13` §4:109-112 heads a
  section calling `-6` the consumer.** A 2-cycle of contradictory directions, not an edge.

### `-7` (marginal offense rate)

- **HIGH — §4's premise is false and the unit's own violation is discharged by raising the ceiling.**
  [verified here] `drift_report.py:1038-1041` ends `build_live_backlog_rows, build_readme_mechanism_drift`.
  Two of the ten `SIGNALS` entries already lead with `build`, row 1 of the declared table. The
  compliant spelling is precedent, in the same list, in the same file — and one of those two produces
  `live_backlog_rows_per_shard`, the exact signal `-4` §4 names as the shape it borrows. So the unit
  whose subject is *whether the declaration constrains new generations* absorbs its own offense by
  moving the pin, on a premise the file refutes, with a free rename available.
  **Fix:** name it `build_lexicon_marginal_offense_rate` (or `measure_…`, also declared), delete S5's
  pin move, delete AC6's `464` and the `463 -> 464` marker requirement. This removes `-7` from the pin
  collision entirely and removes the `-5` §4:129 finding above.
- **MED — §3 forbids the pin move that §4 makes, §6 asserts, and §2 never scopes.** Four-way
  inconsistency inside one spec; §2's S1–S7 contain no occurrence of the word "pin". Dissolved by the
  rename fix; if the rename is refused, the pin move becomes S8 and §3 narrows to "no pin MECHANISM
  change".
- **LOW — §10 reports the `derive_*` family in `render_playbook.py` as "nine functions"; it is eleven**
  (`derive_ci_file`, `derive_default_branch`, `derive_gate_runner`, `derive_id_families`,
  `derive_lexicon_conf`, `derive_memory_disciplines`, `derive_memory_root`, `derive_node_tag`,
  `derive_primary_tree`, `derive_project_name`, `derive_worktree_root`). All fan-in 0 as claimed.
- **NOTE, not a defect — `-7`'s own measurement contradicts the reframe the whole build rests on.**
  The README, research §1 and owner ruling `-16` rest on *"136 definitions and zero offenders"*. `-7`
  §4 re-derives the same window through the kit's own extractor and reports **236 definitions, 50
  offenders, 21.2%**. `-7` says honestly that this does not refute the conclusion but shows the figure
  *"is not yet a measurement"*. Nobody re-opens `-16`. See §5.

### `-8` (canon, probe, NOT-clause grammar)

- **HIGH — §4 asserts a third `VERBS` consumer does not exist; it does.** [verified here]
  `map_extractors.py:135` registers `"lexicon-verbs": lambda: _read_lexicon_verbs()` and `:163` does
  `from lexicon_conf import load_conf; return sorted((load_conf(conf).get("VERBS") or {}).keys())` —
  the kit's own reader, graded by the map coverage ratchet. The conclusion survives by luck (`.keys()`
  is type-stable), and R2 confirmed the failure direction reds rather than silently degrades. But the
  contract-change analysis was written without reading the kit's own dossier, which says four
  consumers. **Fix:** consumer count → three (four with the dossier's engine), and §7 names
  `codebase-map coverage + freshness`.
- **HIGH — the canon is validated against the corpora it grades and ships with no curation stamp.**
  §12's law is *"DERIVE from the repo's own corpus, then FREEZE it and mark that a human curated it."*
  The kit already ships that mechanism (`ratified`, which `adopt-lexicon.sh:87-98` calls "the arm that
  makes 'the human curated it' checkable"). The canon uses none of it, ships `role = "engine"` so no
  adopter can edit it, and F1 closes agent-delegated. The one artifact that must not be derived from a
  corpus is the one with no curation stamp and no recourse.
- **MED — F5 declares itself an owner call and then resolves itself agent-delegated.** [convention check]
  Every other fork a spec calls the owner's is left UNRESOLVED and says so — `-9` F1, `-10` F4,
  `-11` F4, `-12` F2, `-13` F3, `-15` F3. Six for six. `-8` F5 is the only breach.
  **Fix:** strike the `RESOLVED` line, keep the recommendation, leave F5 open.
- **MED — S8 re-creates its own defect one file over.** `scaffold_lexicon.py:34,62` seeds `LANGS` from
  extensions present at scaffold time; F5 ships `lexicon-debt.tsv` as `role = "seed"`, an extension
  also not present then. Gov is immune only because `TOOL-dUnstalledConvoy-29` already declared
  `tsv::dark`. A fresh adopter's first `git add` of the ledger reds `UNDECLARED EXTENSIONS: tsv`.
  **Fix:** one token — S8 seeds `tsv::dark` alongside `conf::dark`.
- **MED — three arithmetic literals go stale against siblings.** AC8's "all 22 rows" becomes 23 after
  `-14`'s `cmd` row; §4's "the ratified table exceeds the canon by exactly two rows" becomes three;
  §7 does not name `lexicon skill wiring`, which `-10` deliberately leaves unguarded so that a `VERBS`
  edit without a Skill re-render reds. `-8` S7 edits eleven `VERBS` rows.
- **MED — nobody schedules the incms `--probe` run the research pass made `-9`'s adoptability
  conditional on.** Research §5 Phase 2: *"that number decides whether R8 is adoptable at all."* `-8`
  builds `--probe` and never schedules it; `-9` cites the figure twice and makes no reading a
  precondition. **Fix:** the read joins `-8`'s DoD or `-9`'s §8 as an owner precondition.
- **MED — `-2` F2 files the P3 FROM-side liveness assertion against `-8`, and `-8` never mentions it.**
  Grep of `-8`: zero occurrences of "FROM" or "P3". No spec in the set owns it. **Fix:** `-8` takes it
  or `-2` F2 records it as unowned rather than filed.
- **LOW — §4/§7 name a "frozen-canon sentinel" in `selftest.py` that no AC covers and no section gives
  a predicate.** A sentinel asserting `len(CANON) == 20` is satisfied by its own configuration.

### `-9` (freeze, grandfather set, five asserts) — see B5, B7

- **HIGH — the shrink-only property has no assert. Five asserts permit re-adding any row ever drained.**
  Walk A–E against a key that was an offender at `FREEZE_SHA`, was drained, and is later re-broken and
  re-listed: A ✓, B ✓ (it is an offender again), C ✓ (it was one at the freeze), D disjoint, E liveness.
  **Green.** Nothing compares the file against its own previous state. The true property is *bounded by
  |offenders at FREEZE_SHA|*, with absorbing capacity equal to the drain history — zero on landing day,
  growing with every `--drain`. This is the exact defect `-9` §10 quotes from `memory/map/baseline.toml`.
  **Fix:** a sixth assert deriving the set at the previous commit and refusing any added row (the same
  `git show` machinery assert C already builds), or state the honest bound in §1 and §5.
- **HIGH — the multiplicity answer is gov-scale.** Gov has 3 multiplicity keys (verified by R2, exactly
  accounting for 463 − 459). incms has **113 keys with >1 occurrence in one file, 183 excess
  occurrences**, worst at 11, and the list includes `__getattr__` — a name Python's protocol reserves
  and nobody can rename, precisely the class `-11` had to build a structural exemption for. §3 forbids
  the multiplicity field; §4 answers with renaming. Three renames on gov becomes 113 on the one real
  adopter, several illegal.
- **HIGH — AC8 asserts a property the cache design cannot deliver.** §4 keys the cache on a digest of
  `FREEZE_SHA` plus conf bytes — the **inputs**. Editing the payload changes nothing the digest covers,
  so the poisoned payload is served. **Fix:** delete AC8, or store `sha256(body)` beside it and
  re-verify (four lines), which makes it true.
- **MED — `extract_text` is specced as a new split twice**, by `-7` S4 (Phase 0) and `-9` §4 step 4
  (Phase 4), same signature, same justification, neither citing the other. M1 assigns it to neither.
  **Fix:** `-7` owns it (it lands first); `-9` cites.
- **MED — where a past-tree read lives is answered two ways.** `-6` §4 argues a second base comparison
  inside the lexicon leg would give the repo two answers, and `-7` follows it into `drift_report.py`.
  `-9` §4 puts assert C's freeze-time derivation inside `lexicon.py` on a self-containment argument and
  does not engage `-6`'s objection. Both arguments are sound; `-9` is the outlier of three.
  **Fix:** `-9` states why a fixed-sha read is not the windowed base comparison `-6` forbids. It
  plausibly is not — nobody has written it down.
- **MED — the backfill size is stated three ways and none is what the freeze will hold.** S9 says 459;
  F5 says freeze at 380 after `-14`; `-11` §4 says "the 55 or so P6 offenders are grandfatherable
  without special handling". `-9` is blocked on `-11`, so the real set is ≈380 + the P6 count measured
  at landing. No spec names that number or the arithmetic.
- **MED — the F-A5 supersession ordering exists in exactly one place.** Ruling `-17` requires it in
  writing before `-9` lands; `-7` §4:160 puts it in `-7`'s commit; `-9` never references `-7` or the
  supersession, so the constraint reads as `-7`'s internal business.
- **MED — `-9` §4 says `-5` owes a reciprocal that `-5` already carries four times.** Delete the claim.
- **LOW — §4's "median 42 renames per commit" does not reproduce.** Over the last 60 commits, taking
  `min(def-lines removed, def-lines added)` as a loose upper bound: **median 0, mean 0.1, max 2, only
  3 of 60 commits carry any**. This makes `-9` *less* risky than its own §5 claims, but the figure is
  load-bearing for the "`--drain` must ship with the asserts" argument.
- **LOW — AC10 asserts "a run over 1.5 s cold is a finding" against a 0.44 s warm baseline four other
  units have already moved.**

### `-10` (--suggest, --brief, the Skill, the charter pointer) — see B8, B9

- **HIGH — F5 ships a `PostToolUse` observer that appears in no scope item, no design, no file list and
  no acceptance criterion.** Every occurrence of "observer" in the spec is at lines 57, 250, 325,
  326-331. §2's S1–S7 do not contain it; §4's nine sub-heads do not design it and its thirteen-path
  Files-touched list has no hook; §6's AC1–AC11 do not observe it; §7 adds no leg for it; §5's testing
  row names seven arms, none for it. And §5:250 lists it as the **unresolved owner scope-menu item**
  while F5 marks it `RESOLVED`. A Tier-2 spec whose §5 unresolved items *are* the owner scope menu (M5)
  is offering the owner a choice its §8 already took. **Fix:** promote it to an S-item with a design, a
  file and an AC, or strike it from F5 and let §5's line stand.
- **HIGH — AC10 cannot distinguish an armed rule from a dead one, and no arm stages its RED.** S6 adds
  a `LAYERS` row `lexicon.py -> scaffold_lexicon.py` with "no live candidate edge today". AC10 observes
  "no offender", which is what an obeyed rule produces **and** what a dead rule produces. A new refusal
  landing with its failing case never observed is a §7 landing condition, not a preference.
  **Fix:** one more AC — stage `import scaffold_lexicon` into `lexicon.py`, observe P3 RED naming the
  row, unstage.
- **MED — the unguarded Skill leg reds on every later `.lexicon.conf` edit and no later unit budgets
  the re-render.** `-8` S7 (11 `NOT` clauses) and `-14` S3 (`cmd`) both edit `VERBS`; neither names the
  leg in §7 and neither has `SKILL.md` in its file list. Working as designed and unbudgeted on both
  sides, which is how an unguarded leg gets `--no-verify`'d the first time it fires.
- **MED — `-10` regresses the four-step un-adoption procedure and does not say so.** `tools/lexicon/README.md:73`
  documents it. `-10` adds a committed artifact **outside the kit home**, two inventory keys to un-claim,
  an `[[lf_pin]]` and a `.gitattributes` row — four to six steps, not four. S7 promises README additions
  for the verbs, the Skill and the leg, and not for the uninstall order. `memory-recall` has already
  paid for this procedure and it can be copied.
- **MED — no `### Rollout`.** `-10` touches five surfaces across three kits and two streams with three
  separately-named landing risks, and has no ordering statement — while carrying a real constraint:
  its charter bullet reads *"let a rendered Skill HAND them to the author"*, which is false until S4
  lands, so the charter edit cannot precede the Skill.
- **MED — the `-8` → `-10` edge is declared by `-10` F1 as owed to `-8`, and `-8` never mentions `-10`.**

### `-11` (the visitor rewrite, P6, the exemption class) — see B7, B10

- **HIGH — the extractor rewrite has no invariance assert for P1.** [verified by grep] `-11` mentions
  `P6` 28 times and `P1` **zero** times, while S2 replaces `_python_defs`'s `ast.walk` with a
  scope-maintaining `NodeVisitor` and S3 widens `extract()` from a 3-tuple of 2-tuples to a flat record
  list — the function whose output P1 grades. Every downstream number in the build is quoted off
  today's P1 population: `-9`'s 459 keys / 463 occurrences, `-14`'s 463 → 384, `-4`'s 109 of 463.
  If the visitor sees one binding `ast.walk` missed, all of them move.
  **Fix:** an S-item and an AC asserting P1's offender count is unchanged by the extractor rewrite
  alone (exemption class and P6 applied separately), with the measured before/after.
- **HIGH — the exemption class is armed entirely by the commit that installs it.** [verified here]
  zero `visit_*`, zero `generic_visit`, zero `cached_property`, three `@property` in two files. After
  landing, the class's population is ~17-18 names **the same commit wrote**, plus 3 properties and 4
  zero-argument methods. AC4 ("the exemption total is greater than zero") is satisfied by the author's
  own dispatch methods forever. AC5 ("the gate that reds at 471 over 463 runs GREEN") is equally
  produced by the exemption over-covering, a raised pin, or a smaller visitor. §4 already concedes the
  class over-covers by half its method arm (`govkit.py::emit`, `_find_charter`). This is §7's
  guard-shares-a-variable shape at the population level.
  **Fix:** an arm asserting the exempted set equals a named enumeration, and AC5 asserting the offender
  delta is exactly −26 rather than merely "green".
- **HIGH — S1 and §4 contradict each other on the refusal's granularity, and one of the two reds on
  landing day.** S1: *"a shape matching zero definitions REDS."* §4: *"one exemption class with one
  population … the refusal fires only if the whole class goes empty."* Under S1 the class reds on the
  landing commit twice over (`visit_` 0 before the commit, `cached_property` 0 permanently). Under §4
  the liveness assertion is a single integer over a heterogeneous class — **the fold `-2` exists to
  delete, reintroduced one level down in the same build.**
  **Fix:** S1 takes §4's wording, and §4 states plainly that the class is arm-checked in aggregate and
  that `@cached_property` ships with an empty population.
- **MED — the kit's own dossier records the transferable P3 lesson and `-11` ignores it.**
  `memory/map/features/lexicon.md`: *"A predicate's correctness concentrates in its helpers, and
  fixtures do not reach them: extend the tables, not just the fixtures"* — earned over three adversarial
  rounds and four blockers, all in two helper functions, none visible to 48 fixture arms. `-11` rewrites
  the extractor helper wholesale and its §5 testing plan is fixtures plus arms plus a
  caller-compatibility arm. **No case table.**
- **MED — F2 narrows owner ruling `-19` and resolves it agent-delegated.** The argument is strong and
  measured, and R2 re-derived it and found `-11` **understates its own case 5×**: the literal
  zero-argument reading exempts **83 (19.9%)**, of which **37** — not seven — are `t_`-prefixed names
  `-14` exists to remove. But it is a re-reading of an owner ruling closed as delegated, while F4 leaves
  the *sequencing* question open to the owner. The wrong one of the two is delegated.
- **MED — `-11`'s four-site call inventory is measured at base and stale by its own phase.** `-7`
  (Phase 0) adds `signal_lexicon_marginal_offense_rate` as a fifth reader whose contract is
  `(path, name)` pairs, exactly the shape S3 widens.
- **MED — `-12` depends on `-11`'s classifier and cites ruling `-19` instead**, so the edge exists on
  neither side. `-19` builds nothing; per M1 and `-11` F2 the classifier is `-11`'s mechanism.
- **LOW — `-11` §4 says `-8` should state that it does not carry the `-19` exemption; `-8` does not.**

### `-12` (the consistency instrument)

- **HIGH — every headline number is measured against an extractor `-11` replaces two phases earlier.**
  AC1 reproduces `CONSISTENCY = 0.716` over 589 object-carrying definitions from a population of 824,
  all measured against today's `_python_defs`. `-11` (Phase 3) emits `param`, `module_const`,
  `class_attr` and `import` records over 2,349 of 8,249 bindings; `-12` is Phase 5. AC1's own escape
  clause fires by construction. `-12` never mentions `-11`. **Fix:** AC1 names the extractor it
  reproduces against, and §4 states that a post-`-11` run re-baselines rather than reproduces.
- **MED — AC7 is pinned to base-`9ddcc5c9` output that six Phase-0-to-3 siblings rewrite.**
- **LOW — §3 forward-references a §8 item that does not exist.** §8 has F1 (the precision bar) and F2
  (does the owner want this measured); neither is the demote-the-verb-table decision §3 points at.

### `-13` (the .ts/.tsx coverage decision)

- **HIGH — AC5 is the only acceptance criterion in the build that observes another unit's artifact**,
  and it instructs `-6` to cite a figure computed under a denominator `-6` refuses. `-6` is Phase 0 and
  `-13` is off-phase, so it is an AC on an artifact that lands first and cannot retroactively satisfy
  it. **Fix:** AC5 becomes an observation of `-13`'s own deliverable (that `LEXICON.md` states the
  figure and names it as `-6`'s input), and the obligation on `-6` moves to §4 as a stated edge — with
  the number corrected to 48.8% under `-6`'s denominator.
- **MED — AC3 and AC4 are pinned to base output that `-2`, `-9` and `-11` all rewrite.**
- **NOTE — F3 (adopt on incms?) is left UNRESOLVED and is the decision that matters.** Legal per the
  brief, but a DECISION unit that does not decide its own headline question has not shipped.

### `-14` (the t_ and do_ renames, the `cmd` row) — the safest unit in the build

R2 executed all 74 renames mechanically and ran everything downstream. Reference count 211 (spec says
"roughly 210"); **zero collisions** in both directions; `memory-recall/selftest.py` 36/36 PASS;
`codebase-map/selftest.py` PASS; five `memory-tree --selftest` modules PASS with all arms held;
`refusal_join.py` 161 branches / 2 modules unchanged; pin after rename plus the `cmd` row lands at
**exactly `VERB_OFFENDER_PIN="384"`**; zero `t_`/`do_` hits in `.memory-tree.conf`,
`.codebase-map.conf`, `memory/project/`, `tools/gate-legs.json` or `.githooks/`. **REFUTED as a risk.**

- **HIGH — S3 never says what the `cmd` row's negative definition is.** S3 says "with a negative
  definition"; AC5 asserts it "carries a negative definition rather than a bare gloss"; the clause
  itself is nowhere in the spec. Compare `-8`, which publishes all eleven of its backfilled negatives
  with the boundary each draws. The charter's rule — quoted verbatim in `-10` §4 — is *"Write the
  NEGATIVE definitions or do not bother … the boundary is the whole product."* `-14` ships the
  product's boundary as a TODO.
- **HIGH — `cmd` reds `codebase-map coverage + freshness` and moves three generated artifacts.** R2
  staged it: `UNCLAIMED {'lexicon-verbs': ['cmd']}`, and after `gen_map.py --write`, `MAP.md`,
  `inventories.json` and `symbols.json` all move. S6 names only `symbols.json`, and `symbols.json` also
  carries 51 `t_*` rows the rename moves. §7 lists the map leg as green.
- **MED — S3 changes a closed enum four other units read** (`-7` F2, `-8` S6 assert 2, `-9` ruling 1,
  `-12`) with no admission order stated against `-8`'s assert or `-9`'s freeze. §3 of the charter makes
  a cross-cutting enum change contract-first.
- **MED — `-14` and `-11` both move the pin off base 463 and neither states an order.** With `-7`'s
  rename applied (see above) this is a two-way, not three-way, collision. **Fix:** `-14` lands first
  (largest move, 463 → 384) and `-11` expresses its move as a delta.
- **LOW — AC7 cannot fail, and §4 already proves it.** `refusal_join`'s population is
  `git ls-files tools/govkit/*.py`; the renames are in `tools/memory-tree/`. Disjoint by construction.
- **LOW — two off-by-ones:** 58 references measured against the table's 59; `main`'s roster is 36 arms,
  not 34.

### `-15` (wiring check_runbook_parity.py) — see B6

- **MED — a new leg reds `govkit selfcheck` on the missing `tools/govkit/subject-pins.tsv` row**, and
  `-15`'s Files-touched list omits it. S4 correctly claims the new gate-leg map key — the only spec in
  the set that does. One command.
- **MED — `WIRE-INTO-PROJECT.md` is 51,481 bytes / 684 lines and carries no row in
  `tools/template-size-limits.txt` or `tools/line-length-limits.txt`** [verified here], so its +20 KB
  is unconstrained by any gate. Blast radius: prose only.
- **LOW — §5's own risk row concedes the failure mode no automation reaches:** *"a body that is
  technically non-empty and substantively hollow passes the machine check and fails the reader."*

### Cross-cutting, no single owner

- **HIGH — six `.lexicon.conf`-subject refusals land inside a leg whose guard cannot see
  `.lexicon.conf`, and the sentence that saves them is stale.** [verified here] `tools/gate-legs.json`
  guards `lexicon naming predicates` on `tools/`, `skills/session-kickoff/`, `.githooks/`, `.claude/`
  and the other two lexicon legs on `tools/lexicon/`. **None covers the repo-root conf**, and
  `tools/lexicon/kit.toml:46-49` says that is deliberate and unfixable. `kit.toml:49-51` answers with
  *"the pre-push hook sets `GATE_FULL=1` … so the authoritative run stays total"* — [verified here]
  `.githooks/pre-push:109` records that it *used* to do so unconditionally, `:129` declares
  `GATE_FULL_MAX_LAG=10`, and `:224` sets it only on a decision. So a `.lexicon.conf`-only commit — the
  exact shape of every absorbing move this build exists to prevent — can reach `main` with no lexicon
  leg having run, whenever a recorded full green covers the tip within the lag bound.
  Affects `-2` S2, `-4`, `-6` S3, `-8` S6, `-9` assert C. `-10` §4 states the property correctly and
  uses it to justify one unguarded leg; five siblings inherit the blindness unremarked.
  **Fix:** one sentence in `-2` (which owns the reporting contract) stating that every conf-subject
  refusal in this build is invisible to a guarded local bar and binds only at the push boundary,
  citing the current decision rule rather than the retired one.
- **MED — the set disagrees with itself on this repo's tracked-file count, and both numbers are right.**
  [verified here] `9ddcc5c9` = 896, `af4de2d5` = 899. `-2` prints 896; `-3`, `-6` and `-10` use 899.
  Every header declares `base 9ddcc5c9`. **Fix:** `-6:156` and `-10` name `af4de2d5` at the point of
  use, as `-3:61` already does.
- **LOW — bare `N/A` in §5's i18n row in `-5`, `-12`, `-13`, `-15`.** The landed hygiene-green exemplar
  `-2` does the same and no gate reads it. House-consistent; fix only to be stricter than the model.
- **LOW — wrap width over 100 columns:** `-11` 19 lines (max 102), `-10` 18 (102), `-15` 8, `-13` 7,
  `-14` 3, `-12` 1. The exemplar has 13 at max 102. No gate checks it.

### Dropped — raised by a lens and refuted; do not re-run these

`-9` assert C as a tautology (two operands from two trees; a past blob is exogenous). `-7`'s two
derived operands (§4 answers `assertion-between-two-derived-values.md` by measurement — its own table
is a run where the comparison disagreed). `-3` AC4's `82.3` literal as circular (the assert is on the
refusal firing, not on the arithmetic agreeing with itself). `-11`'s span arm as decorative (AC2 is the
falsifying arm; 51-versus-1,033 is a real discriminator). `-12` shipping no gate (§7 states the
negative and AC7 asserts triviality — correct for a research unit). `-8` S6 assert 2 as
satisfied-by-configuration (it binds forward on every future row, with a live failing case in AC7).
`-15`'s gate as a presence check (`check_runbook_parity.py:9-17` carries its own non-empty-body
liveness half). `-5` reddening on landing (all five `.memory-tree.conf` keys and all three
`drift_signals.py` `PINS` keys resolve at HEAD). `-14` needing a split. `-12` and `-13` secretly
speccing builds (both fence themselves with machine-checkable criteria: `-12` AC7 and `-13` AC3 both
assert `git diff --stat` names nothing under `tools/`). All nine cited gotcha classes exist. Nine
`-8` §10 / `-14` §10 reuse-lookup results re-run and real. CRLF is a worktree smudge only — the
committed and staged blobs carry zero CR, `.gitattributes:47` pins `memory/**/*.md text eol=lf`.
No spec adds a runtime dependency: everything is stdlib plus git plus an existing precedent.

---

## 4. SPLIT RECOMMENDATIONS

Three units are not one unit. `-14`, `-9`, `-3`, `-4`, `-6` and `-11` each are — verified, do not
re-litigate.

### `-8` splits at the seam between S5 and S6. **Recommended.**

S1–S5 plus S8 are one mechanism: the canon replaces the frequency allowlist, and S5 cannot land
without S1 or the scaffold writes no `VERBS` block at all. S6–S7 are a conf-grammar change plus a
curation pass, and `-8` §2 already says *"S6 and S7 land in ONE commit"* while §5 names them as a
separate landing-day risk from the canon's. The spec found its own seam and declined to cut on it.

The dependency runs the wrong way for keeping them together: §4 argues the canon is validated **by**
the eleven existing negatives (*"The canon reproduces a curated table it never saw"*), so the
negatives are evidence for the canon, not output of it. All eleven are published in §4 and could be
written with `canon.py` nonexistent.

**What the split buys, concretely.** `-10` F1 states that `--suggest`'s replacement message needs
`-8`'s structured NOT-clause index and `-8` is a phase later, so `-10` ships a degraded message and F4
stays open on an unverified claim. The NOT-clause half has no canon dependency and is Phase-0-shaped.
Land it in Phase 0 and `-10`'s degraded-message gap does not exist.

- **`-8a`** = S1, S2, S3, S4, S5, S8 — canon, `--probe`, the `--scaffold` frequency-allowlist deletion.
  Tier-2, Phase 2.
- **`-8b`** = S6, S7 plus the `lexicon_conf.py` `VERBS` value-type change — structured negatives and
  the eleven-row backfill. Tier-1, Phase 0, landing before `-10`.

### `-15` splits into prose and wiring. **Recommended, and its own F3 asks for it.**

F3: *"does this unit write all eighteen sections, or does it wire the gate and hand the prose to
eighteen owners? Genuinely the owner's, and left UNRESOLVED."* The measurements decide it: +20 KB and
+300 lines of runbook against *"three lines of JSON"* of wiring — two work items at a 100:1 size ratio,
different reviewers, different risk. §4's Rollout already describes them as two phases.

- **`-15a`** = S1 (the eighteen sections). Prose only, no gate, bounded commits, `streams deployer`,
  honestly Tier-1.
- **`-15b`** = S2 + S4 + S5 (leg, map claim, leg-row limit text) — **and S3 is dropped per B6**. One
  commit, once the count is zero. Tier-2 on the shared-contract trigger if S3 is ever revived; Tier-1
  as a gov-only leg.

Merged, the tier is wrong in one direction (a new merge-bar leg to every adopter is a shared-contract
change) and the stream is wrong in the other (`WIRE-INTO-PROJECT.md` is the `deployer` stream's
product by §6's routing table, while the header declares `streams tooling`).

### `-10` splits, or takes a `### Rollout`. **Weaker recommendation.**

`-10` touches five surfaces across three kits and two streams (`--suggest`/`--brief` in `lexicon.py`,
a rendered Skill under `.claude/`, a gate leg, a `LAYERS` row, the charter/template edit), has three
separately-named landing risks, one undesigned deliverable (F5's observer), and no ordering statement
— while carrying a real ordering constraint: the charter bullet it publishes says *"let a rendered
Skill HAND them to the author"*, which is false until S4 lands.

**Minimum:** a `### Rollout` naming commits in order, as `-6` and `-15` do, plus the F5 resolution from
§3. **Cleaner:** `-10a` = `--suggest` + `--brief` (the CLI, Tier-1); `-10b` = the Skill + its leg + the
`LAYERS` row + the charter pointer (Tier-2, after `-10a`).

### `-14` S3 is a contract, not a scope item. **Sub-split, not a unit split.**

The 74 renames are one mechanical diff and stay together. Adding `cmd` to `VERBS` changes a closed enum
that `-7`, `-8`, `-9` and `-12` all read, which §3 of the charter makes contract-first. Either split S3
into a three-line contract landing before `-8`, or `-14` §4 states the admission order against `-8`'s
assert and `-9`'s freeze. Neither is written today.
---

## 5. THE PLAN-LEVEL VERDICT

**R4 is substantially right and I am not going to soften it because the plan is ours.** The
diagnosis in the research pass reads *"the gate is the half with the zero. Do not respond to 'it
shipped worthless' by building more gate."* The plan then spends roughly 1,000 of its ~2,000
estimated new lines on gate machinery (`-3`, `-4`, `-5`, `-9`, `-11`) and ~250 on the one mechanism
with a measured record (`-10`), which it schedules seventh. The specs are individually excellent.
**The plan does not follow from its own diagnosis.**

Scale, for the record: the kit is 1,504 lines today (`lexicon.py` 569, `selftest.py` 489,
`lexicon_conf.py` 152, `scaffold_lexicon.py` 140, `adopt-lexicon.sh` 116, `subtokens.py` 38). The
specs' own Files-touched estimates sum to about 1,990 new or changed lines, plus a 459-row tracked
artifact, plus ~20 KB of runbook prose — a 130% growth of a kit with **one** adopter, four Tier-2
reviews, and an unresolved owner sha decision (`-9` F1) before the largest unit can start.

### Does this build deliver the owner's three demands?

**Demand 1 — coverage beyond function names, explicitly including variables. PARTIALLY, and the
first thing it ships is another pin.** `-11` S4 is the entire delivery: `len(name.strip("_")) >= 3`
unless allowlisted or the enclosing scope is ≤10 lines, over reach ≥ 2 — 2,349 of 8,249 bindings, so
71.5% of variable bindings are refused by design. Python only. On the one adopter, `.ts`/`.tsx` are
dark by `-13`'s ruling, so demand 1 reaches a fraction of a fifth of that tree. And it arrives as
`SHORTNAME_OFFENDER_PIN`, a **fourth** raisable integer in Phase 3, two phases before `-9` deletes
them; net pin count across Phases 0–3 goes **3 → 5** counting `-6`'s `COVERAGE_FLOOR`, which `-6` §4
itself calls *"a scalar in a conf, which is a pin with the sign flipped"*. Demand 1's first
deliverable is a ceiling. **Fixable — see the smaller build.**

**Demand 2 — real constraining pressure, not a ceiling that absorbs. ONLY IF `-9` LANDS, AND `-9`
CANNOT LAND AS WRITTEN.** `-9` alone answers it: Phase 4, Tier-2, blocked on `-4` and `-11`, ~600
lines, 459 tracked rows, F1 unresolved. Two things must be said plainly.

First, the standard is applied unevenly. `-5` §3 refuses to claim pressure and is right to:
*"§4 prices the move it deters and the price is five minutes of prose … Against an LLM author, five
minutes of prose is a subroutine rather than a deterrent."* `-9` §5 concedes its own escape — *"a run
with shell access can move `FREEZE_SHA` in the same diff"* — and claims that what assert C buys is
that absorption *"becomes a visible edit to the one value in the file whose purpose is provenance."*
That is one extra line in a diff. Against the same author `-5` prices at five minutes, `-9` claims
pressure for a one-line diff and never applies its sibling's yardstick to itself. The difference is
**visibility, not cost**, and nobody in the set prices visibility.

Second, and decisive: **the demand-2 mechanism has five defects that make it unlandable in its
current form** — B5 (the seed ships gov's 459 rows to every adopter and deletes the hole that
explained the red), B7 (three pins, not four), the shrink-only property with no assert, AC8 asserting
a cache property the digest cannot deliver, and a multiplicity answer that is three renames on gov
and 113 on the one real adopter, several of them illegal names. So the owner's choice is **not**
"build demand 2 or defer it". It is "fix five things and build it" or "defer it". Nobody has costed
the first option.

**Demand 3 — an on-demand probe in existing adopter repos emitting guards that force rework. THE
PROBE SHIPS; THE POPULATION IS STILL ZERO WHEN THE BUILD ENDS.** `-8`'s `--probe` is real, read-only,
correct. `-15` wires the runbook so an adopter is finally told the kit exists. "Guards forcing rework"
is delivered as `-8`'s debt ledger — which `-8` §3 says **no gate reads**, `role = "seed"`, deletable
with no consequence — plus `-9`'s asserts, which bind only a repo that has already adopted. [verified
here] `C:/projects/incms/main` has no `.lexicon.conf`. **No unit in this build installs the kit
anywhere**, and `-13` §3 says so: *"Deciding what the kit says about `.ts` is a different act from
installing it there, and the second one is nobody's unit yet."* The research's §2D calls adopters = 0
*"the population that decides everything"*. Thirteen units later it is still one, by construction.

### The single biggest risk no spec addresses

**Every unit raises the price of adopting the kit, in a build commissioned because nobody adopts it,
and no spec carries an adoption-cost budget.** Sum what a new adopter faces after all thirteen land:
`--scaffold` **refuses** without a receipt file that exists nowhere (`-3` S5); `COVERAGE_FLOOR` must
be cleared (`-6` S3); every `VERBS` row must carry a hand-written `NOT` clause or the bar reds (`-8`
S6); `DEAD PREDICATE` reds every armed (extension, predicate) pair with an empty population (`-2` S2);
four pin keys, then a `FREEZE_SHA`, a `--freeze` verb, a ~6,500-row grandfather file and a standing
`--drain` obligation (`-9`); three waiver registries with mandatory reasons (`-4`); an unguarded Skill
leg that reds on every `.lexicon.conf` edit without a re-render (`-10` S4). Each is individually
defended in its own spec. **Nobody adds them up.** `-3` §4 names the stake — *"un-adoption is the
failure mode this kit can least afford"* — and then adds a refusal.

Two secondary plan-level risks, both real:

- **There is no stop rule.** `-7` is the only instrument that measures whether any of this works, and
  nothing reads it. The research's Phase-2 exit says the incms `--probe` report *"decides whether R8
  is adoptable at all"*; `-8` builds the probe and never schedules the run, `-9` cites the figure
  twice and makes no reading a precondition. Thirteen units of unconditional commitment, two
  measurements taken, zero decisions hanging off either.
- **The build's own arithmetic is contested inside itself and nobody arbitrates.** `-7` measures the
  marginal rate at 21.2%; the README, the research and owner ruling `-16` all say 0%. `-6` sets a
  floor of 35% under a denominator nobody had measured on the adopter until this pass. `-9` deletes
  three pins; `-11` says four. Three units move `VERB_OFFENDER_PIN` off base 463 in three directions
  — and one of the three (`-7`) is moving it on a false premise. In a build whose thesis is that one
  fact must have one carrier.

### CUT list

| unit | verdict | reason |
|---|---|---|
| **`-3`** | **CUT** | B3. Reads a receipt spelling that exists in neither repo, excludes zero files on gov and 2.4% on incms, breaks `--scaffold` on 100% of live repos, and its central justification (a derived proposal computed over a corpus containing the deriver) is **deleted by `-8` S5** two phases later when the frequency allowlist goes away. Lost by cutting: one spurious cluster row a curator deletes. |
| **`-5` S1 (three `RATCHETS` rows)** | **CUT** | The spec prices its own product at five minutes of prose and states that `-9` deletes it. Building a mechanism you have specced as worthless and scheduled for deletion is motion. |
| **`-5` S2–S4 (the repair)** | **RE-FILE** as a drift-audit unit, **after B2 is fixed**. It covers eight existing rows in two other kits and has nothing to do with the lexicon. |
| **`-6` S3–S4 (the floor + its ratchet row)** | **CUT** | A conf scalar defended by a ratchet row whose mechanism `-9` deletes — `-11` §4 forbids exactly this shape in principle (*"the raisable integer under a new name, arriving in the same build that deletes the raisable integer"*) and `-3` §4 takes `-11`'s side for its own cap. Two answers to one question, argued oppositely, neither citing the other. Ship the number, not the verdict. |
| **`-6` S1/S2/S5/S6** | **KEEP — I depart from R4 here.** | R4 cuts S5 with the floor. S5 is the **only control that makes `-2`'s cheap `.js`-dark escape visible** (B4), and R2 measured that escape at 45 offenders with a green bar. Keep the printed fraction, its liveness assertion, and the `parser > probe > dark` mode ratchet; drop the verdict. |
| **`-12`** | **DEFER, not cut** | I depart from R4 slightly. Its own §4 rules three of four gaps NOT CLOSABLE and its pre-registered bar is 0.80 against a measured 0.716, so the predicted outcome is a written refusal. But it is cheap (one probe script, nothing under `tools/`) and its numbers are re-baselined by `-11` anyway. Re-file behind `-11`, out of this build. |
| **`-13`** | **SHRINK to two sentences in `LEXICON.md`** | A 228-line spec for a decision whose headline fork (F3, adopt on incms) it leaves unresolved. Keep the ruling; drop the spec. |
| **`-15`** | **RE-FILE out of this build**, and **drop S3 permanently** (B6) | Correct work, not lexicon work — its own §1 says so. +20 KB and eighteen runbook sections is the single largest schedule item here, and it makes a lexicon build's completion depend on seventeen unrelated deployables' prose. |
| **`-4`** | **KEEP if `-9` is built; CUT if not** | 40 lines against three empty registries. Its standalone value (waivers keyed on `path::name` rather than matched text, mandatory reasons) is real but small; its stated purpose is preparing `-9`. |
| **`-9`** | **DECIDE, do not schedule** | See demand 2 above. Not landable as written. If built, fix all five defects and gate it on `-7`'s first reading and the incms `--probe` report. |
| **`-11`** | **SPLIT the verdict — I depart from R4 here.** | R4 makes all of `-11` conditional on `-9`. The **visitor rewrite and the `-19` exemption class are correctness work that stands alone**: `extract()` has four resolved readers in three kits, the current `ast.walk` destroys enclosing scope, and the exemption is required for any noun-led accessor ruling regardless of freezing. **Cut `SHORTNAME_OFFENDER_PIN`** — that is the fourth ceiling, and shipping P6 without a pin (as a printed count plus the exemption) delivers demand 1 without one. |
| **`-2`, `-7`, `-8`, `-10`, `-14`** | **KEEP whole** | With their fixes. `-14` in particular is the second-most valuable unit in the set and is filed as a footnote to `-9`'s backfill arithmetic: it is the only unit that makes this repo's **names** better rather than making the machinery that judges them bigger, and it drops the pin 463 → 384 by doing the work. It survives `-9`'s cancellation on its own merits. |

### The smaller build

Six units, roughly 750 lines, **no new pin, no new conf scalar, no receipt reader, no 459-row
backfill, no freeze ceremony, no 20 KB runbook.**

1. **`-2` whole**, with the `LANGS` pair-level grammar widening taken into scope (B4) and S4 rewritten
   to name no conditions (§3). ~90 lines. The failing case is already in the tree.
2. **`-6` S1/S2/S5/S6** — the printed fraction, its liveness assertion, the mode ratchet, no floor.
   Lands **with or before** `-2` S2, so the `.js`-dark escape is visible if anyone takes it. ~70 lines.
3. **`-7` whole, renamed and landed first** (R1 F3): `build_lexicon_marginal_offense_rate`, no pin
   move, no marker. Add the one sentence no spec in the set contains — **what reading of it kills the
   pressure chain**. ~120 lines.
4. **`-8b`** — the structured NOT-clause grammar and the eleven backfilled negatives, Phase 0, before
   `-10`. Then **`-8a`** — `canon.py`, the unconditional first-element rule, the `--scaffold`
   frequency-allowlist deletion, read-only `--probe`. Skip `--probe --write`, the debt ledger and its
   `role = "seed"` artifact: no gate reads them and no adopter exists to run them. ~350 lines total.
5. **`-10` whole**, landed first or second, with F5 resolved, a `### Rollout`, both map keys claimed,
   the subject-pin row, and AC9's literals corrected to 64,361 / 48,794. The one half of this kit with
   a measured record. ~250 lines.
6. **`-14` whole**, with the `cmd` negative definition actually written and `cmd` landing as a contract
   before `-8b`. 74 renames, pin 463 → 384 **by doing the work**. ~0 net lines.

Then **stop and read**: `-7`'s first standing reading, and `--probe` run read-only against
`C:/projects/incms/main`. Those are the two measurements this plan takes and never consults. Decide
the pressure chain (`-4`, `-9`, `-11`'s P6 pin) with them in hand.

**Does the thirteen-unit plan beat the six-unit one? On exactly one axis: demand 2 as literally
stated.** It pays about 1,250 extra lines, four Tier-2 reviews, an owner sha decision, a permanently
drained tracked artifact and a ~6,500-row obligation on the first adopter, for a mechanism whose
deterrent is a one-line diff, whose only stated customer does not exist, and which has five defects
that stop it landing today. **Say that to the owner in those words and let them choose.** If they want
demand 2 built anyway — a legitimate answer, since it is what they asked for — build it as a
**seventh** item after `-7` has reported once, not as the terminus of a five-phase chain nobody can
stop.

### The dossier, which one spec of fourteen touches

[verified by grep] only `-7` names `memory/map/features/lexicon.md`. After this build the dossier's
Constraints section still says *"Waivers key on the matched TEXT, never `<path>:<line>`"* (falsified by
`-4`), *"The seed is DERIVED and then FROZEN"* (falsified by `-8` S5), and *"P2 is scoped to DEFINITION
sites only"* beside a four-consumer seam paragraph that `-11` S3's shape change invalidates. Seven units
change recorded constraints; one updates the record. That is the map coverage ratchet passing while the
prose it exists to keep honest goes stale — the exact class §5 of the charter names. **Every surviving
unit that changes a recorded constraint refreshes the dossier in the same commit.** This is not
optional and it is a DoD item, not a nice-to-have.

Related: the dossier files the pin-direction guard as a **shared** follow-up (*"It would serve
`drift-audit` and `memory-tree` too … Related: `TOOL-aNumeralWarden-3`"*, live at
`memory/backlog/TOOL.md:64`). **No spec in this build mentions `aNumeralWarden` at all.** `-9` builds
600 lines of it privately inside `tools/lexicon/` and never answers the sharing question.

---

## 6. THE ORDERED FIX LIST

Apply in this order. Items marked **[blocking]** must land before the spec set is committed.

### Zero — outside the spec set

0.1 **[blocking]** `tools/memory-tree/gen_build_index.py`: apply `_wrap_ids()` (`:686`) to the joined
    id sentences at `:673` and `:678`. Do not raise `BUILD_README_ENTRY_CAP_CHARS`. Regenerate and
    re-run the hygiene gate in a clone with all specs staged. (B1)

### `-2`

2.1 **[blocking]** §2 S2 + §4: take the `LANGS` pair-level dark grammar into scope; delete the "No
    conf grammar change, so `lexicon_conf.py` and `subtokens.py` are untouched" sentence; add
    `lexicon_conf.py` to Files touched. State that `-6` S5 lands with or before this. (B4)
2.2 §2 S4: replace the four named conditions with "every member of `problems` at the point of the
    `measure_mode` return", naming none. (§3)
2.3 §6: delete AC6; remove `lexicon wiring` from §7's keeps-green claim or justify it.
2.4 §4: add one sentence — every `.lexicon.conf`-subject refusal in this build is invisible to a
    guarded local bar and binds at the push boundary, citing `.githooks/pre-push`'s **current**
    decision rule (`GATE_FULL_MAX_LAG=10`), not `kit.toml:49-51`'s retired claim.
2.5 §8 F2: either `-8` accepts the P3 FROM-side assertion or F2 records it as unowned.
2.6 §3: the `.ts`/`.tsx` bullet gains a cut argument or is deleted.

### `-3` — **recommended CUT.** If it survives:

3.1 **[blocking]** §2 S1 + §4 + F2: read `install.index` **and** `install.json` behind one
    role-normalising adapter. `.governance/install.json` exists in neither gov nor incms. (B3)
3.2 **[blocking]** §2 S5: drop the `--scaffold` refusal until a receipt exists to refuse against.
3.3 §2 S4: give the 25% cap a liveness statement (a run that excluded nothing says so) and name the
    remedy for an honest trip — a documented kit-constant raise with the measurement.
3.4 §4: add the three owed reciprocals — "unblocks `-8`'s probe corpus (soft)", "`-9` assert C grades
    at `FREEZE_SHA` under today's scoping, so rows in newly-excluded paths are deleted in this unit's
    commit", and the `-8` edge.
3.5 §4: name `af4de2d5` where 899 is quoted.

### `-4`

4.1 **[blocking]** §2 S6: rename `signal_lexicon_waiver_rows` → `build_lexicon_waiver_rows`. Then §7's
    "keeps `lexicon naming predicates` green" becomes true and no pin moves. (§3)
4.2 §4: add "the reader generalises to a shared keyset loader under `-9`; the key grammar does not
    move" — the `load_waivers` collision.

### `-5` — **recommended: cut S1, re-file S2–S4.** If it survives:

5.1 **[blocking]** §4:100-107 + S3: derive `was` from the file's **full** history, not `base..HEAD`.
    Walk newest-first past the contiguous present-run ending at HEAD and take the value at the newest
    commit where the key was present before it vanished. (B2)
5.2 **[blocking]** §6 AC2: restage with the deletion commit **before** the base — the only shape that
    reaches the branch. AC5's S4 arm is unreachable as written and goes with the S4 rewrite.
5.3 §4:129: "three new edges", naming `-7` — **or delete the paragraph if fix 7.1 lands**, which
    removes `-7` as a marker user.
5.4 §4: state whether S2's vanish arm or `-9`'s live-key assert fires first.

### `-6`

6.1 **[blocking]** §4 + S5: state which mechanism owns the LANGS-weakening question. Either supersede
    `TOOL-dUnstalledConvoy-35` in writing (its premise — a `dark` declaration cannot invalidate a
    curation — is refuted by `-6`'s own 42.9% → 7.9% measurement) or block on it. Then rewrite AC4 to
    assert against the **mode-ratchet finding specifically**, not against a clean report:
    `signal_lexicon_ratified_stale` fires on any `LANGS=` edit with or without the marker.
6.2 §2 S6: add the exogenous arm — every file an armed extractor found a definition in must also be
    seen by the sniffer. Stages by deleting one pattern.
6.3 **Recommended: delete S3 and S4** (the floor and its ratchet row). If kept: §4 states in one
    sentence that an incms-shaped adopter measures **48.8%** under this denominator, cites `-13` as
    the source, and clears 35 by 13.8 points.
6.4 §3/§4: fix the `-13` edge direction — one of the two is the input, stated identically on both
    sides.
6.5 §4:156: name `af4de2d5` where 899 is quoted.

### `-7`

7.1 **[blocking]** §4 + S5 + AC6: rename the signal to `build_lexicon_marginal_offense_rate`. `build`
    is row 1 of the table and two `SIGNALS` entries already use it. **Delete the pin move, delete
    AC6's `464`, delete the `463 -> 464` marker requirement.** [verified here] (§3)
7.2 §3: after 7.1, "No change to any predicate or pin value" becomes true. If 7.1 is refused instead,
    the pin move becomes S8 and §3 narrows to "no pin MECHANISM change".
7.3 §4: state that `extract_text` splits **here**, in Phase 0, and that `-9` and `-11` consume it.
7.4 §10: nine → **eleven** `derive_*` functions.
7.5 Add the stop-rule sentence: what reading of this signal kills the pressure chain.

### `-8` — **recommended SPLIT into `-8a` (S1-S5, S8) and `-8b` (S6-S7, Phase 0).**

8.1 **[blocking]** §4: `map_extractors.py` **does read** `VERBS` — `:135` registers `lexicon-verbs`,
    `:163` calls `load_conf(conf).get("VERBS").keys()`. Correct the consumer count and name
    `codebase-map coverage + freshness` in §7. [verified here] (§3)
8.2 §2 S8: seed `tsv::dark` alongside `conf::dark`, or the debt ledger reds a fresh adopter's first
    `git add` with `UNDECLARED EXTENSIONS: tsv`.
8.3 §8 F5: strike the `RESOLVED (agent…)` line. It is the only owner-declared fork in the set closed
    by the author; six others are left open and say so.
8.4 §4: the canon carries its own ratification line (reviewer + date), checked by the same non-empty
    rule `ratified` already uses. §12's law requires the human-curated mark and the kit already ships
    the mechanism.
8.5 §6 AC8: "every declared row", not "all 22 rows" — `-14` makes it 23. §4's "exceeds the canon by
    exactly two rows" becomes three.
8.6 §2/§4: state "unblocks `-10`'s `--suggest` replacement message" and "unblocks `-3`'s probe corpus
    (soft, per `-3` F2)". Add `lexicon skill wiring` to §7 and `SKILL.md` to Files touched, since S7
    edits eleven `VERBS` rows.
8.7 §4 or DoD: schedule the read-only `--probe` run against `C:/projects/incms/main`. The research
    made `-9`'s adoptability conditional on that number and nobody owns the reading.
8.8 §4/§7: spell the frozen-canon sentinel's predicate or drop it.

### `-9` — **recommended: DECIDE before scheduling.** If built:

9.1 **[blocking]** §2 S2 + §4 Migration + `kit.toml`: the shipped seed must be **empty**; gov's 459
    rows live at a path the `include = "**"` engine rule does not deploy; a `lexicon-freeze` hole
    replaces the deleted `lexicon-pins` hole. (B5)
9.2 **[blocking]** §3 + S5 + §4 Migration: **four** pin keys, the fourth arriving with `-11`. (B7)
9.3 **[blocking]** §2: add a sixth assert deriving the grandfather set at the previous commit and
    refusing any added row — the same `git show` machinery assert C already builds — **or** delete the
    shrink-only claim from §1 and state the honest bound (|offenders at `FREEZE_SHA`|, with absorbing
    capacity equal to the drain history).
9.4 **[blocking]** §6 AC8: delete it, or make the digest cover the payload (`sha256(body)` stored
    beside it and re-verified). As specced the digest covers only the inputs, so the poisoned payload
    is served.
9.5 §3 + §4: the multiplicity refusal is priced on gov (3 keys). incms has **113 keys with >1
    occurrence**, 183 excess occurrences, including `__getattr__`, which cannot be renamed. State the
    adopter cost or take the multiplicity field.
9.6 §2: add `scaffold_lexicon.py` to scope — it writes three `*_OFFENDER_PIN` keys this unit abolishes,
    and AC9's grep reds on it. Or `-8` S5 writes no pin keys at all.
9.7 §3: state that the F-A5 supersession (`-7`, per ruling `-17`) must land before this unit.
9.8 §4: state why a fixed-sha freeze read is **not** the second windowed base comparison `-6` §4
    forbids. It plausibly is not; nobody has written it down.
9.9 §4: delete the claim that `-5` owes a reciprocal — `-5` carries it four times.
9.10 §4: cite `-7` as the owner of the `extract_text` split rather than re-speccing it.
9.11 §5 + S9: state the freeze size as ≈380 (post-`-14`) **plus** the P6 count measured at `-11`'s
     landing, with the arithmetic. Three different numbers appear today.
9.12 §5: correct or delete "median 42 renames per commit" — measured median over 60 commits is 0.
9.13 §4: answer the dossier's shared-mechanism question (`TOOL-aNumeralWarden-3`) or say why this
     stays private to the lexicon kit.

### `-10`

10.1 **[blocking]** §8 F5: either promote the `PostToolUse` observer to an S-item with a design, a
     file, an AC and a §7 line, or strike it from F5 and let §5:250's unresolved line stand. It cannot
     be both `RESOLVED` in §8 and the owner scope menu in §5. (§3)
10.2 **[blocking]** §6 AC9: **64,361** of 64,512 and **48,794** of 49,152. §4's bullet table: 357 for
     the fifth bullet; the arithmetic uses 237, not 236; the delta is **−33**. [verified here] (B9)
10.3 **[blocking]** §4 Files touched + §7: claim `gate-legs: lexicon skill wiring` and
     `rendered-skills: lexicon` in the lexicon dossier in the same commit; add the
     `tools/govkit/subject-pins.tsv` row; add `gen_map.py --write` and `govkit.py selfcheck --write`;
     name `codebase-map coverage + freshness` in §7. (B8)
10.4 §6: add an AC staging the P3 RED — `import scaffold_lexicon` into `lexicon.py`, observe
     `UNSELECTIVE LAYERS RULE` naming the new row, unstage. AC10 alone cannot tell an armed rule from
     a dead one.
10.5 §4: add a `### Rollout`. The charter bullet claims a rendered Skill hands negatives to the author,
     which is false until S4 lands, so the charter edit cannot go first.
10.6 §2 S7: extend `tools/lexicon/README.md:73`'s four-step un-adoption procedure — this unit adds a
     committed artifact outside the kit home, two map keys, an `[[lf_pin]]` and a `.gitattributes` row.
     Copy `memory-recall`'s wording.
10.7 §4: name `af4de2d5` where 899 is quoted.

### `-11`

11.1 **[blocking]** §2 S1 vs §4: pick one granularity. S1 takes §4's wording ("the refusal fires only
     if the whole class goes empty"), and §4 states plainly that the class is arm-checked in aggregate
     and that `@cached_property` ships with an empty population. As written S1 reds on the landing
     commit twice over. (§3)
11.2 **[blocking]** §2 + §6: add an S-item and an AC asserting **P1's offender count is unchanged by
     the extractor rewrite alone**, with the measured before/after. Every downstream number in the
     build is quoted off today's P1 population and this spec never names P1. (§3)
11.3 §6 AC5: assert the offender delta is exactly **−26**, not merely "green"; add an arm asserting the
     exempted set equals a named enumeration, so a widening is a diff to the arm rather than a rising
     total nobody reads.
11.4 **Recommended: cut `SHORTNAME_OFFENDER_PIN`.** Ship P6 as a printed count plus the exemption
     class. If kept, F4 goes to the owner unresolved — it already is.
11.5 §3 + §5: B10. Either `-2`'s widened grammar declares `(.js, P6)` dark, or P6 registers outside
     `-2`'s roll-up with its liveness stated another way.
11.6 §5: add a **case table** for the rewritten helpers. The kit's own dossier records that a
     predicate's correctness concentrates in its helpers and that fixtures do not reach them — four
     blockers, none visible to 48 fixture arms.
11.7 §4: state the call-site inventory as of **this unit's landing**, not as of base — `-7` adds a
     fifth reader in Phase 0. Add the reciprocal edge to `-12` (P6/the classifier).
11.8 §8 F2: the `-19` narrowing is a re-reading of an owner ruling. R2 re-derived it and found the
     literal reading exempts **83 (19.9%)**, of which **37** are `t_`-prefixed — five times what `-11`
     writes. Strengthen the argument and surface it to the owner rather than closing it delegated.
11.9 §4: state that `-9` deletes **four** pin keys (the reciprocal half of B7).

### `-12` — **recommended DEFER.** If it survives:

12.1 §6 AC1: name the extractor the 0.716 reproduces against, and state that a post-`-11` run
     **re-baselines** rather than reproduces.
12.2 §4 K2: cite `TOOL-dScaffoldedMirror-11` as the classifier's owner, not ruling `-19`. Add the edge.
12.3 §6 AC7: re-phrase against `HEAD~1` at landing, not base `9ddcc5c9`.
12.4 §3: the demote-the-verb-table decision points at a §8 item that does not exist. Write F3 or drop
     the pointer.

### `-13` — **recommended: shrink to a `LEXICON.md` ruling.** If it survives:

13.1 **[blocking]** §6 AC5: observe `-13`'s own deliverable, not `-6`'s prose. The obligation on `-6`
     moves to §4 as a stated edge, and the figure becomes **48.8%** under `-6`'s
     definition-carrying denominator (19.3% is the tracked-file denominator `-6` §4 rejects). (§3)
13.2 §6 AC3/AC4: re-phrase against the named predecessor unit, not base — `-2`, `-9` and `-11` all
     rewrite those lines.
13.3 §4:109: fix the `-6` edge direction to match whichever way 6.4 picks.
13.4 §8 F3 is the unit's headline question and is unresolved. Either resolve it or say in §1 that the
     unit's product is a ruling on `.ts` only and adoption is out of scope.

### `-14`

14.1 **[blocking]** §2 S3: **write the `cmd` row's negative definition.** S3 and AC5 both require one
     and the clause is nowhere in the spec. (§3)
14.2 **[blocking]** §2 S6 + §7: claim `lexicon-verbs: cmd` in the map dossier; state that `MAP.md`,
     `inventories.json` **and** `symbols.json` all move (`symbols.json` also carries 51 `t_*` rows);
     name `codebase-map coverage + freshness` in §7. (B8's sibling)
14.3 §4: state the landing order — `-14` first, at 463 → 384 — and that `-11` expresses its move as a
     delta against that. With fix 7.1 applied, `-7` is no longer a claimant.
14.4 §4: state `cmd`'s admission order against `-8` S6's assert and `-9` ruling 1, or split S3 into a
     three-line contract landing before `-8b`.
14.5 §7: add `lexicon skill wiring` — S3 edits `VERBS` and the leg is deliberately unguarded.
14.6 §6 AC7: delete it. `refusal_join`'s population is `tools/govkit/*.py`; the renames are in
     `tools/memory-tree/`. Disjoint by construction.
14.7 §4: 58 → 59 references; `main`'s roster is 36 arms, not 34.

### `-15` — **recommended: SPLIT and re-file out of this build. S3 dies either way.**

15.1 **[blocking]** §2 S3 + §6 AC6: **delete both.** `check_runbook_parity.py` resolves `ROOT` off its
     own location, reads `tools/govkit/registry.toml`, and `registry.toml:218-220` exempts
     `tools/govkit` as never installed into a target. The leg cannot run in an adopter tree and AC6
     observes gov to certify a target. [verified here] (B6)
15.2 §4 Files touched: add the `tools/govkit/subject-pins.tsv` row for the new leg.
15.3 §8 F3 is answered by the split: `-15a` prose, `-15b` wiring.
---

## 7. WHAT I COULD NOT VERIFY

Everything below is asserted by a spec or by a single lens and was **not** independently confirmed by
this pass. Ordered by how much weight the plan puts on it.

**Nobody has run — and nobody can yet run — the measurement the research made `-9` conditional on.**
Research §5, Phase 2: *"Run `--probe` read-only against `C:/projects/incms/main` and read the report.
Its day-one ledger there is 6,482 rows, and that number decides whether R8 is adoptable at all."*
`--probe` does not exist; `-8` builds it. So the gate on the largest unit in the build is a
measurement that cannot be taken until two phases into the plan it is supposed to authorize. Three
different figures for that ledger circulate in the corpus — 6,482 (research), 6,566 (brief, `-9` §5),
6,569 (R2's own re-derivation) — and [verified here] incms has grown from 6,168 to **6,171** tracked
files since the brief was written, so all three are already stale by an unknown amount. **No unit
reconciles them.**

**R2's incms coverage measurement under `-6`'s denominator** — 1,136/2,328 = 48.8% wide, 1,134/2,058 =
55.1% narrow — is the number I used to overturn both convergence passes, and it was produced by one
agent. I confirmed the corpus shape that makes it structurally sound ([verified here] 3,401 `.md`,
1,170 `.py`, 626 `.ts`, 572 `.tsx`, 79 `.sh`, 20 `.js` of 6,171 tracked) and the arithmetic
reconciles, but I did not re-run the sniffer. **If the floor decision turns on it, re-measure.**

**R2's mechanical execution of `-14`'s 74 renames** — 211 references replaced, zero collisions in both
directions, five selftest suites PASS, pin landing at exactly 384 — is the evidence behind calling
`-14` the safest unit in the build. One agent, one clone. I verified none of it; I verified only that
`-14`'s `cmd` row reds the map ratchet, which R2 also staged.

**R2's staged measurements for `-11`** (an 8-method visitor lands the pin at 471, exits 1) and for
`-7` (the staged signal lands at 464), and R2's re-derivation of `-11`'s exemption populations
(83 zero-argument definitions under the literal `-19` reading, 37 of them `t_`-prefixed) are single-agent.
I verified the *inputs* — zero `visit_`/`generic_visit`, zero `cached_property`, three `@property` in
two files — but not the staged pin arithmetic.

**R2's "median 42 renames per commit does not reproduce"** (median 0 over 60 commits, using
`min(def-lines removed, def-lines added)` as a loose upper bound) uses a proxy, not a rename detector.
The direction is almost certainly right and the proxy over-counts rather than under-counts, so the
conclusion holds a fortiori — but the exact figure is not established either way, and `-9` §5's
original 42 is not sourced in the spec.

**`-9`'s own headline arithmetic** — 459 keys over 45 paths (37 `.py`, 8 `.js`), 463 occurrences, 3
multiplicity keys — reproduced exactly for R2 and was not re-run here. Likewise `-12`'s 824/589/418/47
and `CONSISTENCY = 0.716`, and `-3`'s 82.3% drain of the refused R2 rule.

**`-9`'s incms cost estimate** (~1 s batched read plus ~9 s parse on top of a ~4.7 s base) is an
extrapolation from gov constants, not a run. `-9` AC10's "over 1.5 s cold is a finding" is asserted
against a 0.44 s warm baseline that four other units in this build move, and **nobody has measured the
cumulative cost of the set** — `-2`, `-3`, `-6`, `-9` and `-11` each price against the same untouched
baseline.

**The behaviour of every new refusal in an actual adopter tree is unobserved, because there is no
adopter tree.** `-3`'s receipt reader and 25% cap, `-6`'s floor, `-9`'s five asserts and its seed, and
`-10`'s Skill-drift leg have all been reasoned about and none has been run anywhere but gov. B5's
conclusion (the seed ships gov's 459 rows) is derived from `kit.toml:16-18` and `govkit.py:2461` — I
verified the descriptor and the rule, **not** an actual `govkit apply` into a scratch target. Given
[verified here] that nothing has ever run `govkit apply` (incms was hand-wired by its own
`scripts/check_kit_sync.py` and carries `install.index`, not `install.json`), **the entire deployment
half of this build is untested by construction.** That is the largest single gap in the evidence base
and it is worth one scratch-target apply before `-9` or `-15` is scheduled.

**`-8`'s canon content** — twenty frozen clusters, cluster 20 = `test` with `t` non-first, cluster 14 =
`run` with `do` non-first — was checked for *consistency with `-14`* by a lens but the canon itself does
not exist yet, so its correctness is unverifiable by anyone until `canon.py` is written. The eleven
rows lacking a `NOT` clause were verified exactly (`add arm derive extract main measure print resolve
run seed test`).

**Whether the `-10` Skill-drift leg actually reds on a `VERBS` edit** cannot be observed — the leg does
not exist. The argument is sound and the consequence for `-8` S7 and `-14` S3 follows from the design,
not from a run.

**`-15`'s eighteen runbook sections** — the +20 KB, +300 lines estimate and the claim that the prose is
writable at all — rest on the spec's own count of seventeen unwired deployables. I confirmed the gate's
current output (18 problems, 7 anchored sections, 25 registry entries, 0 exempt, exit 1) via a lens and
verified that `WIRE-INTO-PROJECT.md` is 51,481 bytes with **no** row in either size-limit registry, so
the growth is ungated. I did not read the seventeen entries to judge whether their prose is writable
by one agent in one unit — which is precisely what F3 asks and leaves open.

---

*Report ends. Fix list in §6 is ordered for a single application pass; the cut list in §5 is a
decision for the owner and should be taken before §6 is applied, since roughly half of §6's items sit
in units §5 recommends cutting.*
