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
| One primitive | one baseline primitive replaces each check's own list: gov keeps 27 registries in at least 6 grammars, with the count ratchet written twice (`research-retrofit-a.md:26`, `research-retrofit-b.md:149`) | A counts per check, subject and class, with rows in each check's home (`:111`). B keeps a set of keys, one file per population under `memory/<layer>/baseline/` (`:149`) | one factory; A's count is B's `#k`; B's home, by EX-2 |
| Keys, never lines | a row's key is a path, a key or a record, never a line number (`research-retrofit-a.md:111`, `research-retrofit-b.md:149`) | B refuses a label key that holds a number (`:177`) | both |
| The seed | a command seeds every check at a SHA, idempotently, with no agent (`research-retrofit-a.md:182`, `research-retrofit-b.md:157`) | — | both, at every registration as well as adoption |
| An unseeded check | it never reads green (`research-retrofit-a.md:130`, `research-retrofit-b.md:206`) | A refuses the adoption by default (`:198`). B records the population unarmed (`:206`) | B's |
| Never gains, both ways | a key or a count above the base's reds, and so does a row no scan finds (`research-retrofit-a.md:125`, `research-retrofit-b.md:170-171`) | A admits growth through a `reason:` row (`:111`). B admits it through a `widen` record (`:219`) | a widen record |
| Drain on touch | a unit that touches baselined legacy drains it or carries it, under a per-unit cap, and untouched legacy never reds (`research-retrofit-a.md:127`, `research-retrofit-b.md:173`) | A caps sites at 20 per unit (`:193`). B caps keys at 3 per unit (`:218`) | both caps: sites for code, keys for claims |
| Drain scope | the file scope loses, owing a median of 55 sites per commit in A and 97 in B (`research-retrofit-a.md:102`, `research-retrofit-b.md:136`) | A drains changed hunks, a median of 0.03 sites per commit and a p90 of 0.46 (`:98`). B drains the annotations' touched block (`:139`) | the changed hunks, the scope the annotations' budget reads |
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
  tag design holds on positional references becomes one ledger population.
- **Annotations.** The drain's scope is the annotations' touched block. On a block it touches, the drain
  writes the `gov:note` head line. The resolve check's legacy is a ledger population.
- **Instruction writing.** IW-1's shrink-only list is a ledger population. At adoption, the repository's
  own instruction files are seeded into it.
- **Role shapes.** No new role or shape. The builder drains in its unit pass, and the two raters route
  reconstructed decisions.
- **Memory structure.** `memory.legacy-anchors` applies the same rule to records: derive, never rewrite.
  The memory contract gains the `baseline` and `census` kinds and the `origin` field.
- **One budget.** The legacy slot sits inside the work order's one byte budget per item, at most 1 KB.

## [design] The design

### [placement] Where it goes, the owner's question

- **A system across the layers, like the five.** It is not a layer, and it is not an expansion.
- **Its ledger is core.** Under P28, the core carries a build alone. In an existing repository, the
  core's gates meet legacy that no unit touched. Without a baseline, map coverage reds on every
  unclaimed key, check 21 reds on every unbound record, and the annotation resolve check reds on day one
  (`research-retrofit-a.md:68`). Other gates pass by finding nothing (`:69`).
- **Three expansions add to it.** Distribution calls the seed from its install and update.
  Observability ranks what remains by reads and files sweep asks. Integrations import a repository's CI
  jobs as legs.
- **Retrofit is not only adoption.** Every check gov ships later lands over an existing tree, including
  a fresh adopter's tree. gov's own kits did: the map seeded 69 keys when it arrived
  (`research-retrofit-b.md:24`), and each kit's adopter seeds its own pins its own way
  (`research-retrofit-a.md:31`). So the seed runs at every registration. A fresh repository first uses
  the mechanism the day gov adds a practice to it.

### [ledger] One primitive for every population a check tolerates

- **The factory.** One module in `tools/lib`, extending the registry readers gov already has
  (`research-retrofit-a.md:115`). Each check registers its population, its seed (an argv measured at a
  SHA), its key kind (site, key or record) and its drain (hunk, key or none).
- **A row** holds the key's fields as its kind declares them, the count of instances under the key, the
  SHA it was seeded or widened at, and its disposition: `seeded`, `carried:<unit>`, `deferred:<ask>` or
  `widened:<record>`.
  - A code site's key is the lexicon's line-free signature: path, rule and identifier.
  - A map or record key is its stable tag.
  - No key holds a line number.
- **The home.** One file per population, `memory/<layer>/baseline/<population>.tsv`, under EX-2. The
  layer is the check's own. The index of populations is derived from the registrations. That retires
  drift-audit's hand-typed list, which tracks 5 of the 27 lists today (`research-retrofit-a.md:27`).
- **Keys, never a scalar.** A code population is held by its keys. A single count pin acts as a waiver:
  `VERB_OFFENDER_PIN` rose from 412 to 1,087 over 31 edits (`research-retrofit-b.md:31`).

### [seed] The seed and the census

- **`test.seed`**, a command.
  - It runs when a check registers: at adoption, at a kit update that brings a new check, or when a
    check's predicate widens.
  - It runs the check's seed at that SHA and writes the population. A rerun at the same SHA is
    byte-identical.
  - It spends no agent tokens. Its cost is about one bar run plus the map passes
    (`research-retrofit-b.md:157`).
- **A check with no seed** is recorded unarmed and reported, never green (`retrofit.unseeded`).
- **The `adopt` program** runs once in a repository, before its first build, and again at the owner's
  ask. Distribution's `kits.install` calls it. Where distribution is absent, the core's own command runs
  it.
  - `adopt.census`, a command, finds the repository's own practices and counts each one's instances,
    into a `census` record. Practices include lint configurations, CI jobs, decision-shaped documents,
    CODEOWNERS and comment conventions.
  - `adopt.practices`, the owner, rules each practice once: import, translate, keep alongside or
    retire. The asks go largest first, or by keys times reads where observability is installed. Until a
    ruling, the practice stays alongside.
  - `adopt.decisions` routes the decision candidates through two raters, and the owner ratifies the
    major ones, as RF-3 settles.

### [drain] The drain on touch

- **The slot.** The builder's work order carries a legacy slot: counts per path and population for the
  unit's write set, at most 1 KB. It renders filled, empty when nothing is baselined, or "not seeded".
- **`build.unit-pass`, filled.** The builder drains the baselined sites inside the hunks it changes. It
  also claims the baselined map keys its write set holds, which means writing the dossier for the code it
  touches. What it does not drain within the caps, it carries, with a deferral row that names an ask.
- **`build.scope`, filled, adds the touch join.** It reds a unit whose changed hunks still hold a
  baselined site, or whose write set holds a baselined key, with neither a drain nor a carry within the
  caps.
- **The caps.**
  - 20 sites per unit, which binds on 0.18% of code commits (`research-retrofit-a.md:193`).
  - 3 claims per unit, the measured p90 (`research-retrofit-b.md:218`).
- **The cost.** A mean of 0.25 sites per code commit (`research-retrofit-a.md:98`). The gate adds one
  `git diff -U0` over the unit's range. Orientation needs no extra lookup.

### [ratchet] The `ratchet` leg pack

| Check | Red on |
|---|---|
| never gains | a key or a count above the base's, with no `widened` disposition |
| both ways | a measured instance with no row, or a row no scan finds |
| touch join | as `build.scope` above |
| untouched quiet | its negative arm: an offense planted outside the diff must stay green |
| unarmed | a registered check with no seed that reads green |
| keys, not a scalar | a code population held by one count |
| key shape | a label key holding a number |
| origin | a record that reads `written` while its subject predates its build's base |

### [origin] Origin on every record

- **The field.** Every record kind gains `origin`, with one of three values:
  - `written`;
  - `reconstructed@<sha8>`, with the sources it came from;
  - `imported:<path>`.
- **Derived, never typed.** A record is `written` only when it lands in the build that changed its
  subject.
- **A reconstructed record is never a witness.** It renders labelled in work orders, ranks below written
  records in the reuse digest, and never seeds a directive.

### [practices] Per practice

| Practice | Derived at adoption | Done on touch | The owner |
|---|---|---|---|
| tags | namespaces from the inventories and the map | a tag on each touched site | rules the namespaces |
| annotations | `refs=` rows from the comment refs that resolve, 1,248 of 1,250 in gov (`research-retrofit-a.md:52`) | a `gov:note` head line on each touched block | none |
| codebase map and reuse | definitions and callers, generated | a dossier on first touch, and a reuse proposal | accepts each entry (LR-6) |
| decision log | candidates from decision-shaped documents | none | ratifies each reconstructed major decision (RF-3) |
| bug classes | candidates from fix commits | a class on a confirmed finding | none |
| specs | none: legacy code gets no spec | a spec for new units only | none |
| instruction units | the repository's instruction files join IW-1's list | migration per step | retires its own documents |
| records | bindings marked `none`, by the `Serves: none` pass | a real binding on touch | none |

### [cadence] The cadence and the owner's ask

- **`maintain.retrofit-heat`**, a reading in observability. It reports the share of the period's code
  reads that land on baselined files no unit touched in the prior 30 days. It ranks what remains by
  reads times touches, and it files sweep asks. It edits nothing.
- **A sweep** is a patch build at the owner's ask. It drains one population or path, through
  `entry.place`'s `patch` disposition, and enters at Design.
- **What gov cannot measure.** In gov, reads beyond touch are under 1%. But gov's tree is 108 days old,
  and nearly every file changed within 90 days (`research-retrofit-a.md:38`,
  `research-retrofit-b.md:62`). A codebase with years of dormant code may read far more legacy that no
  unit touches. The reading measures that in the adopter, and RF-6 sets what it switches on.

### [never] Never, without the owner's ask

- No edit, reformat or annotation outside a unit's write set.
- No drain outside the touched hunks.
- No population grows without a widen record.
- No rewrite of a record the repository already had.
- No retired practice.
- No reconstructed record for code no unit touched.

### [progress] Progress, derived

- A card cell per population shows the count when seeded, the count now, and the drain this period.
- Where observability is installed, it adds the share of reads on untouched legacy.

### [owners] Owners

| Chain build | Its part |
|---|---|
| dWitnessedBar | the factory, the `ratchet` leg pack, `test.seed` and the registration fields |
| dTotalRecall | the `baseline` and `census` kinds, the `origin` field, and `adopt.census` |
| dScopedBuild | `build.unit-pass` and `build.scope`, filled |
| dBoundRoles | the legacy slot's render |
| dTendedCadence | `maintain.retrofit-heat` |
| dShippedRelease | the install and update hooks that call `adopt` and `test.seed` |

### [keys] Keys

| Key | Values | Default |
|---|---|---|
| `retrofit.drain` | hunk, file, off | as RF-2 settles |
| `retrofit.drain-cap` | 5, 20, 50 sites per unit | 20 |
| `retrofit.claim-on-touch` | claim, carry, off | claim |
| `retrofit.claim-cap` | 1, 3, 5 keys per unit | 3 |
| `retrofit.widen` | record-reason, refuse | record-reason |
| `retrofit.unseeded` | unarmed, refuse | unarmed |
| `retrofit.reconstruct` | on-touch, at-adoption, on-ask | on-touch |
| `retrofit.decisions-import` | docs, docs-and-trailers, none | as RF-3 settles |
| `retrofit.reconstructed-major` | owner-ratifies, author-rubric | as RF-3 settles |
| `retrofit.practice-pending` | alongside, refuse | as RF-4 settles |
| `retrofit.cadence` | off, hot-first | as RF-6 settles |
| `retrofit.slot-bytes` | 512, 1024, 2048 | 1024 |

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

## [gaps-proposed] Gaps to register once the forks settle

| Gap | Severity | Owner |
|---|---|---|
| no single baseline primitive: 27 registries in at least 6 grammars, with the count ratchet written twice (`research-retrofit-a.md:26`) | HIGH | dWitnessedBar |
| "shrink-only" is enforced only for the map's baseline: unarmed-branches grew from 9 rows to 159, and drift tracks 5 of the 27 lists by hand (`research-retrofit-a.md:27`) | MED | dWitnessedBar |
| baselines are not tied to touch: five kits stay baselined after 14 to 278 touches each, and the per-file count ratchet let 29 of 129 encoding sites persist on edited lines (`research-retrofit-b.md:118`, `research-retrofit-a.md:102`) | MED | dScopedBuild |
| a count pin over code acts as a waiver: `VERB_OFFENDER_PIN` rose from 412 to 1,087 (`research-retrofit-b.md:31`); the lexicon's own instance is gap-lex-08's | MED | dWitnessedBar |
| the map's touch-drop is wired to nothing: `--drop-affordance-exempt` has no caller in `tools/`, `.claude/`, `.github/` or `.githooks/`, and `WIRE-INTO-PROJECT.md:554` calls the drop mechanical | MED | dTotalRecall |
| no census of a repository's own practices, and no progress cell | MED | dTotalRecall |
| no origin on records, so a reconstructed record reads as written | LOW | dTotalRecall |
| label keys churn: `b0f5247a9` renamed a key that the baseline's header does not record (`research-retrofit-b.md:237`) | LOW | dWitnessedBar |

## [open] What the round owes

- The owner's answers to `[forks]`.
- Then the fold. v2's catalogue gains the `retrofit.*` keys, the register gains `[gaps-proposed]`, the
  chain rows gain the parts in `[owners]`, and the systems record's `[cross]` gains retrofit.
- A Tier-2 review of the round, at the owner's word.
