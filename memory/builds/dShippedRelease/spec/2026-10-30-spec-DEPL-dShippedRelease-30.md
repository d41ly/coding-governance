# DEPL-dShippedRelease-30 — the patch build's shared budget: one red, one patch, a draw on the root's lease and the third keep-waiting

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 16 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0440@a7f19c9e whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md](../build/2026-10-30-build-DEPL-dShippedRelease-11-reuse-scout-b.md) | research | DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-27 |
| [2026-10-30-build-DEPL-dShippedRelease-30-deviation-301.md](../build/2026-10-30-build-DEPL-dShippedRelease-30-deviation-301.md) | deviation | — |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

Rework raised by a landing stays bounded. One red files one patch under the key (`default-branch-red`,
landed SHA), a chain of patch builds draws on its root's one budget, a draw on a closed root serialises on
the root's lease and always leaves it terminal, and a release hold ends at the third keep-waiting answer.
This is the budget half of P39 for the time after a build has closed.

## 2. Scope (IN)

This unit owns no node. It reads `item.deploy.core` and `item.deploy.released`, the items its filing and its
count hang from, and the keys `flow.rework-budget`, `leases.queued-claim-days` and `patch.ratify`, each read
through its owner's reader.

**Build-run preconditions**, each specced and unbuilt at this base: `budget.py` (TOOL-dDeclaredLoop-30);
`--lease acquire build <slug> --for draw`, tombstones and `--lease prune` (TOOL-dPlacedRequest-16); the
claim's `origin-slug` and `read_claim_body` (TOOL-dPlacedRequest-21); `intake.py` with the `landing` origin
(TOOL-dWellOiledMachine-27, unit 13's ask); `read_landing` (DEPL-dShippedRelease-1); `read_core_verdict` and
`derive_red_key` (DEPL-dShippedRelease-13); and `measure_keep_waiting` and the hold's chain
(DEPL-dShippedRelease-5). The post-close row is stated at DEPL-dShippedRelease-13 §4 "The post-close row".

- **S1** — The root. `resolve_budget_root(slug, root)` in `tools/loop/deploy_items.py` reads `origin-slug`
  from `read_claim_body refs/gov/claims/<slug>` and walks until a claim holds none, falling back to the
  first `parents:` entry of the build's README where no claim exists, as TOOL-dDeclaredLoop-30 S7 does. A
  build with no origin is its own root. A cycle, or more than 32 steps, refuses naming the chain. So a patch
  of a patch draws on the root, where S7 of that spec drew on the middle build. Observed by AC1.
- **S2** — The draw, `run_root_draw(build, cause, item, root)`. `python budget.py draw`
  (TOOL-dDeclaredLoop-30) calls it for a build whose root is another build, and for the causes
  `patch:<slug>` and `release-retry`; every other draw is unchanged. It reads the root's lease class and
  takes the route of §4 "The draw". On a tombstone: `--lease acquire build <root> --for draw`, whose
  compare-and-swap serialises concurrent draws and bumps the epoch; then
  `read_root_budget(root_slug, root)`, always after the acquisition, so a loser re-reads the remaining
  budget before it draws; then one push, `--lease draw build <root> --row <row>`, writing a record with
  status `landed` at the same epoch, parented on the hold, whose body key `draw` is the row
  `draw · <cause> · <item> · <spent>/<total>`. That one commit is both the append and the release (pin C8).
  `exhausted` releases with no row and answers `exhausted`. A lost acquisition retries up to
  `DRAW_ATTEMPTS`, 5, at two-second pauses, then answers `contention`, which draws nothing
  (TOOL-dDeclaredLoop-30 S5). Observed by AC2, AC3, AC9.
- **S3** — The budget's reader. `read_root_budget` reads the root's `transition` rows through `budget.py`'s
  reader and adds each `draw` key on the root lease's first-parent chain, so spent and total stay derived,
  and the frozen total is the root's. `python budget.py state --build <root>` prints the sum. Observed by
  AC1, AC2.
- **S4** — A live root. A red files at `deploy.core`, while the root's lease is live, and the patch draws
  after it claims. A root whose lease is live under another holder answers `contention`, exit 4, no row
  written, and the draw site retries at its next act, which is TOOL-dDeclaredLoop-30 S5's "a wait on a lease
  another live build holds". The root reaches its tombstone at `deploy.unlease`, whose own build is not
  waiting on the draw. Observed by AC6.
- **S5** — A root with no lease (pin C8). An absent lease ref on a root whose README's `**Build status:**`
  line reads a token in `tree_lib`'s `TERMINAL` at the advertised tip is a closed root: `--for draw` creates
  the hold at epoch 1, parentless, and S2's push leaves the tombstone that root never had, so its first draw
  mints it. An absent ref on a slug with no README refuses `no-root`, exit 2; on a live README it answers
  `contention`. Observed by AC7.
- **S6** — `release-retry`. `CAUSES` in `tools/loop/budget.py` gains `release-retry`. Each retry in
  `run_release_promote` (`tools/integrations/release.py`, DEPL-dShippedRelease-15 S8), the first and each
  the owner's "retry again" orders, first draws
  `python budget.py draw --build <the landing's build> --cause release-retry --item item.release.promote`,
  the landed SHA's build read from `read_landing`, whatever the failed attempt's cause. `exhausted` skips
  the retry and raises that function's owner item. Observed by AC8.
- **S7** — One red, one patch. `derive_patch_slug(key, origin_slug)` gives
  `<the origin's node letter>Patch<key>`, a legal `SLUG_RE` slug holding the 12-hex key `derive_red_key`
  gives, so two nodes filing one red name one slug. `placement.py record` (TOOL-dPlacedRequest-4 S7) takes
  it for a patch whose intake carries that key, and the create of `refs/gov/claims/<slug>` is the fence. A
  filer that loses the create and reads the same `content-key` in the claim body prints
  `patch — already filed · <slug>`, exit 0, and draws nothing, whichever origin filed: a landing, or a
  Maintain patch whose offender is a landed SHA, filed `--origin cadence` under the same key. dRankedPlan's
  `plan.dedupe`, which would otherwise catch it, is outside this build's closure. Observed by AC5.
- **S8** — The third answer. `KEEP_WAITING_LIMIT = 3` in `deploy_items.py`.
  `check_keep_waiting_limit(build, sha, root)` runs in `run_released_wake` straight after a `keep-waiting`
  answer is written, reading `measure_keep_waiting`. At the limit it writes `answer: parked`, closes the
  wait, posts `--mail ack` with the body `held · parked at the third keep-waiting answer`, and prints
  `released — <sha8> · parked`; the wait is not re-declared and no later ceiling opens an item. `--park` is
  not called, since it refuses a landed run. The owner ends a parked hold with
  `python deploy_items.py hold-close <build> <sha>`, through `check_terminal_proof` (TOOL-dDeclaredLoop-2
  S5), which writes `close-unreleased` and runs the walk. Observed by AC4.
- **S9** — The fixture and the page. `deploy_fixture.py` gains one `--case` per criterion, two clones of a
  bare remote racing through real subprocesses for AC2 and AC3. `help/deploy.md` gains a section on the
  shared budget: what draws, where the row lives, why a closed root's tombstone is taken and given back, and
  the third answer. Observed by AC1 to AC9; the page NOT OBSERVED by a criterion, read by the memory hygiene
  leg at the close.

## 3. Non-goals (OUT)

- No filing from `deploy.core`: DEPL-dShippedRelease-13 S8's. This unit fences what that filing can double.
- No `maintain.patch`: dTendedCadence holds no spec, and this unit gives it the key's rule and the same
  slug.
- No new policy key: "the third" is the clause's fixed word, not a value (§8 F1).
- No ending for a spent budget: `exhausted` is read by `flow.on-exhausted`, TOOL-dDeclaredLoop-31's.
- No tracked-file row for a draw on a root that has one on its lease: the tracked rows stay for a build
  drawing on itself, and the ask of §8 F5 aligns TOOL-dDeclaredLoop-30.
- No raising of a budget: the owner's alone (flow-steps:446).
- No lease verb for a live holder's own draw: a root's holder does not draw on behalf of a patch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — `read_landing`, the `patch-key` and the landed SHA's build
- **consumes-from** `DEPL-dShippedRelease-13` — `read_core_verdict` and `derive_red_key`, the verdict behind a filing and the key one red files one patch under
- **consumes-from** `DEPL-dShippedRelease-5` — `measure_keep_waiting`, the count the third answer reads, and `run_released_wake`, where the check sits
- **consumes-from** `DEPL-dShippedRelease-15` — `run_release_promote`, the retry site that draws `release-retry`
- **consumes-from** external — TOOL-dDeclaredLoop-30's `budget.py`, TOOL-dPlacedRequest-16's lease verbs and -21's claim body, TOOL-dWellOiledMachine-27's `intake.py`, each specced and unbuilt at base `f4597719`
- **hands-off** external — dTendedCadence's `maintain.patch`, which reads the same key and slug and has no spec to cite

## 4. Design

### Evidence

- TOOL-dDeclaredLoop-30 S3 commits a draw into a tracked transition record, so the row sits on the patch's
  branch until landing and a loser re-reading it sees the old count; its non-goal concedes "two racing draws
  are two rows". The clause's re-read needs a row the remote holds at once, and pin C8 puts it on the lease
  ref.
- TOOL-dPlacedRequest-16's draw is three pushes, acquire, draw and release. The clause says the draw and the
  release are one push, so S2 makes them one commit; the acquisition stays its own compare-and-swap, as the
  clause says.
- The remote holds `refs/gov/runs/*` and nothing else under `refs/gov/` while 147 build READMEs read CLOSED,
  measured by scout B at `f4597719` (PINNED): nearly every root has no tombstone today, which is S5.
- `verb_park` refuses a terminal run (`tools/unattended/unattended.sh:12872`, `refuse_if_terminal`), so S8
  cannot park through it.
- `SLUG_RE` is `^(?=.*[A-Z])[A-Za-z0-9]+$` (`tools/memory-tree/backlog.py:129`), which S7's slug meets.
- TOOL-dPlacedRequest-4's `patch` check requires the patched build to be terminal, and a landing-origin red
  files before its root closes: §8 F6's ask.

### The draw

| The root's lease, after one bounded fetch | Route | Answer |
|---|---|---|
| a `landed` or `withdrawn` tombstone | acquire `--for draw`, read, one push | `drawn`, or `exhausted` |
| a draw's `held` hold, live | retried up to `DRAW_ATTEMPTS`, the loser re-reading after it wins | as above, or `contention` |
| a draw's hold read stale | taken by TOOL-dPlacedRequest-16 S4, then as a tombstone | as above |
| live, under another holder | none | `contention`, exit 4 |
| absent, the root's README terminal | a parentless hold, then one push | `drawn`, and a tombstone minted |
| absent, the README live | none | `contention`, exit 4 |
| absent, no README | refused | `no-root`, exit 2 |

The record after a draw, status and epoch the tombstone's, the `draw` key its one addition:

```
gov-claim leases/<root>/build

status: landed
epoch: <n + 1>
renews: no
draw: draw · patch:dPatch0a1b2c3d4e5f · item.entry.claim · 3/10
```

### Inventory

| Minted | Cell or kind |
|---|---|
| `resolve_budget_root`, `run_root_draw`, `read_root_budget`, `derive_patch_slug`, `check_keep_waiting_limit` | `py.function`, `deploy_items.py`, OK from `lexicon.py --suggest` or put to it in the build pass |
| `DRAW_ATTEMPTS`, `KEEP_WAITING_LIMIT` | `py.constant` |
| `release-retry` | a member of `CAUSES` |
| `--lease draw` | a sub-verb of `--lease` |
| `hold-close` | a `deploy_items.py` verb |
| `draw` | a lease record body key |

### Migration

None for records. A root's tracked draw rows count as before, and S3 adds the lease's. A root closed before
dPlacedRequest lands gains its tombstone at its first draw and never before.

### Rollout

Live at landing, since the clause is the bound. No patch has been raised by a landing yet, so the first draw
is the first use.

### Files touched (estimate)

- `tools/loop/deploy_items.py`, `tools/loop/deploy_fixture.py`
- `tools/loop/budget.py`: the root route, `CAUSES`, the lease rows in the reader
- `tools/loop/placement.py`: `derive_patch_slug` taken for a red's patch
- `tools/unattended/unattended.sh`: `--lease draw`, and `--for draw` over an absent ref
- `tools/integrations/release.py`: the `release-retry` draw in `run_release_promote`
- `help/deploy.md`

### Alternatives rejected

- **The row on a lander-carried default-branch commit.** It keeps TOOL-dDeclaredLoop-30's tracked home and
  needs the whole bar per draw, so two draws cannot serialise inside one lease hold. Rejected by the
  clause's "in one push".
- **A separate `refs/gov/` ledger per root.** It holds the row, and its write is not the release, so
  "appends the draw and releases the lease terminal again in one push" fails. Pin C8 chose the lease ref.
- **A key for "the third".** The clause fixes the number, and v2's `[policies]` holds no such row. A key
  would add a surface the clause does not name, with one legal value.
- **Filing to a holder's mailbox for a live root.** Rejected as a second channel for a case `contention`
  already answers; the risk is in §5.

## 5. Production-readiness checklist

- security: the door (TOOL-dWellOiledMachine-58 S4 (a)) admits S2's tombstone because the tip names the
  writer, the draw's own hold. `hold-close` needs the owner's terminal proof.
- perf / scale: one acquisition, one read and one push per draw; a loser pauses 10 seconds at most.
- error / empty / loading states: `contention` and `exhausted` are answers, a dead fetch is a refusal, and
  an empty chain reads spent 0.
- observability: `budget.py state`, and the `draw` key on the lease chain.
- risks: under `whole-close`, a red landing's root stays live until the owner answers, so its patch reads
  `contention` meanwhile, since `release.pick` requires a green verdict. The owner item at the ceiling is
  what moves it. A killed draw's hold stops other draws until TOOL-dPlacedRequest-17 reads it stale.
- testing: real concurrency on two clones of a bare remote.
- migration: S5 is the only change a pre-lease root sees.
- user docs: S9.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case patch-chain` plants a root, a patch of it and a patch of
  that patch, `resolve_budget_root` prints the root for all three, each patch's draw lands on the root's
  lease, the middle build's own budget stays 0, and `python budget.py state --build <root>` prints spent 2.
  Red when: a patch of a patch draws on the middle build.
- **AC2** — When `--case concurrent-draws` races two clones on one closed root whose budget admits one, one
  prints `drawn` and the other `exhausted`, the lease chain holds one `draw` key, and the ref reads a
  tombstone after.
  Red when: both land, which is a read before the acquisition.
  fixture: two clones of a bare remote under `%TEMP%` with short names.
- **AC3** — When `--case old-tombstone` races two draws on a root closed longer ago than
  `leases.queued-claim-days`, planted at `0` in `.governance/policy.toml`, with a budget admitting both,
  each prints `drawn`, neither is refused, and `unattended.sh --lease prune` then prints
  `prune refused — tombstone` for that ref.
  Red when: an aged tombstone refuses a draw, or the ref is pruned.
- **AC4** — When `--case keep-waiting-third` plants an owner answering `keep-waiting` three times, the first
  two re-declare the wait, the third prints `released — <sha8> · parked`, the hold's chain ends
  `answer: parked`, no fourth item opens past a planted ceiling, and
  `python deploy_items.py hold-close <build> <sha>` with no terminal exits 2.
  Red when: the third answer re-arms the wait.
- **AC5** — When `--case double-filing` files one red twice from one node and once from a second clone, and
  once `--origin cadence` under the same key, one claim ref exists at `derive_patch_slug`'s slug, each later
  filer prints `patch — already filed`, and the root's chain holds one `patch:<slug>` draw.
  Red when: one red opens two patch builds.
- **AC6** — When `--case root-live` draws on a root whose lease another holder keeps live, it prints
  `contention`, exits 4 and the lease tip does not move; after that holder's `--deploy unlease`, the same
  draw prints `drawn`.
  Red when: a live root's lease is written, or the draw is refused for good.
- **AC7** — When `--case pre-lease-root` draws on a planted closed root with no lease ref, the draw prints
  `drawn`, the ref reads `status: landed` at epoch 1 with one `draw` key, and `--case no-root` on a slug
  with no README exits 2 naming `no-root`.
  Red when: a root with no tombstone refuses, or an unknown slug mints a lease.
- **AC8** — When `--case release-retry` drives a planted failing `run_release_promote` under a budget of 1,
  the retry writes one `release-retry` draw, and the owner's "retry again" reads `exhausted` and raises the
  item with no attempt; `python budget.py draw --cause no-such` still refuses.
  Red when: a release retry draws nothing, or the closed set opens.
- **AC9** — When `--case draw-epoch` reads the lease before and after one draw, the tombstone's `epoch` rose
  by one, the status reads `landed`, and the commit carrying the `draw` key is the one that wrote `landed`.
  Red when: the draw and the release are two pushes, or the epoch does not move.

## 7. Gates

`unattended kit gate` · `policy check`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · each `--case` above, the failing case `concurrent-draws` with the budget read moved before the acquisition · none

## 8. Open questions

- **F1 — Is "the third" a constant or a key, and does a silent owner count?** Options: (a) the constant 3, a
  decided answer counted; (b) a new key; (c) only a person's answers count. (b) adds a row v2 lacks for a
  value the clause fixes; (c) lets a silent owner wait forever, against P39. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 1, scout B F9, the clause's "the third". widens: none · relaxes: none
- **F2 — What does a third answer park, given `--park` refuses a landed run?** Options: (a) a `parked`
  answer on the hold's chain, the item held, and an owner verb to end it; (b) extending `verb_park` to
  terminal runs. (b) writes a tracked run-state file after landing, the commit pin C3 confines to one
  records landing. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Where does a draw on a live root go?** Disagreement 6. Options: (a) `contention`, retried; (b) the
  holder draws for the patch; (c) the row posted to the root's mailbox. (b) needs the holder to be alive and
  looking, and (c) is a second store. RESOLVED (agent, 2026-10-30, delegated): (a), rung 1,
  TOOL-dDeclaredLoop-30 S5 names this case. widens: none · relaxes: none
- **F4 — Does a release retry draw when the failure was an unreachable remote?** TOOL-dDeclaredLoop-30 S5
  reads an unreachable remote as contention, and the clause says "each release retry". RESOLVED (agent,
  2026-10-30, delegated): each retry draws, rung 1, the clause's word over that spec's general rule, S6
  scoping it to `release-retry` alone. widens: none · relaxes: none
- **F5 — An ask for dDeclaredLoop.** TOOL-dDeclaredLoop-30's S3 and S7 put a patch's row on a tracked
  transition record, and S3's closed set lacks a release retry. Ask, target dDeclaredLoop: accept S7 says a
  patch's draw lands on the root's lease ref as DEPL-dShippedRelease-30 S2 writes it, S3's set admits
  `release-retry`, and S7's originating slug is the root `resolve_budget_root` walks to, seen as
  `budget.py --fixture` green with those three. RESOLVED (agent, 2026-10-30, delegated): the ask stands,
  filed by the main loop, pin C8. widens: none · relaxes: none
- **F6 — An ask for dPlacedRequest.** TOOL-dPlacedRequest-16 S4 shows the draw as three pushes and defines
  `--for draw` over a tombstone or a hold only, and TOOL-dPlacedRequest-4's `patch` check requires a
  terminal build. Ask, target dPlacedRequest: accept `--lease draw` appends and releases in one commit,
  `--for draw` over an absent ref on a closed root creates the hold, and a `patch` placement from a
  `landing` intake admits a root not yet terminal, each seen on a fixture. RESOLVED (agent, 2026-10-30,
  delegated): the ask stands, filed by the main loop, pin C8. widens: none · relaxes: none
- **F7 — "Always finding the root's tombstone", when most roots have none.** Options: (a) the first draw
  mints it; (b) a backfill of tombstones; (c) an absent ref reads as an empty budget. (b) is a mass write to
  the remote, and (c) refuses a patch on every old build. RESOLVED (agent, 2026-10-30, delegated): (a), rung
  1, pin C8; the difference is deviation 301. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, the spec run.

## 10. Reuse audit

The seams extended: `budget.py`'s `record_draw` and reader (TOOL-dDeclaredLoop-30),
`--lease acquire --for draw` (TOOL-dPlacedRequest-16 S4) and `read_claim_body` (TOOL-dPlacedRequest-21), all
unbuilt at this base, with `derive_red_key` from DEPL-dShippedRelease-13.
`python tools/codebase-map/reuse_lookup.py "a patch build drawing on the root build's rework budget under its terminal lease"`
ranked name-stem hits only (`build`, `repo_root`, `build_commit`), and no budget code exists at HEAD, so
scout B's row is the seam record. Its name for the count, `count_keep_waiting`, is now
`measure_keep_waiting`, and its claim that this unit owns the count moved to DEPL-dShippedRelease-5, as
shared interface I14 says. Scout B's `gen_build_index.py:1212` cite for `parents:` holds at source.

Recall terms used: patch-build rework-budget root tombstone draw terminal-lease origin-slug epoch
compare-and-swap keep-waiting
