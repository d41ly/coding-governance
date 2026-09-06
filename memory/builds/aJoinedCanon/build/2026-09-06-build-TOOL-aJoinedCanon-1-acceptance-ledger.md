# aJoinedCanon — acceptance ledger

**Serves:** journal TOOL-aJoinedCanon-1

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

## What the date re-derivation changed

`REV_SCOPE_CUTOFF` landed at `2026-09-07`, not the `2026-09-06` the specs carried at rev-5. The
owner ratified a RULE — every cutoff this build introduces sits strictly past the newest spec
filename date on any branch, and past a date this fleet can still write into — and §4's Migration
obliges re-deriving the value rather than carrying it. Re-derived on 2026-09-06 across every local
and remote ref: specs dated 2026-09-05 now sit on `main` and eight other live branches, and today is
itself a date two live unattended runs can write into. Specs 1, 4 and 7 moved to rev-6 for it; the
fold's own measurement sentences were left standing as the record of what was measured then, and the
§9 history lines still name the value that fold chose.
