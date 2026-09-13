# Build brief — TOOL-dLoggedFlight-1..13

**Serves:** journal TOOL-dLoggedFlight-1..13

This is what the building agent for any one unit of this build is handed, beyond its spec. One file
serves all thirteen units, because the house knowledge is the same for each. Read "Every unit", then
your own entry under "By unit", then "The pass". Your spec is the design and this file is the house
knowledge a cold agent would otherwise re-derive. Where the two disagree, the spec wins. A needed
change goes into the spec first, as a rev bump with its section 9 line.

## Every unit

- **Function names lead with a declared verb.** `.lexicon.conf` pins `VERB_OFFENDER_PIN` as an
  equality, so one new function outside the table reds the `lexicon naming predicates` leg. The verbs
  are build, load, read, write, parse, render, resolve, check, scan, extract, measure, derive, seed,
  init, run, arm, add, remove, set and print. main, cmd and test are reserved. `append` is not a verb,
  so use `add`. Ask `python tools/lexicon/lexicon.py --suggest <name> --as py.function` when unsure.
  Type names may not end in Manager, Helper, Util, Utils, Handler, Processor, Data or Info.
- **Python is stdlib only**: Python 3.12 and no `unittest`. A self-test follows the shape of
  `tools/process-monitor/selftest.py`. That means a `check(name, got, want)` helper, arms as functions,
  a printed assertion count, a floor the count must meet, and exit 1 on any failure.
- **A kit file names nothing outside itself by literal.** Derive the kit dir from `__file__` or
  `BASH_SOURCE`. The `install-prefix (shipped surface)` leg reds on a `tools/<kit>/<file>` literal in
  a shipped file.
- **A carried-prefix count is raised by hand.** `tools/install-prefix-carried.txt` is a ban list
  (TOOL-dRetiredFork-17), so `--write-ratchet` can lower a row and never raise one. When a new literal
  raises a count, edit that row by hand and extend its fourth-column reason in the same pass. The
  `tools/govkit/registry.toml` row rises with every new registry entry or `[[exempt_leg]]` row.
- **The memory root is declared, not spelled.** Address the memory tree through `MEMORY_ROOT` in
  `.memory-tree.conf`. That means `resolve_memory_root` in the runlog lib once unit 1 lands it, and
  `ctx.memory_root` in drift-audit. A shipped file never spells the root.
- **Never name `MEMORY.md`, `STATUS.md` or `IN-FLIGHT.md`** in a file outside `memory/`. The
  dead-path leg reds on those basenames.
- **No tracked `.jsonl` file.** The lexicon refuses an undeclared extension, so fixtures are `.json`
  or `.txt`.
- **Line endings.** `core.autocrlf` is on. Pin every new script or data path LF in `.gitattributes`,
  and read data files with `newline=""`, since a text-mode read rewrites a lone CR.
- **A new self-test never reaches an adopter** (TOOL-aQuenchedHarness-3). Withhold its file, and its
  fixtures, with a `project-owned` rule in the owning `kit.toml` or govkit entry. Carry its leg with an
  `[[exempt_leg]]` row in `tools/govkit/registry.toml` whose `why` cites that id, never with a
  descriptor `[[gate_leg]]`. The `recall floor` rows there are the precedent. Then regenerate
  `tools/govkit/subject-pins.tsv` with `python tools/govkit/govkit.py selfcheck --write`. Unit 2's
  suite differs, and its spec says how.
- **A `project-owned` list takes file names, never globs.** govkit's `rule_sources` silently ignores
  any element holding a glob, so `fixtures/**` ships every fixture as `engine`. `govkit selfcheck`
  cannot see that, and `govkit plan` into a scratch target can. A new runlog fixture is added by name
  to `tools/runlog/kit.toml`, where a self-test arm checks the list against the files on disk.
- **A watched file needs the kickoff manifest re-stamped.** `tools/gate-legs.json` is among the paths
  `memory/guides/SESSION-KICKOFF.md` watches, so pre-commit refuses a commit touching one until its
  `last-audit` line is re-stamped. Stamp it at `git merge-base origin/main HEAD`, with your real
  local time and offset. Say in the commit message what changed, or why nothing in the body did.
- **A new leg** in `tools/gate-legs.json` has a `name`, an `argv`, a `chunk`, a `subject`, a `ceiling`
  and, for a self-test, a `guard` on its kit dir. A leg in the `selftests` chunk needs a row in
  `tools/run-gates/selftest-budgets.txt`. A new ceiling follows the evidence rule of
  `tools/run-gates/derive-ceilings.py`, which the post-build gate run grades.
- **Codebase map.** A new file or leg must be claimed by a dossier under `memory/map/features/`.
  Regenerate with `python tools/codebase-map/gen_map.py --write` in the same commit.
- **Kit versions move once per build.** runlog lands at 1.0. unattended moves 1.19 to 1.20 in unit 2,
  and unit 11 rides that move. run-gates moves 1.6 to 1.7 in unit 3, memory-tree 2.69 to 2.70 in unit
  7, and drift-audit 1.10 to 1.11 in unit 13. Move every carrier your spec names. The version leg
  grades them after the build, and a move it asks for that no spec names is folded then.
- **Run no gate** (owner, 2026-09-13). That means no leg in spec section 7, no other row of
  `tools/gate-legs.json`, and no hand-run memory-hygiene gate. Every gate runs once, after all
  thirteen units are built. What you do run is the test file you are writing, directly, which is how
  each refusal is staged RED. Run a bash test from Git Bash, never through Python's `subprocess`: on
  this node that finds WSL's `bash`, which fails with "not a git repository". The pre-commit hook
  still checks your commit, and if it refuses, fix what it names.
- **Stage before you commit.** The pre-commit hook reads the index, so an unstaged new file is
  invisible to it.

## By unit

- **1, the runlog kit.** Landed at 03ae473c and 9ac609ec. Read `tools/runlog/README.md` for the
  grammar and `tools/runlog/runlog_lib.py` for the reader before you extend either. The kit has a
  `tools/playbook-kit-waivers.txt` row, which clears itself once the charter names the kit. Copy `tools/process-monitor/kit.toml`: `id` equals the dir name, and a
  `version_from` pattern matches exactly one line of a file this unit lands. Put `include = "**"` under
  `engine`, with `selftest.py` and each fixture, by name, as `project-owned`. The version pair is
  `KIT_RUNLOG_VERSION = "1.0"` on a line carrying `gov:kit runlog@1.0`. The dossier
  `memory/map/features/runlog.md` opens with a toml fence carrying these keys:
  - `feature`, `title`, `status` and `streams`;
  - a NON-EMPTY `decisions` list;
  - `claims`, with all ten inventory keys;
  - `paths`.

  It needs the headings `## Constraints & why`, `## Shared seams`, `## Gaps` and `## Reuse affordance`.
  The first line under each is `seam: <id> — …` or `none — <why>`.
- **2, the driver writer.** Landed at 796c148a and 83e6024d. The driver now writes `driver.log` lines, so
  read `tools/unattended/runlog-writer.test.sh` before writing a test that reads them. The suites that
  were already under `tools/unattended/` are NEVER run: that is a standing owner rule.
- **3, the gate verdict line.** Run only the new suite you write,
  `tools/run-gates/run-gates.runlog.test.sh`. `GATE_CMD` stubs keep every arm off the real bar, and
  the existing run-gates suites run after the build.
- **4, the pre-push line.** The hook gates every push from this clone, the landing push included. Arm
  it through its own suite with `GOV_GATE_CMD` stubs, and never by pushing.
- **5, the redaction table.** Every credential a fixture plants is a template expanded at test time,
  so the kit's scan of its own tree stays clean.
- **6, the extractor.** A test never reads or writes a real store: every root the spec names points
  at scratch. `extract --measure` over the real store is report-only, and nothing it prints is
  committed.
- **7, the `Decided:` trailer.** The method template and its rendered copy stay byte-paired, and the
  method stays under its row in `tools/template-size-limits.txt`, which the post-build run grades.
- **8, 9 and 10, the model, the record and the schema leg.** Build on the fixtures of the units
  before. Unit 8's real-population figures are re-measured, not copied from the spec. Build run-state
  fixtures the way the driver's verbs leave them, never as typed `witness:` lines. Remember that
  `--close` writes no witness. The self-test arm that reads the driver's source is withheld and needs a
  carried row.
- **11, the Skill steps.** The rendered Skill and protocol copies must stay byte-identical to their
  templates. AC5 and AC6 are observed by the run itself, at its landing. Write their ledger lines as
  owed, naming where the observation will be recorded, and never as met.
- **12, the runlog skill.** The adopter renders a Skill whose placeholders are all tokens it
  declares and substitutes. The post-build run grades them.
- **13, the drift signal.** Report-only, with `gateable` false, and the value is asserted against a
  fixture, never against this tree.

## The pass

1. Declare the write set with the driver's `--dispatch`. List EVERY path the commit will carry. That
   includes this brief, the spec, the ledger, the regenerated map files, `memory/LIVE.md`,
   `memory/ledger/2026-09.md` and the build README.
2. Build. Stage every refusal the spec names RED before it lands: break it, watch the arm fail, then
   restore it.
3. Run no gate. Run the unit's own test file directly, and stage each refusal RED with it.
4. Write the acceptance ledger at
   `memory/builds/dLoggedFlight/build/2026-09-13-build-TOOL-dLoggedFlight-<n>-1-acceptance-ledger.md`
   with `**Serves:** journal TOOL-dLoggedFlight-<n>` and `**Evidences:** TOOL-dLoggedFlight-<n>`. Give
   one line per criterion, `- AC1 — \`<command or path>\` — <what was observed>`, with the backticked
   token on the `- ACn —` line itself and not on a continuation line. An AC observed by a gate leg
   is written as owed to the post-build gate run, naming the leg, and never as met. The run records
   the observation after that gate run.
5. Set the spec's status header to CLOSED, run `python tools/memory-tree/gen_build_index.py --write`,
   and stage what it rewrote.
6. Commit with the subject `feat(dLoggedFlight): TOOL-dLoggedFlight-<n> — <the claim>`. Pass a
   600000 ms timeout, because the pre-commit hook runs longer than the default. Record any choice
   that has no other home as a `Decided: <choice> — <why>` line in the final trailer block, beside
   `Co-Authored-By:`.
7. Run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names.

## Never

- Run a gate leg, the full merge bar, or any suite that was under `tools/unattended/` before this
  build.
- Pipe a gate through `tail`. The failure marker is `GATE FAIL`, and a pipe makes `$?` the pipe's.
- Push, merge, touch the primary tree, or use `--no-verify`.
- Use a bare `git stash`. The stash is shared with other sessions.
