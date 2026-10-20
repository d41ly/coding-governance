**Serves:** spec-audit PLAY-dClosedLoop-1

# Shape audit, run A: gaps left in the converged dClosedLoop design

Tier-2 spec-audit, round 1, run A of two independent runs, written by the synthesis role (gov-synthesizer) from findings that adversarial skeptics confirmed. It answers the owner's question: "Can we review the entire design's shape for any gaps that may be left?"

Subjects (round 1): memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@0c6a17dc0401f64659f2da0880ef336a93893688, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@961cf79c163f6d12a0ce8873037daba0d8a8aa0a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md@9fe8384ef79b90cbe62d6d6ba0b4f340a1380894.

## Verdict: CLEAN WITH FIXES

The design has no blocker. It has four high defects: the receipt schema bump that launders a corrupt receipt past S9 (id 28), the Serves-kind rename with no reader inventory (id 29), the orientation-card retirement that leaves the write gate failing open (id 30), and an owner-only proof that an agent can produce itself (id 38). Each high must be fixed in the records before the owning build's spec is written. Item count by severity: 0 blocker, 4 high, 33 medium, 8 low, 45 items. Raw confirmed findings by severity: 0 blocker, 4 high, 33 medium, 8 low, 45 findings. The two counts are equal because no two findings could be merged. Ids 1 and 30 describe one defect, the orientation card retired with live consumers, but their binding grades differ (medium and high), so they stay as two items and each item cites the other.

## Review shape

Intensity full. Raw 49, confirmed 45, refuted 4, unverified 0 (0 uncertain), precision 0.92.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 14 | 14 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 7 | 6 | 1 | 0 | 0 | 0.86 |
| blast-radius | yes | 11 | 11 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 13 | 10 | 3 | 0 | 0 | 0.77 |

Run integrity: 5 of 5 lenses returned and none died. 5 of 5 skeptic batches returned and none died. No contradictory verdicts, orphaned duplicate refutations, spurious verdicts or duplicates were demoted or discarded. The run is complete.

Fixes on confirmed findings: 42 judged sound, 3 judged UNSOUND (ids 26, 27, 43), 0 with no fix proposed, 0 not judged. For each unsound fix, this report gives the skeptic's corrected fix.

Severity: 8 findings were re-graded by the skeptic (ids 1, 2, 7, 26, 27, 34, 39, 40), and 0 were left ungraded. Every grade below is the binding grade.

Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer. Intent: 28 spec documents were supplied as sibling context. Checklist: 17 items, each assigned to one lens (coherence 4, grounding 4, reuse 3, blast-radius 3, failure-envelope 3). By design: the caller's byDesign block. Move check: no checked subject moved. Lens notes were supplied for all five lenses.

Refuted, not reported: id 25 (covered by "as `<key>` says"), id 37 (dWitnessedBar's `test.seed` seeds the legacy population), id 46 (the floor raise was settled in AP-31 and AP-32), id 48 (the window pair rule bounds it).

In each item, v2 means the architecture-v2 record and plan means the memory-plan record.

## High

### H1. The receipt schema bump to 4 launders a corrupt receipt past S9 (id 28)

- **Where:** v2 [chain], the dShippedRelease row, "the receipt's schema 4 gaining steps, superseded, deprecations and prior_commit".
- **What:** At govkit.py:8946-8953, the gov_oid back-fill runs under `if schema < RECEIPT_SCHEMA:`. Its comment says the scoping exists so that a schema-3 receipt is never back-filled. Raising `RECEIPT_SCHEMA` to 4 sends every schema-3 receipt into the back-fill. The row names no reader by value. It also ships no upgrade step and no down step for the 3-to-4 change.
- **Consequence:** A text-merged schema-3 row that has `commit` and no `gov_oid` is filled from evidence before S9 runs, so the integrity check passes a corrupted receipt. A rollback below dShippedRelease has no down step for the receipt, so the down walk cannot be byte-identical.
- **Fix (skeptic: sound):**
  - Pin the back-fill to `schema < 3`.
  - Update the messages at govkit.py:5278 and :9007-9011, and the comment at :49.
  - Inventory the receipt's readers by value: govkit.py, the schema fixtures in matrix.py, and check-receipt.py.
  - Ship the 3-to-4 change as an upgrade step whose down step restores schema 3.
  - Probe: a planted schema-3 receipt whose row carries `commit` and no `gov_oid` is still red at S9 after the bump.
- **Gate:** A retirement-inventory leg that, for any changed constant or kind value, greps for readers by value and not only by name. This is the bug class retirement-inventory-misses-readers-by-value.

### H2. The Serves kind `journal` is renamed `log` with no reader inventory, alias or step (id 29)

- **Where:** The plan's [pockets] paragraph after the table, the v2 [chain] dTotalRecall clause "the Serves kind `journal` renamed `log`", and the plan's [migration].
- **What:** Live code reads and writes the value `journal`:
  - check-memory-hygiene.sh:3005 limits the AC-evidence ledger to `journal` records.
  - gen_build_index.py:550 lists it in `RECORD_KIND_TOKENS`.
  - runlog/record.py:82 and migrate_backlog.py:934/945 write it.
  - HYGIENE.md defines it at :575 and :597.

  [migration] rewrites no file, which leaves 1,443 gov records, and every adopter's records, on `journal`.
- **Consequence:** If the registry switches to `log` and the hygiene awk is not re-pointed, new `log` records skip the Evidences check silently. If the awk is re-pointed and no alias is kept, the 1,443 legacy records drop out of the check and out of the index's classification. In both cases adopters' records split across two kinds.
- **Fix (skeptic: sound):**
  - Add a unit to dTotalRecall that inventories every reader and writer of `journal` by value: the sites above, the conf example and the test fixtures.
  - Either declare `journal` a read alias of `log` in the registry, or ship the rename as an upgrade step with a down step.
  - Probe: a `log` record with a malformed AC line reds the Evidences ledger.
- **Gate:** The same by-value reader inventory leg as H1.

### H3. Retiring the orientation card leaves the write gate's route check failing open (id 30; see also M1, id 1)

- **Where:** The plan's [pockets] row "orientation cards … retired into the session binding … dWellOiledMachine", the plan's [chain] table, and the v2 [chain] dWellOiledMachine and dOrderedCharter rows.
- **What:** The plan retires the per-session `<git-common-dir>/orientation/<id>.md` into the session binding, but no v2 clause carries that retirement or names scratch-guard. Three places in scratch-guard.js use the card:
  - :671 reads the card.
  - :775 returns a witness, not a deny, when the card is absent.
  - :1182 builds the route notice from it.

  The fates record marks scratch-guard STAYS, while the card writer is reshaped into dOrderedCharter's per-worktree card.
- **Consequence:** Once the writer moves or the card retires, every write passes with only "orientation card absent" as a witness. The route check then certifies nothing, no leg goes red, and the injected route notice goes stale.
- **Fix (skeptic: sound):**
  - Add a clause to dWellOiledMachine, or to the build that moves the card writer, that retires the per-session card.
  - In the same unit, re-point scratch-guard.js's card and route reads (:671, :1182) to the session binding.
  - Add the matching row to the plan's [chain].
  - Probe: a planted session with a binding and no legacy card has a misrouted write denied, not witnessed.
- **Gate:** A fates-conformance arm that reds a RETIRED or RESHAPED pocket while any STAYS consumer still reads its path.

### H4. Owner-only actions are proven by signals the agent can produce itself (id 38)

- **Where:** The v2 [policies] rows `policy.proof` and `instructions.proof`, v2 [witnesses], the v2 [chain] dGroundRules minimal guard, and dDeclaredLoop's "the guard, the TTY CLI".
- **What:** The default proof, `tty-cli`, which presets never touch, has three parts:
  - an interactive-terminal confirmation;
  - a plain-text trailer;
  - a guard that refuses only agent writes.

  An agent's Bash call can get a TTY (`/usr/bin/winpty` on this node, `script` or Python's `pty` on Linux). The trailer is ordinary commit text. Shell writes escape the write and role gates (gap-build-03, gap-roles-03). No record states a threat model for owner-only actions.
- **Consequence:** An agent routing around a refusal can change `policy.guard`, the floor or `verdict.remote.pin`, or forge an owner disposition. The push gate then certifies the change as the owner's act.
- **Fix (skeptic: sound):**
  - Add a threat model for owner-only actions to v2.
  - Have dGroundRules's minimal guard and dDeclaredLoop's guard state what proves the owner beyond a TTY in a session an agent shares. Options: a signed trailer whose key no agent process can read, or a confirmation outside the harness process tree.
  - Refuse shell writes to the policy file, its mirror and the manifest.
  - Probes: from an agent Bash call, `winpty gov policy set …` and `python3 -c 'import pty; pty.spawn([...])'` are each refused. A planted commit with a hand-typed proof trailer is refused at the push.
- **Gate:** An owner-proof adversarial fixture in the policy guard's leg that runs those probes. Also a checklist entry: every proof of owner action names the agent capability it excludes.

## Medium

### M1. Retiring the orientation card has no clause and no consumer re-point (id 1; see also H3, id 30)

- **Where:** The plan's [pockets] row "orientation cards" (owner dWellOiledMachine), and the v2 [chain] dWellOiledMachine and dPlacedRequest rows.
- **What:** No chain clause carries the retirement. Two live consumers are left as they are: scratch-guard.js:671 reads the card, and skills/session-kickoff/manifest-check.sh:19 writes it (`--card --write`). dPlacedRequest's card clause covers a per-build ref only. gap-orient-19 counts as closed although neither consumer is touched.
- **Consequence:** The likely outcome is that the old card lives on beside the binding as a second home for the session's route.
- **Fix (skeptic: sound):**
  - On dWellOiledMachine's row, retire the per-session card into the session binding.
  - In the same unit, re-point scratch-guard.js's orientation check and manifest-check.sh's `--card --write` to the binding.
  - Probe: a staged session with no `orientation/<sid>.md` whose routed edit scratch-guard still decides from the binding, seen red before the re-point.
- **Gate:** The fates-conformance arm in H3.

### M2. The causes, pins and orphan arms have no legacy population (id 2)

- **Where:** The plan's [gates] causes and pins arms, [practice] "pinned facts", and [migration].
- **What:** Three arms run over every record:
  - a quoted derived fact with no pin;
  - a non-root record with no `caused-by`;
  - an orphan no root reaches.

  Only `positional` is held shrink-only. [migration] backfills neither causes nor pins. Today the tree has 3 files with Caused-by and 2,642 unpinned "N of M" counts. No chain clause builds the orphan check.
- **Consequence:** The arms either red the whole tree or are quietly narrowed to new records, certifying a scope they never declared. The orphan arm has no owner.
- **Fix (skeptic: sound):**
  - Give each arm a keyed shrink-only legacy population, as `tags.positional` has, or scope it to records written through `record` from a declared commit.
  - Add an orphan-check clause to dTotalRecall's row.
  - Add a [migration] line saying how a legacy record's cause is read: derived from its Serves unit, or held as the population.
- **Gate:** A registration rule that refuses a new check arm with no declared population.

### M3. `record` refuses a missing cause before any root kind exists, and no stand-in is declared (id 3)

- **Where:** The v2 [chain] dTotalRecall row ("refusing a missing cause on a kind that is not a root") against dWellOiledMachine's row.
- **What:** The root kinds are the intake, the session binding and the cadence lease. The intake and the binding land in dWellOiledMachine, a child of dTotalRecall, and the cadence lease lands in dTendedCadence. The H2 rule requires a stand-in for each dependency on a later build, and none is declared here. dPlacedRequest does declare one for its claim commit. [sites] already lets Made-by name `owner`, so the missing root is the open defect, not Made-by.
- **Consequence:** Between the two builds landing, every non-root write is either refused or given an improvised cause.
- **Fix (skeptic: sound):**
  - Declare the stand-ins on dTotalRecall's row: Made-by takes `owner` or the build lease until acts exist, and the build README or the claim commit serves as an interim root kind.
  - Name the unit in dWellOiledMachine that drains them.
- **Gate:** A chain-order check that reds a clause depending on a later build's kind with no declared stand-in.

### M4. "Five doors, and nothing else writes a node" contradicts the plan's own writers (id 4)

- **Where:** The plan's [doors] and [practice] "one door", against [sites] and [pockets].
- **What:** The same record names writers outside the five doors:
  - the builder (code);
  - dTotalRecall's registry (registry rows);
  - the lease verbs and the mailbox (refs);
  - the release (kit-release tags);
  - the renderers (views).
- **Consequence:** The one-door check either reds the lease CLI, the mailbox, the lander's tags and every builder annotation, or is narrowed to whatever passes. One rule then gives two answers about who may write a node.
- **Fix (skeptic: sound):**
  - Make [doors] list every door, or state that the check covers only the five site kinds it names.
  - Derive [practice]'s check from that one list.
- **Gate:** A one-door check whose door list is read from [doors], so the rule and the check cannot drift. Bug class: two-answers-to-one-question.

### M5. `trace.identity: salted` is selectable but undefined (id 5)

- **Where:** The v2 [policies] `trace.identity` row, the plan's [keys] and [gates] commits arm, and the v2 [chain] dWellOiledMachine row.
- **What:** No record defines what `salted` writes, which salt it uses, or where the salt lives. The commit-key leg defines refusals only under `act-only` and `session`.
- **Consequence:** Under `salted`, a builder invents a secret-handling design, and the leg passes any `Gov-Session` unchecked.
- **Fix (skeptic: sound):**
  - Define `salted` in the catalogue row: what the trailer carries, where the salt lives (the node's credential store), and the leg's refusals under it.
  - Or ask the owner whether to drop the value.
- **Gate:** A catalogue check that reds an allowed value no chain clause or leg arm names. Bug class: policy-value-with-no-route.

### M6. P35's `not-local` and `pruned` states and the `transcript=` pointer have no unit (id 6)

- **Where:** v2 [principles] P35, the v2 [chain] dWellOiledMachine row, and the plan's [sessions] and [pockets].
- **What:** The act-key clause lists item, work order, harness, harness session, node and cause, with no transcript pointer. The trace clause cites P35 but names neither state, and no arm or fixture requires them.
- **Consequence:** `gov trace` and `gov why` render another node's transcript, or a pruned journal, as empty or as an error. Claude's and Codex's transcript witnesses are joined by no key.
- **Fix (skeptic: sound):**
  - Add the binding's `transcript=` pointer to the act-key clause.
  - Make the trace clause render each row as filled, `not-local: node <x>` or `pruned`, each state seen on a planted fixture.
- **Gate:** A principle-registry meta-check that reds a principle whose named states appear in no chain fixture.

### M7. The plan declares the `reads` and `writes` edges at two sites (id 8)

- **Where:** The plan's [edges] `reads` and `writes` rows ("declared at the kind's registry row"), against [pockets] role definitions and [integration] roles.
- **What:** The edges are declared at dTotalRecall's registry row and also derived from dBoundRoles' role definitions. This breaks the plan's own rule "declared once at the site that owns its fact".
- **Consequence:** The two copies can disagree silently, and the edge checks cannot tell which one is the fact.
- **Fix (skeptic: sound):**
  - Pick one site and render the other from it.
  - State the derivation in [edges] and in the owning chain clause.
- **Gate:** A render-parity check between the registry's readers and writers and the role definitions. Bug class: two-answers-to-one-question.

### M8. P33 and the namespace registry cannot address acts, sessions, commits or landings (id 9)

- **Where:** v2 [principles] P33, the v2 [chain] dOrderedCharter row (namespace registry, per-tree index), and the plan's [frame] and [edges].
- **What:** P33 says every node is named by a tag, while [frame] allows a tag, a section or a native id. No namespace is registered for act, session, commit or landing. The one index is a per-tree file that cannot hold node-local acts or sessions.
- **Consequence:** The namespace arm either reds every `runs-in`, `made-by` and `follows` edge or skips native ids unchecked. `gov trace <key>` has no index row for an act or a session.
- **Fix (skeptic: sound):**
  - Amend P33 to the three address forms.
  - Register the native-id classes with owners: dDeclaredLoop for commits, dWellOiledMachine for acts and sessions, dShippedRelease for landings.
  - State on dWellOiledMachine's row how node-local nodes join, or are read beside, the per-tree index.
- **Gate:** An edge check fixture planting one edge per address form.

### M9. P34's rationale rule has no check, and the plan's `owned` collides with the tags-pack `owned` (id 10)

- **Where:** The plan's [practice] table (`owned`, `retired`, render parity) against the v2 [chain] dOrderedCharter row and P34.
- **What:** Three practice rules are carried more narrowly than written:
  - dOrderedCharter's clause omits "rationale kept apart from what loads", and no unit builds render parity.
  - The plan's `owned` ("one owning build or layer per node") reuses the name of the systems tags-pack check, which reds only `item.build.x` expansions.
  - `retired` covers tags but not sections.
- **Consequence:** The existing `owned` check will be read as proving one owner per node, which it does not check. Rationale can still render into load sets with no arm to catch it.
- **Fix (skeptic: sound):**
  - Add "rationale apart" and its render-parity arm to dOrderedCharter's writing-practice clause.
  - Give the one-owner check its own name and owning unit, or widen the systems `owned` check explicitly on dOrderedCharter's row and state the new red case.
- **Gate:** A check-name registry that refuses a second definition under an existing check name.

### M10. P37 promises a leg for paths, temp files and quoting that no unit builds (id 11)

- **Where:** v2 [principles] P37, and the v2 [chain] dOrderedCharter and dWitnessedBar rows.
- **What:** dWitnessedBar's portability pack builds legs for line endings, encoding, launch and the interpreter floor. Nothing in the pack, or in gate-legs.json's 140 entries, covers paths, temp files or quoting.
- **Consequence:** Three of P37's seven rules ship with no leg, against the principle's "each rule with its leg".
- **Fix (skeptic: sound):**
  - Add path, temp-file and quoting arms to the portability pack.
  - Or record those three rules as declared without a leg, with the meta-check exemption stated.
- **Gate:** A principle-registry meta-check that reds a rule with neither a leg nor a declared exemption.

### M11. Nothing walks the owner's cycle end to end (id 12)

- **Where:** The plan's [frame] "The plan closes every hop" and [cycle], against [gates] and the v2 [chain] rows.
- **What:** [gates] checks edges one at a time, and the fixture replays four events. Nothing walks the fourteen [cycle] hops by key on a real build.
- **Consequence:** Each unit can pass its own arm while the cycle stays broken at a hop no arm owns, such as landing to verdict or bug class to unit. The owner's directive would be certified only by prose.
- **Fix (skeptic: sound):**
  - Add a cycle-walk acceptance to [gates], owned by the last build that closes a hop: from a planted build's intake, walk every hop by key, and red on any hop resolved by search or prose.
  - Name it on that build's [chain] row.
- **Gate:** The cycle-walk leg itself.

### M12. The kickoff's per-machine skill link has no fate, owner or upgrade path (id 15)

- **Where:** The v2 [chain] dSafePassage, dShippedRelease and dConvergedCharter rows, and P38.
- **What:** WIRE-INTO-PROJECT.md:69-86 links `~/.claude/skills/session-kickoff` to gov's live checkout, outside any repository. `update` walks repository receipts only.
- **Consequence:** The link serves gov's working tree whatever the receipt says, which bypasses release tags. Once the skill directory moves, the link dangles on every machine while the write gate still names `/session-kickoff` as its remedy. dConvergedCharter's exit check goes green regardless.
- **Fix (skeptic: sound), for the owner:**
  - Add a fates row for the per-machine link and place its owner in [chain].
  - Have dSafePassage or dShippedRelease declare node-level install surfaces as an upgrade-step surface.
  - Check the link per node, as a node-registry row or a dWellOiledMachine preflight.
  - Widen dConvergedCharter's exit check to node surfaces.
  - Probe: a planted node whose link targets a removed skill directory goes red.
- **Gate:** The per-node install-surface check above.

### M13. The `help/` pages and the `[docs]` rule have no pocket, fate or owner (id 16)

- **Where:** The plan's [pockets] and the v2 [chain] dConvergedCharter row.
- **What:** `help/` is shipped (HELP_DIR in playbook.kit.toml), and AGENTS.md:38 binds the [docs] rule. The chain rewrites `/build`, the roles and `--scaffold`, which help/roles.md describes, but no unit keeps that page current.
- **Consequence:** P34's "every pocket is a node or a witness" fails for this pocket, and both the atlas view and the fates join pass with the page stale.
- **Fix (skeptic: sound):**
  - Add a [pockets] row (family, level or kind, feature-tag key, owner) and a fates row.
  - Name the build that keeps each page current, for example dConvergedCharter rendering the pages from units' `help` fields, or a check tying each changed user-facing command to its page.
  - If this needs a new kind, it goes to the owner.
- **Gate:** A docs leg that reds a changed user-facing command whose help page is unchanged.

### M14. Transcript retention is stated as 365 days, but that is one node's setting (id 17)

- **Where:** The plan's [pockets] row "Claude transcripts", and [sessions].
- **What:** 365 days is this node's user-level `cleanupPeriodDays`. The harness default is 30 days, and nothing gov ships sets or checks it. `runtime.journal` keeps journal lines for 60 days.
- **Consequence:** On a node left at the default, transcripts are pruned before the journal lines that point at them, so traces older than 30 days render `pruned`.
- **Fix (skeptic: sound):**
  - Restate the cell as "the node's `cleanupPeriodDays` (365 here, default 30)".
  - Give retention an owner: either a measured row in dWellOiledMachine's conformance fixture and node registry, with a preflight warning when it is below `runtime.journal`, or an install setting under `install.guards`.
  - Do the same for Codex rollouts.
- **Gate:** The preflight warning above.

### M15. The bash resolver ignores the execution-based resolvers that already exist (id 19)

- **Where:** The v2 [chain] dWitnessedBar row, "one bash resolver in `tools/lib` with its JavaScript twin" (AP-33), and gap-tool-20.
- **What:** The design never names the existing resolvers:
  - `profile_bar.resolve_bash`, which runs each candidate, honours `GOV_BASH`, and is reused by regen.py in the bar;
  - drift-audit's `resolve_bash_shell`;
  - process-monitor's `resolve_launcher`.

  The new resolver trusts a derived path, although process-monitor/selftest.py:1099-1102 records a Git usr/bin bash executing as WSL on this node.
- **Consequence:** Four resolver definitions remain, so the copied-resolver class stays open. The new resolver can pick a WSL bash, and it drops the `GOV_BASH` override.
- **Fix (skeptic: sound):**
  - Extend `tools/run-gates/profile_bar.py:resolve_bash`.
  - Derive the population by a query over `def resolve_bash|def resolve_launcher|def resolve_bash_shell` and the bare-bash loop.
  - Accept a candidate only once it runs (for example `uname -s` answering MINGW or MSYS).
  - Acceptance: a staged WSL-first break that goes red.
- **Gate:** A copied-resolver population leg keyed by that query.

### M16. `gov trace` and the "one reader" duplicate runlog's model and its `Decided:` reader (id 20)

- **Where:** The plan's [doors] `gov trace`, the plan's [integration] flow row, and the v2 [chain] dWellOiledMachine and dDeclaredLoop rows.
- **What:** `tools/runlog/model.py:build_run_model` already joins journals, git, run state and transcripts into a timeline with cost, and `read_git_range` already reads `Decided:`. The fates record keeps the model as STAYS, and no unit re-points it.
- **Consequence:** gov ships two timeline engines and two `Decided:` readers, so the "one reader" claim is false on landing.
- **Fix (skeptic: sound):**
  - Name `build_run_model` in dWellOiledMachine's trace clause and state its fate. Either it reads through the core reader once that lands (a re-point unit on dTendedCadence), or it is the pre-chain backfill reader that `gov trace` falls back to.
  - Add `read_git_range` to dDeclaredLoop's inventory of readers to re-point.
- **Gate:** A trailer-reader population leg keyed by a query for trailer parsing sites.

### M17. An edited retired file reuses the `forked` role, whose contract does not fit (id 21)

- **Where:** The v2 [chain] dShippedRelease row ("kept as a `forked` row with an order"), and v2 [policies] `install.retired-edits`.
- **What:** govkit's `forked` means "gov's copy is a derivative of the target's". It copies `FORK_RULE_KEYS` from a descriptor rule that a retired file no longer has, and dispatches to `report`. The existing `VERDICT_GRID` cell `("differs","absent")` already covers this case.
- **Consequence:** The rule lookup finds nothing, and the INCOMPLETE arm and `UNLANDED_REASON` describe the file wrongly. A later change to either meaning breaks the other.
- **Fix (skeptic: sound):**
  - Extend the `("differs","absent")` cell with the order arm.
  - Name the state on its own, for example `retired-edited`, with its own `UPDATE_ROLE` and `UNLANDED_REASON` rows, so selfcheck arm 7g covers it.
  - Reuse the `withdrawn` arm's outbox order.
  - Check: a planted row of the new state is not graded as a fork by arm 3c.
- **Gate:** Selfcheck arm 7g, which reds a receipt state with no role row.

### M18. Two builds each build a record finder (id 22)

- **Where:** The v2 [chain] dLinkedLibrary row ("memory-recall narrowed to a record finder") and dTotalRecall row (`record find` and `record show`).
- **What:** The fates record gives the finder to both builds (:47 and :118). No row says what memory-recall still finds that `record find` does not.
- **Consequence:** A core finder and an optional finder answer the same question, and spec writers cannot tell whether query.py is reused or retired.
- **Fix (skeptic: sound):**
  - Give the finder one clause on one row. Either dTotalRecall absorbs query.py's reshape, as fates :118 says, and dLinkedLibrary names what memory-recall keeps (bench, union, "why" search) or its retirement; or dLinkedLibrary owns the finder and dTotalRecall drops `record find`.
  - Align the fates row.
- **Gate:** A fates check that reds a surface named by two owning builds.

### M19. Two builds each spec a write-set bug-class selector, and neither names gotchas.py (id 23)

- **Where:** The v2 [chain] dLinkedLibrary row ("gotchas handed by write set") and dFurnishedOrders row ("bug classes rendered as a core field by the unit's write set").
- **What:** `tools/memory-tree/gotchas.py --for-paths` already selects bug classes by write set. The ownership and layer-memory records name dTotalRecall and dLinkedLibrary as owners, which with the two rows makes three owners for one behaviour.
- **Consequence:** A third selector appears, and a builder's work order and a reviewer's checklist can select different classes.
- **Fix (skeptic: sound):**
  - Keep one clause: dFurnishedOrders renders the field and names `gotchas.py --for-paths`, or `record find --kind bug-class --paths`, as its selector.
  - Strike or narrow dLinkedLibrary's clause.
- **Gate:** The two-owner fates check in M18.

### M20. P38 has no check that reds a missing upgrade step (id 26)

- **Where:** v2 [principles] P38, the v2 [chain] dSafePassage row, and the fates record's [check].
- **What:** The `upgrade-walk` leg proves only steps that were declared. The two arms the supersession research proposed are absent from v2, the away pass and fates: one for a registry removal with no `[[retired]]` row, one for an adopter-visible fates row with no step.
- **Consequence:** A build can remove a registry entry, and every adopter's `update` then refuses whole (gap-deploy-15 recurs). It can also change a command, hook or conf surface with no step. dConvergedCharter's exit check cannot see a step that was never written.
- **Fix (skeptic: UNSOUND; the skeptic's corrected fix):**
  - Add the registry arm to dSafePassage's row: every entry removed from tools/govkit/registry.toml has a `[[retired]]` row, seen red on a planted removal.
  - Add a declared column to the fates `[table]` saying whether each row's surface is adopter-visible, from a closed set such as `adopter` or `internal`, checked for presence on every row.
  - Then add the fates arm: every RESHAPED, MERGED or RETIRED row marked `adopter` names a step id or a `[[retired]]` row, seen red on a planted row with neither.
  - Join both arms into the fates `[check]`.
- **Gate:** The two arms above. Bug class: rule-stated-with-no-check-that-fails.

### M21. Four builds that change adopter surfaces declare no upgrade step, and recovery lands late (id 27)

- **Where:** The v2 [chain] rows of dDeclaredLoop, dTotalRecall, dLinkedLibrary and dWellOiledMachine, and the dShippedRelease row's recovery clauses.
- **What:** Only dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter carry step clauses. Four other builds change adopter-visible surfaces:
  - dDeclaredLoop retires `REVIEW_ROUNDS`, an optional key in the unattended kit's adopter conf.
  - dTotalRecall replaces `--new-build` and `--new-spec` with `record` and renames the Serves kind.
  - dLinkedLibrary retires `reuse_lookup.py` and its agent, which ship in codebase-map.
  - dWellOiledMachine repacks the hooks, without the steps and the `/unattended` shim the research assigned it.

  Hook unwiring, retired-edit orders and stale-lock reclaim all sit on dShippedRelease, after dWellOiledMachine.
- **Consequence:** An adopter updating between dOrderedCharter and dShippedRelease keeps a withdrawn hook wired, sees an edit to a retired file read as `patched`, gets only a report for a moved conf key, and meets retired commands with no shim.
- **Fix (skeptic: UNSOUND; the skeptic's corrected fix):**
  - Give each of the four rows its own clause, "its own upgrade steps: …", naming the surfaces it changes: the REVIEW_ROUNDS conf key, the scaffold verbs and the Serves kind, reuse_lookup and its agent, and the hook repack with its `/unattended` shim.
  - Put the ordering gap to the owner as an open structural question, not as a move: either move the hook-unwiring and retired-edit units forward, or hold adopters at dSafePassage's release until dShippedRelease lands.
- **Gate:** The fates arm in M20.

### M22. The runaway ceiling is read from a file that retires (id 31)

- **Where:** The v2 [policies] row `review.design.round-count`, the v2 [chain] dDeclaredLoop clause "a planted round count at the runaway ceiling refused", and dConvergedCharter's unattended retirement.
- **What:** `RUNAWAY_CEILING` is defined only in tools/unattended/unattended.sh:774 and read by check-unattended.sh. Both files retire at dConvergedCharter, and no unit moves the constant.
- **Consequence:** After the retirement, the schema bound and the refusal read a deleted constant, so the bound is either unreadable or silently gone.
- **Fix (skeptic: sound):**
  - Add a dDeclaredLoop clause moving `RUNAWAY_CEILING` into the loop kit's definition or dGroundRules's schema.
  - Re-point unattended.sh:774/783 and check-unattended.sh:624 to it.
  - Reword the catalogue row to cite the new home.
- **Gate:** The by-value reader inventory leg in H1, run over every retired file's exported names.

### M23. The deprecation window is counted in releases before any release exists (id 32)

- **Where:** The v2 [policies] `install.deprecation-window`, the [presets] pair rule, the v2 [chain] dSafePassage shim, and dOrderedCharter's `map_lib` deprecation.
- **What:** The first release is cut only in dShippedRelease (gap-deploy-11). The pair rule ties the window to `currency.max-behind`, which dShippedRelease also builds.
- **Consequence:** A shim declared early either never closes its window or closes on an undefined count. dConvergedCharter's "every shim removed when its window closes" has no trigger for those shims.
- **Fix (skeptic: sound):**
  - In dSafePassage's row, define what counts as a release before tags exist (for example, landings on the default branch, or gov commits).
  - Or record that windows start at the first cut release.
  - Cover the counting in the shim's planted-path test.
- **Gate:** The shim's planted-path test with that counting.

### M24. "gov runs every step on itself first" has no mechanism until dShippedRelease (id 33)

- **Where:** v2 [principles] P38, the v2 [chain] dShippedRelease row, and gap-deploy-20.
- **What:** Only dShippedRelease's lander runs "each new" step on gov's tree, and gov cannot `update` itself until then. Earlier steps, such as dOrderedCharter's agent-instructions move and `map_lib` deprecation and any dWellOiledMachine hook step, never run on gov.
- **Consequence:** Steps reach adopters without having migrated gov first. gov's source-mode receipt starts without them, so the fleet view and the exit check cannot show gov converged.
- **Fix (skeptic: sound):**
  - Either move the step-run unit and the gap-deploy-20 fix into dSafePassage.
  - Or add a dShippedRelease clause that back-runs, and records in gov's receipt, every step declared since dSafePassage.
  - Witness: gov's receipt lists every declared step id.
- **Gate:** The witness above as a leg.

### M25. The lander's own commits are neither a commit site nor an exemption (id 35)

- **Where:** The plan's [sites] commit row, [doors] "the commit queue writes the trailers", and [gates] commits, and the v2 [chain] dWellOiledMachine commit-key leg.
- **What:** push-main.sh makes four kinds of commit and pushes them through the pre-push hook:
  - the prepared merge (:878);
  - the reconcile merge (:1067);
  - `mint:` (:1089, `--no-verify`, `Pass: none`);
  - `regen:` (:1108, `--no-verify`, `Pass: none`).

  Neither of the commit site's two doors covers them.
- **Consequence:** Every landing's own commits are either refused at the push or filed as findings forever, unless an undeclared carve-out opens a door outside the one-door rule.
- **Fix (skeptic: sound):**
  - Declare the lander as a commit site in [sites] and [doors], writing `Gov-*` trailers from the act binding it runs under.
  - Or declare lander commits a keyed exemption with its own arm.
  - Probe: push a landing with mint and regen commits under `commits.edge-check: push-leg`.
- **Gate:** The probe above as a lander fixture.

### M26. Codex hook trust is surfaced at install only, not when an update changes a hook (id 39)

- **Where:** The v2 [chain] dShippedRelease row ("Codex install targets with their trust step surfaced") and the dWellOiledMachine preflight.
- **What:** Codex trusts hooks by hash, so a new or changed hook entry is skipped until the owner trusts it again. The preflight refuses only a launch that skips hooks or permissions.
- **Consequence:** After an update, a Codex act runs with the changed enforcement hooks silently skipped, which defeats `runtime.hook-failure: closed`.
- **Fix (skeptic: sound):**
  - Have each update that changes a Codex-installed hook surface the re-trust as an owner item.
  - Have dWellOiledMachine's preflight refuse a Codex launch while any registered pack hook's hash is untrusted.
  - Add a conformance-fixture row: a hook edited after trust is seen skipped, and the launch is refused.
- **Gate:** That conformance row.

### M27. The commit-key leg, Maintain's reading and `carries` name no range shape and no outcome for a foreign binding (id 40)

- **Where:** The plan's [gates] commits bullet, and the v2 [chain] dWellOiledMachine commit-key leg, dTendedCadence's reading and dShippedRelease's `carries`.
- **What:** Bindings are node-local and pruned after `runtime.journal`. A push carries merged-in default-branch commits, other nodes' act commits and legacy commits. dScopedBuild pins `--no-merges -M`, but these sites pin no range.
- **Consequence:** A build that merges main, moves nodes (P22) or resumes after retention is falsely refused at the push. If a builder skips non-local bindings instead, a forged `Gov-Act` passes.
- **Fix (skeptic: sound):**
  - Name the range as `<current default>..HEAD` with `--no-merges`, never a frozen base.
  - State the outcome for a non-local or pruned binding: a committed act record it can verify against, or a declared not-local outcome that never passes a forged key.
  - Probes: a branch that merges main containing another node's act commits is green; a planted `Gov-Act` naming no act is red.
- **Gate:** A checklist entry and a leg arm requiring every commit-range reader to declare its shape.

### M28. Set-valued keys accept the empty set (id 41)

- **Where:** The v2 [policies] rows `transitions.record`, `card.store`, `tests.landing-levels` and `platforms.supported`.
- **What:** Each row allows "any subset", and the schema refuses only out-of-set values. The answers fold refused empty for `runtime.act-auth` only, one instance of a class.
- **Consequence:**
  - An empty `transitions.record` switches off a [floor] invariant through an ordinary key.
  - An empty `card.store` breaks P22's pick-up on any node.
  - An empty `tests.landing-levels` lands on a Test verdict that ran no level.
- **Fix (skeptic: sound):**
  - State for each set-valued key whether empty is allowed.
  - Have dGroundRules's schema refuse empty for these four, each seen red on a planted empty value, or route an empty `transitions.record` through the floor's guard.
- **Gate:** A schema check that reds a set-valued key with no declared empty-set rule.

### M29. The edge-line grammar contradicts itself and cannot carry a section target (id 42)

- **Where:** The plan's [sites] record-section row and the paragraph below it, and [frame] node addresses.
- **What:** One line says "at most one line `**Edges:** …`", and the next paragraph says "one line per type". A section address, `<doc> [<seg>]`, contains a space, so a whitespace-split `type=target` line cannot carry it.
- **Consequence:** A parser built to either rule refuses or drops what the other allows, and the target-resolves gate reds valid section edges.
- **Fix (skeptic: sound):**
  - State the line rule once.
  - Give section targets an unambiguous form, for example `<doc>#<seg>` or a quoted target.
  - Check both, each seen red on a planted multi-line section and a planted section target.
- **Gate:** Those planted fixtures in the edge parser's leg.

### M30. The update walk has no route for a step that fails or is killed partway (id 43)

- **Where:** The v2 [chain] dSafePassage row (update walk, down steps, recorded rollback) and dShippedRelease's "a stale lock reclaimed".
- **What:** Nothing says whether the receipt advances per step, or how a half-applied step whose witness is false is re-entered. The upgrade-walk leg tests only clean runs.
- **Consequence:** A crash mid-walk, in an adopter or in gov's prepared merge, leaves a tree no step describes, and the next `update` re-runs up over partial state.
- **Fix (skeptic: UNSOUND; the skeptic's corrected fix):**
  - In dSafePassage's row, declare a forward-recovery route.
  - The receipt advances per completed step. A failed or signalled up leaves earlier steps applied and stops the walk with a recorded failure.
  - Each step's up must be re-runnable over its own partial state, its witness false until it completes.
  - Rollback stays the explicit recorded rollback, and its downs must also tolerate a partial up.
  - Add an upgrade-walk arm that kills a planted step between two writes and sees the re-run reach the target green, and the rollback from that state reach release-0 byte-identical.
- **Gate:** That kill-midway arm.

### M31. Released `[[upgrade]]` rows can be edited or removed (id 44)

- **Where:** The v2 [chain] dSafePassage row: the upgrade-step kind and the `[[upgrade]]` row.
- **What:** Nothing freezes a step that a release carries.
- **Consequence:** An adopter whose receipt records a removed step can never run its down, and an edited down argv no longer reverses the up that ran. The walk leg stays green.
- **Fix (skeptic: sound):**
  - Register step rows as a dWitnessedBar append-only population keyed by step id, with id, introducing commit and argv frozen once released.
  - Make a correction a new step, and a removal a `[[retired]]` row with its successor.
  - Seen red on a planted removal of a released step.
- **Gate:** That append-only population.

### M32. Upgrade steps are a target-side spawn class outside the offer mode's list (id 45)

- **Where:** The v2 [chain] dShippedRelease row, "kits.offer running the steps that need no target code".
- **What:** `needs-target` is self-declared and unchecked. The empty `core.hooksPath` covers govkit's own git calls only. The target-spawn probe reads govkit.py's sites only.
- **Consequence:** A step's `git mv` fires the adopter's hooks, and a step's `python -m` or import runs adopter code, in the workspace that later pushes through the adopter's grant.
- **Fix (skeptic: sound):**
  - Add step processes as a ninth kind in the offer mode.
  - Run each step with `GIT_CONFIG_COUNT`/`GIT_CONFIG_PARAMETERS` pointing `core.hooksPath` at an empty directory, under an isolated interpreter.
  - Verify `needs-target: false` with a planted target hook and a planted target module, each seen not to run.
- **Gate:** Those planted fixtures in the target-spawn probe.

### M33. Emitted CI carries no action pinning or permissions rule (id 47)

- **Where:** The v2 [chain] dShippedRelease row, "optional emitted CI" and its Linux floor job.
- **What:** gov's own workflow pins every action by full commit sha, and that rule is required only of gov's workflow.
- **Consequence:** Adopters' emitted workflows run mutable action tags with the repository's token, on gov's say-so.
- **Fix (skeptic: sound):**
  - Require every emitted `uses:` to be pinned by full sha, read from one declaration that gov's workflow also uses.
  - Require least-privilege `permissions:`.
  - Add a leg that reds a planted tag-pinned `uses:` in an emitted template.
- **Gate:** That leg.

## Low

### L1. `Pass:` has two readers that disagree, and the clause names neither (id 7)

- **Where:** The v2 [chain] dDeclaredLoop row ("registered with one reader"), and the plan's [integration] and [migration].
- **What:** routed_commits.py:22 attributes by the union of the subject's ids and the trailer's. lib-unattended.sh:966 attributes by the trailer alone.
- **Consequence:** A commit with a subject id and `Pass: none` attributes differently in the index than in the lander.
- **Fix (skeptic: sound):**
  - Name both readers on dDeclaredLoop's row, and state the meaning that stands, or put it to the owner.
  - Re-point both in one unit.
  - Prove it on a planted `subject-id + Pass: none` commit that both read the same way.
- **Gate:** The trailer-reader population leg in M16.

### L2. [migration] says "nothing by hand", then routes decision rows by hand (id 13)

- **Where:** The plan's [migration] opening line against its "Decision rows" bullet.
- **What:** The section answers whether migration involves hand edits both ways. The hand step is dLinkedLibrary's two-rater routing of 200 rows.
- **Consequence:** A reader of the opening line will not plan the hand-routing population.
- **Fix (skeptic: sound):** Reword the opening: "Each step is owned and graded; only the decision rows no dossier lists are routed by hand, by dLinkedLibrary's two raters."
- **Gate:** A checklist entry under the bug class amendment-leaves-its-other-half-standing.

### L3. The refs pocket row gives all four ref families to dPlacedRequest (id 14)

- **Where:** The plan's [pockets] refs row.
- **What:** The mailbox belongs to dKeptSession, and bar-red belongs to dWitnessedBar's verdict path.
- **Consequence:** The atlas view shows the wrong owner for the mail and bar-red refs.
- **Fix (skeptic: sound):** Split the row by family: claims and leases to dPlacedRequest, mail to dKeptSession, bar-red to dWitnessedBar.
- **Gate:** A parity check between the [pockets] owner and the v2 clause owner.

### L4. The pockets table omits several live git-dir pockets (id 18)

- **Where:** The plan's [pockets].
- **What:** These pockets have no row: `drift-history.tsv`, the unattended sidecars (whose row the research return had and the plan dropped), `pre-push-allow`, and `codebase-map/lookups.jsonl`.
- **Consequence:** The atlas's Memory view cannot see these pockets, and they have no status, key or owner.
- **Fix (skeptic: sound):**
  - Add rows: drift history (owned by dTendedCadence), the sidecars (out, folded), `pre-push-allow` (out, or superseded by dWitnessedBar's verdict), and the lookups log (out, retired with `reuse_lookup.py`).
  - Or derive the git-dir rows from a listing of the common dir, so that a new pocket reds.
- **Gate:** The derived listing.

### L5. The region-parser factory's population is a typed "five" (id 24)

- **Where:** gap-mem-33 in the gap register, and the v2 [chain] dLinkedLibrary row.
- **What:** The list misses check_roles.py:112/144 (the `gen:roles-catalogue` region) and govkit/selftest.py:1528 (`scan_hold_region`).
- **Consequence:** Duplicate parsers survive the unit meant to remove them.
- **Fix (skeptic: sound):**
  - Derive the population by query, over `REGION_OPEN`/`REGION_CLOSE` constants and marker-pair finds.
  - List the two missed sites in the unit.
- **Gate:** A population-by-query rule for every re-point unit.

### L6. The unattended retirement leaves its legs, size rows and pointers unnamed (id 34)

- **Where:** The v2 [chain] dConvergedCharter row, the unattended retirement clause.
- **What:** The clause names only the kit's README and the product rule. It leaves out:
  - the 8 gate legs that reference the kit;
  - template-size rows :143 and :151 and the `[[exempt_leg]]` rows;
  - the registry `[[retired]]` row;
  - the charter template's protocol line and its renders;
  - AGENTS.md and the docs pointers;
  - root README.md:57's "four-verb driver".
- **Consequence:** The bar forces the legs and size rows at build time, so what is actually left out is documentation and pointer prose.
- **Fix (skeptic: sound):**
  - Extend the clause with an inventory derived from the tree by path and by value, covering everything above.
  - Do the same for agent-instructions at dOrderedCharter (README.md:17).
- **Gate:** The by-value reader inventory leg in H1.

### L7. The policy-values pocket still names dDeclaredLoop as owner (id 36)

- **Where:** The plan's [pockets] row "policy values".
- **What:** RC-1 moved the file, its schema and its reader to dGroundRules, and SP-1 moved the presets to dKeptSession.
- **Consequence:** The atlas shows a superseded owner.
- **Fix (skeptic: sound):** Set the owner to dGroundRules, or split the presets to dKeptSession, and re-render the view.
- **Gate:** The owner-parity check in L3.

### L8. The act-key clause assumes a preset harness session id (id 49)

- **Where:** The v2 [chain] dWellOiledMachine row, "minted at launch with the harness session preset".
- **What:** Codex returns its id only in the stream's start event.
- **Consequence:** A Codex act whose start event is late or lost has no harness session, and under `session` the commit-key leg refuses its commits.
- **Fix (skeptic: sound):**
  - Restate the clause as "the harness session id, preset where the adapter's row says so, else taken from its returned start event".
  - Declare the act record's and the trailer's state while the id is absent.
  - Add a conformance row for a Codex launch whose start event never arrives.
- **Gate:** That conformance row.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=49 confirmed=45 refuted=4 unverified=0 blocker=0 high=4 medium=33 low=8 agents=11 out-tokens=260631

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] row 'orientation cards' (retired into the session binding, owner dWellOiledMachine); v2 [chain] dWellOiledMachine and dPlacedRequest rows | high | medium | confirmed | memory-plan.md:93 retires `<git-common-dir>/orientation/<id>.md` 'into the session binding', with dWellOiledMachine as owner. v2 [chain] gives gap-orient-19 to dWellOiledMachine. That row's session-node clause (row 1412, clause 35) says only 'the session node derived from bindings ... runs-in ... after ... live delivery'. No clause retires the card. dPlacedRequest's card clause (row 1405) covers a per-build ref and says nothing of the per-session card. In v2, `scratch-guard` and `manifest-check` each appear 0 times and `session binding` 0 times. The tree still has both consumers: tools/hooks/scratch-guard.js:671 readCard joins `commonDir, 'orientation', sid + '.md'`, and skills/session-kickoff/manifest-check.sh:19 has `--card --write`. Since no unit stops the card being written, the likely outcome is the second-home case, not edits refused everywhere. The effect is contained, so medium. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] causes and pins arms, [practice] 'pinned facts', [migration] | high | medium | confirmed | memory-plan.md:310 arms 'a non-root record with no `caused-by`; an orphan', and :316 arms pins 'across every record'. Of the arms, only positional (:115, :315) is shrink-only or new-text-only. [migration] (:291-303) backfills neither causes nor pins. Re-run: `git grep -l Caused-by -- memory \| wc -l` printed 3, and the unpinned 'N of M' count printed 2642. In v2 the only 'orphan' is dFairHearing's skeptic orphan check (row 1403). The dTotalRecall and dOrderedCharter clauses (rows 1409 and 1402, clauses 19 and 29) refuse at write time and name 'pinned facts' with no legacy population. The defect is real, but the first gate run would surface it, so it is contained: medium, not high. | sound | - |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall row ('`record` writing each record's header (Serves, Made-by, Caused-by) ... refusing a missing cause on a kind that is not a root') against dWellOiledMachine's row | medium | medium | confirmed | v2 row 1409, clause 19, has `record` 'refusing a missing cause on a kind that is not a root'. The memory plan (:239-240) names the roots as intake, session binding and cadence lease. The first two land in dWellOiledMachine (row 1412, parents dBoundRoles, dTotalRecall, dKeptSession) and the cadence lease in dTendedCadence, all after dTotalRecall. v2 [revisions] around line 483 records the H2 rule: each new dependency on a later build gets a stand-in, a class row or a move. No stand-in is declared for this one, though dPlacedRequest has one for the claim commit ('until dWellOiledMachine's intake kind lands'). One part of the claim is weaker than stated: [sites] (:132) already lets Made-by name `owner`, so Made-by is not left without a value. The missing root and the missing stand-in stand. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[doors] 'Five doors ... and nothing else writes a node' and [practice] 'one door', against [sites] and [pockets] | medium | medium | confirmed | memory-plan.md:237 reads 'Five doors, one per site kind, and nothing else writes a node', and :121 reads 'a write elsewhere reds'. The same record gives other writers. [sites] :135 makes 'the builder' the door for code and :139 makes 'dTotalRecall's registry' the door for a registry row. [pockets] :84 makes refs (claims, leases, mail) nodes and :85 makes kit-release tags nodes, and :96-97 make views nodes written by renderers. None of these is among the five doors. One rule therefore names two different sets of writers. | sound | two-answers-to-one-question |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `trace.identity` row; memory plan [keys] and [gates] commits arm; [chain] dWellOiledMachine | medium | medium | confirmed | A grep for 'salted' across the dClosedLoop build records finds only value lists: v2:1078, memory-plan:342, away-pass:300 (AP-8) and research-observability-trace:137, where OB-1 glosses act-only but not salted. The layer-runtime:862 hit ('a salted id') is about population matches and is unrelated. v2 row 1412, clause 33, and memory-plan [gates] :312-313 define refusals only under act-only and session. Under salted, the value is selectable but nothing is built for it and no check tests it. | sound | - |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P35 ('renders `not-local` or `pruned`, never empty'); [chain] dWellOiledMachine; memory plan [sessions] and [pockets] (the binding's `transcript=` pointer) | medium | medium | confirmed | One count needs correcting: 'not-local' occurs once in v2, in P35 itself at :808, not 0 times. There are no occurrences in [chain]. v2 row 1412, clause 32 (act as the key), lists 'item, work order, harness, harness session, node and cause' with no transcript pointer. Clause 34 (gov trace and gov why) bounds rows by trace.rows and names no not-local or pruned state. The only 'transcript' is 'transcript homes' in clause 36's fixture. Both 'pruned' hits are slug claim refs. Clause 34 does cite P35, so a builder might carry it over, but no arm or fixture requires it. The binding's `transcript=` witness, at memory-plan :89-90, has no unit. | sound | - |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dDeclaredLoop ('`Pass:` and `Decided:` registered with one reader'); memory plan [integration] flow row and [migration] 'Old commits' | medium | low | confirmed | Re-run: routed_commits.py:22 reads 'ATTRIBUTION is the UNION ...', and lib-unattended.sh:966 reads '... attributed by that trailer ALONE'. v2 row 1404, clause 23, says only '`Pass:` and `Decided:` registered with one reader'. It names neither reader and does not say which meaning stands. It owns gap-spine-09, which the register grades LOW. Neither v2 nor the memory plan mentions routed_commits or lib-unattended. The clause already requires one reader, so the open defect is the unnamed meaning and the unnamed re-points. That is low. | sound | - |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[edges] `reads` and `writes' rows ('declared at the kind's registry row') against [pockets] role definitions and [integration] roles row | medium | medium | confirmed | memory-plan.md:174-175 declares both `reads` and `writes` 'item, role → record kind' at 'the kind's registry row'. :65 gives role definitions 'reads and writes edges' from their typed `reads:` and `writes:` fields, and :260 [integration] says 'reads and writes from role definitions'. This conflicts with :23, 'declared once at the site that owns its fact'. The two sites belong to two builds: dTotalRecall's registry, whose clause 1 holds 'writer, readers', and dBoundRoles' role definitions. No derivation between them is stated. | sound | two-answers-to-one-question |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P33 ('Every part of memory and code is a node named by a tag'); [chain] dOrderedCharter (namespace registry, per-tree index); memory plan [frame] and [edges] | medium | medium | confirmed | v2:793 P33 reads 'Every part of memory and code is a node named by a tag'. memory-plan.md:20-22 allows a tag, a section or a native id, and :179 reds an endpoint outside its row's namespaces. Greping namespace registrations across rows 1400-1421 lists reader, level, layer, practice, principle, kind, kit, doc, unit, step, item, policy, command, role, field, record, marker, feature, hook, point, leg, check and pack. None is act, session, commit or landing. The index is 'one JSON file per tree at `<git-common-dir>/gov/index/<tree>.json`' (row 1402), and no clause says how node-local acts or sessions join it. | sound | two-answers-to-one-question |
| 10 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[practice] table (checks `owned`, `retired`, render parity) against v2 [chain] dOrderedCharter ('address, one subject, typed relations, pinned facts and one door') and P34 | medium | medium | confirmed | v2 row 1402, clause 29, lists only 'address, one subject, typed relations, pinned facts and one door', yet P34 (:801-805) includes 'rationale kept apart from what loads'. 'render parity' occurs 0 times in v2. dConvergedCharter (row 1420) moves rationale into `help` fields but arms no check that help stays out of load sets. The systems record :269 defines the tags-pack `owned` check as 'an expansion declaring `item.build.x`'. The plan's `owned` at :122 ('every node names one owning build or layer') takes the same name for a different check. | sound | - |
| 11 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P37 ('One rule set governs encoding, line endings, paths, process launch, temp files, interpreter floors and quoting, each rule with its leg'); [chain] dOrderedCharter and dWitnessedBar | medium | medium | confirmed | v2:814-818 P37 lists seven rules 'each with its leg', and v2:1402 dOrderedCharter repeats 'each rule paired with its leg'. v2:1413 dWitnessedBar's portability pack builds a line-ending class leg, encoding arms, a bare-shell-name arm (launch) and an interpreter-floor arm. Nothing covers paths, temp files or quoting. Of the 140 entries in tools/gate-legs.json, the only names matching temp/tmp/path/quot are template size, shell hygiene x3 plus its selftest, hook destinations and dead-path carriers. The scratch-guard self-test guards write scope, not temp-file practice. So three of the rules have no leg, built or designed. | sound | - |
| 12 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[frame] 'The plan closes every hop' and [cycle], against [gates] and the v2 [chain] rows | medium | medium | confirmed | memory-plan:35 says 'The plan closes every hop', and [cycle] (181-201) lists fourteen hops. [gates] (305-317) checks edges, causes, commits, work orders, positional citations, pins and promotion one at a time. None of them walks the cycle. v2:1412's fixture replays four recorded events. A grep over the design records for 'every hop\|each hop\|cycle walk' found no acceptance that resolves every hop by key. Each arm can pass while a hop stays prose, so the overall claim stays uncertified. | sound | - |
| 13 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[migration] first line against its 'Decision rows' bullet | low | low | confirmed | memory-plan:293 opens with 'Nothing is rewritten by hand. Each step is mechanical, owned and graded'. :297-298 then says decision rows gain `decides` 'then by hand where none does'. That hand step is v2:1410 dLinkedLibrary's 200 rows routed by two raters at kappa 0.8. The two lines contradict each other in wording only. | sound | amendment-leaves-its-other-half-standing |
| 14 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] refs row (owner dPlacedRequest, covering `refs/gov/claims`, `runs`, `mail`, `bar-red`) | low | low | confirmed | memory-plan:84 gives the refs row (`refs/gov/claims`, `runs`, `mail`, `bar-red`) to dPlacedRequest. v2:1405 dPlacedRequest's row holds leases, run claims and the card ref, with no mailbox. The mailbox per build sits in v2:1406 dKeptSession, and `deps.messaging` and `mailbox.reads` are owned by dKeptSession (v2:896, 948). The plan's own 'one owner' edge rule (memory-plan:122) is therefore broken for this row. bar-red belongs to the runner-written verdict the pre-push hook reads (v2:1413 dWitnessedBar), and gap-deploy-10 (owned by dShippedRelease) touches it as well. Either way it is not dPlacedRequest's. The effect is limited to which owner the view shows. | sound | two-answers-to-one-question |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage, dShippedRelease and dConvergedCharter rows; P38 | medium | medium | confirmed | WIRE-INTO-PROJECT.md:69-86 installs the kickoff ONCE per machine as a junction or symlink at ~/.claude/skills/session-kickoff, outside the repository, and the gated write gate names /session-kickoff as its remedy. A grep over the non-research design records for junction\|per-machine\|user-level\|claude/skills hits only layer-runtime's user-level guards (682, 816) and a skill path size row. None of these is a fate for the link. The fates record's skills rows (lines 191-195) reshape the kickoff procedure and the Skills into thin entries but name no per-machine link, and no chain row owns re-pointing or retiring it. A re-shaped or moved skill dir would leave the links stale or dangling, and no designed check would see it. | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] (and v2 [chain] dConvergedCharter) | medium | medium | confirmed | help/ holds README.md and roles.md. AGENTS.md:38 binds the [docs] rule, and playbook.kit.toml:252-255 defaults HELP_DIR to help/. In the subjects, 'help/' appears only in v2:210 (a revision note) and v2:1420 ('never into `help/`'s feature pages'), with 0 hits in the memory plan and the gap register. The sibling layer-instruction:504 even says rationale moves 'under `help/`', which v2 and the systems record supersede. No [pockets] row, fates row or chain unit keeps help/roles.md current, though the chain rewrites /build, the roles and --scaffold, which that page describes. | sound | - |
| 17 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] row 'Claude transcripts' (and [sessions]) | medium | medium | confirmed | memory-plan:89 states the transcripts are 'kept 365 days'. `grep cleanup ~/.claude/settings.json` printed '2:  "cleanupPeriodDays": 365', a user-level setting on this node. `git grep cleanupPeriodDays` outside memory printed nothing, and the only design-folder hit is the research return. No design record gives transcript retention an owner, a measure or a preflight. v2:939 sets `runtime.journal` to 60 days, which exceeds the harness default of 30 on an unconfigured node, so the transcript witness can be pruned before the journal lines that point at it. | sound | - |
| 18 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] | low | low | confirmed | `ls` of the git common dir shows drift-history.tsv (865 lines), unattended/ (dDerivedDocket.lease, *.procs, landed.*.log), unattended-landed, pre-push-allow and codebase-map/lookups.jsonl (479,408 bytes). A grep of memory-plan for drift\|unattended\|pre-push-allow\|lookups finds no pocket row; the only hit is an unrelated 'sidecar list' at :144. research-git-pockets:86 had an 'Unattended sidecars' row (out: folded), and the plan dropped it. pre-push-allow could arguably sit under the catch-all 'gate ledger, logs and caches' row, but the drift history, the sidecars and the lookups log are not covered. The effect is on the view and inventory only. | sound | - |
| 19 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWitnessedBar, the clause 'one bash resolver in `tools/lib` with its JavaScript twin' (AP-33); gap register gap-tool-20 | medium | medium | confirmed | `git grep 'def resolve_bash\|def resolve_launcher'` printed 11 definitions, including profile_bar.py:282 (runs each candidate and honours GOV_BASH), regen.py:232 (reuses profile_bar inside the bar), drift-audit's resolve_bash_shell and process-monitor's resolve_launcher. v2:1413's resolver clause derives Git's bin/bash.exe from `git --exec-path`, refuses System32 and WindowsApps, and names no execution check. No design record in v2, gap-tool-20 or the away pass names profile_bar, GOV_BASH, resolve_launcher or resolve_bash_shell. process-monitor/selftest.py:1099-1102 records that a bash found in Git's usr/bin executed as WSL on this node, so trusting a derived path is a measured risk. The design misses the existing execution-based seam and drops the override. | sound | - |
| 20 | reuse | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[doors] 'gov trace <key> walks caused-by down … into a timeline'; [integration] flow row 'one reader for `Pass:`'; v2 [chain] dWellOiledMachine 'gov trace <key> and gov why <key> over the one index' and dDeclaredLoop '`Pass:` and `Decided:` registered with one reader' | medium | medium | confirmed | tools/runlog/model.py:4-7 says build_run_model joins the sources into a timeline with cost. model.py:588-600 read_git_range reads `Decided:` through git's trailer parse. v2:1412 designs `gov trace`/`gov why` over the one index, and v2:1404 registers `Pass:` and `Decided:` 'with one reader'. In v2 and the memory plan, runlog appears only as an import edge (1402) and an extractor (1408). Neither names build_run_model or read_git_range, and memory-plan:259 counts only the two `Pass:` readers. fates:128 keeps runlog's model STAYS as observability's reader, and no unit re-points it. The research's 'pre-chain backfill reader' line is at :97, not :87, but it reads as quoted. Once the chain lands, gov would hold a second timeline and a second `Decided:` reader. | sound | - |
| 21 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease, 'an edited retired file kept as a `forked` row with an order, as `install.retired-edits` says (P38)'; [policies] `install.retired-edits` | medium | medium | confirmed | Blob 0c6a17dc matches. v2:1091 and the dShippedRelease row (v2:1417) say an edited retired file is 'kept as a `forked` row with an order', and away-pass AP-28 (:320) says 'marked forked'. In govkit.py, `forked` is an existing receipt role with a conflicting contract. :411 defines it as 'gov's copy is a derivative of the target's'. :7527-7539 copies FORK_RULE_KEYS ('direction','record', :3674) from the producing descriptor rule, using .get, so a retired file's row gets nothing. :8121 dispatches it to 'report'. The grid cell that already covers this case exists: VERDICT_GRID ('differs','absent') yields 'patched' (:8047). No design record names that cell. Reusing the role name will mislead the unit spec writer. The effect is contained to reporting and wording. | sound | - |
| 22 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dLinkedLibrary, '`reuse_lookup.py` retired …, and memory-recall narrowed to a record finder'; [chain] dTotalRecall, '`record find`, its last line naming the total past 40 rows, and `record show` over the one index' | medium | medium | confirmed | Re-read. v2:1409 gives dTotalRecall '`record find` ... and `record show` over the one index'. v2:1410 gives dLinkedLibrary 'memory-recall narrowed to a record finder'. The fates record says both: :47 'narrowed to a record finder (dLinkedLibrary)' and :118 'query.py ... RESHAPED \| a record finder, `record find` (dTotalRecall)'. No row says what the narrowed memory-recall still finds that `record find` does not. That leaves two owners for one finder, so a spec writer cannot tell whether query.py is reused or retired. | sound | - |
| 23 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dLinkedLibrary 'gotchas handed by write set' and [chain] dFurnishedOrders 'bug classes rendered as a core field by the unit's write set' | medium | medium | confirmed | v2:1408 (dFurnishedOrders) has 'bug classes rendered as a core field by the unit's write set'. v2:1410 (dLinkedLibrary) has 'gotchas handed by write set'. ownership.md:520 and :772 assign the gotcha kind's 'gotchas handed by write set' to dTotalRecall, while layer-memory.md:450 says dLinkedLibrary. That is three owners for one behaviour. tools/memory-tree/gotchas.py:8 already ships `--for-paths`, the write-set selector, and grep finds it named in no chain row. Selection could diverge between work orders and review checklists. | sound | - |
| 24 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:gap-mem-33; v2 [chain] dLinkedLibrary 'the region-parser factory in `tools/lib`, today's five region parsers re-pointed to it' | low | low | confirmed | gap-register:188 (gap-mem-33) and v2:1410 name 'today's five region parsers' and list five files. `git grep REGION_OPEN *=` also finds tools/roles/check_roles.py:112, a marker pair for gen:roles-catalogue. check_catalogue_region at :144-150 finds and compares that region. govkit/selftest.py:1528 scan_hold_region parses fenced HOLD REGION markers. So the typed population of five is incomplete. A parser left outside the factory is a contained, duplicate-code effect. | sound | - |
| 25 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `commits.squash` and `install.retired-edits`; [presets] strict column; [chain] dShippedRelease | medium | - | refuted | Refuted as covered by the cited section and as unit-level detail (BY DESIGN). The dShippedRelease row (v2:1417) binds the squash unit to the key: 'a squash re-emitting the union of trailers as `commits.squash` says'. It binds the retired-edits unit the same way: 'kept as a `forked` row with an order, as `install.retired-edits` says'. 'As <key> says' is the design's standing form for a unit that honours every value of the key. The catalogue (v2:1077, :1091) declares the values, and the presets (:1354, :1362) select them. Spelling each value's arm, and where `refuse` acts, belongs to the unit spec that dShippedRelease writes later. The design is design-only, with no unit specs. | sound | policy-value-with-no-route |
| 26 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38; [chain] dSafePassage row; fates record [check] | high | medium | confirmed | P38 (v2:819-822) requires a build that changes an adopter-visible surface to ship an upgrade step. dSafePassage's row (v2:1401) carries the step kind, the walk, the `upgrade-walk` leg, which proves declared steps only, and the shim. It has no arm that reds a missing step or a registry removal with no `[[retired]]` row. The fates `[check]` (fates.md:229-249) lists nine arms, none about steps or adopter surfaces. The two arms the research proposed (research-supersession.md:127-128) do not appear in v2, the away pass or fates. The rule is therefore unenforced. Omissions would still surface as loud adopter refusals, not silent wrong results, so medium. | unsound | rule-stated-with-no-check-that-fails |
| 27 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] rows of dDeclaredLoop, dTotalRecall, dLinkedLibrary and dWellOiledMachine; dShippedRelease row's recovery clauses | high | medium | confirmed | I re-ran the per-row count over v2:1400-1420. It printed dSafePassage 4, dOrderedCharter 2, dShippedRelease 4, dConvergedCharter 2, and 0 for every other row, including dDeclaredLoop, dTotalRecall, dLinkedLibrary and dWellOiledMachine. Each of those four changes adopter-visible surfaces. REVIEW_ROUNDS is an optional key at tools/unattended/kit.toml:174, and v2:1404 retires it. reuse_lookup.py and its agent ship in codebase-map. dWellOiledMachine repacks the hooks (v2:1412). research-supersession.md:147 assigned dWellOiledMachine hook re-point steps and a /unattended shim, and its row carries neither. So the per-row step clauses are genuinely missing, unlike dOrderedCharter's 'its own upgrade steps'. Unwiring withdrawn hooks and the retired-edits order sit on dShippedRelease, after dWellOiledMachine. | unsound | - |
| 28 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease row, "the receipt's schema 4 gaining steps, superseded, deprecations and prior_commit" | high | high | confirmed | govkit.py:49 has `RECEIPT_SCHEMA = 3 # ... readers accept 1, 2 and 3`. govkit.py:8946-8953 runs the gov_oid back-fill under `if schema < RECEIPT_SCHEMA:`, and its comment says this is so a schema-3 receipt is NEVER back-filled, because such a row is 'exactly the corruption S9 exists to catch'. Bumping the constant to 4, as dShippedRelease's 'receipt's schema 4' clause (v2:1417) implies, flips schema-3 receipts into the back-fill. That launders a text-merged receipt past S9. The messages at :9005-9011 also interpolate RECEIPT_SCHEMA. The row names only kits.currency and the fleet register as readers, and ships no step or down step for the 3-to-4 change. The upgrade-walk requires down to be byte-identical (v2:1401). The path is narrow, but there the integrity check certifies what it does not check. | sound | retirement-inventory-misses-readers-by-value |
| 29 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] paragraph after the table ("the Serves kind is renamed `log`"); v2 [chain] dTotalRecall clause "the Serves kind `journal` renamed `log`"; [migration] | high | high | confirmed | memory-plan.md:107 says 'Serves kind is renamed `log` when dTotalRecall's registry lands', and v2:1409 carries the rename with no reader inventory, alias or step. [migration] (memory-plan:294) says Serves lines become edges 'with no file changed'. The value `journal` has live readers and writers. check-memory-hygiene.sh:3005 limits the AC-evidence ledger to Serves lines matching `journal`. gen_build_index.py:550 RECORD_KIND_TOKENS contains 'journal'. runlog/record.py:82 has SERVES_KIND = "journal". `git grep -c '^**Serves:** journal' -- memory` sums to 1443. Elsewhere the design names reader derivation for a retirement, as with REVIEW_ROUNDS at v2:1404, but not here. A partial rename silently drops the Evidences check either for new `log` records or for the 1,443 legacy ones. | sound | retirement-inventory-misses-readers-by-value |
| 30 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] row "orientation cards … retired into the session binding … dWellOiledMachine"; [chain] table; v2 [chain] dWellOiledMachine and dOrderedCharter rows | high | high | confirmed | memory-plan.md:93 retires `<git-common-dir>/orientation/<id>.md` into the session binding under dWellOiledMachine. Grep finds no v2 clause that retires the per-session card or names scratch-guard. v2's card hits are :73, :847 and dOrderedCharter's per-worktree card at :1402, and dWellOiledMachine's row has session binding and session node clauses but no card retirement. scratch-guard.js:671 reads the per-session card. :775 returns a witness, not a deny, when the card is absent, and :1182 builds the route notice from it. fates.md:155 marks scratch-guard STAYS, while fates.md:191 reshapes the card writer into dOrderedCharter's per-worktree file. Built as written, the write gate's route check fails open with only a witness. | sound | - |
| 31 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] row `review.design.round-count`; [chain] dDeclaredLoop clause "a planted round count at the runaway ceiling refused"; dConvergedCharter's unattended retirement | medium | medium | confirmed | v2:965 bounds `review.design.round-count` by "unattended's `RUNAWAY_CEILING`". `git grep RUNAWAY_CEILING` finds it defined only at tools/unattended/unattended.sh:774 ("8") and read by check-unattended.sh:624/726/821. Both files retire with the kit: fates.md:148 and :202 mark them RETIRED at dConvergedCharter. dDeclaredLoop's clause retires REVIEW_ROUNDS and refuses "a planted round count at the runaway ceiling", but it never moves the ceiling. dWellOiledMachine's clause dissolving the kit (hooks repacked, supervisor seam taken) doesn't name the constant either. Once the kit retires, no row says where the bound comes from. | sound | - |
| 32 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `install.deprecation-window`; [presets] pair rule; [chain] dSafePassage forwarding shim and dOrderedCharter's `map_lib` deprecation | medium | medium | confirmed | v2:1089 counts `install.deprecation-window` in releases. dSafePassage (v2:1401) keeps the shim for that many releases, and dOrderedCharter re-exports `map_lib` "for one release". gap-deploy-11 ("No release has ever been cut") is in dShippedRelease's Gaps owned. `git tag -l` printed only three archive/* tags. Nothing in v2 says what counts as a release before dShippedRelease; the release-0 fixture is a test tree, not a count. So shims declared early have a window with no defined close, and dConvergedCharter's "every shim removed when its window closes" has no trigger for them. | sound | - |
| 33 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38 "gov runs every step on itself first"; [chain] dShippedRelease "the lander running each new upgrade step on gov's own tree"; gap-deploy-20 | medium | medium | confirmed | P38 (v2:822) says "gov runs every step on itself first". The only general mechanism for that is dShippedRelease's "lander running each new upgrade step on gov's own tree … recorded in the source-mode receipt" (v2:1417), and gap-deploy-20 (gov can't run `update` on itself) is also dShippedRelease's. dSafePassage applies only the floor step to gov. dOrderedCharter declares its own steps (the agent-instructions wiring move and the `map_lib` deprecation) with no clause running them on gov. dShippedRelease comes after dWellOiledMachine and dLinkedLibrary, so steps declared earlier never go through gov first and gov's receipt starts without them. | sound | - |
| 34 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter, "the unattended kit, its four guides and `/unattended` retired … the kit's README and the product rule's 'four-verb driver' corrected with them" | medium | low | confirmed | Re-probed. tools/gate-legs.json holds 140 legs, and 8 of them mention unattended (the names match the finding). template-size-limits.txt:143 and :151 carry the two rendered-file rows. registry.toml:110 has `id = "unattended"` plus the `[[exempt_leg]]` rows. The charter template (:182) and AGENTS.md (:160) name UNATTENDED-PROTOCOL.md, and `git grep -l` prints 53 files outside memory/builds. v2's retirement clause names only "the kit's README and the product rule". `git grep "four-verb driver"` finds .claude/rules/product.md:30 and also root README.md:57, which the clause doesn't name. Graded low: the stale legs and size rows red the bar, which forces the inventory at build time. dConvergedCharter already ships the retirement as upgrade steps, which implies a `[[retired]]` row. What's actually left out is doc and pointer prose. | sound | - |
| 35 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[sites] the commit row; [doors] "the commit queue writes the trailers"; [gates] commits; v2 [chain] dWellOiledMachine commit-key leg | medium | medium | confirmed | memory-plan [sites]:136 gives the commit site one door, "the commit queue from the act binding; a `prepare-commit-msg` filler in the owner's session". [doors]:237 says "Five doors … nothing else writes a node", and [practice]:121's one-door rule says "a write elsewhere reds". tools/push-main.sh creates commits of its own: the merge at :878, the reconcile merge at :1067, `mint:` at :1089 and `regen:` at :1108 (both --no-verify with `Pass: none`). It pushes them at :975 and :1125 without --no-verify. layer-runtime treats the lander as separate from the commit queue ("the commit queue and the lander's prepare"). No record declares the lander's commits as a site or an exemption. | sound | - |
| 36 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] row "policy values … Owner dDeclaredLoop" | low | low | confirmed | memory-plan.md:61's pockets row "policy values … the policy file, and today each kit's conf … dDeclaredLoop" still names dDeclaredLoop. v2:866 and the dGroundRules row (v2:1400) say the file, its schema and its reader moved to dGroundRules (RC-1). The memory-plan pockets table isn't one of the owner fields the BY DESIGN block lists, so this is a stale owner that contradicts RC-1, not a re-argued decision. The effect is limited to a misleading owner shown in a view. | sound | - |
| 37 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] causes and pins bullets; [migration] | high | - | refuted | The premise is false on re-probe: the chain does give these gates a baseline. dTotalRecall's parents are dDeclaredLoop, dWitnessedBar and dPlacedRequest (v2 [chain]). dWitnessedBar's row (v2:1413) builds "`test.seed` at every check's registration, seeding only an absent population and recording a failed or dead-probe seed unarmed", along with the shrink-only ledger factory and "the seven record and row pins as keyed populations, and the date cutoffs registered as cutoffs". So a causes or pins check registered at dTotalRecall seeds today's population as debt instead of redding main. The counts do hold: 2306 Serves lines and 0 Caused-by lines. But memory-plan [gates] isn't the only place a check gets its legacy treatment; the general seeding rule in v2 covers it. | sound | - |
| 38 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] policy.proof / instructions.proof rows; [witnesses]; [chain] dGroundRules minimal guard and dDeclaredLoop 'the guard, the TTY CLI' | high | high | confirmed | v2:883 and :957 default `policy.proof` and `instructions.proof` to tty-cli, and v2:1114 keeps presets off them. The walkthrough (lines 127-129) defines the guard as a CLI that confirms at an interactive terminal and stamps a trailer, plus a push gate that checks the trailer. dGroundRules's minimal guard (v2:1400) enforces "the TTY proof" and refuses "agent writes". `command -v winpty` printed /usr/bin/winpty, so an agent's Bash call can get a TTY on this node. The trailer is plain commit text. gap-build-03 records that shell writes escape the write gate. Grepping the design records (research returns excluded) for threat\|adversar\|evasion\|malicious found no stated threat model for owner-only actions. An agent that sets out to evade the guard can therefore produce every signal it accepts as proof. That takes deliberate evasion, which is a narrow path, so I grade it high. | sound | - |
| 39 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease 'Codex install targets with their trust step surfaced'; dWellOiledMachine preflight clause | high | medium | confirmed | research-harness-cli.md:52 says Codex hooks are "trusted by hash, so a new project hook is skipped until the owner trusts it". Its line 133 scopes the trust step to dShippedRelease's install targets, and v2:1417 says the same: "Codex install targets with their trust step surfaced". dWellOiledMachine's preflight (v2:1412) refuses only "a launch that skips hooks or permissions". No record re-surfaces trust when an update adds or changes a hook entry, and no preflight checks for untrusted hooks. The evidence doesn't show exactly what Codex hashes: under a stable dispatcher command, changing pack bytes might not invalidate trust. But a new or changed hook entry from an update is certainly skipped. Graded medium because it only bites when Codex is the act harness. | sound | - |
| 40 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] commits bullet; v2 [chain] dWellOiledMachine 'the commit-key leg at the push reading the binding'; dTendedCadence 'a pushed commit missing a required key'; dShippedRelease 'carries' | high | medium | confirmed | memory-plan:48 makes runtime "acts, session bindings, the journal … node-local, kept for `runtime.journal`", and the acts and bindings pocket (:86) is a runtime pocket. The commits gate (:311) refuses "a `Gov-Act:` the binding does not hold", and v2:1412 puts the commit-key leg at the push, reading the binding. No record names the commit range the leg, Maintain's reading or `carries` evaluates, or what happens to a commit whose binding is on another node or has been pruned. dScopedBuild's join pins `--no-merges -M` (v2:1416), so the shape question is known elsewhere. A build that moves nodes (P22) or merges in another node's act commits would be falsely refused at the push. The refusal is loud, not a silent wrong result, so I grade it medium. | sound | - |
| 41 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] rows transitions.record, card.store, tests.landing-levels, platforms.supported | medium | medium | confirmed | Checked v2 at blob 0c6a17dc. In [policies], line 887 (transitions.record), 902 (card.store), 976 (tests.landing-levels) and 1086 (platforms.supported) each read 'any subset of ...'. The only non-empty rules are at 567 and 1085, and both are runtime.act-auth. The [policies] intro (857-868) has the schema refuse only out-of-set values, so an empty subset still counts as allowed. [floor] (1367-1369) says every stage transition is recorded and can be switched off only under the policy guard. An empty transitions.record turns that off through an ordinary key. The effect stays within the keys named. | sound | - |
| 42 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[sites] record section row and the paragraph below it; [frame] node addresses | medium | medium | confirmed | memory-plan at blob 9fe8384e, line 133 ([sites]), allows 'at most one line `**Edges:** type=target type=target`'. Lines 140-141 say 'a section with more types than fit takes one line per type'. The two rules contradict each other. [frame] line 20 defines a section address as `<doc> [<seg>]`, which contains a space. Several [edges] rows can target a section: answers ('the answer's section'), amends and supersedes (node to node). A whitespace-separated `type=target` line cannot carry such a target without ambiguity, and the 'target sits outside its row's namespaces' check would red it. | sound | - |
| 43 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage (update walk, down steps, recorded rollback); dShippedRelease 'a stale lock reclaimed' | medium | medium | confirmed | In v2:1401, dSafePassage names the walk, the witness skip, downs in reverse, a recorded rollback and up/down/up on release-0. No outcome is named for a step that fails or is killed partway. Searching the subjects for half-applied, partial, interrupted or killed found only gap-deploy-19 (gap-register:334). The dShippedRelease row (v2:1417) answers that gap only with 'a stale lock reclaimed'. The research row at research-supersession.md:112 also stops at per-kit rollback plus downs and a lock. Neither says how the receipt advances or how a step whose witness is false over a partly changed tree is re-entered. This is not unit-level detail: it is the contract of the step kind's walk. The fix is unsound because it contradicts itself. It auto-runs the downs of the run's already-applied steps and also advances the receipt per completed step, so the receipt would record steps the fix has just undone. It also assumes a step's down tolerates the partial state its own up left, which nothing requires. | unsound | - |
| 44 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage the upgrade-step kind and the `[[upgrade]]` row | medium | medium | confirmed | The dSafePassage row (v2:1401) and P38 (v2:819-822) define `[[upgrade]]` rows and `[[retired]]` succession rows for kits and surfaces. Neither freezes a released step row against later edit or removal. I grepped the subjects for frozen, immutable, append-only, never removed or never edited near 'upgrade' and found nothing. The memory plan's 'retire, never vanish' is about tagged nodes and a tag never being reused. It does not stop the down argv of a step adopters have already run from being edited. The upgrade-walk leg walks only the steps present at the target, so it would stay green. | sound | - |
| 45 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease 'kits.offer running the steps that need no target code, as install.steps says (P38)' | medium | medium | confirmed | In layer-expansions:454, the kits.offer mode refuses eight enumerated kinds of target-side spawn, listed by target_spawns.py over govkit.py's sites. The empty core.hooksPath is stated for 'update's git writes in the target', meaning govkit's own git calls. The v2:1417 clause 'kits.offer running the steps that need no target code' adds step processes as a new spawn class. needs-target is a self-declared field of the step row (v2:1401, research-supersession:107), and no clause checks it. Nothing says a step's own git or Python child runs with the empty hooksPath or an isolated interpreter. Passing GIT_CONFIG_COUNT/PARAMETERS through the environment does reach child git processes, so the fix cures the gap. | sound | - |
| 46 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage 'gov's own executors at the floor in the landing that raises it' | medium | - | refuted | BY DESIGN, and the cited section already covers it. I re-ran the probe: the resolver here yields Python 3.14.5, and .githooks/pre-push has 14 resolve_python lines, so the premise about the tree holds. However, the dSafePassage clause (v2:1401) has the resolver refuse an interpreter below the floor 'naming the install command as `platforms.provision` says', and has the up step be a preflight that refuses the same way. The behaviour on an unprovisioned node is therefore a named refusal with the install command, not a silent hook failure. The owner settled the raise and its fleet consequence in AP-31 ('3.15 now, all the nodes will upgrade') and the provisioning mode in AP-32 ('name'). A fleet-readiness gate before the landing re-argues those answers rather than finding a defect. | - | - |
| 47 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease 'optional emitted CI' and 'a Linux job in emitted CI that sets up Python at the floor' | medium | medium | confirmed | grep 'uses:' .github/workflows/*.yml shows lines 58, 118, 137 and 330, each pinned '@<40-hex> # vX'. v2:1401 requires remote-ci.yml's jobs to be 'pinned by full commit sha'. v2:1417 adds 'optional emitted CI' and 'a Linux job in emitted CI that sets up Python at the floor' with no pin or permissions rule. Grepping the subjects and layer records for 'commit sha', 'pinned by' and 'permissions:' finds only the dSafePassage clause about gov's own workflow. The class (emitted actions) is left out while its instance (gov's workflow) is covered. | sound | - |
| 48 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter 'every shim removed when its window closes, and the exit check widened: ... or an owner item for that adopter (P38)' | medium | - | refuted | The premise does not hold on re-reading. The shim removal in v2:1420 ships in gov's release. An adopter the owner keeps where it is does not update, so it keeps its installed tree and its shims, and meets no retired surface. It meets the removal only if it later updates past the window, and that is the case `install.deprecation-window` bounds: v2:1089 sizes the window at least `currency.max-behind` by the pair rule, so an adopter inside its currency budget never meets a removed surface. The owner item already records the owner's disposition, through the loop's one closed disposition set in dDeclaredLoop. The claim that 'nothing on the default branch records why' is therefore not established. The finder graded this medium, and the claimed consequence does not follow. | - | - |
| 49 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine 'the act as the key: minted at launch with the harness session preset' | low | low | confirmed | v2:1412 reads 'the act as the key: minted at launch with the harness session preset'. memory-plan:225 gives Codex's session id as 'returned in the stream's start event; no preset'. v2:1084 allows codex as runtime.act-harness. The same row's conformance fixture already says 'id preset or returned', so the design half-knows this. The act-key clause is still written for a preset id. It declares no state for the act record or the Gov-Session trailer before, or without, a start event, and the commit-key leg refuses an act-made commit without Gov-Session under `session`. Codex acts are not the default and need the owner's switch, so the effect is narrow and mostly in wording. | sound | - |
