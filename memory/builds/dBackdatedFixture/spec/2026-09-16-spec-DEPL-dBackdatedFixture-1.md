# DEPL-dBackdatedFixture-1 — the vintage fixtures model an install the old vintage could have produced

**Status:** OPEN · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams deployer

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/govkit/selftest.py` fails 30 arms at `4cf0944d`. The cause is in the suite, not in
`tools/govkit/govkit.py`. Two fixtures model "an install landed at an older gov vintage". They do it by
rewinding every row of a fresh `check-wiring` receipt to `24f39915`. `TOOL-aReplayedCard-2`
(`39df2b1a`, 2026-09-14) added `tools/check-wiring.fragment.json` to that kit, and that source did not
exist at `24f39915`. The fixtures therefore record the empty blob's id as its `gov_oid`. `update`'s S9
preamble (`DEPL-dCarriedReceipt-7`) refuses the whole receipt at exit 2, which is its designed
behaviour. Three `check` arms also type `2/2` for a figure that is now `3/3`. This unit makes the
fixtures model a state a real adopter can hold, and makes those counts derived rather than typed.

## 2. Scope (IN)

- **S1** — One module-level helper, `rewind_receipt`, replaces the two inline rewind loops in
  `stale_target` and `delta_target`. For each receipt row with a `source`:
  - if gov shipped that source at the vintage, the row's `commit`, `sha256` and `gov_oid` are rewritten
    from gov's blob there, and the target file gets those bytes;
  - if gov did not ship it, the row is removed from `install.json` and the path is removed from the
    target's index and worktree.

  A row with no `source` is left untouched, which is what `delta_target` already did. Observed by AC1
  and AC2.
- **S2** — The three `check` arms graded over the `u5a` fixture stop typing their figures. Each one
  re-derives its `integrity:`, `provenance:` and `sidecar:` figure from the target's own bytes, gov's
  blobs and `install.sums`, and asserts it is non-zero. Observed by AC3.
- **S3** — A fixture-acceptance arm: `update` run read-only over a rewound fixture exits 0, and the
  arm's detail carries stderr. A fixture `update` refuses then fails one arm that names the refusal. It
  no longer fails a spread of downstream arms whose detail shows only stdout. Observed by AC4.
- **S4** — Every one of the 30 arms red at `4cf0944d` passes again, with no arm weakened. Observed by
  AC5.

## 3. Non-goals (OUT)

- No change to `tools/govkit/govkit.py`. The S9 refusal is correct. `update --write` landing an
  unclaimed source (`TOOL-aScouredKit-25`) is ratified. §4 records the probe that showed both.
- No change to `GOVKIT_NO_REMOTE_PROBE` or to its arms. Its `UNVERIFIED` line is truthful. It was only
  the first stdout line of arms that failed for another reason.
- No rewrite of `install.sums` in the rewind. Neither fixture ever rewrote it, and `update` does.
- No sweep of every arm that passes only `p.stdout` as its detail. S3 closes this build's instance
  where the refusal first appears. A suite-wide rule is a separate unit if anyone wants one.

### Edges

- **consumes-from** external — `TOOL-aReplayedCard-2`'s descriptor change, which is correct and stays.

## 4. Design

### Data model

`rewind_receipt(govroot, target, vintage) -> (kept, dropped)` takes paths and returns two lists of
receipt `path` strings. It writes `install.json` with `indent=2` and no trailing newline, which is
byte-identical to both loops it replaces. It uses gov's `_sha` and `blob_oid` through
`govkit_module()`, the same helpers the replaced loops used, so the fixture and the engine agree on
what a blob is named. Whether gov shipped a source at the vintage is `git cat-file -e <vintage>:<source>`.

### Inventory

One new module-level function, `rewind_receipt`. One new arm label prefix, `[dBF]`.

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

A is chosen. It models what every adopter who installed `check-wiring` before 2026-09-14 holds. It also
puts `update`'s unclaimed-source landing path under the arms that already run. B passes, but it builds
a receipt no verb writes. C fixes this instance and breaks again the next time the kit gains a file.

## 5. Production-readiness checklist

- security — N/A — test fixtures inside a temp directory; no product write path changes.
- perf / scale — the rewind adds one `git cat-file -e` per row, three rows today; negligible against a
  suite measured at 6m42s on node d at `4cf0944d`.
- error / empty / loading states — an empty dropped set is the vacuous case, and AC2's liveness half
  reds on it rather than passing.
- observability — S3's arm puts stderr in the detail, which is the diagnostic this incident lacked.
- risks — AC2's liveness half reds if `check-wiring` ever stops shipping a file `24f39915` lacked. That
  is the `[-8]` fixture's existing "ASSERTED FIRST" precedent: a fixture that stops exercising its case
  says so.
- testing — the arms are the change; each new or rewritten arm is observed RED on a staged break (§7).
- migration — N/A — no receipt schema, data or adopter change.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `stale_target` builds a fixture, every receipt row carrying both `commit` and
  `gov_oid` names gov's own blob. The arm reads it independently with `git rev-parse <commit>:<source>`
  in the gov checkout. Red when: `rewind_receipt` gives an identity to a source the vintage did not
  ship, which a staged break of its drop branch reproduces.
- **AC2** — When the vintage did not ship a row's source, `rewind_receipt` removes the row from
  `install.json` and the path from the target's `git ls-files`. The dropped set equals the receipt
  rows whose source is absent from `git ls-tree -r --name-only 24f39915`, and it is non-empty.
  Red when: the drop branch is removed, or the fixture stops holding such a row.
  figure: DERIVED from `ls-tree` at observation time; non-empty is the only pinned fact.
- **AC3** — When `govkit.py check` runs over a clean `check-wiring` install, the printed `integrity:`,
  `provenance:` and `sidecar:` figures equal counts the arm derives from the target's files,
  `git rev-parse` in gov and `install.sums`, and each is non-zero. Red when: `check` stops counting a
  row, reproduced by a staged break in its engine-row loop.
  figure: DERIVED; no literal count remains in the three arms.
- **AC4** — When `govkit.py update` runs read-only over a `stale_target` fixture, it exits 0 and its
  stderr carries no `REFUSING`, with stdout and stderr both in the arm's detail. Red when: the fixture
  is one S9 refuses, reproduced by the same staged break as AC1.
- **AC5** — When the unit is built, all 30 labels listed failing at `4cf0944d` read `ok`, and the
  suite's closing line is `govkit-selftest: all arms held`. Red when: any of them still fails, or a
  label disappears.
  cost: one full suite run of about seven minutes, taken once at the main loop after the build.

## 7. Gates

`govkit selftest`

New arm: tools/govkit/selftest.py · `[dBF]` rewind arms, staged RED by making `rewind_receipt` rewind an absent source instead of dropping it · none
New arm: tools/govkit/selftest.py · the three `u5a` check-count arms, staged RED by skipping one engine row in `check`'s integrity loop · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, grounded against `4cf0944d` and the baseline run's 30 labels.

## 10. Reuse audit

Probe result: no existing seam fits. `reuse_lookup.py` over "rewind an installed target's receipt to
an older gov vintage in a self-test fixture" ranked nothing in `tools/govkit/selftest.py`, because the
two rewind loops are closures inside `main()`. The seam this unit extends is those two loops,
`stale_target` at `tools/govkit/selftest.py:615` and `delta_target` at `tools/govkit/selftest.py:3754`,
which become one helper at their second instance (template §12). Recall confirmed the S9 refusal is
`DEPL-dCarriedReceipt-7` and the unclaimed-source landing is `TOOL-aScouredKit-25`, both ratified.

Recall terms used: `--terms "gov_oid S9 receipt integrity refusal stale_target fixture older vintage
rewind blob_at selftest update"`, with the question "why does govkit update refuse a receipt row whose
gov_oid does not match gov's blob at its commit, and how do selftest fixtures backdate an install".
