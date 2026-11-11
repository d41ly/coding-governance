**Serves:** journal TOOL-dDeclaredLoop-30

# gov-spec-writer handoff — TOOL-dDeclaredLoop-30

<!-- gov:handoff role=gov-spec-writer build=dDeclaredLoop unit=TOOL-dDeclaredLoop-30 path=memory/builds/dDeclaredLoop/prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-30-2-spec-writer.md role-sha=dcd8416ea3d2 task-sha=d1c814da5a16 -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dDeclaredLoop`, unit `TOOL-dDeclaredLoop-30`.
Not supplied, optional: `card:route`.

### brief:goal

Revise TOOL-dDeclaredLoop-20, -21, -30, -31 and -32 so every statement of when a review loop ends and where its findings go agrees with TOOL-dDeclaredLoop-32 rev-3 and TOOL-dFairHearing-17 rev-4: a spec subject takes `no-fall`, ends at its target or bound and is promoted to units, and BUILD-METHOD M4's spec-audit rule disposes its findings and stops its chain; closing-review follow-ups and fix passes keep strict fall and budget routing. dl20 and dl32 are this build's own specs; their fixes here correct the text the rev-3 fold left behind.

### brief:items

Read the cross-check record first, `memory/builds/dDeclaredLoop/build/2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dDeclaredLoop/build/2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 32: specs 32 and 20

- **dl32, row 28, §4 "byte-for-byte".** The paragraph keeping dl21's four tests says "with neither new argument the function is byte-for-byte its predecessor", though the grammar now gates the second test on `no-fall` and has three new arguments. State that the second test is gated by `no-fall` and that with arguments 4 to 6 unset the behaviour equals dl21's.
- **dl32, row 29, the asks sentence and the Rollout sentence.** "A review loop's open findings go to asks once the budget is spent" becomes a closing-review loop's; "The landing turns the rule on for every subject at once" becomes every closing-review and fix-pass subject.
- **dl32, row 30, S6, check 2.** S6 widens check 2's non-decrease reading to every subject, though check 2's non-convergent red would then fire on a legally flat `no-fall` spec subject. Limit the flat reading to the build slug and fix-pass rows, re-cite the reading by name rather than `:842`, and add to AC7 a plant of a flat, non-terminal spec subject that stays green.
- **dl32, row 31, the edge to dl20.** dl32 says `review.dispose` promotes by the target it writes, while dl20's dispose row routes a new mechanism by the budget. Fold with dl20 below: the edge states that a spec subject's target is always ` · to units`.
- **dl32, row 27 (pre-existing), the `roundLimit` claim.** dl32 says it passes `review.max-rounds` to TOOL-dFairHearing-17's harness as `roundLimit`; no scope item does. Decided: drop the claim, and say no dDeclaredLoop unit takes up fh17's `roundLimit` edge. The edge itself is reported to dFairHearing, whose run is live.
- **dl20, the dispose row and S8, the rev-3 fold's leftovers.** (a) The `item.review.dispose` row sends a spec audit's new-mechanism finding to asks once the budget is spent; state that a spec subject's promotion takes dl32's target, always units. (b) S8, the `item.review.fold` row and AC1 give the fold a NON-CONVERGENT route a `no-fall` spec subject never reaches; replace it with the spec subject's terminal states, BOUNDED or CEILING. (c) The trigger row and the dl32 edge refuse a round past `flow.route-backs` for every subject; limit it to the build slug, as dl32 S2 does. (d) Pre-existing: the dispose row's routes lack the plan-revision and landing-record routes that §3 and the note under the table call its declared routes; add them to the row as declared and unarmed, or make §3 and the note say they are not yet declared, whichever the row's own §3 supports.

#### Group B, led by spec 30: specs 30, 31 and 21

- **dl30, row 17, §3 non-goal.** It gives dl32 "the strict-decrease routing of every `until-*` and `while-*` value". Limit it to `while-*` follow-ups and fix passes, and name BUILD-METHOD M4's spec-audit rule as the owner of a spec audit's stop and disposal.
- **dl30, row 18, S6, the per-item early limit.** Past `flow.route-backs` any item's loop ends `non-converging`, a spec subject included. State that the limit ends follow-up, fix-pass and route-back items only, and that a spec subject's draws are counted but never end its loop (dl32 S2, S3).
- **dl30, row 19, S4, `exhausted`.** Every draw site stops its repetition on `exhausted`. Decided: a spec subject's `review-round` draw is still made and counted, but an `exhausted` answer does not refuse its round; it ends at its target or bound (dl32 S3, S4). Say so in S4 and in the driver paragraph, and add a plant to AC7 or the nearest criterion that reds when a spec subject's round is refused on a spent budget.
- **dl31, row 22, §3 non-goal.** "When a loop ends and where its findings go" is dl32's for follow-up and fix-pass loops; a spec audit's end and disposal are BUILD-METHOD M4's spec-audit rule's. The ` · to on-exhausted` sentence is unchanged.
- **dl21, row 10, §4.** The non-decrease reading applies to the closing-review subject; a spec audit passes `no-fall` (dl32 S3) and ends at its target, BOUNDED or CEILING.
- **dl21, row 11, §3 non-goal.** Name dl32 for follow-ups and fix passes, and M4's spec-audit rule, through dl20's dispose row, for spec audits.
- **dl21, row 14, S4 and F4, the `REVIEW_ROUNDS` readers.** The M4 rewrite left a second mention in `tools/memory-tree/BUILD-METHOD.template.md`, the chain paragraph ("Each generation is a FRESH subject, so `REVIEW_ROUNDS` bounds no chain"). S4 lists both readers and rewords the second so no policy key reads as a chain stop.
- **dl21, row 5 (pre-existing), S3, the parity arm's ceiling.** S3 re-points fh17's parity arm to take the ceiling "as its own variable" but names no value; at the default, fh17's limit-4 row reads CEILING in the driver and BOUNDED in the harness. State that the arm sets the ceiling variable from each row's limit so the driver's ceiling is one round past it, as fh17's harness rule is.
- **dl21, row 7 (pre-existing), the `roundLimit` claim.** Drop the claim that dl32 passes `review.max-rounds` to fh17's harness as `roundLimit` (the non-goal and its edge line), as Group A drops it from dl32.

### brief:acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md`.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  specs staged into it through `GIT_INDEX_FILE`, names nothing of your specs. Delete the copy after.
  Findings that only a `gen_build_index.py --write` render cures belong to the main loop: name them and
  leave them.

### brief:gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### brief:non-goals

- No file outside the specs your group names. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of another build. A parent spec that looks wrong is a line in your return, not an edit.
- No fork opened or re-opened; a fork the owner's picks resolved stays resolved as written.
- No change to what a unit builds beyond what an item states.

### input:spec

memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md

### task:reuse

the 2026-11-03 crosscheck records and briefs in memory/builds/dShippedRelease/build/ and prompts/ as the template; tools/roles/handoff.py render/agents; tools/memory-tree/gen_build_index.py.

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
