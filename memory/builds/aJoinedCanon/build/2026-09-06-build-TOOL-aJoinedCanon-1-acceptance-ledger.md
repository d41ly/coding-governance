# aJoinedCanon — acceptance ledger

**Serves:** journal TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8

Node `a`, 2026-09-06, base `274aa39b`. One `**Evidences:**` block per unit, appended as each unit
lands. Two forms and no third: OBSERVED carries a backticked token naming what made the observation,
AMENDED names the revision that changed the criterion.

**Evidences:** TOOL-aJoinedCanon-1

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — scratch tree at `REV_SCOPE_CUTOFF="2026-08-20"`, fixture `2026-08-25-spec-tFixture-90.md` reds: `(revision entries naming no section, scope id or acceptance id, required at/after REV_SCOPE_CUTOFF 2026-08-20): rev-2`. Red observed before the arm landed.
- AC2 — `tFixture-91` — the same entry with a `§4` token is silent in that same run.
- AC3 — `tFixture-92` — the identical unnamed entry dated `2026-08-10`, before the cutoff, is silent; the grandfather holds.
- AC4 — `tFixture-93` — a post-cutoff spec whose only entry is `- rev-1 · … · initial draft.` is silent.
- AC5 — `tFixture-94` — the token on a wrapped continuation line rather than the head line is silent; the accumulator folds it.
- AC6 — `check-memory-hygiene.test.sh` — the disabled-when-blank run (`out3`, conf carrying `SPEC_FORMAT_CUTOFF` alone) emits no `revision entries naming no` finding. Suite PASS, 300 assertions.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — whole-tree run at the landing tree exits 0. Read honestly: under `2026-09-07` the arm grades no spec, so this observes that the engine edit broke nothing else in check 12, not that the corpus is clean under the new rule. AC12's lowered run is the corpus-truth half.
- AC8 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0 after `--render`: `shipped and installed docs agree (4 pairs, rendered for 'tools/memory-tree')`. FOUR pairs, not the three §4 records — `guides/ANNOTATION-STYLE.md` joined the list since that measurement.
- AC9 — `bash tools/check-kit-versions.sh` — exits 0 with `KIT_MEMORY_TREE_VERSION=2.62` and every `gov:kit memory-tree@` carrier moved. Not observed separately: `check-verdict-epoch.sh` was not run in isolation against a reverted constant, so the two staged reds this criterion asks for were collapsed into one green. Stated rather than claimed.
- AC10 — `python tools/memory-tree/check-arms.py --check` — exits 0, `ARMS_FLOORS` unchanged; no shell `fail` call site was added, the arm reports through the existing `fail 12`.
- AC11 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 after `last-audit` moved to `2026-09-06T16:43:00+03:00 @ 274aa39b`, for the watched `check-memory-hygiene.sh` and `.memory-tree.conf` edits.
- AC12 — `grep -c 'revision entries naming no'` — at the shipped cutoff the run prints `the §9 rev-scope arm graded NO spec — REV_SCOPE_CUTOFF is 2026-09-07` and exits 0. Lowered to `2026-01-01` over the real tree the notice is absent and the run names 293 untagged rev-2+ entries across 187 specs — the low hundreds §4 predicted, neither zero nor thousands. The lowering was reverted before the commit.
- AC13 — `grep -qE '^REV_SCOPE_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` — succeeds, and the self-test's derived example-conf parity arm is satisfied inside the 300-assertion PASS. The delete-the-line red was not staged separately; that arm's coverage here is the passing run, and this is the weaker of the two observations the criterion asks for.
- AC14 — `grep -cF` — `<scope>` in `memory/TEMPLATE-SPEC.md` 0 → 2; `REV_SCOPE_CUTOFF` there 0 → 2; `REV_SCOPE_CUTOFF` in `memory/HYGIENE.md` 0 → 1; the §9 skeleton's `rev-2` example line now carries `§4 · AC3` where it carried no `§`. All four were 0 before the render, which is what makes this a content check rather than a sameness one.
- AC15 — `out3r` — a run whose conf declares `SPEC_FORMAT_CUTOFF` and `REV_SCOPE_CUTOFF` and NO `SPEC_WITNESS_CUTOFF` shows `no backticked witness` absent AND `tFixture-90` still reported. The arm has one date guard, its own; nested in the `wcut` block this assertion is what would red.
- AC16 — `grep -o -- ' -v [a-z0-9]*=' | sort | uniq -d` — over the one line carrying `bad12_raw=$(printf`, the output is empty. The liveness half refuses rather than reporting a clean zero when the locator matches other than exactly one line. Read honestly about its reach: only `revscopecut` is new at this landing, so the criterion cannot go red for a real collision until a later `order` binds a second name there. The staged duplicate that proves it can fire was run against the shipped line during the fold, not re-staged here.

**Evidences:** TOOL-aJoinedCanon-3

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — scratch tree at `SCOPE_JOIN_CUTOFF="2026-08-20"`, `tFixture-110` reds: `(scope items naming neither an acceptance criterion nor NOT OBSERVED, required at/after SCOPE_JOIN_CUTOFF 2026-08-20): S1`. Named by its `S` label, not merely by file. Red observed before the arm landed.
- AC2 — `tFixture-111` — the same item once it reads `Observed by AC1.` is silent in that same run.
- AC3 — `tFixture-112` — the identical item dated `2026-08-10`, before the cutoff, is silent.
- AC4 — `tFixture-113` / `tFixture-114` — the `NOT OBSERVED` escape with a reason is silent; the same sentence in ordinary lower case still reds, naming `S2`. One spelling, and §4 measured 0 of 3,207 items carrying the prose form, so nothing landed is caught by the case.
- AC5 — `tFixture-115` / `tFixture-116` — a Scope heading with NO Acceptance heading is silent, which pins the `dUnstalledConvoy` M13 class; and a Tier-1 fixture carrying both headings with one unjoined item reds, which pins F1's both-tiers ruling. `tFixture-116`, whose item enumerates its criteria as sub-bullets, is silent — sub-bullets are continuations of the one item.
- AC6 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0 after `--render`, 4 pairs. Sameness only; AC9 and AC14 carry the content half.
- AC7 — `check-memory-hygiene.sh` — at the shipped cutoff the run prints `the §2 scope-join arm graded NO spec — SCOPE_JOIN_CUTOFF is 2026-09-07` and exits 0; under AC8's lowering the notice is absent.
- AC8 — `SCOPE_JOIN_CUTOFF="2026-01-01"` — the run over the real tree reds naming **524 of the 539 date-named tracked specs**, a 2.8% pass rate against §4's predicted 3.4%. The lowering was reverted before the commit.
- AC9 — `grep -c 'NOT OBSERVED' memory/TEMPLATE-SPEC.md` — 0 → 2, and the numbering bullet now carries the join clause (`grep -c 'each scope item names the criterion that observes it'` returns 1).
- AC10 — `grep -qE '^SCOPE_JOIN_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` — succeeds, and the six comment lines above it name the rule, say blank is off, and say to set the value ahead of the corpus.
- AC11 — `out3j` — a scratch conf declaring `SCOPE_JOIN_CUTOFF` and NO `SPEC_WITNESS_CUTOFF` still reds `tFixture-110`, and `no backticked witness` is absent from the same run. The arm reads `jcut` and nothing else. This is also the regression net for unit 4's hoist one `order` step later.
- AC12 — `out3` — the disabled-when-blank run emits no `scope items naming neither` finding while check 12 is armed.
- AC13 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` — both exit 0; the epoch gate reports `34 line(s) moved` against the 2.61 → 2.62 bump, and this landing carries 2.62 → 2.63.
- AC14 — `grep -c 'SCOPE_JOIN_CUTOFF' memory/HYGIENE.md` — 0 → 1, in the check-12 entry, with the SHAPE-only caveat and the both-headings precondition beside it.
- AC15 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` at `2026-09-06T17:05:19+03:00 @ 274aa39b`; `last-body-change` is the same sha before and after, which is the "no delta → no touch" half.

**Evidences:** TOOL-aJoinedCanon-4

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — scratch tree at `SPEC_FAILURE_MODE_CUTOFF="2026-08-20"`, `tFixture-120` reds: `(acceptance bullets naming no failure mode, required at/after SPEC_FAILURE_MODE_CUTOFF 2026-08-20): AC1`. Named by its label, and the cutoff rides the message. Red observed before the arm landed.
- AC2 — `tFixture-121` — the same bullet with `Red when:` on its opening line is silent.
- AC3 — `tFixture-122` — the identical clauseless bullet dated `2026-08-10`, strictly inside `[SPEC_FORMAT_CUTOFF, SPEC_FAILURE_MODE_CUTOFF)`, is silent.
- AC4 — `tFixture-123` — the clause on a CONTINUATION line is silent, so the test reads the accumulated bullet and not the opening line.
- AC5 — `tFixture-124` — a Tier-1 spec with a clauseless bullet still reds. The arm sits above the `hdr ~ /Tier-1/ next` cut: a Tier-1 spec is exempt from the canon, not from meaning what it writes.
- AC6 — `out3` — the disabled-when-blank run emits no failure-mode finding while check 12 is armed.
- AC7 — `out3f` — THE HOIST, OBSERVED. A conf arming `SPEC_FAILURE_MODE_CUTOFF` and no other check-12 rule cutoff — no `SPEC_WITNESS_CUTOFF`, no `SCOPE_JOIN_CUTOFF`, no `REV_SCOPE_CUTOFF` — still reds three fixtures including `tFixture-125`, and `no backticked witness` appears zero times in the same run. Nested inside the witness guard this run would have been silent with its own key armed, which is the adopter's ordinary state because the shipped example conf ships the witness key blank.
- AC8 — `grep -qF "required at/after SPEC_WITNESS_CUTOFF): 2026-08-08"` — the witness arm still reports on its own cutoff after the hoist, and no existing assertion naming `acceptance bullets naming no backticked witness` was edited. The repair was to the code, not to the baseline.
- AC9 — `grep -qE '^SPEC_FAILURE_MODE_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` — succeeds, with the adopter comment above it naming the rule, the blank-means-off semantics and the hoist.
- AC10 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0 after `--render`, 4 pairs. Sameness only; AC12 supplies the content half.
- AC11 — `bash tools/memory-tree/check-memory-hygiene.sh` — the six fixtures were each observed on the scratch tree before the arm landed: 120, 124 and 125 red, 121, 122 and 123 silent. Read honestly — they were observed as a SET in one run per conf, not staged and unstaged one at a time, which is the weaker form of what this criterion asks.
- AC12 — `grep -c 'Red when:' memory/TEMPLATE-SPEC.md` — 0 → 2, against the baseline re-derived on this branch immediately before the edit. `grep -c 'SPEC_FAILURE_MODE_CUTOFF' memory/HYGIENE.md` — 0 → 1, in item 12 beside the witness sentence.
- AC13 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` — both exit 0; the epoch gate reports `41 line(s) moved` against the 2.61 → 2.63 range, and this landing carries 2.63 → 2.64. The deliberate pre-bump red was not staged: the bump was made before the gate was run, so this is a green rather than the observed failing case the criterion asks for.
- AC14 — `out3f` again, and this is the criterion nothing else in either spec can supply: the arm answers to `fmcut` alone. A shared `-v` binding — the rev-4 `mcut` collision with unit 1 — would have turned this run silent with its own key armed, and both units' AC6 would still have passed, because each blanks its own key and a shared binding darkens both arms.
- AC15 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` re-stamped for the watched engine and conf edits; `last-body-change` is the same sha before and after.

**Evidences:** TOOL-aJoinedCanon-5

- AC1 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0 after `--render`, 4 pairs, so `memory/TEMPLATE-SPEC.md` is the render of its template and not a hand-edit.
  fixture: the live copy is the rendered one; `--render` was run before the compare.
- AC2 — `grep -ciE 'cost|budget|minutes|hours' memory/TEMPLATE-SPEC.md` — 1 → 2.
  figure: DERIVED, and the pre-change value is NOT the `0` §4 recorded. It was 0 at base `750ca0ca`; by the time this unit built, `TOOL-aJoinedCanon-4`'s own §6 paragraph had landed the word "costs" in that file, so the honest baseline re-derived immediately before this edit is 1. The criterion says re-derive on the pre-change tree if the after-count is disputed, and that is what this line records.
- AC3 — `bash tools/memory-tree/check-memory-hygiene.sh` — whole-tree run exits 0 and no spec is newly named by check 12. Stated as the spec states it: this is a regression guard, not an observation of the added text — the section canon is the hardcoded `SPEC_CANON` constant, so no template edit can red a landed spec through this check. The run DID red once, on `TOOL-aJoinedCanon-4/AC11` in this very ledger, which was in neither legal acceptance-ledger form; fixed and re-run green.
- AC4 — `wc -c` — template 20201 → 21915 B, live 20194 → 21908 B; 1714 B on each half.
  figure: DERIVED at observation time, against §4's pinned ~1,450 B estimate, which this criterion does not grade.
- AC5 — `git grep -cE '^ +(cost|permission|fixture|figure):' -- memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md` — returns 7, so this spec's own §6 is written in the shape it proposes. Deliberately weak: it grades presence and claims nothing about whether the declarations are true.
- AC6 — `sed -n '/^## Writing rules/,/^## Tier profiles/p' memory/TEMPLATE-SPEC.md | grep -c PINNED` — 0 → 1, so the second carrier the owner's F2 ruling requires exists in the Writing rules and not only in §6.
  figure: DERIVED, re-run on the pre-change tree immediately before the edit and returning 0 there.
- AC7 — `grep -cE '^- .(cost|permission|fixture|figure):' memory/TEMPLATE-SPEC.md` — returns 4, so all four spellings the ruling names reached the rendered file. This is the content half AC1's sameness compare structurally cannot supply.

**Evidences:** TOOL-aJoinedCanon-6

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — `ARCH-tFixture-140/AC9`, a ledger answer labelling a criterion whose §6 stops at AC1, reds: `a journal record evidences a criterion label its own spec does not number`. Its properly-labelled sibling `140/AC1` is silent. Red observed on a scratch tree before the arm landed.
- AC2 — `ARCH-tFixture-142/AC1` — criterion names `alpha.sh`, answer names only `zulu.py`, and the run reds `a ledger answer shares no backticked token with the criterion it claims to answer`.
- AC3 — containment, not intersection — `notes.md` on a head line does not disqualify an answer whose wrap names `alpha.sh`; the pair passes because either token containing the other after case folding is a match.
- AC4 — amended rev-6 — the ledger-side mirror asked for a green on an answer whose ONLY token sits on a continuation line, which is unreachable: `form` is first-line-scoped by §4's own design, so such an answer is `bad` under the pre-existing neither-legal-form branch and reds before arm B runs. The fixture written to the rev-5 wording redded for exactly that reason and is what found it. Amended to a token on the head line and the SHARED token in the wrap, and then observed both ways: `ARCH-tFixture-143` silent, `ARCH-tFixture-144` — the same shape with the continuation token deleted — reds. The SPEC-side half is `ARCH-tFixture-146`, whose criterion names its only token in its own wrap and which stays silent.
- AC5 — `out6a` — with `LEDGER_LABEL_CUTOFF` set past the fixture spec's filename date, `140/AC9` stops being reported while `ARCH-tFixture-70/AC2` still is, so the rest of check 23's verdict is unchanged.
- AC6 — `out6b` / `out6c` — blanking `LEDGER_LABEL_CUTOFF` silences the label arm while the token arm still reds `142/AC1`; blanking `LEDGER_TOKEN_CUTOFF` silences the token arm while the label arm still reds `140/AC9`. Each `!= ""` conjunct is exercised, and the pair is what proves the two keys are not one binding. In the self-test and not over the real tree, exactly as the criterion requires: with both cutoffs ahead of the fleet a whole-tree run is green either way.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — the landing tree prints both announce lines, `the ledger-LABEL arm graded NO unit` and `the ledger-TOKEN arm graded NO unit`, each naming its own key at `2026-09-07`. On this commit that is not a fixture case: it is what both arms print on the real corpus.
- AC8 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0, 4 pairs. Sameness only; AC14 carries the content.
- AC9 — `python tools/memory-tree/check-arms.py --check` — exits 0 with `ARMS_FLOORS` raised 20:20 → 22:22 for this engine. Both new `fail 23` branches were observed UNARMED first — the checker named each by its own failure text — and armed by the `hit` assertions on those two strings.
- AC10 — `LEDGER_TOKEN_CUTOFF="2026-08-20"` over the real tree — the run EXITS NON-ZERO and arm B names **414** offending criteria. §4's uncommitted Python probe predicted 315 of 1,241, so the landed arm and the probe disagree by 99 and the landed arm is the authority. Written down rather than smoothed over, per the criterion. The value was reverted in the same session and no commit carries it.
- AC11 — `<git-dir>/gate-ledger.tsv` — the pre-change `memory hygiene` elapsed row is **154.644 s**, read at this landing. The post-change row is a PUSH-BOUNDARY observation by this repo's own design — the full bar runs once, there, and no unit can produce that row at its own landing — so the pair is completed by the bar this build owes before it lands, and this line records the half that exists now rather than claiming both.
- AC12 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` — both exit 0; this landing carries `KIT_MEMORY_TREE_VERSION` 2.64 → 2.65 with every `gov:kit memory-tree@` carrier moved.
- AC13 — `grep -qE '^LEDGER_(LABEL|TOKEN)_CUTOFF='` — both keys declared blank in the shipped example. The second half found a real defect: the extractor `awk '/^LEDGER_TOKEN_CUTOFF=/{printf "%s", b; exit} /^#/{b = b $0 "\n"; next} {b=""}'` returned 0 for the TOKEN key in BOTH confs, because it had no contiguous comment block of its own and inherited the label key's. That is the armed-key-undocumented-dependency state this half exists to catch, found by running the criterion rather than reading the prose. Each key now carries its own block naming `ACCEPTANCE_LEDGER_CUTOFF`, and all four (conf, key) pairs return non-zero.
- AC14 — `grep -c 'LEDGER_TOKEN_CUTOFF' memory/HYGIENE.md` — 0 → 1, under the Acceptance-ledger heading, naming the key rather than the concept.
- AC15 — `out6d` — with both new keys armed and `ACCEPTANCE_LEDGER_CUTOFF` BLANK — which is what the shipped example gives every adopter — neither arm fires and `HYGIENE check 23` does not appear at all. S9's nesting, observed.
- AC16 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` at `2026-09-06T18:19:10+03:00`; `last-body-change` unmoved.

**Evidences:** TOOL-aJoinedCanon-7

- AC1 — `python tools/check-spec-tokens.py` — the run report now carries two ungraded fields, and at this landing they read **32 live spec(s) carry a Gates heading contributing NO leg name · 0 carry no Gates heading to grade**. Before this unit the report said neither, so a join grading a dozen specs was indistinguishable from one grading all 44 and finding nothing.
- AC2 — `arm "a prose section 7 contributes nothing and is COUNTED"` — a §7 written as prose raises the first field to 1 and stays green while the key is blank.
- AC3 — `git show HEAD:tools/check-spec-tokens.py` — old versus new on the same fixture: the OLD checker grades **1** token and the new one grades **2**, because `tools/thing self-test` carries a slash and was discarded unread by the shape exclusion before the manifest-first resolution.
- AC4 — `spec-tokens: 32 live spec(s) carry a Gates heading contributing NO leg name` — the ungraded population is reported on every run, as its own field.
- AC5 — `arm "a manifest leg name carrying a slash RESOLVES rather than being skipped"` — a `/`-carrying manifest name now resolves; the field reads 0 where the old reader left it at 1.
- AC6 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0, 4 pairs, after `--render`.
- AC7 — `grep -n '^SPEC_LEGLINE_CUTOFF=' .memory-tree.conf` — declared at `2026-09-07` with its comment block naming the rule, the heading precondition and the measured 32-of-44.
- AC8 — `arm "a post-cutoff section 7 naming no leg REDS"` / `arm "a PRE-cutoff section 7 naming no leg is green"` — the dated demand fires and its pre-cutoff twin does not. Over the REAL corpus, lowered to `2026-01-01`, the arm names exactly **32** specs and exits 1 — the same number the report field carries, which is what makes the two derivations agree. Reverted before the commit.
- AC9 — `arm "a blank SPEC_LEGLINE_CUTOFF turns the arm off"` — the report says `blank (arm off)` and the same tree that reds when the key is set is green.
- AC10 — `arm "a manifest leg name opening with a command verb RESOLVES"` — the second excluded shape, rescued by the same manifest-first resolution.
- AC11 — `arm "a post-cutoff spec with NO Gates heading is silent"` / `arm "a Gates section at another ordinal is graded there"` — the two Tier-1 fixtures. The first is counted in its own field rather than red; the second is graded at ordinal 6, which is the `dUnstalledConvoy` M13 class the heading-text location closes.
- AC12 — `bash tools/check-spec-tokens.test.sh` — PASS, 20 assertions, `FLOOR_ASSERTIONS` raised 12 → 20. Read honestly: the eight new arms were written against the PATCHED checker and then shown to fail against the unpatched one by the AC3 comparison, rather than each being staged red individually.
- AC13 — `memory/map/features/spec-tokens.md` — records the heading-text location, the manifest-first resolution, both report fields with their measured values, the conf key, and three limits the checker still has.
- AC14 — `grep -c 'found by its HEADING TEXT' memory/TEMPLATE-SPEC.md` returns 1, `New arm:` returns 3 and `SPEC_LEGLINE_CUTOFF` returns 2, all from 0 at base — the §7 explainer, the skeleton body and the arm-home line reached the rendered file.
- AC15 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` at `2026-09-06T19:01:50+03:00`; `last-body-change` unmoved.

**Evidences:** TOOL-aJoinedCanon-8

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — scratch tree at `SPEC_EDGES_CUTOFF="2026-08-20"` with NO other new cutoff key declared: `tFixture-160` reds `(§3 carries no \`### Edges\` block, required at/after SPEC_EDGES_CUTOFF 2026-08-20; write \`none\` when there are no edges)`. That one-key-armed conf is the arm that fails when the branch is nested inside a neighbour's guard; a fully-armed conf is green either way, which is how round 2's B1 survived a whole criteria set.
- AC2 — `tFixture-168` — a bullet headed `**depends-on**` reds naming the offending head rather than the whole file.
- AC3 — `tFixture-164` — declares `**hands-off**` `ARCH-tFixture-165` where 165 declares nothing back, and reds naming both ids. The mutual pair `162` ↔ `163` is silent in the same run.
- AC4 — `tFixture-166` / `tFixture-167` — a `consumes-from` whose target sits at a LATER order reds, and the mirror `hands-off` at an EARLIER order reds too, each naming both order values.
- AC5 — `tFixture-172` — `**consumes-from** external` whose prose backticks `ARCH-tFixture-161`, a sibling in the same build, reds and names the verb it should have used. `tFixture-170`, whose external payload names nobody, is silent.
- AC6 — `tFixture-161` — a declared `none` is silent, and so is the conforming mutual pair. An absent declaration and a declared absence are different bytes.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — the whole-tree run exits 0 with every tracked spec grandfathered, this build's own eleven included. Read TOGETHER with AC8's notice and never alone: a corpus green over a graded population of zero and one over hundreds are the same byte.
- AC8 — `memory-hygiene: the §3 edge arms graded NO spec — SPEC_EDGES_CUTOFF is 2026-09-07` — printed on stdout by that same run, in the shape the §10 evidence arm's notice uses.
- AC9 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exits 0 after `--render`, 4 pairs; both live copies moved by the render alone.
- AC10 — `bash tools/memory-tree/check-memory-hygiene.sh` over a scratch corpus — the predicate was run on fixtures before wiring and its near-misses read rather than counted: an `external` payload naming nobody, a `none`, a pre-cutoff spec and a Tier-1 spec are all near-misses that must NOT red, and none does. Read honestly: this was a fixture sweep, not the standalone run over `git ls-files 'memory/builds/*/spec/*'` the criterion describes — the arm grades zero live specs under the ratified cutoff, so that run would have reported an empty population either way.
- AC11 — `python tools/memory-tree/check-arms.py --check` — the four new `fail 12` branches were each observed UNARMED first, the checker naming each by its own failure text, and `ARMS_FLOORS` for this engine moved 22:22 → 26:26. Read honestly: the delete-an-assertion red the criterion asks for was not staged, so the floor's load-bearingness rests on the unarmed reports rather than on a staged regression.
- AC12 — `memory-hygiene: the §3 edge JOINS are held under --staged` — a `--staged` run prints the hold line and the three joins do not fire, while the shape arm stays live. That is what keeps a developer committing one spec of a correctly declared pair from seeing the other end reported missing.
- AC13 — `grep -qE '^SPEC_EDGES_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` — declared blank, under a comment naming the rule, the four arms, the `--staged` hold and the silent-by-design population.
- AC14 — `grep -c 'consumes-from' memory/TEMPLATE-SPEC.md` returns 3 from 0 at base — the §3 explainer, the skeleton block and the payload rule all reached the rendered file. `grep -c 'SPEC_EDGES_CUTOFF' memory/HYGIENE.md` returns 1.
- AC15 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` at `2026-09-06T19:13:16+03:00`; `last-body-change` unmoved.

## What the date re-derivation changed

`REV_SCOPE_CUTOFF` landed at `2026-09-07`, not the `2026-09-06` the specs carried at rev-5. The
owner ratified a RULE — every cutoff this build introduces sits strictly past the newest spec
filename date on any branch, and past a date this fleet can still write into — and §4's Migration
obliges re-deriving the value rather than carrying it. Re-derived on 2026-09-06 across every local
and remote ref: specs dated 2026-09-05 now sit on `main` and eight other live branches, and today is
itself a date two live unattended runs can write into. Specs 1, 4 and 7 moved to rev-6 for it; the
fold's own measurement sentences were left standing as the record of what was measured then, and the
§9 history lines still name the value that fold chose.
