**Serves:** diff-review TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-4 TOOL-dGatedProse-5

# Closing diff review, round 2 — dGatedProse: the fold of round 1 and the post-build bar's three reds

Node `d` · 2026-09-22 · Tier-2 · on `branch/spec-prose-gates-b41f7c` · adversarial fan through `tier2-review.js` (4 finder lenses → 4 skeptic batches → this synthesis). The subject is the fold commit alone, not the build again. This synthesis re-read every confirmed finding at source before adjudicating it. It re-executed the two check-25 boundary claims in scratch awk outside the repo, using a verbatim copy of `test_whole_token`.

**Reviewed range:** `6526ce5597489edd6066d635845bf53be778c4f0...bbabce16c9dd5138bd7eccb128ee84d878ba0fc7` — **ROUND 2**. One commit, 22 files, +347/−65. The code subject is `check-spec-tokens.py` and its test, and `check-memory-hygiene.sh` and its test. The record subject is the backlog closures and new rows in `memory/backlog/TOOL.md`, the roster table added to the build README, the rev-12 and rev-10 fold lines of specs 1 and 2, the HYGIENE and TEMPLATE-SPEC template edits with their renders, and the 2.83 to 2.84 kit marker move.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and no finding is HIGH. All four round-1 fixes are in the code and do what round 1 asked. The claims join now keys on `claims <- <object>`. Check 25 resolves a by-name token as a whole word. The claims join's fence blanker is a line-preserving port of the engine's `_unfenced`. The two populations are spelled where the spec template states them. None of the four is reopened in its own shape. Two fixes landed with one half of the new property never seen to fail, and one fix closes R2's class for underscore names but not for hyphenated ones. Details are under F2, F3 and F4.

The one MEDIUM is new in this fold and is not a round-1 finding. The fold re-worded `TOOL-dLoggedFlight-32` as it closed it, and the new text credits the claims join with an ownership check. The join refuses three shapes and reads no dossier, and its own header lists a claim in the wrong dossier as limit (5). The roster table the fold added repeats the claim. Three lenses reported this independently. The remaining four LOWs are a stale fixture-count comment, a roster row calling unit 3's the only version bump, and the two unobserved arm halves.

## Review shape

Raw **12** · confirmed **8** · refuted **4** · unverified **0** · precision **0.67**.

Precision clears the 0.5 floor that §8 sets. The eight confirmed findings collapse to **6 items**. Ids 5, 8 and 10 report the same backlog row with the same evidence, and 8 and 10 also name roster row 2. I merged them at write time; the pipeline discarded no duplicates. Id 6 names roster rows 2 and 3. Row 2 is fixed under F1, so id 6 keeps its own LOW item for row 3 and is not merged. The four refuted findings (ids 1, 3, 4 and 11) reached this synthesis only as a count, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 1 MEDIUM · 5 LOW** (6 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 3 MEDIUM · 5 LOW** (8 findings). Every id takes the severity of the item that holds it. No id changed severity from its finder's rating.

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **4/4** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not a hole. That includes zero HIGH or BLOCKER findings and the clean results listed under "Hunted and clean". The one duplicate group was judged by hand in this synthesis, as stated above.

What this synthesis ran:

- A verbatim copy of `test_whole_token` (`check-memory-hygiene.sh:2025-2036`) under GNU Awk 5.4.0 in the scratchpad, against the fixture guide's own lines (`check-memory-hygiene.test.sh:860`). `count_shard` gives 0 and `tRerun` gives 0. `shard_rows`, found only inside `count_shard_rows`, gives 0. With the leading boundary test removed, `count_shard` and `tRerun` still give 0, but `shard_rows` flips to **1**. On the line `run it with --dry-run and tools/check-spec-tokens.py`, `--dry` gives **1**, `check-spec` gives **1** and `check_spec` gives 0. A line spelling the token embedded first and whole second gives 1.
- `git grep` for the kit marker: `memory-tree@2.84` is in exactly nine files. Those are the engine, the four templates and their four renders. The only `2.83` left under `memory/builds/` is an acceptance ledger recording unit 3's move, which is history and correct to keep.
- `grep -nE '^[A-Z_]*CHECK = ' row_grammar.py` returns `CHECK = 20` and `ROTATION_CHECK = 24`. The kit README's check table reads 25.
- The checker's hit, NEAR, `--list`, waived and stale paths (`check-spec-tokens.py:790-812`) read against both new R1 arms and the waiver dict.

What it did not run: the bar, `check-memory-hygiene.test.sh`, `check-spec-tokens.test.sh` and every gate leg. A full bar is running on this tree, and the brief forbids any index change or leg run until it finishes. The mutation repro for id 9 is the skeptic's, run in a scratch repo outside the tree. The code at `:800-803` makes it directly legible.

## Round 1, as the fold left it

| Round 1 | Fold outcome | This round |
|---|---|---|
| R1, the waiver key | Fixed. The composite token reaches the hit, the NEAR row, the `--list` row, the live report line and the stale loop. Arm 1 observes the swallow direction and arm 2 the stale direction, and both go red on the old code. | Not reopened. The documented remedy, waiving by the composite token, has no arm: F3, id 9. |
| R2, substring resolution | Fixed for underscore names and after the call-suffix strip. | Partly mis-fixed. The class stays open for hyphenated names, and HYGIENE item 25 now says it is closed: F2, id 7. The leading half of the boundary has never failed: F4, id 2. The fixture header count went stale: F5, id 12. |
| R3, the fence blanker | Fixed. The port blanks opener and closer lines, keeps one output line per input line, strips a trailing CR before the test, and treats the other marker as content. | Not reopened. No finding. |
| R4, one word, two populations | Folded as prose in the checker header and the spec template, with the predicate change routed to a backlog row. | Not reopened. No finding. |

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| F1 | MED | 5, 8, 10 | `memory/backlog/TOOL.md:559`, `memory/builds/dGatedProse/README.md:64` | The closed backlog row and roster row 2 describe the claims join as an ownership check against the dossier's claims table. The join refuses shapes and reads no dossier. |
| F2 | LOW | 7 | `tools/memory-tree/HYGIENE.template.md:362-364` (renders `memory/HYGIENE.md`), engine header `check-memory-hygiene.sh:1994-1999` | HYGIENE item 25 says a name spelled only inside a longer identifier resolves nothing. That is false for hyphenated and flag names, because `-` counts as a boundary. |
| F3 | LOW | 9 | `tools/check-spec-tokens.test.sh:889-893` | No arm checks that a `claims <- <object>` row actually waives a claims hit. That is the remedy the fold documents in three places. |
| F4 | LOW | 2 | `tools/memory-tree/check-memory-hygiene.test.sh:935-941`, `:1594-1595` | Fixtures 218 and 219 fail only on the trailing byte. Deleting the leading boundary test keeps both arms green. |
| F5 | LOW | 12 | `tools/memory-tree/check-memory-hygiene.test.sh:847` | The fixture header still types "eighteen fixtures, tFixture-200 to tFixture-217" after the fold added 218 and 219. |
| F6 | LOW | 6 | `memory/builds/dGatedProse/README.md:65` | Roster row 3 credits unit 3 with "the one kit version bump". This same fold made the build's second move, 2.83 to 2.84. |

### F1 — MEDIUM · the closed record credits the claims join with an ownership check it does not have (ids 5, 8, 10)

The fold re-wrote `memory/backlog/TOOL.md:559` and closed it. The new text says a dossier-claim sentence "is refused when that dossier does not claim it". It also says the join "is built as a join against the dossier's own claims", and that §8 F1 declined only "the ruled resolution against every inventory key". The roster table the fold added repeats this at `memory/builds/dGatedProse/README.md:64`: the claim "names a key that dossier claims".

The tree says otherwise:

- `tools/check-spec-tokens.py:19` says the claims join "grades the SHAPE of a claimed object and resolves nothing". Limit (5) at `:25` is "a claim in the wrong dossier, because no dossier's claims table is read".
- `scan_claims` (`:499` onward) tests each object only against `CLAIM_REFUSALS`, the PATH, GLOB and CODE SYMBOL shape set. Nothing in the file opens a dossier.
- Unit 2's spec says "No key resolution BY THE JOIN, at any point" (`:107`) and "No ownership check" (`:115`).
- The same spec required this row to be "RE-WORDED at landing to name the refusal set" (`:196`, and again in its files-touched table at `:424`). The new text names no refusal set. It describes the ownership mechanism the unit ruled out.

This is new in the fold and is not a round-1 finding. Unit 2 left the row OPEN, and the fold wrote this text as it closed it. It is MEDIUM rather than LOW because of where it sits. It is a closed, permanent record, and memory-recall returns it for a question like "does spec-tokens catch a claim in the wrong dossier". It gives the opposite answer to the checker's own header, which is the false-confidence shape §7 names. It also contradicts a sentence on the same README page: "A check this build adds grades SHAPE, never completeness". It is not HIGH, because no gate reads either sentence and the checker's behaviour is correct. Classes: `two-answers-to-one-question`, and the §6 rule that a value stated in prose beside its owning source rots.

**Fix.** Re-word the backlog row to say what shipped. A sixth join in `tools/check-spec-tokens.py` refuses a dossier-claim sentence whose backticked object is a PATH (`/`), a GLOB (`*` or `?`) or a CODE SYMBOL (an underscore between letters or digits, or a parenthesis). It resolves nothing and checks no ownership, per unit 2's §3 and §8 F1. It declares six limits, a claim in the wrong dossier and a key-shaped object that is not a key among them. Re-word roster row 2 the same way: "a sixth spec-tokens join: a dossier-claim sentence naming a path, glob or code symbol reds". The backlog is mutable, so this is an in-place edit and needs no superseding id.

**Left-shift.** The class is a closing record that restates a mechanism in words its checker's header contradicts. Add a §10 checklist entry for the closing diff review: every backlog row a build closes is read against the header of the checker it names, limits included. A gate does not fit, because the row is free prose.

### F2 — LOW · check 25's whole-word test still resolves a hyphenated name inside a longer hyphenated sibling (id 7)

`test_whole_token` (`check-memory-hygiene.sh:2025-2036`) counts any byte outside `[A-Za-z0-9_]` as a boundary, so `-` is one. Reproduced above: against a reader line spelling only `--dry-run` and `tools/check-spec-tokens.py`, the tokens `--dry` and `check-spec` both resolve. Every backticked by-name token is graded this way, so a clause listing either of them passes check 25 although neither name exists.

The engine comment is accurate as far as it goes: "An end that is punctuation, a path's slash or a dot, is already its own boundary". The overstatement is in the reader document. HYGIENE item 25 now says, at `HYGIENE.template.md:362-364`, that "a name spelled only inside a longer identifier resolves nothing". The same item defines an identifier shape as including "two dashes then a letter" and a slash (`:340-341`). By its own definition, `--dry-run` and `tools/check-spec-tokens.py` are longer identifiers. Most scripts, legs and flags in this repo are kebab-case, so R2's class stays open for them while the shipped document says it is closed. This is a partial mis-fix of round 1's R2: the class is closed for underscore names and after the call-suffix strip, not for hyphenated ones. It is LOW because the fix code is honest and the gap is narrower than R2's, but the §7 rule that a gate's header states what it does not check applies to this residual.

**Fix.** Choose one:

- Extend the boundary. For a token that contains `-` or starts with `--`, treat `-` as a word character on both sides, so `--dry` does not resolve inside `--dry-run`. A path still resolves, because its ends meet `/`, `.`, `:` or a space.
- Narrow the claim. Rewrite the HYGIENE sentence and the engine header at `:1994-1999` to say "an underscore identifier". Then declare, as a residual, that a hyphenated or flag name resolves inside a longer hyphenated sibling.

**Left-shift.** For the first option, add a fixture listing `--dry` against a reader that spells only `--dry-run`. Observe it RED against today's engine, then raise `FLOOR_ASSERTIONS` by one. For the second option, the `kit/dogfood doc parity` leg holds the template and render together, and the engine header joins the §7 residual list.

### F3 — LOW · the composite-token waiver the fold documents has no arm (id 9)

The fold tells authors to waive a claims refusal by the token `claims <- <object>`. It says so in the checker docstring (`check-spec-tokens.py:106-108`), in the spec template (`SPEC-TEMPLATE.template.md:120-121`), and in unit 2's §5 fleet remedy. Arm 2 (`check-spec-tokens.test.sh:889-893`) writes such a row at `:891`, and its comment says the row "waives it". No assertion reads the result, because `arm()` (`:74-84`) checks only the rc and one substring. The bare `tools/nope.sh` row's STALE line alone forces rc 1 and supplies that substring.

The skeptic mutated a scratch copy of the checker so that a claims hit can never be waived: `live = [h for h in hits if h[2] not in waivers or h[1] == "claims"]`. Arm 2 still returned rc 1 and still printed the STALE line, with a now-live claims hit beside it. Arm 1 (`:885`) asserts that the claims hit is live, so it passes under that mutation too. A regression that breaks the documented remedy leaves all 95 assertions green. Both R1 arms do go red on the pre-fold code, so the fold line's "each observed RED against the join as built" is true. The gap is the third property, which no arm observes. It is LOW because the waiver dict is shared and the guards and bar joins exercise it elsewhere (`:579`, `:613`), though never with a claims hit.

**Fix.** Add an arm whose only registry row is `claims <- tools/nope.sh`, with the claims sentence present. Expect rc 0, and expect the `--list` output to carry `WAIVED [claims]`. Alternatively, extend arm 2 to also assert that no live `` [claims] `claims <- tools/nope.sh` — `` line and no ``STALE WAIVER `claims <- tools/nope.sh` `` line is printed. Stage the mutation above, observe RED, then raise `FLOOR_ASSERTIONS` by the arms added.

**Left-shift.** The arm is the gate. The class is a new arm set that observes the refusal directions of a fix but not its remedy. Add a §10 checklist line: when a fold documents a waiver spelling, one arm must use exactly that spelling and expect green.

### F4 — LOW · the leading half of the whole-word test has never been seen to fail (id 2)

Fixture 218 lists `count_shard`, which the reader spells only as `count_shard_rows`. Fixture 219 lists `tRerun`, which the reader spells only as `tRerunAll`. Both fail on the byte AFTER the token. Reproduced above: with the `(!hb || b !~ /[A-Za-z0-9_]/)` half deleted, both still return 0, so the chit arms at `:1594-1595` stay green. The same mutation makes `shard_rows`, found only inside `count_shard_rows`, flip from 0 to 1. The skeptic listed every by-name fixture clause at `:866-941` and found none that names a suffix-spelled token. The product code is correct. But the fold's own rev-12 line says the fixtures were "each observed RED against the substring engine first", which is the instance, and the §7 rule asks for the class. The leading boundary is half that class and has no failing case.

**Fix.** Add fixture 220, a retirement whose by-name half lists `shard_rows` against `treaders.md`, which spells it only inside `count_shard_rows`. Add ``chit 25 'tFixture-220.md (§2 item S1: by name: lists `shard_rows`, which no reader spells'``. Observe it RED against a scratch engine with the leading test deleted, then raise `FLOOR_ASSERTIONS` by one.

**Left-shift.** The fixture is the gate. The §10 class is a two-sided boundary property tested from one side only.

### F5 — LOW · the check-25 fixture header types a count the fold made wrong (id 12)

`check-memory-hygiene.test.sh:847` still reads "CHECK 25's eighteen fixtures, tFixture-200 to tFixture-217". The fold added `tFixture-218` and `tFixture-219` to the same shared tree (`:935-941`, asserted at `:1594-1595`) without touching the header. Its "All LIVE except 210" sentence does not mention the two new LIVE red fixtures either. The comment has no behaviour, but it is a typed count of a derived population, which the charter's §7 bans, and this fold is what made it wrong.

**Fix.** Drop the count and the upper bound, for example "CHECK 25's fixtures, from tFixture-200 upward". Or correct it to twenty fixtures ending at 219, and extend the LIVE sentence.

**Left-shift.** The §10 class "an amendment leaves its other half standing" already covers this. A gate would have to parse comment prose, so the documented check is the right home.

### F6 — LOW · roster row 3 calls unit 3's the only kit version bump (id 6)

`memory/builds/dGatedProse/README.md:65` says unit 3 landed "with the one kit version bump". This fold moved `KIT_MEMORY_TREE_VERSION` again, from 2.83 to 2.84 (`check-memory-hygiene.sh:21`). Spec 1's rev-12 line says so itself: "this fold is the second move". `git log -S` shows two version-move commits from this build, `ddd08686` and `bbabce16`. The roster is the build's front-door summary, and no gate reads it, so this is LOW. Id 6 also named roster row 2, which is fixed under F1.

**Fix.** Write "with the build's first kit version move, 2.82 to 2.83", or drop "the one".

**Left-shift.** None proposed. The roster is authored prose, and F1's documented check already has the closing review read the rows a fold writes.

## Hunted and clean

Each question below came back clean in this range. No lens died, so each one is evidence and not a hole.

- **Punctuation at a token's end.** `test_whole_token` tests the boundary only at an end that is itself a word character, so `--dry-run` and `tools/x.sh` keep resolving by content. F2 is about that choice's reach, not its correctness.
- **A token on one line twice, embedded first and whole second.** The loop resumes at `q = p` and finds the second occurrence. Reproduced: 1.
- **Multibyte text.** A non-ASCII byte or character next to a token counts as a boundary, and the trigger admits only ASCII identifier shapes. Not exercised by a fixture, and not a finding.
- **Does the composite claims token reach every place a token is used?** It reaches the live hit line, the NEAR row, the `--list` HIT, WAIVED and NEAR rows, the waived filter and the stale loop (`check-spec-tokens.py:790-812`). The claims count line counts runs and examined sentences, not tokens, so it is unaffected. The fold updated the `--list` arm's five NEAR expectations and the unit-25 report arm.
- **The fence port.** It blanks the opener and closer lines, emits one line per input line so line numbers hold, and treats the other marker as content inside a fence. The only deliberate difference from the engine's `_unfenced` (`check-memory-hygiene.sh:424-431`) is that the engine drops lines and the port blanks them. Both R3 arms go red on the boolean toggle.
- **Floor raises.** The spec-tokens raise from 91 to 95 matches the four assertions the fold added: two `arm` calls and two `check_claims_verdict` increments. The hygiene raise from 411 to 434 is to the printed count, and its comment says it includes arms the main reconcile brought in unraised. That count was not re-derived here, because the suite was not run.
- **The check-count arm.** `^[A-Z_]*CHECK = ` sees `CHECK = 20` and `ROTATION_CHECK = 24`, so check 24 is counted and the README's 25 is graded against 25.
- **The version bump.** It reached the engine constant, the four templates and their four renders, and nothing else. `kit.toml` derives the version from the engine by pattern, so it needs no edit.
- **The symbol-tier citation.** `<MEMORY_ROOT>/map/generated/symbols.json` in the spec template is the rendered-path form, which resolves.

## By design — not re-reported

- The by-value half of a Readers clause is graded by presence, and records resolve nothing. Both are unchanged from round 1.
- The claims join grades SHAPE and resolves nothing. F1 is about the record describing it, not the join.
- A single liveness predicate for both checkers is routed to `TOOL-dGatedProse-11`, as R4's fix proposed.

## Left-shift summary

| # | Gate or documented check |
|---|---|
| F1 | A §10 checklist entry: each backlog row a build closes is read against the named checker's header and limits. |
| F2 | A fixture where `--dry` against a reader spelling only `--dry-run` reds. Otherwise the residual goes into the engine header and HYGIENE item 25, held by `kit/dogfood doc parity`. |
| F3 | A `check-spec-tokens.test.sh` arm with only a `claims <- <object>` row, expecting rc 0 and `WAIVED [claims]`, observed RED under the no-claims-waiver mutation. |
| F4 | Fixture 220: `shard_rows` against a reader spelling only `count_shard_rows` reds, observed RED with the leading test deleted. |
| F5 | The existing §10 "amendment leaves its other half standing" check; drop the typed count. |
| F6 | None. Covered by F1's documented check. |

State at synthesis: `branch/spec-prose-gates-b41f7c` at `bbabce16` · base `6526ce55` · a full bar running on the tree, not read · `check-memory-hygiene.test.sh` not run · `check-spec-tokens.test.sh` not run · nothing staged by this review.
