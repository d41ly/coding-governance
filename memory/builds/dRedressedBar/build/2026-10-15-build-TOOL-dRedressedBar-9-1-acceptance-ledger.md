# TOOL-dRedressedBar-9 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-9

Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
builder recorded. Nothing was re-run for it. The unit was built against spec 9 rev-4 in the one
pass commit `59f11096a`. Spec 9's rev-5, rev-6 and rev-7 are records fixes that move no criterion,
so the readings answer the criteria as they stand. The readings are the builder's, from that
commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
under the heading `2026-10-14T14:39:35 · gov-builder · wf_df00997e-69f/aeeca0787c1024036` at line
4681. The probes ran on scratch targets under `%TEMP%/p9fx`. No merge bar, no self-test suite and
no gate leg ran in the build pass, and the section 7 legs were owed to the close.

**Evidences:** TOOL-dRedressedBar-9
- AC1 — `[[outcome]]` — the grep over `tools/govkit/entries/settings-merge.kit.toml` showed the one
  block: code 2, `must_exist` `{prefix}/settings-merge.py`, `must_not_exist`
  `{prefix}/hooks/agent-cap.js`, `means = "no-agent-cap-to-wire"` and `ok = true`. The diff of the
  four files that must not move was empty against `ebce889c`.
- AC2 — `no declared outcome accepts that` — before the block, on `a50d04eb`, the narrow update
  exited 1 with that line, and `gov_commit` stayed at `24f39915`. With the block it exited 0,
  printed `adopter exit 2 — no-agent-cap-to-wire` and `check-wiring.fragment.json wired`,
  re-stamped at HEAD, and the receipt claimed check-wiring, run-gates and settings-merge.
- AC3 — `[accepted stop]` — `apply --kits settings-merge` went from exit 1 to exit 0 with that
  mark, and no `settings.json` was created.
- AC4 — `must_not_exist` — the engine read the three exit-2 states as ACCEPTED, REFUSED and
  REFUSED. With `must_not_exist` dropped, held in memory and not written, the both-present state
  read ACCEPTED.
- AC5 — `missing` — the dirty-README shape and the committed-deletion shape both exited 0, and the
  deletion printed `missing`. The builder did not re-run them over the old descriptor, and wrote
  that the red half "was observed when the spec was written".
- AC6 — `agent-cap.js` — the full install still printed adopter exit 0 for both kits, never
  printed the stop, and wired `agent-cap.js`.
- AC7 — `check_outcome_states` — `symbols.json` lists it for `tools/govkit/matrix.py`, and
  `gen_map.py --check` exited 0. The return lists `matrix.py` and `symbols.json` among the pass
  commit's paths, and the commit body says `gen_map.py --write` run alone moved only
  `symbols.json`. The record names no reading of the `3d1adca9` map.
