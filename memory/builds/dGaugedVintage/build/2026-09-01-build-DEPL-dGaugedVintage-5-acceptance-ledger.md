**Serves:** journal DEPL-dGaugedVintage-5

# Acceptance ledger — DEPL-dGaugedVintage-5, the missing markers

**Evidences:** DEPL-dGaugedVintage-5

- AC1 — `python tools/govkit/govkit.py selfcheck` — exits 0. Every versioned entry now carries at
  least one `gov:kit <entry-id>@` marker in its own derived set, or is exempt by declaration.
- AC2 — `git grep -l "gov:kit <entry-id>@"` — returns exactly one file per entry:
  `tools/check-wiring.sh`, `skills/session-kickoff/manifest-check.sh`,
  `tools/playbook/render_playbook.py`, `tools/codebase-map/map_lib.py` and
  `tools/workflows/tier2-review.js`. Before this unit the first four returned nothing.
- AC3 — `python tools/govkit/govkit.py selfcheck` — with the `check-wiring` marker deleted the run
  reds naming that entry. NOTE: that arm reverted the marker itself, because
  `git checkout -- <path>` restores the WHOLE file and the marker was unstaged — the repo's own
  `checkout-restores-the-whole-file` gotcha, hit here and recovered by re-adding and staging.
- AC4 — `python tools/govkit/govkit.py selfcheck` — `playbook` is reported exempt by its own
  declared `version_from.kind = "marker"`, with the reason, rather than omitted.
- AC5 — amended rev-3 — `codebase-map` took the same marker mechanism as the other four rather than
  a separate generated-artifact declaration. S4 was not built. Logged in §9.
- AC6 — `python tools/govkit/govkit.py selfcheck` — with `kind = "marker"` deleted from
  `tools/govkit/entries/playbook.kit.toml`, the run reds for `playbook`. The exemption is consumed
  from the declaration, not special-cased by id.
- AC7 — `git grep -l "gov:kit review-harness@"` — returns `tools/workflows/tier2-review.js`. Its
  pre-existing `gov:kit tier2-review@1.4` was left in place, since other things may grep it.

## What this ledger does not claim

The marker asserts a version is READABLE, not that it is correct for an adopter's bytes. And check
5c's population still excludes rendered destinations — see `DEPL-dGaugedVintage-4`'s AC6.
