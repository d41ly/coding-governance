**Serves:** journal TOOL-dIndexedDesign-2

# gov-spec-writer handoff — TOOL-dIndexedDesign-2

<!-- gov:handoff role=gov-spec-writer build=dIndexedDesign unit=TOOL-dIndexedDesign-2 path=memory/builds/dIndexedDesign/prompts/2026-11-05-prompt-TOOL-dIndexedDesign-2-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=918c4e023cf0 -->

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

This handoff is for build `dIndexedDesign`, unit `TOOL-dIndexedDesign-2`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the dIndexedDesign specs the build's first cross-read found disagreeing with their parents as they stand: TOOL-dIndexedDesign-1, -2, -5, -8, -9, -10, -11, -13, -14, -20, -32, -38 and -46, and -34 and -52, which restate a revised sibling. Each unit keeps its design; the items state what moves.

### brief:items

Read the cross-check record first, `memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 2: specs 2, 1, 5 and 8

- **The registry factory's grammar, rows 7 and 42 (specs 2, 8).** Each `record_kinds.py new` call lacks `--purpose`, which TOOL-dTotalRecall-16 S2 refuses, and the `home`, `lifecycle`, `readers` and `layer` columns TOOL-dTotalRecall-18 S1 requires; spec 2's also lacks `--writer` and `--check`. Spell each with `--writer`, `--check` and `--purpose`, declare the `schema.form` (`fields` for feature-design and fork; roster is a README region, not `fields`) and set tr18's columns through tr18's landed verb, as TOOL-dLinkedLibrary-13 S1 and S2 and this build's specs 10 and 11 do. Cite tr16 S2 and tr18 S1 in the external edge; spec 2's AC9 gains the writer and the purpose.
- **Row 43 (spec 8), the `hand` writer, the revision's.** The non-goal says the rows' `hand` writer is "the class TOOL-dTotalRecall-2 replaces with doors". Restate it on TOOL-dTotalRecall-1 §4's ground: `hand` is legal because tr2 S9, a one-time pass before this build, never moves these rows, and no door is promised; this unit adds none.
- **Row 3 (spec 1), `item.design.ready`'s stand-in.** TOOL-dDeclaredLoop-13 S8 derives a stand-in row for every item owned outside dDeclaredLoop, `item.design.ready` among them. §3's edge names both stand-ins; §8 F5 (its pick untouched) states that this unit keeps `item.design.ready`'s row on the same ground it keeps exit's.
- **Row 9 (spec 2), `item.design.overlaps`' stand-in.** Add the consumes-from edge for dl13 S8's stand-in row of `item.design.overlaps`, and arm it in this unit's landing as spec 8 S11 arms decompose's: delete the row and point the item's `witness` at `design_lib.py --overlaps`. Add the arming to Files touched and an AC clause.
- **Row 37 (spec 5), `item.design.research`.** TOOL-dDeclaredLoop-12 S2 already transcribes the item, so `loop_items.py new design.research` would exit 2 and AC9 is met before the unit builds. S8 arms dl12's existing row instead: set its `witness` to the `read_declared_kind` check and delete its dl13 stand-in row. Drop the factory call; AC9 reads the armed witness, so it can fail at base.

#### Group B, led by spec 10: specs 10, 9, 11, 13 and 14

- **Row 58 (spec 10), the `hand` writer, the revision's.** The non-goal "TOOL-dTotalRecall-2's door registers one; until then the writer is `hand`" becomes: the kind's writer stays `hand` (TOOL-dTotalRecall-1 §4, a `header` row tr2 S9 does not move), and any door is this kit's or an ask, named by its owner.
- **Rows 57 and 64 (specs 10, 11), the kind classifier.** F1 (spec 10) and F2 (spec 11) say TOOL-dTotalRecall-42 S5 "makes the kind decide and the home admit". tr42 S5 classifies by the record's `**Serves:**` kind only and tr43 S13 makes it the `record` extractor's sole classifier; a playbook or set record has no Serves line. Decided, picks untouched: each fork's ground states that these records are registered but not tagged by the `record` extractor until dTotalRecall classifies a kind without a Serves line, and names that as the ask this build's run files in dTotalRecall's `BACKLOG.md`, with its row text.
- **Row 73 (spec 13), the registry grammar.** S1's `new seams` lacks `--purpose` and tr18's columns, and its home is a filename pattern, not a glob. Add `--purpose`, a glob home such as `memory/builds/*/build/*-reuse-scout*.md`, and the other columns through tr18's landed verb, as specs 10 and 11 do.
- **Row 77 (spec 13), decompose's `finding` route.** A non-empty `upstream` on `item.design.decompose` needs a route for the outcome `finding`, or TOOL-dDeclaredLoop-29 S7's loader refuses the row. S6 adds the `finding` outcome and its route to decompose's row; AC7 runs the loop loader over the row, not `tomllib` alone.
- **Row 50 (spec 9), the deleted harness.** TOOL-dLinkedLibrary-3 S1 deletes `tools/codebase-map/replay-phrases.py`, a parent's landing before this unit builds. Drop it from S6, AC8, Files touched and S11's twin table, and state that ll3 S1 removes this reader.
- **Row 81 (spec 14), the gated cut.** §3 says a class TOOL-dLinkedLibrary-24 S5 marks gated leaves "the index the corpus reads"; ll24 S5 cuts it from `cmd_for_paths` only, keeps it in `INDEX.md`, and S6 adds a `record` tier. §3 and S1 state that S1 extracts `cmd_for_paths` as ll24 S5 and S6 leave it, and whether the corpus filters gated classes out of its index too; pick the reading that keeps the two arms over one class set.

#### Group C, led by spec 20: specs 20, 34, 32, 38, 46 and 52

- **Rows 95 and 117 (specs 20, 38), the registry grammar.** S4 and S7 of spec 20 and S9 of spec 38 call `record_kinds.py new` without `--purpose` or tr18's columns. Add `--purpose`, set tr18's columns through its landed verb, cite tr16 S2 and tr18 S1 in the external edge, and make the AC that checks the rows red on a missing column, as specs 10 and 11 do.
- **Row 99 (spec 20), versioned `returns`.** S10's rows name `record-kind.diff` and `record-kind.inventory` with no version; TOOL-dDeclaredLoop-24 writes `returns` as `record-kind.<name>@<n>`. Write `@1`, and add their `[[record-version]]` rows in `tools/loop/item-schema.toml`. Those rows hash the per-kind table rows spec 34 S1 adds, so they land in spec 34's pass or later: spec 34 gains that line in its scope and Files touched, spec 20's AC9 is re-pointed accordingly.
- **Row 106 (spec 32), the untyped head.** S2 names it `spec-audit`, `diff-review`, `journal`, `research`; TOOL-dTotalRecall-18 S7 makes it `log` with `journal` a read-only alias. Name the head as tr18 S7 leaves it and cite tr18 S7.
- **Rows 115 and 121 (specs 38, 46), the opt-in's order.** Spec 38 S3's predicate is true on a README `spec-audit:` key OR an owed `review.design`, and spec 46 S11 reads README, then `SPEC_AUDIT_DEFAULT`, then `review.design`. TOOL-dDeclaredLoop-19 S8 reads `review.design` first and consults the README and the default only under `opt-in`. Both derive from dl19 S8's table in that order, cite it, and each AC plants `off` with a present README key, which must read not owed. Spec 52 restates spec 46's reader: revise its restatement to match.

### brief:acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground.md`.
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

memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-2.md

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
