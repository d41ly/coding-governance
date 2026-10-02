# DEPL-aHalvedInstall-5 — every row refusal in `update` decides whether it holds its kit back

**Status:** CLOSED · rev-3 · 2026-10-02 · node a · Tier-2 · base cd90f7fa · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-build-DEPL-aHalvedInstall-5-1-acceptance-ledger.md](../build/2026-10-02-build-DEPL-aHalvedInstall-5-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

DEPL-aHalvedInstall-4 holds a kit back when its row is refused in the WRITE loop. Two other channels
refuse a kit's rows and were outside that set, which the closing review's round 1 found (H1, ids 1
and 4). The classification walk refuses a row before it ever enters the write loop. The landing loop,
which lands sources the receipt has never claimed, refuses into its own list after the held set was
final. A kit refused through either still landed its other rows. This unit routes both channels into
the held set, and makes "which refusals hold a kit" a decision every refusal site states, so a new
channel cannot reopen the class silently.

## 2. Scope (IN)

- **S1** — One helper, `_add_held(kit, path)`, local to `_cmd_update`, defined before the classification
  walk. The write loop's problem-count mechanism calls it, and so does every hold below. Observed by
  AC1, AC2 and AC4.
- **S2** — The classification walk's four row refusals hold their row's kit: an unknown role, an
  adopter-owned refusal, a schema-1 role mismatch and a refuse-role. Observed by AC1.
- **S3** — The landing loop records each refused destination's kit and source. After the loop, a
  refusal holds its kit when the source is NEW since the receipt's vintage — absent from gov's tree at
  the receipt's `gov_commit` and present at the vintage the run moves to — and no `[[decline]]` names
  that kit and destination. A refusal of a
  source the receipt's vintage already shipped is a standing state that recurs on every run, and
  holding on it would wedge the kit. Observed by AC2 and AC3.
- **S4** — The HELD BACK lines print after the landing loop, so a kit held there is announced.
  Observed by AC2.
- **S5** — The refusal region of `_cmd_update` is fenced by two marker comments. A selftest arm reads
  that region of `tools/govkit/govkit.py` and refuses any `r.fail(` or `_refused_new.append(` site
  outside the write loop's own counted span that neither calls `_add_held(` within the following lines nor
  carries a `# hold-exempt:` comment stating why it does not split a kit. Observed by AC4.

## 3. Non-goals (OUT)

- A refusal BEFORE the classification walk aborts the whole run (`raise Refusal`), and one AFTER the
  landing loop is not about a row. Neither is in the fenced region.
- Unit 4's rollback is reused unchanged.

### Edges

- **consumes-from** `DEPL-aHalvedInstall-4` — the held set, the declined regenerate and the forced
  rollback; this unit only widens what fills the set.

## 4. Design

### Evidence

Read at `5d1db895`. The classification walk's refusals sit before `acted.append`; the landing loop's
eight refusal reasons append to `_refused_new` and never call `r.fail`, so with no other finding the
receipt re-stamped at the new vintage. Its "already holds this path" refusal recurs on every run for
an adopter-occupied destination, which is why S3 is narrowed rather than holding on every entry.

### Data model

```python
_held: dict[str, list[str]] = {}
def _add_held(kit, path):
    if kit:
        _held.setdefault(kit, []).append(path)
# landing loop: _refused_new_from[_dest] = (_eid, _src0)
# after it, per refused (dest, why): hold when blob_at(root, base_commit, src) is None and
# (kit, dest) is not a [[decline]] row
```

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Holding on every landing refusal.** Rejected by round 1's skeptic: a standing refusal wedges the
  kit's updates permanently.
- **Re-deriving the decline state with `decline_findings`.** It grades and reports; the hold needs only
  the declared pair, which the deploy file states.

## 5. Production-readiness checklist

- security — no new write path; holds only narrow what lands.
- perf / scale — one `git show` per refused landing destination.
- error / empty / loading states — a refusal with no kit holds nothing, as before.
- observability — the HELD BACK line names every refused path per kit.
- risks — a kit whose new source the adopter occupies is held at every run until the adopter moves
  the file or declines it; the REFUSED line already names the path.
- testing — fixtures for each channel, and the structural arm observed red on an unmarked site.
- migration — none.
- user docs — the runbook's held-back paragraph names both channels.

## 6. Acceptance criteria

- **AC1** — When `update --write` runs over a fixture whose receipt carries a row with a role the
  dispatch refuses, alongside a changed clean row of the same kit, the clean row's bytes are restored
  and the output carries `HELD BACK`.
  Red when: the classification refusal does not call `_add_held`.
- **AC2** — When the new vintage adds a source whose destination the target already occupies, outside
  the receipt, and changes a sibling row, the sibling is restored, the operator's file stands and
  `HELD BACK` names the destination.
  Red when: the landing refusal is not routed to `_add_held`, or the print stays above the loop.
- **AC3** — When that occupied destination is named by a `[[decline]]` row, or its source already
  existed at the receipt's vintage, the sibling lands and no `HELD BACK` line names the kit.
  Red when: every landing refusal holds.
- **AC4** — When the structural arm reads the fenced region of `tools/govkit/govkit.py`, it finds no
  unmarked site; with one `# hold-exempt:` comment staged away, it names that site.
  Red when: the arm counts sites outside the fence, or matches nothing.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `recall floor arms` · `govkit acceptance matrix`

New arm: tools/govkit/selftest.py · an unmarked refusal site, and fixtures for both channels · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, promoted from the closing review's round 1 H1, carrying its
  skeptic's corrected fix.
- rev-2 · 2026-10-02 · build pass · S1 · AC2 · the helper is `_add_held`, a declared verb (the lexicon
  refused `hold`). The `REFUSED` lines print at the end of the run, below
  the HELD BACK line, so AC2 no longer orders them; it asserts the operator's file stands instead.
- rev-3 · 2026-10-02 · build pass · S3 · NEW also requires the source at the run's `--to` vintage.
  The landing loop resolves gov's current descriptor, so an update to an older vintage refuses
  sources absent there; absent-at-base alone held those, and the whole suite's `[-8]` arms redded.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record which kit a refused row belongs to and hold the kit back"`
ranked name-stem neighbours only (`kit_rel`, `records`, `CensusRefused`), none of which reads an
update refusal. The seams extended are unit 4's held set and forced rollback, the landing loop's own refusal list, the
`[[decline]]` rows the deploy file declares, and `blob_at`, which reads gov's tree at a commit. The
review record `2026-10-02-review-DEPL-aHalvedInstall-1-closing-diff-round1.md` is the source of the
narrowing in S3. No other seam reads a refusal's kit.

Recall terms used: govkit update conflict rollback regenerate rendered vintage stale partial install hole discharge absent key

The question passed with them: "why does govkit update leave a kit half-installed when one row conflicts, and why does a renderer change roll back a kit".
