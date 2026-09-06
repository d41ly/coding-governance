**Serves:** journal TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

# aHoistedPass — the landing, after the run had already aborted at it

*Written on node `a`, 2026-09-06, after `origin/main` accepted `274aa39b..119c2823`. This record
exists because the run-state file is TERMINAL and says `ABORTED`, and the driver refuses to move a
finished record: "a finished record is not something to move, re-open or re-pin; every later run is
measured against the counter this record left." That refusal is right and the record is not rewritten.
What follows is the part that happened afterwards.*

## Why the run aborted, and why that was not wrong

The run reached `LANDING`, could not land, and took `--abort` with halt code
`repo-state-out-of-mandate`. The reason was not this build: `tools/push-main.sh` must run from the
primary tree on `main`, and that tree's `main` had DIVERGED from `origin/main` — 13 local commits
against 2 remote — where the 13 were another build's completed-but-unpushed landing
(`aWeighedCanon`/`aJoinedCanon`, merged 3 to 6 hours earlier with its own merge commit and post-merge
manifest re-stamp). The lander pushes local `main`, so landing here would have published 13 commits
whose own run had not published them. A standing mandate authorises merging and pushing THIS build;
it does not authorise making another build's publish decision.

**The owner then instructed the landing.** By the time that instruction arrived the objection had
dissolved on its own: those 13 commits had been pushed by their own session, and the primary tree was
clean and synced. Nothing was overridden to make this landing happen — the blocking condition ended.

## What the landing cost, in the order it was found

`origin/main` had moved **156 commits** past the run's pinned BASE. Reconciled ON THE BRANCH first,
so the primary tree only ever saw a conflict-free merge (`d03c90fd`). Six conflicts, resolved by kind:

- **Four were GENERATED** — `memory/LIVE.md`, `memory/ledger/2026-09.md`, `memory/map/generated/MAP.md`
  and `symbols.json` — re-rendered from source, never hand-reconciled. The row-merge driver settled
  the backlog shards itself: 405 rows written, 0 row conflicts, 0 structure conflicts.
- **One was CODE**, and it resolved better than either side alone. `check-pass-order.sh`: this build
  calls `build_commit()` in the kit library, where `TOOL-aHoistedPass-7` lifted it; `main` had
  independently rebuilt the inline `_find_build_commit` with an enumeration cap and a fix for
  `rev-list --reverse --max-count` applying the count before the reverse. `lib-unattended.sh` merged
  clean and ALREADY CARRIED those improvements, so keeping the library call and dropping the inline
  copy lost nothing.
- **One was the MANIFEST**, and this build's half was reconciled AWAY. Both sides had re-stamped;
  `main`'s stamp was taken and re-stamped in a follow-up per the merge exception. The §B bullet this
  build had added — that `passes-harnessed` now resolves — was DROPPED rather than squeezed in: the
  file sits at its 25600-byte cap, check 7 says trim rather than raise, and the fact is enforced by
  check 16's body term and check 31. Gate over remember. The manifest landed byte-identical to
  `main`'s.

## The bar found six red legs, and one of them was a regression this merge caused

**This is the part worth keeping.** The `--close` override was taken on a bar that never RETURNED,
on the argument that the push boundary is the gate that actually binds. The push boundary then ran
the bar to completion and refused the push. It was right to, and here is what it caught.

| leg | cause | after |
|---|---|---|
| `kit version markers` | the new leg shipped at `1.17` against a `1.18` constant | exit 0 |
| `govkit selfcheck` | the same single cause | exit 0 |
| `lexicon naming predicates` | 987 verb offenders over a pin of 978 | exit 0 |
| `lexicon wiring` | the same cause; it shells out to the same engine | exit 0 |
| `brief-recorded` | a cutoff dated at an expected landing, plus contention | exit 0 in 43 s |
| `pass-order history` | **an orphaned subject cache** | exit 0 in 276 s |

**`pass-order history` is the one no reading of the diff would have caught.** The merge resolution
above is correct by every check a reviewer applies — one definition, two call sites, no duplication —
and it silently orphaned a `_SUBJ` subject cache that `main` had added hours earlier, because the
cache's READER lived inside the inline copy that was dropped. The cache went on being BUILT and
size-asserted by `check-pass-order.sh` and consulted by nothing: `git grep _SUBJ` returned four lines
and every one was a write. On a 10,811-commit walk that is a `git log` plus a `printf|tr` per commit.

The magnitudes come from `.git/gate-run/`, which holds a per-leg row for every bar this node ran that
day, and which is the artifact that settled it: **591 s cached, 3977–5401 s uncached**, with the
merged tree back on the uncached side and the leg's own ceiling at 5400 s. The same uncached shape
ran 3977 s green and 5401 s killed on `main` earlier the same day, so the REGRESSION is the merge's
and the TIMEOUT VERDICT was contention-decided — both, not either.

Restored cache-first with the per-commit fallback intact, and the array probe asked ONCE outside the
walk so a caller declaring no `_SUBJ` cannot error under `set -u`. Measured after: 276 s, below even
`main`'s own cached 591 s.

**Two of the six were one leg twice**, and two more were two problems wearing one red:
`brief-recorded`'s exit 1 was the cutoff and its 900 s kill was contention — 43 s standalone. The
cutoff had been dated `2026-09-05` as "the landing" when `TOOL-aHoistedPass-7`'s F1 ratified that
form; the landing slipped to `2026-09-06`, and two builds opened in the gap — `aKeyedAnnotation` and
`dTracedLattice`, both landed on `origin/main` with zero brief rows, because this leg did not exist
when they ran. Moved to the actual landing date, which is what F1 ratified: `graded 0 · 101 skipped`.

## What was deferred rather than done, and where it lives

- `TOOL-aHoistedPass-40` — the kit gate's import allow-list is a fourth hand-typed spelling of its
  conf key set that nothing joins. The join was written and WITHDRAWN unlanded: its two refusal
  branches each owe an arm, the only suite that can carry one is on no bar, and the node could not
  fork to observe the failing case. Predicate measured at zero hits and zero near-misses first.
- `TOOL-aHoistedPass-41` — one of the ten new verb offenders is engine-classified DEBT with a named
  rename (`has` → `check`); nine are UNRULED. Deferred because `has`/`hasnt_`/`same` are the
  assertion helpers every suite in this kit spells identically.
- `TOOL-aHoistedPass-42` — `unattended-build.test.sh` and `unattended-unit.js` are named by no row in
  the 96-leg manifest and by no on-demand runner. Green-by-absence waiting to happen.

## The state this landed in

`origin/main` accepted `274aa39b..119c2823`. The build's merge commit is `8a36ff4e` and the run's
branch tip `36a90178`; both are ancestors of `origin/main`. The pre-push hook forced a FULL gate
because the recorded green was 55 commits behind the tip against a bound of 10 — so the tree that
landed was gated whole, not incrementally.

**Thirteen decisions are parked in `RUN.md`** with the options seen and the reason each was refused,
including the two veto-2 owner turns this build's own design predicted: `TOOL-aHoistedPass-7` edits
`UNATTENDED-PROTOCOL`, and `TOOL-aHoistedPass-2` plus the F6 fold edit `SKILL.template.md`.
