# DEPL-aSealedCaravan-2 — govkit, the mechanical deployer

**Status:** SPECCED · rev-2 · 2026-08-10 · node a · Tier-2 · base 16aeb5ef · streams deployer

## 1. Goal

Replace the prose adoption runbook with `govkit` — a descriptor-driven deployer that lands a chosen
subset of this repo's kits into a target repo that has none, either unattended or by prompting the
owner, and writes a receipt recording what was installed from which commit. Following 66 imperative
steps by hand is how a target ends up with kits in five homes and no record of what it took.

## 2. Scope (IN)

- **S1** `tools/govkit/govkit.py` — a Python stdlib core, no third-party dependency, running on the
  deployer machine only. Subcommands `plan`, `apply`, `apply --resume`, `intake`, `check`, `selfcheck`.
- **S2** A `kit.toml` descriptor for each entry in a tracked kit registry, declaring that kit as data:
  id, version constant location, `requires` and `requires_if`, the files it installs with their roles
  and precedence, the config keys it needs, its adopt command, its outcome map, its gate legs with
  their guards, its LF pins, its scope class, and its non-mechanical holes. The registry — not a
  directory listing — is the population, because three deployable surfaces are not `tools/*`
  directories and two `tools/*` directories are not deployable.
- **S3** A target descriptor at `<target>/.governance/deploy.toml`, written once by `intake` and
  committed. It carries the kit subset, every owner decision, and the failure-policy knobs. Committed,
  it is the standing authorization for an unattended re-run.
- **S4** A receipt at `<target>/.governance/install.json` plus a flat `<target>/.governance/install.sums`
  in `sha256sum -c` format, so a target verifies its own install with bash alone. Per file: role,
  sha256, kit id and version, and the gov source commit the bytes came from.
- **S5** `apply` in two phases. **Land** copies files, renders artifacts and wires gates, in a hard
  order: `.gitattributes` blocks, then `git add --renormalize`, then kit content, then rendered
  artifacts, then `git add` of everything written, then gate-runner and CI legs last. **Configure**
  runs each kit's adopt command. Every copy is taken from the gov git index at a recorded commit,
  never from the working tree. The `git add` step is not housekeeping: every gate in this suite reads
  the index, so an unstaged install is invisible to the verification that follows it.
- **S6** The default kit set is the three-layer chain plus codebase-map and memory-recall: playbook,
  kickoff manifest with its ratchet, memory-tree, codebase-map, memory-recall. `--kits` selects
  otherwise; `--all` adds drift-audit, agent-instructions, the agent-cap hook with the review harness,
  gate-lint and the pytest guardrails.
- **S7** Unattended and interactive are one code path with two decision sources. `intake` prompts and
  writes the target descriptor; `apply --unattended` reads every answer from that descriptor and
  refuses rather than guessing when one is absent.
- **S8** Every non-mechanical hole is declared in its kit's descriptor as a `[[hole]]`, and the outbox
  is derived from the union of holes over the SELECTED kits. A hole that makes its adopter fail
  carries `blocks_adopt = true`: that kit lands but is not configured, and `govkit apply --resume`
  configures it once the order is discharged. `check` distinguishes three states — not landed, landed
  but inert, adopted.
- **S9** `check` — a read-only verifier over an installed target: receipt integrity, provenance, every
  kit's own `--check` arm where one exists, hole discharge, and outbox age. It is the leg a target
  repo runs in its own CI.
- **S10** `skills/deploy-governance/SKILL.md` so an agent invokes the deployer rather than reading the
  runbook. `WIRE-INTO-PROJECT.md` is demoted to narrative, kept honest by a parity gate asserting
  every descriptor step has a runbook section and the reverse.
- **S11** An acceptance matrix over fixture repos, each required to pass apply-twice-changed-zero, on
  both POSIX and Git-Bash.

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
`selfcheck`. It exists because no directory listing equals the deployable set: `tools/` holds ten
directories, of which `tools/lib/` is gov-internal by `TOOL-aBatchedTribunal-6j` and `tools/hooks/`
deploys as part of the review-harness entry, while three deployable surfaces are not `tools/*`
directories at all — the playbook and its two companions are root files, the manifest ratchet is
`skills/session-kickoff/manifest-check.sh`, and `settings-merge.py` is a single file. Each entry
names its descriptor's location; each `tools/*` directory not in the registry is listed as exempt
with a reason. `map_extractors._tool_kits()`'s own docstring records why this must be a declaration
rather than a heuristic: README-gating "would have silently dropped three of ten".

**`kit.toml`**, one per registry entry, beside the kit where the kit is a directory:

```toml
id = "memory-tree"
scope = "repo"                         # repo | machine — the kickoff engine is machine-scoped
version_from = { file = "check-memory-hygiene.sh", pattern = "^KIT_MEMORY_TREE_VERSION=" }
requires = []
requires_if = [{ kit = "memory-recall", when = "pins.corpus_ids_enabled", why = "corpus_ids.py:44 binds GRAMMAR_DIR to a memory-recall sibling" }]

[[files]]                              # precedence: later rules win, so exclusions are expressible
include = "**"
role = "engine"
[[files]]
include = ["map_extractors.py", "drift_signals.py", "*.conf"]
role = "project-owned"                 # never copied FROM gov, never overwritten in the target
[[files]]
include = ["generated/**", "baseline.toml"]
role = "generated"                     # produced in the target, never carried across

[config]
file = ".memory-tree.conf"
owner = "memory-tree"
required_keys = ["MEMORY_ROOT", "DISCIPLINES", "FAMILIES"]

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
name = "memory hygiene (19 checks)"
argv = ["bash", "{kit}/check-memory-hygiene.sh"]
guard = []                             # gate-legs.json carries three keys, not two
history_depth = "full"                 # CI checkout needs fetch-depth 0 or the leg WARN-skips

[[hole]]
id = "measured-pins"
kind = "authoring"
blocks_adopt = false
why = "every pin is measured against the target corpus; an inherited number is vacuous or permanently red"
```

Four fields exist because rev-1's model could not express what the adopters actually do.

**`[[outcome]]` probes rather than declares.** The exit-code collision is per BRANCH, not per kit.
`adopt-codebase-map.sh` alone exits 1 for six unrelated outcomes — an identity refusal at `:52` with
nothing written, three prefix refusals explicitly before any write, a seeded conf at `:150`, seeded
extractors at `:184`, a `gen_map` crash at `:191` leaving a half-written map tree, and a failing gate
at `:212` with the conf, the map tree and the gate file all on disk. A code-to-meaning table cannot
tell those apart, and parsing stdout is fragile. So each outcome declares a filesystem probe the
deployer RUNS. The classification is measured, which is the rule `adopt-codebase-map.sh:137` already
states: claim nothing until it is read back.

**`[[files]]` has precedence.** A bare whole-kit engine glob would copy gov's own filled
`map_extractors.py`, its measured pins and its generated inventories into the target — the
inherited-vacuous-numbers failure the memory-tree adopter warns about in its own closing output.
Later rules win, so `role = "project-owned"` and `role = "generated"` carve out of the engine glob.

**`requires_if` is conditional.** memory-recall depends on memory-tree unconditionally, and drift-audit
does too, both enforced in code by a refuse-never-create. The reverse edge is different: memory-tree
needs memory-recall only when the corpus-id checks are armed, because `corpus_ids.py:44` binds its
grammar directory to a memory-recall sibling. A blanket `requires` would force memory-recall on every
target; omitting the edge lets a target arm checks 13 through 16 against a kit that is not there.

**`scope` separates repo from machine.** The kickoff engine installs once per machine as a junction,
not per repo. Without the class, `apply` would either try to commit a junction or silently skip the
one component `/session-kickoff` needs.

**`.governance/deploy.toml`** in the target: `gov_source`, `prefix`, the selected kit ids, one table
per kit holding its config answers, and the failure-policy knobs — on a diverged remote, on a
pre-existing red gate, on a hook block, on a push-scope failure.

**`.governance/install.json`** — the receipt, tool-written only, plus the flat `install.sums` sidecar.
The apply layer has no code path that writes a file whose role is `project-owned`.

### Inventory: what the deployer must know per kit

Measured by running all eight adoption entrypoints end to end in throwaway repos.

| Kit | In default set | Config | Holes | Blocking |
|---|---|---|---|---|
| playbook | yes | none | 36 placeholders across two files | no — an unfilled playbook is inert, not fatal |
| kickoff manifest | yes | none | manifest section B | no |
| memory-tree | yes | owns `.memory-tree.conf` | taxonomy, measured pins | no |
| codebase-map | yes | owns `.codebase-map.conf` | `map_extractors.py` | **YES** |
| memory-recall | yes | reads `.memory-tree.conf` | none | no |
| drift-audit | `--all` | reads `.memory-tree.conf` | `drift_signals.py` | no, and that is worse |
| agent-instructions | `--all` | none | none | no |
| agent-cap + workflows | `--all` | none | none | no |
| gate-lint | `--all` | none | leg wiring is the adopter's | no |
| pytest guardrails | `--all` | none | `pyproject.toml` knobs | no |

The default set therefore declares **four** holes — playbook placeholders, manifest section B,
memory-tree's taxonomy and pins, and `map_extractors.py` — exactly one of which blocks.

### The blocking hole, and why apply has two phases

An unfilled `map_extractors.py` does not defer, it fails.
`map_extractors.template.py:112` raises on an empty extractor dict and `gen_map.py:38` calls
`inventory_ids()` at module level, so `adopt-codebase-map.sh` exits 1 at `:191` with no map tree, no
baseline and no gate file. The installed gate cannot even import, because
`test_codebase_map.template.py:70` binds the same call at module scope. codebase-map is in the default
set, so a single-phase `apply` of the default set can never reach a green fixture.

Hence S5's split and S8's `blocks_adopt`. The land phase copies codebase-map's files and writes the
work order; the configure phase skips it; `check` reports it landed-but-inert; and
`govkit apply --resume` runs its adopter once `map_extractors.py` is filled. The codebase-map adopter
remains the model for everything else — it is the only one that verifies its own effect by running
the gate it just installed — but it is not the model for the unattended path, which rev-1 claimed.

The inverse failure is drift-audit's and it is the more dangerous of the two: it seeds empty product
globs and unmeasured pins, and its own `--check` passes on that file because it tests existence only.
memory-recall's `--check` likewise exits 0 as a skip when nothing was rendered. Exit 0 from an adopter
means "the adopter ran", never "the kit works", so `apply` records the hole and `check` reports the
target incompletely adopted regardless of adopter status.

### The bash-from-Python trap

`govkit.py` shells out to bash adopters, and on a Windows node `subprocess` resolving the bare name
`bash` finds the System32 WSL launcher before git-bash. WSL then sees a different filesystem: an
existing path reports no such file, and a relative path resolves under a mount prefix. The remedy
already exists and is not to be rewritten — `resolve_bash()` in `tools/memory-tree/corpus_ids.py:120`
names the executable, accepts a candidate only if it RUNS, and treats a set-but-unusable `GOV_BASH` as
a named failure rather than a fall-through.

### Rollout

Four commits, each independently valuable and independently green:

1. `registry.toml`, a `kit.toml` for every entry, and `selfcheck`. No deployer behaviour; immediate
   value as a machine-readable kit inventory. TOOL fork F3 must resolve first, since it decides
   whether `tools/lib/` is an entry or an exemption.
2. `plan` and `check`, both read-only. Zero write risk, and `check` is usable against an
   already-adopted target on day one.
3. `apply`, `apply --resume` and the receipt, plus the acceptance matrix.
4. `intake`, the Skill, the runbook demotion and the parity gate.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` and modules | the bulk |
| Registry, descriptors | 1 + 12 | one per registry entry, not one per `tools/*` dir |
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

- security — the deployer writes into a repository the operator names. The identity guard the
  codebase-map adopter already carries is the model: refuse before writing when the resolved target is
  not the tree the operator named. No credentials are handled; landing is by branch and PR.
- perf / scale — a single-target install; the cost is the adopters', not the orchestrator's.
- a11y — N/A: a command-line tool with no interface beyond stdout.
- i18n — N/A: developer tooling, English only.
- error / empty / loading states — "exit 0 from an adopter is not installation proof" is this line,
  and the three-state `check` is its implementation.
- observability — the receipt is the observability surface, and `check` is its reader.
- risks — a half-applied install is the main one; S5's ordering and branch-and-PR landing bound it. A
  crash leaves an abandoned branch, never a half-mutated primary tree. Receipt provenance is the
  second: bytes must be provably from the recorded commit, not from a dirty working tree.
- testing + left-shift gates — the acceptance matrix is the deliverable's own gate; fixtures reuse
  the existing prefix-parameterized fixture builder.
- migration / rollback — no migration, by non-goal. Rollback of a fresh install is deleting the branch.
- user docs — the Skill plus the demoted runbook.

## 6. Acceptance criteria

- **AC1** When `apply` runs unattended against a fixture repo with no kit and a committed target
  descriptor, every default-set kit with no blocking hole lands AND configures, and each of their gate
  legs exits 0 in that fixture. codebase-map is excluded from this criterion by AC5.
- **AC2** When that `apply` runs a second time, no path in the receipt changes content hash and no
  path is added or removed. The predicate is path-and-hash over the receipt, not `git status
  --porcelain`, because the adopters stage their own writes and a porcelain-empty tree would be
  satisfied by an install that did nothing. Runs on POSIX and Git-Bash.
- **AC3** When `apply` runs from a gov checkout whose working tree is deliberately dirty, every file
  named in the receipt has bytes equal to `git show <recorded_commit>:<path>`. This is the receipt's
  provenance claim and nothing else observes it.
- **AC4** When `apply` runs, its log shows the `.gitattributes` write and the renormalize strictly
  before the first kit-content write, the `git add` of everything written before any gate leg runs,
  and the gate-runner and CI wiring strictly last.
- **AC5** When the default set is applied, codebase-map is landed-but-inert: its files are present,
  its adopter did not run, `check` reports it in the inert state, and its gate leg is red by design.
  After a fixture `map_extractors.py` is filled and `govkit apply --resume` runs, the adopter
  completes and the leg exits 0.
- **AC6** When the default set is applied, the outbox holds exactly one order per `[[hole]]` declared
  by a selected kit — for the default set, the four ids named in section 4 — and `check` exits
  non-zero until each is discharged. The criterion asserts the id set, never a literal count.
- **AC7** When a file whose receipt role is `project-owned` is modified in the target and `apply` is
  re-run, that file is not rewritten, and `check` reports it as project-owned rather than as drift.
- **AC8** When `apply` is pointed at a repo that already carries a kit, it refuses before writing.
  Detection predicate: any registry entry's version constant resolves in the target, or
  `.governance/install.json` exists. The refusal names which.
- **AC9** When `apply --unattended` is given a descriptor missing an answer the selected kits require,
  it refuses before writing anything and names the missing key.
- **AC10** When `govkit.py selfcheck` runs in this repo, every `registry.toml` entry has a descriptor,
  every descriptor's declared files exist, every declared gate leg appears in `tools/gate-legs.json`
  with a matching `guard`, every `version_from` pattern matches exactly one line in its named file,
  and every `tools/*` directory is either an entry or an exemption with a reason.
- **AC11** When `plan` runs against a fixture, it lists every file it would write with its role and
  source commit and writes nothing; running `apply` then produces exactly that file set.
- **AC12** When `intake` runs non-interactively with a prepared answer stream, it writes a
  `deploy.toml` that `apply --unattended` accepts with no further prompting.
- **AC13** When `govkit.py` runs on a Windows node with WSL on PATH, it resolves git-bash and the
  adopters execute; with `GOV_BASH` set to something unusable it fails naming that override rather
  than falling through.
- **AC14** When the runbook and the descriptors disagree — a descriptor step with no runbook section,
  or the reverse — the parity gate reds naming both sides.
- **AC15** When the acceptance matrix runs, it covers at minimum a fresh empty repo, a non-Python
  repo, a repo whose pre-commit hook blocks, and a repo with a pre-existing red gate; each arm asserts
  a specific message or on-disk effect, never an exit code alone.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary. Three new legs: `govkit selfcheck`, the
acceptance matrix, and the runbook parity gate. Each addition trips the same four gates named in
`TOOL-aSealedCaravan-1` section 7 — codebase-map coverage, codebase-map freshness, the manifest
ratchet, and drift-audit's handkept charter citation, which has zero slack.

Two obligations are specific to this unit. `tools/govkit/` is a new `kits` inventory key, so it needs
a dossier at `memory/map/features/govkit.md` before the coverage gate goes green. And
`check-kit-versions.sh` is a hardcoded list of `need` calls rather than an enumeration, so govkit's
own version constant must be added to it explicitly or nothing gates it.

A deployed `[[gate_leg]]` carries `history_depth`, because a leg wired into a target's CI with the
`actions/checkout` default depth makes the manifest drift check WARN-and-skip on every run — the
runbook already calls `fetch-depth: 0` mandatory rather than advisory, and the descriptor must carry
that or the deployed leg is vacuously green.

Before review: `python tools/memory-tree/gotchas.py --for-diff 16aeb5ef..HEAD`.

## 8. Open questions

- **F1 — `tools/govkit/` or the research's `deploy/`?** RECOMMENDATION: `tools/govkit/`, on the
  four-gate measurement in section 4. One of the four cited at rev-1 (`check-arms.py`) was wrong and
  has been dropped; the remaining three hold and were re-verified. This departs from an approved
  research shape, so it is the owner's to ratify.
- **F2 — does the target descriptor live in the target or in gov?** RECOMMENDATION: the target,
  copier-style, so it travels with clones. The cost is that a target repo carries a file naming its
  gov source, which is a disclosure the owner should weigh for a public target.
- **F3 — does `check-arms.py` grow a Python population?** It scans tracked `*.sh` repo-wide today, so
  `govkit.py`'s refusal branches carry no arming obligation, and the strongest new write path in the
  repo would be the least armed. RECOMMENDATION: do not extend it in this unit — require instead that
  every refusal branch is exercised by a matrix arm asserting its own message, which buys the same
  guarantee at the test layer. Raise the engine change separately.
- **F4 — what does `apply` do when a selected kit's gate is red in the target for reasons predating
  the install?** RECOMMENDATION: record the baseline before touching anything, and fail only on a leg
  that was green before and is red after. The knob is in the target descriptor.
- **F5 — is `tools/lib/` a registry entry or an exemption?** Blocked on `TOOL-aSealedCaravan-1` fork
  F3. `selfcheck` is rollout commit 1's whole deliverable and cannot be written until it resolves.

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
state clean. THREE adopters ship a `--check` render-parity arm — agent-instructions, drift-audit and
memory-recall — not five; codebase-map and memory-tree have none, which is why `check` cannot be a
thin fan-out over adopter `--check` and must carry receipt integrity itself. `manifest-check.sh` C1 is
already "no placeholder survived the render" and C6 is already "every declared pathspec matches at
least one tracked file"; `check` composes both rather than restating them.

The lookup returned no seam for the descriptor loader, the receipt writer or the plan engine; those
are new. Recorded as "no existing seam fits" for those three, with the note that bash is a declared
recall-dark layer, so the lookup's coverage of the shell surface is partial by design.
