# Brief — dRenderedAnchor: the closing review's round-3 findings on unit 3

**Serves:** research TOOL-dRenderedAnchor-4

## The brief

### Goal
Close every confirmed finding of the closing diff review's round 3, which read unit 3, as one batch unit: the harness branch of the C4 split in `roles_lib.resolve_cited_paths` gets a check that can fail, and every carrier of the citation rule states the predicate that ships.

### Items
1. M1 — one floored assertion in `tools/roles/adopt-roles.test.sh` (in arm 14 or a new arm 17), `FLOOR_ASSERTIONS` raised by its count: a prefixed kit built by `build_fixture`, each `HARNESS_PAIRS_READ` pair written only at `$FX/<home>/<file>`, no receipt and nothing under `tools/<home>/`; after `--scaffold` the Skill names each pair as the backticked `<home>/<file>` and never `tools/<home>/<file>`, and `roles.json` names the same path.
2. L1 — `help/roles.md`, `tools/roles/README.md` and the `tools/roles/adopt-roles.sh` header state that a repository-root file never answers a non-harness citation only at a prefixed install.
3. L2 — the same three carriers and the `resolve_cited_paths` docstring in `tools/roles/roles_lib.py` say "a `workflow`-driver harness of the workflow table", since the table's merge bar is a `program`-driver harness.

### Acceptance
Each item's fix as the round-3 review record states it. Item 1's assertion observed RED with `roles_lib.py`'s branch staged as `here = kit`, then GREEN on the shipped line. `grep -n 'harness of the workflow table'` over the four carriers prints no line lacking "`workflow`-driver".

### Gates
The unit's spec §7 derives them; at least roles adopter self-test · roles render wiring · roles catalogue · memory hygiene; then the full bar.

### Non-goals
Everything unit 3's spec §3 rules out, including `resolve_harness_path` and `resolve_kit_dir`'s probe order. No change to `resolve_cited_paths`' behaviour.

### Limitations
Scratch fixtures only under the system temp root. Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
The review record names each fix and the skeptic's verdict: `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-3-closing-diff-round3.md`. `build_fixture` and `HARNESS_PAIRS_READ` in `tools/roles/adopt-roles.test.sh` build the fixture.

## Drawn from the session

> **Fix (judged SOUND by the skeptic):**
— agent, closing review round 3, M1

## Owner confirmation

Asked: none — M4 promotes every medium and low at the exit by the owner's 2026-10-04 ruling, and the owner's go on this build stands.
Answer: none
