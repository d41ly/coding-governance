# TOOL-dPlacedRequest-5 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-5

The unit was built from its spec at rev-7 (PINNED) on base `8c3d875c8`. A placement block gains the
`breakpoint` key, written only where the return carries it (`tools/loop/placement.py#add_placement`,
`tools/loop/placement.py#render_placement_block`). `tools/loop/placement.py#check_breakpoint` is the
`breakpoint` row of `tools/loop/placement.py#check_disposition_fact`: a name
`tools/loop/breakpoints.py#derive_placed_position` reads, a live build, an `item <tag>` among the rows
`tools/loop/breakpoints.py#read_build_item_rows` reads at the build's pin, and the request's consent through
the driver's new read-only `--request-consent`, a 1 refused `relayed`. The verb `placement.py breakpoint`
is `tools/loop/placement.py#write_breakpoint_declaration`: the lease read `amend` uses, refused
`live-holder`; the disposition record through the record factory under the build's lowest unit id; and,
where `tools/loop/placement.py#check_position_passed` reads the newest transition in a later step, an
at-once `--trigger ... --cause placement`. Every driver call of the module now runs through
`tools/loop/placement.py#run_unattended_verb`, the pre-claim draw's included.
`tools/loop/breakpoints.py#read_placed_breakpoints` lists the tracked records and
`tools/loop/breakpoints.py#read_breakpoints` hands them to `tools/loop/breakpoints.py#derive_breakpoints` as
its `placed` fact, so `--plan` prints them. The driver's `check_authorization` gains the source
`placement` and `print_spec_audit_line` its line; `--request-consent` runs `check_request_consent`.

Three readings of the spec, each in the commit's `Decided:` trailers. The spec cites
`derive_breakpoints(policy, definition, build)`; the landed rule takes `(values, steps, tags, facts)` and
reads no tree, so the records are read by its one caller and passed in. The spec's `check_breakpoint(block)`
takes the root and the key besides, which its facts read. The placement source is read at the
default-branch side of the pinned BASE, `_cb`, as the project default is, so a record a run commits on its
own pushed branch opts nothing in; on a first anchor that commit is BASE. Also: a declaration names
`item.entry.place` as an owner's release does, so `tools/loop/placement.py#read_owner_release` now skips
placed breakpoints, else a later `amend` on the build would read the declaration as the owner disposing
`breakpoint`.

No gate, suite or bar ran in this pass, and no `--selftest`. Each criterion below was observed by a probe of
the changed code, one `python tools/loop/placement.py --fixture --plant <case>` or
`python tools/loop/breakpoints.py --fixture --plant <case>` per case, each printing `held` (the run's node,
2026-11-20, PINNED).

**Evidences:** TOOL-dPlacedRequest-5
- AC1 — `--plant audit-request`: a build tRun in designing with no `spec-audit:` key and no
  `SPEC_AUDIT_DEFAULT`, the prompt "audit the specs" kept as the session's own words, placed, checked and
  declared, each exit 0, the record committed and pushed; the copied conf's `--preflight tRun` exited 0
  printing its spec-audit line, opted in `by placement` and `so it is owed: 2026-11-20`.
  `--plant audit-request-owed-only`, its policy `review.blocks = "owed-only"`: the list
  read `spec audit · after item.design.reason · owed`, and `--trigger tRun --subject tRun-specs --cause owed`
  exited 0 with `"trigger": "owed"` and `"blocks": "yes"`.
- AC2 — `--plant breakpoint-unnamed`: no `breakpoint:` key refused `names no breakpoint`, `design review`
  refused naming the four reviews, `item item.build.nothing` refused not declared, and no build refused
  `names no build`, each exit 1. `--plant breakpoint-closed`: `spec audit` on dDone refused
  `dDone is CLOSED, not live`, exit 1.
- AC3 — `--plant relayed`: the request's record on the scratch remote and no `.typed` line, check exited 1
  `placement: refused — breakpoint · relayed: ...`; with the line `s-fx` TAB the kept copy's blob planted
  it exited 0 `placement: pass — breakpoint dLive`.
- AC4 — `--plant declare`: `breakpoint` before `check` exited 1 naming no passed placement; after it, exit 0
  and one record `2026-11-20-build-TOOL-dLive-1-disposition-1.md`, `Item` `item.entry.place`, `Disposition`
  `breakpoint`, `Channel` `prompt`, `Reason` `spec audit · request <key>`, served
  `disposition TOOL-dLive-1`. `--plant declare-held`: another node's live lease, `breakpoint` exited 1
  `placement: refused — breakpoint · live-holder`, the folder holding no record.
- AC5 — `breakpoints.py --plant placed`: two records, `spec audit` and `item item.build.unit-pass`, listed
  as `breakpoint: spec audit · after item.design.reason · reviewer · owed` and
  `breakpoint: breakpoint · before item.build.unit-pass · reviewer · placement`, between the plan gate and
  the closing review.
- AC6 — `--plant past-position`: declared after a move into designing the stub driver recorded no call;
  after a move into building it recorded one, `--trigger dLive --subject dLive-specs --cause placement`.
- Unchanged plants re-run over the moved code, each `held`: placement `refusals` (its breakpoint row now
  `names no breakpoint`), `owner-released`, `predicate-fails` (the draw through the moved driver call),
  `each-disposition`, `late-answer`, `claim-lines`; breakpoints `driver-optin`, `values`, `ratification`.

- The checklist pass over the first commit (`destructive-step-before-its-precondition`,
  `refusal-branch-with-no-arm`, `two-readers-of-one-config-one-re-derived`):
  `tools/loop/placement.py#write_breakpoint_declaration` now reads the position before its one write, so a
  read that refuses leaves no record. `--plant breakpoint-unnamed` gains a build with no README, refused
  `dFresh does not exist`; `--plant declare` gains a live build whose README names no unit spec, refused
  `the build dBare has no unit spec` with no `build/` folder written; `--plant past-position` gains a stub
  that refuses, exit 1 `trigger refused — dLive · UNATTENDED check 37 FAILED`, the record kept;
  `breakpoints.py --plant placed` gains a record naming `design review`, the list refused exit 2 naming the
  record. The driver's reader of the record's `Reason` now matches the Python reader's split, `spec audit`
  before ` · request ` or alone, never `spec audit · <anything else>`. Each plant printed `held` again, and
  `--plant audit-request` over the narrowed reader.
- Unarmed, named: `tools/loop/placement.py#check_breakpoint`'s consent read timing out or answering
  neither 0 nor 1, and its composed rows not reading at the build's pin;
  `tools/loop/placement.py#write_breakpoint_declaration`'s trigger bound firing and a record-factory
  refusal; `tools/loop/placement.py#read_owner_release` over a placed record whose name refuses.

**Owed at the close (main loop):** the `loop placement fixtures` leg over every plant and TOOL-dDeclaredLoop-19's
breakpoint plants; the three `New arm:` lines of the spec's Gates section, the placement plants' failing
cases staged by `relayed` with the provenance read removed and by `audit-request-owed-only` with the placed
`spec audit` listed with cause `placement`, the breakpoint plants' by `placed` with
`read_placed_breakpoints` unhooked, and the `unattended.test.sh` blocks `DPR5 S7` and `DPR5 S3`, their
failing cases the placement source dropped and the verb answering 0 regardless, waived for this build's
landing by README rule 8; and the legs the Gates section names: `unattended protocol size`, `recall floor`,
`recall floor arms`, `memory hygiene`, `spec tokens`, `scratch-guard self-test`, `tier2-review self-test`,
`docs` and `codebase-map coverage + freshness`, with the template size gate over the two raised rows and the
unattended kit gate's check 26 over the new verb's header line, Skill line and verb-carrier entry.
