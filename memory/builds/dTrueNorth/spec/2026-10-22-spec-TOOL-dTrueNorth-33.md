# TOOL-dTrueNorth-33 — the two legs the close's bar redded: a fixture remote named through one constant, and the manifest re-stamped past the merge

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-33-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-33-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-33-deviation-41.md](../build/2026-10-22-build-TOOL-dTrueNorth-33-deviation-41.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-33-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-33-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-33-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-33-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-33-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-33-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`unattended.sh --close dTrueNorth` on the prepared merge blocks on `gates-green`, with 2 of 71 legs
red and both of them caused by this build. `remote literals (kit code names no remote)` names six lines
of `tools/memory-tree/deviation_join.py`: the fixture remote TOOL-dTrueNorth-31 S8 added, and its arms'
expectations. `kickoff-manifest ratchet` fails check 5, because three watched files changed after
`last-audit` and no later commit re-stamped it. This unit turns both legs green at their cause, and it
does not loosen either gate. Every line cited below was read at `850d13eb7`.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/deviation_join.py` names the fixture's remote through one module-level
  constant, `FIXTURE_REMOTE`. The remote add, the tracking ref and both arms' expected `ref` are built
  from it, and so are the docstring and arm messages that describe it. Each arm still asserts what it
  asserted, as §4 shows. Observed by AC1. The `routed-commits selftest` leg in §7 runs both arms and
  re-observes that they hold.
- **S2** — `memory/guides/SESSION-KICKOFF.md`'s §B claims fed by the three watched files are re-checked
  and any stale one is updated. `last-audit` is then re-stamped under the manifest's own stamp rule, and
  the pass commit's message carries the delta line in the house shape §4 gives. Observed by AC2.

## 3. Non-goals (OUT)

- Any other leg, the flagged bar, and any other spec.
- A line marker, a waiver, or a change to the population or predicates of `tools/check-remote-literals.sh`.
- The template remote at `tools/memory-tree/deviation_join.py:1600`, which belongs to TOOL-dTrueNorth-32
  AC7's arm. It is not the fixture's remote and it matches no shape the gate reads.
- A shared fixture-remote helper across the memory-tree kit's self-tests. Each self-test owns its fixture.

### Edges

- **consumes-from** external — the CLOSED unit whose fixture this edits, TOOL-dTrueNorth-31 (its S8
  helper and two AC8 arms). A frozen spec cannot write the mirroring hands-off line, so the unit is named
  here in prose.

## 4. Design

### The fixture remote (S1)

The gate is a pure ban with no marker. A fixture that needs a remote must name it through a variable
(`tools/check-remote-literals.sh:14-15`). Shape 4 (`:104`) also reds a variable assigned the quoted
name, so the constant holds a different name. `tools/memory-tree/migrate_backlog.py:2769` sets the
precedent in the same kit: `FX_REMOTE = "upstream"`, with every ref built from it at `:2927-2929`.

- Declare `FIXTURE_REMOTE = "upstream"` in the fixture block at `tools/memory-tree/deviation_join.py:829-835`.
- `add_fixture_remote` (`:1270-1277`) passes `FIXTURE_REMOTE` to `remote add`, and it builds the
  `update-ref` target as `f"refs/remotes/{FIXTURE_REMOTE}/main"`. Its docstring and its error text name
  the remote through the constant or in plain words.
- The AC8 arm at `:1579-1587` and the AC8 arm at `:1662-1677` compare `ref` to `f"{FIXTURE_REMOTE}/main"`,
  and their message strings interpolate the constant. The comments at `:1580` and `:1591` describe that
  ref, so they are reworded to match.

The arms keep their meaning because of how the ladder works. It takes the only remote whatever its name
(`tools/lib/resolve_remote.py:51-52`), and with no `refs/remotes/<remote>/HEAD` its branch is empty
(`:61-67`). So `read_decision_ref` answers `<remote>/main` (`tools/memory-tree/deviation_join.py:676-689`)
for this name exactly as it did for the old one. The arms still red against a remote half that joins
a wrong ref or reads no rows. They now also red against a join that reads a hard-coded `origin/main`.

### The manifest re-stamp (S2)

Two commits touch the watch set since the stamp `c01f0f86e`. The first is `92a0dcb96`, which changed a
`.memory-tree.conf` comment and re-stamped in that same commit with `delta none`. The second is the merge
`cbdf819b2`, which set memory-tree 2.151 at `memory/guides/BUILD-METHOD.md:1` and
`tools/memory-tree/check-memory-hygiene.sh:68`. Check 5 (`skills/session-kickoff/manifest-check.sh:1461-1478`)
reds because the newest watch-touching commit, the merge, is not an ancestor of the newest stamp change.

No §B bullet front-loads a kit version or that conf comment. The BUILD-METHOD pointer
(`memory/guides/SESSION-KICKOFF.md:49`) and the carries-join bullet (`:66`) both still hold, so this
reading finds no stale claim. The builder re-reads §B against the same diff before stamping.

- Re-stamp `last-audit` (`:5`) as `<ISO datetime with offset> @ <full 40-hex sha>`. The sha is `HEAD`
  at commit time and the datetime is later than the old one (stamp rule `:23`,
  `skills/session-kickoff/manifest-check.sh:1346`). The pass commit is the last commit of the unit that
  touches a watched file.
- `last-body-change` (`:8`) moves only if a §B bullet is edited. Check 9
  (`skills/session-kickoff/manifest-check.sh:1575-1578`)
  counted 2 watched non-merge commits since it at `850d13eb7`, against a limit of 10 (PINNED, measured then).
- No memory-tree version bump is expected. Both epoch legs grade from the merge-base with the default
  branch, `271aa59d`, which carries 2.150, and `HEAD` already carries 2.151. UNVERIFIED by a run: this
  role may not run either leg.

The delta line, in the shape of `92a0dcb96`'s, with its count and shas re-derived at commit time:

```
manifest-audit: delta none · watch-commits-since-stamp: 2 (92a0dcb96: .memory-tree.conf's TOOL-dTrueNorth-1 comment, audited in that commit; cbdf819b2: the memory-tree 2.151 version line in BUILD-METHOD.md and check-memory-hygiene.sh; no command, flag or knob section B front-loads changed)
```

### Inventory

- `FIXTURE_REMOTE` — module constant in `tools/memory-tree/deviation_join.py`, graded by
  `lexicon naming predicates`.

### Files touched (estimate)

`tools/memory-tree/deviation_join.py`
`memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- Keep the conventional name, assembled from two literals the way the gate builds its own
  (`tools/check-remote-literals.sh:92`).
  Rejected for three reasons. The kit would rebuild at run time the literal the ban exists to keep out.
  The arms could not red a join that hard-codes that name. And the kit already has a precedent value.

## 5. Production-readiness checklist

- security — N/A — a self-test fixture's remote name and a manifest stamp; no write path and no surface.
- perf / scale — N/A — no git call is added.
- error / empty / loading states — `add_fixture_remote` keeps its raise on a failed git call.
- observability — two arm messages name the constant's value where they named the old literal.
- risks — an arm could keep its name and lose its claim. §4 shows the ladder answers the same shape.
- testing — AC1 and AC2 as probes; the `routed-commits selftest` leg runs both arms.
- migration — N/A — no adopter conf, record or data changes.
- user docs — N/A — no page under `help/` covers either file.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-remote-literals.sh` runs, it exits 0 and prints
  `remote-literals: clean`. `grep -n FIXTURE_REMOTE tools/memory-tree/deviation_join.py` lists the
  declaration, the two git calls in `add_fixture_remote` and the two arms' `ref` comparisons.
  Red when: any line of `tools/memory-tree/deviation_join.py` names the remote by literal. At
  `850d13eb7` lines 1272, 1273, 1276, 1584, 1586 and 1673 do, and the gate exits 1 naming them.
  figure: the six line numbers are PINNED, read by the close's bar at `850d13eb7`.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh` runs after the pass commit, it prints
  no line holding `MANIFEST check 5 FAILED`. The `last-audit:` line of
  `memory/guides/SESSION-KICKOFF.md` names a sha that has `cbdf819b2` as an ancestor.
  Red when: the stamp still names `c01f0f86e`, or any sha before the merge. Check 5 then names
  `.memory-tree.conf`, `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/check-memory-hygiene.sh`.
  fixture: check 5 reads committed history from the stamp to `HEAD`, so the observation is made on the
  pass commit and not on the staged tree.

## 7. Gates

`remote literals (kit code names no remote)` · `kickoff-manifest ratchet` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

`routed-commits selftest` runs the deviation join's fixture arms, both AC8 arms included. `recall floor`
and `recall floor arms` are owed by the `memory/` guard. `lexicon naming predicates` grades the new
constant. No arm is added or moved: the two arms are edited where they stand, so no `New arm:` line is
owed.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft: the fixture remote named through `FIXTURE_REMOTE`, and the kickoff
  manifest re-audited and re-stamped past the merge `cbdf819b2`, with deviation 41.

## 10. Reuse audit

The unit extends the deviation join's own fixture seam, which is the fixture constant block at
`tools/memory-tree/deviation_join.py:829-835` and `add_fixture_remote` at `:1270`. It takes the value
shape of `FX_REMOTE` (`tools/memory-tree/migrate_backlog.py:2769`), read at source.
`tools/codebase-map/reuse_lookup.py` ranked `build_fixture` and `Fixture` in this file and
`resolve_remote` in the gov lib dir. No candidate names a remote for a fixture, so no helper is minted. The manifest half re-stamps under the manifest's
own rule and builds nothing.

Recall terms used: `python tools/codebase-map/reuse_lookup.py fixture remote name constant update-ref "remote add" ladder resolve_remote GOV_REMOTE "decision ref" remote-literals`
