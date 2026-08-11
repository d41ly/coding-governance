# DEPL-aSealedCaravan-2 — govkit, the mechanical deployer

**Status:** INPROGRESS · rev-6 · 2026-08-11 · node a · Tier-2 · base 16aeb5ef · streams deployer · ratified 2026-08-11

## 1. Goal

Replace the prose adoption runbook with `govkit` — a descriptor-driven deployer that lands a chosen
subset of this repo's kits into a target repo that has none, either unattended or by prompting the
owner, and writes a receipt recording what was installed from which commit. Following 66 imperative
steps by hand is how a target ends up with kits in five homes and no record of what it took.

## 2. Scope (IN)

- **S1** `tools/govkit/govkit.py` — a Python stdlib core, no third-party dependency, running on the
  deployer machine only. Subcommands `plan`, `apply`, `apply --resume`, `intake`, `check`, `selfcheck`.
- **S2** A `kit.toml` descriptor for each entry in a tracked kit registry, declaring that kit as data:
  id, version constant location, `requires` and `requires_if`, the files it installs with their roles,
  precedence and DESTINATIONS, the config keys it needs split by the consumer that requires them, its
  adopt command, its outcome map, its gate legs with their guards, its LF pins, its scope class, and
  its non-mechanical holes each carrying a runnable discharge probe. The registry — not a directory
  listing — is the population, and that population extends past `tools/*` directories: single files
  directly under `tools/`, files under `.githooks/` and `skills/session-kickoff/`, and the shipped root
  playbook files are all deployable. **No population count appears anywhere in this document.** Every
  one is DERIVED by `selfcheck` over the tracked surface, because this spec has now twice stated a
  count that the tree moved underneath — see section 4.
- **S3** A target descriptor at `<target>/.governance/deploy.toml`, written once by `intake` and
  committed. It carries the kit subset, every owner decision, and the failure-policy knobs. Committed,
  it is the standing authorization for an unattended re-run.
- **S4** A receipt at `<target>/.governance/install.json` plus a flat `<target>/.governance/install.sums`
  in `sha256sum -c` format, so a target verifies its own install with bash alone. Per file: role,
  sha256, kit id and version, and the gov source commit the bytes came from.
- **S5** `apply` in three ordered steps, of which the last two are the phases. **Baseline** runs the
  target's own declared gate command once, records a per-leg verdict, and writes nothing. **Land**
  copies files, renders artifacts and wires legs into the target's runner, in a hard order:
  `.gitattributes` blocks, then `git add --renormalize`, then kit content, then rendered artifacts,
  then `git add` of everything written, then the target's gate-runner and CI legs last. **Configure**
  runs each kit's adopt command. Every copy is taken from the gov git index at a recorded commit,
  never from the working tree. The `git add` step is not housekeeping: every gate in this suite reads
  the index, so an unstaged install is invisible to the verification that follows it. `apply` stops
  there — section 3 states that it never commits, branches, pushes or opens a pull request.
- **S6** The default kit set is the three-layer chain plus codebase-map and memory-recall: playbook,
  kickoff manifest with its ratchet, memory-tree, codebase-map, memory-recall. `--kits` selects
  otherwise. `--all` is DERIVED — it selects every registry entry that is neither an exemption nor
  marked `selectable = "conditional"` — rather than being a hand-kept list. A hand-kept list is how a
  registry grows an entry no selection ever reaches, and the unattended kit is exactly that today: it
  ships an adopter, a rendered Skill, a binding protocol and five gate legs, and no rev of this spec
  before rev-6 named it at all.
- **S7** Unattended and interactive are one code path with two decision sources. `intake` prompts and
  writes the target descriptor; `apply --unattended` reads every answer from that descriptor and
  refuses rather than guessing when one is absent.
- **S8** Every non-mechanical hole is declared in its kit's descriptor as a `[[hole]]` carrying a
  `discharge` probe the deployer RUNS, and the outbox is derived from the union of holes over the
  SELECTED kits. Each hole also declares what OBSERVES it: `blocks_adopt` when an undischarged hole
  makes the adopter fail, so that kit lands but is not configured and `govkit apply --resume`
  configures it once the order is discharged; `blocks_gate` when it instead leaves one of that kit's
  gate legs red or absent; and NEITHER when nothing in the target observes it at all. That third class
  is the majority and is the whole reason S8 exists — a hole nothing observes is invisible without the
  probe. The outbox lives at `<target>/.governance/outbox/<hole-id>.md`, one order per hole. `check`
  distinguishes three states — not landed, landed but inert, adopted — and reds on an undischarged hole
  regardless of what the kit's adopter exited with.
- **S9** `check` — a read-only verifier over an installed target: receipt integrity against
  `install.sums`, byte provenance against the recorded gov commit, every kit's own `--check` arm where
  one exists, every declared hole's discharge probe, and the outbox. It is the leg a target repo runs
  in its own CI. Every arm carries its own acceptance criterion in section 6, because an arm no
  criterion observes is precisely how a verifier ships vacuous.
- **S10** `skills/deploy-governance/SKILL.md` so an agent invokes the deployer rather than reading the
  runbook. `WIRE-INTO-PROJECT.md` is demoted to narrative, kept honest by a parity gate asserting
  every descriptor step has a runbook section and the reverse.
- **S11** An acceptance matrix over fixture repos, each required to pass apply-twice-changed-zero, on
  both POSIX and Git-Bash.
- **S12** The registry is asserted over the tracked deployable SURFACE rather than over `tools/*`
  directories. Every depth-1 path under `tools/`, every path under `.githooks/` and
  `skills/session-kickoff/`, and every shipped root playbook file is either an entry, a member of
  exactly one entry's `[[files]]`, or an exemption with a non-empty reason. `selfcheck` asserts it in
  both directions and reds on an exemption whose path no longer exists. The directory-scoped predicate
  it replaces left every single-file deployable the runbook already prescribes in no population at all.
- **S13** `[gate_runner]` in the target descriptor declares the target's OWN runner and CI: its kind,
  the command that runs it, the file `apply` edits, the grammar a leg is spelled in, the dedupe key
  that makes a re-run idempotent, and the CI system, workflow file and job. `history_depth` on a
  `[[gate_leg]]` is consumed by the CI emitter and renders as that system's full-history setting.
  `kind = "none"` is legal and emits an outbox order rather than skipping silently. Every `guard`
  pathspec is RENDERED against the target's install prefix and memory root before it is emitted, and a
  guard that would render to nothing is dropped with its leg left unguarded rather than emitted empty.

## 3. Non-goals (OUT)

- Upgrading or converging a repo that already carries kits. Owner-stated, and its own unit. This unit
  designs the receipt and descriptor so that unit is possible, and executes only the install path.
- Fleet fan-out across several targets, and `remove`. Both named in the 2026-07-12 research; both wait.
- The three-way living-document merge the research designs for upgrades.
- Migrating a target off the retired sharded session ledger. The descriptor carries it as a
  `[[migration]]` block the unattended path refuses outright rather than as installable steps.
- Deploying into this repo. The research's standing item calls gov fleet target zero on the grounds
  that it carries none of its own medicine; two thirds of that is now false — the manifest and the
  memory tree both exist and both are gated. Only the instantiated playbook is missing, which is one
  file, not a deployment.
- Declaring the install prefix. `TOOL-aSealedCaravan-1` owns that, and this unit consumes it.
- Assigning distinct exit codes to every adopter refusal branch. That would edit seven adopters whose
  refusals were each bought with a defect; section 4 solves the collision by probing effects instead.
- **Landing the install.** `apply` writes and stages; it never commits, branches, pushes or opens a
  pull request, and the operator lands. Measured 2026-08-11: no adopter under `tools/*/` runs
  `git commit`, `git push`, `git checkout -b` or `git switch -c`; three of the six stage their own
  writes; and `WIRE-INTO-PROJECT.md` has an agent working directly on the target's default branch
  rather than on a branch it opened. A deployer that pushes to somebody else's remote unattended is a
  write surface this unit does not price. If it is wanted it is a further unit, and it inherits
  `memory/guides/UNATTENDED-PROTOCOL.md` rather than inventing a second answer to the same question.
  Two failure-policy knobs die with this cut, on a diverged remote and on a push-scope failure, because
  neither state is reachable any more.
- **Shipping gov's own gate runner.** `tools/run-gates.sh`, `tools/gate-legs.json` and their two
  self-tests are exemptions rather than an entry. Measured: `WIRE-INTO-PROJECT.md` prescribes copying
  neither file anywhere, every one of its gate-runner instructions adds a leg to the runner the target
  already has, and the runner is not deployable as it stands — `run-gates.sh:15` sources
  `tools/lib/resolve-python.sh`, the one directory this unit declares permanently exempt, and the
  runner exits 2 with zero legs run when that path is absent. A target with no runner of its own gets
  an outbox order, per S13.
- **Repairing the defects this unit's grounding found in gov's own shipped files.** Four were measured
  and each is filed as its own backlog row instead of folded here: a kit-version marker that ships
  stale to every adopter, two false counts in a shipped companion, a runbook cross-reference to a
  section that does not exist, and rendered documents that are install-prefix-correct but not
  memory-root-correct. They bound what `check` can honestly claim about a target and section 4 names
  them for that reason, but repairing them is not this unit's diff.

## 4. Design

### Where it lives

`tools/govkit/`, not the `deploy/govkit.py` the research proposed. A repo-root directory sits outside
`check-review-join.sh:44`, which scopes to `^tools/.*\.js$`, and outside
`check-workflow-syntax.js:38`, which filters on `startsWith('tools/')`. It is outside every
codebase-map inventory, because `map_extractors._tool_kits()` enumerates `tools/*` and nothing else,
so a root directory is in no inventory and demands no dossier. And it is outside drift-audit's product
globs. `tools/govkit/` is inside all four, and is automatically a new `kits` inventory key that
demands a dossier. The unit whose thesis is that everything lives under one directory should not
except itself. Recorded as fork F1.

`check-arms.py` is NOT part of this argument. Its population is repo-wide — `check-arms.py:116` reads
every tracked path ending `.sh` — so a root-level shell script would be inside it, and `govkit.py`
is outside it either way because the scan is shell-only. That claim was wrong at rev-1 and is dropped
rather than repaired.

### Data model

Four files carry all state. Nothing is inferred from a directory listing.

**`tools/govkit/registry.toml`** — the kit population, tracked and asserted in both directions by
`selfcheck` over the tracked surface S12 defines. It exists because no directory listing equals the
deployable set, and the ways it fails to are not symmetric. Some `tools/*` directories are not
deployable: `tools/lib/` is a permanent exemption and the gate-runner cluster is a §3 non-goal. Some
entries are not `tools/*` directories at all: the playbook is root files, the manifest ratchet is
`skills/session-kickoff/manifest-check.sh` and lands renamed and flat, `settings-merge.py` is a single
file, and several single-file gates the runbook already prescribes for copy sit directly under
`tools/`. One directory carries TWO entries, because `tools/workflows/` versions its files under two
different kit ids, which a single `version_from` per descriptor cannot describe. And one entry has TWO
destinations for ONE source file, because the agent-cap parity arm requires both the kit copy and the
wired copy and fails outright if the wired copy is absent.

`map_extractors._tool_kits()`'s own docstring records why this must be a declaration rather than a
heuristic: README-gating "would have silently dropped three of ten".

**No count of that population is written in this document, deliberately.** Both counts earlier revs
stated were true when measured and false when read. The `tools/` directory count moved when the
unattended kit landed, and the playbook file count was wrong from the start because the customize
companion is explicitly not shipped — the runbook's own words are "read it, don't ship it".
`selfcheck` derives every count, section 6 gates the derivation, and a number in prose here is a
defect in this document.

`tools/lib/`'s exemption carries the longest reason, because it is the entry most likely to be misread
as dead. It has no README, no version constant and no adopter, and it is load-bearing inside gov:
`resolve-python.sh` is the canon every inline copy is gated against, a measured population of tracked
non-`memory/` files references it, and `tools/run-gates.sh:15` sources it — which is why §3 makes the
runner an exemption too rather than a deployable that would arrive broken. The `merge.rows.driver`
argument earlier revs gave for this exemption is now STALE and is dropped rather than repaired:
`TOOL-aSealedCaravan-1` S9 landed, and that config reads `bash tools/memory-tree/merge-rows.sh` today,
a kit-internal launcher. That same S9 is why nothing under `tools/lib/` ever needs to travel. The
registry states the surviving reason in the exemption itself rather than in a comment, so
`selfcheck`'s output is where a future reader meets it.

**`kit.toml`**, one per registry entry, beside the kit where the kit is a directory:

```toml
id = "memory-tree"
scope = "repo"                         # repo | machine — the kickoff engine is machine-scoped
version_from = { file = "check-memory-hygiene.sh", pattern = "^KIT_MEMORY_TREE_VERSION=" }
requires = []
# Spelled against keys that EXIST. `corpus_ids.py` arms checks 13-16 on any of these three pins and
# raises when the memory-recall sibling is absent. The edge is FALSE at apply time (pins ship blank)
# and becomes TRUE at discharge time, which is why `--resume` re-evaluates it.
requires_if = [{ kit = "memory-recall",
                 when_any_key_set = ["DEAD_PATH_PIN", "ORPHAN_ID_PIN", "READ_PATH_CEILING"],
                 why = "corpus_ids.py binds its id grammar to the memory-recall kit and raises when it is not installed" }]

[[files]]                              # precedence: later rules win, so exclusions are expressible
include = "**"
role = "engine"
to = "{prefix}/{kit_id}/{relpath}"     # the DEFAULT; every rule may override it
[[files]]
include = ["map_extractors.py", "drift_signals.py", "*.conf"]
role = "project-owned"                 # never copied FROM gov, never overwritten in the target
[[files]]
include = ["generated/**", "baseline.toml"]
role = "generated"                     # produced in the target, never carried across
[[files]]
include = ["HYGIENE.template.md"]
role = "rendered"                      # substituted, so it equals no gov blob — see the role enum
to = "{memory_root}/HYGIENE.md"
placeholders = ["KIT_DIR", "TOOL_ROOT"]
[[files]]
include = [".memory-tree.conf.example"]
role = "project-owned"
to = ".memory-tree.conf"               # repo ROOT, renamed, whatever the prefix

[config]
file = ".memory-tree.conf"
owner = "memory-tree"
# SPLIT BY CONSUMER. One list records the wrong answer for any kit whose renderer and whose gate leg
# require different keys, and at least one shipped kit is measurably in that state.
required_keys_gate = ["MEMORY_ROOT", "DISCIPLINES", "FAMILIES"]
required_keys_render = ["MEMORY_ROOT"]
optional_keys = ["SPEC_FORMAT_CUTOFF", "STREAMS_CUTOFF", "DEAD_PATH_EXCLUDE"]
defaults = { MEMORY_ROOT = "memory" }

[adopt]
argv = ["bash", "{kit}/adopt-memory-tree.sh", "--scaffold"]
mutates_index = true

[[outcome]]                            # code + PROBE, not code + meaning
code = 1
probe = { must_exist = ".memory-tree.conf", must_not_exist = "{memory_root}/HYGIENE.md" }
means = "seed-and-stop"
[[outcome]]
code = 1
probe = { must_exist = "{memory_root}/HYGIENE.md" }
means = "refused-foreign-tree"

[[gate_leg]]
name = "memory hygiene"
argv = ["bash", "{kit}/check-memory-hygiene.sh"]
guard = []                             # gate-legs.json carries three keys, not two
history_depth = "full"                 # consumed by the CI emitter; renders as full-history checkout
red_after_land = false                 # true = this leg is red between land and configure, by design

[[hole]]
id = "measured-pins"
kind = "measurement"
blocks_adopt = false                   # the adopter exits 0 with the pins blank
blocks_gate  = false                   # and the hygiene leg exits 0 too: checks 13-16 are simply OFF
why = "every pin is measured against the target corpus; an inherited number is vacuous or permanently red"
# NEITHER flag set means NOTHING in the target observes this hole, so the probe is the only evidence
# it exists. `selfcheck` refuses a hole in that state with no `discharge`.
discharge = { command = ["bash", "-c", "for k in ORPHAN_ID_PIN DEAD_PATH_PIN READ_PATH_CEILING; do grep -qE \"^${k}=\\\"[^\\\"]+\\\"\" .memory-tree.conf || exit 1; done; python {kit}/corpus_ids.py --check"] }
```

Nine fields exist because no earlier rev's model could express what the adopters actually do. Four
were argued into existence at rev-2; five more were forced by measurement at rev-6.

**`[[outcome]]` probes rather than declares.** The exit-code collision is per BRANCH, not per kit.
`adopt-codebase-map.sh` alone exits 1 for six unrelated outcomes — an identity refusal at `:52` with
nothing written, three prefix refusals explicitly before any write, a seeded conf at `:150`, seeded
extractors at `:184`, a `gen_map` crash at `:191` leaving a half-written map tree, and a failing gate
at `:212` with the conf, the map tree and the gate file all on disk. A code-to-meaning table cannot
tell those apart, and parsing stdout is fragile. So each outcome declares a filesystem probe the
deployer RUNS. The classification is measured, which is the rule `adopt-codebase-map.sh:137` already
states: claim nothing until it is read back.

A probe reads INPUTS as well as outputs, and rev-2's prose describing probes as reading what the
adopter WROTE was too narrow. Measured on the unattended adopter: of its distinct outcomes, only one
pair is separable by output state at all. Two exit-1 branches are both "nothing written", and three
exit-2 branches are all "nothing written" — they are told apart only by what the operator supplied,
which is the template file, the project conf, the `.git` directory and the shape of the kit prefix
string. `must_exist` and `must_not_exist` already express that; what needed correcting was the claim
about where a probe is allowed to look.

**`[[files]]` has precedence.** A bare whole-kit engine glob would copy gov's own filled
`map_extractors.py`, its measured pins and its generated inventories into the target — the
inherited-vacuous-numbers failure the memory-tree adopter warns about in its own closing output.
Later rules win, so `role = "project-owned"` and `role = "generated"` carve out of the engine glob.

**`requires_if` is conditional, and its condition names real keys.** memory-recall depends on
memory-tree unconditionally, and drift-audit does too, both enforced in code by a refuse-never-create.
The reverse edge is different: memory-tree needs memory-recall only when the corpus-id checks are
armed. Rev-2 spelled that condition as a key that does not exist anywhere in the tree, which made
AC9's "names the missing key" have no key to name and `selfcheck` no key to resolve. Measured: the
arming predicate is any of `DEAD_PATH_PIN`, `ORPHAN_ID_PIN` or `READ_PATH_CEILING` being non-blank, and
the raise fires when the memory-recall sibling's extractor is absent. `when_any_key_set` spells it
against those three.

The edge has an ORDERING consequence rev-2 could not have seen, because it follows from the hole
model: the pins ship blank, so the condition is FALSE during `apply` and becomes TRUE the moment the
`measured-pins` hole is discharged. Measured in a fixture — setting a pin in a target without
memory-recall turns a green hygiene leg red. So `apply --resume` re-evaluates every conditional edge
after a discharge, and a discharge that would newly require an unselected kit writes an outbox order
rather than proceeding.

**`scope` separates repo from machine, and names the action.** The kickoff engine installs once per
machine as a junction or symlink outside the target repo entirely, not per repo. Rev-2 justified the
class only by naming two behaviours `apply` must NOT have and never said what it does have, which
leaves the one field that reaches outside the operator's repository undefined. It is defined here:
`apply` NEVER writes a machine-scoped file. It emits an outbox order carrying the junction command for
the operator's platform, and `check` reports a machine-scoped entry as undischargeable from inside the
repo rather than as missing. That keeps §5's "the deployer writes into a repository the operator
names" true without exception, and it excludes machine-scoped entries from AC1's "lands AND
configures", which has no meaning for them.

**`to` gives every file rule a destination.** Rev-2's `[[files]]` carried `include` and `role` only,
so every byte landed at the kit-relative default and four registry entries could not be written at
all. Measured destinations that the default cannot express: the manifest ratchet lands renamed and
flat outside its source tree, the agent-cap hook lands at a Claude Code path outside any kit prefix
AND a second time inside one, `settings-merge.py` is flat, the playbook lands at an owner-chosen path
with its domain-rules companion required to be a sibling, two conf examples land at the repo root
renamed, and the pre-push hook lands at a verbatim repo-root path with no prefix. `to` defaults to
the kit-relative form, so the common case stays silent; `flat = true` is the shorthand for an entry
with no kit directory, and `link = true` marks a machine-scoped entry whose order is a junction rather
than a copy.

**The role enum grew, because three shapes had no slot.** `engine`, `project-owned` and `generated`
could not classify a file gov RENDERS, a file gov contributes a BLOCK to, or a file gov seeds once and
the target then owns.

| role | receipt row | re-apply | measured reason it exists |
|---|---|---|---|
| `engine` | sha256 + source commit | overwritten | the base case |
| `project-owned` | sha256 at install, then never compared | never rewritten | the target edits it |
| `generated` | path only | never carried across | produced in the target |
| `rendered` | template path, substitution inputs, output sha256 | re-rendered and compared | a substituted file equals no gov blob, so AC3's byte-equality is false for it |
| `merged` | anchor pair and the sha256 of the BLOCK ONLY | the block is replaced, the rest untouched | the target owns the file and gov owns a region of it |
| `seed` | sha256 at install, then never compared | never rewritten | copied from gov once, then owned — the version gate copied verbatim reds immediately, and its own runbook step is "edit its list to your kit subset" |

**`[config]` splits its required keys by consumer.** A single `required_keys` list records the wrong
answer for any kit whose renderer and whose gate leg disagree, and one shipped kit is measurably in
that state: removing one key leaves its gate leg green and its own render-parity check red, on the
same tree. AC9's refusal must name which consumer wanted the missing key, or the operator is told a
key is required by something that does not require it.

**`[[hole]]` carries a probe, and declares what observes it.** This is the field rev-2 left asserted
rather than measured, and it is the one that gates `--resume` and reds `check`. Every hole now carries
a `discharge` probe in `[[outcome]]`'s shape, extended with a `command` form because most measured
probes are commands rather than file predicates. Two probes were MEASURED going false-green in their
first, narrower form: a placeholder grep over only the main playbook file passes while its companion
sits unfilled, and a non-empty test over drift-audit's product globs passes on a glob matching no
tracked file — which does not make its oracle vacuous but makes it FALSE-POSITIVE, reporting a finding
that is not there. A probe this spec has not observed failing is not a probe, and `selfcheck` refuses
a hole with no `discharge`.

The observation flags are `blocks_adopt`, `blocks_gate`, and neither. Rev-2 had only the first, which
covers exactly one measured hole. The distribution matters more than the names: of the holes measured
across the shipped kits, one blocks its adopter, several red or absent a gate leg, and the LARGEST
group is observed by nothing at all — the adopter exits 0 and every leg the kit ships exits 0 with the
hole wide open. `selfcheck` refuses a hole with neither flag and no probe, because in that state the
probe is the only evidence the hole exists.

**`red_after_land` separates two states rev-2 conflated.** `blocks_adopt` models a kit whose ADOPTER
fails, which stops the configure phase. A different and commoner state is a kit that lands, configures
cleanly, and whose gate legs are simply red until the configure phase has run — measured on the
unattended kit, where both unguarded legs are red after land and green after adopt. Marking that with
`blocks_adopt` would falsely stop the configure phase; leaving it unmarked makes AC1 unsatisfiable.
The flag exists so a leg's red window is declared rather than discovered.

**`.governance/deploy.toml`** in the target: `gov_source`, `prefix`, the selected kit ids, one table
per kit holding its config answers, the `[gate_runner]` declaration S13 defines, and the failure-policy
knobs. There are TWO knobs, not four. Rev-2 listed four, of which two — on a diverged remote and on a
push-scope failure — described states only a deployer that pushes can reach, and §3 says this one does
not. Each surviving knob has a key, a value vocabulary and a default:

| key | values | default | what it governs |
|---|---|---|---|
| `on_baseline_red` | `proceed` · `refuse` | `proceed` | a target gate leg already red before the install |
| `on_hook_block` | `report` · `refuse` | `report` | a target hook that would refuse a commit |

`on_hook_block`'s default is `report` for a measured reason rather than a cautious one: `apply` never
commits, so no pre-commit hook fires during an install, and the knob exists only so a target whose
hooks WILL refuse the operator's own landing commit is told before it discovers that by hand. AC15's
hook-block fixture arm observes exactly that — the install completes, the receipt is written, and the
outbox carries the warning — instead of asserting whatever the code happens to print.

```toml
[gate_runner]
kind = "manifest"        # manifest | make | npm | shell | none
command = "..."          # what `check` runs to prove a wired leg EXECUTES
file = "..."             # the file `apply` edits; required unless kind = "none"
grammar = "json-array"   # how a leg is spelled in `file`
anchor = "govkit:legs"   # begin/end pair for line grammars; ignored for structural ones
dedupe_key = "name"      # what makes a re-run idempotent — the runbook's grep-guard, mechanised

[gate_runner.ci]
system = "github-actions"   # the only CI grammar this repo has ever measured
file = "..."
job = "..."
full_history = true         # emitted for any leg whose descriptor says history_depth = "full"
```

`kind = "none"` writes an outbox order naming the legs, never a silent skip. `command` defaults to the
target's already-declared gate command where one exists: a repo carrying the unattended kit has
committed exactly that string in its own project layer, and reading it beats asking for it twice.
`full_history` is `history_depth`'s only consumer, which rev-2 left with none — the runbook makes it
mandatory rather than advisory, because a shallow CI checkout makes the ratchet's drift check
WARN-and-skip on every run and the deployed leg is then vacuously green.

The effect is observable rather than inferred: gov's own runner prints one status line per leg, so
"the leg executed" is a string in the runner's output, and AC17 asserts it there.

It lives in the TARGET rather than in gov, per fork F2. That location is what makes a committed
descriptor a standing authorization an unattended re-run can read from a fresh clone. A gov-side
descriptor is absent from that clone, so the re-run would have nothing to read, and S3's claim would
be false. The cost is a disclosure: the target carries a file naming its gov source. The operator
owns that repository and named it, so the disclosure is theirs to make, but it is real and it is
stated here rather than discovered. A redaction knob is a follow-up, not this unit.

The pre-existing-red knob has a decided default, per fork F4, and rev-6 corrects what it baselines.
Rev-5 said "every selected kit's gate legs", which is empty by construction: AC8 guarantees the target
carries no kit, so those legs do not exist yet and the rule could never fire. The baseline is over the
TARGET's own gate runner, which is the only leg population that exists before the install.

The verdict is three-valued, because two values cannot express a leg that is not there:

| verdict | meaning | what `apply` does |
|---|---|---|
| `green` | the leg ran and passed before the install | a red one after fails the install, naming the leg |
| `red` | the leg ran and failed before the install | reported, does not fail the install — `on_baseline_red` |
| `absent` | the leg did not exist before the install | expected to become green; red after fails, UNLESS a hole declares `blocks_gate` or its leg declares `red_after_land` |

Reading `absent` as `green` would fail every install that legitimately leaves a leg red by design,
including the two the inventory now marks that way. Reading it as `red` would mean no newly installed
leg can ever fail the install, which is most of them. Naming the third state is the only reading that
is not one of those two mistakes. The baseline step is a write-free step and appears in S5's hard
order and in AC4's log assertion, which rev-2's ordering started too late to include.

**`.governance/install.json`** — the receipt, tool-written only, plus the flat `install.sums` sidecar.
The apply layer has no code path that writes a file whose role is `project-owned`. A `merged` row
carries the sha256 of its BLOCK rather than of its file, and a `rendered` row carries its template
path, its substitution inputs and its output sha256 rather than a source commit — both because the
alternative is a receipt that claims something false about bytes it did not fully write.

One receipt row exists that is nobody's file: merging into a target's settings writes a `.bak`
sidecar, and `plan` must list it or the file set `apply` produces is not the file set `plan` promised.

### Guards, and why a deployed one is green by absence

A `[[gate_leg]]`'s `guard` is a list of pathspecs, and a leg whose guarded paths did not change is
skipped. Gov's own guards are gov-layout literals, so emitting them verbatim into a target hands it
legs that can never fire. The failure is silent in the worst direction: a skipped leg prints a
reassuring line and the bar reports GREEN.

This was reproduced in the real runner rather than argued. Driving `tools/run-gates.sh` in a throwaway
repo with a three-leg manifest whose second and third legs exit 1, and whose guards name paths that do
not exist, the runner skipped both failing legs and reported GREEN at exit 0. The underlying primitive
is that `git diff --quiet <BASE> -- <path-that-does-not-exist>` exits 0, meaning no difference.

Guards are therefore RENDERED, and three classes of pathspec exist:

| class | rendering | measured population |
|---|---|---|
| kit-relative | to the target's install prefix | the largest class |
| memory-root-relative | to the target's memory root | a handful, and one of them is a literal that is wrong the moment a target renames its memory root |
| gov-layout only | DROPPED — the path cannot exist in a target | the hooks directory, the kickoff engine's own tree, and `tools/lib/` |

`tools/lib/` alone accounts for most guard occurrences in gov's manifest, and it is the directory this
unit declares permanently exempt. Emitting it would also red the target's own run-gates canary, which
refuses a guard matching no tracked path — so the same value is both a silent skip and a loud failure
depending on which gates the target took.

A leg whose guard set renders to nothing is emitted UNGUARDED rather than emitted empty. That costs an
unnecessary run and never a silent skip, which is the correct direction to fail. The empty-prefix edge
fails safe for the same reason and by accident: an empty pathspec makes the diff command error rather
than report no-difference, so the leg runs.

### The merged files

Three target-owned files receive a gov-written region, and each needs a different anchor because each
has a different comment grammar. Reuse rather than invention: this repo already ships an anchored-region
writer with exactly the right refusal semantics — one open marker, one close, close after open, replace
by line index, raise rather than guess — and it is already gated. The descriptor names a `marker_style`
because there are three grammars, and a hash-comment anchor was measured legal and non-interfering
inside a git attributes file.

The settings file is structural rather than textual, because JSON carries no comment: its anchor is the
hook entry keyed by a marker substring, which is the mechanism the existing merge tool already uses and
proves idempotent. One consequence must be stated rather than discovered: that merge re-serializes the
whole document, so the FIRST apply reformats bytes the target owns and gov never wrote. The receipt
records that as an accepted reformat. Without that line, AC2's second run still passes while any
reasoning about that file's bytes is wrong.

The markdown pointer is the cheap case and needed no new machinery at all: its existing detector already
matches a LINE rather than the whole file, so the merged behaviour is "append the import line if no line
matches", and a target file carrying its own prose plus that line is already reported in sync.

The first file in S5's hard order is the one with no implementation anywhere in this repo. Nothing
currently writes a git attributes block and nothing performs the renormalize that follows it — measured,
by grepping every adopter. So S5's first step and AC4's second clause are new code with no seam to
extend, and §10 records that rather than implying a reuse that does not exist.

### The limits this deployer cannot verify away

Four defects in gov's own shipped files were measured while grounding this rev. Each is a §3 non-goal to
repair and each bounds what `check` may claim, so they are named here rather than left for the next
reader to rediscover:

- A kit-version marker in one shipped template disagrees with its kit's constant, and the pairing gate
  asserts a different file. The stale marker is rendered into every adopter's tree, so a receipt
  recording "the version the kit declared" records a number the kit does not agree with itself about.
- A shipped companion states that its placeholder set is disjoint from the main file's and gives a count
  one lower than the measured one. Both are false, and the discharge probe for that hole must name both
  files precisely because of it.
- The runbook cross-references a section that does not exist, for the one selectable kit that also has
  no version constant and no runbook section.
- The rendered rule-set documents are install-prefix-correct and NOT memory-root-correct: a target that
  renames its memory root receives documents still naming the default. A `rendered` role that records
  "the substitution inputs" would faithfully record a substitution that did not happen. `check` must
  therefore compare a render against a fresh render, never assert that a render is CORRECT.

The general form is the one this unit exists to attack: two spellings of one fact with nothing asserting
they agree. A cross-check between the registry's version data and the version gate's own list is in
scope and is AC10's; repairing the disagreements it finds is not.

### Inventory: what the deployer must know per kit

Measured by running the adopters end to end in throwaway repos. Rows marked UNVERIFIED were not
exercised and say so, because an inventory that cannot tell "measured none" from "did not look" is the
same vacuous claim this unit exists to attack.

| Kit | Selected by | Config | Holes | What observes an open hole |
|---|---|---|---|---|
| playbook | default | none | placeholders, across BOTH deployed files | nothing — no leg in a target reads the playbook |
| kickoff manifest | default | none | manifest section B | its **gate leg**: red unfilled, and exit-2 with no manifest at all |
| memory-tree | default | owns `.memory-tree.conf` | taxonomy, measured pins | nothing — adopter and hygiene leg both exit 0 |
| codebase-map | default | owns `.codebase-map.conf` | `map_extractors.py` | its **adopter**, which fails; and the leg file is never installed, so that leg is ABSENT rather than red |
| memory-recall | default | reads `.memory-tree.conf` | none | — |
| drift-audit | `--all` | reads `.memory-tree.conf` | product globs, measured pins | its **gate leg**, which reds with a WRONG finding rather than a missing one |
| unattended | `--all` | owns `.unattended.conf` | keepalive tool names, lander and bar commands, core floor, kickoff pins | mixed, and partly nothing — see below |
| agent-instructions | `--all` | none | none UNVERIFIED | — |
| agent-cap | `--all` | none | none UNVERIFIED | — |
| review harness | `--all` | none | none UNVERIFIED | — |
| gate-lint | `--all` | none | leg wiring is the adopter's UNVERIFIED | — |
| pytest guardrails | `--all` | none | ini knobs | nothing — its leg grades the SHIPPED snippet, never the target's ini |
| the single-file gates | `--all` or conditional | none | the version gate's own list | its **gate leg**: copied verbatim it reds immediately |

Rev-2 said the default set declares four holes, exactly one of which blocks. That is still true and it
was still misleading, because `blocks_adopt` was the only observation the model had. Measured across
every kit above, the LARGEST class of hole is observed by nothing at all — the adopter exits 0, every
leg the kit ships exits 0, and the hole is wide open. Two of the default set's own holes are in that
class. A model whose only flag is `blocks_adopt` describes the rarest case and stays silent about the
common one, which is why rev-6 replaces the Blocking column with this one.

The unattended row is the sharpest instance and earns its own sentences. A key ABSENT from its conf
reds two legs, so that shape is `blocks_gate`. But the shipped conf example copied verbatim — which is
exactly what an operator in a hurry does — renders its angle-bracket placeholder text into the Skill as
literal prose, and the adopter, its own check arm and the kit's gate leg all exit 0 over a document
instructing an agent to invoke a placeholder as if it were a tool. The placeholder detector greps for
the brace shape only. A lander naming a script that does not exist is silent the same way. This is the
failure class the manifest ratchet's first check exists to catch, reproduced one shape sideways, and it
is the strongest argument in this document for probes over flags.

### The blocking hole, and why apply has two phases

An unfilled `map_extractors.py` does not defer, it fails. `map_extractors.template.py` raises on an
empty extractor dict at its `inventory_ids` guard, and `gen_map.py` calls `inventory_ids()` at module
level, so `adopt-codebase-map.sh` exits 1 with no map tree, no baseline and no gate file. The installed
gate cannot even import, because the gate template binds the same call at module scope. codebase-map is
in the default set, so a single-phase `apply` of the default set can never reach a green fixture.
Reproduced three runs deep, and one precision the earlier revs got wrong: a fresh target hits an EARLIER
exit first, where the adopter seeds the extractors file from its template and stops. The crash is the
SECOND run, not the first.

A second precision changes what AC5 may assert. Because the adopter never reaches its copy step, the
gate file is never installed at all — so that leg is **ABSENT, not red**. A runner that skips a missing
leg would score this state green, which is the same green-by-absence this document warns about two
subsections earlier. AC5 asserts absent-or-red and never red alone.

Hence S5's split and S8's `blocks_adopt`. The land phase copies codebase-map's files and writes the
work order; the configure phase skips it; `check` reports it landed-but-inert; and
`govkit apply --resume` runs its adopter once `map_extractors.py` is filled. The codebase-map adopter
remains the model for everything else — it is the only one that verifies its own effect by running
the gate it just installed — but it is not the model for the unattended path, which rev-1 claimed.

**It is not the only kit whose leg cannot be green after a default-set install**, which is the
correction rev-6 owes AC1. The kickoff-manifest kit ships no adopter at all: installation is a copy,
so `blocks_adopt` is structurally inapplicable to it. Measured on a fresh install of it, the ratchet
exits 1 on the copied-and-unfilled template, failing its placeholder check and its stamp check
together — and exits 2, an environment error, when no manifest is scaffolded at all. There is no
install of that kit which leaves its leg at exit 0 without an authoring step. AC1's "each of their gate
legs exits 0" therefore had no satisfying assignment for a kit in its own default set, and `blocks_gate`
is the flag that lets the criterion be stated truthfully instead of loosened.

The discharge probe for that hole is the whole check rather than its placeholder grep, and that choice
was forced by measurement too: filling every placeholder and stamping the audit line with a well-formed
but foreign sha passes the grep and still reds the leg on a later check. A grep-shaped probe would
discharge the hole while the leg stayed red, which is the "operator deleted the order file" failure in
a new place.

The inverse failure is drift-audit's, and it is worse than rev-2 described. Its own adopter check passes
on an unfilled signals file because it tests existence only, and memory-recall's likewise exits 0 as a
skip when nothing was rendered — that much rev-2 had right. What it missed is the shape of the damage:
the product globs ship EMPTY, and the oracle then runs its search with no pathspec, so it searches the
whole repository and every specification matches its own identifier. Measured, same tree, same spec:
empty globs report a violation OVER PIN; one correct glob reports none. An unfilled hole there does not
silence the signal, it INVENTS one. And the obvious repair is not enough on its own — a glob that is
non-empty but matches no tracked file passes a non-empty test and silences the oracle for real, so the
probe asserts both.

Exit 0 from an adopter means "the adopter ran", never "the kit works", so `apply` records the hole and
`check` reports the target incompletely adopted regardless of adopter status.

### The bash-from-Python trap

`govkit.py` shells out to bash adopters, and on a Windows node `subprocess` resolving the bare name
`bash` finds the System32 WSL launcher before git-bash. WSL then sees a different filesystem: an
existing path reports no such file, and a relative path resolves under a mount prefix. The remedy
already exists and is not to be rewritten — `resolve_bash()` in `tools/memory-tree/corpus_ids.py:120`
names the executable, accepts a candidate only if it RUNS, and treats a set-but-unusable `GOV_BASH` as
a named failure rather than a fall-through.

### Rollout

Four commits, each independently valuable and independently green:

1. `registry.toml`, a `kit.toml` for every entry, and `selfcheck` — including the surface predicate
   S12 defines and the version cross-check against the repo's existing version gate. No deployer
   behaviour; immediate value as a machine-readable kit inventory, and immediate value as the ratchet
   that stops this spec's population claims going stale a third time. Unblocked: F5 is resolved.
2. `plan` and `check`, both read-only. Zero write risk, and `check` is usable against an
   already-adopted target on day one.
3. `apply`, `apply --resume` and the receipt, plus the acceptance matrix.
4. `intake`, the Skill, the runbook demotion and the parity gate.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` and modules | the bulk |
| Registry, descriptors | one registry, one descriptor per entry | the entry count is DERIVED by `selfcheck` over the tracked surface, and is deliberately not written here — every earlier estimate was measured over `tools/*` directories and was wrong for that reason |
| Tests | `tools/govkit/selftest.py`, `tools/govkit/acceptance.test.sh` | the matrix |
| Skill | `skills/deploy-governance/SKILL.md` | the agent entrypoint |
| Gates | `tools/gate-legs.json`, the parity gate | three new legs |
| Map | `memory/map/features/govkit.md` | new `kits` key demands a dossier |
| Charter | `AGENTS.md` | gate-suite citation for all three legs, zero slack on the pin |

### Alternatives rejected

**A bash orchestrator over the existing adopters.** Cheaper and more house-native, and Phase 0 already
closed the idempotency objection the 2026-07-12 judges raised against it. Rejected on the owner's
call to resurface govkit with a widenable scope: the receipt, the plan and the eventual upgrade path
all want a data model.

**Reimplementing each adopter's logic inside `govkit.py`.** Rejected. The adopters carry refusals that
were each bought with a defect — the codebase-map adopter alone was the one changed file no gate leg
executed, and a Tier-2 review found four of seven defects in it including a blocker that wrote into a
repository the operator never named. `govkit` drives them; it does not replace them.

**Giving every adopter refusal branch its own exit code.** Would make classification trivial, and is
rejected because it edits seven adopters to serve one consumer. The probe model gets the same
information without touching them.

**A `deploy/` directory at the repo root.** Rejected on measurement, see the location subsection.

## 5. Production-readiness checklist

- security — the deployer writes into a repository the operator names, and into no other. The identity
  guard the codebase-map adopter already carries is the model: refuse before writing when the resolved
  target is not the tree the operator named. No credentials are handled, and no remote is contacted:
  §3 puts committing, branching, pushing and pull requests out of scope, so the operator lands. The one
  path that reaches outside the named repository is a machine-scoped entry, and §4 resolves that by
  emitting an order rather than writing.
- perf / scale — a single-target install; the cost is the adopters', not the orchestrator's.
- a11y — N/A: a command-line tool with no interface beyond stdout.
- i18n — N/A: developer tooling, English only.
- error / empty / loading states — "exit 0 from an adopter is not installation proof" is this line,
  and the three-state `check` is its implementation.
- observability — the receipt is the observability surface, and `check` is its reader.
- risks — a half-applied install is the main one, and §3's cut changes how it is bounded. `apply` never
  commits, so a crash leaves a working tree and an index the operator can inspect and discard, rather
  than an abandoned branch. What bounds it is the receipt: every path `apply` wrote is named there, so
  a half-applied install is enumerable rather than guessed at, and S5's ordering makes the enumeration
  meaningful. Receipt provenance is the second risk: bytes must be provably from the recorded commit,
  not from a dirty working tree. The third is the one §4's limits subsection names — the deployer can
  prove a render matches a fresh render and cannot prove a render is correct.
- testing + left-shift gates — the acceptance matrix is the deliverable's own gate; fixtures reuse
  the existing prefix-parameterized fixture builder. Every refusal branch is bound to a matrix arm by
  AC16, which is fork F3's resolution made mechanical, and every refusal also needs a negative arm
  proving it does NOT fire on the authorized path.
- migration / rollback — no migration, by non-goal. Rollback of a fresh install is bounded by the
  receipt: unstage and remove exactly the paths it names. That is a stronger claim than deleting a
  branch, and it is the claim §3's cut leaves available.
- user docs — the Skill plus the demoted runbook.

## 6. Acceptance criteria

- **AC1** When `apply` runs unattended against a fixture repo with no kit and a committed target
  descriptor, every selected repo-scoped kit with no `blocks_adopt` hole lands AND configures, and every
  gate leg of a kit with no undischarged `blocks_gate` hole and no `red_after_land` flag exits 0 in that
  fixture. Machine-scoped entries are excluded — §4 gives them an order, not an install, so "lands and
  configures" has no meaning for them. The kit-by-kit exclusions are DERIVED from the descriptors, never
  listed in this criterion: rev-2 named codebase-map by hand and the criterion was then unsatisfiable
  for the kickoff-manifest kit, which nobody noticed because nothing derived the list.
- **AC2** When that `apply` runs a second time, no path in the receipt changes content hash and no
  path is added or removed. The predicate is path-and-hash over the receipt, not `git status
  --porcelain`, because the adopters stage their own writes and a porcelain-empty tree would be
  satisfied by an install that did nothing. Runs on POSIX and Git-Bash.
- **AC3** When `apply` runs from a gov checkout whose working tree is deliberately dirty, every file
  named in the receipt whose role is `engine` has bytes equal to `git show <recorded_commit>:<path>`.
  This is the receipt's provenance claim and nothing else observes it. The role scope is load-bearing
  rather than cautious: a `rendered` file's bytes equal no gov blob by construction, a `merged` file's
  bytes are mostly the target's, and a `generated` file was never carried across — so an unscoped
  quantifier makes this criterion false on every install that succeeds. AC21 and AC22 carry the other
  two roles' provenance claims in the only forms that can be true of them.
- **AC4** When `apply` runs, its log shows the baseline read strictly before any write, the
  `.gitattributes` write and the renormalize strictly before the first kit-content write, the `git add`
  of everything written before any gate leg runs, and the target's gate-runner and CI wiring strictly
  last.
- **AC5** When the default set is applied, codebase-map is landed-but-inert: its files are present,
  its adopter did not run, `check` reports it in the inert state, and its gate leg is **absent or red**
  by design. Absent-or-red rather than red: measured, the adopter never reaches its copy step, so the
  gate file is never installed — and a runner that skips a leg it cannot find would score the red state
  green. After a fixture `map_extractors.py` is filled and `govkit apply --resume` runs, the adopter
  completes and the leg exits 0.
- **AC6** When the default set is applied, the outbox holds exactly one order per `[[hole]]` declared
  by a selected kit, at `<target>/.governance/outbox/<hole-id>.md`, and `check` exits non-zero until
  each is discharged. `check` decides discharge by RUNNING that hole's `discharge` probe, never by the
  order file's presence — deleting the order must not turn `check` green, because "the operator deleted
  the file" is not evidence about the artifact. The criterion asserts the id set, never a literal count.
- **AC7** When a file whose receipt role is `project-owned` is modified in the target and `apply` is
  re-run, that file is not rewritten, and `check` reports it as project-owned rather than as drift.
- **AC8** When `apply` is pointed at a repo that already carries a FOREIGN kit, it refuses before
  writing, naming which kit resolved and at which prefix. Detection predicate: a registry entry's
  version constant resolves in the target at either the canonical or the root prefix, AND this
  target's own `.governance/install.json` does not claim that entry. A re-run over govkit's own
  receipt PROCEEDS — that is the authorized path, and rev-2's unqualified predicate refused it, which
  left AC2, AC5, AC7 and S3 with no satisfying assignment at all after the first successful install.
  For an entry with no version constant the predicate falls back to a declared sentinel path, because
  a constant-less kit is otherwise invisible to the first disjunct, and measurement found several.
- **AC9** When `apply --unattended` is given a descriptor missing an answer the selected kits require,
  it refuses before writing anything, names the missing key AND names the consumer that requires it.
  The consumer half is not decoration: at least one shipped kit has a key its renderer requires and
  its gate leg does not, so "required" without an owner is a claim the operator cannot check.
- **AC10** When `govkit.py selfcheck` runs in this repo it asserts, and reds naming the offender: every
  `registry.toml` entry has a descriptor; every descriptor's declared files exist; every declared gate
  leg appears in `tools/gate-legs.json` with a guard that renders to gov's own guard under the identity
  substitution; every `version_from` pattern matches exactly one line in its named file, or carries an
  explicit `none` with a reason; every registry version claim agrees with the repo's existing kit-version
  gate in BOTH directions; every `[[hole]]` carries a `discharge` probe whose interpolation tokens
  resolve against that kit's config keys or the target descriptor's answer set; every hole with neither
  observation flag carries a probe; `--all` selects exactly the non-exempt, non-conditional entries; and
  the S12 surface predicate holds in both directions, reddening on an exemption whose path no longer
  exists. No count in this spec is an input to any of those — each is derived.
- **AC11** When `plan` runs against a fixture, it lists every file it would write with its role and
  source commit, including side-effect files an adopter or a merge produces, and writes nothing;
  running `apply` then produces exactly that file set, with no path added and none missing.
- **AC12** When `intake` runs non-interactively with a prepared answer stream, it writes a
  `deploy.toml` that `apply --unattended` accepts with no further prompting.
- **AC13** When `govkit.py` runs on a Windows node with WSL on PATH, it resolves git-bash and the
  adopters execute; with `GOV_BASH` set to something unusable it fails naming that override rather
  than falling through.
- **AC14** When the runbook and the descriptors disagree — a descriptor step with no runbook section,
  or the reverse — the parity gate reds naming both sides.
- **AC15** When the acceptance matrix runs, it covers at minimum a fresh empty repo, a non-Python repo,
  a repo whose pre-commit hook blocks, and a repo carrying a pre-existing red gate leg of its own; each
  arm asserts a specific message or on-disk effect, never an exit code alone, and each arm's expected
  outcome is stated in this spec rather than read off the implementation. The hook-block arm asserts
  that the install COMPLETES and the outbox carries a warning, because §3 means no commit happens
  during an install and therefore no pre-commit hook fires — an arm with no stated expectation is a
  test written after the fact against itself. The pre-existing-red arm asserts the three-valued
  baseline: a target leg red before is reported and does not fail the install, and a target leg green
  before and red after does fail it, naming the leg.
- **AC16** When `govkit.py selfcheck` runs, every refusal message in `govkit.py` is asserted by name
  somewhere in the acceptance matrix, and a refusal branch whose message no arm asserts reds naming
  that branch. This is fork F3's resolution made mechanical. `check-arms.py` scans tracked `*.sh` and
  is deliberately not extended here, so without this criterion the strongest new write path in the
  repo would also be its least armed. Every refusal additionally carries a NEGATIVE arm proving it does
  not fire on the authorized path — a guard that always fires and a guard that never can are the same
  defect wearing opposite signs, and AC8 shipped the first of those for four revisions.
- **AC17** When `apply` has wired a leg into a fixture's own gate runner and that runner is then run,
  the new leg's name appears in its output as an executed leg. Existence in a config file is not
  execution: a wired leg that never runs is the deployed-leg-vacuously-green failure §7 names, and this
  is the only criterion that observes the last step of S5's hard order having any effect at all. A
  shallow-checkout arm asserts that a leg declaring `history_depth = "full"` either reds or names its
  own degradation, rather than passing.
- **AC18** When one `engine`-roled file in an installed fixture is modified, `check` exits non-zero
  naming the path and the hash it expected. This is the receipt-integrity arm, and nothing else
  observes it.
- **AC19** When an installed fixture's receipt is pointed at a commit whose bytes differ, `check` exits
  non-zero naming that file and both commits. This is the provenance arm at CHECK time; AC3 proves
  provenance at APPLY time, which is the harness observing rather than the product.
- **AC20** When a kit whose adopter ships a `--check` arm is broken in an installed fixture — by
  editing its rendered artifact — `check` surfaces that adopter's own refusal rather than reporting the
  target clean. `check` cannot be a thin fan-out over adopter check arms, because two shipped kits have
  none, but where one exists it must be consulted.
- **AC21** When a `rendered` file is re-rendered from the inputs the receipt recorded, the output is
  byte-identical to what is installed. `check` asserts equality against a fresh render and never
  asserts that the render is CORRECT — measured, the memory-tree renders are install-prefix-correct and
  not memory-root-correct, so a criterion claiming correctness would be false on a target that renamed
  its memory root.
- **AC22** When a `merged` file is edited by the target OUTSIDE the gov-written block, `check` reports
  no drift and a re-run of `apply` leaves that edit intact; when the block itself is edited, `check`
  reports drift naming the block. The receipt hashes the block, never the file. For the structural
  merge into the settings file, the first `apply` is additionally allowed to reformat bytes the target
  owns, and the receipt records that reformat as accepted — without which AC2 passes while every
  statement about that file's bytes is wrong.
- **AC23** When `--all` runs, the selected set equals exactly the registry's non-exempt,
  non-conditional entries, with no hand-kept list anywhere in the code or the descriptors. When a
  non-default `--kits` selection runs, the outbox holds exactly that selection's hole ids and no
  others, and a conditional `requires_if` edge that the selection leaves unsatisfied is refused by name
  rather than silently dropped.
- **AC24** When a gate leg is emitted into a target, every guard pathspec has been rendered against
  that target's install prefix and memory root, no emitted guard names a path that cannot exist there,
  and a leg whose guard set renders to nothing is emitted UNGUARDED. A fixture arm proves the failure
  this prevents: a leg guarded on an absent path is skipped by a runner that then reports green.
- **AC25** When a machine-scoped entry is selected, `apply` writes nothing for it, the outbox carries
  an order with the platform-appropriate link command, and `check` reports it as undischargeable from
  inside the repository rather than as missing or as drift.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary. Three new legs: `govkit selfcheck`, the
acceptance matrix, and the runbook parity gate. Each addition trips the same four gates named in
`TOOL-aSealedCaravan-1` section 7 — codebase-map coverage, codebase-map freshness, the manifest
ratchet, and drift-audit's handkept charter citation, which has zero slack.

Two obligations are specific to this unit. `tools/govkit/` is a new `kits` inventory key, so it needs
a dossier at `memory/map/features/govkit.md` before the coverage gate goes green. And
`check-kit-versions.sh` is a hardcoded list of `need` calls rather than an enumeration, so govkit's
own version constant must be added to it explicitly or nothing gates it.

That second obligation is also where this unit could create the very defect it is built to detect. The
registry's `version_from` data and that gate's `need` list are two spellings of one fact. AC10 requires
`selfcheck` to cross-check them in BOTH directions rather than letting them drift, and grounding this
rev already measured disagreements in both — constants and marker pairs the gate does not assert, and
entries the registry must describe that the gate has no call for. `selfcheck` reports them; §3 says
repairing them is not this unit's diff.

A deployed `[[gate_leg]]` carries `history_depth`, because a leg wired into a target's CI with the
`actions/checkout` default depth makes the manifest drift check WARN-and-skip on every run — the
runbook already calls `fetch-depth: 0` mandatory rather than advisory, and the descriptor must carry
that or the deployed leg is vacuously green.

Before review: `python tools/memory-tree/gotchas.py --for-diff 16aeb5ef..HEAD`.

## 8. Open questions

none — every fork below is RESOLVED. F1 and F5 by the owner on 2026-08-10. F2, F3 and F4 by the agent
on 2026-08-11 under the standing mandate of `memory/builds/aSealedCaravan/README.md`, which delegates
resolver authority for forks these specs already state.

- **F1 — `tools/govkit/` or the research's `deploy/`?** RESOLVED (owner, 2026-08-10):
  `tools/govkit/`, ratifying the departure from the 2026-07-12 research shape. The argument is the
  three re-verified gate and inventory exclusions in section 4; the fourth cited at rev-1
  (`check-arms.py`) was wrong and has been dropped.
- **F2 — does the target descriptor live in the target or in gov?** RESOLVED (agent, 2026-08-11,
  delegated): the target, copier-style, as S3 already declares. It is the only option that makes S3's
  own claim true — a committed descriptor is a standing authorization for an unattended re-run, and a
  gov-side descriptor is not present in a fresh clone of the target, so that re-run would have nothing
  to read. A gov-side descriptor would also accumulate one file per target in a public deployer repo,
  a write and disclosure surface this unit never priced. The accepted cost is stated in section 4.
- **F3 — does `check-arms.py` grow a Python population?** RESOLVED (agent, 2026-08-11, delegated): it
  does not, in this unit. Its population is every tracked `*.sh` repo-wide, so admitting Python either
  demands an arm from every tracked `*.py` or needs a scoping rule — and either is a change to a
  governance carrier, which M3's second veto reserves for the owner. The engine change is raised as
  its own backlog row. The guarantee moves to the test layer, where AC16 makes it mechanical rather
  than a convention that decays.
- **F4 — what does `apply` do when a selected kit's gate is red in the target for reasons predating
  the install?** RESOLVED (agent, 2026-08-11, delegated): record a per-leg baseline verdict before
  writing anything, and fail only on a leg that was green in that baseline and is red after. The knob
  lives in the target descriptor. Failing on any red leg instead would make a target with one
  unrelated red leg undeployable, and section 3 does not make a pre-existing red gate a refusal.
  Section 4 carries the mechanism and AC15's fixture arm observes it.
- **F5 — is `tools/lib/` a registry entry or an exemption?** RESOLVED (owner, 2026-08-10): a
  permanent exemption. It is not a kit and ships nothing; `TOOL-aSealedCaravan-1` S9 gives the
  memory-tree kit its own launcher instead. Rollout commit 1 is unblocked.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft. Grounded on a five-probe inventory that ran all eight adoption
  entrypoints end to end in throwaway repos, decomposed the runbook into 66 steps, and confirmed the
  2026-07-12 research's Phase 0 landed in full.
- rev-2 · 2026-08-10 · folded review 1 (28 findings on this spec, 3 blockers) as a design pass over
  sections 4 and 6. Dropped the false `check-arms.py` third of fork F1's evidence. Replaced the
  per-kit exit-code map with per-outcome filesystem probes, after measuring six distinct exit-1
  outcomes in one adopter. Split `apply` into land and configure phases with `blocks_adopt` and
  `--resume`, because an unfilled `map_extractors.py` fails rather than defers and codebase-map is in
  the default set. Added `[[files]]` precedence so gov's own filled extractors and measured pins are
  not copied into a target, `requires_if` for the config-conditional memory-tree edge, a `scope` class
  for the machine-scoped kickoff engine, and `guard` plus `history_depth` on `[[gate_leg]]`. Replaced
  the undefined "8 shipped kits" with a tracked registry asserted in both directions. Added a staging
  step to S5, since every gate here reads the index. Rewrote section 6: AC2 is path-and-hash rather
  than porcelain, AC3 proves provenance, AC5 covers the blocked kit, AC6 derives the outbox from
  declared holes, AC8 names its detection predicate, and `plan`, `intake` and the S5 ordering gained
  the criteria they lacked.
- rev-3 · 2026-08-10 · resolved F5 on the owner's steer that `tools/lib/` is not a kit, after a
  repo-wide consumer audit showed "not a kit" does not mean "leftover". It becomes a permanent
  registry exemption whose stated reason carries the three ways it is load-bearing, so `selfcheck`
  is where a future reader meets that fact. Rollout commit 1 is no longer blocked.
- rev-4 · 2026-08-10 · owner ratified F1, so `tools/govkit/` is settled rather than recommended. F2,
  F3 and F4 stay open by choice — none blocks a build, and each wants the `plan`/`check` slice to
  exist before it is answered. The header carries no ratified pointer while they do.
- rev-6 · 2026-08-11 · folded the M4 spec audit, which returned BLOCKED with seven blockers, and the
  four measurement probes the fold needed. Four blockers landed inside rollout commit 1's own
  deliverable, so none of this could have waited for code. The population claims are gone: no count of
  any kind now appears in this document, because both counts earlier revs stated were true when
  measured and false when read, and `selfcheck` derives every one instead (S12, AC10). `[[files]]`
  gained destinations and the role enum gained `rendered`, `merged` and `seed`, without which four
  entries could not be written at all. `[[hole]]` gained a runnable discharge probe, a `blocks_gate`
  flag and an explicit observed-by-nothing class — measured as the LARGEST class, which is why AC5 and
  AC6 previously had no evaluator. AC1 was unsatisfiable for a default-set kit and is now derived from
  the descriptors; AC8 refused every re-run the spec designs for and now carves out the
  receipt-authorized path; AC3 is scoped to `engine`, because it was false for every other role. The
  gate-runner write gained a declaration, a consumer for `history_depth` and an effect criterion, and
  guards are now rendered — a fixture reproduced the runner reporting GREEN while skipping two failing
  legs guarded on absent paths. §3 gained three cut-lines: `apply` never commits, branches, pushes or
  opens a pull request, gov's own runner is not deployable and is exempt, and the four defects this
  grounding measured in gov's own shipped files are backlog rows rather than this unit's diff. Nine
  new criteria, AC17 through AC25, cover the arms that had none.
- rev-5 · 2026-08-11 · resolved F2, F3 and F4 under the standing mandate, closing the fork set before
  the first line of code. Deferring them until the `plan`/`check` slice existed was rev-4's plan, and
  it is abandoned rather than forgotten: a fork resolved mid-build is a rewrite of code already
  written, and all three turned out to be answerable from what the spec already states. F2 ratifies
  the target-side descriptor S3 already declares and names the disclosure it costs. F3 keeps
  `check-arms.py` shell-only, because extending it is a governance-carrier change, and moves the
  guarantee to the test layer where new AC16 makes it mechanical. F4 fixes the pre-existing-red policy
  as a measured baseline, which AC15's own fixture arm had no defined behaviour to observe until now.
  Section 4 carries the two design consequences and the header gains its ratified pointer.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py "deploy a kit into a target repo: copy files, render
config, wire gates, write an install receipt"`. Four seams are reused rather than reinvented.

`resolve_bash()` in `tools/memory-tree/corpus_ids.py:120` is the seam for launching the bash adopters
from Python. `resolve_python` in `tools/lib/resolve-python.sh` is the seam for the launcher probe, and
the repo bans the retired idiom it replaced, so there is no second spelling available. The fixture
builder `mkrepo()` in `tools/codebase-map/adopt-codebase-map.test.sh:64` already constructs a
throwaway repo with a kit installed at a caller-supplied prefix, which is exactly the acceptance
matrix's need; S11 extends it rather than writing a second one. `tools/gate-legs.json` plus its
iterator in `run-gates.sh` is the shape `[[gate_leg]]` adopts — including the `guard` key, which rev-1
omitted by describing the file as two-keyed when it carries three.

For `check`, the reuse is larger than a function. `tools/check-wiring.sh` implements five arms that
RUN the command they bless rather than asserting a file exists, and refuses to call an unverifiable
state clean. **FOUR** adopters ship a `--check` render-parity arm — agent-instructions, drift-audit,
memory-recall and unattended — corrected from the three earlier revs claimed, and the count matters
because it sizes `check`'s fan-out. codebase-map and memory-tree have none, which is why `check` cannot
be a thin fan-out over adopter check arms and must carry receipt integrity itself.
`manifest-check.sh` C1 is already "no placeholder survived the render" and C6 is already "every
declared pathspec matches at least one tracked file"; `check` composes both rather than restating them.

The reused seam rev-5 missed entirely is the declaration layer itself. `.unattended.conf` plus
`check-unattended.sh` is already this repo's "committed declarations the tooling READS and never
restates" mechanism, and it already solves four problems this spec designs from scratch: an explicit
required-versus-optional key split, a gate that reds when a script respells a declaration, a rendered
Skill graded for placeholder completeness as a question separate from template parity, and a
shipped-equals-installed parity check. Those map onto `[config]`'s key lists, AC9's named-missing-key
refusal, S10's rendered Skill and AC14's parity gate. `govkit check` composes that behaviour rather
than restating it, and the kit's own measured blind spot — a placeholder detector that greps one brace
shape and passes an angle-bracket one — is the reason AC6 runs a probe instead of a grep.

The anchored-region writer for the `merged` role is also reuse, not new code: `gen_build_index.py`'s
region splice already carries the exact refusal semantics this needs, one open marker and one close and
raise rather than guess, and it is already gated.

The lookup returned no seam for the descriptor loader, the receipt writer or the plan engine; those
are new. A fourth is new and was found by grep rather than by the lookup: **nothing in this repo writes
a git attributes block or performs a renormalize**, so S5's FIRST land step and AC4's second clause
have no implementation to extend anywhere. Recorded as "no existing seam fits" for those four, with the
note that bash is a declared recall-dark layer, so the lookup's coverage of the shell surface is partial
by design and that fourth gap is exactly the kind it cannot see.
