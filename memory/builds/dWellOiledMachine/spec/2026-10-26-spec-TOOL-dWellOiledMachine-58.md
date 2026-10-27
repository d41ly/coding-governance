# TOOL-dWellOiledMachine-58 — the record door: every coordination write bound to its writer's session binding, and the two closing items it admits

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 26 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0505@d65ddfae whole
**Carries:** node:item.life.unlease
**Carries:** node:item.life.quiesce
**Carries:** node:record-kind.quiesce

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-c.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

A coordination write today is bound to nothing: only run claims are identity-checked
(`check_claim_writable`, `tools/unattended/unattended.sh:2243`), so a session can post into another
session's mail ref, write a terminal tombstone on a lease it does not hold, or delete another
build's mailbox. This unit puts one door in front of every coordination write the `gov`
coordination verbs make, today `unattended.sh`'s `--lease`, `--mail` and `--request`, the memory plan's
`[doors]` door through which the coordination verbs write refs, claims, leases and mail, and binds
each write to the writer's own session binding (layer-runtime `[act]`). It ships the two closing
items the door admits, `life.quiesce` and `life.unlease`, and states the door's limit openly: a
process outside the door that holds push rights to the remote is not stopped, since under Codex the
git boundary is the floor (the owner's FK-5-3, the whole-design audit's A2-F10).

## 2. Scope (IN)

- **S1** — The door (I32), `check_writer_binding(ref, expected, src, binding, verb)` in
  `tools/memory-tree/gov_record.py`, TOOL-dTotalRecall-2 S1's record door, reached as the verb
  `gov_record.py door <ref> <expected sha or empty> <src or empty>`. The writer is
  `CLAUDE_CODE_SESSION_ID` and its binding is the I17 record
  `<git-common-dir>/gov/session-bindings/<session id>.md` (TOOL-dWellOiledMachine-12 S1), read through
  that unit's `session_binding.py read <session id>` (its S2) run as a subprocess resolved by
  `resolve_kit_dir`, since a kit imports no sibling kit (TOOL-dGroundRules-1 §4); the verb is
  `GOV_DOOR_VERB`, which each coordination verb sets before it writes. It reads every first-parent
  commit of `<expected>..<src>`, so a chain of messages is judged message by message.
  No session or no binding is refused. It exits 0 admitted, 1 refused printing
  `door — refused · <ref> · <reason>`, and 2 when git cannot say what the write is. Observed by AC1,
  AC2, AC3, AC4, AC5.
- **S2** — The seam: `write_gov_ref` (TOOL-dPlacedRequest-11 S1, the one ref writer) runs
  `"${GOVREF_DOOR[@]}" <ref> <expected> <src>` before its push whenever `<ref>` sits under
  `refs/gov/leases/`, `refs/gov/mail/`, `refs/gov/requests/` or `refs/gov/runs/`, the coordination
  namespaces. A door exit 1 or 2 makes `write_gov_ref` return 2 with `GOVREF_WHY` set to the door's
  line, pushing nothing. `tools/unattended/unattended.sh` sets `GOVREF_DOOR` once, through
  `resolve_kit_dir "$py" memory-tree gov_record.py "$KIT_DIR"` (`tools/unattended/lib-unattended.sh:132`);
  an empty `GOVREF_DOOR` refuses every coordination write with `door — not wired`, deny by default.
  The block stays byte-identical in `tools/lib/gov-ref.sh`, `tools/unattended/unattended.sh` and
  `tools/run-gates/post-merge.sh`, whose `refs/gov/bar-red` write is outside the namespaces. The two
  pushes that carry a coordination ref outside `write_gov_ref`, the lander's atomic landing push in
  `tools/push-main.sh` and the commit queue's `run_build_push` in `tools/runtime/commit_queue.py`
  (TOOL-dWellOiledMachine-60 S3, S7), run the same door on each lease or mail refspec they carry
  before pushing, and a refusal pushes nothing. Observed by AC1, AC7, AC9.
- **S3** — The write rule: a mail write to `refs/gov/mail/<slug>/<fleet tag>/<segment>` is admitted
  only when `<fleet tag>` is the binding's `node`, `<segment>` is `derive_ref_segment` of the binding's
  `session` (TOOL-dPlacedRequest-12 S1), and the message's `from-tag` and `from-session` keys
  (KICK-dKeptSession-5 S4) name the same; a lease or request write only when the record's `session`
  and `fleet-tag` keys (TOOL-dPlacedRequest-1 S2) name the writer. A ref path or sender naming another
  session, act or fleet tag is refused `cross-session`. Observed by AC1.
- **S4** — The tombstone rule: a lease record whose `status` is `landed` or `withdrawn` is admitted
  only when (a) the tip read names the writer, its holder; (b) `GOV_DOOR_VERB` is `lease.take-over`;
  or (c) `GOV_DOOR_VERB` is one of `DOOR_CLOSING_VERBS` and the writer holds the build lease
  `refs/gov/leases/<slug>/build` (live, naming the writer), and, for a unit lease whose tip names
  another holder, the build's newest `quiesce` record (S8) names that ref `ack` or `ceiling`. Any
  other tombstone is refused `forged-tombstone`. Observed by AC2, AC6.
- **S5** — The prune rule, for a write with an empty `<src>`: pruning a ref under the build's own
  `refs/gov/mail/<slug>/` is admitted only when `GOV_DOOR_VERB` is one of `DOOR_CLOSING_VERBS`, every
  message id on that ref has a `mailbox-message` record under `memory/builds/<slug>/`
  (KICK-dKeptSession-5 S12), so the copy came first, and the writer holds that build's lease as its
  holder, which a session that took the lease over through the take-over verb is, or acts as the
  owner's guarded command: an I17 binding whose `owner` is `yes` with the door's stderr a terminal, the
  owner proof `.githooks/pre-commit:207` reads. Pruning any other `refs/gov/mail/` ref, a build or unit
  lease, or a request is refused; TOOL-dPlacedRequest-16 S7's `lease.prune` of a terminal
  `refs/gov/leases/run/` ref is admitted as that unit states it. Observed by AC3, AC4, AC5.
- **S6** — The closing verbs, `DOOR_CLOSING_VERBS = ("life.unlease",)` in `gov_record.py`.
  `life.unlease` alone closes a build until dShippedRelease lands `deploy.unlease`, which adds its
  name to the tuple in its own unit, and a landing ends at the lander until then; dTendedCadence adds
  Maintain's prune the same way once it lands it. A name not in the tuple is no closing verb, so
  `deploy.unlease` set today is refused. Observed by AC4.
- **S7** — `life.quiesce`, the verb `unattended.sh --quiesce <slug> [--request <id>]`, refused unless
  the writer holds the build lease or acts as the owner's guarded command. Where the build has a
  run-state file it holds the run through `run_hold` (`tools/unattended/unattended.sh:6848`) under
  `host-owner-action`, so nothing new is dispatched. For each unit lease of the build whose holder is
  another session or node, it posts once a `question` with subject `quiesce <ref>` to `unit:<id>`
  (KICK-dKeptSession-5 S5, KICK-dKeptSession-28's recipient), then judges each: `ack` when an `ack`
  answers that post, `ceiling` when `check_deadline_passed` (TOOL-dPlacedRequest-17 S4) reads the post
  older than `runtime.act-ceiling` hours, read through `policy-shim.sh get runtime.act-ceiling`,
  `waiting` otherwise. It is re-runnable: it prints `quiesce — waiting · <n> unit lease(s)` and exits
  3 while any waits, and once none does it writes the S8 record and prints `quiesce — done · <slug>`,
  exit 0. Observed by AC6.
- **S8** — The record kind `record-kind.quiesce`, a `[[record-kind]]` row in
  `tools/memory-tree/record-kinds.toml` (TOOL-dTotalRecall-1's registry) written by
  `gov_record.py new quiesce`, fields `Build`, `Request`, `Unit-leases` (one `<ref> ack <message id>`
  or `<ref> ceiling <utc>` per held unit lease, or `none`) and `Ceiling-hours`. Observed by AC6.
- **S9** — `life.unlease`, the verb `unattended.sh --unlease <slug>`, every write under
  `GOV_DOOR_VERB=life.unlease`, in this order: refused unless the writer holds the build lease or acts
  as the owner's guarded command; a build whose build lease is a `landed` tombstone prints
  `unlease — <slug> · landed: its close ends at the lander until deploy.unlease lands` and exits 0;
  each unit lease written `withdrawn` through `--lease release unit <slug> <id> --as withdrawn`
  (TOOL-dPlacedRequest-16 S2); the mailbox closed, each message on every ref under
  `refs/gov/mail/<slug>/` read through `read_mailbox` (KICK-dKeptSession-5 S6) and given a
  `mailbox-message` record where it has none, titled `<id> — undisposed at close`, and only then each
  ref pruned through `write_gov_ref <ref> <tip read> ""`, a missing ref counting as done; then the
  build lease written `withdrawn`. It prints `unlease — <slug> · <n> unit lease(s) · <m> mail ref(s) ·
  build lease withdrawn`. Observed by AC4, AC6.
- **S10** — The fixture, `tools/memory-tree/door_fixture.py`: a bare remote and two clones under
  `%TEMP%` with short names, two I17 bindings on two fleet tags, the unattended kit resolved through
  `resolve_kit_dir`, and `--case <name>` running one planted case through the coordination verbs,
  never through `gov_record.py door` itself, printing the verb's last line and its exit code.
  Observed by AC1 to AC7, AC9.
- **S11** — The limit, stated where a reader meets it: the door's docstring, the verbs guide's door
  section in `tools/unattended/VERBS.template.md` (rendered to `memory/guides/UNATTENDED-VERBS.md`) and
  `help/runtime.md`, each saying a process outside the door that holds push rights to the remote is not
  stopped. The guide also gains `--quiesce`, `--unlease`, `GOV_DOOR_VERB` and the door's refusal
  reasons. Observed by AC8.

## 3. Non-goals (OUT)

- No signed coordination commits: FK-5-3's option B, rejected by the owner for its key management on
  every node.
- No secret scan at the door: TOOL-dWellOiledMachine-57 adds the token-shape arm to this door.
- No `deploy.unlease` and no Maintain's prune: dShippedRelease's and dTendedCadence's, each adding its
  name to `DOOR_CLOSING_VERBS`.
- No lifecycle request, pause wait, snapshot or terminal transition: `life.request`, `life.snapshot`
  and `life.close` are TOOL-dWellOiledMachine-3's, which calls `--quiesce` and `--unlease`.
- No workspace reaping: S9's tombstones leave the build's workspaces unleased, and
  TOOL-dWellOiledMachine-11's sweep reaps an unleased workspace the supervisor allocated.
- No change to `check_claim_writable`'s table: the door is a second, independent check in front of the
  push.
- No act binding read: the door compares a write with the session binding; acts are bound at the
  dispatcher by TOOL-dWellOiledMachine-7.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-12` — `session-bindings`, the I17 record whose `session`, `node` and `owner` fields every door verdict compares a write with
- **consumes-from** `TOOL-dWellOiledMachine-60` — `check_writer_binding`, which the landing's notice chain and lease beat pass in the lander's atomic push and the commit queue's fenced push, outside `write_gov_ref`
- **hands-off** `TOOL-dWellOiledMachine-57` — `check_writer_binding`, the door that unit adds its token-shape refusal and its request-record proof to
- **hands-off** `TOOL-dWellOiledMachine-3` — `check_writer_binding` and the `--quiesce` and `--unlease` verbs, which that unit's withdraw and supersede call and whose tombstones and mailbox close the door admits
- **hands-off** `TOOL-dWellOiledMachine-41` — `check_writer_binding`, through which that unit's offers and holder writes on a unit lease pass
- **consumes-from** external — TOOL-dTotalRecall-2's `gov_record.py` and TOOL-dTotalRecall-1's `record-kinds.toml`, the door and registry this unit grows
- **consumes-from** external — TOOL-dPlacedRequest-11's `write_gov_ref`, -12's `derive_ref_segment`, -1's lease record and `--lease` verb, -16's tombstone and `--as withdrawn`, -17's `check_deadline_passed`
- **consumes-from** external — KICK-dKeptSession-5's `read_mailbox`, `--mail post`, `--mail ack` and `mailbox-message` kind, and KICK-dKeptSession-28's `unit:` recipient
- **hands-off** external — dShippedRelease's `deploy.unlease` and dTendedCadence's Maintain's prune, each joining `DOOR_CLOSING_VERBS`
- **hands-off** `TOOL-dWellOiledMachine-63` — `check_writer_binding` and its verdict table, which that unit gives a node writer for the sessionless tick and supervisor (finding 1)
- **hands-off** `TOOL-dWellOiledMachine-79` — the door's namespaces and rules (finding 67), which the spec audit's minors batch repairs
- **hands-off** `TOOL-dWellOiledMachine-84` — `write_gov_ref`'s namespace list and `check_writer_binding`, which gain the exact-entry kind for `refs/gov/attendance` (finding 39)
- **hands-off** `TOOL-dWellOiledMachine-90` — `door_fixture.py`'s binding and token cases, its resolver for bash, and the door's reading of a scan exit 2 (findings 6, 24, 66)

## 4. Design

### Evidence

- No coordination write passes a door today: `git grep -n "gov_record" -- tools` finds nothing, and
  the claim push is `write_claim` (`tools/unattended/unattended.sh:2396`), whose only identity check is
  `check_claim_writable` (`:2243`) keyed on `CLAUDE_CODE_SESSION_ID`.
- KICK-dKeptSession-5 S11 marks the door's hand-over at `write_mail_ref`, its one mail writer, and
  every mail, lease and request write ends in `write_gov_ref` (TOOL-dPlacedRequest-11 S1), so one
  call there binds them all where a call per verb would be several.
- The owner's terminal proof is `[ -t 2 ]` (`.githooks/pre-commit:207`); `tools/policy/guard.py`
  judges only the commit that lacks it.
- `resolve_kit_dir "$py" <home> <anchor> "$KIT_DIR"` is the unattended kit's sibling-kit reach
  (`tools/unattended/unattended.sh:1268`, `:14304`), and the kit requires memory-tree
  (`tools/unattended/kit.toml`, `requires`), so an install with the verbs has the door.
- The memory plan names the door's writes: "the coordination verbs write refs, claims, leases and
  mail, through `record`'s door once dTotalRecall lands it, which binds each such write to its writer"
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:273-276`).
- `life.quiesce` and `life.unlease` are rows of flow-steps' lifecycle table
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:685,688`), and the
  mailbox close is its rule at `:84-90`.

### The verdict

| Op, read off `<src>` | Ref | Admitted when |
|---|---|---|
| write | `refs/gov/mail/<slug>/<tag>/<seg>` | `<tag>` and `<seg>` and the message's `from-tag` and `from-session` name the writer |
| write | `refs/gov/leases/…`, `refs/gov/runs/…`, `refs/gov/requests/…` | the record's `session` and `fleet-tag`, where it carries them, name the writer |
| tombstone (`status: landed` or `withdrawn`) | a build or unit lease | the tip read names the writer; or `lease.take-over`; or a closing verb under the writer's build lease, a unit lease held elsewhere only with a `quiesce` record naming it |
| delete (empty `<src>`) | `refs/gov/mail/<slug>/…` | a closing verb, every message copied, and the writer the build lease's holder or the owner's guarded command |
| delete | `refs/gov/leases/run/…` | TOOL-dPlacedRequest-16 S7's `lease.prune` |
| delete | anything else | never |

The op is read off the commit `<src>` names, through `git cat-file commit`; the tip read is
`<expected>`. Each refusal names one reason word: `no-session`, `no-binding`, `cross-session`,
`forged-tombstone`, `not-closing-verb`, `not-copied`, `not-holder`, `delete-refused`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_writer_binding` | Python function | `check`, OK |
| `door` | `gov_record.py` verb | none |
| `DOOR_CLOSING_VERBS` | constant, one name | none |
| `GOVREF_DOOR` | shell array, the door's argv | none |
| `GOV_DOOR_VERB` | environment variable each verb sets | none |
| `--quiesce`, `--unlease` | `unattended.sh` verbs | none |
| `quiesce` | record kind | none |
| `door_fixture.py` | fixture script | none |

### Files touched (estimate)

- `tools/memory-tree/gov_record.py`: `check_writer_binding`, the `door` verb, `DOOR_CLOSING_VERBS`
- `tools/memory-tree/record-kinds.toml`: the `quiesce` row
- `tools/memory-tree/door_fixture.py`: the fixture
- `tools/lib/gov-ref.sh`: the door call in `write_gov_ref`, copied byte-identical into
  `tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh`
- `tools/unattended/unattended.sh`: `GOVREF_DOOR`, `GOV_DOOR_VERB` on each coordination verb,
  `--quiesce`, `--unlease`, and `KIT_UNATTENDED_VERSION` moved
- `tools/push-main.sh` and `tools/runtime/commit_queue.py`: the door on each coordination refspec of
  their atomic pushes
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `help/runtime.md`: the door and its limit, the page created if no earlier unit made it

### Alternatives rejected

- **A door call in each verb.** Mail, lease, tombstone, request and prune writes would each carry one,
  and a sixth verb could forget it; `write_gov_ref` is the one writer every one of them ends in.
- **The door in the pre-push hook.** A hook sees refs and shas but not the writing session's binding,
  and `git push --no-verify` skips it.
- **Signed commits.** The owner's FK-5-3 option B; the key management on every node was declined.

## 5. Production-readiness checklist

- security — a deny-by-default guard on every coordination write: an unwired door, an absent session
  and an absent binding each refuse; the owner path needs both the owner binding and a terminal. The
  limit is stated in three places: a push outside the door is not stopped.
- perf / scale — one Python spawn and one `git cat-file` per coordination write, beside a push that
  already costs a network round trip.
- error / empty / loading states — a git failure inside the door exits 2 and the write is not
  completed; a missing mail ref counts as deleted; `--quiesce` re-runs until nothing waits.
- observability — every refusal is one `door — refused` line with one reason word, carried in
  `GOVREF_WHY` to the verb that wrote.
- risks — a legitimate holder whose binding is missing is refused until TOOL-dWellOiledMachine-12
  binds the session; `--unlease` before a `quiesce` record refuses a unit lease held elsewhere, which is
  the clause's order.
- testing — the fixture cases under AC1 to AC7 and the arm in §7.
- migration — none: the door adds a check and no record moves; legacy `refs/gov/runs/` claims pass
  the write rule because their writer is their holder.
- user docs — the verbs guide's door section and `help/runtime.md`.

## 6. Acceptance criteria

Each case runs `python door_fixture.py --case <name>`, which drives the coordination verbs in the
fixture's clones, never `gov_record.py door` itself.

- **AC1** — When `--case cross-session-mail` runs `unattended.sh --mail post fx` as session `s2` with
  the ref planted to be `s1`'s, the verb exits 2 printing `door — refused · refs/gov/mail/fx/a/s1 ·
  cross-session` and the remote's ref is unchanged; `--case own-mail` posts as `s1` to its own ref and
  exits 0.
  Red when: the planted cross-session post reaches the remote, as a `write_gov_ref` with the door call
  removed shows.
- **AC2** — When `--case forged-tombstone` runs `--lease release unit fx TOOL-fx-1 --as withdrawn` as
  `s2` on a unit lease `s1` holds, with no take-over and no closing verb, the verb exits 2 printing
  `forged-tombstone` and the lease stays `live`; `--case holder-tombstone` run as `s1` writes it.
  Red when: the forged tombstone lands.
- **AC3** — When `--case prune-no-lease` runs `--unlease fx` as a session holding no lease of `fx`,
  it exits 2 printing `not-holder` and every `refs/gov/mail/fx/` ref is still on the remote.
  Red when: a mail ref is deleted by a session holding no lease.
- **AC4** — When `--case closing-build` runs `--unlease fx` as the build lease's holder over a build
  holding `s2`'s mail ref `refs/gov/mail/fx/b/s2`, every message gains a `mailbox-message` record
  before the ref is deleted and the run prints `build lease withdrawn`; `--case closing-build
  --verb deploy.unlease` exits 2 printing `not-closing-verb`, and `--case closing-build --closing
  deploy.unlease` adds the name to the fixture's `DOOR_CLOSING_VERBS` and closes the build the same way.
  Red when: a ref is deleted before its messages are copied, or a name outside the tuple closes it.
- **AC5** — When `--case other-mailbox` runs `--unlease fx` as `fx`'s holder with a delete of
  `refs/gov/mail/fy/a/s1` planted into its ref list, the delete exits 2 printing `delete-refused` and
  `fy`'s ref is unchanged.
  Red when: another build's mailbox is deleted.
- **AC6** — When `--case quiesce-ceiling` runs `--quiesce fx` over a unit lease held on fleet tag `b`
  with `runtime.act-ceiling` planted at `0.001`, the first run exits 3 printing `quiesce — waiting · 1
  unit lease(s)`, a run past the ceiling writes a `quiesce` record whose `Unit-leases` line names
  `ceiling`, and `--unlease fx` then writes that unit lease `withdrawn`; with no `quiesce` record,
  `--unlease fx` refuses that unit lease `forged-tombstone`.
  Red when: a unit lease held on another node is tombstoned with no `quiesce` record, or a quiesce
  that never reached the ceiling records one.
- **AC7** — When `--case unwired` runs `--mail post fx` with `GOVREF_DOOR` emptied, it exits 2
  printing `door — not wired`; and `grep -c "GOVREF_DOOR" gov-ref.sh` over the three copies prints the
  same count in each.
  Red when: a coordination write is pushed with no door, or one copy of the block differs.
- **AC8** — When `grep -n "push rights" runtime.md tools/unattended/VERBS.template.md` runs over the
  help page and the guide, each
  file names the limit, and the guide names `--quiesce`, `--unlease`, `GOV_DOOR_VERB` and the eight
  reason words.
  Red when: either file omits the limit or the guide omits a verb or a reason.
- **AC9** — When `--case fenced-push-forged` runs the commit queue's `run_build_push` as `s1` with its
  lease beat planted to name session `s2`, the push exits non-zero printing `door — refused ·
  refs/gov/leases/fx/build · cross-session`, and the remote's branch and lease are both unchanged.
  Red when: the atomic push lands the forged beat, as a `run_build_push` with its door call removed
  shows.

## 7. Gates

`unattended kit gate` · `push-main self-test` · `memory hygiene` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

The unattended kit's self-test suites are waived for this build's landing (README rule 8); the
fixture is this unit's own observation and the arm below its home.

New arm: tools/memory-tree/door_fixture.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC9 · each planted case staged against `write_gov_ref` with its door call removed · none

## 8. Open questions

- **F1 — Where does the door sit?** (a) Inside `write_gov_ref`, before its push, for the coordination
  namespaces; (b) one call in each coordination verb; (c) the pre-push hook. (b) leaves a verb that
  forgets the call unbound and (c) cannot read the writing session's binding and is skipped by
  `--no-verify`. Rung 3, the most capable option, reusing the one writer the parents built.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — How does the door know the verb?** (a) `GOV_DOOR_VERB`, set by each verb before it writes,
  with no value admitting no closing path; (b) the door inspecting its parent process. (b) is
  platform-specific and reads a process table a hook cannot trust either. Rung 3. The variable is
  forgeable by a caller that sets it, which is the stated limit's class: a writer outside the verbs.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — What marks an undisposed message in the build folder?** (a) A `mailbox-message` record
  titled `<id> — undisposed at close`, written for every message no transition's disposal recorded;
  (b) a new `Disposed` field on KICK-dKeptSession-5 S12's kind. (b) changes a parent's record kind,
  an ask for dKeptSession, where (a) needs none, since disposed messages already carry records from
  their transitions. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — What does `life.quiesce` post to a unit holder?** (a) A `question` with subject
  `quiesce <ref>`, answered by `--mail ack`; (b) a new `quiesce` mail kind. (b) widens
  KICK-dKeptSession-5 S3's closed set of twelve, a parent change. Rung 3. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-63, TOOL-dWellOiledMachine-79.
- rev-3 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-84, TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam extended is the one compare-and-swap ref writer, `write_gov_ref` (TOOL-dPlacedRequest-11 S1,
extracted from `write_claim` at `tools/unattended/unattended.sh:2396`), which gains the door call, and
the record door `gov_record.py` (TOOL-dTotalRecall-2 S1), which gains the `door` verb; the closing
items reuse the lease verb's `--as withdrawn` (TOOL-dPlacedRequest-16 S2), KICK-dKeptSession-5's mail
verbs and record kind, and `run_hold` (`:6848`). The probe
`python tools/codebase-map/reuse_lookup.py "refuse a ref write whose path names another session than
the writer"` ranked `write`, `write_text`, `write_claim` and `extract_session` by name stem: `write_claim`
is the writer the parent already factors into `write_gov_ref`, and none of the rest binds a write to a
session, so no existing seam does the binding. Scout C's row cites `check_claim_writable` at `:2243`,
which holds at this base.

Recall terms used: `python tools/memory-recall/query.py "which writer may write or delete a
coordination ref, a mail ref or a lease tombstone" --terms "record door coordination verbs writer
binding mail ref tombstone lease holder take-over unlease prune"`
