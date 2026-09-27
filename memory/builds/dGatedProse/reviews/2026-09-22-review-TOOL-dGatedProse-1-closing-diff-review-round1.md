**Serves:** diff-review TOOL-dGatedProse-1 TOOL-dGatedProse-2 TOOL-dGatedProse-3 TOOL-dGatedProse-4 TOOL-dGatedProse-5

# Closing diff review, round 1 — dGatedProse units 1–5: check 25's Readers clause, the claims join, the guide cap, M4's precision bound, the corpus migration

Node `d` · 2026-09-22 · Tier-2 · on `branch/spec-prose-gates-b41f7c` · adversarial fan through `tier2-review.js` (4 finder lenses → 5 skeptic batches → this synthesis). Every confirmed finding was re-read at source in this synthesis before it was adjudicated. The two `check-spec-tokens.py` classes were also re-executed here, by importing the module and calling `scan_claims` and `read_waivers` directly. Nothing below rests on the skeptic's word alone.

**Reviewed range:** `663a0dec891d35716e8376480784ed01f5131977...6526ce5597489edd6066d635845bf53be778c4f0` — **ROUND 1**. 29 commits, 58 files, +9077/−77. The primary subject is 16 of those files, +944/−42: `check-memory-hygiene.sh` and its test (check 25), `check-spec-tokens.py` and its test (the claims join), `template-size-limits.txt`, the memory-tree conf example and README, the four kit templates (HYGIENE, SPEC-TEMPLATE, BUILD-METHOD, ANNOTATION-STYLE) and their renders under `memory/`, and `memory/guides/SESSION-KICKOFF.md`. The 37 migrated items across 19 specs were subject only for clause correctness.

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing, and no finding is HIGH. The five units do what their specs say. Check 25 triggers on the retirement vocabulary, grades the two halves by resolution and by presence, and refuses an unresolved name while printing the escape spelling. The claims join refuses PATH, GLOB and CODE SYMBOL objects, and its canary holds over 4 arms. The cap, the version bump and M4's bound are in place. `check-spec-tokens.test.sh` is **PASS (91 assertions)** at HEAD. No lens produced a confirmed finding against any of the 37 migrated clauses, so the unit-5 migration stands as written.

This round finds two gates that can be satisfied without the property they name, both MEDIUM. The claims join keys its hits on the bare object token. The waiver registry is one dict over every join, so a `[path]` row silently waives a claims refusal on the same string, and the claims hit keeps that row from ever reading stale. That is a guard sharing state with what it guards, and the guards join avoided it on purpose. Separately, check 25 resolves a by-name reader by bare substring, so a name no file spells passes whenever a longer identifier contains it. Two LOWs remain. The claims join's fence blanker is a weaker copy of the engine's fence machine, although its docstring says it is the same one. The shipped TEMPLATE-SPEC also uses "every LIVE spec" for two different populations. All four fixes are a few lines plus an arm, and should fold before the close.

## Review shape

Raw **14** · confirmed **8** · refuted **6** · unverified **0** · precision **0.57**.

Precision clears the 0.5 floor §8 sets, but not by much. The eight confirmed collapse to **4 items**. Two groups reported the same defect with the same repro from different lenses: ids 3, 7 and 11 (the waiver key) and ids 4, 8 and 10 (the fence toggle). I merged them at write time; the pipeline discarded no duplicates. The six refuted (ids 1, 2, 6, 9, 12 and 14) reached this synthesis only as a count, not as text, so they are not re-adjudicated here.

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 2 MEDIUM · 2 LOW** (4 items).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 4 MEDIUM · 4 LOW** (8 findings). Every id takes the severity of the item that holds it. Ids 3 and 7 were rated low by their finders and take the MEDIUM of R1. Id 5 keeps its finder's MEDIUM although its skeptic leaned low. Each item says why.

## Run integrity

- Lenses **4/4** returned, **0 DIED**.
- Skeptic batches **5/5** returned, **0 DIED**.
- **0** contradictory verdicts demoted to unverified, **0** spurious verdicts discarded, **0** duplicates removed by the pipeline.

No stage died, so a zero in this report is evidence of absence and not a hole. That includes zero HIGH or BLOCKER findings and zero confirmed findings against the migrated clauses. The two duplicate groups were judged by hand in this synthesis, as stated above.

What this synthesis ran:

- `scan_claims` called directly on the claim `` `memory/map/features/runlog.md` claims `tools/run-gates.sh`. `` in four shapes. Unfenced it gives 1 run and one PATH hit. Inside a backtick fence it gives 0. Inside a `~~~` fence it gives **1 run and one PATH hit**. After a `~~~` block holding a lone backtick-fence line it gives **0 runs**.
- `read_waivers` over the live registry: `tools/run-gates.sh` is a key.
- `python tools/check-spec-tokens.py` at HEAD: 24 live specs, 698 terminal, 22 waivers. The claims join examined 0 dossier-claim sentences with its canary held over 4 arms.
- `bash tools/check-spec-tokens.test.sh`: **PASS (91 assertions)**, rc 0, output to a file and grepped.
- Check 25's attribution pass (`check-memory-hygiene.sh:2008-2040`) read against `test_bounded_word` (`:1207`) and fixtures 204–209.
- The DEFERRED population counted with `git grep`.

What it did not run: the bar, `check-memory-hygiene.test.sh` and the check-25 substring repro. The skeptic's scratch-repo repro for that one is recorded under R2, and the code at `:2032` makes the claim directly legible.

## Findings

| # | Sev | Ids | Where | What |
|---|-----|-----|-------|------|
| R1 | MED | 3, 7, 11 | `tools/check-spec-tokens.py:781`, `:786-789` | Claims hits are keyed on the bare object. The one global waiver dict then lets a `[path]` row waive a claims refusal on the same string, and the claims hit keeps that row from reading stale. |
| R2 | MED | 5 | `tools/memory-tree/check-memory-hygiene.sh:2032`, `:2014` | Check 25 resolves a by-name token with `index(ln, tok) > 0`, a bare substring. A reader name no file spells passes whenever a longer identifier contains it, and `run()` stripped to `run` resolves almost anywhere. |
| R3 | LOW | 4, 8, 10 | `tools/check-spec-tokens.py:502-506`, docstring `:498-500` | The fence blanker toggles only on backtick fences, ignores `~~~` and is not marker-matched. The docstring says it is the engine's toggle. |
| R4 | LOW | 13 | `tools/memory-tree/SPEC-TEMPLATE.template.md:108` vs `:311` (renders `memory/TEMPLATE-SPEC.md`) | "every LIVE spec" means the whitelist OPEN, SPECCED, INPROGRESS or BLOCKED for the claims join, and "not CLOSED or WONTDO" for check 25. DEFERRED sits between the two meanings. |

### R1 — MEDIUM · the claims join shares the waiver key space with the path join (ids 3, 7, 11)

`tools/check-spec-tokens.py:781` builds each claims hit as `(f, "claims", obj, …)`, with the bare claimed object in the token slot. `:786` filters every join's hits with `live = [h for h in hits if h[2] not in waivers]`. `read_waivers` (`:568-579`) keys the registry on the text before the tab, and the `[path]` or `[leg]` tag lives only in the reason string, so nothing parses it as a join key. The effect runs in two directions:

- **A waiver swallows a refusal.** Reproduced here: `scan_claims` on `` `memory/map/features/runlog.md` claims `tools/run-gates.sh`. `` returns a PATH hit whose object is exactly `tools/run-gates.sh`, and that string is a key in the live registry. The hit reports `WAIVED` and the checker exits 0. A skeptic reproduced the same thing end to end in a scratch repo with `memory/project/MEMORY.md`: rc 0, nothing printed by default, and `WAIVED [claims] … PATH at line 7` under `--list`.
- **A refusal keeps a stale waiver alive.** The `:787-789` loop adds the claims hit's token to `seen_waived`. A `[path]` row whose path hit has been fixed therefore stops reading stale while any claims sentence names the same string. That defeats the stale-row check.

The existing joins mostly stay apart by token shape. A leg token has no slash, a cite token carries `:line` and a bar token carries spaces. The claims join refuses every `/` token whether or not git tracks it, so it is the first join whose hits take the path join's exact shape. The guards join met the same collision and built a composite `leg <- path` token for it (comment at `:722-723`, token at `:752`). Unit 2's spec names the guards join as the template it follows. It also names "one row with a reason" as the fleet remedy for a claims red. Under bare keying, that row would also waive any path-join hit on the same token across the whole corpus.

Why MEDIUM and not LOW: this is a guard sharing state with what it guards, the trust class this review was briefed to hunt. It departs from a documented template, and the unit's own prescribed remedy walks into it. Why not HIGH: it is latent. The live run examines 0 claim sentences, and a collision needs a claim on one of the 22 waived strings. Classes: `two-answers-to-one-question` (the guards join's key versus this one) and the §7 "a guard that shares a variable with the thing it guards".

**Fix.** Emit claims hits under a composite token no path or leg row can equal, `f"claims <- {obj}"` in the guards join's spelling, and use the same form for the NEAR rows. State that waiver spelling in the join's WHAT IT DOES NOT CHECK block and in the unit-2 spec's remedy sentence.

**Left-shift.** Two arms in `check-spec-tokens.test.sh`, each observed RED against today's code before wiring. First, a registry row naming the bare object plus a live spec claiming it gives a claims hit and exit 1. Second, a `[path]` row with no path hit left plus a claims hit on the same string still reads stale.

### R2 — MEDIUM · check 25 resolves a reader name by substring (id 5)

`tools/memory-tree/check-memory-hygiene.sh:2032`:

```awk
for (i = 1; i <= np; i++) if (!(pl[i] in got) && index(ln, pl[i]) > 0) { got[pl[i]] = 1; left-- }
```

The prefilter at `:2014` is `git grep -F -f`, also a substring match, and no word-boundary step sits between the two. A by-name token that no reader spells as a whole identifier therefore resolves whenever a longer identifier contains it. The skeptic reproduced this with a scratch copy of the engine in a scratch repo. The only reader was a guide spelling `count_shard_rows_total`, and the clause `` by name: `count_shard` and `shard_rows_to` spell it `` passed check 25 although neither name exists anywhere. Swapping in `tZzz` redded, so the arm was live in that run. Three shapes reach it:

- A deleted helper with a surviving longer sibling, such as `check_audit` beside `check_audit_green`. That is exactly the retirement case check 25 exists to grade.
- Any short name after the `()` strip. `run()` becomes `run`, which resolves in nearly every reader file.
- The fixture tree itself. `memory/guides/treaders.md` spells `count_shard_rows` (`check-memory-hygiene.test.sh:860`), so a clause listing `count_shard` would pass. Fixture 208 (`:884-886`) uses the disjoint token `tAbsentReader`, so the arm only ever sees a token that shares nothing with a real name.

HYGIENE item 25 (`HYGIENE.template.md:356`) and S5 define resolution as "where a reader spells it". The header at `:2003-2004` names one residual it accepts, a reader spelling a name that is no longer live, and S5 adds a shared basename. Substring over-match is not among them, and §7 requires a gate's header to state what it does not check. The unit-1 measurement counted false reds only, never false passes, and the engine already carries the right primitive, `test_bounded_word` at `:1207`.

Why MEDIUM, against the skeptic's lean to low: this is the half the gate grades by RESOLUTION, it is the primary subject, and the short-name shape turns resolution into near-certain green rather than an edge. Why not HIGH: a clause still has to exist and name something, the by-value half is untouched, and no migrated clause was found to depend on it. Classes: `id-matched-as-a-substring` and the §7 "gate the class, not the instance".

**Fix.** Keep `git grep -F -f` as the superset prefilter. In the attribution awk, accept an occurrence only when the byte before it and the byte after it are not `[A-Za-z0-9_]`. Apply that test only at each end of the token that is itself an identifier character, so a path or a space-bearing fragment keeps resolving by content. Loop over occurrences the way `test_bounded_word` does, or call it. If some substring behaviour is deliberate, state it in the `:1995-2007` header and in HYGIENE item 25.

**Left-shift.** A fixture in `check-memory-hygiene.test.sh`: a guide spelling only `count_shard_rows_total` and a clause listing `count_shard` must red with the unresolved-name message. A sibling arm listing `run()` against a reader where `run` occurs only inside longer words must red too. Stage both against today's engine and observe RED first.

### R3 — LOW · the claims join's fence blanker is a weaker copy of the engine's (ids 4, 8, 10)

`tools/check-spec-tokens.py:502-506` sets `fence` true for any line whose left-stripped text starts with three backticks, and flips a boolean on every such line. The docstring at `:498-500` says this is "the same line-level toggle the hygiene engine reads a spec with". It is not. The engine's `_unfenced` (`check-memory-hygiene.sh:421-430`) and `gen_build_index.unfenced_lines` both recognise `~~~` and close a fence only on the marker that opened it. The repo has already left-shifted this exact class once: `row_grammar.py:220-224` records replacing "a private boolean toggle" with the marker-matched reader as the two-answers class and the weaker copy. Reproduced here, both directions:

- **False green.** After a `~~~` block holding a lone backtick-fence line, which is how a spec shows a fenced example, the toggle stays flipped. The unfenced refused claim that follows returns `(0, [], [])`, and everything below it is blanked until the next backtick-fence line.
- **False red.** A refused claim inside a `~~~` block returns one PATH hit at its line. Declared limit (3) and S4 promise that fenced examples are blanked.

LOW because it is latent. No tracked spec under `memory/builds/*/spec/` opens a `~~~` fence today, and the join examines 0 sentences. The docstring is still a false parity claim over a second fence grammar. Classes: `two-answers-to-one-question` and the fence-machine class `TOOL-aMouldedFolio-5` recorded.

**Fix.** Port the engine's machine. Strip a trailing CR, open on a line matching three backticks or `~~~` after optional whitespace, remember the marker, close only on the same marker, and treat the other marker as content while inside. If porting is refused, correct the docstring and limit (3) to say that only backtick fences are blanked.

**Left-shift.** Two direct-half arms in `check-spec-tokens.test.sh`. First, a `~~~` block holding a lone backtick-fence line, followed by an unfenced refused claim, must give exactly one hit on the unfenced line. Second, a refused claim inside a `~~~` block must give zero hits.

### R4 — LOW · one shipped document, one word, two populations (id 13)

`tools/check-spec-tokens.py:143` defines LIVE as the whitelist `OPEN|SPECCED|INPROGRESS|BLOCKED`, which leaves DEFERRED out. The run prints "698 terminal spec(s) not graded", and DEFERRED specs are counted there. Check 25 uses the negative test `rilive = (hdr !~ /^\*\*Status:\*\* (CLOSED|WONTDO)/)` (`check-memory-hygiene.sh:1329`), and HYGIENE item 25 spells it out at `HYGIENE.template.md:334`. This build added both paragraphs of `SPEC-TEMPLATE.template.md`: `:108` says the claims join refuses "in every LIVE spec" in the whitelist sense, and `:311` says check 25 asks it "of every LIVE spec" in the negative sense. Nothing on the page tells the two apart.

The corpus holds 9 DEFERRED specs at HEAD, two of them migrated by unit 5 (`TOOL-aWalkedCorpus-2`, `TOOL-dScaffoldedMirror-9`). A skeptic confirmed that a DEFERRED spec carrying a refused claim is counted terminal and never refused, while check 25 grades the same spec. The code behaviour is inherited by design: unit 2's S1 says "over its existing live-spec population", and unit 1 recorded the divergence, but only in a record. The shipped reader document misstates the claims join's coverage, and the red arrives unannounced the day a DEFERRED spec is resumed. LOW because that red is loud when it comes. Class: `two-answers-to-one-question`.

**Fix.** In the TEMPLATE-SPEC bullet at `:108` and in the checker's claims header, state the claims join's population as OPEN, SPECCED, INPROGRESS or BLOCKED, and say that DEFERRED is not graded. Better, grade the claims join on the engine's negative test, so both checks read one liveness predicate and DEFERRED stops being reported as terminal. That is a behaviour change to a shared population and belongs in a spec of its own.

**Left-shift.** For the prose fix: the `kit/dogfood doc parity` leg holds template and render together, and the §10 checklist gains "a population word defined twice in one shipped doc". For the predicate fix: an arm where a DEFERRED spec carrying a refused claim gives a hit.

## By design — not re-reported

Stated in the specs and confirmed unchanged at source. None of these is a finding.

- Records resolve nothing for check 25. A name quoted only by a record under `memory/` outside the allowlist does not resolve (header `:1995-2001`, applied at `:2022-2026`).
- The by-value half is graded by presence, not resolution. Completeness of either list is the author's question (`SPEC-TEMPLATE.template.md:315`).
- Check 25 has no cutoff date, and neither does the claims join (owner, 2026-09-21).
- A reader spelling a name that is no longer live still resolves. The `:2003-2004` header states it; R2 is about a name that is spelled by nobody.
- The claims join refuses every `/` token whether or not git tracks it. That is the map contract the join enforces; R1 is about how its hits are keyed, not what it refuses.
- The guide cap raise to 98304 bytes and 1200 lines, the build-method size row at 30720 bytes and 400 lines, and the single version bump to 2.83 are owner rulings recorded in the build.

## Checklist classes run

These produced a confirmed finding:

- The §7 shared-variable guard rule, and `two-answers-to-one-question`: R1.
- `id-matched-as-a-substring`, and the §7 "gate the class, not the instance": R2.
- The fence-machine class and `two-answers-to-one-question`: R3.
- `two-answers-to-one-question`: R4.

These were run and came back clean on this range:

- `fixture-passes-by-finding-nothing`. Check 25's fixtures 204–209 carry passing and redding arms, and the claims arms carry a canary over 4 arms.
- `text-mode-read-eats-a-bare-cr`. `read_waivers` decodes bytes rather than reading in text mode, and the engine's `_unfenced` strips a trailing CR before its fence test (`:424`).
- `swallowed-delegate-reads-as-clean`. Check 25's attribution pass prints a terminal `D`, and its absence reds through fail 25 (`:2042-2046`).
- `vacuous-selector-empty-population`. An empty token batch runs no grep at all (guard at `:2011`, rationale at `:2006-2007`), so nothing rests on an empty pattern file matching nothing.

## Left-shift summary

| # | Gate or documented check |
|---|---|
| R1 | `check-spec-tokens.test.sh` arms: a bare-object registry row does not waive a claims hit; a path row still reads stale beside a claims hit on the same string. |
| R2 | `check-memory-hygiene.test.sh` fixtures: `count_shard` against a reader spelling only `count_shard_rows_total` reds; `run()` against a reader with `run` only inside longer words reds. |
| R3 | `check-spec-tokens.test.sh` direct-half arms: a `~~~` block holding a lone backtick-fence line, then an unfenced claim, gives one hit; a claim inside `~~~` gives zero. |
| R4 | Prose now, held by the `kit/dogfood doc parity` leg. A DEFERRED-spec arm if the predicate is unified. |

State at synthesis: `branch/spec-prose-gates-b41f7c` at `6526ce55` · base `663a0dec` · `check-spec-tokens.test.sh` PASS (91 assertions) · `check-memory-hygiene.test.sh` not run · bar not run.
