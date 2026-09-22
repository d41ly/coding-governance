**Serves:** spec-audit DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18

# Spec audit round 2 — did the round-1 fold hold, and what did it break

*Node d, 2026-09-02, round 2, on `branch/kit-update-complexity-af0fb0` against gov HEAD `3c7cd2b4`. Round 1 returned BLOCKED with 35 confirmed findings; all 30 reported items were folded across two commits — `b17f22ed` for the six blockers and the inverted premise, `3c7cd2b4` for the remaining 24. Fifteen of the 25 specs moved a rev, and `TOOL-dRetiredFork-4` was rescoped from an absorption to a reconciliation and dropped from Tier-2 to Tier-1. This round treats the fold text itself as unreviewed surface, which is round 1's own left-shift note applied to round 1's own output: **every claim a fold sentence makes about existing code was re-derived at HEAD before it was graded.** `HOOK_MARKER`, `merge()` and the dedup branch were read at their definitions in `tools/settings-merge.py`; every gate name in every §7 was resolved against the 87 rows of `tools/gate-legs.json`; every backticked path was put through `git ls-files`; `tools/install-prefix-carried.txt` and check 3's whitelist `case` in `tools/memory-tree/check-memory-hygiene.sh` were counted rather than quoted; `tools/unattended/adopt-unattended.sh` and `tools/memory-tree/adopt-memory-tree.sh` were compared for which token each substitutes; `tools/hooks/scratch-guard.test.sh` and `tools/hooks/kit.toml` were read to decide what `TOOL-dRetiredFork-14` S2 actually withdraws. Review shape: **raw 74, confirmed 62, refuted 12, unverified 0, precision 0.84**, consolidated below into 30 distinct defects — the raw set carried heavy duplication because the lenses reached the same fold seams independently, and a defect is listed once here with every address it occupies.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md@8ce9344c5d3c` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-2.md@5e7ec4aefc0b` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md@6404ce8661bf` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-4.md@f81e863eaec2` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-5.md@1008b4df9f3f` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md@8c73238c1ab6` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-7.md@be211bac4513` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-1.md@9fe7e4e8a56f` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-10.md@8a25911cc67a` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-11.md@e6bb180724ee` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md@210fba302470` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-13.md@1c619bc41b6b` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md@1504b519a8a3` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-15.md@8f5077c7a348` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-16.md@3f12065480f6` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-17.md@a700659aa1ea` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-18.md@9810d7eb5db2` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-2.md@446a079ec450` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-3.md@f3f2879ad5fa` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-4.md@4f7664dcd8b3` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md@aa3a5b593dcc` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-6.md@7f8eb5036cb7` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-7.md@93b19570f183` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-8.md@e159845e1c14` · `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-9.md@cb8f0b0693f8`. **ROUND 2.**

## Verdict: BLOCKED

Five blockers stand after adjudication, and four of the five were **created by the fold**, not survived by it. That is the finding above the findings: round 1's own left-shift note — fold text is unreviewed surface — is now measured rather than asserted. A fold sentence is authored under time pressure, makes fresh claims about code nobody re-read, and lands in a document no gate grades. Of the 30 defects below, 21 did not exist at `b0108f13`.

Three failure shapes account for almost all of it, and each has a mechanical fix.

**The fold corrected the instance and not the class.** `TOOL-dRetiredFork-14` rev-2 records B4 as fixed — it changed AC5's untracked `.claude/hooks/agent-cap.test.sh` to the tracked path and left the byte-identical string in AC3, one line above, which is the criterion that actually observes the unit's highest-risk mitigation. This is the AGENTS.md §7 rule the build exists to enforce, broken in the act of enforcing it.

**The fold prepended corrections instead of substituting them.** `TOOL-dRetiredFork-14` §10 now carries the corrected sentence, a truncated fragment reading `The seam is — `, and rev-1's refuted conclusion, in that order. The section asserts both that the seam is insufficient and that no new mechanism is built. `TOOL-dRetiredFork-12` did the same at the section level: S1 struck `TOOL_ROOT` and proved it unrenderable, while §4 Data model and §10 still declare the two-token pair. `TOOL-dRetiredFork-3` fixed the probe sentence in §10 and left the recall-terms line — the half BUILD-METHOD M7 actually re-executes.

**The fold moved work between units and reconciled only one side.** `b17f22ed` rescoped `TOOL-dRetiredFork-4` to a reconciliation that "absorbs nothing" and dropped the build's fix count to eight; `3c7cd2b4` then rewrote `DEPL-dRetiredFork-6` AC2 — the fix for round 1's H2, whose whole defect was a criterion a correct implementation fails — and kept `TOOL-dRetiredFork-4` in the falsification set. H2's exact shape, one commit later, in the file H2 was fixed in. The same non-reconciliation produced the build's worst defect: B1's fold wrote `DEPL-dRetiredFork-3` AC10 as the single criterion carrying the README's done-condition, H3's fold wrote `DEPL-dRetiredFork-1` AC6 permitting the `unattributed` count to survive, and `tools/govkit/govkit.py:6566-6573` withholds the `gov_commit` re-stamp AC10 demands while any such row exists. Both criteria can be green and the build still fails its README.

Two counts are reported for honesty rather than alarm. Round 1 ran at precision 0.46; this round ran at 0.84, which is the expected direction — a folded corpus has fewer speculative seams and the surviving defects are concrete. And the four systematic checks round 1 skipped came back **three clean, one dirty**, reported in full below so a green row is never misread as an unrun one.

## Severity table

| # | Severity | Subject | Address | Defect |
|---|---|---|---|---|
| 1 | blocker | DEPL-6 | §6 AC2, §1, §4 Rollout, §5 | The falsification set still counts `TOOL-dRetiredFork-4` and still says nine; a correct verb reds AC2 |
| 2 | blocker | DEPL-3 / DEPL-1 | DEPL-3 §6 AC10 vs DEPL-1 §2 S6 / §6 AC6 | The done-condition demands a stamp the engine withholds, and its sibling permits the blocker to survive |
| 3 | blocker | TOOL-12 | §4 Data model, §10, §5 user docs | S1 declares one token; §4 and §10 still declare two, and a builder ships an unresolved brace |
| 4 | blocker | TOOL-14 | §6 AC3 | The criterion observing S3 names an untracked path inside the directory S2 withdraws |
| 5 | blocker | TOOL-14 | §2 S1/S1b | The repath is built only in the engine default; two of three hooks wire from fragment files that hardcode the withdrawn path |
| 6 | high | DEPL-3 | §6 AC10, second sentence | The inCMS half of the done-condition is gated on a receipt repair no unit in the roster owns |
| 7 | high | TOOL-14 | §10 Reuse audit | The correction was prepended, not substituted; the section asserts both verdicts and carries a truncated fragment |
| 8 | high | TOOL-14 | §2 S3, §7 | S2 withdraws scratch-guard's wired copy; its parity arm hard-FAILs on absence and no criterion or leg names it |
| 9 | high | DEPL-7 | §2 S6 vs §3, §6 AC7 | The README's delegated deliverable is mandated by §2, forbidden by §3 and observed by nothing |
| 10 | high | TOOL-17 | §2 S1/S2, §8 F1 | Half the unit's title is unobservable, and an UNRESOLVED fork recommends the opposite carrier set |
| 11 | high | TOOL-5 | H1 title, §1, §3 | The refuted "four guarded arms" survives in the three places a reader meets first, and the README renders the title |
| 12 | medium | DEPL-3 | §3 `generated` non-goal vs §2 S2, §6 AC2/AC10 | Named-versus-run: the non-goal and the central mechanism answer one question opposite ways |
| 13 | medium | DEPL-2 | §5 error/empty row vs §6 AC4, §2 S6 | `0 new` and byte-identity cannot both hold, and nothing observes `0 new` |
| 14 | medium | DEPL-2, DEPL-3 | §5 testing rows vs §2 S6 (and DEPL-3 §9 rev-2) | Stale arm counts: both say four, both S6 lists enumerate five, DEPL-3's rev line says six |
| 15 | medium | TOOL-13 | §1, §2 S1 | 32 files carrying 259 occurrences; the ratchet says 33 rows sum to 259 |
| 16 | medium | TOOL-13 / TOOL-8 | TOOL-13 §3 third bullet vs TOOL-8 §2 S6 | The class of non-test checkers is disclaimed on the strength of its one owned member; 41 occurrences stay orphaned |
| 17 | medium | TOOL-3 | §10 recall-terms line | The fold fixed the query and left the terms — the half M7 re-runs — copied from the install-prefix units |
| 18 | medium | TOOL-3 | §4 Data model vs §2 S6 | Five registries versus nine; nine is measurable and correct |
| 19 | medium | TOOL-16 | §6 AC3 vs §3; §2 S2 vs §6 AC4 | AC3 names a path gov does not track and its own non-goal forbids; S2's kit-README half is unobserved |
| 20 | medium | TOOL-15 | §3 third non-goal vs §2 S1/S3 | The unit believes it added no disarming key, so neither disarming value is guarded |
| 21 | medium | TOOL-4 | §2 S1 | The sole pointer to the unit's evidence cites `ARCH-aFerriedToolkit-3`; every other mention is `ABL-` |
| 22 | medium | DEPL-1 | §5 security row vs §2, §6 | A stated grading obligation on the build's highest-severity path has no scope item and no criterion |
| 23 | medium | DEPL-3 | §6 AC11 vs §7 | The fold removed `runbook parity` correctly and replaced it with nothing; the program has zero callers |
| 24 | medium | TOOL-12 | §7 Gates | The rename put the unit's central checker's leg out of the list and a leg it does not touch into it |
| 25 | medium | TOOL-9, TOOL-8, TOOL-14 | §7 Gates | The rename collapsed distinct legs onto one name; TOOL-9's duplicate also dropped `playbook validity gate` |
| 26 | medium | TOOL-14 | §7, §5 testing row | The unit's central code change has no leg named against it, and §5 claims a fixture DEPL-3 owns |
| 27 | medium | TOOL-11 | §7 Gates | Names `check-wiring self-test` for a file it does not touch; omits the leg every criterion runs |
| 28 | low | DEPL-3 | §6 label sequence | AC8 trails AC11 — the renumber inserted AC9-AC11 ahead of a criterion it left in place |
| 29 | low | TOOL-8 | §3 first bullet | A cut-line section that declares itself empty and then lists a genuine non-goal |
| 30 | low | TOOL-14, TOOL-12, DEPL-2 | TOOL-14 §2 S1/S1b, TOOL-12 §2 S1, DEPL-2 header | Four fold-authored details: a citation four lines short, a false premise, an undecided fork outside §8, a missing `ratified` pointer |

---

## Blockers

### 1 — `DEPL-dRetiredFork-6` still counts a unit that absorbs nothing, and still says nine

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-6.md` §6 AC2 (line 102), §1 (line 15), §4 Rollout (lines 66-67, 74), §5 testing row (line 91).

**The defect.** The H2 fold rewrote AC1 and AC2 to name unit ids instead of counts — the right correction — and kept `TOOL-dRetiredFork-4` among "the SIX inCMS-sourced units" `contribute` must independently propose classed 1 or 2. In the *earlier* commit of the same fold, `b17f22ed` rescoped that unit: `TOOL-dRetiredFork-4` §1 now reads "there is no fail-open of that shape to close" and "absorbs nothing until it has", §3 forbids editing `tools/hooks/agent-cap.js` at all, and its rev-2 line states "The README's 'nine fixes' count drops to eight". The README took the change at lines 16, 30 and 37. `DEPL-dRetiredFork-6` did not, at any of its four sites.

`contribute` derives candidates from BYTES — §4 Alternatives rejects every other basis — and under every one of TOOL-4's three S3 dispositions the inCMS `KIT_AGENT_CAP_DELTA` D1 row is class 4, stale, or already-absorbed, never a class-1 or class-2 contribution. So a CORRECT verb proposes five inCMS-sourced units and reds AC2, and reds §4's "must independently propose at least those nine, or it does not work" as well. **This is H2's exact shape — a criterion a correct implementation fails — reintroduced by the commit that fixed H2, in the file H2 was fixed in.** §4 calls that run "a genuine falsification test rather than a demonstration"; it currently sets the bar one above the population that exists.

The README is itself split and must move with it: lines 43-44 ("nine separable upstream fixes are nine units") and line 115 ("Order 1 is nine independent absorptions") still say nine beside the corrected eights.

**Fix.** Strike `TOOL-dRetiredFork-4` from AC2 and restate it as FIVE inCMS-sourced units — `-5`, `-6`, `-7`, `-8` and the C21 half of `-9`. Add a clause requiring the verb to report the D1 row as stale or already-absorbed (F2's ALREADY ABSORBED shape) rather than as a contribution. Change nine to eight in §1, §4 Rollout (both sites) and §5, and say once in §4 Rollout why the ninth order-1 unit is excluded, so the set reads as deliberate rather than as a miscount. Re-render the README's two surviving nines.

**Left-shift gate.** The cheapest form, and the one worth wiring: forbid a bare cardinal in a §4 Rollout or §5 testing row where a §2 or §6 list owns the population, per the charter's derive-over-author rule. A stronger arm for this exact class: extract every unit id enumerated inside a §6 acceptance criterion and red when the named spec's §1 carries a disclaiming phrase, so a spec cannot count a sibling that says it contributes nothing.

### 2 — the build's done-condition demands a stamp the engine withholds, and its sibling permits the blocker to survive

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §6 AC10 (lines 119-123), against `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-1.md` §2 S6 and §6 AC6 (line 109).

**The defect.** Two criteria written in the same fold round, from two different round-1 findings, that cannot both be satisfied. B1's fold produced AC10, which labels itself "THE BUILD'S DONE-CONDITION, and the only criterion in the set that observes it" and pins the exact argv `python tools/govkit/govkit.py update --target C:/projects/nicocares/main --write`, requiring the run to "re-stamp `gov_commit`". H3's fold produced DEPL-1 AC6, which accepts a non-zero `unattributed` row count so long as the ledger records why it cannot fall.

Verified at HEAD: `tools/govkit/govkit.py:6566-6573` withholds the `gov_commit` re-stamp whenever any receipt row carries `evidence: "unattributed"`, unless `--allow-ungraded` is passed; it names `govkit adopt --re-adopt --write` and `--allow-ungraded` as the two escapes. AC10's argv carries neither flag. DEPL-1 S6 states outright that nothing in the 25-unit set drives that population down — 32 rows at NicoCares, 30 at inCMS — and a grep of the whole spec set finds no unit scoping `--allow-ungraded` or `--re-adopt --write`.

So DEPL-1 AC6 can pass with 31 of 32 rows surviving, and those 31 rows block AC10. **The build can pass every unit and fail its README, for a reason recorded in a sibling spec.** This is round 1's blocker about the union of criteria not implying the README's acceptance, folded into two criteria that were never read against each other.

**Fix.** AC10 must name which escape it depends on, in its own text. Either require the `unattributed` count to reach zero at both adopters — which makes DEPL-1 AC6's "or state why it cannot" branch a build blocker rather than an accepted outcome, and needs a scope item somewhere that drives the population down — or state that AC10 is observed with `--allow-ungraded` and that the ledger records the surviving count. Carry the same sentence in DEPL-1 AC6 so the two agree in writing.

**Left-shift gate.** The narrow mechanical form: when an acceptance criterion pins an exact argv, resolve that argv's flags against the program's own refusal paths and red when a refusal reachable on the pinned argv is unmentioned in the criterion. Where that is too deep, the documented manual check belongs in BUILD-METHOD — a criterion labelled as a build's done-condition is read against every other spec's §2 before the spec set closes.

### 3 — `TOOL-dRetiredFork-12` declares one token in scope and two in its data model

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md` §4 Data model (line 52), §10 (line 125), §5 user-docs row, against §2 S1 (lines 24-30).

**The defect.** The H12 fold rewrote S1 to `placeholders = ["KIT_DIR"]` and proved the reason: `TOOL_ROOT` "cannot be rendered here", and an unresolved `{{TOOL_ROOT}}` brace "would otherwise ship to every adopter". It then left §4 Data model reading "Two tokens only, `KIT_DIR` and `TOOL_ROOT` … No new token alphabet", §10 asserting that the memory-tree rules "already declare the exact `["KIT_DIR", "TOOL_ROOT"]` placeholder pair this unit adopts", and §5's user-docs row saying "its two tokens". rev-2's own log names §10 as part of the H12 defect and then does not edit it.

Verified at HEAD: `tools/unattended/adopt-unattended.sh:222-228` substitutes `{{KIT_DIR}}`, `{{MEMORY_ROOT}}`, `{{LANDER}}`, the three `KEEPALIVE_*` tokens and `{{ANCHOR_SCOPE}}`, and never computes `TOOL_ROOT`. `grep -rn TOOL_ROOT tools/` finds it only in `tools/memory-tree/adopt-memory-tree.sh:36-37,85`, `tools/lib/render-doc.sh:35`, `tools/workflows/kit.toml:18` and the install-prefix gate's own fixtures. `tools/memory-tree/kit.toml` declares the pair at three rules — which is why §10's precedent claim reads plausible and is still false about *this* kit.

**§4 Data model is the section a builder implements from.** Following it declares both tokens in `tools/unattended/kit.toml` and ships the literal brace to every adopter — precisely the harm H12 was raised to prevent. §10's probe half additionally asserts a placeholder pair the unit no longer adopts, so the machine-graded reuse fact is false.

**Fix.** Rewrite §4 Data model to "One token, `KIT_DIR`", carrying S1's reason and stating that `TOOL_ROOT` is computed only by `tools/memory-tree/adopt-memory-tree.sh` and is not available in this kit's adopter. Rewrite §10's seam sentence to cite the memory-tree rendered-template family as a SHAPE precedent while this kit's adopter substitutes a narrower token set. Correct §5's "its two tokens".

**Left-shift gate.** A kit-descriptor check that already has the data: for every `[[files]]` rule declaring `placeholders`, assert each named token is actually substituted by that kit's own adopter script, and red on one that is not. That gate would have caught the rev-1 declaration at the source and made the whole unit's §4/§10 drift unbuildable rather than merely unreviewed.

### 4 — `TOOL-dRetiredFork-14` AC3 observes the unit's highest-risk arm with a command that cannot run

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §6 AC3 (line 103).

**The defect.** AC3 ends "Observed via `bash .claude/hooks/agent-cap.test.sh`". AC5, one line below at 106, names the tracked `bash tools/hooks/agent-cap.test.sh`. rev-2's log at lines 133-134 records the B4 fold as "corrected AC5's untracked `.claude/hooks/agent-cap.test.sh` to the tracked `tools/hooks/agent-cap.test.sh`" — **the instance was fixed and the sibling instance one line above was not.** That is the AGENTS.md §7 rule this build exists to enforce ("Gate the CLASS, not the instance"), broken inside the fold that enforces it.

Verified at HEAD: `git ls-files .claude/hooks/` returns only `agent-cap.js`, `recall-opened.js` and `scratch-guard.js`, and no `agent-cap.test.sh` exists there on disk either. Worse than a stale path: **S2 withdraws that entire destination**, so the witness sits inside the surface the unit removes and will exist less after the unit lands than it does now. AC3 is the only criterion observing S3's self-arming parity arm — the mitigation for the green-by-absence hole S3 exists to close — so the unit's highest-risk behaviour is graded by a command nobody can run, and the criterion can never be answered in the acceptance ledger.

**Fix.** Change AC3's observation to `bash tools/hooks/agent-cap.test.sh`, matching AC5. Then grep §2, §4, §5 and §6 of this spec for any remaining `.claude/hooks/` spelling used as an invocation target rather than as a legacy path being withdrawn, and record in rev-2's log that B4 touched AC3 as well as AC5 — the log currently overstates what the fold did.

**Left-shift gate.** A spec lint that extracts every backticked token matching a path shape from §6 and resolves it with `git ls-files`, redding on one the tree does not track, with a declared exception list for paths a unit is deliberately about to create. This is cheap, exact, and would have caught B4's original instance, this survivor, and finding 19's `scripts/` case in one pass.

### 5 — `TOOL-dRetiredFork-14` builds the repath where two of its three hooks cannot reach it

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §2 S1 and S1b (lines 24-36), against §4 Inventory.

**The defect.** S1 and the fold-added S1b build the repath capability inside `tools/settings-merge.py` — the `hook_path` default and the `HOOK_MARKER` dedup. That is correct *for agent-cap and nothing else.* Verified at HEAD, `tools/settings-merge.py:286` resolves `hook_path = a.hook_path or frag["hook_path"]`, so for the other two hooks the path comes from the committed fragment FILE, not from the built-in default S1 fixes:

- `tools/hooks/scratch-guard.fragment.json:6` — `"hook_path": ".claude/hooks/scratch-guard.js"`
- `tools/memory-recall/recall-opened.fragment.json:6` — `"hook_path": ".claude/hooks/recall-opened.js"`

No item in §2 touches either file. Independently, `tools/memory-recall/adopt-memory-recall.sh:179-181` copies `recall-opened.js` into `.claude/hooks/` under `--with-hook`, re-installing the exact copy S2 withdraws, regardless of what the descriptor says.

So two of the three rows in §4's Inventory stay wired to a path that no longer ships, and one adopter keeps re-creating it. **That is the silent unwiring §5 calls the highest risk in the build, produced by the unit written to prevent it** — S1b's engine work is real and cannot reach them, because their path never came from the default it fixes.

**Fix.** Add a scope item covering the two fragment files and `adopt-memory-recall.sh`'s `--with-hook` copy, and an acceptance criterion asserting that after the change no tracked fragment file and no adopter script names `.claude/hooks/` for a withdrawn source. Say explicitly in S1b whether the repath mode rewrites a path supplied by a fragment or only the built-in default, because the answer decides whether the fragment edits are sufficient.

**Left-shift gate.** A check over `tools/**/*.fragment.json` plus every adopter script asserting that every `hook_path`, and every hook destination an adopter writes, resolves to a destination some `kit.toml` rule declares. A fragment naming a path no descriptor ships is a wiring hole whatever unit created it, and this class recurs every time a destination moves.

---

## High

### 6 — the inCMS half of the done-condition is gated on an event with no owner

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-3.md` §6 AC10, second sentence (line 123).

**The defect.** AC10's second sentence reads "Repeated for `C:/projects/incms/main` once its receipt is repaired." Grepping the whole build folder returns that phrase exactly once, and no unit in the 25-spec roster performs the repair: DEPL-4 fixes an `apply` pathspec crash, DEPL-5 fixes `check`'s outcome grading, DEPL-2 reads inCMS read-only, and DEPL-7 §3 explicitly refuses to edit either adopter's tree. The README's done-condition is `govkit update --write` being the whole update at BOTH adopters, so half of the only criterion observing it can neither be discharged nor fail — an arm that is permanently neither green nor red, which is worse than a missing one because it looks covered.

**Fix.** Either name the unit that repairs inCMS's receipt and give AC10 a forward reference to it, or strike the inCMS sentence from AC10 and state in §3 that inCMS's half of the done-condition is deferred, so the README's claim and the criterion set agree in writing rather than by hope.

**Left-shift gate.** A spec lint that reds on a conditional clause in an acceptance criterion — "once", "after", "when X is repaired" — whose condition names no unit id and no gate command. A criterion whose precondition has no owner is unfalsifiable by construction.

### 7 — `TOOL-dRetiredFork-14` §10 asserts both verdicts and carries a truncated sentence

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §10 Reuse audit (lines 5-9).

**The defect.** The fold inserted its correction in FRONT of the text it refutes instead of replacing it. The paragraph now reads, in order: the corrected claim that `merge()` is "parameterised for the FIRST write and NOT for a repath — the dedup branch above it decides that, and S1b builds what is missing"; then the broken fragment "The seam is — `reuse_lookup.py` reports"; then rev-1's surviving conclusion, "already parameterised and already exercised by `--hook-path`. No new mechanism is built; a default is stopped from being a decision."

"S1b builds what is missing" and "No new mechanism is built" are opposite verdicts in one paragraph, and the dangling em dash shows the sentence was never finished. rev-2's log claims "§10 corrected: the seam is not already sufficient" — the log is wrong about its own edit. §10 is the machine-graded reuse half that BUILD-METHOD M7 regrounding reads to decide whether a design pass is owed, and it currently resolves to the refuted answer: a reader sizing the unit from §10 sizes it as the call-site change B3 measured as inverted.

**Fix.** Delete the dangling fragment and everything from "already parameterised and already exercised" onward, so the section states one claim: `merge(obj, hook_path, frag)` at `tools/settings-merge.py:91` is the extension point, its dedup at `:108-109` makes it insufficient for a repath, and S1b builds the missing mode.

**Left-shift gate.** A hygiene arm redding on a structurally broken sentence in a spec — a line ending in a bare ` — ` or an em dash immediately followed by a paragraph break — and a second arm redding when a §9 rev line claims a section was corrected while that section still contains a phrase the rev line quotes as the defect. The second is the general fold-integrity check this whole round argues for.

### 8 — S2 withdraws scratch-guard's wired copy and nothing in the unit predicts the leg that reds

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-14.md` §2 S2 and S3 (lines 38-45), §7 Gates.

**The defect.** S2 drops the `.claude/hooks/` destination "from the hooks and memory-recall descriptors", which in `tools/hooks/kit.toml:43-46` includes `scratch-guard.js`, not only `agent-cap.js`. S3 then arms "The two-copy parity arm" — singular — and §7 names `agent-cap self-test` and never `scratch-guard self-test`, which is a real declared leg (`bash tools/hooks/scratch-guard.test.sh`).

`tools/hooks/scratch-guard.test.sh:182-192` carries a byte-identical arm that hard-FAILs, not skips, when the kit copy is tracked and the wired copy is absent: "FAIL the wired copy .claude/hooks/scratch-guard.js is MISSING (parity must not be satisfiable by absence)". That is exactly the state AC1 requires after this unit lands. The descriptor states the reason inside the file the unit edits — `tools/hooks/kit.toml:9-10`, "the parity arm fails outright when the wired copy is absent, so a single-destination model reds it in every target". **The unit passes its own DoD while redding a bar leg it does not name.**

**Fix.** Restate S3 as "every two-copy parity arm" and enumerate them by path — `tools/hooks/agent-cap.test.sh:810-817` and `tools/hooks/scratch-guard.test.sh:183-190`. Add `scratch-guard self-test` to §7. Add an AC3b observing the scratch-guard arm self-arming against a population of one and REFUSING at zero, the same shape AC3 gives agent-cap.

**Left-shift gate.** A spec lint that reads every source path a unit's §2 declares it edits, resolves which `tools/gate-legs.json` legs exercise those paths, and reds when §7 omits one. The manifest already carries the mapping; nothing currently joins it to a spec.

### 9 — `DEPL-dRetiredFork-7` S6 is mandated, forbidden and unobserved at once

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-DEPL-dRetiredFork-7.md` §2 S6 (line 47), §3 (line 58), §6 AC7 (line 116).

**The defect.** S6 is imperative: "Reclassify inCMS's `gen_build_index.py` row from `diverged` to a contract-adopted class." That row lives in inCMS's own `kits.json`. §3 makes "Editing either adopter's tree" a non-goal — "gov owns none of it; the deliverable is the measurement and the contract, handed over" — and AC7 asserts that neither register is edited by this unit. Walking AC1 through AC7: AC1-AC4 cover the census, AC5 the ledger contract, AC6 the S5 backlog rows, AC7 the S4 contradiction. **None observes S6.**

The build README line 77 parks the reclassification here — "Reclassifying that registry row is `DEPL-dRetiredFork-7`" — so this is the only home the work has. The unit can pass its DoD with the row untouched while the README believes it was reclassified, and every metric computed over that registry keeps carrying the 2764-line inflation S6 exists to remove. §10 line 132 compounds it by citing S6 as the convergence example.

**Fix.** Decide which side owns the edit, in writing. Either restate S6 as "the census RECORDS the row as contract-adopted and the reclassification is handed to inCMS as a named recommendation", and add a criterion observing it — the census output names the row, its class and the two symbol counts — which carves the item cleanly out of §3's non-goal; or move the row edit to a follow-up unit and say so in §3, so the README stops delegating it here.

**Left-shift gate.** A spec lint asserting that every `S<n>` label in §2 is referenced by at least one criterion in §6 — by label, not by prose similarity. It is a one-pass grep over a spec's own headings and would have caught this, finding 10 and finding 22 together.

### 10 — half of `TOOL-dRetiredFork-17`'s title is unobservable, and its own fork recommends against S2

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-17.md` §2 S1 and S2, §6 AC1-AC8, §8 F1.

**The defect.** S1 is the authoring rule, written once — four clauses about literals, derivation, tokens and replicated policy values. S2 is where it lands: `tools/hooks/README.md` and `AGENTS.md`, not the size-gated charter template. Neither has an acceptance criterion. AC1 through AC8 observe only the ban's RED, the exception list and its stale-row arm, the empty-population refusal, the two inherited defects (`TOOL-aScouredKit-20`, `TOOL-dTieredTribunal-27`), the pre-wiring near-miss listing, and the testsuite-count leg. The ban can land green with the authoring rule never written, which leaves a gate enforcing a rule no document states.

This is not a template quirk — sibling specs in the same roster do gate doc landings, DEPL-7 AC5 for `WIRE-INTO-PROJECT.md` and TOOL-16 AC4 for the same file. And §8 F1 is UNRESOLVED while recommending the opposite of S2: "the kit README owns the rule; `AGENTS.md` carries a pointer, not a copy". §2 and §8 name different carrier sets and no criterion can settle which one binds.

**Fix.** Add a criterion naming both carriers and their content — the four clauses of S1 in `tools/hooks/README.md`, the pointer F1 resolves to in `AGENTS.md`, and `bash tools/check-template-size.sh` still exiting `0` with the template untouched. Resolve F1 in place and reconcile S2's plain text to whichever answer wins, so §2 and §8 stop disagreeing.

**Left-shift gate.** The same §2-to-§6 coverage lint as finding 9, plus a second arm: red when §8 carries an UNRESOLVED fork whose recommendation contradicts a §2 scope item, detectable in the narrow case where both name the same file path with opposite verbs.

### 11 — the refuted "four guarded arms" survives in the title, the goal and the README

**Address.** `memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-5.md` H1 title (line 1), §1 (line 16), §3 non-goal (line 42); `memory/builds/dRetiredFork/README.md` lines 93 and 138.

**The defect.** The H10 fold restated S1, S2 and AC2 against the measured truth and left the claim they refute standing in the three places a reader meets first. S1 says outright, at line 24, "There are TWO guarded arms, not four", and rev-2's log names rev-1's error precisely: "rev-1's 'four guarded arms' counted guard exits". Verified at HEAD: `tools/codebase-map/selftest.py` holds 26 `test_` definitions with exactly two guarded arms — `test_identifier_tokens_corpus_recall` at `:1165` and `test_js_probe_against_the_lexicon` at `:1226` — and four guard EXITS at `:1186`, `:1194`, `:1218` and `:1246`.

The title still reads "four codebase-map selftest arms stop being stamped ok" and §1 still opens "Four guarded arms in `tools/codebase-map/selftest.py`", two paragraphs above S1 contradicting it. It propagates: the build README's roster row at line 93 and its GENERATED unit table at line 138 both render the title, so **the build's own overview states a number its spec refutes.** §3's "Making the four guards satisfiable" leaves it ambiguous whether four means arms or exits.

**Fix.** Retitle to "two codebase-map selftest arms stop being stamped ok", rewrite §1 as two guarded arms printing an honest "NOT a pass" line at four guard exits, disambiguate §3 to "the four guard EXITS", and re-render the build index so the roster row and the generated table follow.

**Left-shift gate.** A hygiene arm asserting that a spec's H1 and its §1 first sentence contain no cardinal that a §2 scope item explicitly negates — the "there are TWO, not four" shape is greppable. More generally, this is the derive-over-author rule applied to spec prose: a count a scope item measures should be stated once, in the scope item.

---

## Medium

### 12 — `DEPL-dRetiredFork-3`'s `generated` non-goal contradicts its own central mechanism

**Address.** §3 non-goal (lines 52-53) against §2 S2, §6 AC2 and AC10.

§3 says of `generated` rows: "The report NAMES which generators are owed; running the target's own tooling is the adopter's." S2 requires `gen_map.py --write` and `gen_build_index.py --write` to be "performed rather than described in a runbook"; AC2 requires the run to perform the declared argv; AC10 requires it to run "every declared generator"; and §5 makes the runbook's shrinkage an acceptance criterion *because* the obligations become declarations. Named-versus-run is one question and the document answers it both ways, naming the same two programs on each side. A builder can satisfy §3 by printing a list and satisfy nothing else — and the build's done-condition rests on the other reading.

**Fix.** Rewrite the §3 bullet to disclaim only what `update` will not do — write a `generated` file's bytes itself — and state plainly that a `[[regenerate]]` argv declared by a gov descriptor IS run by the verb. If some generators genuinely stay the operator's, name the discriminator rather than the role.

**Left-shift gate.** A spec lint that reds when a §3 non-goal bullet and a §2 scope item name the same backticked identifier — a cheap proxy for exactly this contradiction, firing on findings 9, 12 and 20 alike.

### 13 — `DEPL-dRetiredFork-2`'s anti-vacuity line and its byte-identity criterion cannot both hold

**Address.** §5 error/empty/loading row (line 86) against §6 AC4 (line 106) and §2 S6.

§5 requires "a target with no missing sources must print `0 new`, not nothing". AC4 requires that same run's output to be "byte-identical to the pre-change run", and S6 repeats it. The pre-change run has no concept of a new source, so it cannot emit `0 new`. No criterion observes the `0 new` line at all, so whichever a builder picks the other is silently violated. `TOOL-dRetiredFork-3` rev-2 records folding M1 as exactly this shape — "AC5 demanded byte-identity while §5 requires an unconditional `0 tolerated` line, and the two cannot both hold" — so the fold caught the class there and missed the instance here.

**Fix.** Restate AC4 as "differs from the pre-change run by EXACTLY the `0 new` line §5 requires, and by nothing else", which is the wording TOOL-3 AC5 already uses after its M1 fold, and extend a criterion to observe the `0 new` emission on a target with no missing sources.

**Left-shift gate.** A spec lint pairing every "byte-identical to the pre-change run" criterion with the §5 error/empty row and redding when that row mandates unconditional output. Two greps and a join.

### 14 — three counts for one arm list, in two specs

**Address.** `2026-09-02-spec-DEPL-dRetiredFork-3.md` §5 testing row (line 94) against §2 S6 (lines 41-43) and §9 rev-2 (line 153); `2026-09-02-spec-DEPL-dRetiredFork-2.md` §5 testing row (line 94) against §2 S6 (lines 52-54).

DEPL-3's S6 enumerates five arms — a rendered row re-rendered, a version bump triggering its declared generator, a role change surviving a round trip, a failed render rolling back, and a target whose wired command still names the copy S5 would withdraw. §5's testing row says "S6's four arms plus the acceptance matrix". rev-2's log calls the arm the fold added "a sixth arm". Three figures, one five-item list. The uncounted arm is the S5/B6 one, which observes the constraint `TOOL-dRetiredFork-14` §5 calls the build's highest risk and which B6 found observed nowhere — so the lowest count is the one that would drop precisely the arm the fold was written to add.

DEPL-2 carries the same defect from the B2 fold: S6 enumerates five arms after the SEED arm was added, §5's risks row was updated, and §5's testing row was left at "S6's four arms in `tools/govkit/selftest.py`". The uncounted arm there is the seed arm, mitigating the severe overwrite risk §5 itself says rev-1 missed. AC6 independently mandates the seed observation, so the harm is bounded — the confirmed defect is the stale count, not a guaranteed missing arm.

**Fix.** Replace both counts with a pointer — "one arm per S6 item" — and correct DEPL-3's rev-2 line to "a fifth arm".

**Left-shift gate.** Red on any cardinal in a §5 testing row. §5 rows describe populations §2 owns, the charter already bans a count in prose beside the source that owns it, and this is the smallest place to enforce it — it fires on findings 1, 14, 15 and 18.

### 15 — `TOOL-dRetiredFork-13`'s file count and occurrence count cannot both be right

**Address.** §1 (line 6) and §2 S1 (line 12).

The population is stated as "the other 32 shipped test and selftest files, which carry 259 of the ratchet's 656 recorded occurrences". Measured directly on `tools/install-prefix-carried.txt`: the test and selftest rows number **33** and sum to exactly **259**. Dropping `.githooks/pre-push.test.sh` (2 occurrences) gives 32 files carrying 257; no reading yields 32 carrying 259. S1 iterates the file count, so a builder enumerating 32 leaves one suite unswept — and AC4 asks only for "a carried total strictly below 656", which any partial sweep satisfies, so the miss stays invisible until `TOOL-dRetiredFork-17`'s ban reds at order 9.

**Fix.** Re-derive the pair from the ratchet file and write the reconciled numbers, stating explicitly whether `.githooks/pre-push.test.sh` belongs to this unit's population or `TOOL-dRetiredFork-11`'s. Better, make AC4 name the per-file rows expected to reach zero rather than a total, so a partial sweep cannot pass.

**Left-shift gate.** A ratchet-derived assertion in AC4's place: the criterion names the expected post-sweep rows and the checker compares against the file. A total is satisfiable by any subset, which is the could-not-fail shape §7 already names.

### 16 — the non-test checker class is disclaimed on the strength of its one owned member

**Address.** `2026-09-02-spec-TOOL-dRetiredFork-13.md` §3 third bullet (lines 42-45) against `2026-09-02-spec-TOOL-dRetiredFork-8.md` §2 S6.

H4's finding was "a class of literal sites with no owning unit". The fold made TOOL-13 §3 disclaim the whole class — "Non-test shipped CHECKERS. `tools/check-wiring.sh` is the measured case and it is NOT this unit's" — and both revision logs record the gap as closed, "the pointer is corrected on both sides". Measured at HEAD against `tools/install-prefix-carried.txt`, the loose non-test checkers under `tools/` are **seven files carrying 47 occurrences**: `check-kit-versions.sh` 30, `check-install-prefix.sh` 6, `check-wiring.sh` 6, `check-agent-cap-restatement.sh` 2, `check-line-length.sh` 1, `check-microformats.sh` 1, `settings-merge.py` 1. TOOL-8 S6 claims one of them. The fold narrowed the orphan set from 47 to 41 and recorded it as closed.

`TOOL-dRetiredFork-17` §4 then sizes the ban's population as "whatever survives units 10 through 13" — a phrase naming neither TOOL-8 nor those six files — so 41 occurrences arrive at the order-9 ban undrained and undeclared, and F2's owner turn is priced against a number nobody has.

**Fix.** Either narrow TOOL-13 §3's bullet to name only `tools/check-wiring.sh` as the excluded case, leaving the rest visibly unowned, or state in TOOL-17 §4 Migration that the loose non-test checkers — 47 occurrences across seven files, minus TOOL-8's six — are the exception list's seed population.

**Left-shift gate.** The ban itself, run in report mode before it is armed: `tools/check-install-prefix.sh` printing the surviving population grouped by owning unit, with rows no unit claims listed as UNOWNED. §7's rule about running a candidate predicate over the real tree before wiring it applies exactly here.

### 17 — `TOOL-dRetiredFork-3` corrected the probe query and left the terms M7 re-runs

**Address.** §10 recall-terms line (line 11).

The M8 fold replaced §10's probe sentence with this unit's own question and left rev-1's terms line untouched: `carve-out`, `install-prefix`, `KIT_REL`, `carried`, `relocate`, `rung`, `adopter`, `divergence`, `repath`, `govkit`, `receipt`, `unattributed`, `derive`, `prefix` — byte-identical to `DEPL-dRetiredFork-1`'s and `TOOL-dRetiredFork-10`'s, the two install-prefix units. Every other spec in the build carries bespoke terms, so this is not a shared house list. Not one of the fourteen reaches `StaleHeader`, `gen_build_index`, header, waiver or registry, which are this unit's entire subject. The fold also deleted the only measured result rev-1 had, so the section now asserts a probe with the wrong terms and no result at all — weaker than rev-1, which at least reported a number.

`memory/guides/BUILD-METHOD.md:151` says the terms are recorded "because composing them is the expensive half and M7 re-runs the query", so the fold fixed the half that is read and left the half that is EXECUTED. A resumed session regrounds this unit against the install-prefix corpus and gets records that cannot bind the change.

**Fix.** Re-run the probe with this unit's terms — `StaleHeader`, `header`, `parse failure`, `waiver`, `registry`, `shrink-only`, `gen_build_index`, `collect`, `build README`, `tolerated`, `memory/project`, `check 3` — replace the terms line, and restore a measured result line.

**Left-shift gate.** A hygiene arm redding when two specs in one build carry byte-identical `Recall terms used` lines. Exact, cheap, zero false positives on this corpus, and it catches the copy-paste directly.

### 18 — five registries versus nine, inside one spec

**Address.** `2026-09-02-spec-TOOL-dRetiredFork-3.md` §4 Data model against §2 S6.

§4 says the new registry matches "the shape of the five registries already under `memory/project/`" while S6 — the H7 fold — says check 3's whitelist names nine. Measured at HEAD: `git ls-files memory/project/` returns nine tracked files, and check 3's whitelist `case` at `tools/memory-tree/check-memory-hygiene.sh:320-329` has nine `F:` arms — `legacy-files`, `curation-debt`, `id-orphan-waiver`, `corpus-path-unresolved`, `unarmed-branches`, `method-carriers`, `testsuite-count-waivers`, `trace-waiver`, `readme-contract`. No reading of the registries yields five, by row shape or by non-empty rows. §4 is the section a builder reads to size the change, and the smaller number also weakens S6's argument, which rests on the whitelist being an exhaustive hardcoded list.

**Fix.** Change §4's "five registries" to nine, or drop the count and name `legacy-files.txt` and `readme-contract.txt` as the shape precedents, which is what §10 already does.

**Left-shift gate.** The §5-row cardinal ban of finding 14, extended to §4 Data model — the two sections where a builder sizes work are the two where a stale count costs the most.

### 19 — `TOOL-dRetiredFork-16` AC3 names a path gov does not track and its own non-goal forbids

**Address.** §6 AC3 (lines 92-93) against §3 (line 45); §2 S2 (line 30) against §6 AC4.

AC3 requires `bash scripts/check-build-readme-comments.sh` to exist, source `.memory-tree.conf` and red on a fixture. `git ls-files scripts/` returns zero paths in gov. Unlike every other adopter-facing criterion in this build — DEPL-1 AC4, DEPL-2 AC5, DEPL-3 AC7 all spell `C:/projects/nicocares/main` — AC3 names no target, so it cannot be read as an adopter-tree observation either. Making it true in gov collides with §3's "Absorbing check 90 into gov" non-goal. Separately, S2 requires the worked pattern in BOTH `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md`, and §5's user-docs row names both, while AC4 observes only the latter — leaving the kit README, the carrier an adopter actually reads, unobserved in a unit whose §5 says it "is largely user docs".

**Fix.** Restate AC3 against the adopter's own tree — "NicoCares' `scripts/check-build-readme-comments.sh` is quoted verbatim in this build's record with its fixture and its red output" — or land the example under gov's own `tools/` and reconcile §3. Extend AC4 to name `tools/memory-tree/README.md` alongside `WIRE-INTO-PROJECT.md`.

**Left-shift gate.** The §6 path-trackedness lint of finding 4, whose exception list must require a target prefix on any path outside gov's tree. A criterion naming a foreign path without naming the tree it lives in is unobservable by construction.

### 20 — `TOOL-dRetiredFork-15` believes it added no disarming key, so neither is guarded

**Address.** §3 third non-goal (lines 47-48) against §2 S1 and S3, §6 AC3 and AC5.

§3 refuses "Any key that can drive a violation count to zero … a threshold key is a different animal and none is added here". S3 adds `RECORD_SERVES_CUTOFF` as a date filter over check 21 branch A — the spec's own F2 calls it a cutoff "matching the five cutoffs already in `.memory-tree.conf`", which is a threshold — and S1 adds `BUILD_SLUG_RE`, whose over-permissive value §5 itself flags as "silently admits everything" when mis-anchored. The acceptance set matches the false belief: AC3 catches only an unanchored or empty regex, so an anchored `^.*$` passes, and AC5 imposes no bound on a cutoff set past today's date. An adopter can zero check 21 and check 4 from `.memory-tree.conf` and the bar stays green.

**Fix.** Either narrow the non-goal to "no key that sets a THRESHOLD on a violation count" and state why a population date filter is admissible, or add the guards and their criteria: reject a `RECORD_SERVES_CUTOFF` in the future, and reject a `BUILD_SLUG_RE` that matches the empty string.

**Left-shift gate.** In the checker itself: every conf key that can shrink a population declares a bound, and the validation loop reds on a value outside it. The gate then cannot be disarmed by the file it reads — §7's rule that a guard sharing state with the thing it guards is not a guard.

### 21 — the only pointer to `TOOL-dRetiredFork-4`'s evidence cites a family that does not exist

**Address.** §2 S1 (line 31) against §9 rev-1 (line 79).

S1 — fold-added text, and the rescoped unit's sole input — tells the builder to obtain inCMS's D1 reproduction "from `ARCH-aFerriedToolkit-3`". A grep across the whole memory tree returns that string exactly once, here. This spec's own rev-1 log line spells it `ABL-aFerriedToolkit-3`, the round-1 review record spells it `ABL-aFerriedToolkit-3`, and `TOOL-dRetiredFork-5` §1 cites the sibling row as `ABL-aFerriedToolkit-4`. A builder greps `ARCH-aFerriedToolkit-3`, finds nothing, and the unit whose entire purpose is "reproduce before absorbing" has no reachable input — which is how rev-1's premise inverted in the first place.

**Fix.** Settle the prefix against inCMS's own register and spell it identically in S1 and in rev-1's log. If the record is `ABL-aFerriedToolkit-3`, correct S1. Consider naming the register row by path as well as by id, since the id is foreign and gov cannot resolve it.

**Left-shift gate.** A hygiene arm asserting that every `<FAMILY>-<slug>-<seq>` cited anywhere in one build folder resolves to a single FAMILY per slug. Two spellings of one slug is always a defect and needs no knowledge of the foreign register to detect.

### 22 — `DEPL-dRetiredFork-1` states a grading obligation nothing builds and nothing observes

**Address.** §5 security row (lines 80-82) against §2 and §6.

§5's security row requires the design to "grade the derived fragments and refuse a degenerate one, such as an empty string". No scope item builds it: S3 is a liveness assertion on an EMPTY needle MAP, which is a different population from a degenerate needle inside a non-empty one, and AC3 observes only the empty-map refusal. §4's per-row needle derivation works only if every derived fragment matches exactly the path it names; a degenerate fragment makes the whole-file-equality proof match too much and takes the row onto the automatic raw-write path — which §5's own risks row calls the highest-severity risk in the build, gov's bytes written over a target's real edit. TEMPLATE-SPEC defines §5 rows as "what's needed", so this is a stated obligation with no scope item and no criterion, on the most dangerous path in the set.

**Fix.** Add an S3b requiring every derived needle to be graded and a degenerate one refused, and a criterion observing the refusal on a fixture whose row yields an empty or single-character fragment.

**Left-shift gate.** Extend the §2-to-§6 coverage lint of finding 9 to §5: every §5 row stating an obligation in imperative voice must name a scope item or a criterion. That is the "production-readiness rows against their own §6" check round 1 skipped, mechanised.

### 23 — `DEPL-dRetiredFork-3` AC11 lost its gate and gained no replacement

**Address.** §6 AC11 (lines 124-126) against §7.

The fold removed `runbook parity` from §7 — correctly, since `tools/gate-legs.json` carries no such leg — and added nothing in its place. AC11 requires `WIRE-INTO-PROJECT.md`'s maintenance section to be strictly SHORTER than at `b0108f13` with every dropped obligation carried by a `[[regenerate]]` block, and now has no check of any kind that the runbook still agrees with the descriptors. `tools/govkit/check_runbook_parity.py` exists, asserts exactly that in both directions, and a repo-wide grep finds **zero callers** — no leg, no script. `TOOL-dRetiredFork-16` AC4 sets the counter-precedent inside this same set, invoking the program directly and calling it "the only thing exercising the runbook claim anywhere in the build". So the unit that materially rewrites the runbook is the one unit with no runbook check, and DEPL-6 and DEPL-7 edit that file with the same gap.

**Fix.** Extend AC11 with a direct invocation — `python tools/govkit/check_runbook_parity.py` exits `0` after the shrink — mirroring TOOL-16 AC4's wording, and do the same in DEPL-6 §5 and DEPL-7 AC5.

**Left-shift gate.** Add `runbook parity` to `tools/gate-legs.json` as a real leg. A checker with zero callers is a check nobody runs, and this build is about to depend on it from three units.

### 24 — `TOOL-dRetiredFork-12` names a leg it does not touch and omits the one that grades it

**Address.** §7 Gates.

The fold's leg-name normalisation mapped rev-1's `unattended playbooks` onto `unattended kit gate`, which in `tools/gate-legs.json` runs `bash tools/unattended/check-unattended.sh`. The checker this unit exists to make pass at a foreign prefix — and which AC2 runs literally — is `tools/unattended/check-playbook.sh`, whose leg is `playbook validity gate`, and it appears nowhere in the spec. `check-unattended.sh` only reads `check-playbook.sh`'s source for parser parity; it never runs it, so the substituted leg grades nothing about `playbook.fixture.md`. Under §16 the green line must enumerate every expected leg, so this unit's DoD would report a gate that says nothing about its subject. Impact is bounded because AC2 names the command explicitly.

**Fix.** Replace `unattended kit gate` with `playbook validity gate` in §7, and keep `unattended kit gate` only if a scope item actually touches `check-unattended.sh`.

**Left-shift gate.** A spec lint resolving every backticked name in a §7 Gates line against `tools/gate-legs.json`, redding on an unknown name AND on a duplicate. This one lint closes findings 24, 25, 26 and 27 at once and would have refused the entire rename pass.

### 25 — the rename collapsed distinct legs onto one name in three specs

**Address.** `2026-09-02-spec-TOOL-dRetiredFork-9.md` §7, `2026-09-02-spec-TOOL-dRetiredFork-8.md` §7, `2026-09-02-spec-TOOL-dRetiredFork-14.md` §7.

TOOL-9 §7 reads `unattended kit gate` · `unattended kit gate` · `unattended skill wiring` · `kit version markers`; `git log -p` on `b17f22ed` shows the rename replaced the distinct pair `unattended run-state records` · `unattended playbooks` with the same name twice, silently dropping `playbook validity gate` from a unit that edits the unattended kit. A four-item list naming three legs, one of them owed and now unnamed. TOOL-8 §7 and TOOL-14 §7 each name `check-wiring self-test` twice, where rev-1 carried the distinct pair `wiring` · `wiring self-test`; `tools/gate-legs.json` holds exactly one check-wiring leg, so the duplicate names no second leg and additionally conceals that `tools/check-wiring.sh` is never executed by the bar in its own right. TOOL-9 changed its §7 content with no rev bump and no §9 entry, so the edit is invisible in the revision log.

**Fix.** De-duplicate all three against the manifest. TOOL-9 becomes `unattended kit gate` · `playbook validity gate` · `unattended skill wiring` · `kit version markers`, or drops the second entry with one line saying why the playbook gate is not owed. TOOL-8 and TOOL-14 reduce to a single `check-wiring self-test`, and TOOL-8 gains one line naming the compensating direct invocation for `tools/check-wiring.sh` itself. Add a rev-2 line to TOOL-9 recording that its gate list was re-spelled.

**Left-shift gate.** The §7-against-manifest lint of finding 24, with the duplicate arm.

### 26 — `TOOL-dRetiredFork-14`'s central code change has no leg named against it

**Address.** §7 Gates, §5 testing row (lines 14-15).

`tools/gate-legs.json` carries `settings-merge selftest` (`python3 tools/settings-merge.py --selftest`), and §7 omits it although S1 and S1b build a new repath capability inside exactly that file — while one slot in the list is spent on the duplicate of finding 25. Separately, §5's testing row claims "a fixture that verifies the two-step ordering", which §4 Migration and the fold both hand to `DEPL-dRetiredFork-3` AC9, and which this unit's §6 observes nowhere. A reader sizing the work from §5 and gating it from §7 gets both the wrong scope and the wrong bar.

**Fix.** De-duplicate §7 to `agent-cap self-test` · `check-wiring self-test` · `settings-merge selftest` · `scratch-guard self-test` · `kit version markers` · `govkit selfcheck` · `agent-cap restatement`, and restate §5's testing row as "the agent-cap suite, the wiring suite, and the settings-merge selftest; the two-step ordering fixture is `DEPL-dRetiredFork-3` AC9".

**Left-shift gate.** The path-to-leg join of finding 8: a unit editing `tools/settings-merge.py` must name the leg that runs it.

### 27 — `TOOL-dRetiredFork-11` gates a file it does not touch

**Address.** §7 Gates.

§7 names `push-main self-test`, `install-prefix (shipped surface)`, `check-wiring self-test` and `testsuite counts`. The unit changes `.githooks/pre-push`, and AC1 through AC4 all run `bash .githooks/pre-push.test.sh` — the leg `pre-push self-test`, which §7 does not name. So the unit names a leg exercising a file it does not touch and omits the one leg that would catch a regression in its forcing predicates. The original finding's provenance clause was wrong — TOOL-11 is at rev-1 with no fold recorded, so this defect predates the fold rather than being caused by it — but the gate-list error is real either way.

**Fix.** Replace `check-wiring self-test` with `pre-push self-test` in §7, matching the argv the criteria already invoke.

**Left-shift gate.** The §7-against-manifest lint plus the path-to-leg join. Together they make a §7 line derivable rather than typed.

---

## Low

### 28 — `DEPL-dRetiredFork-3`'s acceptance labels are out of sequence

**Address.** §6 (lines 102-127).

The renumber inserted AC9, AC10 and AC11 ahead of a criterion it left in place, so the section reads AC1 · AC2 · AC3 · AC4 · AC5 · AC6 · AC7 · **AC9 · AC10 · AC11 · AC8**. No label is duplicated and none is skipped — this is an ordering defect, not a numbering one — but AC8 (`selftest.py` and `selfcheck` exit `0`) now sits after the build's done-condition and after the runbook criterion, where a reader scanning for it stops looking. Every other spec in the set is in sequence, and the cross-spec reference hunt found no criterion cited by the wrong number from a sibling, so this is the renumber's only collateral of its kind.

**Fix.** Move AC8 back to its position after AC7, or renumber the tail so the sequence ascends.

**Left-shift gate.** A hygiene arm asserting that §6's `AC<n>` labels form a contiguous ascending sequence, with a `b` suffix permitted only immediately after its base label. That is the exact convention this corpus already uses (AC1b, AC2b, AC6b) and it is trivially checkable.

### 29 — a cut-line section that declares itself empty and then lists an item

**Address.** `2026-09-02-spec-TOOL-dRetiredFork-8.md` §3 Non-goals, first bullet (lines 42-47).

The fold rewrote the first bullet to open "- Nothing." and then explain the H4 reassignment, while a second bullet below states a genuine non-goal — `.claude/settings.json` as a written default, which is the actual defect the unit exists to fix. §3 is the explicit cut-line an eager builder reads; declaring it empty and then listing an item is self-contradicting, and the surviving non-goal is the one a reader who stopped at "Nothing" never reaches.

**Fix.** Delete the word "Nothing." and open the bullet with its content — "inCMS's residual literal prefix sites are NOT deferred: S6 takes them here".

**Left-shift gate.** A hygiene arm redding when a §3 bullet is exactly "Nothing." (or "None.") and §3 carries more than one bullet. The empty-section spelling is a real and useful convention; it just cannot coexist with content.

### 30 — four fold-authored details, each small and each wrong

**Address.** `2026-09-02-spec-TOOL-dRetiredFork-14.md` §2 S1 and S1b; `2026-09-02-spec-TOOL-dRetiredFork-12.md` §2 S1; `2026-09-02-spec-DEPL-dRetiredFork-2.md` status header.

**A citation four lines short.** TOOL-14 S1 places `HOOK_MARKER` at `tools/settings-merge.py:53`; at HEAD `:49` is `HOOK_MARKER = "agent-cap.js"` and `:53` is `AGENT_CAP = {`. Its three neighbours in the same fold-added sentence all verify — the docstring at `:37`, `def merge(obj, hook_path, frag=AGENT_CAP)` at `:91`, and the marker test plus `return obj  # already wired` at `:108-109`. So the one citation the fold introduced to carry B3's measurement is the stale one, and it is the line a reader goes to in order to check the corrected premise. This is the same class the same fold corrected in `TOOL-dRetiredFork-16` as L1, "the citation was four lines short". Change `:53` to `:49`.

**A fork outside the section that holds forks.** TOOL-14 S1b offers an unresolved either/or — a `--rewrite-stale-path` mode, or a fragment-level `hook_path` compare distinct from the marker compare — and §8 carries only F1 and F2, neither touching it. A CLI-surface choice sits outside the section that exists to force decisions, so nothing makes it before the first code pass. Promote it to a §8 fork with a recommendation.

**A false premise carrying a true conclusion.** TOOL-12 S1 says `adopt-unattended.sh` "substitutes only `{{KIT_DIR}}` (`:222`)". At HEAD it substitutes seven tokens — `{{KIT_DIR}}` at `:222`, `{{MEMORY_ROOT}}` at `:223`, `{{LANDER}}` at `:224`, then the three `KEEPALIVE_*` and `{{ANCHOR_SCOPE}}`. The conclusion (it never computes `TOOL_ROOT`) is correct and grep confirms it; the premise is a false claim about existing code sitting in the sentence carrying H12's whole measurement, and it forecloses a memory-path token the render channel actually offers. Change to "substitutes `{{KIT_DIR}}`, `{{MEMORY_ROOT}}` and `{{LANDER}}` (`:222-224`) and never computes `TOOL_ROOT`".

**A missing ratified pointer.** DEPL-2's rev-3 fold marked F2 `RESOLVED (agent, 2026-09-02, delegated)` without adding the `ratified <date>` pointer TEMPLATE-SPEC line 123 requires alongside the mark. The header tail still reads `· streams deployer · order 6`. The hygiene gate reads only §8's first non-blank line, so nothing catches it. Append `· ratified 2026-09-02`.

**Left-shift gate.** Two arms. First, a citation resolver: for every `<path>:<n>` in a spec, assert the path is tracked and that where the sentence names a symbol in backticks, that symbol appears at the cited line — this fires on both stale citations above and is the only mechanical defence against a fold inventing evidence. Second, a hygiene arm redding when §8 carries a fork marked RESOLVED and the status header tail carries no `ratified <date>`, a rule TEMPLATE-SPEC already states and nothing enforces.

---

## The four systematic checks round 1 skipped

Reported in full, green rows included, so a clean result is never mistaken for an unrun one.

- **§5 production-readiness rows against their own §6 — DIRTY.** One row states an obligation that no scope item builds and no criterion observes: `DEPL-dRetiredFork-1`'s security row, finding 22. The remaining rows across the eleven Tier-2 specs either name an S-item explicitly or describe a property a criterion covers. The testing rows are separately dirty for stale counts, findings 14 and 18.
- **§10 probe result before the terms marker — CLEAN.** All fourteen specs carrying a §10 place the `reuse_lookup.py` result ahead of the `Recall terms used:` line. `TOOL-dRetiredFork-14` is the one degenerate case, and its problem is the truncated sentence of finding 7, not the ordering.
- **Cross-spec id citations against the roster — CLEAN.** Every `TOOL-dRetiredFork-<n>` and `DEPL-dRetiredFork-<n>` cited anywhere in the spec set resolves to a spec that exists, and every one of the 25 roster ids is cited at least once. The one broken id in the build is foreign — `ARCH-aFerriedToolkit-3`, finding 21 — which this check by construction does not reach.
- **§3 non-goals against the README — CLEAN as stated, but two non-goals are contradicted by their OWN spec.** No §3 bullet contradicts the README. Three contradict §2 of the document they sit in: `DEPL-dRetiredFork-7` (finding 9), `TOOL-dRetiredFork-15` (finding 20) and `DEPL-dRetiredFork-3`'s generated-rows bullet (finding 12). The check was aimed at the wrong document; the intra-spec form is the one that pays, and it is the §3-versus-§2 identifier lint recommended under finding 12.

Two structural checks were run without being asked for, both **CLEAN**, and both worth keeping as gates. Every spec's status-header rev matches the last rev line in its §9 — all 25, no exceptions, which is the one thing this fold did uniformly well. And every Tier-1 spec carries exactly sections 1, 2, 3, 6, 7 and 9 while every Tier-2 spec carries 1 through 10, so the light profile is applied correctly throughout and `TOOL-dRetiredFork-4`'s demotion from Tier-2 to Tier-1 shed its §4, §5, §8 and §10 cleanly.

## What to do with this

Five blockers, six highs. The blockers are not independent: 1 and 2 are both the same non-reconciliation between `b17f22ed` and `3c7cd2b4`, and 3, 4 and 5 are all `TOOL-dRetiredFork-14` and `TOOL-dRetiredFork-12` folds that corrected one site of a multi-site claim. Fixing them is a half-day of text, not a redesign — **but the third round must re-read the round-3 fold, because that failure mode is now twice measured.**

The single highest-value left-shift is the one recurring under seven findings: **a spec lint that resolves a spec's own machine-facing tokens.** Gate names against `tools/gate-legs.json`, backticked paths against `git ls-files`, `path:line` citations against the file. Round 1 found defects of this class, the fold introduced more of them, and every one is a two-line grep away from impossible. The second is the §2-to-§6 coverage assertion, which fires on findings 9, 10 and 22 and is a single pass over a spec's own headings. Neither needs an agent, and both are cheaper than the round that found their absence.
