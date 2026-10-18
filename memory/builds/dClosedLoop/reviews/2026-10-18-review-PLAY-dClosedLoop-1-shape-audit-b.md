**Serves:** spec-audit PLAY-dClosedLoop-1

# Shape audit, run B: gaps left in the converged dClosedLoop design

Tier-2 spec-audit, round 1, run B of two independent runs. The synthesis role (gov-synthesizer) wrote it from findings that adversarial skeptics confirmed. It answers the owner's question: "Can we review the entire design's shape for any gaps that may be left?"

Subjects (round 1): memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@0c6a17dc0401f64659f2da0880ef336a93893688, memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@961cf79c163f6d12a0ce8873037daba0d8a8aa0a, memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md@9fe8384ef79b90cbe62d6d6ba0b4f340a1380894.

## Verdict: CLEAN WITH FIXES

The design has no blocker. It has five high items, covering six raw findings:

- **H1:** P38 promises an upgrade step for every adopter-visible change, but nothing enforces it (ids 1, 34).
- **H2:** an owner-only proof that an agent can produce itself (id 42).
- **H3:** commit-key and cause checks that read node-local bindings off-node (id 45).
- **H4:** an upgrade walk with no failure or interruption route (id 48).
- **H5:** a restarted supervisor that can launch a second act on the same item (id 49).

Fix each high in the records before the owning build's spec is written.

Tally by item: 0 blocker, 5 high, 31 medium, 10 low, 46 items.

Tally by raw confirmed finding: 0 blocker, 6 high, 37 medium, 10 low, 53 findings.

Seven findings merge into others: ids 1 and 34, 2 and 37, 3 with 20 and 46, 4 with 19 and 32, and 8 and 51. Two findings describe a defect already in a higher item but keep their own item because their binding grade differs:

- id 13 (medium) is the same defect as H1.
- id 11 (low) is the one-line half of M8 (id 50).

Each of those items cites the other.

## Review shape

Intensity full. Raw 56, confirmed 53, refuted 3, unverified 0 (0 uncertain), precision 0.95.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 10 | 8 | 2 | 0 | 0 | 0.80 |
| reuse | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 10 | 9 | 1 | 0 | 0 | 0.90 |
| failure-envelope | yes | 15 | 15 | 0 | 0 | 0 | 1.00 |

Run integrity:

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 51 judged sound, 2 judged unsound (ids 13 and 42), 0 with no fix proposed, 0 not judged. Each unsound fix is replaced below by the skeptic's corrected fix.
- Severity: 0 confirmed findings were left ungraded by the skeptic, and 13 were re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes were supplied for all five lenses.

The run is complete on these counts.

- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 28 spec documents supplied as sibling context.
- Checklist: 17 items, each assigned to exactly one lens (coherence 4, grounding 4, reuse 3, blast-radius 3, failure-envelope 3).
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Refuted and not reported:

- id 14: intake redaction is already carried by the core journal's scanner.
- id 16: the mirror hash is read from the blob, so a CRLF checkout does not break it.
- id 40: `reuse_lookup.py`'s readers are already rewritten by its clause.

In every item below, v2 means the architecture-v2 record, plan means the memory plan, and register means the gap register.

## High

### H1. P38's upgrade-step promise has no check that can fail (ids 1, 34)

**Where:**

- v2 [principles] P38.
- v2 [chain]: dSafePassage, plus the rows of dTotalRecall, dLinkedLibrary, dDeclaredLoop, dWellOiledMachine, dWitnessedBar and dMindYourWords.
- Plan [migration] ("In an adopter, the backfill runs as an update's upgrade step") and the [integration] distribution row.

**What is wrong:** P38 binds every build that changes what an adopter can see to ship an upgrade step. Only 4 of the 21 [chain] rows name a step: dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter. Other rows change installed surfaces and name none:

- dTotalRecall refuses unknown README front-matter keys and renames the Serves kind `journal` to `log`.
- dWellOiledMachine repacks the hooks and replaces govkit's per-fragment wiring with one dispatcher entry per event.
- dDeclaredLoop retires `REVIEW_ROUNDS`.
- dLinkedLibrary retires `reuse_lookup.py`, which the receipt fixture installs.
- dMindYourWords replaces the lexicon count pin.

The `upgrade-walk` leg walks only the steps that exist, so a surface change with no step is invisible to it. The plan's adopter backfill step sits on no [chain] row in either record.

**Consequence:** an adopter's `update` across these builds breaks, or silently leaves records, hooks and conf keys stale. Meanwhile the walk certifies the steps it can see. That is the opposite of the seamless supersession the owner's away-pass point 6 asked for. P16's meta-check would also refuse P38 as a rule with no check.

**Fix (skeptic judged both fixes sound):**

1. Give dSafePassage a class gate: a leg that diffs the adopter-visible surface population between base and tip. That population is the receipt's `files` rows, kit.toml-declared files, hook and command paths, conf keys, record-kind schemas and CLI verbs. The leg reds a landing that changes a member with no `[[upgrade]]` or `[[retired]]` row whose `surfaces` names it. It must be seen red on a planted rename of an installed file with no step, and green with one.
2. Name the step clause on each row listed above.
3. Put the plan's adopter Serves-and-edge backfill on dTotalRecall's or dShippedRelease's row.

The id 34 skeptic notes this is a new check, so it goes to the owner rather than being designed here. Id 13 (medium, M3) is the same defect, filed separately at a lower binding grade.

**Left-shift gate:** the surface-diff leg itself, which is a gate for the whole class "rule stated with no check that fails".

### H2. The `tty-cli` owner proof can be produced by an agent (id 42)

**Where:**

- v2 [policies] `policy.proof` and `instructions.proof`.
- v2 [witnesses].
- v2 [chain] dGroundRules (the minimal guard) and dDeclaredLoop (the guard and the TTY CLI).

**What is wrong:** the guard rests on the claim that an agent's shell call cannot pass a CLI that needs an interactive terminal, plus a trailer that a push gate checks. A pty wrapper (`script`, `python -m pty`, or winpty in Git Bash) makes `isatty` true inside an agent's Bash call. The trailer is plain text anyone can type. No record says what makes either one unforgeable.

**Consequence:** several things rest on this proof: the policy guard, `instructions.edit`, the owner's pause, withdraw, supersede, attend and unattend, and `verdict.remote.pin`. An unattended agent with Bash can loosen policy or switch a floor invariant off. This is the T2 class: a guard that reads state the actor writes.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**

1. State in the records what `tty-cli` proves: owner presence against a cooperative agent only, never against an agent with Bash on the same node.
2. Have the harness refuse the guarded CLI's argv from an agent's Bash call, as it already refuses policy-file writes.
3. For the unattended guarantee, rest the floor's owner-only writes on a proof the agent cannot produce on its own node. That means a signature from a key that needs user presence (a hardware key or an OS prompt), checked at the push and by the off-node verifier.
4. Run both owed probes as red cases before the guard counts as a gate: a pty-wrapped CLI call, and a hand-typed trailer.

The owner's choice of `tty-cli` is not re-argued here.

**Left-shift gate:** a checklist entry, "every owner-only proof names its adversary and has a forged-proof red case".

### H3. Commit-key and cause checks read node-local bindings with no off-node rule (id 45)

**Where:**

- Plan [gates] commits and causes, the [families] runtime row and [doors].
- Mirrored in v2 [chain] dWellOiledMachine: "the commit-key leg at the push reading the binding".

**What is wrong:** the commit-key leg checks `Gov-Act:` against the act binding, and the causes check walks every record to a root. Both bindings and the session-binding root are node-local. No record says what either check does on a node that lacks them, such as:

- the lander's node;
- a peer verifier;
- remote CI;
- a take-over node;
- any node after `runtime.journal` prunes them.

The leg also has no independent way to tell an act-made commit once its trailer is missing.

**Consequence:** in a product built for several machines on one repository, this path is the common case. Either:

- the leg false-reds other nodes' work at landing, and the orphan check marks committed records orphans; or
- a builder skips non-local bindings, and the gate certifies nothing.

**Fix (skeptic judged sound):** declare the cross-node rule for both checks. Either:

- push a minimal binding record (act id, epoch, node, task-sha) to a ref the leg reads on any node; or
- limit the leg to commits whose binding is local, and render the others `not-local`, counted rather than passed.

Name the independent witness that marks a commit act-made, such as the commit queue's ref or a committer identity the act session is launched with. Owed probe: two nodes each make act commits, and the landing runs on a third node.

**Left-shift gate:** a checklist entry, "every check that reads node-local state declares its off-node verdict", with the three-node fixture as its red case.

### H4. The upgrade walk has no route for a failed or interrupted step (id 48)

**Where:**

- v2 [chain] dSafePassage: `update` walking every step, the release-0 fixture and the `upgrade-walk` leg.
- v2 P38.

**What is wrong:** the walk is specified only for success: up, down byte-identical, up again. No record says what happens when a step exits non-zero or is killed partway through a multi-step walk:

- whether the walk stops or rolls back;
- what the receipt records;
- whether a witness can hold over a half-applied step.

**Consequence:** steps are "skipped when [the] witness holds". So a step whose witness marker was written by its first write is skipped as done on re-run. The adopter is left with a half-migrated tree under a receipt that says it is current. gap-deploy-19 is today's instance.

**Fix (skeptic judged sound):**

1. A step is atomic or declares its own resume, and its witness is written last.
2. A failed or killed step stops the walk, and the receipt records the last completed step.
3. A declared rule governs rolling back the steps the walk already applied.
4. Extend `upgrade-walk` with two arms:
   - Kill each step after its first write, re-run `update`, and expect byte-identical convergence.
   - Make the k-th step exit 1, and expect the receipt to name step k-1.

**Left-shift gate:** those two `upgrade-walk` arms.

### H5. A restarted supervisor can launch a second act on the same item (id 49)

**Where:** v2 [chain] dWellOiledMachine: the supervisor "started and restarted by the node tick", and the fencing epochs.

**What is wrong:** the epoch bumps only at a take-over. Nothing says how a supervisor restarted on the same node, under the same lease and epoch, finds act sessions its dead predecessor launched that are still running. It computes `next` without them. The reap-orphans sweep is neither tied to act sessions nor ordered before `next`.

**Consequence:** after a supervisor crash during an act, a second act session can start on the same item in the same worktree. Both pass the epoch check, so their commits and returns interleave. The slot reservation is also lost. The claim that a supervisor's death "loses only the beat in flight" has no mechanism behind it.

**Fix (skeptic judged sound):** give the restarted supervisor a reconcile step before its first beat. It enumerates the act sessions recorded in the journal and process-monitor under this lease, then either re-adopts them (rebuilding slot reservations) or kills their trees. The alternative is to bump the epoch at every supervisor start. Owed fixture: kill the supervisor while an act runs, let the node tick restart it, and expect exactly one act session on the item.

**Left-shift gate:** that fixture in the runtime's fencing fixture set.

## Medium

### M1. Upgrade steps landed before dShippedRelease never run on gov first (ids 2, 37)

**Where:**

- v2 [principles] P38: "gov runs every step on itself first".
- v2 [chain] dSafePassage, dOrderedCharter and dShippedRelease.

**What is wrong:** the only general mechanism that runs a step on gov's own tree is dShippedRelease's lander. dOrderedCharter ships its own steps first: the agent-instructions wiring move and the `map_lib` deprecation. dShippedRelease is not an ancestor of dOrderedCharter. Only dSafePassage's floor step was patched to run on gov first.

**Consequence:** those steps reach adopters having never run on gov. Their witnesses are never recorded for gov, and gap-deploy-20 says gov cannot run `update` on itself today.

**Fix (skeptic judged sound):** either:

- move the "run each new step on gov's tree in the prepared merge, recorded in the source-mode receipt" clause to dSafePassage; or
- have dShippedRelease's lander first walk every step registered since release-0, not only new ones.

It must be seen red on a planted step whose witness does not hold on gov's tree.

**Left-shift gate:** that planted-step red case on the landing.

### M2. Three record gates arm over legacy populations with no ledger and no predicate (ids 3, 20, 46)

**Where:**

- Plan [gates]: causes and orphans, pins, and work orders.
- Plan [practice] "pinned facts".
- Plan [migration].

**What is wrong:** each gate runs over every record but declares no legacy population:

- **Causes and orphans:** "a non-root record with no `caused-by`; an orphan". Today almost no record carries `Caused-by`.
- **Pins:** "a quoted derived fact with no pin on its line, across every record". It has no predicate for what counts as a derived fact. The `map.py` arm it generalises matches only two shapes.
- **Work orders:** "a handoff with no marker; a return with no `answers`". Today 535 handoffs are unmarked.

Only `positional` is declared shrink-only over today's population. [migration] rewrites no file. The plan's own unpinned counts are already stale at HEAD: 2,278 Serves lines against 2,306, and 6,084 commits against 6,090.

**Consequence:** the gates red the whole corpus the day they arm. The alternative is that they are scoped ad hoc, or the pins predicate is narrowed to two shapes. In that case "pinned facts across every record" is certified while almost nothing is read, which the charter's [gate] rule forbids reading as coverage. The same class reaches dTendedCadence's "a pushed commit missing a required key" over 6,084 keyless commits.

**Fix (skeptic judged sound):**

1. Give each gate a population and direction, as for `positional`: either a shrink-only ledger seeded by `test.seed` and keyed by record path and section (or commit SHA), or a cutoff to records written through `record` after dTotalRecall lands, registered as a cutoff.
2. Define the pins predicate (which shapes count as a derived fact) and state what the arm does not read.
3. Pin the plan's own quoted counts to the commit they were measured at.
4. State the choice in [gates] and on dTotalRecall's and dOrderedCharter's rows.

Each gate must be seen green on today's tree with the population seeded, and red on a planted new causeless record, unpinned fact or unmarked handoff.

**Left-shift gate:** a checklist entry, "every gate over an existing corpus declares its legacy population".

### M3. Adopter-visible reshapes with no step, seen from the fates table (id 13)

**Where:** v2 [principles] P38, and every [chain] row except dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter.

**What is wrong:** this is the same defect as H1, found by the grounding lens. The finder graded it high and the skeptic graded it medium. That medium grade binds, so it is not merged into H1. Additional evidence:

- the away pass measured 107 of the fates table's 131 rows as changing shape, moving or retiring;
- dBoundRoles merges spec-reviewer and diff-reviewer and folds gov-session, renaming adopters' rendered agents;
- dWellOiledMachine retires `resume-tick.sh` and `RESUME_SCHEDULE_*`.

**Consequence:** an adopter can be left with a hand-registered `gov-resume-tick` task pointing at a removed script, stale agent files and unread conf keys.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):**

1. Arm dSafePassage's step kind on surface-level change, not on file edits. It reds when a landed commit removes or renames a path a kit descriptor declares installable, or retires or renames an agent, hook entry, command or conf key an adopter receives, and no `[[upgrade]]` or `[[retired]]` succession row names it in `surfaces`.
2. A content edit delivered by a plain update needs no step.
3. It must be seen red on a planted agent rename with no row, and green on a planted content-only edit.
4. Give each listed row its step clause, or a recorded reason it changes no adopter surface.

**Left-shift gate:** as H1.

### M4. The Serves kind rename `journal` to `log` has no mechanism and no reader inventory (ids 4, 19, 32)

**Where:**

- Plan [pockets]: the journal-collision paragraph.
- Plan [migration].
- v2 [chain] dTotalRecall: "the Serves kind `journal` renamed `log`".

**What is wrong:** 1,443 records carry `**Serves:** journal`. [migration] says Serves lines are read "with no file changed". Neither record says whether the old records are rewritten or read through an alias. Neither lists the readers that pin the token by value:

- `tools/runlog/record.py` (`SERVES_KIND`, and the check at :1467);
- `check-memory-hygiene.sh` check 23 (:3005, :3191);
- `gen_build_index.py` (`RECORD_KIND_TOKENS`);
- `handoff.py`;
- `migrate_backlog.py`;
- `HYGIENE.md` and `HYGIENE.template.md` :575;
- `adopt-memory-tree.sh` :721;
- `WIRE-INTO-PROJECT.md` :418;
- the test fixtures.

[migration] also opens "Nothing is rewritten by hand", then has decision rows gain `decides` "then by hand".

**Consequence:** once `record` writes `log`, check 23 fails every newly closed unit, and `gen_build_index` mis-kinds the new records. Runlog keeps writing `journal`, and adopters' rendered docs keep teaching it. Otherwise the 1,443 frozen records get rewritten against the migration rule. Either way, one rule returns two verdicts.

**Fix (skeptic judged sound):**

1. Keep `journal` as a read-only retired alias of `log`, per "retire, never vanish", so no file is rewritten. Only new records are written `log`.
2. Build the reader inventory by value (`git grep -n 'journal'` over tools/, the templates and the runbook) and re-point each reader in the rename's own unit.
3. Ship the alias as a dTotalRecall upgrade step for adopters.
4. Reword [migration] so the hand step for decision rows is named as the exception it is.

Probe: write one `log` record for a closed unit in a scratch clone, and check 23 stays green. Grade the tree and see 0 Serves failures on the existing journal records.

**Left-shift gate:** a checklist entry, "every rename or retirement carries a by-value reader inventory".

### M5. `review.design.round-count` is bounded by a constant the chain deletes (id 5)

**Where:** v2 [policies] `review.design.round-count`, and v2 [chain] dDeclaredLoop.

**What is wrong:** the key's allowed values are bounded by "unattended's `RUNAWAY_CEILING`", and dDeclaredLoop refuses a planted round count at that ceiling. The constant lives only in `tools/unattended/unattended.sh:774`. dWellOiledMachine dissolves that kit and dConvergedCharter retires it. No row or fates entry re-homes the constant.

**Consequence:** after retirement the schema bound vanishes silently, so the refusal arm can no longer fail, or the arm breaks.

**Fix (skeptic judged sound):** re-home the ceiling in one of three ways:

- as a loop-kit constant declared by dDeclaredLoop;
- as a catalogue key;
- by stating that `flow.route-backs` replaces it.

Then restate the catalogue bound against that home, and add fates rows for `RUNAWAY_CEILING` and the runaway detector. Probe: delete `unattended.sh` in a scratch clone, and the round-count refusal still reds.

**Left-shift gate:** a fates-coverage check that every constant a catalogue row cites has a fate (see M7).

### M6. Two settled owner answers have no chain clause (id 6)

**Where:** v2 [chain] dTotalRecall (gap-mem-40) and dWellOiledMachine (gap-tool-14).

**What is wrong:** two away-pass answers are carried by no chain clause:

- AP-4: a design-only build's units become nodes through the README's `ids:`, and design-only builds are exempt from the bindings check.
- AP-16: hooks use node, declared as a dependency.

Their gaps are owned in the register, but no unit builds the fix.

**Consequence:** a spec writer working from the rows builds neither. The bindings check keeps reporting design-only rows, and node stays an undeclared hard dependency.

**Fix (skeptic judged sound):**

- Add to dTotalRecall: "the build README's `ids:` defining a design-only build's units as nodes, the bindings check exempting design-only builds (AP-4)".
- Add to dWellOiledMachine or dOrderedCharter: "node declared as the hooks' dependency in the toolchain fact and the descriptors, its version measured in the conformance fixture and refused below a declared floor (AP-16)".

Each needs a planted red.

**Left-shift gate:** a join from each settled away-pass answer to a [chain] clause, red on an answer no clause carries.

### M7. P35's three-state render has no unit and no check (id 7)

**Where:** v2 [principles] P35, and v2 [chain] dWellOiledMachine `gov trace`.

**What is wrong:** P35 says a hop that lives on another node renders `not-local` and one past retention renders `pruned`, never an empty cell. The `gov trace` clause names `trace.rows` and a four-event fixture, but has no three-state row and no planted case.

**Consequence:** a trace run on a node missing the transcript, or past `runtime.journal`, renders empty cells, and nothing reds.

**Fix (skeptic judged sound):** add to the `gov trace` clause: each row is filled, `not-local: node <x>` or `pruned`, never empty. It must be seen red on a fixture event whose transcript lives on another node, and on one whose journal line is past retention.

**Left-shift gate:** those two fixture events.

### M8. Section-edge addresses do not fit the edge grammar (id 50)

**Where:** plan [frame] node addresses, [sites] the record-section row, and the shared grammar under [practice].

**What is wrong:** a section is addressed `<doc> [<seg>]`, which contains a space, but the edge line is space-separated (`type=target type=target`, with grammar `type=target[,target]`). [sites] also says "at most one line" of edges, then "one line per type". Id 11 (L3) carries that second half alone at low grade.

**Consequence:** either `caused-by=` and `serves=` cannot target a section, or each reader tokenizes the line its own way. That is the two-readers class `Pass:` already shows. The edge check either reds legitimate multi-line blocks or admits what the rule forbids.

**Fix (skeptic judged sound):**

1. Fix one target encoding, such as the `id#tag` form dRankedPlan already uses, or a quoted target.
2. State the separator and the escaping for commas and brackets, given `gov:note`'s `[refs=…]`.
3. Settle one line versus one line per type.
4. Give arms for a section target and for a two-line edge block.

**Left-shift gate:** those grammar arms in the edge check.

### M9. The one-door rule lists five doors where the class is every node writer (ids 8, 51)

**Where:** plan [doors], compared with [sites], [practice] "one door" and [pockets].

**What is wrong:** [doors] says "Five doors … and nothing else writes a node". The plan's own text names other writers:

- the builder, for code annotations under the grammar;
- dTotalRecall's registry, for registry rows;
- the coordination verbs, for refs (claims, leases, mail);
- view renderers;
- `kit-release` tags.

**Consequence:** a one-door check built from [doors] reds legitimate lease, mail and annotation writes. Built from [sites], it admits writers [doors] forbids. Exempted ad hoc, it certifies only five doors.

**Fix (skeptic judged both fixes sound):**

1. Derive the door list from the kind registry's writer column, which [pockets] and layer-memory [contract] already fill. Otherwise list the annotation writer, the registry writer and the ref writers explicitly, or route them through `record`.
2. Have the check read that one list.
3. It must be seen red on a planted write by an unlisted writer, and green on a lease acquisition.

**Left-shift gate:** the derived one-door check itself.

### M10. Convergence's exit check never derives the shipped-part population (id 15)

**Where:** v2 [chain] dConvergedCharter: "every part in the fates table at its fate, the table's join run as convergence's exit check".

**What is wrong:** the join runs over the fates table's 131 hand-typed rows. Shipped parts no row names include:

- `help/`;
- `.claude/roles.json`;
- `.claude/rules/product.md`;
- `tools/runlog/redaction.tsv`;
- `check_by_design_parity.py` and `orient.agent.md`;
- `tools/govkit/registry.toml` and `subject-pins.tsv`;
- `.githooks/pre_push_bar_selftest.py`;
- the top-level check scripts, covered only by a grouped row.

**Consequence:** a stale help page or an orphaned registry passes a check that reports the product converged.

**Fix (skeptic judged sound):** add an arm that derives the population from `git ls-files tools skills .githooks .claude .github help WIRE-INTO-PROJECT.md coding-governance-agents.template.md`. It requires each path to be matched by a fates row's path glob, and is red on a planted unlisted file. Give `help/` and `.claude/roles.json` rows with owners.

**Left-shift gate:** that derived-population arm.

### M11. P37's Python encoding rule has only an optional-kit leg (id 17)

**Where:**

- v2 [principles] P37 and P28.
- v2 [chain] dOrderedCharter (the portable practice) and dWitnessedBar (the portability leg pack).

**What is wrong:** P37 is core, with "each rule with its leg". The existing Python text-IO leg (`gate-lint/encoding_posture.py`) and the shell-hygiene legs live in gate-lint, which the fates table keeps as an optional expansion pack. dWitnessedBar's core pack adds only stdout and JavaScript encoding arms.

**Consequence:** on a core-only install the rule has no leg, which P16's meta-check refuses. Otherwise a builder writes a second Python encoding scanner.

**Fix (skeptic judged sound):** pair each P37 rule with a named leg and kit in dOrderedCharter's clause. Then either:

- move `encoding_posture.py`, and the relevant `sh_hygiene` mode, into dWitnessedBar's core pack; or
- declare gate-lint's leg the optional slot, with a core fallback.

Update gate-lint's fates row to match.

**Left-shift gate:** P16's meta-check run against a core-only install fixture.

### M12. The promotion gate reads node-local auto-memory with no declared runner (id 21)

**Where:** plan [gates] "promotion", and plan [pockets] "auto-memory".

**What is wrong:** the gate reds on "a standing directive found in memory and not promoted". It reads `~/.claude/projects/<repo>/memory/`, which is node-local: 90 files on the owner's node, none on CI. Nothing says whether it is a bar leg or a node reading.

**Consequence:** if it is built as a bar or push leg, a tree's verdict depends on which node runs it, and remote CI passes what the local run reds. That breaks P3's tree-keyed verdict.

**Fix (skeptic judged sound):** declare it a node-scoped cadence reading under observability (Maintain or Loop Review), filed as an ask, never a bar or push leg. Otherwise have it read only a committed snapshot of claimed rows.

**Left-shift gate:** a checklist entry, "a bar leg reads only the tree".

### M13. aScoutedSeam's grader and benchmark are on an unmerged branch (id 23)

**Where:** v2 [chain] dFairHearing, dBoundRoles and dLinkedLibrary, and register gap-test-18.

**What is wrong:** three builds take aScoutedSeam's grader or benchmark as input:

- dFairHearing's scorer factory names it as the second instance;
- dBoundRoles' `experiment` takes its parts from it;
- dLinkedLibrary's acceptance re-runs it.

The files (`bench.py`, `cases.json`, `results.json`, `judge.js`) exist only on `branch/deterministic-reuse-workflows-f70c33`. No unit or [owed] item lands them. The finder graded this high and the skeptic medium; layer-roles pins the branch, so a builder can find it.

**Consequence:** the factory is never proven over two instances, dLinkedLibrary's acceptance cannot run, and a builder likely rebuilds the grader.

**Fix (skeptic judged sound):** add a unit or [owed] item that lands the grader, cases, results and judge scripts on the default branch ahead of dFairHearing. Otherwise cite each branch blob by SHA in the three clauses. Say whether the out-of-repository corpora (inCMS, NicoCares) are needed. A factory test must refuse when only `review_replay.py`'s instance is present.

**Left-shift gate:** a check that every artifact a [chain] clause names resolves on the default branch or at a pinned SHA.

### M14. Five catalogued policy values have no route, two of them in the strict preset (id 24)

**Where:**

- v2 [policies] `commits.edge-check`, `commits.squash`, `trace.identity` and `memory.legacy-anchors`.
- v2 [presets].
- v2 [chain] dWellOiledMachine, dShippedRelease and dTotalRecall.
- Plan [keys].

**What is wrong:** five values have no arm, witness or route in any clause:

- `commits.edge-check: commit-msg`;
- `commits.squash: refuse`;
- `commits.squash: accept-loss`;
- `trace.identity: salted`;
- `memory.legacy-anchors: retag`.

The strict preset selects `commit-msg` and `refuse`. The finder graded this high and the skeptic medium.

**Consequence:** a strict repository checks no trailers at all, because the push leg is switched away and nothing replaces it. Meanwhile the catalogue reads as complete.

**Fix (skeptic judged sound):**

1. Write each value's arm into its owning clause:
   - a commit-msg hook check with its planted red (dWellOiledMachine);
   - the squash refusal and the accept-loss record (dShippedRelease);
   - the salting rule and its leg (dWellOiledMachine);
   - the retag rewrite as an upgrade step (dTotalRecall).
2. Walk the strict preset through the clauses.

Probe: in a strict-preset repository, an act commit with no `Gov-Act:` reds.

**Left-shift gate:** a catalogue join that reds on any value with no arm on its owning build's row (class: policy-value-with-no-route).

### M15. The record finder is split across two builds (id 25)

**Where:** v2 [chain] dTotalRecall and dLinkedLibrary, and the plan's [pockets] "recall index" row.

**What is wrong:** two builds claim the finder:

- dTotalRecall builds a new `record find` and `record show`.
- dLinkedLibrary narrows memory-recall "to a record finder".

Neither names `query.py` or `check-recall.py`, which the fates table gives to dTotalRecall. Meanwhile the plan gives the recall-index pocket to dLinkedLibrary.

**Consequence:** a likely duplicate finder. Otherwise `query.py` and `check-recall` sit at no fate when the exit join runs.

**Fix (skeptic judged sound):** choose one owner. Either:

- dTotalRecall's `record find` reshapes `query.py` and takes over the check-recall leg, and dLinkedLibrary drops its finder clause; or
- the finder moves to dLinkedLibrary in both records.

Align the plan's Owner cell with the choice.

**Left-shift gate:** an owner-agreement join between the fates table, [chain] and plan [pockets].

### M16. "One reader" for `Pass:` and `Decided:` ignores three existing readers and a deliberate difference (id 26)

**Where:**

- Plan [integration] flow row and [migration] "Old commits".
- v2 [chain] dDeclaredLoop and dLinkedLibrary.

**What is wrong:** three readers already exist:

- `routed_commits.py` takes the union of subject and trailer ids;
- unattended's `read_attribution_tokens` lets the trailer replace the subject;
- `runlog/model.py` parses `Decided:`.

The plan calls the union/replace difference a disagreement, but it is documented as deliberate, because the two answer different questions. No record names these seams.

**Consequence:** a builder may collapse union and replace into one rule, silently changing one leg's answers, or write a fourth parser.

**Fix (skeptic judged sound):** name the three seams in dDeclaredLoop's clause. State that the one reader exposes both the union and the replace views, and which consumer reads which. Reword [integration]. Run routed_commits' AC2 arms and `unattended --check-commit` on planted `Pass: none` and `Pass: <id>` commits, before and after the re-point.

**Left-shift gate:** that before-and-after parity run.

### M17. Three replay measurements bypass dFairHearing's scorer factory (id 27)

**Where:** v2 [chain] dCalibratedLens (instruction evals), dTotalRecall (the map replay) and dLinkedLibrary (the code-slot losing test).

**What is wrong:** dFairHearing builds one deterministic scorer factory that refuses a partial population. These three clauses specify scoring without citing it.

**Consequence:** each build grows its own scorer, which repeats gap-test-18 and loses the partial-population refusal.

**Fix (skeptic judged sound):** have each clause score through dFairHearing's factory. Add a conformance arm in dFairHearing that reds on a second scorer, for example code outside the factory that pairs variants with cases.

**Left-shift gate:** that second-scorer arm.

### M18. The shared bash resolver drops the `GOV_BASH` contract and the copy-install carry (id 28)

**Where:** v2 [chain] dWitnessedBar: "one bash resolver in `tools/lib`".

**What is wrong:** the clause gives only Git's `bin/bash.exe` before PATH. Today six files honour `GOV_BASH` first and refuse an unusable value by name: govkit, corpus_ids, handoff, lexicon selftest, row_grammar and profile_bar. Their self-tests check this. govkit is copy-installed and cannot import `tools/lib`.

**Consequence:** a resolver built from the text ignores the operator override and breaks those arms.

**Fix (skeptic judged sound):** give the full order:

1. `GOV_BASH`, with a set but unusable value refused by name;
2. `git --exec-path`'s bash;
3. PATH, with System32 and WindowsApps refused.

Name govkit's `resolve_bash` as the extracted seam, and state that copy-installed kits carry it inline. corpus_ids' and govkit's `GOV_BASH` arms stay green.

**Left-shift gate:** a checklist entry, "a consolidation clause names the seam it extracts and the contracts it keeps".

### M19. The baseline ledger's "row-keyed driver" does not name `merge-rows.py` (id 29)

**Where:** v2 [chain] dWitnessedBar, the baseline ledger factory clause.

**What is wrong:** `tools/memory-tree/merge-rows.py` is already the row-keyed three-way merge driver, with postconditions on the written bytes. The clause does not name it.

**Consequence:** the repository ends up with a second driver with different guarantees.

**Fix (skeptic judged sound):** name `merge-rows.py` and `merge-rows.sh` as the seam. Add the ledger TSV class with the factory's row key, and extend the postconditions to it. Run `merge-rows.test.sh`'s append-collision case on a planted ledger conflict.

**Left-shift gate:** as M18.

### M20. dConvergedCharter builds a record-kind factory beside dTotalRecall's registry (id 30)

**Where:** v2 [chain] dConvergedCharter, compared with dTotalRecall's record-kind registry.

**What is wrong:** dTotalRecall already generates templates and checks from its registry. dConvergedCharter separately builds "the record-kind factory and its conformance gate". That contradicts P16, under which each kind's factory and gate lands with its owning build.

**Consequence:** the per-kind shape is re-derived in a second place. The kinds added in between have no conformance gate until convergence:

- dPlacedRequest's `probe`;
- dTotalRecall's view, registry, archive, instrument, witness and shape-run kinds;
- dIndexedDesign's playbook kinds.

**Fix (skeptic judged sound):** reword dConvergedCharter's clause as the conformance gate over dTotalRecall's registry. Otherwise move the factory into dTotalRecall and give each later kind-adding clause its conformance row. Plant a kind row missing its writer and see the gate red.

**Left-shift gate:** that planted kind row.

### M21. `.governance/deploy.toml` is not a pocket (id 31)

**Where:** plan [pockets], and [view], which draws from it.

**What is wrong:** the table claims every pocket but omits the committed overlay whose `[answers]` and `[charter] adopter_rules` render into AGENTS.md at level 0.

**Consequence:** charter-loading text can change through a plain file edit outside `instructions.edit`, with no node, door or owner, while the files beside it are guarded.

**Fix (skeptic judged sound):** add a [pockets] row for `.governance/deploy.toml`: family instruction, nodes at level 0, key tag, owner dOrderedCharter, door `instructions.edit`. Add it to dGroundRules' minimal guard list if the owner agrees. Consider a row for `.governance/install.json`.

**Left-shift gate:** a join from every file that renders into the charter to a [pockets] row.

### M22. Retiring the orientation cards leaves the write gate reading a file nothing writes (id 33)

**Where:**

- Plan [pockets]: "orientation cards … retired into the session binding | dWellOiledMachine".
- v2 [chain] dWellOiledMachine and dPlacedRequest.

**What is wrong:** `scratch-guard.js` reads `<git-common-dir>/orientation/<sid>.md` and denies routed writes when the card is absent. The fates table keeps scratch-guard. dScopedBuild later builds "a write gate reading derived state", but lands after dWellOiledMachine. No clause re-points the read in the retiring unit. The finder graded this high and the skeptic medium.

**Consequence:** between the two builds every routed product write is refused, in gov and in every adopter.

**Fix (skeptic judged sound):** in dWellOiledMachine's row, or dBoundRoles' (which owns the write-gate pack), re-point scratch-guard's route read to the session binding in the same unit that retires the cards. List the readers:

- `readCard` and `extractRouteUnits`;
- `manifest-check.sh --card`;
- `check-wiring.test.sh`;
- `format-guard.test.sh`.

Keep the old path read inside `install.deprecation-window` as an upgrade step. Probe: in a scratch clone with the cards retired, a routed Write is allowed under the new binding and refused without it.

**Left-shift gate:** a by-value reader inventory for every retired path (checklist).

### M23. The deprecation window counts releases before any release exists (id 35)

**Where:**

- v2 [policies] `install.deprecation-window`.
- v2 [presets] pair rule.
- v2 [chain] dSafePassage (the forwarding shim) and dConvergedCharter.

**What is wrong:** the window and `currency.max-behind` are both counted in releases. gov has no release tags, only `archive/*` tags. Releases start with dShippedRelease's `kits.cadence`, many builds after dSafePassage.

**Consequence:** shims created in between either never retire, or retire at 0 elapsed releases while adopters are still on them.

**Fix (skeptic judged sound):** state what counts as a release before dShippedRelease, for example a receipt-recorded landing SHA, or a first tag cut at dSafePassage's landing. Otherwise start the clock at the first tag and hold shims until then. Add an untagged-history case to the release-0 fixture.

**Left-shift gate:** that fixture case.

### M24. The default credential order cannot be read on either platform (id 43)

**Where:**

- v2 [policies] `runtime.act-auth`.
- v2 [chain] dWellOiledMachine: "each read from the node's credential store and never from a file".

**What is wrong:** on Windows, oauth-shared is the harness's own file, `~/.claude/.credentials.json`. On headless Linux no store is named for the setup token. The finder graded this high and the skeptic medium, since it fails loudly.

**Consequence:** unattended acts fail at launch, or a builder breaks the rule silently. The fixture proves the fallback only against a planted store.

**Fix (skeptic judged sound):** name the credential home per platform and per credential:

- oauth-shared is the harness-managed file, read by the harness only;
- the setup token lives in Credential Manager or libsecret, with a declared headless-Linux answer.

Either amend the rule to "gov never reads or copies a credential file", or name each store. Run the fixture against the real harness store on each `platforms.supported` row.

**Left-shift gate:** that per-platform fixture run.

### M25. Codex hook trust is lost on a hook-changing update (id 44)

**Where:**

- v2 [chain] dWellOiledMachine (preflight, and the conformance fixture's fail-closed path).
- v2 [chain] dShippedRelease (Codex trust step).
- v2 P36.

**What is wrong:** Codex trusts each hook by hash and skips an untrusted hook. Trust is surfaced only at install. An update that changes a hook's bytes untrusts it silently, and preflight checks only launch flags.

**Consequence:** under `runtime.act-harness: codex`, the next unattended act after any hook-pack release runs with that hook skipped. That is fail-open.

**Fix (skeptic judged sound):** add a preflight arm comparing each wired hook's hash with the harness's trusted set, refusing the launch on a mismatch. Have `update` and `kits.offer` treat a hook-byte change as an attended re-trust step or an owner item. Probe: change one byte of a trusted planted hook, and the launch is refused.

**Left-shift gate:** that probe as a conformance-fixture arm.

### M26. Mailbox intake can serve as the owner's ratification (id 47)

**Where:**

- v2 [chain] dWellOiledMachine (intake through the mailbox or a cadence filer).
- v2 [chain] dKeptSession (the `intake` message kind).
- v2 [chain] dRankedPlan (intake read as ratification).
- v2 P4.

**What is wrong:** any sender can append an `intake` message by CAS, including an act's agent. It is placed like an owner prompt. Under `plan.ratification: request`, the request is the mandate. No record marks origin or restricts who may send. The finder graded this high and the skeptic medium.

**Consequence:** unmandated work runs past Plan unattended.

**Fix (skeptic judged sound):** mark each intake's origin: owner-bound hook, mailbox sender, or cadence filer. Let only owner-origin intake, or mailbox intake carrying the owner binding's proof, satisfy ratification. Route the rest to an owner breakpoint or an ask. Probe: an act posts an `intake` proposing a build, and Plan's exit does not pass.

**Left-shift gate:** that probe.

### M27. Emitted CI carries no action-pin requirement (id 52)

**Where:** v2 [chain] dSafePassage (gov's `remote-ci.yml` pinned by full SHA), compared with dShippedRelease ("optional emitted CI").

**What is wrong:** the SHA pin is specified for gov's own file only, not for the workflows emitted to adopters.

**Consequence:** adopters' verdict-producing jobs resolve actions by mutable tag, which is a supply-chain path.

**Fix (skeptic judged sound):** in dShippedRelease's clause, require every `uses:` in an emitted workflow to be pinned by full SHA with the tag as a comment. Add a leg over the emitted templates, red on a planted `@v6`.

**Left-shift gate:** that leg.

### M28. Upgrade steps have no execution contract (id 53)

**Where:** v2 [chain] dSafePassage (the `[[upgrade]]` row), compared with dShippedRelease (the `kits.offer` sandbox).

**What is wrong:** steps are a ninth class of code run in an adopter's tree, and the step kind declares none of:

- a working directory;
- an environment scrub;
- Python `-I`;
- an empty `core.hooksPath`;
- a credential rule.

The "needs the target's code" field is self-declared and never checked, yet `kits.offer` relies on it unattended.

**Consequence:** steps fire the adopter's git hooks, import from the adopter's working directory, and are offered unattended on a false declaration.

**Fix (skeptic judged sound):** put the isolation contract in the step kind, so every caller inherits it: scrubbed environment, `-I`, an empty hooksPath and no ambient credential. Check the field by running each release-0 step under that sandbox, so a step that needs target code fails there and is marked attended.

**Left-shift gate:** that sandboxed release-0 run.

### M29. The core code record has no input exclusions or over-ceiling behaviour (id 54)

**Where:** v2 [chain] dTotalRecall (the `code` record), v2 P32, and v2 [owed] the cold-derivation check.

**What is wrong:** the record declares nothing for:

- vendored or minified trees;
- binary and LFS blobs;
- submodules;
- very large files.

Its 30 s and 1 MB ceiling is measured only on gov's tree.

**Consequence:** in an adopter with `node_modules` or a 5 MB bundle, the core render blows its bounds with no degradation. The losing test passes on gov and fails first in the field.

**Fix (skeptic judged sound):**

1. Declare exclusions: registered vendored and generated paths, binary and LFS by attribute, and submodules as boundary nodes.
2. Add a per-file byte cap with a `skipped: <reason>` row.
3. Add a per-run time ceiling that degrades to the `git grep` floor.
4. Re-time on a planted adopter-scale fixture.

**Left-shift gate:** that fixture.

### M30. The annotation span rule leaves malformed spans undefined (id 55)

**Where:** v2 [chain] dLinkedLibrary (the span rule), v2 P33, and plan [gates].

**What is wrong:** nothing defines or reds:

- an unterminated note outside a definition;
- an orphan `gov:end`;
- crossed or nested tags;
- a tag mismatch.

The research return puts 6 of 57 spans in need of `gov:end`.

**Consequence:** a missing `gov:end` silently extends or empties a region. `part-of` edges and bundles then carry wrong ranges.

**Fix (skeptic judged sound):** define the extent of an unterminated span, or refuse it. Add the four span arms to the annotations leg, each red on a planted file.

**Left-shift gate:** those arms.

### M31. A declined retirement leaves convergence unable to exit (id 56)

**Where:** v2 [chain] dConvergedCharter: retirements through ratified proposals, and the fates join as the exit check.

**What is wrong:** only the owner's yes is routed. A declined retirement keeps the part in place, and the join reds. This is class C15, owner item without its reject outcome.

**Consequence:** the last chain build cannot exit, or its check is weakened ad hoc.

**Fix (skeptic judged sound):** a declined retirement amends the part's fates row through the ratification record, to `kept` or a new fate, and the join reads the amended row. Plant a declined proposal: the exit passes on the amended fate and reds on an unamended one.

**Left-shift gate:** a checklist entry, "every owner item routes its no".

## Low

### L1. Pocket owner fields disagree on refs (id 9)

**Where:** plan [pockets] refs row Owner, compared with the layer-memory kind table.

**What is wrong:** [pockets] gives claims, leases and mail to dPlacedRequest. The kind table gives claims to dTotalRecall and mail to dKeptSession.

**Consequence:** the atlas views disagree on one fact.

**Fix (skeptic judged sound):** split the row (claims dTotalRecall, leases dPlacedRequest, mail dKeptSession, and bar-red its owner), or defer the cell to the registry.

**Left-shift gate:** the owner-agreement join in M15.

### L2. dKeptSession depends on a later build for live owner questions (id 10)

**Where:** v2 [chain] dKeptSession, the attendance rule.

**What is wrong:** "owner questions asked live" is dFurnishedOrders' mechanism, and dFurnishedOrders is not an ancestor. A stand-in is named only for the `step —` announcement.

**Consequence:** the arm cannot be accepted on what the ancestors provide, or the unit builds a second mechanism.

**Fix (skeptic judged sound):** append "owner questions asked live joining when dFurnishedOrders lands them", or move that half of the rule to dFurnishedOrders.

**Left-shift gate:** a chain check that every mechanism a clause names is built by the row or an ancestor.

### L3. Edge lines: "at most one line" against "one line per type" (id 11)

**Where:** plan [sites] record-section row, compared with the paragraph below the table.

**What is wrong:** the two wordings give opposite verdicts on a two-line section. This is the half of M8 that M8 already covers, kept separate at its low binding grade.

**Consequence:** the record check and its spec disagree.

**Fix (skeptic judged sound):** pick one wording, state it once, and plant red cases for a two-line section and an overlong line.

**Left-shift gate:** as M8.

### L4. `Pass:` has no edge type, and the hop tallies disagree (id 12)

**Where:** plan [sites] commit row, [edges], and [frame] compared with [cycle].

**What is wrong:** `Pass:` is said to map to an edge type, but no type declares it. Its values are unit ids. Separately, [frame] says "seven of twelve hops typed", while [cycle] tabulates 14 hops with 2 typed.

**Consequence:** the edge check has no type for `Pass:`, and readers get two tallies.

**Fix (skeptic judged sound):** add `Pass:` to `serves`' "Declared at" cell, or call it a field. Pin [frame]'s figure to the research return's hop set, or restate it from [cycle].

**Left-shift gate:** the edge check's "unregistered type reds" arm run over the plan's own [sites].

### L5. Transcript retention of 365 days is one node's setting (id 18)

**Where:** plan [pockets] "Claude transcripts", and [sessions].

**What is wrong:** `cleanupPeriodDays: 365` is in this node's user settings. The harness default is 30. No unit sets, reads or reports it. The finder graded this medium and the skeptic low, since P35 already renders `pruned`.

**Consequence:** on other nodes, hops older than 30 days render `pruned`, unbudgeted.

**Fix (skeptic judged sound):** restate the figure as "harness default 30 days; 365 on gov's node". Measure it in dWellOiledMachine's conformance fixture. Have install set it, or have the Loop Review report a node whose retention is shorter than `runtime.journal`.

**Left-shift gate:** that conformance row.

### L6. P3 states that remote CI is unavailable (id 22)

**Where:** v2 [principles] P3.

**What is wrong:** P3 rests on "remote CI is not available (R4.4)". `remote-ci.yml` runs on every push to main and blocks nothing, as the register's own picture and gap-test-02 say.

**Consequence:** a spec writer may leave out the remote-CI job that dSafePassage and gap-tool-23 must edit.

**Fix (skeptic judged sound):** restate the ground as "remote CI runs after the fact and blocks nothing (gap-test-02), so the local hook is the binding verdict", keeping R4.4.

**Left-shift gate:** none fits; this goes on the checklist as "a principle's stated ground is re-probed at each full audit".

### L7. The `map_lib` re-export is held for one release against a window of two (id 36)

**Where:** v2 [chain] dOrderedCharter: "map_lib re-exports the moved names for one release".

**What is wrong:** the literal "one release" contradicts `install.deprecation-window`'s default of 2, which is pair-ruled at no less than `currency.max-behind`. The shim covers only command and hook paths, not module imports. The finder graded this medium and the skeptic low: `update` re-copies the template with the kit, so no runtime break was shown.

**Consequence:** the clause and the policy disagree.

**Fix (skeptic judged sound):** bind the re-export to `install.deprecation-window`, and widen the shim rule to cover moved module imports.

**Left-shift gate:** a catalogue check that reds a literal window in a clause.

### L8. The plan's adopter backfill step has no owner (id 38)

**Where:** plan [integration] distribution row, [migration] "In an adopter", and plan [chain].

**What is wrong:** the backfill is promised as an update step, but neither [chain] lists it. Under `memory.legacy-anchors`' default, adopters already get derived edges with no step, so what remains is an orphaned promise and the unbuilt `retag` path. The finder graded this medium and the skeptic low. It is related to H1 but kept separate at its grade.

**Consequence:** the chain-echo arm cannot red on its absence.

**Fix (skeptic judged sound):** add a plan [chain] row and a matching v2 clause on dTotalRecall or dShippedRelease, and define what "the Serves backfill" writes.

**Left-shift gate:** the chain-echo arm extended to [migration] promises.

### L9. The unattended kit's retirement misses value readers (id 39)

**Where:** v2 [chain] dConvergedCharter, the unattended kit retirement clause.

**What is wrong:** the clause omits several readers:

- `memory/project/fork-ceilings.txt` rows `unattended-status` and `check-unattended`;
- `method-carriers.txt`'s unattended Skill rows;
- `README.md:17` and `README.md:57`.

The finder graded this medium and the skeptic low, since the fork-count break reds the bar at once.

**Consequence:** the spawn-budget leg reds, a carrier row points at a removed Skill, and the README advertises dead kits.

**Fix (skeptic judged sound):** add a by-value reader inventory to dConvergedCharter's clause and to dWellOiledMachine's agent-instructions dissolution clause. Run the spawn-budget leg on a scratch clone with `tools/unattended/` removed.

**Left-shift gate:** the by-value inventory checklist entry (M4, M22).

### L10. The interpreter-floor inventory searches one value (id 41)

**Where:** register gap-tool-22, and v2 [chain] dSafePassage ("declared once and read from there by every reader").

**What is wrong:** the inventory is `git grep -l '3\.11'`, which misses `tools/settings-merge.py:3`'s "py>=3.10".

**Consequence:** after the raise to 3.15 a stale floor is still stated. This is documentation only.

**Fix (skeptic judged sound):** restate the query as a floor-statement search (for example `git grep -nE 'py ?[>≥]=? ?3\.[0-9]+|Python ?>= ?3\.[0-9]+|CPython 3\.[0-9]+\+'`) and re-point every hit.

**Left-shift gate:** that query as a leg after the floor unit lands.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=56 confirmed=53 refuted=3 unverified=0 blocker=0 high=6 medium=37 low=10 agents=11 out-tokens=290166
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38; [chain] all rows; memory plan [migration] and [integration] distribution row | high | high | confirmed | All three blobs matched their pins. P38 at v2:819-822 binds every build that changes what an adopter can see. Counting upgrade-step mentions per [chain] row (lines 1400-1420) gives non-zero only for dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter. dTotalRecall (1409: unknown front-matter keys refused, `journal` renamed `log`), dWellOiledMachine (1412: 'its hooks repacked'), dDeclaredLoop (1404: `REVIEW_ROUNDS` retired) and dLinkedLibrary (1410: `reuse_lookup.py` retired) all change adopter-visible surfaces and name no step. dSafePassage's row builds the step kind, `update` and the upgrade-walk leg, but no check reds a change that ships without a step. The memory plan's [integration] distribution row and [migration] 'In an adopter, the backfill runs as an update's upgrade step' are mapped to no build in its own [chain] table (lines 268-287). Built as written, an adopter's update across these builds can break with no step to walk. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38 'gov runs every step on itself first'; [chain] dShippedRelease, dOrderedCharter, dConvergedCharter | medium | medium | confirmed | AP-30 (away-pass:322) puts 'runs each new step on gov first' on dShippedRelease's lander unit, and v2:1417 carries it there. dOrderedCharter (1402) ships its own upgrade steps, and its only parent chain is dSafePassage then dGroundRules. dShippedRelease is not its ancestor: dConvergedCharter is the only row with dShippedRelease as a parent. The away-pass fold (466-476) patched gov-first for dSafePassage's floor step only. So dOrderedCharter's steps reach adopters having never run on gov, against P38's 'gov runs every step on itself first'. This shows the answer's placement conflicts with the chain order; it does not re-argue the answer. | sound | - |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] causes and pins; [practice] pinned facts; [migration] | medium | medium | confirmed | memory-plan [gates] (lines 308-318) arms the orphan check ('a record nothing reaches from a root') and the pins check ('across every record') with no legacy population. The positional rule in [practice] is the only one declared shrink-only over today's population. `git grep -l '^**Caused-by:**' -- memory` printed 0, so every existing non-root record is causeless. v2's dTotalRecall clause only refuses a missing cause at `record` write time, and [migration] rewrites no file. The gates therefore red the corpus the day they arm, or get exempted ad hoc. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] the journal collision paragraph; [migration]; v2 [chain] dTotalRecall | medium | medium | confirmed | `git grep` counted 1443 `**Serves:** journal` lines (the plan says 1,436). Code pins the token in four places: tools/runlog/record.py:82 SERVES_KIND = "journal", with :1467-1468 refusing any other kind; gen_build_index.py:550 RECORD_KIND_TOKENS includes journal; handoff.py:422 and migrate_backlog.py:934/945 emit it. memory-plan:106-107 renames the kind to `log`, while [migration]:295 says Serves lines are read 'with no file changed'. Neither v2:1409 nor the plan names an alias or a reader inventory. [migration] opens 'Nothing is rewritten by hand' and then says decision rows gain `decides` 'then by hand' (297-298). | sound | - |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `review.design.round-count`; [chain] dDeclaredLoop | medium | medium | confirmed | v2:965 bounds `review.design.round-count` by 'unattended's `RUNAWAY_CEILING`', and v2:1404 refuses 'a planted round count at the runaway ceiling'. The constant lives at tools/unattended/unattended.sh:774 (RUNAWAY_CEILING="8", refusal at :783, detector at :12474-12478). dWellOiledMachine (1412) dissolves the kit and dConvergedCharter retires it. The fates record and layer-runtime have 0 matches for runaway or REVIEW_ROUNDS, and the only build-record mentions are v2 and audit-fold. No row re-homes the constant. | sound | - |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall (gap-mem-40) and dWellOiledMachine (gap-tool-14) | medium | medium | confirmed | The away pass's AP-4 (296/426: README `ids:` defines a design-only build's units, exempt from the bindings check) and AP-16 (308/438: node, declared as a dependency) are settled answers. Grepping v2 and the memory plan for `ids:`, 'bindings check', 'node, declared' and 'hard dependency' finds no chain clause. The only JavaScript hits on rows 1409 and 1413 are tokenizers, edge extraction and portability arms. The register's gap-mem-40 (195) and gap-tool-14 (209, MED: node an undeclared hard dependency) are owned, but no unit on their rows builds the fix. | sound | - |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P35 'renders not-local or pruned, never empty'; [chain] dWellOiledMachine `gov trace` | medium | medium | confirmed | P35 (v2:808-809) requires 'not-local or pruned, never empty'. The only other carriers are memory-plan:218 and away-pass:195; no chain row carries it. dWellOiledMachine's clause (1412) reads '`gov trace <key>` and `gov why <key>` over the one index, each timeline bounded by `trace.rows` ... a fixture replaying four recorded events', with no three-state row and no planted not-local or pruned case. The optional-slot rule (v2:278), by contrast, is built and checked. | sound | - |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[doors] versus [sites], [practice] one door and [pockets] refs | medium | medium | confirmed | memory-plan [doors] (around 237-244) reads 'Five doors, one per site kind, and nothing else writes a node', listing instructions.edit, record, the commit queue, the handoff renderer and the supervisor. Three writers fall outside that list. [sites]:135 gives code edges the door 'the builder, under the annotation grammar' and :139 gives registry rows 'dTotalRecall's registry'. [pockets]:84 makes refs nodes ('claims, leases, mail') whose writers are none of the five. [practice] one door (121) says 'a write elsewhere reds', so one rule returns two verdicts. | sound | two-answers-to-one-question |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] refs row Owner; [pockets] policy values row | low | low | confirmed | memory-plan:84's refs row names dPlacedRequest as owner of 'claims, leases, mail'. layer-memory's kind table names dPlacedRequest for the lease (434), dKeptSession for the mailbox message (435) and dTotalRecall for the claim (460). Two owner fields disagree on the same nodes; the effect is limited to derived views. | sound | two-answers-to-one-question |
| 10 | coherence | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dKeptSession, the attendance rule | low | low | confirmed | v2:1406's dKeptSession attendance rule 'has owner questions asked live' and names a stand-in only for the `step —` announcement ('joining when dWellOiledMachine lands it'). v2:1408 places 'owner questions asked live while the build is attended' on dFurnishedOrders. dKeptSession's parents are dDeclaredLoop and dPlacedRequest, and its ancestry back to dGroundRules does not include dFurnishedOrders. The arm it tests is an actor swap, so the effect is contained, but the dependency is unstated. | sound | - |
| 11 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[sites] the record-section row versus the paragraph below the table | low | low | confirmed | memory-plan:133's [sites] record-section row reads 'then at most one line `**Edges:**` type=target type=target'. The paragraph at 141-142 reads 'a section with more types than fit takes one line per type'. The two wordings give a record check opposite verdicts on a two-line section. | sound | two-answers-to-one-question |
| 12 | coherence | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[sites] commit row; [edges]; [frame] versus [cycle] | low | low | confirmed | memory-plan:136 says `Pass:` and `Decided:` are each 'mapped to its edge type in the registry'. [edges] gives `Decided:` to `decides` (157) but declares `serves` only at the Serves line and the `Gov-Unit:`/`Gov-Item:` trailers (166); no type declares `Pass:`. `git log` shows Pass values are unit ids (e.g. TOOL-dSweptBranches-24) or 'none'. [frame]:32-34 also says 'seven of twelve hops typed', while [cycle] tabulates 14 hops with only record→unit plainly typed. The frame quotes the research return's own hop set, so the second half is a tally mismatch of low weight. | sound | two-answers-to-one-question |
| 13 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38; [chain] every row but dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter | high | medium | confirmed | Re-probed v2 at blob 0c6a17dc. P38 (line 819) says a build that changes what an adopter can see ships an upgrade step. Grepping each [chain] row for upgrade/P38/deprecat/shim finds step clauses only in dSafePassage (1401, the step kind and the floor step), dOrderedCharter (1402, 'its own upgrade steps'), dShippedRelease (1417) and dConvergedCharter (1420). Rows 1403 to 1416 and 1418 to 1419 name none, dBoundRoles, dWellOiledMachine, dTotalRecall, dLinkedLibrary, dDeclaredLoop and dMindYourWords among them. No arm anywhere reds a build that changes an adopter surface without a step. dConvergedCharter's widened exit check counts only steps pending, and upgrade-walk walks only declared steps. away-pass.md:210 does read '107 of the fates table's 131 rows'. The principle is still stated, so a later spec writer could honour it, which makes this medium rather than high. | unsound | - |
| 14 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine (the intake hook clause, 'its secrets redacted'); [layers] runtime | high | - | refuted | The premise is false on re-probe. The sibling flow-steps.md:86-88 says the intake prompt 'passes the secret scanner runlog ships (`scan_secrets` and its closed class list), which moves into the core with runlog's journal grammar. A match is redacted in the record'. v2's dWellOiledMachine row (1412) carries 'the journal grammar moved into the core' and 'the secret value scan at every boundary that publishes'. tools/runlog/runlog_lib.py:522 holds scan_secrets and :553 render_redacted, both in the same runlog_lib module that fates.md:127 MERGES into the core journal. So the design does move the scanner and its class table into the core, and the hook needs neither an optional-kit import nor ad hoc rules. A missing fates row for redaction.tsv is fates-coverage detail, which id=15 covers. | sound | - |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter ('every part in the fates table at its fate, the table's join run as convergence's exit check') | medium | medium | confirmed | fates.md says it covers 'every shipped kit, each function in it'. `grep -c -F 'help/'` and `grep -c roles.json` on fates printed 0 each. Fates also printed 0 for pre_push_bar_selftest, check_by_design_parity, orient.agent, subject-pins, registry.toml, redaction and product.md. The checks at fates.md:228-240 admit only kit nodes, top-level, skills, .githooks and guides as row kits, and none of them derives the population from the tree. `git ls-files help .claude` lists help/README.md, .claude/roles.json and .claude/rules/product.md, which no fate row names. v2 1420 runs 'the table's join' as the exit check, so unlisted parts pass it unchecked. | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dGroundRules (the JSON mirror's hash check and parity leg) and dSafePassage ('up, down byte-identical'); register gap-tool-13 | medium | - | refuted | The premise is false on re-probe for the mirror. The evidence reproduces: core.autocrlf=true, `* text=auto`, 141 w/crlf files, policy.toml and settings.json w/crlf. But v2's dGroundRules row (1400) has every consumer 'reading the mirror from the landed revision's blob, or checking its hash against the TOML at that revision'. Blob content is LF-normalised, so the hash is not taken over working-tree bytes and a CRLF checkout does not read as tampered. The fixture's up/down byte identity is compared within one checkout on one node, so the claimed flip with autocrlf is speculation and not shown. The finder graded it medium, and it does not establish. | sound | - |
| 17 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P37 and P28; [chain] dOrderedCharter (the portable practice) and dWitnessedBar (the portability leg pack) | medium | medium | confirmed | tools/gate-lint/encoding_posture.py:2 is the Python text-IO encoding scan, and gate-legs.json:231 runs it with sh_hygiene at 165-217. fates.md:42 makes gate-lint 'optional \| a Flow leg pack', and :160 says 'leg pack, expansion'. P37 (v2:814-818) puts encoding 'each rule with its leg' in one rule set. dWitnessedBar's portability pack (1413) adds only 'encoding arms for stdout and JavaScript', a bare-shell-name arm and a floor arm, and dOrderedCharter's 'each rule paired with its leg' names no leg for Python file IO. On a core-only install, P37's Python encoding rule therefore has only an optional-kit leg. | sound | - |
| 18 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] 'Claude transcripts' row ('kept 365 days'); [sessions] | medium | low | confirmed | memory-plan.md:89 reads 'Claude transcripts ... kept 365 days'. Grepping the settings files found `cleanupPeriodDays: 365` only in the node's user ~/.claude/settings.json, and none in the project settings. The harness default is 30 days, and no design record except the research return mentions cleanupPeriod. P35 already renders an aged-out hop as `pruned`, never empty, so behaviour degrades as designed. The defect is a node-specific figure stated as a platform fact, plus a retention that is never measured. | sound | - |
| 19 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] (the closing paragraph: Serves kind `journal` renamed `log`); [migration]; v2 [chain] dTotalRecall ('the Serves kind `journal` renamed `log`') | medium | medium | confirmed | `git grep -l '^\*\*Serves:\*\* journal' -- memory \| wc -l` printed 1443. gen_build_index.py:550 hard-codes 'journal' in RECORD_KIND_TOKENS. memory-plan.md:106-107 renames the kind to `log` when dTotalRecall's registry lands, but neither [migration] (:293-300) nor v2's dTotalRecall row says whether the old records keep reading through an alias. Neither names the readers to re-point or an adopter step. The plan's 'retire, never vanish' practice (:123) and 'Nothing is rewritten ... with no file changed' (:293-294) point to an alias without stating it for this rename. | sound | - |
| 20 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] 'pins'; [practice] 'pinned facts' row | medium | medium | confirmed | memory-plan.md:316 arms 'pins: a quoted derived fact with no pin on its line, across every record'. :118 defines the fact only loosely, as 'a count, a size, a path's length', and gives no legacy or shrink-only population, while positional (:115) is shrink-only. map.py:538-547 shows the arm being generalised: its COUNT regex matches only map node/byte counts and the critical path, and it 'does not read ... any other count'. The plan's own unpinned figures are stale at HEAD: the Serves count at :32 is 2,278 against 2306 now, and the commit count at :83 is 6,084 against 6090. Generalised as written, the gate is either undefined or reds frozen records. | sound | - |
| 21 | grounding | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] 'promotion'; [pockets] 'auto-memory' row | medium | medium | confirmed | memory-plan.md:317 arms 'promotion: a standing directive found in memory and not promoted', and :92 places the auto-memory at node-local `~/.claude/projects/<repo>/memory/`. `ls` of that directory printed 90 files on this node. [gates] names no runner and does not say whether this is a bar leg or a node reading, while P3/dWitnessedBar key the runner-written verdict to the tree. remote-ci.yml runs on a fresh windows-latest runner with no auto-memory, so a bar-leg build would make the verdict depend on the node. | sound | - |
| 22 | grounding | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P3 | low | low | confirmed | v2:625-627 reads 'because remote CI is not available (R4.4)'. .github/workflows/remote-ci.yml:31-35 triggers on push to main, schedule and dispatch, and :10 reads 'it blocks nothing'. Gap register line 30 draws 'remote CI (after the fact, blocks nothing)', and gap-test-02 (297) says the same. The ground P3 states is false of today's tree, though the principle's direction, local-first, is unaffected. | sound | - |
| 23 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] rows dFairHearing, dBoundRoles, dLinkedLibrary; gap register gap-test-18 | high | medium | confirmed | `git merge-base --is-ancestor` printed notinmain and notmerged for origin/branch/deterministic-reuse-workflows-f70c33. `git ls-tree` lists the aScoutedSeam bench.py, cases.json, results.json and judge.js only on that branch, and `git ls-files \| grep -i scoutedseam` printed nothing. v2 1403 extracts the scorer factory 'with aScoutedSeam's grader as its second instance', 1407 takes experiment parts from 'aScoutedSeam's benchmark', and 1410 accepts by 're-running aScoutedSeam's benchmark'. No chain or [owed] item lands those files. The sibling layer-roles.md:644 does pin the branch at b0fe68f30, so a builder can find them, and the consequence is contained: medium, not high. | sound | - |
| 24 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] rows commits.edge-check, commits.squash, trace.identity, memory.legacy-anchors; [presets]; [chain] dWellOiledMachine, dShippedRelease, dTotalRecall; memory plan [keys] | high | medium | confirmed | The catalogue lists the values: v2:1076 `commits.edge-check` push-leg/commit-msg/off, :1077 `commits.squash` re-emit-union/refuse/accept-loss, :1078 `trace.identity` with salted, and :1063 `memory.legacy-anchors` with retag. Strict selects commit-msg and refuse (:1353-1354). dWellOiledMachine (1412) builds only 'the commit-key leg at the push ... as `commits.edge-check` says', and its seen-red cases are push-leg and act-only/session only. dShippedRelease (1417) builds only 're-emitting the union'. dTotalRecall (1409) covers derived anchors only, and no clause arms commit-msg, refuse, accept-loss, salted or retag. Elsewhere the design arms every value explicitly, for example 'each `instructions.edit` value given its arm, witness and planted red'. That makes 'as X says' an incomplete route for these values, but the clauses at least defer to the key, so medium. | sound | policy-value-with-no-route |
| 25 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall and dLinkedLibrary; memory plan [pockets] row 'recall index' | medium | medium | confirmed | The three blobs match their pins. v2:1409 (dTotalRecall) builds "`record find`, its last line naming the total past 40 rows, and `record show` over the one index". v2:1410 (dLinkedLibrary) separately says "memory-recall narrowed to a record finder". Neither row names query.py or check-recall. fates.md:118 and :122 give query.py and check-recall to dTotalRecall, but memory-plan.md:101 gives the recall-index pocket to dLinkedLibrary. So the finder is split across two builds and its owner is ambiguous. One reading is that dLinkedLibrary only trims the rest of memory-recall after dTotalRecall's finder exists, which limits the risk to a misleading split rather than certain duplicate code. | sound | - |
| 26 | reuse | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[integration] flow row; [migration] 'Old commits'; v2 [chain] dDeclaredLoop and dLinkedLibrary | medium | medium | confirmed | v2:1404 reads "`Pass:` and `Decided:` registered with one reader", and memory-plan.md:259 reads "one reader for `Pass:`, whose two readers disagree today". routed_commits.py:22-25 documents the difference as deliberate: it takes the UNION, while unattended's `read_attribution_tokens` (used at check-brief-recorded.sh:306) has the trailer REPLACE the subject, because the two answer different questions. runlog/model.py:593 is a third reader of `Decided:`. No record names these seams. A builder who follows "one reader" could collapse union and replace into one rule and change one leg's answers. | sound | - |
| 27 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dCalibratedLens, dTotalRecall and dLinkedLibrary replay clauses vs dFairHearing's scorer factory | medium | medium | confirmed | v2:1403 builds dFairHearing's scorer factory, which pairs the cases every variant answered and refuses a partial population. Three later clauses specify scoring without citing it: v2:1409 "the replay with the map and without at its first unit", v2:1410 "the replay's losing test extended to code ... with the `code` slot and without it" and v2:1419 "instruction evals: a replay suite". A grep for 'scorer' in v2 matched only 1403 and 1407. gap-register:313 (gap-test-18) records two scorer instances as a defect, so a builder working from these clauses could repeat it. | sound | - |
| 28 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWitnessedBar, 'one bash resolver in `tools/lib`' clause | medium | medium | confirmed | The v2:1413 clause specifies only Git's `bin/bash.exe` from `git --exec-path` before PATH, System32 and WindowsApps refused, and "a refusal in place of any fall-back". It never mentions GOV_BASH. grep finds no GOV_BASH in any dClosedLoop build record; the only hit is in run A's untracked review file. git grep shows GOV_BASH honoured first in govkit.py:1171, corpus_ids.py:409, lexicon/selftest.py:62 and others, with a set but unusable value refused by name. govkit/selftest.py:15269 tests that refusal. govkit.py:1150-1152 says the resolver is duplicated because govkit is COPY-INSTALLED. A resolver built from the clause alone would drop the override contract. | sound | - |
| 29 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWitnessedBar, the baseline ledger factory clause | medium | medium | confirmed | v2:1413 says "its TSV rows merged by a row-keyed driver" and names no seam. A grep over the build records found no 'merge-rows' or 'row-keyed' alongside the ledger; v2 names merge-rows.py only as a grammar importer (1402) and in merge-rows.test.sh's PEP 701 ban (1401). tools/memory-tree/merge-rows.py:6 is already "A row-keyed three-way merge driver", with postconditions on the written bytes. The clause invites a second driver whose guarantees differ. | sound | - |
| 30 | reuse | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter 'the record-kind factory and its conformance gate' vs dTotalRecall's record-kind registry | medium | medium | confirmed | v2:1409 (dTotalRecall) builds the record-kind registry with "templates and checks generated from it", which is in effect the factory. v2:1420 (dConvergedCharter) separately builds "the record-kind factory and its conformance gate" without referring to that registry. v2:27 and P16 (v2:728) say each kind's factory and gate lands with its owning build, so placing the record-kind factory in the final build contradicts the principle. It also leaves the kinds added in between without the conformance gate. | sound | - |
| 31 | reuse | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] (and [view], which draws from it) | medium | medium | confirmed | The memory plan's [pockets] table (lines 58-104) claims every pocket but has no row for `.governance/deploy.toml`. grep -c 'deploy.toml' gives 0 in both v2 and memory-plan.md, and 'install.json\|receipt' gives 0 in memory-plan.md. `head -30 .governance/deploy.toml` shows a COMMITTED file that "carries every owner decision" and selects the kits that render into gov's charter. The charter row covers only `AGENTS.md`. The overlay that feeds it therefore has no node, key, door or owner. | sound | - |
| 32 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall row, clause 'the kind registry completed ... the Serves kind `journal` renamed `log`'; memory plan [pockets] closing note and [migration] 'Serves lines' | high | medium | confirmed | The re-probe reproduces. git grep counts 1443 `**Serves:** journal` lines. Each reader is present: check-memory-hygiene.sh:3005 sets j only on `journal`, and check 23 (:3191) fails on no journal evidence. gen_build_index.py:550 RECORD_KIND_TOKENS, runlog/record.py:82 SERVES_KIND = "journal", WIRE-INTO-PROJECT.md:418, HYGIENE.template.md:575 and adopt-memory-tree.sh:721 also read it. v2 dTotalRecall says only "the Serves kind `journal` renamed `log`", with no readers, no rule for legacy records and no adopter step. memory-plan [migration] says Serves lines change no file, which leaves the rename's mechanism undecided. Graded medium rather than high: the bar's check 23 would go red on the first `log` record, so the break is loud rather than shipped silently. | sound | retirement-inventory-misses-readers-by-value |
| 33 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[pockets] row 'orientation cards ... retired into the session binding \| dWellOiledMachine'; v2 [chain] dWellOiledMachine and dPlacedRequest rows | high | medium | confirmed | memory-plan.md [pockets] retires the per-session cards at `<git-common-dir>/orientation/<id>.md` under dWellOiledMachine. scratch-guard.js:671 reads exactly that path, and :1180-1183 denies a routed write when the card is absent. fates.md:155 keeps scratch-guard (STAYS). grep for scratch-guard, orientation/ or ROUTED_PATHS in v2 gives 0. One part of the claim is overstated: v2:1416 gives dScopedBuild "a write gate reading derived state", so the gate's re-point has an owner. But dScopedBuild depends on dWellOiledMachine and lands after it, and no clause re-points the route read in the retiring unit. Between the two builds the gate would read a file nothing writes. | sound | - |
| 34 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[principles] P38; [chain] dSafePassage row; the rows of dTotalRecall, dLinkedLibrary, dDeclaredLoop, dWellOiledMachine, dWitnessedBar and dMindYourWords | high | high | confirmed | P38 (v2:819-822) promises that a build changing an adopter-visible surface ships an upgrade step. grep finds upgrade steps declared only at v2:820 and in the dSafePassage, dOrderedCharter, dShippedRelease and dConvergedCharter rows. dSafePassage's `upgrade-walk` leg (v2:1401) walks only the steps that exist and their planted cases; nothing reds on a changed surface that has no step. Several rows change installed surfaces with no step named, for example v2:1410 "`reuse_lookup.py` retired", which the receipt fixture installs (fixture line 68). Some conf keys are covered by the translation window's legacy-home population (v2:1400, REVIEW_ROUNDS), but installed files, hooks and wiring have no such gate. | sound | rule-stated-with-no-check-that-fails |
| 35 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `install.deprecation-window`, [presets] pair rule, [chain] dSafePassage (forwarding shim) and dConvergedCharter ('every shim removed when its window closes') | medium | medium | confirmed | `git tag` lists only three archive/* tags and no kit release. v2:1089 counts `install.deprecation-window` in releases, and v2:994 counts `currency.max-behind` in releases behind. Both are owned or used before v2:1001's `kits.cadence`, which dShippedRelease owns and which is the first thing to cut releases. dSafePassage's shim (v2:1401) is "kept for `install.deprecation-window` releases", and no record says what counts as a release before the first cut. Builds in between, such as dOrderedCharter's moves and dLinkedLibrary's retirements, create shims whose windows cannot be measured. | sound | - |
| 36 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dOrderedCharter row, clause 'map_lib re-exports the moved names for one release' and 'the map_lib re-export declared as a deprecation (P38)' | medium | low | confirmed | v2:1402 fixes the re-export at "for one release", while v2:1089 and :1111-1113 set the window default to 2 with a pair rule of at least `currency.max-behind`. dSafePassage's shim covers only "a moved command or hook path". The contradiction is real, but the finder's breakage path does not hold. A behind adopter still has its old copy-installed map_lib. Per v2:1402, `update` re-copies the template together with the kit, so the copied test's import does not break across an update. What remains is a contradiction between the clause and the policy, with no demonstrated runtime break. | sound | - |
| 37 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dShippedRelease ('the lander running each new upgrade step on gov's own tree') vs P38 'gov runs every step on itself first'; dSafePassage | medium | medium | confirmed | v2:1401 runs only the floor step on gov's tree. v2:1402 has dOrderedCharter declare 'its own upgrade steps: agent-instructions' wiring moved ... map_lib re-export declared as a deprecation (P38)', and dOrderedCharter lands before dShippedRelease. v2:1417 has the lander run 'each new upgrade step on gov's own tree', and that lander only exists from dShippedRelease on. No row between them runs their steps on gov. P38 (v2:821) says 'gov runs every step on itself first'. The answers-compared fold 'ap30-self-run' fixed the same class only for the floor step. | sound | - |
| 38 | blast-radius | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[integration] distribution row and [migration] 'In an adopter'; [chain] table | medium | low | confirmed | memory-plan:265 and :303 say the backfill runs in each adopter as an update's upgrade step. The plan's [chain] table (274-286) lists no such unit. In v2, 'backfill' appears only in dTotalRecall/dLinkedLibrary's research-return backfill, so no clause builds the step. The impact is overstated, though. dTotalRecall's clause (v2:1409) reads Serves lines as edges and derives anchors 'as memory.legacy-anchors says', and that key's default rewrites no file (memory-plan:339). So under the default, adopters do get derived edges with no step. The gap that remains is an orphaned promise plus the unbuilt `retag` path. | sound | - |
| 39 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter clause 'the unattended kit, its four guides and /unattended retired ... the kit's README and the product rule's "four-verb driver" corrected' | medium | low | confirmed | Re-probed. fork-ceilings.txt:15-16 copy $ROOT/.unattended.conf and run tools/unattended/unattended.sh and check-unattended.sh. gate-legs.json runs fork-count.sh over that file. method-carriers.txt:5,10,11,15,16,23 name unattended files. README.md:17 and :57 advertise both kits. The dConvergedCharter clause (v2:1420) names only 'the kit's README and the product rule's "four-verb driver"', while the same row lists readers by name for other moves. Graded low because the fork-count break reds the bar at the retiring unit (loud, not shipped), and the README is documentation. | sound | retirement-inventory-misses-readers-by-value |
| 40 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dLinkedLibrary clause '`reuse_lookup.py` retired with its readers rewritten' | medium | - | refuted | The cited section already says it. v2:1410 reads '`reuse_lookup.py` retired with its readers rewritten', and check-memory-hygiene.sh:2474-2480 and the templates are those readers. The claimed impact (the hygiene check still demands a reuse_lookup citation) assumes the readers are not rewritten, which contradicts the clause. The adopter window is governed by P38 (v2:819-822), which binds every build that changes what an adopter can see. Naming each of the 31 files is the unit-level detail the BY DESIGN block leaves to the build's own spec. | sound | retirement-inventory-misses-readers-by-value |
| 41 | blast-radius | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:gap-tool-22 (and v2 [chain] dSafePassage 'declared once and read from there by every reader') | low | low | confirmed | tools/settings-merge.py:3 reads 'py>=3.10 (write_text newline=)'. gap-tool-22 (register:217) builds its inventory from `git grep -l '3\.11'`, so it misses a floor statement made with a different version. dSafePassage promises the floor is 'declared once and read from there by every reader'. The effect is documentation only. | sound | retirement-inventory-misses-readers-by-value |
| 42 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `policy.proof` and `instructions.proof` rows; [witnesses]; [chain] dGroundRules (the minimal guard) and dDeclaredLoop (the guard, the TTY CLI) | high | high | confirmed | layer-instruction:557-559 asserts 'An agent's shell call cannot pass the proof'. The walkthrough (:127-129) and v2 [witnesses] (:1374-1375) rest the guard on 'a policy CLI that needs an interactive terminal' plus a trailer that a push gate checks. No record says what makes the TTY check or the trailer unforgeable. A grep for pty, pseudo-term, winpty or adversar over the subject records found nothing. A pty wrapper (script, python pty, winpty in Git Bash) makes isatty true for an agent's Bash call, so the stated guarantee is false. The owner's choice of tty-cli is not re-argued: the defect is the unfounded claim, and the floor invariants that rest on it. | unsound | - |
| 43 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[policies] `runtime.act-auth` row (line 1085); [chain] dWellOiledMachine ("each read from the node's credential store and never from a file") | high | medium | confirmed | v2:1085 and :1412 say each credential, oauth-shared included, is 'read from the node's credential store and never from a file'. `ls -la ~/.claude/.credentials.json` on this Windows node shows the harness's shared OAuth login is a file. `runtime.secret-home` (v2:940) offers os-keychain or env-injected, and a grep for libsecret, keyring or Credential Manager over the subjects found no named headless-Linux store. The rule is ambiguous about who reads, and taken literally it refuses the default second credential. Graded medium: the failure is a loud launch refusal, not a wrong result. | sound | - |
| 44 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine ("preflight refusing a launch that skips hooks or permissions", the harness conformance fixture's "fail-closed path") and dShippedRelease ("Codex install targets with their trust step surfaced"); P36 | high | medium | confirmed | research-harness-cli.md:52 and layer-runtime:799 record that Codex trusts each project hook by hash and skips an untrusted hook. v2 says only 'Codex install targets with their trust step surfaced' (dShippedRelease, :1417) and 'preflight refusing a launch that skips hooks or permissions' (dWellOiledMachine, :1412). Neither names re-trust after an update that changes a hook's bytes, or a hash comparison at preflight. The general preflight wording could be read to cover it, but nothing designs how. Graded medium because it applies only where an operator selects runtime.act-harness: codex. | sound | - |
| 45 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] commits and causes; [families] runtime row; [doors]; mirrored in v2 [chain] dWellOiledMachine ("the commit-key leg at the push reading the binding") | high | high | confirmed | memory-plan:48 makes the runtime family, acts and session bindings included, 'node-local'. :86 has the supervisor write them. :190/:242 make the session binding a root that caused-by chains reach. [gates] (:311-313) checks Gov-Act against 'the binding' and checks orphans 'from a root'. AP-6 puts the check at a push leg 'reading the binding'. The only off-node rule is for transcripts ('not-local', :217-218); nothing covers bindings at a lander, a peer verifier or remote CI. In a product built for several machines on one repo this path is the common case, so the gate either false-reds other nodes' work or is quietly scoped to certify nothing. | sound | - |
| 46 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[gates] causes, pins and work orders, against [migration] | high | medium | confirmed | Re-probed. `git grep -l -F '**Caused-by:**' -- memory` prints 1, Serves prints 2449, prompts total 602 and gov:handoff marks 67. memory-plan:115 scopes only `positional` as shrink-only over today's population. The pins gate is explicitly 'across every record' (:316), and the causes and work-order gates have no scope. [migration] (:291-303) migrates none of these populations. As specified, the gates red the tree at arming or get an undeclared scope. Graded medium because arming them on today's tree shows the problem at once. | sound | - |
| 47 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine ("intake for a prompt that reaches no owner session, through the mailbox's `intake` message or a cadence filer"), dKeptSession (the `intake` message kind) and dRankedPlan (intake read as ratification); P4 | high | medium | confirmed | flow-steps:103-105 records a mailbox `intake` message as intake through dWellOiledMachine's filer, 'placed by entry.place the same way'. v2:1406 adds the kind to the mailbox, which coordination:99-108 lets any sender append by CAS. No record restricts who sends intake or marks its origin. dRankedPlan (v2:1414) names the hook-written intake log as the ratification, which narrows the path, but the filer writes the same intake kind and nothing excludes it. Graded medium: the result is unmandated work that still passes the bar and landing review. | sound | - |
| 48 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage (`update` walking every step; the release-0 fixture and `upgrade-walk` leg); P38 | high | high | confirmed | v2:1401 specifies the walk and the release-0 fixture only for success ('up, down byte-identical, up again ... each step seen load-bearing'). away-pass [p6-distribution] (:214-224) gives no route for a failing or interrupted step. research-supersession:112 notes 'per-kit rollback (exists) plus reverse down steps', but no subject adopts it for a mid-walk failure, or orders the witness write last. Combined with 'each skipped when its witness holds', an interrupted step can be skipped as done on re-run and leave a half-migrated tree under a current receipt. | sound | - |
| 49 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dWellOiledMachine (the supervisor: "started and restarted by the node tick", fencing epochs) | high | high | confirmed | Re-read layer-runtime.md:401-419 and 455-458. The epoch is bumped only "at every take-over". A supervisor kills only "the act sessions it launched under the old epoch" once it finds its lease taken over. The same-node kill is described only for a take-over. Line 367 has the node tick start a supervisor "when none beats under a live lease", and nothing says whether that restart is a take-over or what epoch it runs under. Each act's --session-id is recorded with its epoch (line 405), but no record has a restarted supervisor read those records before its first `next`. The fixtures at 1191-1203 (fencing, idempotence, host) cover a cross-node take-over and a reboot, not a same-node restart while an act is still live. The per-beat reap-orphans sweep (line 440) kills only flagged rows whose parent is gone (process-monitor.template.conf:56). The design neither ties it to act sessions nor orders it before `next`. So a duplicate act in one worktree goes unaddressed, a wrong result on a narrow path. | sound | - |
| 50 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[frame] node addresses, [sites] a record's section, and the shared grammar under [practice] | medium | medium | confirmed | memory-plan.md:20 addresses a section as `<doc> [<seg>]`, which contains a space. Line 126 gives the shared grammar as `type=target[,target]`, and line 133 has the section site carry "at most one line `**Edges:** type=target type=target`", with space-separated pairs. Lines 141-142 then say "a section with more types than fit takes one line per type", which contradicts "at most one line". The `id#tag` form exists in systems.md:183/481 and in v2's dRankedPlan, but the memory plan never names it as the edge-target encoding. Two readers could tokenize the line differently. The effect is contained to the edge index. | sound | - |
| 51 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:[doors] ("Five doors ... and nothing else writes a node") and [practice] one door | medium | medium | confirmed | memory-plan.md [doors] reads "Five doors, one per site kind, and nothing else writes a node", and [practice] line 121 says "a write elsewhere reds". [pockets] declares nodes that none of the five writes: refs (claims, leases, mail, line 84), written by the coordination verbs; view kinds (lines 96-101), written by renderers; `kit-release` tags (line 85); and the code record, which is derived. [sites] line 135 itself names "the builder" as the door for code annotations, which [doors] omits. Some examples in the finding overreach: verdict and landing records can go through `record`, and policy values are instruction units under instructions.edit. The core claim holds even so. A one-door check built from the five-door list either reds legitimate writes or is exempted ad hoc. | sound | - |
| 52 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage (gov's remote CI "pinned by full commit sha") against dShippedRelease ("optional emitted CI", "a Linux job in emitted CI that sets up Python at the floor") | medium | medium | confirmed | In v2:1401 (dSafePassage), the full-commit-SHA pin applies only to jobs of `.github/workflows/remote-ci.yml`. v2:1417 (dShippedRelease) has "optional emitted CI" and "a Linux job in emitted CI that sets up Python at the floor" with no pin. A grep for pinning over layer-expansions and the gap register found no emitted-CI pin. All four `uses:` lines in .github/workflows/remote-ci.yml are SHA-pinned, so the pattern exists, but the class is unspecified for adopters. | sound | - |
| 53 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dSafePassage (the `[[upgrade]]` row: "up and down argv run from gov's checkout ... whether it needs the target's code") against dShippedRelease (`kits.offer` sandbox) | medium | medium | confirmed | v2:1401's step kind declares id, introducing commit, up/down argv "run from gov's checkout", witness, surfaces and "whether it needs the target's code". It gives no execution contract: no working directory, no environment scrub, no -I and no hooksPath. Nothing checks the self-declared needs-target-code field. The isolation in layer-expansions.md (`kits.offer` row) is scoped to update's own git writes ("runs git there with core.hooksPath pointed at an empty directory") and to the eight enumerated kinds. An upgrade step's own argv is not among them, and the gap-deploy-13 row lists eight kinds with no upgrade step. v2:1417 has kits.offer "running the steps that need no target code, as install.steps says", so the unattended path rests on the unchecked self-declaration. The attended-path part of the claim is weaker, since attended update already runs target code by design. The unattended gap stands. | sound | - |
| 54 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dTotalRecall (the core `code` record "derived per blob ... cached by tree hash"); P32; [owed] the night pass's cold-derivation check | medium | medium | confirmed | v2:1409's code-record clause and night-pass.md:201-206 give "derived per blob ... cached by tree hash" in the languages `memory.code-languages` names, measured "13.1 s cold and 941 KB" on this tree only. v2:1530 ([owed]) re-times it at dTotalRecall's first unit, again on gov's tree. A grep for vendor, minified, binary, lfs, submodule, per-file and exclude over night-pass, layer-memory, systems, project-map, v2 and the memory plan matched nothing relevant. The level-0 map has a budget with degradation (v2:1409), but the core code record declares no exclusions, no per-file cap and no over-ceiling behaviour for an adopter's tree. | sound | - |
| 55 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dLinkedLibrary ("the span rule: a definition's extent where one derives, `gov:end <tag>` only where none does"); P33; memory plan [gates] | medium | medium | confirmed | night-pass.md:256-261 and systems.md:293-294 define the span only as "a definition's extent where one derives, gov:end <tag> closes it only where none does". No record defines an unterminated note outside a definition, an orphan gov:end, nested or crossed tags, or a mismatch. memory-plan [gates] (edges, causes, commits, work orders, positional, pins, promotion) has no span arm, and the dLinkedLibrary row's `annotations.grammar` resolve check names none either. The finding's impact overstates frequency: the research return (research-relational-syntax.md:99) puts only 6 of 57 spans in need of gov:end, since most of the 68% are single-line uses. The missing definition and check are still real. | sound | - |
| 56 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:[chain] dConvergedCharter ("superseded parts retired through ratified proposals" and "every part in the fates table at its fate, the table's join run as convergence's exit check") | medium | medium | confirmed | v2:1420 (dConvergedCharter) holds both "superseded parts retired through ratified proposals" and "every part in the fates table at its fate, the table's join run as convergence's exit check". fates.md [check] lists the design map's joins with no declined-ratification outcome. A grep for reject or declin in fates.md found none. layer-expansions `loop.file` has a keep record for a Loop Review row the owner keeps, but nothing makes the fates-table join read it or amend the part's fate. A declined retirement therefore leaves the exit check red with no route. | sound | owner-item-without-its-reject-outcome |
