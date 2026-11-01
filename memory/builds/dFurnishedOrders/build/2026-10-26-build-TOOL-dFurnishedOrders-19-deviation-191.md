# TOOL-dFurnishedOrders-19 deviation 191 — a dropped, invented or doubled upstream row fails the return on every edge, not only on a measured one

**Serves:** deviation TOOL-dFurnishedOrders-19

- **Departs from:** `TOOL-dDeclaredLoop-29@rev-2` [S6]
- **Hand-off:** design-to-spec
- **Before:** `join_upstream` classes a handed row with no answer as `dropped`, an answered id not handed as `invented` and an id answered twice as `doubled`; on a `measured` edge any of these refuses the return, and on a `record` edge each is recorded as a finding and the return stands (TOOL-dDeclaredLoop-29 S6).
- **After:** the work order's return schema, rendered from its own rows by `render_return_schema`, fails a return carrying a dropped, invented or doubled row on every edge, `record` and `measured` alike, and `validate_return`'s defects send it back under `roles.retries`; `join_upstream` still classes and records every answer of the return that is finally accepted, and a `bypassed` answer still gates only on a `measured` edge (TOOL-dFurnishedOrders-19 S5, §8 F1).
- **Cause:** owner ruling
- **Reason:** the clause this unit carries, cl-dClosedLoop-0210@c44de500, is the owner's NT-10: "each work order's return schema rendered from its own rows, each row id an allowed value and each required once, so a dropped, invented or doubled row fails the return and is retried as `roles.retries` says". The night pass two states both halves, the schema failure on the return and the measurement gate on a `bypassed` row, and TOOL-dDeclaredLoop-29 S6 read the gate as covering both.
- **Evidence:** `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:313-317`; `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-handoffs-prior-art.md:237-245`, where the per-order schema refused all three planted rows; TOOL-dFurnishedOrders-19 AC5.
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer stage of the harness's spec run for dFurnishedOrders, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dFurnishedOrders-21
- **Caused-by:** cl-dClosedLoop-0210@c44de500
