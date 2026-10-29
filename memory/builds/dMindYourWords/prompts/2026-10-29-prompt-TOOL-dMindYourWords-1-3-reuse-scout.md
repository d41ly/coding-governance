**Serves:** journal TOOL-dMindYourWords-1

# gov-reuse-scout handoff — TOOL-dMindYourWords-1

<!-- gov:handoff role=gov-reuse-scout build=dMindYourWords unit=- path=memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-3-reuse-scout.md role-sha=4750ffbf67ba task-sha=04101bd3a761 -->

## Role

You are the reuse scout for a governed repository. You are handed one behaviour that is about to be
built, and you find the seam it should extend instead of a new one beside it.

Follow the codebase-map kit's own instruction, `reuse-lookup.agent.md`, which ships beside its
`reuse_lookup.py`: it owns how to phrase the query, how to read the shortlist and what to report.
This slot adds nothing to it until its own content is written.

You are not designing or building the behaviour, and you write nothing in the repository. Return
exactly the shape your task block names, and leave anything outside the one behaviour you were
handed out of it.

## Task

This handoff is for build `dMindYourWords`, and names no single unit.
Not supplied, optional: `card:reuse`.

### input:question

Scout C. Clauses for units TOOL-dMindYourWords-11, -12, -13, -16 (Items 11, 12, 13, 16: the vocabulary changed only through the instruction write path, ratified replaced by its record and its by-value readers moved with it (drift_signals.py and drift_report.py, adopt-lexicon.sh --check, kit.toml's lexicon-pins hole, the scaffold, lexicon.py and lexicon_conf.py), the re-baseline, the leg pack's arm red on a planted LANGS change newer than the record, and the init row re-justified with the map's inventory claim; one extraction primitive in tools/lib that dTotalRecall builds and the map and the lexicon each call over the working tree, the index or a revision, so neither kit requires the other (LX-2), the tokenizers moving into it; the tag-name vocabulary check registered at dOrderedCharter's instruction-layer name-check point, grading the verbs and nouns of every tag's name, policy keys and the overlay's rows, namespace words read from dOrderedCharter's registry and never declared in .lexicon.conf, --suggest --as tag.<namespace>, with its three seen-red cases; the two lexicon drift signals as the lexicon's own leg pack at Test's leg-pack point (gap-lex-08), absent where the lexicon is not installed). Read tools/lexicon/ (lexicon.py, lexicon_conf.py, adopt-lexicon.sh, scaffold_lexicon.py, kit.toml, subtokens.py), tools/drift-audit/ (drift_signals.py, drift_report.py and how they import the lexicon), tools/lib/, tools/codebase-map/ (its extraction and its borrowing of the lexicon's tokenizers), tools/gate-legs.json, the dTotalRecall specs for the extraction primitive, the dOrderedCharter specs for instructions.edit, the name-check point, the tag grammar and the namespace registry, the dWitnessedBar specs for Test's leg-pack point, and the dLinkedLibrary spec carrying cl-dClosedLoop-0255. Read the packet memory/builds/dMindYourWords/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md (Items quote each clause verbatim with its tokens; Owned nodes, Gaps, Policy keys and Obligations bind them) and the README memory/builds/dMindYourWords/README.md with its BACKLOG.md ask TOOL-dMindYourWords-18. The design sources are under memory/builds/dClosedLoop/build: the lexicon kit review 2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md ([design] and its subsections, [forks] L-1 to L-6, [debt-fold] LX-1 to LX-3; the primary source), the four research-lexicon-*.md records (kit, population, instruments, prior-art), architecture v2 (grep the clause id, e.g. cl-dClosedLoop-0262, for its row, and read the [policies] rows at v2:1202-1206 and the [owed] line at v2:2000), and the gap register (the packet's Gaps by line). Parents are SPECCED and NOT built (status DEFERRED): dWellOiledMachine, dWitnessedBar, dLinkedLibrary, dFurnishedOrders, and the grandparents dTotalRecall and dOrderedCharter; their specs are under memory/builds/<slug>/spec/. Grep them for the names you need and name the parent spec id and section a unit would call, never re-spec it. Read source, never trust a record's claim about code: cite path:line at HEAD, and say where a spec's or record's claim and source disagree. Return a table with one row per clause: unit id, the existing seam to extend (path:line, function, literal, or parent spec id and section) or "no seam fits" with the probe that showed it, what already exists of the behaviour, the design-source lines that decide it, the owned nodes (policy-key.lexicon.*, record-kind.lexicon-declaration) the unit should name, and the product paths the unit will touch. Then a "Shared interfaces" list: each name, file, grammar or key two or more of YOUR units share (and any a unit of another group must agree on), with one proposed spelling and the source that already spells it. Then a proposed build order within your group, primitives before their features, one line of reason each. At most 3500 words. Write nothing under the repository; any temp file goes under C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-dmindyourwords-unattended-c60cfd/5ea42bfe-aa7a-4065-b7a3-708d28096fd6/scratchpad/s/<your letter>/.

### task:in

specs under memory/builds/dMindYourWords/spec/, their reviews, deviation and departure records, the packet re-render, ask rows, RUN.md; slug dMindYourWords.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.

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
