# Review — aWalkedCorpus, round 3 (re-review of the rev-2 fix, TOOL-aWalkedCorpus-3, UNBUILT)

**Serves:** spec-audit TOOL-aWalkedCorpus-3

## Verdict: BLOCKED

*Synthesis over four live lenses against the worktree at HEAD `84711c0`, declared base `3e5c6d43`.
**4/4 lenses live, 0 dead. 17 raw judged — 16 confirmed, 0 unverified, 1 dropped at the skeptic
stage.** The 16 collapse to **5 findings** after merging four duplicate clusters: two lenses filed the
`kit.toml` exclude no-op (F1), two the evaluation-order contradiction (F2), four the undeclared
`OVERLAP_MAX` and its undefined metric (F3), two the gov-keyed arms landing in the shipped
`selftest.py` (F4). **Every row was re-executed here before it entered the table**, and three were
narrowed or dropped on re-execution — recorded under Report limits, not silently. This is a spec:
**not one finding reds a leg today.***

*The tree was not mutated. `git status --short -uall` is empty before and after; every degradation
was simulated in-process over JSONL extracted into the scratchpad, never by editing a tracked file.*

## Are F1 and F2 closed?

**Both are closed on their measurement half and open on their arming half.** rev-2 folded the halves
that could be settled by running something, and left the halves that required a number to be declared
or an arm to be reachable.

**F1 — the fixture and its numbers: CLOSED, exhaustively.** Every figure in §4 reproduces on this
tree. `python tools/memory-recall/extract.py . <tmp> --chunk-max 600` gives `records 257 docs,
112002 indexed chars` — §4:158's figure exactly. `bench.py <tmp> tools/memory-recall/recall-fixture.json
--sets records,chunks --subs fts5,fts5w --ks 1,5,10` gives records/`fts5` r@1/r@5/r@10 =
0.75/0.83/0.83 at `ceiling 1.00`, `fts5w` r@10 **0.83 — equal to `fts5`**, and chunks/`fts5` r@5 0.17.
So §3's 0.1667 and §4:80's equality claim — the two numbers that *reversed* under round-2's
independently authored fixture — are now honest. Driving `bench.expected_by_target` and `bench.score`
per question reproduced **all twelve** rows of §4's Inventory with zero mismatches on both `homes` and
`hits`, yielding h=10, R=12, `(h-1)/(R-1) = 0.8182 -> 0.81`. Re-benching filtered `records.jsonl`
reproduced all five degradation rows cell for cell across all six columns:

| lever (measured here) | ceiling | `r@5` | normalised | floor | per-id |
|---|---|---|---|---|---|
| baseline | 1.0000 | 0.8333 | 0.8333 | green | green |
| drop the `DECISIONS.md` home of `TOOL-aWrittenMethod-4` | 1.0000 | 0.7500 | 0.7500 | **RED** | green |
| retire `TOOL-aMouldedFolio-1` | 0.9167 | 0.8333 | 0.9091 | green | **RED** names the id |
| retire `TOOL-aStandingWrit-2` | 0.9167 | 0.7500 | 0.8182 | green | **RED** names the id |
| drop `memory/DECISIONS.md` wholesale | 0.8333 | 0.1667 | 0.2000 | **RED** | **RED** |

I invented the record filters from the row labels alone before comparing, so round-2 F6's "how is the
degraded dir built" seam is closed in practice as well as in prose. **Nothing in §4 failed to
reproduce.** The fixture is also not the tautology round-2 built: content-term overlap of each
question against the union of every record carrying its id peaks at **0.500** (mean 0.362; Jaccard
peaks at 0.107) against ~1.0 for a query-is-the-record set, two of the twelve genuinely fail today,
and every `from` citation resolves.

**F1's second half — NOT closed.** Round-2's remedy asked for the anti-tautology property to become
"a gate rather than a sentence, **failing above a declared share**". The observer is designed
(`--audit-fixture`) and the share is not declared: `OVERLAP_MAX` is used three times in the tree and
defined nowhere, the metric behind it is ambiguous by a factor of five across readings that are all
consistent with §4's wording, and its red branch is armed by no arm S6 enumerates. rev-1 carried a
measured number here; rev-2 deleted it and replaced it with the undefined constant. See **F3**.

**F2 — the arithmetic: CLOSED, and the pin is not a cherry-pick.** `r@k / ceiling` reducing to `h/R`
is stated correctly and the derived pin holds. I enumerated **all twelve single retirements**, as this
pass was convened to do:

```
retire TOOL-aUnmannedHelm-5     norm 0.8182 GREEN     retire TOOL-aWrittenMethod-4   norm 0.8182 GREEN
retire TOOL-aUnmannedHelm-6     norm 0.8182 GREEN     retire TOOL-aWrittenMethod-6   norm 0.8182 GREEN
retire TOOL-aStandingWrit-2     norm 0.8182 GREEN     retire TOOL-aUnmannedHelm-10   norm 0.9091 GREEN
retire TOOL-aStandingWrit-4     norm 0.8182 GREEN     retire TOOL-aMouldedFolio-1    norm 0.9091 GREEN
retire TOOL-cSteadyMetronome-1  norm 0.8182 GREEN     retire TOOL-aUnmannedHelm-9    norm 0.8182 GREEN
retire TOOL-aWidenedGuide-1     norm 0.8182 GREEN     retire TOOL-cFinalBerth-1      norm 0.8182 GREEN

MIN normalised over ALL TWELVE = 0.8182  ->  pin 0.81 HOLDS
```

The ten hitting targets all land on exactly `(h-1)/(R-1)`, the two missing targets on 0.9091, and no
retirement caused collateral rank movement. **AC2c's "one retirement is free by construction"
generalises to every retirement, not only the one §4 picked.**

**F2's second half — NOT closed, and the fold is what broke it.** F2's remedy had two parts: fix the
arithmetic *and* arm the separation. The arms were written as AC2b and AC2c — and the evaluation order
added in the *same* revision to fold F6 makes both of them assert a verdict the program, as specified,
never computes. See **F2** below. Round-2's blocking observation was "a mechanism whose one arm cannot
distinguish it working from it broken"; rev-2 fixed the mechanism and left the arms unreachable.

## Findings

| id | sev | where | finding | fix |
|---|---|---|---|---|
| **F1** | **blocker** | `spec:43-47` (S8), `:65`, `:211`, `:306-308` (AC12) | **The F5 fold names a mechanism govkit does not implement, so it is a silent no-op and the AC written to verify it is structurally blind.** S8 gives `kit.toml` "a `[[files]]` exclude for `recall-fixture.json` and `check-recall.py`". There is no `exclude` key in any govkit code path — `grep -rn exclude tools/govkit/` returns one hit, a docstring at `govkit.py:124`. I drove `resolve_rule_pool` (`govkit.py:715`) in-process against this descriptor: **today** the `**` pool is 15 files and contains `tools/memory-recall/recall-fixture.json`; **with `exclude = [...]` added to the `**` rule the pool is still 15 and still contains it**; only a second rule claiming the destination drops it to 14. `selfcheck` (`:297-440`) validates ids, source existence, destination collisions, `version_from`, holes and `requires_if` and has **no unknown-key arm**, so it stays green on the no-op — AC12's first clause is insensitive to whatever S8 writes, and its second clause ("excludes … from the kit payload") is asserted by no leg on the bar. So `§3:65`'s "S8 excludes the fixture and the program from the kit payload" is **false as S8 specifies it**, and round-2 F5 is relocated rather than closed. | Replace S8's `exclude` with the idiom the engine implements and two sibling kits already use: a **second `[[files]]` rule**, `include = ["recall-fixture.json", "check-recall.py"]` with `role = "project-owned"` and no `to`, citing `tools/drift-audit/kit.toml:13-15` and `scan_claimed_paths`'s own contract (`govkit.py:738-741`, "a `**` include means everything not otherwise claimed"). State in S8 that a `**` rule excludes **only** by another rule CLAIMING the destination. Then restate AC12 against the payload rather than the exit code — `project-owned` is outside `LANDABLE_ROLES` (`govkit.py:688`) so `apply` skips it, but `plan` still PRINTS a `project-owned` row (I ran it), so pin the **role tag on the row**, or `apply`'s writes into a scratch target, not "plan lists neither path". |
| **F2** | **blocker** | `spec:98-109` (Data model steps 3 & 5) vs `:279-284` (AC2b, AC2c) and `:261-262` (§5) | **The evaluation order the F6 fold introduced makes the two single-direction levers the F2 fold introduced unobservable — the two fixes collide, and one of two stated properties is false whichever way the builder resolves it.** §4:98 fixes the order "because the message a red prints must be determinate", §4:104 puts per-id resolution BEFORE the floor, and §4:108 rests the no-0/0 guarantee on a step-3 red never reaching the division. I measured both rows that carry F2's separation claim and **step 3 fires in both**: retire `TOOL-aMouldedFolio-1` -> per-id RED `['TOOL-aMouldedFolio-1']`; retire `TOOL-aStandingWrit-2` -> per-id RED `['TOOL-aStandingWrit-2']`. Yet AC2b:280 asserts "the floor stays green" and "Measured normalised 0.9091", AC2c:283 asserts "the normalised score is 0.8182 and does NOT breach `RECALL_FLOOR`", and §5:261 asserts a red prints "the cell, the raw score, the ceiling **and the normalised value**". Terminate at step 3 and all three are false for exactly those rows, leaving AC2b/AC2c able to assert only the ABSENCE of a `RECALL_FLOOR` string — a pass-by-finding-nothing arm, the class this unit exists to close. Accumulate instead and §4:108's stated no-0/0 property is false: I confirmed the all-miss fixture yields `ceiling 0.0` with the cell present at 0.0, so AC5:291's "never divides by a zero `ceiling`" then needs an explicit branch that no step declares. rev-2 resolves that fork nowhere, and the cheapest build-time exit is to weaken the arm — which is what round-2's disposition blocked on. (AC2a is unaffected: step 3 passes there, and I measured floor RED / per-id green.) | Separate **EVALUATION** from **REPORTING** in §4's Data model, the way `run-gates.sh` already separates scheduling order from reporting order: steps 3, 4 and 5 all evaluate and all PRINT their verdict, the process exits non-zero if any failed, and the fixed order governs only which message leads. Keep the 0/0 guarantee as an explicit rule rather than a side effect — when `ceiling` is 0 the floor step prints "not evaluated: ceiling 0" and never divides — and point AC5's second half at that rule. Reconcile §5:261 with the wording that lands. While there: state which inputs the normalisation uses, because AC2b's `0.9091` is reproducible only from UNROUNDED values — `bench.py:456` and `:475-477` round the `--json` report to four decimals, and `0.8333 / 0.9167` = **0.9090**, so a builder implementing against the seam §10:361 names gets 0.9090 and the arm fails on a figure §4 calls measured (row 4 is 0.8182 either way). |
| **F3** | high | `spec:111-113`, `:299-301` (AC9) | **The mechanical observer that closes F1's anti-tautology half rests on an undeclared threshold over an undefined metric.** `OVERLAP_MAX` appears at `spec:112`, `spec:300` and `recall-fixture.json:15` — three uses, **zero definitions**: no value, no home, no owner anywhere in the tree, and no Files-touched row, while S3 gives `RECALL_FLOOR` a value, a home and a derivation. rev-1 carried the only measured number here ("eleven of the twelve questions share under half their content terms with the record they target"); rev-2 deleted it and left the bare constant, so the builder sets the knob **after** seeing the result — the move §4:246-248 itself rejects via `aQuarriedLantern-1:568`. The metric is undefined where it matters: §4:111 says overlap is against "its target's **own text**" (singular) while §4's Inventory three lines above lists ids with **3 homes**. Recomputed with `bench.terms` over the committed fixture, the readings disagree by 5x — union-of-homes max **0.5000** / mean 0.362 (9 of 12 strictly under half), first-home max 0.5000 / mean 0.299 (**11 of 12** — precisely rev-1's deleted claim, so a single-home denominator was the author's own), last-home reporting **0.000** for questions 2, 6, 7 and 8 (it would certify a question tautological against any home but the last), share-of-TARGET-terms max **0.13**, Jaccard max **0.107**. Direction is stated consistently ("reds above" / "at or below"), so three questions sitting exactly at 0.500 pass — but any threshold in [0.5, 1.0) is green on landing and binds nothing. The red direction is also armed by nothing standing: S6:36-38 enumerates its arms exhaustively and carries no overlap arm, AC7:293-294 scopes its red-proof to "§4's degradation table", §7's invocation omits `--audit-fixture`, and `check-arms.py:118` scans tracked `*.sh` only, so the repo's meta-gate cannot backstop a python gate's fail branch. | Declare in §4 the three things AC9 needs to be a measurement, not a decoration: **(i)** the tokenizer — `bench.terms`, imported not reimplemented, the same choice §4 already makes for `query.CHUNK_MAX`; **(ii)** the denominator as one formula, naming the multi-home reduction explicitly (`\|terms(q) ∩ terms(union of every home)\| / \|terms(q)\|`, citing the Inventory's `homes` column of 3); **(iii)** `OVERLAP_MAX`'s value and its home the way S3 does for the floor — a module constant in `check-recall.py` with its justification beside it — plus a Files-touched row. Seed it from a MEASUREMENT: add the per-question overlap as a column on §4's Inventory (max 0.500, mean 0.362, three at 0.500, none at or above 0.60) and pin at 0.55 or 0.60 so it carries margin; say in §5 that raising it is the move that makes the check stop working. Add one arm to S6 — a fixture whose queries are their targets' own text reds, naming the offending question and its overlap — and extend AC7's red-proof clause to cover it, so the branch has a standing arm rather than a build-day demonstration. |
| **F4** | high | `spec:36-38` (S6) against `tools/memory-recall/kit.toml:9-11,36-39` and `selftest.py:6-7,39,79-104` | **S8 withholds two files from adopters and S6 puts arms that depend on them into a file that ships to every adopter AND runs as a standing leg there.** `kit.toml:9-11` is the `**` engine rule and `:36-39` declares `[[gate_leg]] name = "memory-recall kit selftest", argv = ["python", "{kit}/selftest.py"], guard = ["{kit}/"]`, so `selftest.py` lands in and runs on every adopting tree; `SHIPPED` at `selftest.py:39` lists it. Today's file is deliberately gov-independent — every arm runs inside `make_repo`'s throwaway repo over the synthetic two-record `CORPUS`, whose only ids are `TOOL-aFoo-<n>`, and its own docstring says "What this gates is the KIT CONTRACT, not a recall floor. **No adopter has a graded fixture.**" S6 adds "one arm per row of §4's degradation table" — rows keyed on `TOOL-aWrittenMethod-4`, `TOOL-aMouldedFolio-1`, `TOOL-aStandingWrit-2` and `memory/DECISIONS.md` at literals 0.7500 / 0.9091 / 0.8182 / 0.2000, with AC2a/b/c naming the same — and §4:93 says `--data-dir` "is the seam every arm in S6 needs", i.e. the arms need `check-recall.py` and `recall-fixture.json`, the two files S8 removes. An adopter therefore receives a leg whose new arms reference a program and a question set deliberately not shipped: it reds, or it silently skips, and rev-2 says which nowhere. I grepped §3, §4 Files touched, §5, §8 and every AC — nothing reconciles S6 with S8. This is the exclusion being incomplete, not the §8 fork. | Say in S6 that the degradation arms run over a **SYNTHETIC** corpus built by the existing `make_repo`/`CORPUS` harness, reproducing each row's SHAPE (a multi-homed id losing one home; a single-homed id retired; a hitting target retired; the record file dropped) and asserting the **direction pair** (floor red/green × per-id red/green) that §4's table is actually about — those stay true in any tree — and state that §4's gov literals are the pin's derivation and AC2a/b/c's one-time acceptance measurement, NOT what the arms pin. Since a synthetic corpus still leaves `check-recall.py` unshipped, close it fully: carry the arms in a gov-only sibling (`check-recall.py --selftest`, this repo's stated idiom, or `tools/memory-recall/check-recall.test.py`) covered by the same non-landable rule F1 asks for, and give it its own `tools/gate-legs.json` entry beside S5's. |
| F5 | med | `spec:124-127`, AC2c `:282-284`, §6 | **The property §4 italicises for the derived pin over-states in the permissive direction, and nothing re-asserts the derivation as `h` and `R` move.** §4:124 claims *"the floor carries exactly one legitimate retirement's headroom by construction"* and §4:125 supports it with "A second retirement (`8/10 = 0.80`) … reds, which is correct". I swept all 66 two-retirement pairs: **45 RED, 21 GREEN** (min green 0.9000, max 1.0000), and the green set is exactly the pairs containing one of the two currently-MISSING targets — retiring a miss drops `R` without dropping `h` and so RAISES the score, with retire-both-misses scoring **1.0000, above baseline**. `8/10 = 0.80` is the worst case only when both retirements are of HITTING targets. §4's own row 3 already demonstrates the mechanism (0.9091 > 0.8333), so the table and the prose disagree. Separately, **no AC in §6 asserts the declared pin against the `h`/`R` it is derived from**: grow the fixture to h=12/R=14 and the worst case becomes `11/13 = 0.8462`, at which a stale 0.81 silently passes two hit-retirements — and §4:158-160 already records the corpus moving 256 -> 257 mid-build. (Not filed as worse: S4's per-id assertion reds on EVERY retirement naming the id, which I measured, so a second retirement is never invisible — only the floor half of the signal stays green.) | Two edits, both in this spec. **(a)** Restate §4:124-127 to what the arithmetic gives: the floor carries one retirement of a **HITTING** target, retiring a non-hitting target costs the floor nothing (it raises the score), and the second retirement reds only when both are hits — so the prose agrees with row 3 of its own table. **(b)** Arm the derivation without recomputing the threshold from the graded run (which §4:246-248 rightly refuses): fold it into `--audit-fixture`, which already walks the fixture — print measured `h` and `R` and red when the DECLARED `RECALL_FLOOR` differs from the two-decimal floor of `(h-1)/(R-1)`. That ASSERTS the declared pin against an independent derivation rather than adopting it. Name it in an AC. |

## Checked and clean

- **Every number in §4 reproduces.** `records 257 docs, 112002 indexed chars`; records/`fts5`
  r@1/r@5/r@10 0.75/0.83/0.83 at `ceiling 1.00`; `fts5w` r@10 0.8333 equal to `fts5`; chunks/`fts5`
  r@5 0.1667. All five degradation rows reproduce cell for cell across all six columns, from record
  filters I derived from the row labels before comparing. **F1's and F2's measurement debt is paid in
  full.**
- **The Inventory table is correct in both columns.** All twelve `homes` values (3,3,2,2,1,2,3,3,2,1,2,2)
  and all twelve `hits` booleans match measurement — including the two misses, `TOOL-aUnmannedHelm-10`
  and `TOOL-aMouldedFolio-1`. The hand-kept `hits` field is documentation the fixture says nothing
  reads, and today it is accurate; I did not file it.
- **The fixture is not a tautology.** Overlap against the union of every home peaks at 0.500 (mean
  0.362; Jaccard 0.107) against ~1.0 for the copied-text set round-2 built; two of twelve genuinely
  fail; every `from` resolves — the two §10-probe citations at
  `memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-2.md:260-261`, and the
  `DECISIONS.md` quotes verbatim at `:32`, `:47` and elsewhere.
- **The pin is derived, not cherry-picked.** Minimum normalised score over all twelve single
  retirements is 0.8182, above the 0.81 pin, with the ten hitting targets landing on exactly
  `(h-1)/(R-1)`. Robust to corpus growth too: nine of the ten hitting targets sit at rank 1 and one at
  rank 2, so a target must be outranked by five new documents to flip — I probed that and am not
  filing it.
- **Round-2 F4 is CLOSED.** `grep -n memory.recall memory/map/baseline.toml` returns exactly four
  (`:32`, `:33`, `:52`, `:71`), matching S7's "measured at four"; `memory/map/generated/` holds
  exactly `MAP.md`, `inventories.json`, `symbols.json` — the three Files touched now names; and
  `gen_map.py:206` carries `--write`, documented at `:6` as "(re)render generated/ to disk".
- **Round-2 F6's two degenerate fixtures behave as §4 says.** `{"queries": []}` yields
  `substrates {}` with `ceiling 0.0` at exit 0, so step 4 catches it rather than a `KeyError`; an
  all-miss fixture leaves the cell present at 0.0 with `ceiling 0.0`, so step 3 reaches it before any
  division. Also verified that an unknown SUBSTRATE name already reds by name through step 4
  (`rank_with` returns `None` -> `substrates {}`), so only `<set>` is unguarded.
- **§4's `query.CHUNK_MAX` claim is load-bearing and correct.** `query.py:111` is 600 and
  `extract.py:137` is 2400, so "imported rather than restated so the graded corpus is the served one"
  is doing real work, and 600 is the argv the reproduction uses.
- **`bench.py` and `union.py` are untouched**, and the round-2 degradation seam (round-2 F6a) is
  genuinely closed by `--data-dir`.

## Report limits

- **Verified but uncapped — three findings that reproduce and did not displace a row above.**
  (a) **A grammar-valid pin naming a set the extractor does not produce crashes rather than redding by
  name.** `--sets recordz` ends in `FileNotFoundError` inside `bench.load` (`bench.py:69`) before
  `report["sets"]` is populated at `:452`, so step 4's "absent cell" branch is unreachable and
  §5:257-260's "five ordered branches … each redding by NAME" is false for a state one typo in
  `.memory-tree.conf` produces. One extra alternation in step 2's grammar (constrain `<set>` only)
  plus an AC4/S6 extension closes it; the leg still exits non-zero, so it reds indeterminately rather
  than falsely green. (b) **§10:361-363 is false as written** — "`bench.py`'s `--json` report … already
  carries every value the pin and the per-id assertion need". I dumped a live report: it is
  `{slice, n_queries, sets:{<name>:{docs, chars, index_s, ceiling, substrates:{<sub>:{metrics}}}}}`
  with no per-query, per-target or per-id field, because `expected_by_target` drops an unresolvable
  target (`bench.py:360-361`) before `ceiling` is computed. `git diff` shows rev-1 read "every value
  BOTH PINS need", true then; rev-2 word-substituted it. Not filed for the cap because both normative
  statements (S4:29-30 and §4 step 3) already route the per-id assertion to the graded set itself, so
  the false clause sits in the reuse audit and nothing gets built on it. (c) The `0.9091`/`0.9090`
  rounding seam is folded into **F2**'s fix rather than filed separately.
- **Narrowed on re-execution.** A lens filed S4:30's "any id with an empty hit set" as a
  permanently-green predicate, since `expected_by_target` drops rather than empties. I implemented
  both readings: the vacuous one returns `[]` on every degraded dir and so fails AC2b at first
  contact, and §4 step 3 states the predicate correctly. Dropped to a wording note inside **F3**'s
  neighbourhood, not filed. A lens also filed the hand-kept `hits` booleans as unobserved claims;
  all twelve match measurement today and the fixture states nothing reads them — dropped.
- **Not attempted, so not findings.** §5's perf figures (extract 0.43 s, bench 0.07 s) are
  machine-variable and round-2 already banded them. §4's provenance-pool arithmetic — "8 specs carry
  a probe, 3 name ids, 2 cite a MISS" — was not re-derived.
- **By design, not re-reported** per this round's brief: that the unit grades only `records`; that
  `bench.py`/`union.py` are byte-pinned; that the predecessor stays DEFERRED and the adopter-facing
  floor is PARKED in §8; and that twelve questions is deliberately small. **F4 is not the parked §8
  question** — it is the S8 exclusion being incomplete in a direction §8 does not discuss.
- **Every measurement is against this worktree at HEAD `84711c0`.** Corpus figures: 326 files,
  257 records, 10394 chunks at `--chunk-max 600`, 214 anchored ids. They will move — §4 says so, and
  that is exactly why **F5**'s maintenance half matters.
- **The tracked tree was not mutated.** All extraction went to the scratchpad; all degradations were
  in-process filters over the extracted JSONL; all govkit probing was against deep-copied descriptors.
  `git status --short -uall` is empty.

**Disposition — the build may NOT proceed to its first code pass, and the gap is narrower than round
2's.** rev-2 did the hard, honest half of both blockers: the fixture is committed, every number
reproduces, the two reversed design arguments are corrected, and the pin is derived from an arithmetic
I re-verified across all twelve retirements. What did not land is the *arming* half of each — the
share `--audit-fixture` fails above is undeclared over an undefined metric (F3), and the two
single-direction levers §5 calls "the unit's centre" assert values the specified evaluation order never
computes (F2). Alongside them the F5 fold names a `kit.toml` mechanism that does not exist, so it ships
the fixture anyway while AC12 goes green (F1), and S6 routes gov-keyed arms into the one file S8 forgot
to look at (F4). All four fold into the spec; none says the unit is the wrong unit. Take it to rev-3.
