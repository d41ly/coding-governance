**Serves:** spec-audit TOOL-aKeyedAnnotation-1 TOOL-aKeyedAnnotation-2 TOOL-aKeyedAnnotation-3 TOOL-aKeyedAnnotation-4

# aKeyedAnnotation — Tier-2 spec audit, round 1

Node `a` · streams `tooling` · 2026-09-05 · adversarial fan → skeptic refutation → synthesis, per `memory/guides/REVIEW-PROTOCOL.md`. Subjects are the four unit specs plus the fork resolutions committed immediately before this base, which were fresh and unreviewed and are in scope.

**Reviewed at:** `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-1.md@2f713a8f35e2a216e1b9de48cca811e5df08c717` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-2.md@02d35a1b003277509117433de3b648828d0d5070` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-3.md@7252fcd51bc9d03a92b2b59861a7d594c87d0de7` · `memory/builds/aKeyedAnnotation/spec/2026-09-05-spec-TOOL-aKeyedAnnotation-4.md@cd7d0a5673d85bef6152eb96875421e119edf659` · ROUND 1

## Verdict: BLOCKED

Two defects block, both unsatisfiable as written. B1 is an acceptance criterion asserting a count and a field the tree refutes, and it is the *only* criterion written for the thing it proves. B2 is a scope item ordering a change that reds the bar whichever way it is spelled, against a criterion demanding the bar be green. A builder reaching either has no honest way forward and will fake the observation or quietly drop it. Everything else below is repairable in place. Nothing in this round argues against the build's shape: the design pass's refusals hold up, and no finding asks for a grammar, a marker or a source-side gate.

The recurring shape across all twelve defects is one thing: **a criterion or a resolution that asserts rather than derives.** Five state a count, a carrier set or a verification that the tree refutes when you run the command the spec itself names. This repo's own bar is verify-over-assert, and the spec set is where it was skipped.

## Review shape and run integrity

- Raw findings 56 · confirmed 19 · refuted 37 · unverified 0 · precision 0.34.
- Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the pipeline. **The run is complete**: every lens and every skeptic batch came back, so a zero count in this report is a measured zero and not an absence of coverage.
- Precision 0.34 is below the ~0.5 floor §8 of the charter names. The correct response is tighter scope and priming next round, not more agents. Two of the four lenses produced most of the refuted volume.

**Convergence.** The 19 confirmed findings describe 12 distinct defects; this record collapses them and names the contributing raw ids on each. Three lenses independently found the same unsatisfiable AC4 in unit 2 and two found the same duplicated exclusion list — convergence is a severity signal, not extra findings, and the severity table below counts defects.

## Findings

| # | Severity | Unit | Address | Defect | Raw ids |
|---|---|---|---|---|---|
| B1 | blocker | `-2` | §6 AC4 (with §2 S4/S5, §4 Migration) | The drainability proof names two annotations where five exist, and asserts against the wrong field | 3, 21, 32 |
| B2 | blocker | `-1` | §2 S4 (against §6 AC6) | The backlog row S4 orders reds the bar whichever way it is spelled, and the measured escape was not carried over | 20 |
| H1 | high | `-1` | §2 S1/S6, §4 Rollout, §6 AC1 | A rendered guide is declared in three carriers; the spec names one and AC1 cannot see the other two | 35, 44 |
| H2 | high | `-4` | §2 S2, §6 AC2/AC3 | The test module is a byte-identical dogfood/template pair with no leg comparing them, and the spec never says which one gets the check | 37, 55 |
| H3 | high | `-2` | §2 S2, §4 Inventory | The narrowed globs are declared only in the project-owned copy, so the correction reaches gov and no adopter | 42 |
| H4 | high | `-2` | §5 error/empty states, §6 AC5 | The liveness assertion §5 names as the control for S2's hazard is computed before the globs are used, so it cannot see that hazard | 22 |
| H5 | high | `-2` | §2 S1, §6 AC1/AC4 | The id grammar has two entry points and S1 forecloses neither; the scratch-tree ACs run in exactly the place the wrong one reports a confident zero | 47 |
| H6 | high | `-4` | §2 S1 | Both premises S1 states about `reuse_lookup.py` are false — it holds dossier text, not parsed dossiers, and `detail` is an overloaded branch key | 53 |
| H7 | high | `-4` | §8 F1 resolution, §2 S3 | The resolution asserts a verification the named file refutes, and the shrink-only property it claims has no mechanism | 38, 52 |
| M1 | medium | `-1` | §6 AC5 | The only criterion written for S5's deletion is satisfied by never doing the deletion | 19 |
| M2 | medium | `-1` | §8 F2 resolution | The exclusion list exists in two files; the resolution patches the one that does not red the bar | 41, 46 |
| M3 | medium | `-4` | §1 Goal, §4 | "No consumer reads it" is false — `map_diff` already reads and prints the field | 54 |

Unit `-3` (the report-only signal for a source-cited id resolving to no record) drew no confirmed finding. Read that as "one round found nothing", not as a certificate: at precision 0.34 the round's discriminating power is modest, and `-3` is the smallest and most sequenced of the four.

---

## B1 — BLOCKER · `TOOL-aKeyedAnnotation-2` §6 AC4 (with §2 S4, §2 S5, §4 Migration)

AC4 and S5 both say the population drains when "the two real product annotations for the pinned ids" are removed. There are not two, and the field AC4 asserts on is not the field that moves.

Measured at this base with the oracle's own invocation, `git grep -l -w -F <id> -- tools skills .claude memory/guides/SESSION-KICKOFF.md coding-governance-agents.template.md WIRE-INTO-PROJECT.md`:

- 4 files cite the first pinned id (`TOOL-aBatchedLintel-1`): `tools/drift-audit/drift_signals.py`, `tools/memory-tree/check-memory-hygiene.sh` (two sites, `:633` and `:935`), `tools/memory-tree/check-memory-hygiene.test.sh`, `tools/memory-tree/hygiene-parity.test.sh`.
- 8 files cite the second (`TOOL-dNarrowedAnchor-1`): `tools/drift-audit/drift_signals.py`, `tools/unattended/.unattended.conf.example`, `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`, `tools/unattended/cross-component.test.sh`, `tools/unattended/run-unattended-gates.sh`, `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`.

After S3 drops the self-citation in `drift_signals.py` and S2 drops the `*.test.sh` population, **one** non-test product citation survives for the first id and **four** for the second. Removing two leaves the signal at 1, not 0.

The second half is worse and independent of the count. AC4 asserts "the signal's population reaches zero". The population is `of`, and `signal_spec_status` (`tools/drift-audit/drift_report.py:474-483`) returns `"of": checked` where `checked` counts non-terminal keyed specs — nothing a builder does to annotations moves it. What removing citations moves is `value`. AC5, three lines below, requires that same population to stay **non-empty**. As literally written, AC4 and AC5 demand opposite things about one number.

There is a third consequence in §4. Its ordering discipline — one change, one measurement, one recorded line — will produce three identical readings, because on this corpus S1, S2 and S3 each move the value by zero. A builder who was told "S1, S2 and S3 each move the population independently" (S4) will read three unmoved numbers as the change not working.

**Fix.** Rewrite AC4 to name an operation rather than a count: in a scratch tree, delete every remaining product citation of both pinned ids — enumerated by the `git grep -l -w -F` invocation above, which the AC prints — and assert the signal's **`value`** reaches 0 while `of` stays at its measured size. Restate S5's third arm the same way. Correct S4 to say that S1, S2 and S3 are each expected to move the value by zero on this corpus and that the recorded line must say so, so an unmoved reading is a confirmed result rather than an ambiguous one.

**Left-shift.** This is a derived count typed into prose beside the source that owns it, in an acceptance criterion — the class §7 of the charter bans, one level up from the code it usually bans it in. File it as a bug-class row so `python tools/memory-tree/gotchas.py --for-diff` selects it on any diff touching `memory/builds/*/spec/`: *an AC that states a numeral over a derived population must name the command that derives it, and the AC must assert on the field that command actually moves.* A machine gate is available if this recurs — `tools/check-spec-tokens.py` already walks the spec population and could carry a fourth join — but the checklist row is the cheap first move.

## B2 — BLOCKER · `TOOL-aKeyedAnnotation-1` §2 S4 (against §6 AC6)

S4 orders the missing records "filed as a backlog row" and does not carry over the escape the design pass measured. Every obvious way to write that row breaks something:

- **Id in the row's head.** `tools/memory-recall/extract.py:119` defines `A_DASH` as `^\s*[-*]\s+[`*]*(ID)\b[`*]*\s*[·|]`, and `memory/backlog/TOOL.md` rows are exactly `- <ID> · …`. So an id in the head **defines** it. `corpus_ids.py`'s own check-14 fixture comment says so verbatim. That resolves the id — and unit 3's AC1 needs it to resolve to nothing, so the row would quietly delete unit 3's only fixture.
- **Id in the row's body.** Then it is a bare citation, and hygiene check 14 counts cited-never-defined against `ORPHAN_ID_PIN="0"` with a waiver file that is empty by its own declaration. The bar reds. Raising the pin instead trips the `drift-audit records` RATCHETS row that marks it `weakens: up`.

AC6 ("the full bar is green on this unit's commit") therefore cannot hold if the row spells either id anywhere. The design pass §1 measured exactly this catch-22 and recorded the only escape — name the build and the seq range in prose, which no grammar matches — and §2 does not carry that constraint or point at it. A builder writing the obvious row reds the bar with no spec line telling them why. This repo has already paid for this class once; the gotcha record for it exists.

**Fix.** Extend S4: the backlog row is minted under one of this session's reserved ids and must name the foreign build plus its seq range in prose, spelling **no** id of that build anywhere in the row. Add an AC asserting `python tools/memory-tree/corpus_ids.py --report` shows an orphan count of 0 and an unchanged defs set for those ids after the row lands.

**Left-shift.** The gate exists (check 14 plus the RATCHETS row) and did its job; what is missing is the class being *selected before* the row is written. Extend the existing "citing a dangling id creates it as an orphan" gotcha record with the backlog-row disposition — head defines, body orphans, prose escapes — so `gotchas.py --for-diff` surfaces it on any diff touching `memory/backlog/`.

## H1 — HIGH · `TOOL-aKeyedAnnotation-1` §2 S1/S6, §4 Rollout, §6 AC1

§4 says "one template file, one render line, and whatever the carrier registry requires. Nothing else in the kit changes." A fourth rendered memory-tree guide touches three carriers beyond the render line, and the spec names none of them:

- `tools/memory-tree/kit.toml` — a `[[files]] role = "rendered"` stanza per guide with `to` and `placeholders` (`:24-40`). Without a fourth stanza the new template falls to the catch-all `include = "**" / role = "engine"` at `:21-22` and ships to adopters with **no render destination**.
- `tools/memory-tree/kit-dogfood-parity.test.sh:53` — a hand-kept three-entry `PAIRS` literal (HYGIENE, TEMPLATE-SPEC, BUILD-METHOD). Without a fourth row the dogfood copy can diverge from its template forever while the leg prints a green line.
- `tools/gate-legs.json:276-288` — that leg's `guard` names the three rendered paths explicitly, so the new one must join or the leg never fires on a diff that only touches it.

`memory/DECISIONS.md:47` records this registration verbatim for the build method: "It rides the existing parity leg as a third PAIRS row." AC1 exercises `adopt-memory-tree.sh` against a scratch clone only, so it passes on the render line alone and cannot catch either omission. `kit.toml:137-145` already carries a comment recording this exact two-carrier miss for BUILD-METHOD.md, which makes this a repeat of a documented failure rather than a novel one.

**Fix.** Add the three carriers to S1 by name and to the §4 Rollout sentence. Add an AC asserting the parity leg reports one more pair than at this base — a count the test already prints — and that editing the rendered guide away from its template reds it.

**Left-shift.** Derive over author: make `kit-dogfood-parity.test.sh` build `PAIRS` from `kit.toml`'s `role = "rendered"` stanzas instead of a hand-kept literal. Adding a stanza then adds the pair automatically and the class cannot recur. Same move kills the guard drift if the leg's guard is derived from the same stanzas.

## H2 — HIGH · `TOOL-aKeyedAnnotation-4` §2 S2, §6 AC2/AC3

S2 says "a new CHECK inside the existing codebase-map test module". There are two byte-identical copies of that module — `cmp tools/codebase-map/test_codebase_map.py tools/codebase-map/test_codebase_map.template.py` reports identical, both 8677 bytes — and `tools/codebase-map/adopt-codebase-map.sh:207` `cp`s the template to the adopter's `GATE_FILE`. Nothing on the bar compares them: `kit-dogfood-parity.test.sh`'s `PAIRS` covers only the memory-tree docs, so codebase-map has no parity leg at all.

Neither S2 nor AC2/AC3 says which file gets the check, and the consequences differ:

- Check in the dogfood copy only — gov's coverage leg runs it (`.codebase-map.conf` sets `GATE_FILE=tools/codebase-map/test_codebase_map.py`), but zero adopters receive it, while §5 ships a kit-README line claiming the field "is read and graded". `tools/codebase-map/selftest.py:241,350` reads the **template** into its scratch trees, so the kit selftest does not see the check either.
- Check in the template only — gov's own leg never runs it and AC2/AC3 pass or fail for the wrong reason.

Either way the copy relation silently ends with no leg noticing. §7 does implicitly point at the dogfood copy ("the module the coverage leg already runs"), so the "never says which" half is weak; the material half — the template is what ships, and the pair is unguarded — stands and the spec addresses it nowhere. `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-2.md` S5 makes the template an explicit write target for exactly this reason, which is live precedent.

**Fix.** State that the check lands in `test_codebase_map.template.py` and that the dogfood copy is re-copied in the same commit; S3's blank-pin scaffolding rides the template too. Add an AC asserting the two files compare identical after the unit.

**Left-shift.** Generalize the parity mechanism from H1: compare every kit's `role = "seed"` file against its `to =` target on the bar. One leg then covers this pair, the `drift_signals.py` pair in H3, and every future one.

## H3 — HIGH · `TOOL-aKeyedAnnotation-2` §2 S2, §4 Inventory

S2 declares the narrowed glob list in `tools/drift-audit/drift_signals.py` only. The precedent it copies, `TRACE_GLOBS`, ships in **two** places: `drift_signals.template.py:96` carries `TRACE_GLOBS: list[str] = []` with its own documentation block at `:90-95`, and `drift_report.py:1452` spells the fallback `list(getattr(proj, "TRACE_GLOBS", None) or proj.PRODUCT_GLOBS)`. `kit.toml` marks `drift_signals.py` `role = "project-owned"` and `drift_signals.template.py` `role = "seed"` with `to = "{kit}/drift_signals.py"` — the template **is** the file adopters receive.

So a declaration added only to the project-owned copy reaches gov and nobody else: every copy-installed drift-audit keeps the self-certifying oracle this unit exists to correct, while §5's user-docs line advertises the correction as one the kit README carries for adopters. §4's Inventory names three sites and never the template.

Raised from the lens's medium to high for consistency: this is the same "the fix lands in the dogfood copy only" class as H2, and the two should not carry different severities.

**Fix.** Add `drift_signals.template.py` to the §4 Inventory and to S2, with the row shipping empty plus the fallback comment exactly as `TRACE_GLOBS` does. State that the new name is read with getattr-and-fallback so an older adopter's project layer does not trip `load_project_layer`'s required-attribute check.

**Left-shift.** The generalized seed/target parity leg from H2 covers this too. Until it exists, add a bug-class row: *a declaration added to a `project-owned` kit file must be checked against its `seed` sibling in the same commit.*

## H4 — HIGH · `TOOL-aKeyedAnnotation-2` §5 error/empty/loading states, §6 AC5

§5 names the liveness assertion as "the control" for S2's hazard — "a narrowed glob that matches nothing reports a reassuring zero". It is not the control, because it cannot see that hazard.

`signal_spec_status` (`drift_report.py:441-483`) increments `checked` per non-terminal keyed spec **before** `ctx.product_globs` is ever used, and returns `"of": checked, "live": checked > 0`. The globs filter only `suspect`, that is `value`. A glob set resolving to no files therefore leaves `live` True and `of` at full size while `value` falls to 0 — precisely the reassuring zero, wearing a live flag.

AC5 ("reports a live, non-empty judgeable population") passes identically whether the narrowed globs match forty files or none: a criterion that cannot fail on the change it is written to cover. AC2's second half (a product-file citation must still count) gives the unit *some* coverage of a total collapse, but the control §5 names and the criterion §6 writes are both inert. Unit `-3` §S3 requires **two** counts for this same class, so the sibling specs apply opposite liveness discipline to one hazard.

**Fix.** Add a second liveness half owned by the narrowed declaration — the count of tracked files the narrowed globs resolve to — and make §5 name that as the control. Add an AC asserting the count is non-empty on this tree and that emptying the declaration in a scratch tree makes the signal report itself **dead** rather than 0.

**Left-shift.** A real gate, and cheap: a `selftest.py` arm that, for every signal whose declaration is a glob set, empties that declaration and asserts `live` goes False. That is the charter's "a probe that cannot move says so" made mechanical for the whole signal population rather than for one signal.

## H5 — HIGH · `TOOL-aKeyedAnnotation-2` §2 S1, §6 AC1/AC4

S1 says the pattern is "built from the shipped id grammar the recall extractor owns" without naming the entry point. The extractor has two, and they behave differently:

- Module-level `ID` / `ID_RE` (`extract.py:104-105`) bind at import from `CONF = recall_conf.resolve()`, anchored on `extract.py`'s own file — i.e. to the repo the **kit** lives in.
- `grammar_for(root)` (`extract.py:436`) rebinds families and eras to an explicit tree. Its own docstring says the module-level form is wrong for a caller classifying a different tree, and that "a grammar that recognises nothing yields an empty classification and an empty classification is what a clean corpus yields."

`memory/gotchas/grammar-bound-to-the-wrong-root.md` records the measured incident and names `grammar_for(root)` as the fix, "one accessor, no second grammar". The hazard is live inside this unit's own harness: `selftest.py:236` copies `drift_report.py` into a scratch tree carrying `TOOL-*` fixture ids and no `.memory-tree.conf` — exactly where a wrongly-bound grammar reports a confident zero. AC1 and AC4 both run against scratch trees and would pass or fail for reasons unrelated to what they test. (AC3, AC5 and AC7 run in gov and are unaffected, so "every acceptance criterion" as the lens put it is an overstatement; the two that matter are the two that observe the new pattern.)

**Fix.** S1 states the pattern comes from `extract.grammar_for(root)` bound to the tree being classified, never the module constants, and cites the gotcha record. Add an AC in the shape `corpus_ids.py --selftest` already uses: a scratch fixture declaring a family this repo does not, so a re-binding regression makes the arm fail rather than pass empty.

**Left-shift.** A ban-grep leg, which this repo already knows how to write: no module outside `extract.py` imports the module-level `ID` / `ID_RE`. That gates the class rather than the instance, and the gotcha record is the compensating check for anything the grep cannot reach.

## H6 — HIGH · `TOOL-aKeyedAnnotation-4` §2 S1

Both premises S1 states about `tools/codebase-map/reuse_lookup.py` are false.

- "The dossier loader already has the parsed dossier in hand." It does not. `:165` calls `m.load_dossier_texts(map_dir)`, whose own docstring in `map_lib` calls it "the prose half, read WITHOUT parsing the toml claims (so it needs no inventory_ids)". The `.decisions` tuple comes from `m.load_map_tree(ids, …)`, which needs `map_extractors.inventory_ids()` — project code the module's header explicitly disclaims: "Portable: reads only committed artifacts + dossiers + the conf … it needs NO project `map_extractors.py`". The sibling `map_diff.py:257-260` pays that price with `import map_extractors as ext`.
- "The candidate already carries a human-context detail field; this extends that field." `detail` is a single overloaded string (`detail: str = ""  # inventory id / owning dossier`), branched on per source in `_sources` around `:358-383`: `where = "FOUNDATION.md" if c.detail == "foundation" else f"features/{c.detail}.md"`. Extending it corrupts the branch that resolves a candidate back to its dossier or inventory.

A builder taking S1 literally either breaks the module's declared portability or breaks `_sources`. Both are silent.

**Fix.** Rewrite S1 against what the file holds: read the `decisions` ids out of the dossier **text** already loaded at `:165` (front-matter parse, no project layer) and carry them in a new candidate field printed on its own line — never in `detail`. State explicitly that the portability property is preserved, and add an AC asserting `reuse_lookup.py` still runs in a tree with no `map_extractors.py`.

**Left-shift.** That AC is the gate, and it should be a permanent selftest arm rather than a one-off observation: run `reuse_lookup.py` in a scratch tree with the project layer removed. A declared portability property with no arm asserting it is a comment.

## H7 — HIGH · `TOOL-aKeyedAnnotation-4` §8 F1 resolution, §2 S3

F1's resolution asserts: "Verified at this base that the file exists and already carries this kit's other measured pins." The file refutes it. `.codebase-map.conf` carries `MAP_ROOT`, `GATE_FILE`, `MAP_DIFF_CMD`, `RECALL_DARK_LAYERS`, `SEAM_FANIN_THRESHOLD` and `CLONE_COUNT_FILE`. There is no measured pin in it. Its one number says so in its own comment — "Kept at the kit default of 3 — this is a small tree and the threshold has not been re-measured against it" — and `CLONE_COUNT_FILE` is a path, empty. "Measured" is a loaded word here; the memory tree's own pins are declared as seeded at measured values, never guessed. S3's "the way the kit's other measured pins ship" rests on the same false premise.

The decision itself — (a), the kit's own conf — survives on its other stated ground: the kit is copy-installed and its pin must travel with it. But the omission the false verification hides is load-bearing. Nothing would make the pin shrink-only. The only mechanism in this repo is a `RATCHETS` row in `tools/drift-audit/drift_signals.py`, read by `ratchet_findings()` during `--check`, and F1's option set never mentions it or the kit's own shrink-only idiom (`affordance-exempt.toml` under `MAP_ROOT`, with a renderer, a seeder and drop-on-touch in `map_diff`). As written, "shrink-only" ships as a comment: anyone raises the number with no justification and no gate — the invisible-raise defect `TOOL-aNumeralWarden-3` built `RATCHETS` to close — so §4's claim that the pin "converts legal into declining" does not hold.

**Fix.** Correct the resolution's factual claim. Then decide the question it skipped: either the pin lives in `.codebase-map.conf` **and** a `RATCHETS` row names that file — recording that shrink-only enforcement needs drift-audit present, and what an adopter without it gets — or it lives where the ratchet already reaches. Add an AC that a raise without a nearby `<old> -> <new>` marker reds `drift-audit records`. Say why the `affordance-exempt.toml` registry idiom was not taken. Cite `TOOL-aNumeralWarden-3`.

**Left-shift.** Gate the general case: every conf key whose comment claims a pin is measured or shrink-only must resolve to a `RATCHETS` row, and every `RATCHETS` row must name a live key. Both directions, so a stale row reds as loudly as a missing one — the declared-population discipline §7 already asks of tooling.

## M1 — MEDIUM · `TOOL-aKeyedAnnotation-1` §6 AC5

S5 mandates a deletion: the mechanism paragraphs two gotcha records absorbed verbatim from call-site comments. AC5 is the only criterion written for it, and every clause it asserts holds unchanged if those paragraphs are never touched. `python tools/memory-tree/gotchas.py --check` exiting 0 is an invariant before and after; "each edited record still carries its class name and its incident" asserts residue, not removal. No other criterion observes the deletion — AC3 and AC4 cover S4's citation repairs, AC1 and AC2 the guide, AC6 the bar, which cannot see absorbed prose.

That is the shape §7 names: a gate you have only ever seen pass is an assertion about nothing. AC5 also drops "its reach", which S5 names as the third thing each record must keep.

**Fix.** Assert the specific mechanism sentences are gone by naming them, or assert each record's body shrinks below a stated size. Add "its reach" to the list of what must remain.

**Left-shift.** Same bug-class row as B1, second clause: *an AC whose assertions all hold unchanged when its scope item is skipped is not an acceptance criterion.* Selected per-diff on `memory/builds/*/spec/` by `gotchas.py --for-diff`. There is no cheap machine form of this; it is a documented check by construction, which §7 permits provided it is written down.

## M2 — MEDIUM · `TOOL-aKeyedAnnotation-1` §8 F2 resolution

F2's resolution routes the template's second half to "a skip case beside the two already in that block" — the seeder block in `tools/memory-tree/adopt-memory-tree.sh:229-232`. The file that actually reds the bar is the gate, `tools/memory-tree/check-method-carriers.sh:65-68`, which keeps its own byte-identical four-case exclusion list (memory root, `BUILD-METHOD.template.md`, the leg itself, `*.test.sh`). That leg is `subject = repo` with **no** guard key in `tools/gate-legs.json:291-297`, so it runs on every bar in every adopting tree, and its check 3 fails on any file mentioning `BUILD-METHOD.md` that is not declared in `memory/project/method-carriers.txt`.

A seeder-only patch therefore leaves gov red on the new template and leaves a fresh adopter red at install. The resolution's own liveness note says the probe was run on the seeder only. Patching both leaves the exclusion in two hand-kept spellings — the drift class `kit-dogfood-parity.test.sh`'s own tail comment (`:138-139`) calls out.

**Fix.** Take the cheap resolution instead: add a one-line constraint to S1 that the new template must not contain the literal `BUILD-METHOD.md` at all, which needs no skip case in either file. Add an AC asserting `bash tools/memory-tree/check-method-carriers.sh` is green after the unit. If the literal must appear, name both sites in F2.

**Left-shift.** Single-source the exclusion list. The repo already has the mechanism for a deliberate inline copy — the marked-copy parity table in `tools/lib/resolve-python.test.sh`, which gates `kit-dogfood-parity.test.sh`'s own inlined render block byte for byte. One more row there, or the seeder sources the checker's list.

## M3 — MEDIUM · `TOOL-aKeyedAnnotation-4` §1 Goal, §4

§1 says of the dossier `decisions` field: "no consumer reads it." One does. `tools/codebase-map/map_diff.py:275` reads the parsed field and prints it per feature — `meta = f" · {d.status} · {', '.join(d.decisions[:3])}"` — and `map_diff` is shipped and wired: `MAP_DIFF_CMD` in `.codebase-map.conf`, cited by `memory/guides/SESSION-KICKOFF.md:137`, `memory/map/README.md:24` and `skills/session-kickoff/SKILL.md:58`. The claim is unqualified, not scoped to the reuse audit.

The unit's causal story ("nothing reads it, so nobody fills it") therefore rests on a premise the tree refutes, and the existing consumer's conventions — read the **parsed** dossier, truncate to the first three ids — are live precedent S1 neither follows nor knowingly diverges from. §4's validation story survives; §1's premise does not.

**Fix.** Correct §1 and §4 to "one consumer reads it, in the range digest; the reuse audit — the orientation path this build cares about — does not." Have S1 state whether it matches `map_diff`'s three-id truncation or prints all of them, with the reason.

**Left-shift.** No gate. A "nothing reads X" claim is a grep away from being checked, so this is a review-checklist item rather than machinery: *a spec asserting that a field has no consumer names the grep that established it.* Fold into the same bug-class row as B1.

---

## What to do before building

1. Repair B1 and B2 in the specs. Both are unbuildable as written and neither has a workaround a builder can improvise honestly.
2. Repair H1, H2 and H3 together — they are one class (a change landing in the dogfood copy and not the shipped one) across three kits, and one derived parity leg closes all three permanently.
3. Repair H4 and H5 before the first `drift_report.py` edit: both change what unit `-2`'s scratch-tree criteria mean.
4. H6 rewrites unit `-4` S1 against the real file. H7 corrects a false verification and decides a question the fork resolution skipped.
5. M1–M3 are prose and criterion corrections; land them with the rest, not in a follow-up.

The fork resolutions committed at the base of this review carried three of these defects (B2's missing constraint, M2's wrong site, H7's false verification). That resolution prose was fresh and unreviewed by construction, and it was worth reviewing: it produced a blocker and two highs on its own.
