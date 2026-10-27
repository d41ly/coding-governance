**Serves:** journal TOOL-dLinkedLibrary-1

# gov-spec-writer handoff — TOOL-dLinkedLibrary-1

<!-- gov:handoff role=gov-spec-writer build=dLinkedLibrary unit=- path=memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-6-spec-writer.md role-sha=06b14b1ac42a task-sha=cd5cc1f3068d -->

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
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dLinkedLibrary`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dLinkedLibrary specced and built, so that each of the 25 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 25 owned nodes (Owned nodes) is built, and each of its 23 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0238@36136b48` · now `36136b48`, as at the baseline · tokens: `[records]`, `flow.on-exhausted`, `memory/map/conventions/` — decisions split by kind: reuse entries as level-3 instruction units beside their dossiers and under `memory/map/conventions/`, proposed with their build through the instruction command and rendered once the owner accepts them, the major-decision log with its holds-now view, today's 200 rows routed by two raters at kappa 0.8 or better, below it the rubric revised and the routing re-run, no row moving until it passes, each re-run drawing on the build's rework budget and ending as `flow.on-exhausted` says, and the `[records]` rule reworded
2. `cl-dClosedLoop-0239@36d4c1c8` · now `36d4c1c8`, as at the baseline · tokens: `**Reuse:**`, `[reuse]`, `reuse.delivery` — the reuse scout's house index in M1c's shape (a digest of symbols, callers, dossiers and reuse entries, with the sketch and census steps), delivered through the task card's `**Reuse:**` field (`reuse.delivery`) and accepted by re-running aScoutedSeam's benchmark and its twelve held-out cases, which dFairHearing lands and whose cases name commits in two adopter repositories, the re-run refusing, naming the clone it lacks, without them, and the acceptance passing only at M1c's 16 of 24 on the benchmark and its 8 of 12 on the held-out cases or better (layer-memory `[reuse]`, the scouted-seam research's held-out run)
3. `cl-dClosedLoop-0240@5773ca81` · now `5773ca81`, as at the baseline · tokens: `MAP_CLI`, `[[retired]]`, `experiment`, `record find`, `reuse-probed`, `reuse_lookup`, `reuse_lookup.py` — `reuse_lookup.py` and its agent retired with their readers rewritten, by name and by value, and their own upgrade step, the readers by value named: hygiene check 12's §10 arm, which accepts the token `reuse_lookup` as reuse evidence and past a new cutoff accepts the reuse scout's record instead, seen red on a planted spec citing `reuse_lookup` after it, unattended's `MAP_CLI`, re-pointed at the map's CLI, and the `reuse-probed` DoD item and M5, which read the reuse scout's record in place of the lookup's and recall's query logs, a `[[retired]]` row for the files codebase-map installs (P38), and memory-recall narrowed to what `record find` does not answer, its why-search, its bench and union becoming dBoundRoles' `experiment` instance, the finder itself dTotalRecall's (SA-6)
4. `cl-dClosedLoop-0241@0e5185f1` · now `0e5185f1`, as at the baseline · tokens: `annotations.grammar`, `annotations.resolve-scope`, `gov:feature`, `gov:note` — the `gov:note` grammar and `gov:feature` anchors checked both ways with reuse entries, the generated annotation index and its resolve check (`annotations.grammar`), over notes alone or every comment reference as `annotations.resolve-scope` says, the shipped-evidence signal re-checked first
5. `cl-dClosedLoop-0242@866cebbc` · now `866cebbc`, as at the baseline · tokens: none, so the token arm cannot see this clause — the generated views: the decisions' holds-now view and the reuse view, beside dTotalRecall's README routing and relation graph, which this build reads and never renders again
6. `cl-dClosedLoop-0243@9acc070e` · now `9acc070e`, as at the baseline · tokens: none, so the token arm cannot see this clause — the research view, over the research-return kind
7. `cl-dClosedLoop-0244@e14fc5fd` · now `e14fc5fd`, as at the baseline · tokens: `annotations`, `annotations.lookup` — the `annotations` leg, the marker query with the map's index rows where the map is installed, the query alone or the map's index alone as `annotations.lookup` says (AN-1), and the read hook on shell reads too (AN-2), the follow-through test that chooses it given a threshold, a sample size and a window fixed before it runs, and a measure that separates following a pointer from working on the same build
8. `cl-dClosedLoop-0245@2d7af537` · now `2d7af537`, as at the baseline · tokens: `adopt`, `adopt.census`, `adopt.decisions`, `adopt.practices`, `adopt.reconstruct`, `baseline`, `census`, `docs-and-trailers`, `docs-owner-ratifies`, `origin`, `reconstructed`, `rejected`, `retrofit.decisions`, `retrofit.practice-pending`, `retrofit.reconstruct` — retrofit's `baseline` and `census` record kinds, the `origin` field, and the `adopt` program the core's own command runs where distribution is absent: `adopt.census`, `adopt.practices` (the owner's one ruling per practice, through `retrofit.practice-pending`) and `adopt.decisions` (two raters by the author's rubric, through `retrofit.decisions`, a candidate the raters split on kept `reconstructed` and not major, and ratified by the owner only under `docs-owner-ratifies` or `docs-and-trailers`, seen on a planted split candidate, the owner's FK-4-6), with `adopt.reconstruct`, which `retrofit.reconstruct` governs, and a declined decision kept `rejected`
9. `cl-dClosedLoop-0246@96afa172` · now `96afa172`, as at the baseline · tokens: `origin` — the origin check, re-derived from history, `origin` among the fields every slice renders, and the reuse digest's ranking
10. `cl-dClosedLoop-0247@87bb7e47` · now `87bb7e47`, as at the baseline · tokens: none, so the token arm cannot see this clause — the progress cell
11. `cl-dClosedLoop-0248@8c261008` · now `8c261008`, as at the baseline · tokens: none, so the token arm cannot see this clause — the annotation resolve check's legacy and the untouched long blocks registered as ledger populations
12. `cl-dClosedLoop-0249@49ce83a8` · now `49ce83a8`, as at the baseline · tokens: `gov:`, `marker` — the `marker` namespace over the existing `gov:` words
13. `cl-dClosedLoop-0250@9ea3dfcf` · now `9ea3dfcf`, as at the baseline · tokens: `1b759b620`, `kind: research-return` — and the dated backfill of `kind: research-return` over the existing returns, 72 at `1b759b620`
14. `cl-dClosedLoop-0251@23b8b8e1` · now `23b8b8e1`, as at the baseline · tokens: `callers`, `code`, `git grep`, `gov code show`, `gov map code`, `tests`, `where` — `gov map code` and `gov code show`, `callers`, `tests` and `where`, `git grep` the engine of `where` and the floor for a language with no extractor, the map's level 0 holding one counted `code` line (night pass, point 3)
15. `cl-dClosedLoop-0252@5aa0f94b` · now `5aa0f94b`, as at the baseline · tokens: `memory.code-enrich` — the enrichment workflow: purposes derived first from docstrings and headers, an agent's pass for the rest as `memory.code-enrich` says, each keyed to its definition's body hash and stale when the hash moves, joined both ways with a pending population (night pass, point 3)
16. `cl-dClosedLoop-0253@22d88118` · now `22d88118`, as at the baseline · tokens: `code` — the replay's losing test extended to code: a unit's files read and its lookups counted, with the `code` slot and without it, scored through dFairHearing's scorer factory, the slot losing if its recall of the files the unit then read is no better than its seed's alone, the losing test the code research committed before its probe (night pass, point 3)
17. `cl-dClosedLoop-0254@e703feac` · now `e703feac`, as at the baseline · tokens: `decides`, `gov:end`, `gov:end <tag>` — extractors emitting typed edges from annotations, front matter, dossiers and decision rows, `decides` written on decision rows, and the span rule: a definition's extent where one derives, `gov:end <tag>` only where none does, an unterminated note outside a definition, an orphan `gov:end`, crossed or nested tags and a mismatched tag each refused by the annotations leg, seen red on a planted file, and the span share re-measured with the map's own extractors, the hybrid losing if 80% or more of a feature's outside spans sit in a derivable definition (night pass, point 4)
18. `cl-dClosedLoop-0255@c0b78911` · now `c0b78911`, as at the baseline · tokens: `REGION_CLOSE`, `REGION_OPEN`, `check_roles.py`, `tools/lib` — the region-parser factory in `tools/lib`, every region parser a query over `REGION_OPEN` and `REGION_CLOSE` constants and marker-pair finds returns re-pointed to it, `check_roles.py`'s roles-catalogue region and govkit selftest's hold-region scan among them beside the register's five (night pass, point 4)
19. `cl-dClosedLoop-0256@aea4db49` · now `aea4db49`, as at the baseline · tokens: none, so the token arm cannot see this clause — the dossier's header becoming the feature node and its prose moving into units and records, as NP-16 settles (night pass, point 4)
20. `cl-dClosedLoop-0257@ac01a5f8` · now `ac01a5f8`, as at the baseline · tokens: `feature` — the `feature` namespace armed as an instruction selector when it registers, as NP-13 settles (night pass, point 4)
21. `cl-dClosedLoop-0258@bbce050b` · now `bbce050b`, as at the baseline · tokens: `ctags`, `memory.code-languages: builtin+ctags` — the ctags extractor pack, opted into by `memory.code-languages: builtin+ctags` or `ctags`: definitions and their ranges for every language the built-in extractors do not read, the record naming its extractors and the ctags version, and a missing ctags stopping the run rather than degrading to file level (NP-10)
22. `cl-dClosedLoop-0259@2b91da03` · now `2b91da03`, as at the baseline · tokens: `Decided:`, `[cycle]`, `decides` — `decides` on every decision row, `Decided:` trailers read as decision rows through dDeclaredLoop's one reader, and every bug class naming its cause, language and platform (the memory plan's `[cycle]`, P37)
23. `cl-dClosedLoop-0260@c677f704` · now `c677f704`, as at the baseline · tokens: `CLAUDE.md`, `GEMINI.md`, `adopt.instructions`, `instructions.legacy`, `refuse` — `adopt.instructions`: at install an adopter's own instruction files rendered verbatim as a legacy block after the project block, the block a member of `instructions.legacy`'s population, admitted at install only and shrink-only after, under `refuse` admitted only with every paragraph ruled before the first landing, every harness file wired at once and none overwritten, then each paragraph proposed as a repository unit, an amendment of a gov unit or a drop, for the owner to rule once, seen on a fixture repository holding its own `CLAUDE.md`, `GEMINI.md` and Copilot instructions, each file's bytes kept in the block and each harness file wired, red on today's installer, on a planted row added to the legacy list, and on a planted strict install carrying an existing `CLAUDE.md` (IA-5, the folds' review)
24. `cl-dClosedLoop-0261@6566da73` · now `6566da73`, as at the baseline · tokens: none, so the token arm cannot see this clause — each bug class's gate status derived, never declared: gated only where the class names a leg in the leg manifest and a planted case of the class that the leg is seen to refuse, partly gated or ungated otherwise, a class so gated left off every checklist, the review's among them, a syntactic class turned into a gate at its second occurrence, and its anchors marked as where it bit, never what triggers it, seen red on a class marked gated whose leg is absent or whose planted case passes the leg (the night pass two, point 6, the owner's NT-25, the status derived by the night pass two's review)
25. `cl-dClosedLoop-0500@84eb6d7a` · now `84eb6d7a`, as at the baseline · tokens: `ANNOTATION-STYLE`, `HYGIENE.md`, `backlog.py`, `note` — the records that contradict the code corrected at their sources: the map README's path, `backlog.py`'s shards claim, the DEPL rows of other families, the duplicated ids, the spec template's security-model line, the typed README statuses, the `ANNOTATION-STYLE` guide and its template naming the signal that reads comment citations, and `HYGIENE.md`'s unused `note` kind

### brief:acceptance

- At the Design exit, `carries.py --build dLinkedLibrary --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dLinkedLibrary` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dLinkedLibrary --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 484 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dLinkedLibrary by <decision>` line.
- Any path outside `memory/builds/dLinkedLibrary/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dLinkedLibrary/prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md

### task:reuse

the parent dTotalRecall's spec set and reuse-scout records (memory/builds/dTotalRecall/build/*reuse-scout*), tools/codebase-map/map_lib.py, tools/memory-recall/, tools/lib/; recorded per spec in §10.

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
