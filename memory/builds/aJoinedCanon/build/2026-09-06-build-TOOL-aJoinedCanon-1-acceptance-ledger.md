# aJoinedCanon — acceptance ledger

**Serves:** journal TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4

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
- AC11 — the six fixtures were each observed on the scratch tree before the arm landed: 120, 124 and 125 red, 121, 122 and 123 silent. Read honestly — they were observed as a SET in one run per conf, not staged and unstaged one at a time, which is the weaker form of what this criterion asks.
- AC12 — `grep -c 'Red when:' memory/TEMPLATE-SPEC.md` — 0 → 2, against the baseline re-derived on this branch immediately before the edit. `grep -c 'SPEC_FAILURE_MODE_CUTOFF' memory/HYGIENE.md` — 0 → 1, in item 12 beside the witness sentence.
- AC13 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` — both exit 0; the epoch gate reports `41 line(s) moved` against the 2.61 → 2.63 range, and this landing carries 2.63 → 2.64. The deliberate pre-bump red was not staged: the bump was made before the gate was run, so this is a green rather than the observed failing case the criterion asks for.
- AC14 — `out3f` again, and this is the criterion nothing else in either spec can supply: the arm answers to `fmcut` alone. A shared `-v` binding — the rev-4 `mcut` collision with unit 1 — would have turned this run silent with its own key armed, and both units' AC6 would still have passed, because each blanks its own key and a shared binding darkens both arms.
- AC15 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 with `last-audit` re-stamped for the watched engine and conf edits; `last-body-change` is the same sha before and after.

## What the date re-derivation changed

`REV_SCOPE_CUTOFF` landed at `2026-09-07`, not the `2026-09-06` the specs carried at rev-5. The
owner ratified a RULE — every cutoff this build introduces sits strictly past the newest spec
filename date on any branch, and past a date this fleet can still write into — and §4's Migration
obliges re-deriving the value rather than carrying it. Re-derived on 2026-09-06 across every local
and remote ref: specs dated 2026-09-05 now sit on `main` and eight other live branches, and today is
itself a date two live unattended runs can write into. Specs 1, 4 and 7 moved to rev-6 for it; the
fold's own measurement sentences were left standing as the record of what was measured then, and the
§9 history lines still name the value that fold chose.
