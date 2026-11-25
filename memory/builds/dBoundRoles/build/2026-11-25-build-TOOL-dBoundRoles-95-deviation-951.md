# TOOL-dBoundRoles-95 deviation 951 — the gap TOOL-dBoundRoles-23 names, closed in the guard

**Serves:** deviation TOOL-dBoundRoles-95

- **Departs from:** `TOOL-dBoundRoles-23@rev-7` [S6, §3 Edges, §4 the floor's table, AC5, §8 F6]
- **Hand-off:** spec-to-code
- **Before:** S6 and F6 say the guard's run admission lands a live run's change to `roles.effort.*` under every `policy-file.guard` value, so closing that path is the guard's, outside that unit; the verdict admits the same set under `owner-only` and `agents-within-mandate`.
- **After:** (1) S6 and F6 restated: where the landed policy file leaves `policy-file.guard` at `owner-only`, `tools/policy/guard.py#check_run_mandate` refuses a live run's own change to `.governance/policy.toml`, alone or beside other guarded paths, so an agent's commit changes that file only as the raised cap or as a merge taking a parent's blob whole. `agents-with-reason` and `agents-within-mandate` still admit the run, their records owed, and no longer admit the same set as `owner-only`. An unset key is `owner-only`, whatever the catalogue's default says, and a reader that does not answer admits nothing. `tools/roles/roles_lib.py#check_effort_floor` does not move. The limits stand in the header of `tools/policy/guard.py` and in `help/policy.md`: the guard's or the reader's code edited in the working tree, the landed revision moved by hand, a merge taking an old parent's blob, a level written while the key read another value, and a run closing an opened key beside a low level. (2) One limit this unit's section 4 does not list is named beside them: the catalogue decides whether the landed file is valid, so a run that makes it invalid moves the read to an older revision, whose own set value then answers. (3) The owner-only step's refusal line also ends with the reason the admission gave, as the guard-self step's does, and step 4's sentence joins the shapes it offers with semicolons.
- **Cause:** owner ruling
- **Reason:** the owner answered `TOOL-dBoundRoles-23` F6 on 2026-11-25, "Close it before landing"; that spec is CLOSED and frozen, so the restated text stands here. (2) keeps the pages true, and (3) tells a run on its own branch why a line worded for other branches met it.
- **Evidence:** the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-25-build-TOOL-dBoundRoles-95-1-acceptance-ledger.md`, and the owner's answer in `memory/builds/dBoundRoles/prompts/2026-11-25-prompt-TOOL-dBoundRoles-95-spec-brief.md`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-95
