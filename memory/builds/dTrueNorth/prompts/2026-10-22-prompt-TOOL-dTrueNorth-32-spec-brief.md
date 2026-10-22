**Serves:** research TOOL-dTrueNorth-32

# Spec brief — TOOL-dTrueNorth-32, the round-3 closing review's findings and one hygiene red

## The prompt

> The round-3 closing diff review over `ef8fd59d0...2057f2272`, TOOL-dTrueNorth-31's diff, reads CLEAN WITH FIXES: 0 blockers, 0 highs, 16 confirmed findings in 14 items, M1 to M6 and L1 to L8. Its record is `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-31-closing-diff-review-round3.md`. Beside it, `tools/memory-tree/check-memory-hygiene.test.sh` at `3c4271e8f` reds one arm unit 31 caused: `.memory-tree.conf.example does not declare GIT_CONFIG_GLOBAL, which a module in tools/memory-tree reads out of a dict`, from `asbuilt_view.py`'s `check_node_merge_arm` reading `os.environ.get("GIT_CONFIG_GLOBAL")`. Under M4 every confirmed finding is promoted to a unit of this build.

## The brief

### Goal
Author TOOL-dTrueNorth-32, one Tier-2 unit whose pass fixes each of the fourteen items and the hygiene red at its cause, taking the fix the review's skeptic judged sound (for findings 6, 11, 13 and 16 the skeptic's corrected fix). Where a round-2 fix proved incomplete (M1, M2, M4, M5), close the class the item names rather than the one instance, so a fourth round has nothing left on that surface. Author only: no product code, no commit, no gate.

### Items
1. One scope item per review item, M1 to M6 and L1 to L8, each citing the item, its finding number and the file and line the record names, and stating the fix the record's sound fix gives or a better one with the reason.
2. One scope item for the conf-example parity red: the arm's environment read must not look like a conf key to the parity scan (read it without a `.get` of an uppercase literal, or another way that keeps the scan's meaning), and the scan is not loosened.
3. Where an item's fix would change a shipped verb's output, refusal or argument contract (M1 and M2's attribute read, M3 and M4's consumes-from reading), say so in §4 and keep the change the narrowest that closes the class.
4. Each fix that a self-test arm can guard declares its `New arm:` line in §7 with the suite that holds it; a fix no arm can guard says why.
5. The spec carries `**Derived:** PLAY-dClosedLoop-2`, `order 15`, Tier-2, status OPEN, path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-32.md`, and one AC per item that a pass can observe with a probe on the touched files: suites are the close's, and a unit runs none of them.
6. Write `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-32-deviation-35.md` for the unit itself: Departs from `dTrueNorth [roster]`, design-to-spec, review finding, additive, spec writer under author-recorded, `new unit TOOL-dTrueNorth-32`, Caused-by `PLAY-dClosedLoop-2`. A fork the spec takes at rung 5 owes its own record, numbered from 36.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the spec; every AC is a probe a pass can run; the records read with no malformed field under `python tools/memory-tree/deviation_join.py`; the spec stays under 49152 bytes.

### Gates
No gate runs in this pass; the spec's §7 names every leg its files trip.

### Non-goals
Any other spec; product code; the four refuted findings; earlier rounds' items whose fixes hold; the flagged bar's inherited reds; inside §6, an untracked file named by full path inside a backticked token.
