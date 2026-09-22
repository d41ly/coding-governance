**Serves:** diff-review TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-4 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8

# Diff review round 3 — the cumulative diff landing on main

**Reviewed range: `747ab9293b611624ec0b47db11c5b280afc40053...HEAD` (HEAD = `3a8e36d4c269b012886a02326cf7de07eaaed0e4`). ROUND 3.**

*Node d, 2026-08-25. Reviews round 2's fix commit and its bar fallout. Adversarial finder fan, then skeptics prompted to REFUTE, then this synthesis. Every finding below was reproduced in this worktree by patching a real file and running a real entrypoint, not reasoned about; every experiment was reverted and the tree left clean.*

## Two corrections to the range before anything else

Both are facts about this record's own framing, and neither is cosmetic.

**The BASE sha this round was handed does not exist.** The orchestrator named `747ab9299f5e9b3f0b7e2a2fbbb0ff3ba0b0f5e0`; `git rev-parse` refuses it. The prefix `747ab929` is unambiguous in this repo and resolves to `747ab9293b611624ec0b47db11c5b280afc40053`, the round-2 fix commit, which is what the heading above names and what every measurement below was taken against. If a later pass greps for the long form it will find nothing.

**That range is one commit and does not contain the code two of the three findings are about.** `747ab929..HEAD` is a single commit, `3a8e36d4`, touching three files — the build's RUN.md, the kickoff guide, and the dead-path waiver registry — for six inserted and four deleted lines. Rounds 1 and 2 both set BASE to the commit *before* the fixes so the fixes fell inside the diff; this round's BASE is the fix commit itself, so the round-2 fixes sit at the boundary rather than inside it. Findings H1 and M1 below are defects in `tools/memory-tree/gen_build_index.py` that landed *in* `747ab929`. They were found by reviewing the cumulative set landing on main, which is this review's stated subject, not by diffing the one commit. Read them as findings against the landing set. A round-4 BASE of `54bb6276` would put the fixes back inside the window.

## Verdict: BLOCKED

Not by a blocker — there is none, and that is real progress. Blocked because two of round 2's own confirmed findings are still open in a form the merge bar cannot see, and one confirmed finding from round 2 exists in neither the fix commit nor the refusal record.

### Review shape

Raw 5 · confirmed 3 · refuted 2 · unverified 0 · precision 0.60.

Zero blockers · 1 HIGH · 2 MEDIUM. Precision fell from round 2's 0.86 to 0.60, which is the expected shape over a hardened surface: the rich seams are gone and the fan starts manufacturing noise. Per §8 that is the signal to review light or skip, not to add agents.

### The shape of what was found

Round 2's through-line was *a check that cannot fail, reintroduced by the fix for a check that could not fail*. Round 3's is narrower and more specific: **the fixes landed, and their arms did not.**

Both code findings are the same defect at one remove. The behaviour was corrected in `747ab929` and the guard that would keep it corrected was either half-written or never written at all. In each case the current suite is byte-identical whether the fix is present, removed, or inverted. That is §7's rule verbatim — a gate you have only ever seen pass is an assertion about nothing — and it is now the third consecutive round in which this build has re-created its own subject matter.

The third finding is bookkeeping rather than code, and it is not minor: a confirmed finding fell out of both catalogs, so the record that a later pass is explicitly directed to treat as its live list now routes that pass at symbols that no longer exist.

---

## HIGH

### H1 — the D4 left-shift arms name `do_bump` and never call it

**`tools/memory-tree/gen_build_index.py:1912`** *(and `:1917`)*

Round 2's H1 found that the arm covering D4 — the `--bump` keep-filter that duplicated all five high-water rows on every run — called neither of the two functions in its label. The fix made half of that real. The arm at `:1915` now reaches `read_slot_table`, a genuine function. The arms at `:1912` and `:1917` still do not reach `do_bump`; they build an inline list comprehension over `read_text(_bhw)` that restates its keep-filter:

```python
lambda: str(len([l for l in read_text(_bhw).split("\n")
                 if "\t" not in l and l.strip()]))
```

`do_bump` is defined at `:1578` and its filter lives at `:1590`. Nothing in the selftest calls it.

**Reproduced.** Patching `do_bump`'s keep-filter at `:1590` from `if "\t" not in l` to `if l.startswith("#")` — the exact D4 spelling — leaves `python tools/memory-tree/gen_build_index.py --selftest` printing `PASS — gen_build_index: all arms held`, exit 0.

The reinstated bug is live data corruption, not a hypothetical. With the break applied, two consecutive `--bump` runs grew `tools/memory-tree/build-readme-slot-highwater.txt` from 25 to 30 to 35 lines: five duplicated rows per run, matching the 5 -> 10 -> 15 progression the comment at `:1902` describes as the original defect.

Nothing else covers it. `check_slot_table` is armed at `:1516` against `SLOT_LIMITS` only, never against the high-water file. `read_slot_table` collapses duplicate keys into a dict, so a corrupted file reads clean to every downstream consumer — the corruption is invisible except by line count. The only other `bump` hits under `tools/memory-tree/` are in `check-verdict-epoch.test.sh` and `hygiene-parity.test.sh`, both about the kit VERSION constant, neither about this file.

The two spellings have already drifted. The inline copy adds `and l.strip()`; `do_bump` handles trailing blanks with a separate pop loop at `:1591-1592`. So the arm and its subject are not the same predicate today, and nothing stops them separating further in either direction. The arm at `:1917` claims *a `--bump` round-trip cannot duplicate a row* while performing no round-trip.

This is the write path that already lost data inside this build.

**Fix.** Call `do_bump` for real. Point `SLOT_HIGHWATER` at a scratch file under `base`, seed it with the comment-plus-data fixture already built at `:1910`, invoke `do_bump(root, conf)`, and assert the round-trip row count is unchanged. The cleaner shape: extract the keep-filter into a named module-level function and call THAT from both `do_bump` and the arm, so there is one predicate and the drift is structurally impossible.

**Left-shift gate.** Stage the `l.startswith("#")` break and confirm the new arm REDs before landing it. Then generalise one level up, because the class is *an arm that names a function and restates it instead*: add a selftest arm asserting that every `arm(...)` label mentioning a module-level function name appears in a lambda whose source actually references that name. That predicate is cheap over this file's own source and catches the next copy before it ships.

---

## MEDIUM

### M1 — M3's canon-scoping guard landed with no arm at all

**`tools/memory-tree/gen_build_index.py:1181`**

Round 2's M3 found that the duplicate-heading scan covered every `## ` heading rather than only the canonical ones, so a repeated NON-canonical heading was reported as a duplicated canonical slot AND suppressed the accurate `heading outside the canon` message through the early return at `:1183`. The fix scoped the predicate with `h in canon_heads and`. The arm the round-2 record specified was never added.

**Reproduced.** With `h in canon_heads and` deleted from `:1181`, both entrypoints stay green:

```
--selftest      PASS — gen_build_index: all arms held                                             exit 0
--check-format  build-index: slot contract clean (62 build README(s); heading canon BOUND on 1)   exit 0
```

Baseline unpatched output is byte-identical, so the guard's removal is invisible to the bar.

The two arms that look like candidates genuinely cannot reach it. The outside-the-canon arm at `:1880` appends a single `## Afterword`, so `count(h) > 1` is False with or without the guard. The D2 arm at `:1898` repeats `## Build-level rules`, which IS in `canon_heads`, so the predicate is True on both sides. A repo-wide grep for `Afterword`, `appears more than once` and `heading outside the canon` across `.py`, `.sh`, `.json` and `.md` finds no other coverage — no shell test, no gate leg, nothing outside this one file.

The guard is not decorative. On a README repeating a non-canonical heading, the guarded function returns `[(29, 'heading outside the canon: ## Afterword'), (33, ...)]`; the unguarded one returns `[(29, 'canonical slot heading appears more than once: ## Afterword'), (33, ...)]` — the exact wrong-diagnosis regression the comment at `:1178-1180` describes, plus the suppression that comment warns about.

The round-2 record named the required arm and named its negative half as the load-bearing one. The code shipped; the arm did not.

**Fix.** Add the specified arm: a fixture repeating a NON-canonical heading (`## Afterword` twice), asserting the emitted string contains `outside the canon` AND does not contain `more than once`. The negative half is the load-bearing one — an arm asserting only the positive passes under both spellings.

**Left-shift gate.** Stage the guard's removal and confirm the arm REDs before landing. The class-level gate is the same one H1 needs, approached from the other side: no fix commit closes a finding until its staged break has been observed RED. That is unenforceable by a script, so it belongs in the build method's fix-pass checklist as a documented check — the compensating manual check §7 requires when a class cannot be gated.

---

### M2 — round 2's confirmed M2 landed in neither the fix nor the refusal record

**`memory/builds/dFramedEntrypoint/reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md:23`**

Round 2 confirmed that the round-1 record's symbol-name caveat was false: it claimed a concurrent rename was uncommitted and outside the reviewed range, when that rename had in fact landed. The finding was neither fixed nor parked. It is in no catalog.

**Verified at HEAD, every element.**

Line 23 still reads that the rename *is uncommitted and outside the reviewed range*. `git log` on that path returns exactly one commit, `2b6b2e62` — the same commit that landed the rename — so the claim was false when it was written, and no addendum has been added since. Grepping the record for `addendum`, `2b6b2e62`, `measure_slot_sizes` and `check_contract_registry` returns zero hits.

The cited symbols are dead. `git grep` under `tools/` returns zero source hits for `assert_contract_registry`, `_canon_violations` and `budget_findings`, and none for bare `slot_sizes`. Only stale `__pycache__` binaries match.

Both round-1 items that instruct against those names are still open. `gen_build_index.py:1042` is still `if lines[i] in heads:`, and round-1 line 221 says to fix it *in `slot_sizes`*. `check_contract_registry` runs only at `:1508` while `read_contract_registry` is still called bare at `:1562`, `:1581` and `:1611`, and round-1 line 310 says to call *`assert_contract_registry`*. Round 2's own scope section designates the round-1 record as the live list for its open findings, so a later pass following it greps deleted symbols and finds nothing.

M2 is in neither catalog. The body of `747ab929` enumerates B1, H1, M1 and M3 by name and never mentions M2. `3a8e36d4` is bar fallout only — a manifest body pointer and a re-keying of the line-keyed dead-path waivers. The Parked section of `memory/builds/dFramedEntrypoint/RUN.md` carries no M2 refusal; its last two entries are bare verdict lines. There is no round-3 record in `reviews/` other than this one.

*Refutation attempted and rejected.* This is not a restatement of round 2's M2. That finding claimed the record was false. This one claims a confirmed finding survived the fix pass in neither the fix nor the refusal record, which §7 and §8 require to exist in one of the two.

**Fix.** Either add the dated addendum the round-2 record asked for — correct line 23 to name `2b6b2e62`, then map every cited old spelling to its HEAD spelling, including the three the original caveat omitted — or park an explicit refusal in `memory/builds/dFramedEntrypoint/RUN.md` stating why M2 is not being closed. Either is acceptable. Neither is optional.

**Left-shift gate.** This one is gateable and worth gating, because it is the third bookkeeping defect this build has produced in its own records. Add a hygiene check: for each review record under a build's `reviews/` whose verdict is BLOCKED, every finding id in its headings must appear in a later record, in a fix commit body reachable from the build, or in that build's Parked section. A confirmed finding with no downstream mention reds. The predicate is a grep over already-structured text and needs no new authored data.

---

## Refuted

Two of the five raw findings were dropped by the skeptic stage.

The first alleged that `3a8e36d4`'s re-keying of `tools/dead-path-waivers.txt` masked a real dead path rather than following a line shift. It does not: the three re-keyed rows point at the same surrounding text at their new line numbers, and RUN.md already carries a dated decision recording that the registry's `<path>:<line>` keying forces exactly this re-key on any insertion above a waived hit.

The second alleged that the kickoff guide edit in `3a8e36d4` broke a documented invocation. The changed line is a body pointer whose target exists and resolves.

## What this round did NOT cover

The round-1 record remains the live list for its own open findings, with the correction that its symbol names are stale — see M2 above, and do not grep the names it cites until that record is amended.

No gate run was performed for this round. The findings were reproduced by patched-copy experiments against `--selftest` and `--check-format` only. A full bar with `GATE_FULL=1 GATE_SELFTESTS=1` is still owed before landing, and this record is not evidence about it.

The two code findings sit outside the one-commit diff this round's BASE defines, as the range note above states. They are findings against the cumulative landing set.
