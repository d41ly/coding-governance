# The retrofit system: bringing an existing repository under gov's practices

**Serves:** research PLAY-dClosedLoop-1

The owner opened a sixth system after the five of the systems round: how gov brings its practices into a
repository that already has an extensive codebase and practices of its own. This record holds the owner's
words, what the design already holds for it, and the research and its method. Once the runs return, it
also holds what they agree on, and then the design.

## [words] The owner's words, 2026-10-17

> Continue with your current work queue but budget research+design for another system: retrofitting the
> gov practices. What layer (extension?) does it go to? When gov is adopted into a fresh repo, maintaining
> its methods (to be designed) like tagging, code annotations, decision log and its major decisions, etc.,
> is not an issue - they all happen along as code is planned, designed, and built. However, Gov may be
> adopted into a product/repo that has an extensive codebase already and has been following different
> practices. How would gov retrofit its practices into an existing repo as it goves over its code to
> ensure efficient practices?

## [scope] What the design already holds

- **No design record covers it.** The flow record names an existing codebase only as where Plan
  integrates a new feature (`build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:112,119`). The deployer
  research's retrofit installs gov's kits into an adopter's toolchain
  (`memory/builds/aDeployScout/spec/governance-deployer-research.md:22`). It does not bring the adopter's
  code under gov's practices.
- **Pockets tolerate legacy, one practice at a time:**

  | Pocket | What it tolerates | Where |
  |---|---|---|
  | the codebase map's baseline | keys no dossier claims yet; it shrinks unless a recorded decision says otherwise | `memory/map/baseline.toml`, and AGENTS.md's section 2 |
  | IW-1's legacy list | hand-written instruction documents, shrink-only, each chain build migrating its own step's guides | the systems record's `[answers]` |
  | `instructions.legacy` | the same list's policy: `shrink-only` or `refuse` | the systems record's `[design-instruction-writing]` |
  | `memory.legacy-anchors` | legacy record headings, given derived anchors | the systems record's `[design-memory-structure]` |

- **What it lacks** is the system the owner asks for: where it sits, how it reaches the code as gov goes
  over it, what each practice derives from what the repository already holds, and the bound that keeps
  it out of the owner's way.

## [research] Dispatched, 2026-10-17

- **The method** is the systems round's. One handoff, `prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-1-researcher.md`, runs twice at the researcher's declared
  effort, medium, as dispatches 83 and 84. The design is based on what the two runs agree on.
- **The handoff** shares the systems round's handed facts, way of working and return shape. It differs
  in its context, which quotes the owner's words above, in its part, and in the return shape's third
  section, which asks across the five systems instead of the other four. The script below assembles it,
  `handoff.py render` renders it, and `handoff.py check` passes it.
- **The order.** Both runs go out together once review dispatch 65 returns, two agents at once. The
  review queue resumes at dispatch 66 after both return, so no more than five agents run at once.
- **The returns** are filed verbatim as `build/2026-10-17-build-PLAY-dClosedLoop-1-research-retrofit-<run>.md`.

### [instrument] The script that assembles the question

```python
"""Assemble the retrofit system's research question from the systems round's shared blocks and its own
part, for the system the owner opened on 2026-10-17, then render and check its handoff.

Usage: python assemble_retrofit.py <dir> <systems-dir>   (from the worktree root)
Writes <dir>/question-retrofit.md, renders the handoff with handoff.py into the build's prompts/ folder,
writes the spawn prompt (the marker line, a blank line and the Task section) to <dir>/prompt-27.txt, and
runs handoff.py check on the rendered file. The handed facts, the way of working and the return shape are
the systems round's, so this question differs from those five only in its context, its part, and the
return shape's third section, which asks across the five systems instead of the other four.
"""
import pathlib
import subprocess
import sys

d, sysd = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
head = (sysd / "head-expansions.md").read_text(encoding="utf-8").rstrip("\n") + "\n" + \
    (sysd / "head-more.md").read_text(encoding="utf-8")
tail = (sysd / "shared-tail.md").read_text(encoding="utf-8")
old = "   it; then what it needs from, and gives to, the other four systems.\n"
if tail.count(old) != 1:
    sys.exit("the return shape's third section has moved")
tail = tail.replace(old, "   it; then what it needs from, and gives to, each of the five systems the round designed.\n")
CONTEXT = (
    "**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.\n"
    "The owner reviews the design layer by layer. All eight layers, the five core and the three expansions,\n"
    "are designed, reviewed and folded. Five systems that cut across every layer were then researched and\n"
    "designed: tags, code annotations, instruction writing, role workflow shapes and memory structure. The\n"
    "owner is settling their forks. The owner now opens a sixth system, in these words:\n\n"
    "> Continue with your current work queue but budget research+design for another system: retrofitting the\n"
    "> gov practices. What layer (extension?) does it go to? When gov is adopted into a fresh repo, maintaining\n"
    "> its methods (to be designed) like tagging, code annotations, decision log and its major decisions, etc.,\n"
    "> is not an issue - they all happen along as code is planned, designed, and built. However, Gov may be\n"
    "> adopted into a product/repo that has an extensive codebase already and has been following different\n"
    "> practices. How would gov retrofit its practices into an existing repo as it goves over its code to\n"
    "> ensure efficient practices?\n\n"
    "Yours is **retrofitting gov's practices into an existing repository**. Design it to fit the architecture\n"
    "handed below, across all eight layers and the five systems. Measure what today's product does, say what\n"
    "the current design already settles and what it lacks, and say what makes your pick efficient, in numbers\n"
    "a check could hold it to.\n")
part = (d / "part-retrofit.md").read_text(encoding="utf-8")
text = "\n".join([CONTEXT, head, part, tail]).rstrip("\n") + "\n"
if "\r" in text:
    sys.exit("a carriage return reached the question")
(d / "question-retrofit.md").write_text(text, encoding="utf-8", newline="\n")
print(f"question-retrofit.md: {len(text.split())} words, {len(text.encode('utf-8'))} bytes")

r = subprocess.run([sys.executable, "tools/roles/handoff.py", "render", "--role", "gov-researcher",
                    "--build", "dClosedLoop", "--unit", "PLAY-dClosedLoop-1", "--input", "question=" + text,
                    "--part", "task"], capture_output=True)
sys.stderr.write(r.stderr.decode("utf-8"))
if r.returncode:
    sys.exit(f"render exited {r.returncode}")
task = r.stdout.decode("utf-8")
(d / "prompt-27.txt").write_bytes(task.encode("utf-8"))
marker = task.split("\n", 1)[0]
path = marker.split(" path=", 1)[1].split(" ", 1)[0]
print(f"rendered {path}")
c = subprocess.run([sys.executable, "tools/roles/handoff.py", "check", path], capture_output=True)
print(c.stdout.decode("utf-8") + c.stderr.decode("utf-8"), end="")
sys.exit(c.returncode)
```

## [agreement] What the two runs agree on

Run A beside run B, question by question. "Both runs" holds only what each run found on its own, with each
run's line cited. The returns are filed verbatim as `research-retrofit-a.md` and `-b.md` in `build/`.

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| Placement | a system across the layers, like the five, and neither a layer nor an expansion (`research-retrofit-a.md:15`, `research-retrofit-b.md:13`) | — | both |
| What the core must hold | the baseline and its ratchet, since without them the core's gates red on legacy no unit touched, and the core could not carry a build alone (P28) (`research-retrofit-a.md:15`, `research-retrofit-b.md:18`) | A names map coverage, check 21 and the designed annotation resolve check (`:68`). B names `install-prefix` (`:86`), which is a deliberate pure ban over the files gov ships (`tools/check-install-prefix.sh:24-33`), which skips a consumer's tree, so it is not an adopter's case | A's three |
| One primitive | one baseline primitive replaces each check's own list: gov keeps 27 registries in at least 6 grammars, with the count ratchet written twice (`research-retrofit-a.md:26`, `research-retrofit-b.md:149`) | A counts per check, subject and class, with rows in each check's home (`:111`). B keeps a set of keys, one file per population under `memory/<layer>/baseline/` (`:149`) | one factory; A's count is B's `#k`; A's homes, each population where its check keeps it (revised 2026-10-17, the audit's H4: B's home under EX-2 is a directory the adopter's hygiene refuses) |
| Keys, never lines | a row's key is a path, a key or a record, never a line number (`research-retrofit-a.md:111`, `research-retrofit-b.md:149`) | B refuses a label key that holds a number (`:177`) | both |
| The seed | a command seeds every check at a SHA, idempotently, with no agent (`research-retrofit-a.md:182`, `research-retrofit-b.md:157`) | — | both, at every registration as well as adoption |
| An unseeded check | it never reads green (`research-retrofit-a.md:130`, `research-retrofit-b.md:206`) | A refuses the adoption by default (`:198`). B records the population unarmed (`:206`) | B's |
| Never gains, both ways | a key or a count above the base's reds, and so does a row no scan finds (`research-retrofit-a.md:125`, `research-retrofit-b.md:170-171`) | A admits growth through a `reason:` row (`:111`). B admits it through a `widen` record (`:219`) | a widen record |
| Drain on touch | a unit that touches baselined legacy drains it or carries it, under a per-unit cap, and untouched legacy never reds (`research-retrofit-a.md:127`, `research-retrofit-b.md:173`) | A caps sites at 20 per unit (`:193`). B caps keys at 3 per unit (`:218`) | both caps: sites for code, keys for claims |
| Drain scope | the file scope loses, owing a median of 55 sites per commit in A and 97 in B (`research-retrofit-a.md:102`, `research-retrofit-b.md:136`) | A drains changed hunks, a median of 0.03 sites per commit and a p90 of 0.46 (`:98`). B drains the annotations' touched block (`:139`) | the changed hunks; `[cross]` says how the annotations' budget meets them (revised 2026-10-17, the audit's M5) |
| Why touch | code added inside legacy copies legacy practice: 16.1% marginal offenses in files that predate the lexicon's declaration, against 9.1% in fresh files (`research-retrofit-a.md:29`, `research-retrofit-b.md:32`) | A: the per-file count ratchet let 29 of 129 encoding sites persist on edited lines (`:102`). B: a drain on first touch clears 15 of 26 keys in a median of 7 days, where the passive baseline cleared 48% in 63 days (`:129`) | both |
| Big-bang reconstruction | it loses, since 25 of 31 authored dossiers already sit behind their paths (`research-retrofit-a.md:100`, `research-retrofit-b.md:118`) | — | rejected |
| Cadence sweep | it loses as the primary mode, adding under 1% of reads beyond touch (`research-retrofit-a.md:100`, `research-retrofit-b.md:118`) | A measures 0.7%, B 0.8%. B adds that a low-churn repository is untestable here (`:118`) | an optional expansion (RF-6) |
| Reads follow change | 99.3% and 99.2% of code reads land on files changed in the prior 30 days (`research-retrofit-a.md:45`, `research-retrofit-b.md:70`) | A reads 52,566 calls, B 22,971 | both, with `[design]`'s caveat |
| Origin | a reconstructed record is marked apart, is never a witness, and is labelled in work orders (`research-retrofit-a.md:165`, `research-retrofit-b.md:161`) | A: `origin: reconstructed <sources>`. B: `provenance`, derived and never typed, with `written`, `reconstructed@<sha8>` and `imported:<path>` | B's three values, in a field named `origin` |
| Decisions | candidates from decision-shaped documents, routed by two raters at kappa 0.8, with the owner ratifying the major ones (`research-retrofit-a.md:159`, `research-retrofit-b.md:186`) | A imports documents only, and mines commit trailers at the owner's ask, since gov has 1,829 trailers against about 12 majors (`:196`). B takes trailers as candidates too | RF-3 |
| The repository's practices | a census counts them, and the owner rules once per practice: import, translate, keep alongside or retire, with alongside until then (`research-retrofit-a.md:167`, `research-retrofit-b.md:192`) | A asks largest first. B ranks by keys times heat | B's ranking where observability is installed, A's otherwise |
| Never without the owner's ask | no edit, reformat or annotation outside a unit's write set, no reconstructed record for untouched code, and no retired practice (`research-retrofit-a.md:172`, `research-retrofit-b.md:200`) | — | both |
| Owners | dWitnessedBar builds the primitive and its legs; dTotalRecall the kinds and the origin field (`research-retrofit-a.md:119`, `research-retrofit-b.md:144`) | A has dBoundRoles render the slot. B gives `build.retrofit` to dDeclaredLoop | both, with Build's items under dScopedBuild, which owns the Build step (v2 `[chain]`) |

## [cross] Where retrofit meets the five systems

- **Tags.** A key for a record or a map entry is a stable tag, never a label: `b0f5247a9` renamed a
  label key that the baseline's header does not record (`research-retrofit-b.md:237`). The ratchet the
  tag design holds on positional references becomes one ledger population, keyed by path and
  reference, never a count (revised 2026-10-17, the audit's M4).
- **Annotations** (revised 2026-10-17, the audit's M5 and M25).
  - The drain's scope is the changed hunks (RF-2). The annotations budget grades the whole block a
    hunk touches.
  - The drain writes no `gov:note` of its own accord. Under `annotations.grammar: voluntary`, the
    default in every preset, it checks a note's shape only where the unit writes one, since presence
    stays voluntary (`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:674-676`). Under
    `required`, it owes a head line on each block a hunk touches.
  - The resolve check's legacy, and the untouched long blocks the budget holds, are ledger
    populations keyed by path and block anchor.
- **Instruction writing.** IW-1's shrink-only list is a ledger population. At adoption, the repository's
  own instruction files are seeded into it.
- **Role shapes.** No new role or shape. The builder drains in its unit pass, and the two raters route
  reconstructed decisions.
- **Memory structure.** `memory.legacy-anchors` applies the same rule to records: derive, never rewrite.
  The memory contract gains the `baseline` and `census` kinds and the `origin` field.
- **One budget per slot.** The legacy slot is one of the work order's slots, capped by
  `retrofit.slot-bytes` at 1 KB like the code-notes slot's 2 KB, and outside `memory.item-budget`, which
  prices memory slices only (systems `[cross]`) (revised 2026-10-17, the audit's M1).

## [design] The design

### [placement] Where it goes, the owner's question

- **A system across the layers, like the five.** It is not a layer, and it is not an expansion.
- **Its ledger is core.** Under P28, the core carries a build alone. In an existing repository, the
  core's gates meet legacy that no unit touched. Without a baseline, map coverage reds on every
  unclaimed key, check 21 reds on every unbound record, and the annotation resolve check reds on day one
  (`research-retrofit-a.md:68`). Other gates pass by finding nothing (`:69`).
- **Three expansions add to it.** Distribution calls the seed from its install and update.
  Observability ranks what remains by reads and files sweep asks. Integrations import a repository's CI
  jobs as legs, test jobs only, each through an adapter row carrying its grant (`[seed]`).
- **Retrofit is not only adoption.** Every check gov ships later lands over an existing tree, including
  a fresh adopter's tree. gov's own kits did: the map seeded 69 keys when it arrived
  (`research-retrofit-b.md:24`), and each kit's adopter seeds its own pins its own way
  (`research-retrofit-a.md:31`). So the seed runs at every registration, and writes only a population that is absent (`[seed]`). A
  fresh repository first uses
  the mechanism the day gov adds a practice to it.

### [ledger] One primitive for every population a check tolerates

- **The factory.** One module in `tools/lib`. Each check registers six things:
  - its population;
  - its seed, an argv measured at a SHA;
  - its key kind: site, key, record or cutoff;
  - its drain: hunk, key or none;
  - its direction;
  - its home.
- **What it extends** (revised 2026-10-17, the audit's M19 and L8).
  - **The readers.** It extends the registry readers gov already has (`research-retrofit-a.md:115`):
    `sh_hygiene.read_registry` and `check_registry`, `encoding_posture.read_registry` and
    `check_registry`, `map_lib.resolve_compare_base` and `derive_baseline_additions`.
  - **Its both-ways arm** is `map_lib.compute_coverage` (`map_lib.py:1404-1412`), the join factory the
    systems record moves to `tools/lib`. The ledger supplies the baseline and adds the never-gains
    and touch rows, so one engine grades a population, never two.
  - **How it reaches an adopter.** Both factories reach a copy-installed adopter as the expansion
    layer settled for every `tools/lib` primitive: an inline copy regenerated under dShippedRelease's
    `gap-tool-04` regen and its drift gate. Until that regen lands, each kit that calls a factory
    carries a generated copy from its first unit.
  - **`compute_coverage`'s consumers move with it:** map_lib.py, gen_map.py, selftest.py,
    test_codebase_map.py and test_codebase_map.template.py.
- **A direction per population** (revised 2026-10-17, the audit's H1). Ledger rows are not all debt.
  - `shrink-only debt`: never gains.
  - `append-only history`: refuses an edited or removed row.
  - `declared set`: checked both ways, and grows with its row.
  - `ceiling`: refuses a value above its row.
  - **Never gains reds shrink-only debt alone.** The first design applied it to every population, so
    every new build README would have owed a widen record.
  - **Of gov's 27, each read from its own header:**
    - 17 are shrink-only debt;
    - 2 are append-only histories: refusal-retirements and transition-audit;
    - 7 are declared sets: readme-contract, method-carriers, legacy-files, playbook-kit-waivers,
      dead-path-waivers and the two lexicon waiver files;
    - 1 is a ceiling: fork-ceilings.

    The table is `registry_directions.py` (`build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`
    `[probes-86]`).
  - **legacy-files stays out of drift's shrink signal,** as `drift_signals.py:124-126` keeps it.
  - **dWitnessedBar's migration** confirms each direction against its reader. Its probe migrates
    readme-contract.txt in a scratch tree, adds a build README with its row, and expects the ratchet
    leg green.
- **A row** holds four things:
  - the key's fields, as its kind declares them;
  - the count of instances under the key;
  - the SHA it was seeded or widened at;
  - its disposition: `seeded`, `carried:<unit>`, `deferred:<ask>`, `keep:<ask>` or
    `widened:<record>`.
- **Its key.**
  - A code site's key is the lexicon's line-free signature: path, rule and identifier.
  - A map or record key is its stable tag.
  - A cutoff's key is its date.
  - No key holds a line number.
- **A rename carries its rows** (revised 2026-10-17, the audit's M34).
  - The ratchet diffs with rename detection (`-M`) over the unit's range. It moves each row from the
    old path to the new one, keeping its disposition.
  - A rename alone is neither a gain nor a drain.
  - Probe: stage a `git mv` of a baselined file, and see the pack green with its rows re-keyed.
- **A deferral follows its ask** (revised 2026-10-17, the audit's M23).
  - While the ask is open, the touch join accepts the carry.
  - Once the ask closes `WONTDO` or `KEEP`, backlog.py's verbs, the row turns `keep:<ask>`. The touch
    join accepts that from then on.
  - Once the ask closes done, its drain has landed, and the row leaves with it.
  - The touch join reads `carried`, `deferred` and `keep`. Both ways reads every state.
- **Concurrent drains merge by row** (revised 2026-10-17, the audit's M28).
  - Each population file takes a row-keyed merge attribute, whose driver keys a row by its
    population's declared key.
  - A drained row wins over a carried one, and a count takes the lower value.
  - The driver extends merge-rows.py with a row class for populations, or is a sibling driver.
  - Its carriers are `.gitattributes`, check-wiring's merge check and the row-keyed replay leg. The
    build replays two concurrent drains of one population.
- **The home** (revised 2026-10-17, the audit's H4 and M24).
  - **No population moves.** Each stays where its check keeps it today: the 27 sit in
    `memory/project/`, under `tools/` and in `memory/map/`. Each is converted in place to the row
    grammar, and its readers are re-pointed in the same unit.
  - **A new population declares its home at registration.** The home is a path the target's hygiene
    check admits. `test.seed` refuses to write anywhere else, and the population then reads unarmed,
    with that reason (`[seed]`).
  - **Why the first design was wrong.** It moved every population to
    `memory/<layer>/baseline/<population>.tsv` by EX-2. Check 3 refuses that directory
    (`check-memory-hygiene.sh:686-688`). An adopter's forked checker cannot be widened to admit it
    (TOOL-cMendedVintage-2). The move would also have stranded every reader of a default path. EX-2
    still homes the records no build owns.
  - **The index of populations is derived** from the registrations, wherever each lives. That retires
    drift-audit's hand-typed SHRINK_ONLY list, which tracks 5 of the 27 lists today
    (`research-retrofit-a.md:27`), and its PINS list beside it.
- **The readers the conversion owes** (revised 2026-10-17, the audit's M14).
  - **`drift_report.derive_low_waters`** (`drift_report.py:778-790`) replays each list's path history.
    It keeps its low water through an in-place conversion that keeps one row per key.
  - **The rest:**
    - `drift_report.py:195`, `:831` and `:3582`;
    - `drift_signals.template.py:199-205`, the DECLARED_EMPTY list, which an adopter that seeds
      populations derives from the index instead;
    - `selftest.py:374`, `:661` and `:2231`;
    - each kit checker that reads its waivers at its default path, such as unattended's pass-order
      checker and roles' stand-in waiver, each with an adopter migration step.
  - **Probe:** convert one list in a scratch tree, and confirm that its signal's low water and verdict
    are unchanged.
- **Every class a check tolerates** (revised 2026-10-17, the audit's M16 and M20).
  - **The 27 exemption files,** converted in place (RF-5).
  - **The 9 scalar pins** in `.lexicon.conf`, `.memory-tree.conf` and `.codebase-map.conf`, each
    becoming a keyed population:
    - The lexicon's two code pins, `VERB_OFFENDER_PIN` and `SUFFIX_OFFENDER_PIN`, are keyed by
      offender name. dMindYourWords registers them under `lexicon.pin` once dWitnessedBar's factory
      lands.
    - Five record and row pins take their record or row keys in dWitnessedBar's migration:
      `DOSSIER_DECISIONS_EMPTY_PIN`, `RECORD_UNBOUND_PIN`, `ROW_DUPLICATE_PIN`, `ORPHAN_ID_PIN` and
      `DEAD_PATH_PIN`.
    - The two unset pins, `SEVERITY_UNLABELLED_PIN` and `LIVE_ROW_PIN`, register unseeded.
  - **The 34 date cutoffs,** 24 in `.memory-tree.conf` and 10 in `.unattended.conf`.
    - Each stays a date in its conf file and registers as a cutoff population, whose never-gains
      reds a date moved later.
    - A cutoff has no drain, since no record is ever rewritten (`[never]`).
    - The derived index counts each cutoff's population.
  - **The inline `gov:` markers a gate reads as a waiver.** Each word is a population of its reading
    check, keyed by path, rule and identifier (systems `[design-annotations]`' marker class).
  - **The census probe** counts each class, and the derived index holds their sum.
- **Keys, never a scalar.** A code or record population is held by its keys. A single count pin acts as a
  waiver: `VERB_OFFENDER_PIN` rose from 412 to 1,087 over 31 edits (`research-retrofit-b.md:31`).
  - The check's day-one population is the 9 pins above, re-counted at `51dfed5a5`. Research A had
    counted 6.
  - A date cutoff is not a population of keys, and it registers as a cutoff.

### [seed] The seed and the census

- **`test.seed`**, a command.
  - It runs when a check registers: at adoption, at a kit update that brings a new check, or when a
    check's predicate widens.
  - **It seeds only an absent population** (revised 2026-10-17, the audit's H3).
    - It runs the check's seed at that SHA, and writes the population only where none exists. The
      codebase map's and drift-audit's adopters already guard the same way:
      `adopt-codebase-map.sh:194-199` says a re-seed "would mask" a violation, and
      `adopt-drift-audit.sh:239-245` says it "would silently reset every ratchet". `test.seed`
      extends those guards, then retires them.
    - A rerun at a later SHA adds only the keys a new or widened predicate measures, each written
      `widened:<record>`. It never rewrites, removes or re-dates an existing row, and the `ratchet`
      pack's `seed laundering` row reds a run that does.
    - A rerun at the same SHA is byte-identical, and it resumes the populations a failed run left
      unwritten.
  - It spends no agent tokens. Its cost is about one bar run plus the map passes
    (`research-retrofit-b.md:157`).
- **A check with no seed** is recorded unarmed and reported, never green, under
  `retrofit.unseeded: unarmed`. Under `refuse`, `adopt` refuses the adoption, and `test.seed` refuses
  the registration, while any registered check lacks a seed (revised 2026-10-17, the audit's M30).
- **A failed seed** (revised 2026-10-17, the audit's H5).
  - A seed records its population unarmed, with its reason, and writes no rows, when any of these
    holds: it exits nonzero, it times out, it reports a dead probe, or it would write where the
    target's hygiene check refuses.
  - An empty population after a live seed also reads unarmed, until a planted row has been seen red.
    That is research A's `populated` row, restored to the `ratchet` pack.
  - `adopt` writes each population atomically. A run that dies partway leaves armed and unwritten
    populations, never a half-written one, and its rerun resumes the unwritten.
  - The build stage-breaks a seed twice, with a nonzero exit and with a probe whose output is empty,
    and sees each case read unarmed, never green.
- **The adopter's own drain load** (revised 2026-10-17, the audit's M36). At adoption, `test.seed` counts the baselined sites in
  the changed hunks of the last 30 days' code commits, per unit. It reports the cap's binding share
  before the touch join arms, since `[drain]`'s rates are gov's.
- **The `adopt` program** runs once in a repository, before its first build, and again at the owner's
  ask. Distribution's `kits.install` calls it. Where distribution is absent, the core's own command runs
  it.
  - `adopt.census`, a command, finds the repository's own practices and counts each one's instances,
    into a `census` record. Practices include lint configurations, CI jobs, decision-shaped documents,
    CODEOWNERS and comment conventions.
  - **CI jobs, denied by default** (revised 2026-10-17, the audit's M32).
    - The census lists each CI job as its own practice, so no class-wide ruling covers them.
    - An imported job becomes a leg only through an integrations adapter row that carries its grant
      and a secret reference.
    - A job whose steps deploy, publish or push is refused.
    - dShippedRelease's registration check reds an imported leg with no grant row, seen red on a
      planted deploy job.
  - `adopt.practices`, the owner, rules each practice once: import, translate, keep alongside or
    retire. The asks go largest first, or by keys times reads where observability is installed. Until a
    ruling, the practice stays alongside.
  - `adopt.decisions` routes the decision candidates through two raters by the author's rubric. The
    owner ratifies the major ones only where `retrofit.decisions` says so (RF-3). A candidate the owner
    declines is kept with the lifecycle `rejected`, which the index hides, so a rerun never proposes it
    again (revised 2026-10-17, the audit's M23).
  - `adopt.reconstruct` reconstructs records for code no unit touched (revised 2026-10-17, the audit's M30).
    - Under `retrofit.reconstruct: at-adoption`, it runs once, after the census.
    - Under `on-ask`, it runs at the owner's ask.
    - Under the default `on-touch`, it never runs. `build.unit-pass` reconstructs on first touch
      instead.
    - The policy value is the owner's ask `[never]` requires.
  - **What `adopt.*` is** (revised 2026-10-17, the audit's M3). Each part is an item of a repository-level group. flow-steps
    declares the group in `[adopt]`, beside the owner's lifecycle controls, so the item join reads
    it.
- **An offered update** (Revised 2026-10-17, the folds' closing review). An update `kits.offer` offers runs neither `test.seed` nor `adopt` in
  the adopter's tree, since both run the adopter's code. Its new checks land unseeded and read unarmed
  under `retrofit.unseeded: unarmed`. Its outbox order names the adopter's own run of `test.seed`, which
  arms them. Under `refuse`, the adopter's own lander refuses the update until that run.

### [drain] The drain on touch

- **The slot.** The builder's work order carries a legacy slot: counts per path and population for the
  unit's write set, at most 1 KB. It renders in one of four states:
  - filled;
  - empty, when nothing is baselined;
  - "not seeded", when its check is unarmed;
  - "not installed", when no ledger exists (revised 2026-10-17, the audit's M2).
- **`build.unit-pass`, filled.** The builder drains the baselined sites inside the hunks it changes. It
  also claims the baselined map keys its write set holds, which means writing the dossier for the code it
  touches. The keys it claims drop their grace through the map's existing touch-drop,
  `_drop_affordance_exempt` (`map_diff.py:107-118`). The touch join calls it, so the drop is the one
  writer to that population (revised 2026-10-17, the audit's M21). What it does not drain within the caps, it carries, with a
  deferral row that names an ask.
- **`build.scope`, filled, adds the touch join** (revised 2026-10-17, the audit's M6 and M13).
  - **One check, one home.** The touch join is `build.scope`'s check, and dScopedBuild owns it. The
    `ratchet` pack points at it, never restates it.
  - **What it finds.** A unit whose changed hunks still hold a baselined site, or whose write set
    holds a baselined key, with neither a drain nor a carry within the caps.
  - **The value grades it.** `build.scope: refuse` refuses it. `warn-and-ask`, the standard and
    guarded presets' value, warns and asks the owner. `report`, velocity's value, reports it.
  - **Its range** is the union of `git diff-tree -U0 --no-merges -M <commit>` over the unit's own
    commits. It is never a frozen base older than a merge. It is never `--first-parent` alone, and
    never `<default>...HEAD`, which spans every unit on the branch.
  - **Probe:** merge a main commit that edits a baselined site into the unit's range. Expect the
    touch join green for that site, and still red on a baselined site the unit's own commit leaves.
- **Under `retrofit.drain: file`,** RF-2's third option, the unit owes every baselined site in each
  touched file, still under `retrofit.drain-cap`. That is a policy over the drain's scope, not a new
  drain kind. Under `off`, nothing is owed, and the slot still renders (revised 2026-10-17, the audit's M30).
- **The caps.**
  - 20 sites per unit, which a model estimates binds on 0.18% of gov's code commits
    (`research-retrofit-a.md:193`).
  - 3 claims per unit, the measured p90 (`research-retrofit-b.md:218`).
- **The cost.** A mean of 0.25 sites per code commit, modelled the same way
  (`research-retrofit-a.md:98`). The gate adds the touch join's diff over the unit's own commits.
  Orientation needs no extra lookup.
- **Both figures are modelled, and both are gov's** (revised 2026-10-17, the audit's M36 and L4).
  - Each is site density times lines touched, over gov's 1,093 code commits in 30 days. Neither
    counts baselined sites in changed hunks.
  - Legacy clusters in hot files, so the model understates the cap's binding share.
  - 98.9% of gov's code lines are 90 days old or younger, so an adopter with years of legacy can bind
    the cap far more often.
  - dWitnessedBar re-measures both by counting real sites of today's site registries
    (encoding-posture-sites.txt and spawn-idiom-sites.txt) in each commit's changed hunks.
  - `test.seed` measures an adopter's own figures at adoption (`[seed]`).

### [ratchet] The `ratchet` leg pack

| Check | Red on |
|---|---|
| never gains | in shrink-only debt, a key or a count above the base's, with no `widened` disposition |
| both ways | a measured instance with no row, or a row no scan finds |
| touch join | `build.scope`'s check (`[drain]`), pointed at, never restated |
| untouched quiet | its negative arm: a baselined offense outside the unit's hunks stays green, and an unbaselined one planted there reds never gains |
| unarmed | a registered check with no seed, or with a failed or dead-probe seed, that reads green |
| populated | an empty population after a live seed that reads armed before a planted row was seen red |
| seed laundering | a `test.seed` rerun that removes, rewrites or re-dates an existing row, seen red on a planted offense re-seeded at a later SHA |
| rename | a `git mv` of a baselined file that reads as a gain or a drain |
| merge | a spurious gain or stale row after two staged branches drain one population and merge |
| keys, not a scalar | a population held by one count, its day-one population the 9 pins `[ledger]` lists |
| key shape | a label key holding a number |

- **The base** is `map_lib.resolve_compare_base`'s rule: the merge-base with the observed remote
  branch, else its tip. With no base, as at an adoption with no remote, every population reports
  unresolved and never reads green (revised 2026-10-17, the audit's M13).
- **The origin check left the pack** for `[origin]`, where dTotalRecall owns it (revised 2026-10-17, the audit's M2 and M11).

### [origin] Origin on every record

- **The field.** Every record kind gains `origin`, with one of three values:
  - `written`;
  - `reconstructed@<sha8>`, with the sources it came from;
  - `imported:<path>`.
- **Derived once, never typed** (revised 2026-10-17, the audit's M11).
  - A record is `written` when the build that lands it is the build of its subject's last-changing
    commit before it lands.
  - It is `reconstructed@<sha8>` when gov derived it from sources: `adopt.decisions`,
    `adopt.reconstruct`, or a first-touch dossier.
  - It is `imported:<path>` when it came from the repository's own documents.
- **The check, dTotalRecall's** (revised 2026-10-17, the audit's M2 and M11).
  - It moved here from the `ratchet` pack.
  - It re-derives each record's origin from history, independently of the write path, comparing the
    subject's last-changing commit before the record lands with the record's landing build.
  - It reds a record whose stored origin differs, seen red on a planted record typed `written` whose
    subject's last change predates its build.
- **A reconstructed record is never a witness.**
  - It renders labelled in work orders.
  - It ranks below written records in the reuse digest.
  - It never seeds a directive.
  - **Where those are built** (revised 2026-10-17, the audit's M3). dTotalRecall declares `origin` among the fields every slice
    renders, and ranks the reuse digest. dBoundRoles' work-order render shows a slice's declared
    fields, so the label needs no change there.

### [practices] Per practice

| Practice | Derived at adoption | Done on touch | The owner |
|---|---|---|---|
| tags | namespaces from the inventories and the map | a tag on each touched site | rules the namespaces |
| annotations | `refs=` rows from the comment refs that resolve, 1,248 of 1,250 in gov (`research-retrofit-a.md:52`) | under `annotations.grammar: voluntary`, the default, a note's shape checked where the unit writes one; under `required`, a head line on each block a hunk touches (revised 2026-10-17, the audit's M25) | none |
| codebase map and reuse | definitions and callers, generated | a dossier on first touch, and a reuse proposal | accepts each entry (LR-6) |
| decision log | candidates from decision-shaped documents, and from commit trailers under `docs-and-trailers` | none | none under `author-rubric`; ratifies each major one under the other two values (RF-3) |
| bug classes | candidates from fix commits | a class on a confirmed finding | none |
| specs | none: legacy code gets no spec | a spec for new units only | none |
| instruction units | the repository's instruction files join IW-1's list | migration per step | retires its own documents |
| records | bindings marked `none`, by the `Serves: none` pass | a real binding on touch | none |
| CI jobs | each job counted as its own practice | none | rules each job: a test job imported as a leg through an integrations adapter row with its grant and secret reference; a job that deploys, publishes or pushes refused (revised 2026-10-17, the audit's M32) |

### [cadence] The cadence and the owner's ask

- **`maintain.retrofit-heat`**, a reading in observability. It reports the share of the period's code
  reads that land on baselined files no unit touched in the prior 30 days. It ranks what remains by
  reads times touches (revised 2026-10-17, the audit's M22).
  - Under `retrofit.cadence: hot-first`, the default wherever observability is installed (RF-6), it
    files each period's sweep of the most-read untouched legacy as a patch build, under the standing
    ask that the policy value is.
  - Under `off`, it files sweep asks only.
  - It edits nothing itself.
- **A sweep** is a patch build, run at the owner's ask or under `hot-first`'s standing one. It drains
  one population or path, through `entry.place`'s `patch` disposition, and enters at Design.
- **What gov cannot measure.** In gov, reads beyond touch are under 1%. But gov's tree is 108 days old,
  and nearly every file changed within 90 days (`research-retrofit-a.md:38`,
  `research-retrofit-b.md:62`). A codebase with years of dormant code may read far more legacy that no
  unit touches. The reading measures that in the adopter, and RF-6 sets what it switches on.
  `[drain]`'s cap and cost figures are gov's too, modelled on young code, and `test.seed` measures an
  adopter's own at adoption (revised 2026-10-17, the audit's M36).

### [never] Never, without the owner's ask

- No edit, reformat or annotation outside a unit's write set.
- No drain outside the touched hunks.
- No population grows without a widen record.
- No rewrite of a record the repository already had.
- No retired practice.
- No reconstructed record for code no unit touched.
- A policy value that names a run is the owner's standing ask for that run: `retrofit.cadence:
  hot-first` for the period's sweep, and `retrofit.reconstruct: at-adoption` for the reconstruction
  (revised 2026-10-17, the audit's M22 and M30).

### [progress] Progress, derived

- A card cell per population shows the count when seeded, the count now, and the drain this period.
- Where observability is installed, it adds the share of reads on untouched legacy.
- dTotalRecall registers the cell at the card's cell point, reading the ledger, and the share is
  dTendedCadence's `maintain.retrofit-heat` reading (revised 2026-10-17, the audit's M3).

### [owners] Owners

| Chain build | Its part |
|---|---|
| dWitnessedBar | the factory, with each registration's direction and home; the `ratchet` leg pack; `test.seed`, seeding only an absent population and recording a failed seed unarmed; the in-place conversion of gov's own 27 registries (RF-5) and the seven record and row pins onto the ledger, with the readers the conversion owes; the date cutoffs registered as cutoffs; the positional references and IW-1's legacy list registered from dOrderedCharter's keyed lists; the `pack` tag namespace (revised 2026-10-17, the audit's H1, H3, H4, H5, M14, M16, M20 and M24) |
| dTotalRecall | the `baseline` and `census` kinds, which declare the ledger's files once they exist; the `origin` field, its check and its rendering; the `adopt` program, run by the core's own command where distribution is absent: `adopt.census`, `adopt.practices`, `adopt.decisions` and `adopt.reconstruct` (Revised 2026-10-17, the folds' closing review: this row once named `adopt.census` alone); the progress cell; the annotation resolve check's legacy and the untouched long blocks as populations; the `marker` namespace (revised 2026-10-17, the audit's M2, M3 and M11) |
| dScopedBuild | `build.unit-pass` and `build.scope`, filled: the claims over map keys, and the touch join as `build.scope`'s one check, over the unit's own commits, calling the map's touch-drop (revised 2026-10-17, the audit's M6, M7, M13 and M21) |
| dBoundRoles | the legacy slot's render, in its four states |
| dTendedCadence | `maintain.retrofit-heat`, filing the period's sweep under `hot-first`, and the progress cell's share of reads |
| dShippedRelease | the install and update hooks that call `adopt` and `test.seed`; the integrations import of CI jobs as legs, denied by default (revised 2026-10-17, the audit's M32) |
| dMindYourWords | the lexicon's two code pins as keyed populations under `lexicon.pin`, once dWitnessedBar's factory lands (revised 2026-10-17, the audit's M16) |

Each consumer descends from its producer (revised 2026-10-17, the audit's M2). dTotalRecall and dBoundRoles follow
dWitnessedBar, whose ledger they read, and dShippedRelease follows dTotalRecall, whose census `adopt`
runs. dOrderedCharter, at the chain's root, keeps its two populations as keyed lists until the factory
registers them.

### [keys] Keys

| Key | Values | Default |
|---|---|---|
| `retrofit.drain` | hunk, file, off | hunk (RF-2) |
| `retrofit.drain-cap` | 5, 20, 50 sites per unit | 20 |
| `retrofit.claim-on-touch` | claim, carry, off | claim |
| `retrofit.claim-cap` | 1, 3, 5 keys per unit | 3 |
| `retrofit.widen` | record-reason, refuse | record-reason |
| `retrofit.unseeded` | unarmed, refuse | unarmed |
| `retrofit.reconstruct` | on-touch, at-adoption, on-ask | on-touch |
| `retrofit.decisions` | author-rubric, docs-owner-ratifies, docs-and-trailers | author-rubric, set per repository (RF-3) |
| `retrofit.practice-pending` | alongside, propose-retire | alongside (RF-4) |
| `retrofit.cadence` | off, hot-first | hot-first where observability is installed, off where it is absent (RF-6) |
| `retrofit.slot-bytes` | 512, 1024, 2048 | 1024 |

`retrofit.practice-pending`'s second value is `propose-retire`, RF-4's second option, which
`adopt.practices` reads. It was written `refuse`, which no option named (revised 2026-10-17, the audit's M30).

## [forks] To put to the owner

Run A named its forks RF-1 to RF-5 and run B named its forks RT-1 to RT-5. RT- already names the
runtime layer's forks, so the design keeps A's names and A's numbering. B's RT-5 becomes RF-6.

| Fork | The question | Options, the recommendation first |
|---|---|---|
| RF-1 | Where does retrofit go? | a system across the layers, with its ledger in the core and its parts owned by the chain builds in `[owners]`; a `retrofit` expansion, which fails P28 because the core's gates red on legacy without it; one new chain build that owns all of it |
| RF-2 | What does a unit owe the legacy it touches? | drain the changed hunks and claim the touched keys, capped at 20 sites and 3 claims per unit, and carry the rest; carry only, reporting touched legacy and never requiring a drain; drain every touched file whole, which owes a median of 55 to 97 sites per commit |
| RF-3 | How are an existing repository's major decisions recovered? | candidates from decision-shaped documents, two raters routing them, the owner ratifying each major one, and commit trailers mined only at the owner's ask; mine trailers at adoption too, which gave 1,829 candidates in gov against about 12 majors; let the author's rubric decide, with no ratification |
| RF-4 | What happens to a repository practice the owner has not ruled on? | it stays alongside; it is proposed for retirement |
| RF-5 | Do gov's own 27 registries move onto the ledger? | yes, in dWitnessedBar, which also retires drift's hand-typed list; no, the ledger serves new checks only, and the count ratchet stays written twice |
| RF-6 | When does the cadence sweep run? | off until the owner opts in, with observability's reading reporting the share of reads on untouched legacy; hot-first by default wherever observability is installed |

## [answers] The owner's answers, 2026-10-17

Each answer is quoted verbatim.

| Fork | The owner's answer | What it settles |
|---|---|---|
| RF-1 | "Across the layers (Recommended)" | retrofit is a system across the layers. Its ledger is core, and its parts belong to the chain builds in `[owners]` |
| RF-2 | "Drain hunks, capped (Recommended)" | `retrofit.drain` defaults to `hunk`: a unit drains the baselined sites in its changed hunks and claims the keys it touches, within 20 sites and 3 claims, and carries the rest |
| RF-3 | "Author's rubric by default, owner-switchable between the three options per repo" | one key, `retrofit.decisions`, replaces the two the design drafted. Its values are the three options: `author-rubric` (the default), `docs-owner-ratifies` and `docs-and-trailers`. The owner sets it per repository. Under `author-rubric`, no reconstructed decision waits on the owner, and each stays marked `reconstructed` |
| RF-4 | "Stays alongside (Recommended)" | `retrofit.practice-pending` defaults to `alongside`: a practice the owner has not ruled on stays as it is |
| RF-5 | "Migrate in dWitnessedBar (Recommended)" | gov's own 27 registries move onto the ledger in dWitnessedBar. The index of populations is derived from the registrations, which retires drift's hand-typed list |
| RF-6 | "Hot-first by default" | `retrofit.cadence` defaults to `hot-first` wherever observability is installed. Each period, Maintain files a sweep of the most-read untouched legacy as a patch build. The policy value is the standing ask that `[never]` requires. Where observability is absent, the key reads `off`, and its slot renders not installed, with the touch drain as the core's fallback. So the default never meets `policy.on-missing-expansion` |

## [gaps-proposed] Gaps to register once the forks settle

| Gap | Severity | Owner |
|---|---|---|
| no single baseline primitive: 27 registries in at least 6 grammars, with the count ratchet written twice (`research-retrofit-a.md:26`) | HIGH | dWitnessedBar |
| "shrink-only" is enforced only for the map's baseline: unarmed-branches grew from 9 rows to 159, and drift tracks 5 of the 27 lists by hand (`research-retrofit-a.md:27`) | MED | dWitnessedBar |
| baselines are not tied to touch: five kits stay baselined after 14 to 278 touches each, and the per-file count ratchet let 29 of 129 encoding sites persist on edited lines (`research-retrofit-b.md:118`, `research-retrofit-a.md:102`) | MED | dScopedBuild |
| a count pin over code acts as a waiver: `VERB_OFFENDER_PIN` rose from 412 to 1,087 (`research-retrofit-b.md:31`); the lexicon's own instance is `gap-mem-10`'s (corrected 2026-10-17: it was written as gap-lex-08's) | MED | dWitnessedBar |
| the map's touch-drop is wired to nothing: `--drop-affordance-exempt` has no caller in `tools/`, `.claude/`, `.github/` or `.githooks/`, and `WIRE-INTO-PROJECT.md:554` calls the drop mechanical | MED | dTotalRecall |
| no census of a repository's own practices, and no progress cell | MED | dTotalRecall |
| no origin on records, so a reconstructed record reads as written | LOW | dTotalRecall |
| label keys churn: `b0f5247a9` renamed a key that the baseline's header does not record (`research-retrofit-b.md:237`) | LOW | dWitnessedBar |

## [open] What the round owes

- The owner's answers to `[forks]`.
- Then the fold. v2's catalogue gains the `retrofit.*` keys, the register gains `[gaps-proposed]`, the
  chain rows gain the parts in `[owners]`, and the systems record's `[cross]` gains retrofit. Revised
  2026-10-17: folded, the gaps registered as `gap-test-14` to `gap-test-17`, `gap-build-05` and
  `gap-mem-23` to `gap-mem-25`.
- A Tier-2 review of the round, at the owner's word. Done 2026-10-17: dispatch 86 returned CLEAN WITH
  FIXES, and its fold is mapped item by item in
  `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md` `[fold-systems-retrofit]`.
