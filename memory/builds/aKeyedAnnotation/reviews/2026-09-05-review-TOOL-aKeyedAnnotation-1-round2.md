**Serves:** spec-audit TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# aKeyedAnnotation — Tier-2 spec audit, round 2

Node `a` · streams `tooling` · 2026-09-05 · adversarial fan → skeptic refutation → synthesis, per `memory/guides/REVIEW-PROTOCOL.md`. Round 1 was BLOCKED on 12 distinct defects; all twelve have been folded, plus a follow-up commit closing four other-halves the fold left standing. **The fold is what this round measures** — the folded prose is fresh and unreviewed by construction, and it is where most of what follows lives.

**Reviewed at:** `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-1.md@eb99290d675367b0732d853070bcc657bee5b720` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-2.md@1973c62f107046dea9500f8c9b053213a68854c9` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-3.md@6493e04e11621510f38fbeece2f0bdad85f390d1` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-4.md@73bf178fc91c0017288b3d4e952a216f375a4c0f` · ROUND 2

## Verdict: BLOCKED

Two defects block, both in unit `-1` and both created by the fold rather than survived by it. B1 is a scope bound that guarantees a red bar against a criterion demanding a green one: the unit lands two new files under glob-derived codebase-map inventories and §4 forbids the carrier that would claim them. B2 is an acceptance criterion that passes green on precisely the violation it was written to catch, while naming a figure the command it invokes does not print — round 1's B1 class, reproduced in the text written to close round 1's B1 class.

Nothing here argues against the build's shape. The design pass's refusals still hold, no finding asks for a new grammar, marker, source-side gate, recall entry or tokenizer change, and unit `-2` — the most heavily folded of the four — came out of this round with one stale sentence and one adopter-reach gap and nothing structural.

The recurring shape this round is narrower and more specific than last round's: **the fold repaired one half of a statement and left the other half standing.** Six of the fifteen defects below are literally that (H1, H2, H3, H7, H8, M2), and three of those six are a sentence pointing at a correction that was never made. The repo already keeps a gotcha record for this class; it is now the dominant class in this build's own records.

## Review shape and run integrity

- Raw findings 37 · confirmed 23 · refuted 14 · unverified 0 · precision 0.62.
- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the pipeline. **The run is complete**: every lens and every skeptic batch came back, so a zero count anywhere in this report is a measured zero and not an absence of coverage.
- Precision 0.62 clears the ~0.5 floor §8 names, and is up from round 1's 0.34 on half the raw volume. Read that as the round-1 record doing its job as priming: the lenses spent their budget on the folded text instead of re-deriving the spec set.

**Convergence.** The 23 confirmed findings describe **15 distinct defects**; this record collapses them and names the contributing raw ids on each row. Three lenses independently found unit `-4`'s F1/S3 contradiction and two found unit `-3`'s missing ratchet row from opposite directions. Convergence is a severity signal, not extra findings, and the table counts defects.

## Findings

| # | Severity | Unit | Address | Defect | Raw ids |
|---|---|---|---|---|---|
| B1 | blocker | `-1` | §4 Rollout, §2 S7 (against §6 AC6) | Two new files mint unclaimed codebase-map inventory keys, so the bar reds and §4 forbids the only carrier that fixes it | 23 |
| B2 | blocker | `-1` | §6 AC9 | AC9 is green on the violation it exists to catch, and names a figure its own command never prints | 31 |
| H1 | high | `-1` | §2 S7, §4 Rollout | S7 says THREE declaration carriers; there are four, and the missed one is the guard that ships to adopters | 10 |
| H2 | high | `-1` | §6 (all criteria) against §2 S7 | Only the `PAIRS` row is observed; no criterion reads the descriptor stanza or either guard | 1, 18 |
| H3 | high | `-2` | §4 Migration against §2 S4, §6 AC4 | The sentence the fold rewrote S4 to repudiate still stands verbatim four sections away | 11, 25 |
| H4 | high | `-3` | §2 S4, §4 Rollout, §8 F2 | A shrink-only pin with no ratchet row is the comment unit `-4`'s S8 says it is | 13, 26 |
| H5 | high | `-3` | §10 Reuse audit, §4 Inventory, §8 | The declared seam is a cross-kit import that raises for adopters and takes the whole gate leg down | 27, 32 |
| H6 | high | `-4` | §2 S3, §6 (no criterion) | S3's adopter half names no carrier, states no unset-pin behaviour, and has no criterion | 4, 29, 34 |
| H7 | high | `-4` | §8 F1 against §2 S3 | S3 points at a correction in §8 that was never made, and F1's stated verification is false | 16, 28, 30 |
| H8 | high | `-4` | §5 against §3 | The fold's bound on a second copy-installed kit cites a non-goal that does not exist | 15 |
| M1 | medium | `-3` | §2 S3 against §6 AC3 | Two declared liveness counts, one observation — and the unrun half is the unit's own stated hazard | 5 |
| M2 | medium | `-3` | §2 S4 against §8 F2, §4 Rollout | Scope says "tolerance pin"; the resolved fork rejects the tolerance form by name | 21 |
| M3 | medium | `-2` | §2 S2 against §5 | Adopters receive an empty row and the unnarrowed oracle, while the kit README advertises the correction | 20 |
| M4 | medium | `-4` | §5 against §6 AC8 | The "permanent" portability arm is a one-off scratch-tree run wired into no self-test | 8 |
| L1 | low | `-1` | §7 | Four leg names typed under a sentence saying none is typed, and one of the four does not exist | 22 |

Unit `-2` drew two defects, both repairable in a sentence. Unit `-3`, which drew **no** confirmed finding in round 1 and is the only unit still at rev-2, drew four here — including one high and one that ships an adopter-visible break. That is the answer to round 1's own caveat: its zero on `-3` was one round finding nothing at precision 0.34, not a certificate, and folding the other three specs moved the standard `-3` is now measured against.

---

## B1 — BLOCKER · `TOOL-aKeyedAnnotation-1` §4 Rollout ("Nothing BEYOND those changes"), §2 S7, against §6 AC6

The unit lands a new file under `memory/guides/` (the rendered annotation convention) and, per §5, a new bug-class record under `memory/gotchas/`. Both directories are **glob-derived codebase-map inventories**: `tools/codebase-map/map_extractors.py:119` derives `guides` by globbing `memory/guides/*.md`, and `gotcha-classes` is the same shape one line over. Every new key in either must be claimed by a dossier, because `memory/map/baseline.toml` has `guides = [ ]` empty under a header stating the file only SHRINKS and "New keys belong in a dossier, not here".

`test_every_inventory_key_is_claimed_or_baselined` asserts `cov.clean`, and it is the `codebase-map coverage + freshness` leg — the leg §7 of this spec itself calls load-bearing and AC6 demands green. So the unit as scoped reds the bar twice, and the two sanctioned escapes are both closed: the baseline only shrinks by its own convention, and §4's "Nothing BEYOND those changes" forbids the dossier claim and the regenerated map artifacts that would actually fix it.

A builder reaching this has an obvious correct move — claim both keys in a dossier, precedent `memory/map/features/build-method.md`, which already claims `guides = ["BUILD-METHOD.md"]` and globs both the template and the rendered copy — and a spec telling them not to. That is the round-1 B2 shape: a scope bound and a criterion that cannot both hold.

**Fix.** Add a carrier to S7: the dossier claim, naming `memory/map/features/build-method.md` as the precedent for the template/rendered pair, requiring the same pair for the new guide and a claim for the new gotcha-class record, and requiring `memory/map/generated/` regenerated in the same commit. Delete or qualify §4's "Nothing BEYOND those changes" so it does not forbid the thing AC6 requires.

**Left-shift.** The gate already exists and would have caught this at the first commit; what failed is that the spec was written without asking it. File a bug-class row so `python tools/memory-tree/gotchas.py --for-diff` selects it on any diff touching `memory/builds/*/spec/`: *a scope item adding a file under a glob-derived map inventory owes a dossier claim and a regen in the same commit, and any "nothing else changes" clause in the same spec must say so.* The charter's DoD already states the rule; the spec population is where it is not being read.

## B2 — BLOCKER · `TOOL-aKeyedAnnotation-1` §6 AC9

AC9 names `python tools/memory-tree/corpus_ids.py --report` as "the observation that proves S4's prose-only constraint was actually honoured". It cannot observe either half of the violation.

Run at this base, `--report` prints exactly six labelled lines — ids defined 967, ids cited 967, orphan ids 0 `[]`, build collisions 0 `{}`, dead path cites 0, read path — plus the read-path file list. `cmd_report` (`corpus_ids.py:681`) emits **no per-build definitions set**, and neither does `--measure`, which prints only the two pins. AC9's second clause therefore asserts on a figure the named command does not produce, and the printed totals are no substitute: this build lands records that move `ids defined` for unrelated reasons.

The first clause is worse. S4's fatal case is a foreign id in the backlog row's **head**, which anchors and therefore DEFINES it — `A_DASH` is one of the anchor patterns `anchor_at` matches (`tools/memory-recall/extract.py:415`), so a head-anchored id lands in `defs` and the orphan count stays 0. `def_builds` is populated only for paths under `builds/`, so the collision line stays 0 too. AC9 passes green on precisely the violation it exists to catch, leaving only the body-citation case observable.

This is the criterion shape this same spec's §5 left-shift row was written to gate — "must assert on the field that command actually moves" — reproduced in the text the fold added.

**Fix.** Replace AC9 with a criterion over a set the command actually derives. Assert that `git grep -o -E "[A-Z]+-<foreign-slug>-[0-9]+[a-z]?" -- memory/ | sort -u` is byte-identical before and after the row lands, which catches the head case, and keep the orphan count at 0 as the separate body-case guard — naming which clause catches which failure, since a criterion covering two failure modes with one number covers neither.

**Left-shift.** Extend the existing "citing a dangling id creates it as an orphan" gotcha record with the observation side: *head-anchored ids do not show up as orphans, so an orphan count is not an observation of a prose-only constraint.* This is the second time in two rounds that this spec set has written an AC against a `corpus_ids.py` field that does not move; the checklist row is cheaper than the fourth gate.

## H1 — HIGH · `TOOL-aKeyedAnnotation-1` §2 S7 and §4 Rollout

S7's folded sentence reads "A rendered memory-tree guide is declared in THREE carriers beyond the render line, and all three are in scope." The tree says four. `tools/memory-tree/kit.toml` carries both a `[[files]] role = "rendered"` stanza (the one S7 names) **and** a separate `[[gate_leg]] name = "kit/dogfood doc parity"` block whose own `guard` lists `{memory_root}/HYGIENE.md`, `{memory_root}/TEMPLATE-SPEC.md`, `{memory_root}/guides/BUILD-METHOD.md` and `{kit}/`. That descriptor guard is a fourth carrier, distinct from the manifest guard at `tools/gate-legs.json:279-285` that S7 does name.

The comment sitting directly under that descriptor guard is the one S7 cites as its precedent, and it says in terms: "TWO carriers, because govkit copies a descriptor's declared guard verbatim into a target: fixing gov's manifest alone would leave the half that SHIPS open, and the hole would be exported rather than fixed." S7 patches gov's manifest alone. Every adopting tree then installs a parity leg whose guard omits the new guide, and the leg skips on any scoped run in which only that guide changed — the exported hole, from the record that closed it. S7's own framing, "a documented failure repeated rather than a novel one", is literally true of S7.

**Fix.** S7 names four carriers and puts the `[[gate_leg]]` guard in `tools/memory-tree/kit.toml` into the write set beside the `[[files]]` stanza. §4 Rollout's "plus the three declaration carriers S7 names" moves to four.

**Left-shift.** Take round 1's H1 left-shift, which was declined: derive `PAIRS` **and** both guards from `kit.toml`'s `role = "rendered"` stanzas. Adding a stanza then registers the pair and both guard rows automatically, four carriers collapse to one, and the class cannot recur in this kit or in any kit that copies the pattern.

## H2 — HIGH · `TOOL-aKeyedAnnotation-1` §6, against §2 S7

Of S7's declared carriers, only the `PAIRS` row is observed, and the fold that added AC7 did not close the rest.

- **AC1 cannot see the descriptor stanza.** `adopt-memory-tree.sh:93` renders BUILD-METHOD from a hardcoded `if [ -f … ]; then render_doc` line, not from the descriptor, so the render happens with or without a `role = "rendered"` row and the new template is swallowed by the `include = "**" / role = "engine"` catch-all at `kit.toml:21-22`. AC1 passes either way, and the template then ships to adopters with no render destination.
- **AC6's green bar cannot see it either.** `govkit` walks only rows whose role is already `rendered` (`govkit.py:4718-4735`) — declared-then-present, never present-then-declared — and `check-kit-placeholders.py` states in its own header that it asserts one direction only, declared ⊆ substituted. An absent stanza declares nothing and reds nothing.
- **AC7 bypasses the guards.** It invokes `kit-dogfood-parity.test.sh` directly, so the manifest guard is not exercised; and that guard already names `tools/memory-tree/`, so on this unit's own commit the leg fires whether or not the new rendered path joins it. The omission only bites later, on a diff that touches the guide alone.

Two of the four carriers from H1 can therefore be omitted with every criterion green, on a unit whose whole justification is that this exact miss is documented.

**Fix.** Cheapest and preferred: take H1's left-shift, derive the pairs and guards from the descriptor, and AC7's single observation then covers all four carriers. Failing that, add one criterion per unobserved carrier — deleting the stanza makes an adopt/govkit run REFUSE, and a diff touching only the rendered guide produces a leg-selection run that INCLUDES `kit/dogfood doc parity`.

**Left-shift.** The general form is a bar leg: for every kit descriptor, assert `present-then-declared` as well as `declared-then-present`. A catch-all `include = "**"` that silently claims a new template is a green-by-absence machine, and it is one leg away from being impossible.

## H3 — HIGH · `TOOL-aKeyedAnnotation-2` §4 Migration, against §2 S4 and §6 AC4

§4 Migration still opens "The population moves under each of S1, S2 and S3." That is the exact wording S4's fold identifies as the defect it repairs — "which is how the earlier wording here, that each step moves the population independently, would have been read" — and replaces with "S1, S2 and S3 are each expected to move the value by ZERO on this corpus". AC4 refutes it a third way, in the spec's own vocabulary: "the judgeable population counts non-terminal keyed specs and nothing done to annotations touches it."

So the document gives two answers to "what should the three readings show", and under its own terms §4 Migration is false on the literal reading (population cannot move) and contradicts S4 on the colloquial one. A builder taking three identical readings after S1, S2 and S3 has one clause calling that the confirmed result and another calling it evidence the change did not work — the misreading S4 was folded to prevent.

**Fix.** Rewrite the Migration paragraph's first sentence in AC4's vocabulary: the one-change-one-measurement-one-recorded-line order stands, the expected movement of the **value** under each of S1, S2 and S3 is zero on this corpus, three identical readings are the confirmed result, and the discipline exists so an UNEXPECTED movement is attributable — not because movement is expected.

**Left-shift.** Same bug-class row as H7 below, and this is the cheaper of the two instances to catch: *a fold that rewrites a claim greps the spec for the claim's other copies before it is done.* One `git grep` over the file for the repudiated phrasing would have caught both.

## H4 — HIGH · `TOOL-aKeyedAnnotation-3` §2 S4, §4 Rollout, §8 F2

Unit `-3` declares a shrink-only pin whose only carrier is §4's "one pin row". Nothing in drift-audit enforces that. `drift_report.py:1580` computes `over = [s for s in out if s["gateable"] and s["live"] and s["value"] > s["pin"]]`, and rc is `1 if (over or dead or ratchets) else 0` — a signal declared `gateable: False` (S4) can never be in `over` or in `dead`, and the summary only prints "out of tolerance (report only)".

The sole enforcement for such a pin is a `RATCHETS` row, and the kit says so in prose beside the one existing report-only pin: `live_backlog_rows_per_shard` carries "the signal is `gateable: False` so crossing it never blocks a merge. What it buys is that RAISING it lands in RATCHETS below", with its row at `tools/drift-audit/drift_signals.py:288`. `RATCHETS` is an explicit opt-in list (`:279-290`) — sibling PINS keys such as `lexicon_ratified_older_than_language_surface` carry no row — so a new pin is unratcheted by default.

Unit `-3`'s inventory is "One signal function, one registry row, one pin row, two self-test arms", with no ratchet row anywhere in the spec and no criterion observing a raise. So the new pin can be raised silently in the same commit that raises the population, §4's "a drain target from the first commit rather than a permanent tolerance" does not hold, and F2's whole ground for rejecting the tolerance form rests on a property nothing ships. Sibling unit `-4` spends S8 and AC9 on exactly this rule, in the same kit, in the same build: "SHRINK-ONLY NEEDS A MECHANISM, and naming it in a comment is not one."

**Fix.** Add a scope item landing `{"file": "tools/drift-audit/drift_signals.py", "key": "<new signal name>", "weakens": "up"}` in `RATCHETS`, list it in §4's Inventory, and add the AC pair unit `-4` uses: a raise with no `<old> -> <new>` marker REDS `drift_report.py --check`, and passes with one. Or drop the shrink-only language from S4 and §4 and say plainly that the pin is a recorded reading no gate enforces — but F2 must then be reopened, since that is the option it rejected.

**Left-shift.** Machine-checkable and cheap: a bar leg asserting every PINS key declared shrink-only in prose has a `RATCHETS` row. The declaration is already in the module; the row is already in the module; nothing currently joins them.

## H5 — HIGH · `TOOL-aKeyedAnnotation-3` §10 Reuse audit and §4 Inventory, no fork in §8

Unit `-3`'s declared seam is "the definitions map plus id grammar already built by `tools/memory-tree/corpus_ids.py`". That is a cross-kit import from drift-audit into memory-tree — the exact boundary question unit `-2`'s F1 exists to resolve — and unit `-3` carries no resolution, no fallback and no fork.

`tools/drift-audit/drift_report.py` imports stdlib only and says so at its head ("NO SECOND CONF … This kit declares no conf of its own"), deliberately **copying** `map_lib.load_conf` rather than importing a sibling kit. Unit `-2`'s F1 resolved this class for the id grammar with option (a) — import when importable, fall back to a local copy the kit self-test byte-compares — after ruling out (c), a shared cross-kit location, as a contract change needing its own design pass. Unit `-3` lands one unit later into the same module and reaches straight for `corpus_ids`' definitions map with none of that.

It is also the worse edge. `walk()` (`corpus_ids.py:361`) opens `E = grammar(root)` unconditionally, and `grammar()` (`:258`) raises `Problem` when `tools/memory-recall/extract.py` is absent — the raise is not gated on the pins, only its message assumes it. Line 370 then calls `ask_shell("--print-append-only-ere", root)`, shelling out to `check-memory-hygiene.sh` through `resolve_bash()`, itself a named-Problem path on a node where no bash resolves. `tools/drift-audit/kit.toml` declares `requires = ["memory-tree"]` and no memory-recall edge, while `tools/memory-tree/kit.toml` puts memory-recall behind `requires_if … when_any_key_set = ["DEAD_PATH_PIN", "ORPHAN_ID_PIN"]` with its own comment noting the edge is FALSE at apply time "because the pins ship blank". The adopter configuration drift-audit's own `requires` permits is precisely the one where `walk()` raises.

The blast radius is larger than a missing signal. `main()` evaluates every signal in one unguarded comprehension — the module's own `_load_lexicon` docstring says an exception there "kills all eight and takes the `--check` gate leg with it" — so an unguarded `corpus_ids` call takes down `drift-audit records` for that adopter rather than producing the dead-signal report S3 promises. The kit already carries the correct idiom: the lexicon signals' try/except plus `not_asked`, whose docstring calls itself "the ONLY place this shipped engine names an optional kit". Unit `-3` names neither the idiom nor the fork.

**Fix.** Add a §8 fork adopting unit `-2` F1's resolution **by reference** rather than re-deciding it, and state in §2 how the definitions map crosses the boundary — import-when-importable with a byte-compared local fallback, or rebuild the map inside drift-audit from the grammar unit `-2`'s S1 already binds. Declare the dependency in §4's Inventory, add the memory-recall edge (or a `requires_if`) to `tools/drift-audit/kit.toml`, and add a criterion running the report in a scratch tree with memory-recall absent and blank pins, asserting the signal reports itself DEAD rather than raising.

**Left-shift.** A self-test arm in `tools/drift-audit/selftest.py` that runs `drift_report.py --check` in a scratch tree holding drift-audit and memory-tree and nothing else. Any future signal that reaches for an unrequired kit reds on the arm rather than in an adopter's bar.

## H6 — HIGH · `TOOL-aKeyedAnnotation-4` §2 S3, and §6 (no criterion)

S3's adopter half — "an adopter scaffolding the kit gets the row with no value" — names no carrier, states no behaviour, and has no criterion.

The carrier is `tools/codebase-map/.codebase-map.conf.example`, which `adopt-codebase-map.sh:142-143` copies to the adopter's repo root. No §2 item names it: S1 through S8 speak to gov's own tree, the test-module pair, `gen_map.py` and `drift_signals.py`. Every §6 criterion runs against gov — AC2 measures this repo, AC4 measures an empty map root, AC10's `cmp` covers only `test_codebase_map.py` against its template, and nothing on the bar compares the conf to its example. This is the identical "the fix lands in the dogfood copy only" class the fold closed one file over in S2/AC10 and unit `-2` closed with its own AC10.

The unstated behaviour is the sharper half. `map_lib.load_conf` (`map_lib.py:180`) yields `""` for a bare `KEY=` and omits the key entirely when the row is absent, so the check meets `KeyError` or `int("")` before it meets a number. `test_codebase_map.template.py` reads no conf key today (only `m.map_root()`), and `tools/codebase-map/selftest.py` execs that template from scratch trees carrying no `.codebase-map.conf` at all (`:252-262` creates only `.git` and stub kit files) — so a module-level pin read that refuses on a missing key breaks the kit's own self-test. S4 keeps a scaffolded dossier's `decisions` empty, so a fresh adopter's dossiers are all empty: a missing pin read as 0 reds their first gate run, and read as a silent skip makes the check the vacuous selector §4 says it is closing. A third behaviour exists and is the repo's own idiom — report the count as ungraded and say so, the `not_asked` / `DECLARED_EMPTY` shape — which is why this is a specification gap rather than a forced choice between two bad defaults. Meanwhile §5 ships a kit-README line claiming the field is graded.

**Fix.** Name `.codebase-map.conf.example` in S2's write set beside the test-module template, with the row carrying an empty value and a documentation comment. State the absent/empty-pin behaviour in S3 explicitly: report ungraded and announce it, never a bare 0 and never a red. Add an AC running `bash tools/codebase-map/adopt-codebase-map.sh` into a scratch adopter tree and then the installed gate with the pin unset, asserting the declared report rather than a traceback or a perfect score.

**Left-shift.** Generalize the seed/target parity leg round 1's H2 already proposed to cover `.example` conf files: for every kit, every key the shipped code reads from the conf appears in the conf example. That kills this class for the whole kit population, not just this pin.

## H7 — HIGH · `TOOL-aKeyedAnnotation-4` §8 F1's resolution, against §2 S3

S3's folded correction reads: "The kit conf carries no other measured pin today, so this is the first rather than one more of a set, and an earlier draft claiming otherwise is corrected in §8." §8 F1 still reads: "Verified at this base that the file exists and already carries this kit's other measured pins."

The correction S3 announces was never made, and the tree sides with S3. `.codebase-map.conf` holds `MAP_ROOT`, `GATE_FILE`, `MAP_DIFF_CMD`, `RECALL_DARK_LAYERS`, `CLONE_COUNT_FILE` and `SEAM_FANIN_THRESHOLD=3` — the only number among them, carrying its own comment "Kept at the kit default of 3 — this is a small tree and the threshold has not been re-measured against it", which is the definition of not-measured.

A fold that points at a correction that is not there is worse than no fold: the false premise still stands, still wears a "Verified at this base" stamp, and is now certified as fixed by the sibling section. F1's ranking of (a) over (b) is argued partly from it, and a builder reading §8 goes looking for an existing measured-pin idiom in that file to copy and finds none. The outcome (a) survives on its other stated ground — the kit is copy-installed, so its pin must travel with it, and (b) would create a cross-kit read an adopter without memory-tree could not satisfy — so this is a false stated ground and a dead pointer, not a wrong resolution.

**Fix.** Rewrite F1's RESOLVED clause to rest (a) on the surviving reason alone, delete the "already carries this kit's other measured pins" clause, and state that this is the conf's FIRST measured pin — matching S3, which is why S3 spells out that an adopter gets the row with no value.

**Left-shift.** The bug-class row H3 shares: *a fold that rewrites a claim greps the whole document for the claim's other copies, and a sentence asserting "corrected in §N" is not done until §N is read.* Three of this round's fifteen defects are this exact shape (H3, H7, M2) and the repo already keeps an `amendment-leaves-its-other-half-standing` record — extend it with the spec-fold disposition rather than minting a second one.

## H8 — HIGH · `TOOL-aKeyedAnnotation-4` §5 testing + left-shift gates, against §3

§5's folded sentence reads: "Note that S8 puts a second kit, `tools/drift-audit/`, into this unit's write set; §3's non-goals bound what may change there to the one ratchet row." §3's five non-goals are: no annotation in code, no `map_lib` tokenizer/stripper change, no new generated artifact, no bulk backfill, no dossier-schema change. None mentions drift-audit or bounds anything in it.

So the fold closes the missed-second-kit finding by asserting a control that does not exist. A reviewer checking §3 for the named limit finds nothing, and the write set into a second copy-installed kit is in fact unbounded. The bound that does exist lives in S8 — "This unit lands that row naming the kit conf and the new key" — which is not where the fold sends a reader. The citation is the only thing standing between this unit and edits to the drift-audit signals module.

**Fix.** Add the non-goal to §3 verbatim — "No change in `tools/drift-audit/` beyond the single `RATCHETS` row S8 names" — and leave §5's sentence pointing at it.

**Left-shift.** Cheapest available: extend `tools/check-spec-tokens.py`, which already walks the spec population, with a cross-reference check — a spec sentence citing "§N" must find its claim's subject in §N. It is a substring join, not a semantic one, and it would have caught this and H7 in the same pass.

## M1 — MEDIUM · `TOOL-aKeyedAnnotation-3` §2 S3, against §6 AC3

S3 declares TWO liveness counts — known slugs and scanned source files — and AC3 exercises only the empty-memory-root case, which empties the slug set while tracked source outside the memory root is untouched. No other criterion reaches the file-set half: AC1 and AC2 assert the healthy state and the discriminator, AC4 the family enum, AC5 the orphan count, AC6 the bar.

The unrun half is the one covering the unit's own stated hazard. §5 risks says "a false zero from an empty population is the whole hazard", and a source walk that resolves to no tracked file leaves the slug set full and live while the finding count falls to zero — the reassuring zero wearing a live flag, which is round-1 H4's class. Sibling unit `-2` was folded to carry exactly this observation (AC8, emptying the declaration to see the signal report itself DEAD, observed RED against pre-change code). One build, two liveness disciplines for one class.

**Fix.** Add an AC mirroring unit `-2`'s AC8: in a scratch tree where the signal's source walk resolves to no tracked file, `python tools/drift-audit/drift_report.py --check` reports the signal DEAD rather than zero findings — observed, and wired as the second self-test arm beside S6's two.

**Left-shift.** Already a charter rule ("a probe that cannot move says so") and already a drift-audit convention; what is missing is one arm per declared count. Make it structural in the kit: a self-test that enumerates every signal's declared liveness counts and refuses one with no arm.

## M2 — MEDIUM · `TOOL-aKeyedAnnotation-3` §2 S4, against §8 F2 and §4 Rollout

S4 specifies "Report-only, with its own tolerance pin". F2 — which explicitly treats the two as distinct shapes, "Its siblings use two forms, a tolerance and a shrink-only pin" — RESOLVES to shrink-only, and §4 Rollout independently calls the pin "a drain target from the first commit rather than a permanent tolerance", i.e. explicitly not a tolerance.

Scope and resolved fork name different artifacts in the one spec that was not folded, and §6's AC1–AC6 contain no criterion that distinguishes a tolerance from a shrink-only pin. A builder reading §2 first wires the shape §4 and §8 both refuse and hits nothing until the fork's own text is re-read.

**Fix.** Change S4 to "with its own shrink-only pin" and point at F2, so scope, rollout and the resolution give one answer. H4's ratchet row is what makes that answer true.

**Left-shift.** Shares H7's row. Note also that this defect exists because `-3` was never folded: rev-3 and rev-4 reconciled exactly this class in the siblings.

## M3 — MEDIUM · `TOOL-aKeyedAnnotation-2` §2 S2, against §5 user docs

S2 justifies the second carrier purely by adopter reach — "every copy-installed drift-audit would keep the self-certifying oracle this unit exists to correct while the kit README advertises the correction" — then specifies "The template row ships EMPTY, and the reader takes the name with getattr-and-fallback to the product globs." An empty row falling back to `PRODUCT_GLOBS` hands the adopter the unnarrowed oracle, which is the outcome S2 says it exists to prevent, while §5 has the kit README record the correction as shipped.

The kit's own descriptor proves this is a named class rather than a preference. `tools/drift-audit/kit.toml` carries `[[hole]]` entries with `blocks_adopt = false, blocks_gate = true` for exactly this shape — `drift-product-globs` and `drift-trace-cutoff`, the latter worded "correct on day one, and permanently inert if nobody ever fills it" — each with a discharge probe. This unit declares none, so the precedent it claims to follow is followed halfway: adopters get the declaration and no forcing function to fill it.

**Fix.** Either add a `[[hole]]` for the new declaration in the kit descriptor and name it in S2, or amend S2 and §5 to say adopters receive the DECLARATION and its documentation block while the correction itself lands only in this repo — so the README line does not overstate what a fresh install gets.

**Left-shift.** The hole mechanism already is the left-shift; what is missing is the reflex. Bug-class row: *a seed row that ships empty and falls back to the old behaviour is a hole, and it declares one or the README does not get to claim the fix.*

## M4 — MEDIUM · `TOOL-aKeyedAnnotation-4` §5 testing + left-shift gates, against §6 AC8

§5 claims "the portability arm AC8 makes permanent". AC8 names only `reuse_lookup.py` run in a scratch tree with the project-side extractor removed — a one-off build-time observation. It never names `tools/codebase-map/selftest.py`, which is a real bar leg guarded on `tools/codebase-map/`, and no scope item S1–S8 puts an arm there.

Round 1's H6 left-shift reads verbatim: "it should be a permanent selftest arm rather than a one-off observation." AC8's own closing line — "a declared property with no arm asserting it is a comment" — condemns what AC8 specifies. The sibling shows the difference: unit `-2`'s AC9 names `python tools/drift-audit/selftest.py` outright. As written, the module's declared portability is verified once at build time and unguarded afterwards, and the next edit to `reuse_lookup.py` can end it silently. The same gap sits behind AC10's one-shot `cmp` of the dogfood/template pair, which §5 does not list at all.

**Fix.** State in S1 that the arm lands in `tools/codebase-map/selftest.py` — and, since that module ships as a pair, in the copy adopters receive — and reword AC8 to observe the arm: `python tools/codebase-map/selftest.py` runs the project-layer-removed case, exits 0, and has been observed RED with the decisions line reading the parsed dossier. Add the pair comparison to §5's left-shift list, or say plainly that AC10 is a build-time check with no durable guard.

**Left-shift.** This is itself the left-shift, declined once. If it is declined again, §5 must stop claiming permanence — the claim, not the arm, is what makes this a defect rather than a preference.

## L1 — LOW · `TOOL-aKeyedAnnotation-1` §7

§7 types four leg names and then says "Read the manifest for the names; none is typed here" in the same breath. The sentence refutes itself, and one of the four names is wrong: `tools/gate-legs.json` has no leg called `kit versions`; the leg is `kit version markers` (`gate-legs.json:128`). The other three — `memory hygiene`, `codebase-map coverage + freshness`, `drift-audit records` — are exact.

So the one name a reader would grep for returns nothing, and the section's own advice is the only usable half of it.

**Fix.** Either drop the four names and keep the pointer, or keep the names, correct `kit versions` to `kit version markers`, and delete the "none is typed here" clause. Not both.

**Left-shift.** `tools/check-spec-tokens.py` already walks the spec population; a join asserting that any backticked string in a spec that looks like a leg name resolves in `tools/gate-legs.json` is a few lines and covers every future spec. Same file as H8's cross-reference check, same pass.

---

## What the fold got right

Worth recording, since the table is a list of what it did not. Unit `-2`'s AC4 — round 1's B1, the drainability proof asserting on the wrong field — came back correct, with the operation named and the field split from the population. Unit `-1`'s S4 backlog row now carries the prose-only escape round 1's B2 said was missing; only its observation (B2 above) is broken, not its constraint. Unit `-4`'s S2 now names the template as the write target and AC10 compares the pair. Unit `-2`'s S2 reached the seed file, and its AC8 is the cleanest liveness criterion in the set — good enough that M1 is written by pointing at it.

## Recommended order

B1 and B2 first: both are unit `-1`, both are cheap, and both are unsatisfiable-as-written rather than merely wrong. H1 and H2 then collapse into one edit if the derive-`PAIRS`-from-`kit.toml` left-shift is taken, which is the single highest-value change available in this round. Unit `-3` needs a rev-3 of its own — H4, H5, M1 and M2 are four defects in the one spec that has never been folded, and H5 in particular should not land as scoped.
