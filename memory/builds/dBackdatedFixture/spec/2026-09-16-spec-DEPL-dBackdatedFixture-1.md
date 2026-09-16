# DEPL-dBackdatedFixture-1 — the vintage fixtures model an install the old vintage could have produced

**Status:** INPROGRESS · rev-3 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-review-DEPL-dBackdatedFixture-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-dBackdatedFixture-1-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/govkit/selftest.py` fails 30 arms at `4cf0944d`. The cause is in the suite, not in
`tools/govkit/govkit.py`. Two fixtures model "an install landed at an older gov vintage". They do it by
rewinding every row of a fresh `check-wiring` receipt to `24f39915`. `TOOL-aReplayedCard-2`
(`39df2b1a`, 2026-09-14) added `tools/check-wiring.fragment.json` to that kit, and that source did not
exist at `24f39915`. The fixtures therefore record the empty blob's id as its `gov_oid`. `update`'s S9
preamble (`DEPL-dCarriedReceipt-7`) refuses the whole receipt at exit 2, which is its designed
behaviour. This unit makes the two fixtures model a state a real adopter can hold. Three further
labels are `check` arms that type `2/2`; they are `DEPL-dBackdatedFixture-3`.

## 2. Scope (IN)

- **S1** — One module-level helper, `write_vintage_receipt`, replaces the two inline rewind loops in
  `stale_target` and `delta_target`. For each receipt row with a `source`:
  - if gov shipped that source at the vintage, the row's `commit`, `sha256` and `gov_oid` are rewritten
    from gov's blob there, and the target file gets those bytes;
  - if gov did not ship it, the row is removed from `install.json` and the path is removed from the
    target's index and worktree.

  Observed by AC1 and AC2.
- **S2** — One fixture-acceptance arm per fixture builder, emitted before that builder's first consumer
  arm. It runs `update` read-only over a fresh fixture and asserts exit 0 with no `REFUSING`, and its
  detail carries stderr. It ADDS a FAIL line that names the refusal. It does not stop or silence the
  consumer arms that fail after it. Observed by AC3.
- **S3** — The 27 labels among the 30 that are built over `stale_target` or `delta_target` pass again.
  No arm is weakened: the ones whose population S1 widens are named in §4 with the reason each still
  grades its target, and the one that would not is `DEPL-dBackdatedFixture-2`. Observed by AC4.
- **S4** — A row with no `source` is left untouched by `write_vintage_receipt`, which is what
  `delta_target` already did. NOT OBSERVED: every row writer in `govkit.py` sets `source`, so no fixture
  holds such a row and no arm can see the branch.

## 3. Non-goals (OUT)

- No change to `tools/govkit/govkit.py`. The S9 refusal is correct. `update --write` landing a source
  the receipt never named is DEPL-dRatifiedSeam-1 S3, landed at `3fe56d56`. §4 records the probe that
  showed both.
- No change to `GOVKIT_NO_REMOTE_PROBE` or to its arms. Its `UNVERIFIED` line is truthful. It was only
  the first stdout line of arms that failed for another reason.
- No rewrite of `install.sums` in the rewind. Neither fixture ever rewrote it, and `update` does.
- No sweep of every arm that passes only `p.stdout` as its detail, and no mechanism that skips consumer
  arms after a refused fixture. S2 adds one diagnosable line; a suite-wide rule is a separate unit.
- No edit to backlog row `TOOL-aFlaggedScaffold-3`, which is still OPEN and claims `update` cannot land
  a new source. `3fe56d56` contradicts it. The reconciliation is parked in the README.

### Edges

- **hands-off** `DEPL-dBackdatedFixture-2` — the `[dGV-9]` arms, whose population this unit's landed row widens.
- **hands-off** `DEPL-dBackdatedFixture-3` — the three `u5a` check-count labels, and the suite's closing line.
- **consumes-from** external — `TOOL-aReplayedCard-2`'s descriptor change, which is correct and stays.

## 4. Design

### Data model

`write_vintage_receipt(govroot, target, vintage) -> (kept, dropped)` takes paths and returns two lists
of receipt `path` strings. It writes `install.json` with `indent=2` and no trailing newline, which is
byte-identical to both loops it replaces. It uses gov's `_sha` and `blob_oid` through `govkit_module()`,
the same helpers the replaced loops used, so the fixture and the engine agree on what a blob is named.
Whether gov shipped a source at the vintage is `git cat-file -e <vintage>:<source>`.

The arms never read the helper's return value. AC1 and AC2 derive their expectation independently: the
descriptor's writes through `resolve_entry`, split by `git ls-tree -r --name-only` at the vintage.

### Inventory

One new module-level function, `write_vintage_receipt`. `--suggest` answers OK for cell `py.function`.
One new arm label prefix, `[dBF]`. Existing arm labels are unchanged.

### Arms whose population S1 widens

Under S1, `update --write` over a `stale_target` fixture lands `tools/check-wiring.fragment.json` as a
new `current` row. An arm reading the receipt or stdout after such a write sees one more row.

| Arm | Still grades its target because |
|---|---|
| `[dGV-9]`, three arms | it would not; `DEPL-dBackdatedFixture-2` scopes it to the rows held before the write |
| u2a "a second update over the same target reports current" | `check-wiring.test.sh` already supplied a `current` row before 2026-09-14, and `stale` absent still grades the refreshed rows |
| `[-12]` AC9 "a COMMITTED deletion … reaches `missing`" | the landing prints `landed`, never `missing`, and its sibling arm checks the restored file by path |
| `[-8]` AC3 "provenance: 2/2 resolved" | `--to 372e6b2a` REFUSES the fragment, so the population is frozen at two rows; the literal is pinned to that historic vintage |

### Files touched (estimate)

`tools/govkit/selftest.py` only. About 60 lines added and 25 removed.

### Alternatives rejected

Each candidate was tested before choosing, with the probe script driving the real `update` over a
`check-wiring` install at `24f39915` (M12).

| Candidate | Would lose if | Observed |
|---|---|---|
| A. drop rows the vintage did not ship | `update` refused the fixture, or an arm's text stopped matching | read-only `stale 2` and `NOTHING was written`, rc 0; `--write` rc 0 and `landed tools/check-wiring.fragment.json`; second run `current 3` |
| B. leave such rows at the pin's vintage | the mixed-vintage receipt were refused | not refused; `current 1 · stale 2`, then `current 3` |
| C. choose a newer fixed vintage | no commit shipped every current source with different `check-wiring.sh` bytes | one exists today (`39df2b1a`) |

A is chosen. It models what every adopter who installed `check-wiring` before 2026-09-14 holds. B passes,
but it builds a receipt no verb writes. C fixes this instance and breaks again the next time the kit
gains a file. A's cost is the widened populations in the table above. A second probe ran A over
`delta_target`'s shape: `update --to 372e6b2a --write` exited 0 with `diverged` and `stale`, and `check`
then printed `provenance: 2/2 resolved`.

## 5. Production-readiness checklist

- security — N/A — test fixtures inside a temp directory; no product write path changes.
- perf / scale — the rewind adds one `git cat-file -e` per row, and S2 adds two fixtures with one
  read-only `update` each; small against a suite measured at 6m42s on node d at `4cf0944d`.
- error / empty / loading states — AC1 and AC2 each carry a non-zero floor, so an empty population reds
  rather than passing.
- observability — S2's arms put stderr in the detail, which is the diagnostic this incident lacked.
- risks — AC2's liveness half reds if `check-wiring` ever stops shipping a file `24f39915` lacked. That
  is the `[-8]` fixture's "ASSERTED FIRST" precedent.
- testing — every new arm is observed RED on a staged break named in §7.
- migration — N/A — no receipt schema, data or adopter change.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `stale_target` builds a fixture, every receipt row carrying both `commit` and
  `gov_oid` names gov's own blob, read independently with `git rev-parse <commit>:<source>` in the gov
  checkout, and at least one such row exists.
  Red when: `write_vintage_receipt` gives an identity to a source the vintage did not ship.
- **AC2** — When the vintage did not ship a row's source, the row is absent from `install.json` and the
  path from the target's `git ls-files`. The expected dropped set is the descriptor's writes whose
  source is absent from `git ls-tree -r --name-only 24f39915`, the receipt holds exactly the rest, and
  the dropped set is non-empty.
  Red when: the drop branch is removed, or the fixture stops holding such a row.
  figure: DERIVED from `resolve_entry` and `ls-tree` at observation time; non-empty is the only pin.
- **AC3** — When `govkit.py update` runs read-only over a fresh `stale_target` fixture and over a
  fresh `delta_target` fixture, each exits 0 with no `REFUSING` on stderr. Both arms carry stdout and
  stderr in their detail, and each is emitted before its builder's first consumer arm.
  Red when: either builder produces a fixture S9 refuses.
- **AC4** — When the unit is built, the 27 of the 30 labels listed failing at `4cf0944d` that are not
  `u5a` check arms read `ok` in the suite output, each line opening `ok   `.
  Red when: any of them still fails, or a label disappears.
  cost: one full suite run of about seven minutes, taken once at the main loop after the build.

## 7. Gates

`govkit selftest` · `lexicon naming predicates`

New arm: tools/govkit/selftest.py · `[dBF]` AC1 and AC2 arms, staged RED by making `write_vintage_receipt` rewind an absent source instead of dropping it · none
New arm: tools/govkit/selftest.py · `[dBF]` AC3 acceptance arms, staged RED by that same break · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, grounded against `4cf0944d` and the baseline run's 30 labels.
- rev-2 · 2026-09-16 · §2 S2 S3 S4 S5 S6 · §3 · §4 · §5 · §6 AC2 AC3 AC4 AC5 AC6 · §7 · folded spec audit
  round 1 (BLOCKED, 14 confirmed of 31). B1: `[dGV-9]` scoped to pre-write rows with a liveness arm,
  new S4 and AC5. H1: `check` counts come from the descriptor, not the receipt. M1: one staged break per
  figure, plus a receipt-shrink break. M2: S3 reworded to what is built, covering both builders. M3: the
  landing is cited as DEPL-dRatifiedSeam-1 S3 at `3fe56d56`. M4: helper renamed `write_vintage_receipt`
  and `lexicon naming predicates` added to §7. L1: the source-less clause is S6, NOT OBSERVED.
- rev-3 · 2026-09-16 · §1 · §2 · §3 Edges · §4 · §5 · §6 · §7 · the round-1 disposition by severity
  (BUILD-METHOD M4, `REVIEW_ROUNDS` 1, exit BOUNDED). The BLOCKER B1 and the HIGH H1 are PROMOTED rather
  than folded: rev-2's S4/AC5 move to `DEPL-dBackdatedFixture-2` and its S2/AC3 to
  `DEPL-dBackdatedFixture-3`, each audited as a spec. The remaining items renumber S1-S4 and AC1-AC4.
  The medium and low folds stay as rev-2 wrote them.

## 10. Reuse audit

Probe result: no existing seam fits. `reuse_lookup.py` over "rewind an installed target's receipt to
an older gov vintage in a self-test fixture" ranked nothing in `tools/govkit/selftest.py`, because the
two rewind loops are closures inside `main()`. The seam this unit extends is those two loops,
`stale_target` at `tools/govkit/selftest.py:615` and `delta_target` at `tools/govkit/selftest.py:3751`,
which become one helper at their second instance (template §12).

Recall disagreed with the source once, and the source wins. The query returned `TOOL-aScouredKit-25`
and `TOOL-aFlaggedScaffold-3`, which both say `update` cannot land a source gov started shipping. The
first is CLOSED as a duplicate and the second is still OPEN. DEPL-dRatifiedSeam-1 S3 at `3fe56d56` built
that landing, and §4's probe observed it. The S9 refusal is `DEPL-dCarriedReceipt-7`, confirmed at
`govkit.py:6090`.

Recall terms used: `--terms "gov_oid S9 receipt integrity refusal stale_target fixture older vintage
rewind blob_at selftest update"`, with the question "why does govkit update refuse a receipt row whose
gov_oid does not match gov's blob at its commit, and how do selftest fixtures backdate an install".
