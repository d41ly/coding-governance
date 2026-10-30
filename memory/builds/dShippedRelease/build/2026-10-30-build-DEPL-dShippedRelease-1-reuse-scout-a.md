**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14

# Reuse scout A — dShippedRelease

The scout's final return, extracted from its transcript by script, never retyped.

# Scout A: reuse return for units 1, 2, 4, 5, 13, 14

All paths are relative to `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d`. I read each cited line at HEAD `f4597719e`. Nothing was written to the repository and no scratch files were used.

- **Lookup:** I ran `reuse_lookup.py` on six behaviour sentences. It reported no recall-dark layers. Its useful hits were `read_landing_commit`, `write_claim`, `write_bar_green`, `check_landed_facts_due` and `read_missing_landed_facts`; the rest were name-stem noise.
- **Parents:** none of these surfaces exists at HEAD, confirmed for `tools/runtime/`, `tools/loop/`, `gov_record.py`, `record-kinds.toml`, `build_records.py`, `gov-ref.sh`, `lenses.toml` and `review_pin.py`. Each is cited by spec and section, and each is not built.
- **Packet:** it was re-rendered and staged during this scout, by something other than me. The change moves the as-built pin, `rendered at`, and the parents' "specs done" lines to yes. I read the earlier render, so its line numbers may be off by a few, but the Items, Owned nodes, Gaps and Policy keys content did not change.

## 1. One row per unit

### DEPL-dShippedRelease-1: the landing record

- **Seam:** `write_landed_observation` / `read_landed_observation` (`tools/unattended/unattended.sh:1661,1672`), reuse for keying a landing by commit; extend via `verb_landed` (`:6371`), after a home is chosen (fork 1).
- **What exists:**
  - a node-local line, `landed <commit> on <ref> at <tip>`
  - the lander marker (`tools/push-main.sh:354-397`)
  - the hook's allow and bar files (`:197,202`)
  - the close's frozen facts `units-at-landing` and `asks-at-landing` (`unattended.sh:11020-11027`)
  - `read_missing_landed_facts` (`tools/unattended/lib-unattended.sh:1782`)
- **Design:** flow-steps:439 gives the fields, layer-memory:430 the kind, memory-plan:219-220 the edges.
- **Owned nodes:** `item.deploy.record`, `record-kind.landing`.
- **Policy keys:** none of its own. It records `build.closes`, which has a row at `catalogue.toml:1064`.
- **Product paths:** `tools/unattended/unattended.sh`, `lib-unattended.sh`, `tools/push-main.sh`, the `tools/memory-tree/record-kinds.toml` row (TOOL-dTotalRecall-1), `HYGIENE.template.md`, `memory/guides/UNATTENDED-*`.

### DEPL-dShippedRelease-2: `deploy.distill` unarmed

- **Seam:** `test.seed`'s unarmed grammar, `# unarmed · <reason> · <sha>` (TOOL-dWitnessedBar-15 S2, not built), reuse for "measured nothing, never green"; extend via one landing-record field.
- **What exists:** no decision-log writer. `build.distill` is dScopedBuild's, and that build has 0 specs. TOOL-dLinkedLibrary-1:145,169 leaves both distill items out.
- **Design:** flow-steps:440, 448-450, 105-109.
- **Owned nodes:** `item.deploy.distill`.
- **Policy keys:** none.
- **Product paths:** a new `deploy.distill` verb beside the landing writer, plus its fixture.
- **Armed detection:** read the `[[stand-in]]` row (TOOL-dDeclaredLoop-13 S8) for `item.build.distill`.
- **Seen red:** the planted empty join must print `unarmed`, not green.

### DEPL-dShippedRelease-4: the deploy engine, `deploy.unlease` and mailbox closure

- **Seam:** `life.unlease` in TOOL-dWellOiledMachine-58 S9 (not built), reuse for the unit-lease, mail-copy and prune sequence; extend via `DOOR_CLOSING_VERBS` (S6) and a shared body with `--as` set to `landed`. Do not write a second closer.
- **What exists:**
  - `write_claim` (`unattended.sh:2396`)
  - the `refs/gov/runs` record (`:2077-2087`)
  - the in-place terminal write (`:6381-6384`)
  - the specced tombstone and queue refusal, TOOL-dPlacedRequest-16 S3, S5, S6
  - `read_mailbox` and the `mailbox-message` record, KICK-dKeptSession-5 S6, S12
- **Design:** flow-steps:84-90, 434-446.
- **Owned nodes (proposed):** `item.deploy.unlease`, `item.deploy.close`, `item.deploy.current`, `item.deploy.mandate`, `item.deploy.notify`, `item.deploy.snapshot`, `item.deploy.land` (gap-deploy-09's outcome classes), `record-kind.comparison`. `item.deploy.parents` goes to Scout B's -11.
- **Policy keys:** none of its own. It reads `leases.queued-claim-days` (`catalogue.toml:148`).
- **Product paths:** `unattended.sh`, `tools/push-main.sh` (the outcome record), `tools/runtime/gov_record.py` or its final home, `VERBS.template.md`, `STOPS.template.md`, `help/runtime.md`.

### DEPL-dShippedRelease-5: the `deploy.released` wait and the release arm

- **Seam:** `WAIT_KINDS` and `WAIT_OUTCOMES` in `waits.py` (TOOL-dWellOiledMachine-18 S6, S7, not built), reuse for the one sweep; extend via a new kind row, a new outcome row and an `OWNER_ITEM_KINDS` member (TOOL-dWellOiledMachine-48:134). Add no sweep and no clock.
- **What exists at HEAD:** nothing. `resume-tick.sh` has no deadline path.
- **Design:** flow-steps:443, 506-511; v2:1313.
- **Owned nodes:** `item.deploy.released`, `policy-key.build.closes`, `policy-key.build.release-hold`, `policy-key.build.release-ceiling`. `record-kind.release-exit` should sit with -15 (its writer `release.record`, layer-memory:434), and -5 only reads it.
- **Policy keys:** rows exist at `catalogue.toml:1064,1070,1076`. None of the three has `summary` or `usage`, so by the file's own rule each owes both and a drain of `unsummarised-keys.txt`.
- **Product paths:** `tools/runtime/waits.py`, `owner_items.py`, `waits_fixture.py`, `help/runtime.md`, and the lease path in `unattended.sh:6381-6384` (disagreement 5).

### DEPL-dShippedRelease-13: core checks on the landed tree and the patch filing

- **Seam:** `run_post_merge` (`tools/push-main.sh:427`) and `post-merge.sh` (`tools/run-gates/post-merge.sh:305,337`), reuse for the full bar on a landed SHA; extend via a keyed verdict beside `write_post_merge_record` (`:55`) and a filing step.
- **What exists:**
  - the detached start and per-SHA log (`push-main.sh:454-459`)
  - the `refs/gov/bar-red` publication, serialised by its lease (`post-merge.sh:375-397`)
  - the hook's reader (`.githooks/pre-push:1911-1974`)
  - the run record (`run-gates.sh:3481,5556`)
- **Design:** flow-steps:438, 446, 451-472; flow.md:628; foundations:366-376.
- **Owned nodes:** `item.deploy.core`.
- **Gaps:** gap-deploy-02 and gap-deploy-10.
- **Policy keys:** none owned. It reads `core.exceptions` (`catalogue.toml:35`, owner dOrderedCharter) and `flow.wait-ceiling`.
- **Product paths:** `tools/run-gates/post-merge.sh`, `tools/push-main.sh`, `.githooks/pre-push`, `tools/runtime/intake.py`.

### DEPL-dShippedRelease-14: the landing review blocks the close

- **Seam:** the `landing review` breakpoint (TOOL-dDeclaredLoop-19 S2, not built) and `review.dispose`'s declared unarmed route (TOOL-dDeclaredLoop-20:105,132), reuse for placement and disposal; extend via a close term in `deploy.close`.
- **What exists:** `closing-review-recorded` (`unattended.sh:11767`) is a pre-push item mapped to `item.build.ratify`, so it is not this seam. The harness kinds are `tools/workflows/tier2-review.template.js:190`. The role row is `tools/roles/workflows.toml:62`.
- **Design:** flow-steps:441-442, 494-495, 574; v2:705-708.
- **Owned nodes:** none. `item.deploy.recommend` is dDeclaredLoop's.
- **Gaps:** gap-deploy-06 in part.
- **Policy keys:** none owned. It reads `review.<stage>` (`catalogue.toml:1206`). `review.pin` is not a key.
- **Product paths:** `tools/workflows/review_pin.py`, the `deploy.close` verb, a `landing` review subject in the harness.

## 2. Where records and source disagree

1. **Close order is inverted.** Today `--close` runs before the push and commits LANDING on the graded merge (`unattended.sh:10703-10719`). flow-steps has `deploy.record`, `deploy.unlease` and `deploy.close` all after the push. `unattended.sh:6354-6357` calls a post-push commit "the one change no bar ever grades". No spec gives the landing record, the mailbox copies or the closing transition a route onto the default branch. TOOL-dWellOiledMachine-58 S5 also requires the copies to exist under `memory/builds/<slug>/` before a prune.
2. **`--close` and `deploy.close` are different acts sharing a name.** TOOL-dDeclaredLoop-11 maps `records-current`, `asks-disposed` and `parked-decisions-surfaced` to `item.deploy.record`, and `keepalive-reaped` to `item.deploy.unlease`. All four are graded before the landing they name (`unattended.sh:868`; compare `:11615-11619`).
3. **"The lander running the core checks" is not what the lander does.** It starts a bar and returns, and "does not check" whether it finished (`push-main.sh:43-47`). The undeclared case starts nothing (`:433`), and gov's `gate-env.sh` does not declare `GATE_POST_MERGE`. flow-steps:452 has `deploy.core` start the bar anyway, but the hook binds a red only where the key is declared (`pre-push:1911-1912`). So under undeclared, a published red binds no later push.
4. **flow-steps:469 cannot be followed as written.** It says to read the run record, but nothing maps a SHA to a run id:
   - the start record has no run id (`push-main.sh:458`)
   - the log names the record only on RED (`post-merge.sh:406`)
   - only the header's `head` key can join, by scanning `gate-run/*/header` (`run-gates.sh:2444`)
   - a REFUSED run makes no copy (`post-merge.sh:370`)
5. **TOOL-dPlacedRequest-16 S2 conflicts with cl-0508.** It turns the `landed` write at `unattended.sh:6383` into `released`, which hands the lease over at `--landed`. TOOL-dWellOiledMachine-60 S4 and the clause keep it live until `deploy.unlease`.
6. **The per-SHA verdict is not in dWitnessedBar.** The task implies it is. TOOL-dWitnessedBar-6 S4 is per-tree (`gate-verdict/<tree hash>`, absent at HEAD), `refs/gov/verdict/<sha>` is the peer's, and its §3 leaves `deploy.core` to this build. gap-deploy-02 is -13's to build.
7. **Clause order conflicts with the door.** The clause and flow-steps:445 name tombstones first, then the mailbox. TOOL-dWellOiledMachine-58 S5 needs the writer to hold the live lease to prune, so the mailbox must close first, as its S9 does.
8. **`life.unlease` is not reusable as specced.** S9 writes `withdrawn`, and it exits early on a `landed` tombstone with a message that goes stale once this lands. Its AC at spec:288 asserts `not-closing-verb` and flips when the name joins the tuple.
9. **TOOL-dWellOiledMachine-18 does not fit the release wait in three ways.**
   - S6 fixes the options to `keep-waiting` and `default`; the clause needs close-unreleased and wait-for-later-release, keyed by (build, landed SHA).
   - S5 never raises a `woken` wait. A prefix wake from an unrelated SHA's exit record ends the wait, and re-declaring restarts the clock, against "counted from the landing record or the owner's last keep-waiting answer".
   - S5 counts from the declaration's first sighting, not from the landing record.
10. **The patch filing has no working route.** TOOL-dWellOiledMachine-27 S1 offers origins `mailbox` and `cadence`. S3 says a cadence receipt never ratifies, and S4 refuses any placement but `breakpoint` or `ask` for such a request. So `deploy.core` cannot place a patch build as written, and "files a patch build before that build closes" fails. The post-close row is real but lives at flow.md:628, not in flow-steps `[entry]`.
11. **"The owner's alone" is contradicted by the default.** flow-steps:446 reserves the exception to the owner. `core.exceptions` defaults to `any-session-recorded`, and PLAY-dOrderedCharter-7 S9 admits any well-formed record. That record's fields (`Principle`, `Excuses`, `Reason`, `Expires`, `Caused-by`) carry no landed SHA, so the close cannot join an exception to its landing.
12. **`review.pin` passes no landing preset.**
    - It is an item with a stand-in (TOOL-dFairHearing-3 S8), not a catalogue key.
    - S8 maps spec and design subjects only.
    - `preset` is refused on `diff-review` (TOOL-dFairHearing-2 AC1).
    - A non-spec subject under `spec-audit` is treated as a design document (`tier2-review.template.js:428`).
13. **The default landing review places nothing.** TOOL-dDeclaredLoop-19:148-150 says `opt-in` places nothing with no per-build opt-in, and `review.deploy` defaults to `opt-in`. "Blocks the close" is vacuous at the default.
14. **The `landed` notice no longer follows the review.** TOOL-dWellOiledMachine-60 S2 and cl-0508 put the notice in the landing push. So flow-steps:442 and the breakpoint "before `item.deploy.notify`" gate nothing dependents see, and `deploy.notify` becomes a held-id no-op.
15. **Stale names and wording.** flow-steps:905 and :944 still say `deploy.release`. layer-expansions:97 and research-integrations-a:106 say the item deletes lease refs, which P40 superseded. cl-0415's "deploy engine" is v1's promotion engine (v1:139, flow.md:518), which v2 split into -6 and -15.
16. **cl-0413 is three words with no tokens.** The token arm cannot see it, so -1's spec must state the fields itself, which is the packet's own warning.
17. **`status: OPEN` is still at README:8.** Ask PLAY-dClosedLoop-31 says this refuses the first spec commit at `gen_build_index.py --write`.

Checked and still true: gap-deploy-09's exit table, and flow-steps:437's race behaviour under `GOV_PUSH_MAIN_MAX_RETRIES=1` (`push-main.sh:1000-1008`).

## 3. Shared interfaces, as proposed names

Within this group:

- `landing record`, keyed by landed SHA, fields:
  - `sha`, `builds`, `units`
  - `outcome` (`landed-gated|landed-ungated|already-held`)
  - `pre-push`, `core`, `patch-key`
  - `closes`, `distill`, `review`
- `read_landing <sha>`: the one reader, used by -2, -4, -5, -13 and -14.
- `distill: unarmed · <reason> · <sha>`: one field, same grammar as `test.seed`.
- `read_core_verdict <sha>` returning `verdict`, `published`, `run_id`: the gap-deploy-02 record, with verdict and publication kept apart.
- `run_unlease <slug> --as landed|withdrawn`: the shared body under `life.unlease` and `deploy.unlease`.
- `deploy.close` terms: `check_unleased`, `check_released`, `check_core_settled`, `check_landing_review`.

To other groups:

- **-15:** the release exit record ref or prefix, the `on` of the wait. Proposed `refs/gov/release-exit/`, with -15 as writer.
- **-12:** `deploy.land` admission before the push, and the outcome class after it.
- **-27:** `carries` as a landing-record field.
- **-3:** `read_landing` over a tag range.
- **-30:** the intake key `(default-branch-red, <sha>)` and `count_keep_waiting <build> <sha>`. The third answer parks the build, so -5 records the answers and -30 owns the rule.

To parents, to be added:

- wait kind `deploy.released` (or `release`)
- outcome `release-hold`
- owner-item kind `release-hold`
- a second wait kind for the close on a red landing
- an intake origin `landing` that ratifies through the originating build's mandate

## 4. Order constraints

Within this group: -1, then -2 and -13, then -4, then -5 and -14.

- -1 comes first because every other unit reads the record.
- -13 lands the verdict record that `deploy.record` copies.
- -4's `deploy.close` red-landing term needs -13, so -4 either splits its close term or follows -13.
- -5 needs -4's unlease and -1's anchor. Its exit record can be planted until -15 lands.
- -14 needs -1 as its subject and -4's close terms.

| Unit | Parent surfaces needed (none built) |
|---|---|
| -1 | TOOL-dTotalRecall-1 registry, TOOL-dPlacedRequest-11 `write_gov_ref` |
| -2 | TOOL-dWitnessedBar-15 grammar, TOOL-dDeclaredLoop-13 S8 stand-ins |
| -4 | TOOL-dWellOiledMachine-58, -60, -3; TOOL-dPlacedRequest-1, -15, -16, -17, -21; KICK-dKeptSession-5, -39 |
| -5 | TOOL-dWellOiledMachine-18, -48, -6, -25; TOOL-dPlacedRequest-17 |
| -13 | TOOL-dWellOiledMachine-27 (with change); PLAY-dOrderedCharter-7; TOOL-dWitnessedBar-6 |
| -14 | TOOL-dDeclaredLoop-19, -20; TOOL-dFairHearing-3, -13 |

Note that `parents:` omits dPlacedRequest, dKeptSession, dDeclaredLoop, dFairHearing and dOrderedCharter. They arrive only transitively, and the table needs them all.

## 5. Forks

I could not settle the first six from source.

1. **Where the landing record lives.** Options:
   - (a) a tracked file on a post-landing commit, which meets `:6356`'s objection
   - (b) a per-SHA ref written by `write_gov_ref` and projected into the trail
   - (c) a pre-push half in the tree and a post-push half on a ref

   Fork 2 below rests on this answer.
2. **What bar grades a post-landing records commit.** This covers the mailbox copies and the closing transition. It may be a rung 5 or 6 ruling because it touches an owner-set invariant.
3. **Who runs the post-push items, and in what order relative to `--landed`.** Options are driver verbs before `--landed`, or `--landed` deferring its lease write to `deploy.unlease` (disagreement 5). This is also what a second node must resume.
4. **The patch intake's origin and ratification** (disagreement 10). This is a change to a deferred parent spec, and it may need an owner ruling.
5. **The landing review's subject and preset** (disagreement 12). Options are `diff-review` over the landed range with default lenses, or a new subject kind.
6. **Whether exceptions are the owner's alone** (disagreement 11), and how an exception joins a landed SHA.
7. **The wait clock after a spurious wake.** My read favours declaring on an exact exit ref per SHA where possible, otherwise re-declaring with the remaining seconds. Either keeps the clause's clock and needs a -15 decision on the ref.
8. **The form of `deploy.core`'s verdict record.** A node-local `<common-dir>` file cannot be read by a second node after a take-over, so a ref distinct from `refs/gov/verdict/<sha>` looks required.
9. **The scope of "the deploy engine" in -4.** My read is the core `deploy.*` items only, with adapters and promotion left to -6 and -15.
