# TOOL-dBoundRoles-96 deviation 961 — the guard takes the key from the valid landed file alone

**Serves:** deviation TOOL-dBoundRoles-96

- **Departs from:** `TOOL-dBoundRoles-95@rev-1` [S2, S4, §4 "The value", "The wrappers", "What it does not check" and "Texts"]
- **Hand-off:** spec-to-code
- **Before:** the value table of that spec answers the reader's value for source `file` and for a `last-valid` answer not resting on the catalogue's default; its wrappers print, for a policy leaf, the line worded for branches off a live run's, whatever the key reads; and its texts name a catalogue edit among the limits.
- **After:** (1) the value table's first row reads source `file` alone, and its second row any other source, `last-valid` among them, as `owner-only` with the reader's reason, in `tools/policy/guard.py#read_guard_value`. (2) The sentence on a `last-valid` answer whose reason is the default has no object left. (3) The limit deviation record 951 names in its second item is closed; it had held for the cap census as for the catalogue, since each decides in the working tree whether the landed file is valid. (4) The guard-self and owner-only lines of a policy leaf, in `tools/loop/guard.py#check_staged`, name a live run's branch only where it would be admitted, which amends the third item of 951; the list path's line keeps its words. (5) The header of `tools/loop/floor.py` and section "The guard" of `tools/policy/README.md` state `guard-self` as the floor table of `help/policy.md` does. (6) Beside these, section "The arms" of `tools/policy/README.md` spelled a stale figure of `guard-*` cases, now the figure a probe over `CASES` of `tools/policy/check_policy.py` prints.
- **Cause:** review finding
- **Reason:** the security review of `TOOL-dBoundRoles-95` found the path by which a run's edit of the catalogue or the cap census moved the read to an older opened revision, and the owner answered "Close it before landing" on 2026-11-25; that spec is CLOSED and frozen, so the restated text stands here. (6) sits in the paragraph the new case extends.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-25-build-TOOL-dBoundRoles-96-1-acceptance-ledger.md`, and the review `memory/builds/dBoundRoles/reviews/2026-11-25-review-TOOL-dBoundRoles-95-security-diff-review-round1.md`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-95
