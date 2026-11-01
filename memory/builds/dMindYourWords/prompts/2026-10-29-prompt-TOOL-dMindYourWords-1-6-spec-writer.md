**Serves:** journal TOOL-dMindYourWords-1

# gov-spec-writer handoff — TOOL-dMindYourWords-1

<!-- gov:handoff role=gov-spec-writer build=dMindYourWords unit=- path=memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-6-spec-writer.md role-sha=06b14b1ac42a task-sha=b355fa55369f -->

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

This handoff is for build `dMindYourWords`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dMindYourWords specced and built, so that each of the 17 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 6 owned nodes (Owned nodes) is built, and each of its 11 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0262@8be7fb04` · now `8be7fb04`, as at the baseline · tokens: `PINS:`, `SUFFIX_OFFENDER_PIN`, `VERB_OFFENDER_PIN`, `lexicon.pin` — the definition classes (conforming, forced, out of scope, not a name, debt), with only debt counted against the shrink-only pin (`lexicon.pin`), one pin over today's three seams, `VERB_OFFENDER_PIN` becoming the debt pin, `SUFFIX_OFFENDER_PIN` folded into it and the per-cell `PINS:` block retired, its cells counted inside it, held as a keyed ledger population of offender names once dWitnessedBar's factory lands, never as a count, with its own upgrade step converting an adopter's pin (P38)
2. `cl-dClosedLoop-0263@bab0ffd1` · now `bab0ffd1`, as at the baseline · tokens: `__*__`, `lexicon.forced`, `pytest_*` — forced names recognised by what forces them (`lexicon.forced`): packs keyed by base member, base prefix and host namespace, member and prefix rows applied only where the site resolves statically through its imports to that base, a namespaced closed set applied by name through its rows' namespace pattern (`pytest_*`, `__*__`), against committed pack data, and three cases with their own outcome, each with its fixture: an unresolved base graded as debt and reported unresolved, an override of a parent defined in the repository forced by that parent, and a marker on a base defined in the repository or on an unpacked base reported rather than red
3. `cl-dClosedLoop-0264@a1b36116` · now `a1b36116`, as at the baseline · tokens: none, so the token arm cannot see this clause — gov's own contract-forced names declared in a table the instruction write path owns, the code carrying at most a pointer a check resolves (LX-3), with a stale arm
4. `cl-dClosedLoop-0265@a234cd84` · now `a234cd84`, as at the baseline · tokens: none, so the token arm cannot see this clause — override markers verified against the packs
5. `cl-dClosedLoop-0266@db50d898` · now `db50d898`, as at the baseline · tokens: none, so the token arm cannot see this clause — a reasoned site suppression as the owner's counted fallback
6. `cl-dClosedLoop-0267@06ce7948` · now `06ce7948`, as at the baseline · tokens: `--suggest` — `--suggest` made forced-aware
7. `cl-dClosedLoop-0268@2d14651f` · now `2d14651f`, as at the baseline · tokens: `.d.ts`, `ast`, `cmd`, `http.server`, `inspect`, `json`, `logging` — the packs, generated per host kit (`inspect` per Python minor, wheel AST, pluggy hookspecs, `.d.ts`), shell hosts curated, each with its kit, version range and generator command: the first wave (the data model, the commonly subclassed stdlib bases, unittest, pytest, argparse, `ast`, `http.server`, `logging`, `json`, `cmd`, the shell hosts), and the second wave (Django, Flask, Starlette, FastAPI, React) after an adopter-side census
8. `cl-dClosedLoop-0269@f2bbdcc2` · now `f2bbdcc2`, as at the baseline · tokens: `lexicon.packs` — packs detected from the import census and manifests and declared by the owner, custom packs included (`lexicon.packs`)
9. `cl-dClosedLoop-0270@01096b8c` · now `01096b8c`, as at the baseline · tokens: `lexicon.at-commit` — enforcement: the work order's vocabulary slice and forced-aware answers, staged definitions checked at commit (`lexicon.at-commit`), and the branch's offenders compared with its base's by name at the bar, with move-aware keys proven by replaying the merges since 2026-08-16
10. `cl-dClosedLoop-0271@09fb0fff` · now `09fb0fff`, as at the baseline · tokens: `digest`, `hash`, `instructions.edit`, `lexicon.drift`, `oid`, `sha` — drift beyond verbs (`lexicon.drift`): one verb per declared family per object, the families declared by the packs the stack census selects for the kits it discovers and by the owner through `instructions.edit` (LX-1), and a noun canon of clusters written exogenously, such as `sha` against `oid`, `hash` and `digest`, the corpus deciding only which clusters are live
11. `cl-dClosedLoop-0272@aac8dd76` · now `51d03a52` by deviation `2026-10-29-build-TOOL-dMindYourWords-11-deviation-111` · tokens: `adopt-lexicon.sh --check`, `drift_report.py`, `drift_signals.py`, `init`, `lexicon-pins`, `lexicon.py`, `lexicon_conf.py`, `ratified` — the vocabulary changed only through the instruction write path, with `ratified` replaced by its record and its readers by value moved with it: the drift signal comparing VERBS and LANGS edits (`drift_signals.py`, `drift_report.py`), `adopt-lexicon.sh --check`, the kit's `lexicon-ratified` hole, and the scaffold that writes the stamp, the lexicon's own reads of the record added in `lexicon.py` and `lexicon_conf.py`, which read no `ratified` today, the kit's `lexicon-pins` hole left to the pin's units, the leg pack's arm seen red on a planted LANGS change newer than the record, and the `init` row re-justified
12. `cl-dClosedLoop-0273@e1bd67f4` · now `e1bd67f4`, as at the baseline · tokens: `tools/lib` — one extraction primitive in `tools/lib`, which dTotalRecall builds and the map and the lexicon each call over the working tree, the index or a revision, so neither kit requires the other (LX-2)
13. `cl-dClosedLoop-0274@5185348f` · now `5185348f`, as at the baseline · tokens: `--as tag.<namespace>`, `--suggest`, `.lexicon.conf`, `gap-lex-10` — the tag-name vocabulary check, registered at the instruction layer's name-check point that dOrderedCharter builds, grading the verbs and nouns of every tag's name, policy keys and the overlay's rows among them, against the declared families and the noun canon, the namespace words read from dOrderedCharter's registry and never declared in `.lexicon.conf`, and `--suggest` answering a tag's name as it answers a function's, with `--as tag.<namespace>`, never proposing a name whose first segment is a namespace word, seen red on a planted tag whose name takes an undeclared verb, on a planted request for a name opening with a namespace word answered with a conforming one, and on a namespace word added to `.lexicon.conf` (the owner's tag-grammar answers, `gap-lex-10`)
14. `cl-dClosedLoop-0275@f7d892e0` · now `f7d892e0`, as at the baseline · tokens: none, so the token arm cannot see this clause — the kit's defects fixed: repeated block headers refused, IIFE values and properties ungraded, the dead modes, and the Skill, conf and README reconciled
15. `cl-dClosedLoop-0276@c565a516` · now `c565a516`, as at the baseline · tokens: `memory/builds/**`, `py.constant`, `py.file` — records kept out by the path selector, `py.file` and `py.constant` re-armed once it excludes `memory/builds/**`
16. `cl-dClosedLoop-0277@11ec04ed` · now `089f8d27` by deviation `2026-10-29-build-TOOL-dMindYourWords-16-deviation-161` · tokens: none, so the token arm cannot see this clause — the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point, and the report-only marginal offense rate moved into the lexicon kit with them, so drift-audit's engine imports nothing of the lexicon
17. `cl-dClosedLoop-0278@3bd5d4af` · now `8c3bb6f9` by deviation `2026-10-29-build-TOOL-dMindYourWords-17-deviation-171` · tokens: none, so the token arm cannot see this clause — each word keeps one sense, written once as a `definition` unit the one-fact check guards; the user-facing prose, comments and printed or persisted values in the carriers scout D lists, and every session-kind `attended` hit, are reworded; the names that spell a word in another sense (`tools/playbook/` and the kit id `playbook`, the `PLAY` family, `{{PLAYBOOK_PATH}}`, `baseline_units`, `DESIGN_BASELINE`, `BASELINES`, `on_baseline_red`, `STEP_BASELINE`, the as-built view's `baseline` row word) and the other kits' `baseline` senses bound to them are kept and listed in the spec's §4 "Kept names"

### brief:acceptance

- At the Design exit, `carries.py --build dMindYourWords --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dMindYourWords` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dMindYourWords --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 492 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dMindYourWords by <decision>` line.
- Any path outside `memory/builds/dMindYourWords/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dMindYourWords/prompts/2026-10-29-prompt-TOOL-dMindYourWords-22-promoted-fix-brief.md

### task:reuse

tools/lexicon/ (lexicon.py, lexicon_conf.py, canon.py, adopt-lexicon.sh), tools/drift-audit drift signals, tools/lib extraction primitive from dTotalRecall; scouts name the seams per unit.

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
