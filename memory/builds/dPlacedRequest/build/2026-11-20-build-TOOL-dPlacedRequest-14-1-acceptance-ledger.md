# TOOL-dPlacedRequest-14 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-14

The unit was built from its spec at rev-6 (PINNED) on base `7dc12c126`. `tools/loop/budget.py` gains the
request arm of `draw`, `--request <key>`, `--request-text <file>` and `--rows <file>`, in
`tools/loop/budget.py#print_request_draw`, counting the rows `tools/loop/budget.py#read_request_rows` reads
from the request record's first-parent messages, and answering through
`tools/loop/budget.py#derive_request_draw`, which writes nothing. The cause and item checks of
`tools/loop/budget.py#record_draw` moved into `tools/loop/budget.py#check_draw_cause`, which both draws call.
The unattended driver gains `--request-draw <content key> --cause <cause> --item <item>` in
`tools/unattended/unattended.sh#run_request_draw`: `check_request_recorded`, a create through
`write_request_record` from the kept copy where no record exists, one bounded fetch,
`budget.py draw --request`, and the row built by `build_gov_commit` on the tip read and written by `write_gov_ref` with
that tip expected, a lost race re-read at most three times (PINNED). `tools/loop/placement.py#write_placement`
draws before `tools/loop/placement.py#add_placement` writes, through its new `before` hook, the cause from
`tools/loop/placement.py#derive_request_draw_cause` and the call in
`tools/loop/placement.py#run_request_draw_verb`; an owner's placement draws nothing.

Two names moved from the spec's inventory: `record_request_draw` leads with `record`, which the naming
lexicon refuses as undeclared, so the function is `derive_request_draw`, the name saying it writes nothing,
as S3 states. The spec names no text file on the driver verb; the driver's text file is the kept copy
`<git-common-dir>/requests/<key>.md` that TOOL-dPlacedRequest-19's `--request` writes, and the create runs
under no session, so a draw never adds a `.typed` consent line for a session that did not type the words.

No gate, suite or bar ran in this pass, and no `--selftest`. Each criterion below was observed by a probe
of the changed code, one `python tools/loop/budget.py --fixture --plant <case>` per new plant, each
printing `held` (the run's node, 2026-11-20, PINNED). The draw site's RED was staged once as a probe: with
the cause in `tools/loop/placement.py#write_placement` forced to none, `--plant placement-loop` printed
`MISSED re-placement 1 did not draw 1/4`, and held again once restored.

**Evidences:** TOOL-dPlacedRequest-14
- AC1 — `--plant placement-loop`: a recorded request placed `continue dDone` under `declared-checked`, its
  check refusing `the build dDone is CLOSED, not live` each lap; re-placements 1 to 4 printed
  `draw · route-back · item.entry.place · 1/4` up to `4/4`, the fifth exited 3 printing
  `placement: pre-claim budget exhausted — <key> · 4/4`, the placement file holding 5 (DERIVED) blocks and
  the record 5 (DERIVED) commits, the create and 4 (DERIVED) rows. The spec's "the fifth `place`" is read
  as the fifth re-placement, the sixth call, since the fourth re-placement is the fifth call and draws 4/4.
- AC2 — `--plant no-intake`: no `--request` ran and the origin held no request ref; the first re-placement
  printed `request — <key> · recorded refs/gov/requests/<key>` then
  `draw · route-back · item.entry.place · 1/4`, the key the one `derive_request_content_key` gives the text, and the loop was refused at the same
  lap; `budget.py draw --request-text <the kept text> --rows <the record's messages>` printed
  `exhausted · 4/4`, exit 3.
- AC3 — `--plant rows-on-ref`: two draws printed `1/4` and `2/4`; the origin's
  `git log --first-parent` of the record read three commits, each row parented on the tip before it and
  the create parentless, every message opening `gov-request <key>`, and no object on the origin carried
  the request text's marker.
- AC4 — `--plant two-nodes`: the second clone's push was held by a `git` shim until the first clone drew
  `1/4`; the second then printed
  `lost the race, re-read 1 of 3 · lost the race on the lease: [rejected] (stale info)` and `draw · route-back · item.entry.place · 2/4`, exit 0, the record's rows reading 2/4 over
  1/4. `--plant unreachable`: with the remote's URL pointing nowhere the draw exited 2 printing
  `not drawn, contention · the remote did not answer the record read`, and the record kept its create alone.
- AC5 — `--plant slug-retry`: the draw the claiming step makes before a fresh slug, made as
  TOOL-dPlacedRequest-21's `entry.claim` will make it, printed `draw · route-back · item.entry.claim · 1/4`;
  the cause `retry` exited 2 printing `the cause retry is outside the closed set` and added no row.
- AC6 — `--plant owner-after-exhausted`: four draws spent the budget, a declared re-placement exited 3
  exhausted, and under `owner-places` a placement with `--owner <record>` exited 0 `placer owner`,
  printing no draw, the record still 5 (DERIVED) commits.
- The placement plants — every one of the 21 (DERIVED) plants of `tools/loop/placement.py#PLANTS` run by
  direct CLI printed `held`; `predicate-fails`, which places again after a refused check, now runs with
  the driver and a remote, its record planted by `tools/loop/placement.py#write_fixture_gov_ref`, and owes
  the draw `1/4`. The budget plants `unknown-cause`, `patch-draw`, `value` and `no-own-conf-read` printed
  `held` over the moved cause check.

- The checklist pass over the first commit (`refusal-branch-with-no-arm`,
  `destructive-step-before-its-precondition`): `--plant unreachable` now also re-places with the remote
  unreachable, exit 2 printing `drew nothing, so no block is written` with the block count unchanged (S6),
  and draws on a key whose kept text keys to another request, which the driver now refuses before any write,
  exit 2 naming both keys, the origin gaining no record; the first commit created the other key's record
  before refusing. `--plant slug-retry` now drives `budget.py draw`'s own refusals, a key that is no content
  key, no `--rows` and `--rows` beside `--build`, each exit 2, and a draw over rows holding a malformed row
  and a message under another key, each named on stderr as not counted, the count reading `2/4`. The
  `unattended.test.sh` block gains the kept-text refusal.
- Unarmed, named: the driver's branches for no python, no loop kit, a scratch file it cannot create, a
  fetch failing after the record read answered, a fetched record that does not read, a row commit git
  cannot build, a push the remote answers and refuses, and a race lost four times; and
  `tools/loop/placement.py#run_request_draw_verb`'s bound firing.

**Owed at the close (main loop):** the `loop budget fixtures` and `loop placement fixtures` legs over every
plant; the two `New arm:` lines of the spec's Gates section, the budget plants' failing case staged by
`placement-loop` with the draw site removed from `place`, and the `unattended.test.sh` block `DPR14`, its
failing case a parentless row commit, waived for this build's landing by README rule 8; and the legs the spec
names, read from the Gates section: `scratch-guard self-test`, `tier2-review self-test`, `recall floor`, `recall floor arms`,
`memory hygiene`, `spec tokens`, `docs` and `codebase-map coverage + freshness`, with the unattended kit
gate's check 26 over the new verb's header line, Skill line and verb-carrier entry.
