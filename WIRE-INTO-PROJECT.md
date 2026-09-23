# Wire the coding-governance chain into a project — agent runbook

You are wiring the **full coding-governance chain** into a target project. Follow this top to bottom;
verify after every step. This file is agent-facing: imperative steps, exact commands, explicit
derive-vs-ask calls.

**The chain is three composing layers:**

1. **Governance playbook** (`coding-governance-agents.template.md`) — the multi-node ruleset (IDs,
   streams, work state, gates, reviews, memory, output discipline). Lives in the project as one doc.
2. **`/session-kickoff` skill** (`skills/session-kickoff/`) — the project-agnostic kickoff *engine*,
   installed ONCE per machine; it reads a per-project **kickoff manifest** to learn project specifics.
3. **memory-tree kit** (`tools/memory-tree/`) — the gated `memory/` structure that operationalizes the
   playbook's §5/§6. Optional but recommended.

**Precedence (never violate):** project `CLAUDE.md` > kickoff manifest > the skill. The playbook is the
ruleset the manifest points at, not a duplicate of it.

**Posture:** DERIVE everything the repo reveals (gate commands, layout, remote, default branch, id
families); use `AskUserQuestion` ONLY for what it genuinely can't (node registry, stream ownership, tier
policy, whether to adopt memory-tree). Keep it tight — this is wiring, not a meeting.

**Definitions:** `<gov>` = the `coding-governance` checkout (the repo this file lives in); `<project>` =
the target repo root. Commands are bash (git-bash on Windows). If `<gov>` is unknown, ask.

---

## 0 — Preconditions + the decisions to lock first

- Confirm `<project>` is a git repo, on its default branch, clean:
  `git -C <project> status --short` (empty) · `git -C <project> symbolic-ref --short HEAD`.
- **Ask the user** (not derivable):
  - **Fleet** — one node-registry row per machine/agent: tag · machine · primary-tree path · worktree
    root · variances. (Solo/single machine → one row.)
  - **Stream ownership** — which node owns which stream (keeps merges disjoint).
  - **Tier policy** — single-tier, or Tier-1/Tier-2 and what forces Tier-2 (new write path · migration ·
    auth/sanitization/egress surface · shared-contract change · cross-stream merge).
  - **memory-tree is REQUIRED** — not a question. Playbook v2.5 made it so
    (`coding-governance-agents.template.md` §5): §5's work-state
    rules and §6's record protocol both assume the tree. There is no drop path and no
    `{{MEMORY_*}}`-deletion branch; §3 is mandatory.
  - **Adopt codebase-map?** yes (recommended for any repo past ~20 modules) / no. If yes, lock:
    MAP_ROOT (under the memory tree when memory-tree is adopted, e.g. `memory/map`; else `docs/map`),
    GATE_FILE (a path the project's EXISTING test suite collects), and which surfaces to inventory
    (walk `tools/codebase-map/INVENTORY-DERIVATION.md` §1 with the user). If no: skip §3b and delete the
    FOUR codebase-map lines from the playbook (§1 DoR + §1 DoD + §5 kit bullet + §7 gates line).
  - **Adopt memory-recall?** yes / no — retrieval over the memory tree (ask the decision corpus a
    question in English, get the records that answer it, ranked). **Requires memory-tree**: the kit
    reads `.memory-tree.conf` and refuses without it, so a "no" above forces a "no" here. Also lock
    whether to take the optional `recall-opened` PostToolUse hook (§3c step 4 — declining is a
    supported end state). If no: skip §3c and delete the ONE memory-recall §5 kit bullet.
- **Derive, don't ask:** gate commands (`package.json` / `Makefile` / CI config), repo layout (the tree),
  remote + default branch, id families.

<!-- govkit:entry kickoff-manifest -->
## 1 — Install the kickoff skill (ONCE per machine — NOT per project)

Link the engine into the user-level skills dir so `/session-kickoff` fires in every project:

```powershell
# Windows — junction, no admin needed
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-kickoff" -Target "<gov>\skills\session-kickoff"
```

```bash
# POSIX
ln -s <gov>/skills/session-kickoff ~/.claude/skills/session-kickoff
```

**Verify:** restart Claude Code; `/session-kickoff` is listed. (A project MAY keep its own tuned variant
alongside — both then appear; pick by description.) Skip this step on a machine that already has it.

<!-- govkit:entry playbook -->
## 2 — Install the governance charter (per project)

The charter is ONE file and it BECOMES the project's `AGENTS.md`. There is no companion to ship
alongside and no placeholder catalogue to read: `tools/playbook/adopt-playbook.sh` fills every
placeholder from the target's own `deploy.toml` and drops the conditional blocks the target has no
kit for. Run it rather than copying by hand.

```bash
python <gov>/tools/govkit/govkit.py intake --target <project> --kits playbook,playbook-render,check-microformats,…
bash  <gov>/tools/playbook/adopt-playbook.sh --target <project>
bash  <gov>/tools/playbook/adopt-playbook.sh --target <project> --check   # wire as a gate leg
```

**Keep the `<!-- governance-template: vN.N -->` marker verbatim** — the kickoff engine's Step-2
fallback and the upstream re-pull both read it.

### What the renderer cannot decide for you

Everything below is a judgement call about YOUR project. The renderer refuses rather than guessing,
so these are the answers `intake` will ask for, and the kits whose blocks the charter carries.

- **The memory tree is not droppable.** `§5`'s derived work-state index and `§6`'s record protocol
  are both written against it, so a charter without it states rules nothing can make true. Adopt it
  at §3 below.
- **A self-verifying codebase map** (`codebase-map/` kit): per-feature dossiers claim EXACT KEYS from
  machine-enumerated inventories, and a ratchet fails on any unclaimed new key AND any claim naming a
  dead key, so the map cannot rot into fiction. `map_diff` renders any git range as a feature-level
  changelog. Zero CI changes — the gate rides the existing suite. Keeping it selected keeps three
  `kit:codebase-map` blocks in the charter.
- **A records-vs-reality audit** (`drift-audit/` kit): asks whether this repo's RECORD of its own
  state still matches the tree — stale claims, closed specs with no product commit, hand-kept
  inventories disagreeing with what they describe. Stdlib and git, seconds, no agents. Drop it if the
  project keeps no in-repo records for an audit to compare reality against.
- **Retrieval over that tree** (`memory-recall/` kit, requires the memory tree): ask the decision
  corpus a question and get the records that answer it, ranked. Offline, stdlib, writes nothing in
  the worktree.
- **One canonical instruction file** (`agent-instructions/` kit): agents do not all read the same
  filename, and Claude Code does not read `AGENTS.md` natively. Drop it only if exactly one agent
  tool reads this repo; with two, this kit is what stops the second reading a stale copy.
- **Parallel-test guardrails** (`pytest-parallel-guardrails/` kit): drop it if the project is not
  Python or does not run `pytest -n auto`. The bug classes it fixes stay in the charter either way.
- **A source-hygiene scan for PowerShell** (`gate-lint/` kit): drop it if the project has no `.ps1`
  files. A repo with none gets a clean report that proves nothing, which is honest and is why it is
  adopted only where the language exists.
- **A deployer for your own tooling** (`govkit/` kit): drop it unless this repo DEPLOYS kits into
  other repos. An adopter that only consumes them has no population to declare.
- **A naming lexicon** (`lexicon/` kit): a closed verb table every definition leads with, banned type
  suffixes, and forbidden import directions between layers. Opt-in — with no conf it reports NOT
  ADOPTED and exits 0. Keeping it selected keeps the `kit:lexicon` block in `§12`; dropping it
  removes five bullets and `{{LEXICON_CONF}}` with them.
- **Unattended runs** (`unattended/` kit): keeping it selected keeps the `kit:unattended` block in
  `§1`, which is the ONE substitute for the explicit ask before a merge and a push. A repo that keeps
  that clause without the kit is carrying a rule nothing can make true.

### The two blocks that are not about a kit

`drop_blocks` in the target's `deploy.toml` names blocks to remove that no kit governs. Two exist:

- `when:security-outbound` — the outbound-call and stored-content rules in `§9`. Drop them if the
  project has no such surface.
- `when:cross-os` — `§11` whole. Drop it for a single-OS team.

`§15`'s persona is adjustable per project and is NOT a droppable block: editing the persona is the
sanctioned change, and its facts-over-wit rules are not adjustable at all.

### Where each value comes from

- **Precedence.** `[charter]`, then `[answers]`, then the probe or the declared default. An answer
  outranks a probe, and the render prints both, so correct a wrong derivation by answering it rather
  than by forking the descriptor.
- **`playbook_path` names the TEMPLATE** when `playbook-render` is selected; the charter is
  `--charter`, default `AGENTS.md`, and the render refuses when the two are one file. Without the
  renderer it is the copied charter, and the placeholder hole probes it.
- **`[charter]`** holds render-only prose that `[answers]` refuses, such as the commit trailer with
  its angle brackets. govkit never reads it into an argv. A key there must name a declared
  placeholder and no argv token, and a value may not carry a control character other than a
  newline, `{{`, or a `gov:playbook` marker.

**Verify:** the renderer's `--check` is the standing verification and it asserts two separate things
— that the rendered region still matches the template plus the answers, and that no placeholder
survived. Those are two questions, and a conf that declares nothing for a key renders a region that
is perfectly in sync and still tells the agent to invoke a placeholder's name.

**Authoring a kit: a `placeholders` list may only name tokens that kit's OWN adopter substitutes.**
Declaring one the adopter never computes ships an unresolved `{{TOKEN}}` brace into every adopter's
committed tree, and they can only fix it by forking the descriptor. `python
tools/check-kit-placeholders.py` is the join and reds on it; a kit that legitimately has no adopter
says so with `why_no_adopter` in its `[adopt]` block.

<!-- govkit:entry check-microformats -->
### 2a — The micro-format definition gate

`check-microformats` arrives with the charter and grades the micro-format DEFINITION block inside
it, so a target that renders the charter gets the gate that keeps that block honest. It is in the
default selection; decline it by naming a selection that omits it.

Wire the leg into your gate runner and CI as `micro-format definitions`, running
`bash {prefix}/check-microformats.sh <playbook>` — the argv the descriptor declares, with
`{prefix}` resolved to your install prefix. The token form is deliberate: a literal `tools/` path
here would raise this file's carried-prefix count and red `install-prefix`.

<!-- govkit:entry memory-tree -->
## 3 — Adopt the memory-tree kit (if chosen in §0)

1. Copy the kit in and configure:
   ```bash
   cp -r <gov>/tools/memory-tree <project>/tools/memory-tree
   cp <project>/tools/memory-tree/.memory-tree.conf.example <project>/.memory-tree.conf   # then edit
   ```
   Edit `.memory-tree.conf`. The example ships SIXTEEN keys and this lists the ones you must decide;
   read the file itself for the rest, and note the adopter's own closing output names three more as
   REQUIRED arming steps (`STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF`, and MEASURING every pin against
   YOUR corpus rather than inheriting another repo's numbers). `MEMORY_ROOT` · `DISCIPLINES` (your streams) · `FAMILIES`
   (`discipline:FAMILY`, MUST match the playbook's `{{ID_FAMILIES}}`) · `TOMBSTONE_ROOTS` (blank for a
   fresh tree; set to the old root only when migrating an existing docs tree — see `tools/memory-tree/README.md`).
   Arm the spec-format ratchet: `SPEC_FORMAT_CUTOFF=<adoption date>` — specs dated ≥ it must follow
   `memory/TEMPLATE-SPEC.md` (hygiene check 12); older specs stay grandfathered by filename date.
2. Scaffold + verify:
   ```bash
   cd <project>
   bash tools/memory-tree/adopt-memory-tree.sh --scaffold
   bash tools/memory-tree/check-memory-hygiene.sh ; echo $?    # expect 0
   ```
   The scaffold writes `memory/` with `builds/`, `backlog/<FAMILY>.md`, the generated `LIVE.md`, and
   `project/` — which holds the gate's own six waiver registries (`*.txt`) **and nothing else**. Work
   state is not authored anywhere: `gen_build_index.py` renders it. See §3a if you already run a kit
   older than 1.8.
3. Wire the gate in all three places:
   - **CI:** a job running `bash tools/memory-tree/check-memory-hygiene.sh` (no args = full check, incl. TREE drift).
   - **Local gate runner:** add it as a concurrent leg (cheap, parallel with test/typecheck).
   - **pre-commit hook** — guarded so a scripts-less checkout stays green:
     ```sh
     top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
     if [ -f "$top/memory-tree/check-memory-hygiene.sh" ] &&
        git diff --cached --name-only --diff-filter=ACMR -- 'memory/**' | grep -q .; then
       bash "$top/memory-tree/check-memory-hygiene.sh" --staged || exit 1
     fi
     ```
   - **`.gitattributes`** (Windows-determinism for check 9) — add:
     ```
     memory/**/*.md text eol=lf
     memory/**/*.txt text eol=lf
     memory/**/*.toml text eol=lf
     # The broad form on purpose: the scaffolder writes SIX registries under project/, not two
     # (legacy-files, curation-debt, id-orphan-waiver, corpus-path-unresolved, unarmed-branches),
     # and §6 step 6 already asserts all five exist. Naming them individually is how three of them
     # went unpinned.
     ```

4. **Wire the row-keyed merge driver** — `cp -r` delivered `merge-rows.py` and its launcher, but a
   merge driver is a per-node git config and no scaffolder can write it. Without this, two nodes
   appending to `DECISIONS.md` or a backlog shard get git's line merge, which duplicates or drops
   rows on an append collision.
   ```bash
   git config merge.rows.driver "bash tools/memory-tree/merge-rows.sh %O %A %B %P"
   ```
   Add the attributes (adjust to your `MEMORY_ROOT`), then let the wiring checker verify it:
   ```
   memory/DECISIONS.md   merge=rows
   memory/backlog/*.md   merge=rows
   ```
   `bash tools/check-wiring.sh --check` RUNS the configured command on a scratch three-way before it
   reports `ok`, because a driver that cannot start never writes `%A`: git prints `CONFLICT` and
   leaves the path holding OURS-ONLY content with zero conflict markers. `--fix` sets the config for
   you and refuses to declare a driver wired when it cannot run.

<!-- govkit:entry drift-audit -->

### 3a-bind — Record bindings, if your tree already holds records (kit ≥ 2.19)

**An untouched tree with records reds on the first run, and that is the design.** Hygiene check 21
requires every file under `<MEMORY_ROOT>/builds/*/{build,prompts,reviews}/` to name, in its own head,
the spec ids it is evidence about. Branch 1 names every record carrying no such line. No value of
`RECORD_UNBOUND_PIN` makes that green: the pin bounds the deliberate `none` escape, and a record
nobody has annotated is a different state from one someone declared unbindable.

This section applies to an EXISTING adopter as much as a new one — `adopt-memory-tree.sh` exits early
on an already-adopted tree, so a rule added after your adoption reaches you here and nowhere else.

1. **See the work.** `python <kit>/gen_build_index.py --print-bindings` — read-only, writes nothing,
   always exits 0. Every `A` row is a record with no line.
2. **One mechanical pass.** Give each `**Serves:** none — <why>`. This needs no judgement about what
   any document was about, which is what makes it mechanical rather than a retrofit, and it is not a
   cutoff: nothing is exempted by date and every record stays visible and countable.
3. **Then measure.** Set `RECORD_UNBOUND_PIN` to the `N` count that pass leaves. Measured against
   YOUR corpus — a number copied from another repo is either vacuous or permanently red.
4. **Drain it.** As you bind records for real, replace `none` with
   `**Serves:** <kind> <id> [<id>…]`, kinds `spec-audit` · `diff-review` · `journal` · `research`.
   The pin is shrink-only, so the ratchet points down from wherever you started.

Worked example, measured on this repo at kit 2.19: 78 records, of which 72 bound and 6 carry `none`
with a reason — a build that predates the spec-format ratchet and holds no spec at all, two design
passes their READMEs grade as rejected or preceding, two commissioning censuses, and one build's own
design-pass record. That six is the pin, and it falls when those builds gain specs a record can name.

Renaming records so the FILENAME also names its spec is optional and separate. This repo did it; the
grammar does not change to allow it, because the ordinal is redefined rather than widened. If you do
it, check 21's branch 4 keeps the two carriers in agreement afterwards.

## 3d — Adopt the drift-audit kit (optional, recommended)

Does this repo's own RECORD of its state still match reality? Signals over stdlib + git, seconds,
no agents. It reads `.memory-tree.conf` and **refuses** without it, so §3 comes first.

1. `cp -r <gov>/tools/drift-audit <project>/tools/drift-audit`
2. `bash tools/drift-audit/adopt-drift-audit.sh` — seeds `drift_signals.py` from the template and
   renders `.claude/skills/drift-audit/SKILL.md`.
3. **Fill `tools/drift-audit/drift_signals.py`** — `PRODUCT_GLOBS` at minimum. This is the real work
   and it is NOT mechanical. The adopter seeds the file with empty globs and unmeasured pins, and its
   own `--check` passes on that file because it tests existence only: exit 0 here means "the adopter
   ran", never "the kit works".
4. Run `python tools/drift-audit/drift_report.py`, then seed each PIN at the value you just MEASURED
   — never at zero, and never inherited from another repo.
5. Wire three legs into your gate runner and CI: `python tools/drift-audit/selftest.py`,
   `bash tools/drift-audit/adopt-drift-audit.sh --check`, and
   `python tools/drift-audit/drift_report.py --check`.

## 3e — Adopt the process-monitor kit (optional, recommended)

Every deadline this chain owns bounds a command a CHECKER launched. Nothing bounds a process an
AGENT launched, and that is where the observed failures come from: spin loops hours old holding
core-hours of CPU, suites still running long after the session that started them was stopped, a gate
runner surviving its own harness. This kit identifies those, reports them to the session, and kills
them on request.

1. `cp -r <gov>/tools/process-monitor <project>/tools/process-monitor`
2. **Write `.process-monitor.conf` at the project root.** `PROCMON_ROOTS` is the whole safety fence
   and it is the one value nobody can write for you — it declares which directory trees a process
   must be attributable to before this kit will look at it, let alone signal it. Everything outside
   is invisible BY DESIGN. Do not name a filesystem root, your home directory, or the system temp
   directory; the adopter refuses all three.
3. `bash tools/process-monitor/adopt-process-monitor.sh --check` — it grades the DECLARATION, not
   the result. Exit 0 means the conf is well-formed and the hook is wired, never that your roots
   admit your own work.
4. **Answer the roots question separately**, because step 3 does not:
   `python tools/process-monitor/scope.py --check-conf`, and
   `python tools/process-monitor/scope.py --explain <winpid>` on a process you care about.
5. Wire the reporting hook (the adopter writes the fragment) and two legs into your gate runner:
   `python tools/process-monitor/selftest.py` and
   `bash tools/process-monitor/adopt-process-monitor.test.sh`.
6. `python tools/process-monitor/reap.py --sweep --dry-run` before you ever pass `--kill`. The walk
   root is graded before anything is walked, and a dry run is how you find out that your roots are
   narrower — or wider — than you assumed.

**Read the kit README's "What this kit does NOT check" before you trust a clean report.** The
limitation that costs most: a process whose command line names no declared root AND whose ancestry
has died is unattributable, and the report names that count rather than passing over it. A tree
launched by a relative path falls into it the moment its parent exits — which is why a launcher
worth monitoring invokes its program by absolute path.

### 3a — Migrating an existing repo off the sharded session ledger (BREAKING)

**The sharded authored session ledger is RETIRED** at **playbook v2.4 / memory-tree kit 1.8** — two
products, two version lines, and the ruleset change is the playbook's, not the kit's. If your repo
carries `<MEMORY_ROOT>/project/IN-FLIGHT.md` (the pointer stub) plus `<MEMORY_ROOT>/project/in-flight/<tag>.md`
(the per-node shards), it was scaffolded by kit ≤ 1.7 and this is a breaking upgrade: the scaffolder
no longer writes that shape and hygiene check 3 no longer admits it, so an untouched tree goes red on
its first run of the new gate. Skip this whole section if you are scaffolding fresh.

1. **Relocate the shards — never delete them.** `git mv` each one byte-identically to
   `<MEMORY_ROOT>/archive/ledger/<tag>.md`, and fold `IN-FLIGHT.md`'s protocol prose into
   `<MEMORY_ROOT>/archive/ledger/README.md`. Status content in those rows is redundant with git, but
   the shards are the ONLY carrier of worktree names, review ids and session narrative. Verify the
   move was a rename, not a delete-plus-add:
   `git log --follow -p --find-renames -- <path> | grep -m1 'similarity index'` → `similarity index 100%`.
2. **Take work state from the generated index instead.** `python tools/memory-tree/gen_build_index.py --write`
   renders `LIVE.md` and the `ledger/<month>.md` shards from each build's `README.md` front matter plus
   every spec's `**Status:**` header. Nothing about work state is authored after this, so nothing about
   it can rot.
3. **Front matter is the prerequisite, and it is per build.** `slug` · `node` · `opened` · `streams` ·
   `roster` · `ids` are ALL REQUIRED on every `builds/<slug>/README.md`. `status:` is required *only*
   when no spec under that build carries a parseable `**Status:**` header; a `status:` key alongside a
   spec that does carry one is a HARD ERROR, because that is two answers to one question. A build with
   no README front matter is invisible to the index — it does not fail loudly, it simply does not
   appear.
4. **Budget it as its own unit.** Measured on the one adopter on this node (`swydee`): kit 1.4, a
   pre-flatten tree, three live ledger rows, no `LIVE.md`, no `ledger/`, and **zero** build READMEs
   carrying front matter. For that repo the migration is a flatten plus a front-matter backfill across
   every build folder, then step 1 — its own work unit in its own repo, not a step in this runbook.

Then re-pull §3, §5 and this kit's handling per the playbook's v2.4 banner, and drop any ledger row,
pointer stub or self-prune rule from your kickoff manifest (§4) and your instantiated playbook (§2).

<!-- govkit:entry codebase-map -->
## 3b — Adopt the codebase-map kit (if chosen in §0)

1. Copy the kit dir into the project as a directory **named `codebase-map`** (the fixed name the
   gate template resolves — don't rename): `cp -r <gov-repo>/tools/codebase-map <project>/tools/codebase-map`.
   The NAME is fixed and the prefix is ONE segment: `test_codebase_map.template.py` resolves the kit
   at the root, at `<x>/codebase-map`, and nowhere deeper, and `adopt-codebase-map.sh` refuses a
   two-segment prefix before writing anything. `tools/` is the declared prefix for every kit here.

   **Then delete the GOV-ONLY file that copy brings with it.** `kit.toml` withholds it from
   `govkit apply`, but a `cp -r` does not read `kit.toml`, so this path needs its own step:
   ```bash
   rm -f <project>/tools/codebase-map/{replay-phrases.py,rank_harness.py,scen-adversarial.json,adopt-codebase-map.test.sh,selftest.py,test_codebase_map.py}
   ```
   All three are gov's own grading instruments. `replay-phrases.py` reads `memory/builds/**` for
   recorded probe phrases and the seam each spec's §10 names, and grades the ranker against that
   pair. `scen-adversarial.json` is 28 scenarios whose seams were established by reading THIS
   repo's code, and `rank_harness.py` is what scores a ranking against them. In your tree the first
   finds no such corpus and the last two grade a corpus you do not have — the same
   `memory/gotchas/pin-copied-from-another-corpus.md` shape the memory-recall fixture has. If you
   want the measurement, point an equivalent at YOUR records: `rank_harness.py` reads any scenario
   file carrying a `scenarios` array, so the instrument travels even though the set may not.
2. `cp <kit>/.codebase-map.conf.example .codebase-map.conf` and fill MAP_ROOT · GATE_FILE ·
   MAP_DIFF_CMD (per the §0 decisions). It lives at the project **root** whatever the kit's prefix:
   the kit walks up from its own directory looking for this file, and that is how it finds the root.
3. `cp <kit>/map_extractors.template.py <kit>/map_extractors.py` and declare the
   project's inventories — this is the real work; follow `<kit>/INVENTORY-DERIVATION.md`
   (prefer registry imports; fail-closed helpers; full extension sets; POSIX keys).
4. `<kit>/adopt-codebase-map.sh --scaffold` — scaffolds the map tree, seeds the shrink-only
   baseline from live inventories AND the shrink-only `affordance-exempt.toml` from existing
   dossiers (so the graced `## Reuse affordance` check never retro-reds the fleet), installs the
   gate at GATE_FILE and runs it once (green on a fresh seed, by construction). `MAP_PY` overrides
   the launcher; unset, the kit RUNS each candidate (`python3`, `python`, `py`) and takes the first
   that executes, because the Microsoft Store `python3` stub answers `command -v` and then exits
   9009 without running anything. A NEW dossier is never exempt — new work records its reuse decision
   (`seam: <id> — reuse for <need>; extend via <point>`, or `none — <why>`) or the gate reds.
   **DoR (before building):** run `python <kit>/reuse_lookup.py "<behaviour>"` (the
   behaviour→seam lookup, per `<kit>/reuse-lookup.agent.md`) to find an existing seam to
   wire through; list any layer with no symbol extractor in `.codebase-map.conf` `RECALL_DARK_LAYERS`
   so the lookup flags the gap instead of a falsely-confident "no seam fits".
   **DoD (at review):** run `python <kit>/map_diff.py <base>..<head> --drop-affordance-exempt`
   — touching a graced feature's files drops its `affordance-exempt.toml` grace mechanically, so the
   gate then demands its `## Reuse affordance` block (no human remembering). Also run
   `python <kit>/map_diff.py <base>..<head> --converge` (the closing loop) — it WARNs on each
   NEW export that resembles an existing high-fan-in seam of the same kind it did not wire through
   (shipped reinvention, over ALL new code) and routes each to
   `<git-common-dir>/codebase-map/reinvention-backlog.md` (deduped) — OUTSIDE your worktree, so a
   `--converge` run never leaves untracked clutter in a gated directory; it falls back into
   `<MAP_ROOT>/` only where git cannot answer at all. A run that finds a pre-2026-09-06 file at the
   old location NAMES it and deletes nothing. It is a report + WARN, never a merge gate (a
   token-stem collision has false positives).
   To converge the active surface up front, `python <kit>/gen_map.py --seed-affordances --top
   <N>` lists the N highest-fan-in seams no dossier yet declares as the backfill worklist.
   Both CLIs read only committed artifacts, so nothing fails closed for them: each exits **2** with
   a refusal when the resolved root carries no `.codebase-map.conf`. Treat that as "not adopted /
   wrong tree", never as "no seam fits" — the refusal names the root it resolved and the kit dir.
5. Verify the project's test suite COLLECTS the gate (run the suite; the map tests must appear) —
   for a Python repo that is the entire CI wiring: zero pipeline changes by design.
   **Non-Python repo** (no pytest/py collector to discover the `.py` gate): wire it as an explicit
   leg instead — add `python <GATE_FILE>` (the gate's `__main__` runner; `${MAP_PY:-python}` if the
   launcher differs) to BOTH your CI config and your local gate runner, grep-guarded so a re-run
   doesn't duplicate the leg. Without this the freshness/coverage ratchet silently never runs.
6. Fill the manifest's "Codebase map" section (§4) and keep the playbook's map DoR/DoD lines (§2).
7. Commit `<kit>/ .codebase-map.conf <GATE_FILE> <MAP_ROOT>/` as one landing.

<!-- govkit:entry memory-recall -->
## 3c — Adopt the memory-recall kit (if chosen in §0)

Retrieval over the §3 tree: `query.py` indexes the corpus offline (stdlib only, no network, nothing
written inside the worktree) and answers a plain-English question with the records that bind it. It
declares no config of its own — it reads `.memory-tree.conf` for the corpus root and the id families,
and **refuses** when that file is absent, printing a two-key stub to paste. It never creates one;
memory-tree owns that file, which is why §0 makes this decision depend on §3.

1. Copy the kit dir in **as `tools/memory-recall/`**. The kit dir's NAME is load-bearing; the prefix
   is not — `adopt-memory-recall.sh` derives its own with `git rev-parse --show-prefix` and
   `check-wiring.sh` probes both spellings — but `tools/` is what this runbook declares, and
   `corpus_ids.py` needs memory-tree and memory-recall to be SIBLINGS, so they move together:
   `cp -r <gov>/tools/memory-recall <project>/tools/memory-recall`.

   **Then delete the three GOV-ONLY files that copy brings with it.** `kit.toml` withholds them from
   `govkit apply`, but a `cp -r` does not read `kit.toml`, so this path needs its own step:
   ```bash
   rm -f <project>/tools/memory-recall/{check-recall.py,recall-fixture.json,test_recall_floor.py}
   ```
   They are gov's recall floor: a question set keyed on gov record ids, the gate that grades it, and
   its arms. A question set from another corpus grades nothing in yours, and a floor copied from one
   is `memory/gotchas/pin-copied-from-another-corpus.md`. Keeping them is loud rather than silent —
   `check-recall.py` refuses with `RECALL_FLOOR is not declared` — but it is still a file you did not
   ask for. If you later want a floor, author your own fixture and MEASURE your own value.
2. Render the Skill from the conf and prove the index sees your ids. The Skill's `description` is the
   whole trigger mechanism and it names project values (id families, query path, corpus root), so it
   is GENERATED, never shipped:
   ```bash
   cd <project>
   bash tools/memory-recall/adopt-memory-recall.sh --scaffold   # -> .claude/skills/memory-recall/SKILL.md
   # One throwaway record first: §3 step 2 scaffolds DECISIONS.md files that are header-only,
   # so a fresh tree has NO id for the record arm to anchor and this step cannot pass without
   # one. `<FAM>` is one of YOUR families; the corpus is tracked-only, hence the `git add`.
   echo '- <FAM>-aSeed-1 · a throwaway record, delete after this step' >> memory/DECISIONS.md
   git add memory/DECISIONS.md
   python3 tools/memory-recall/query.py "why is <X> the way it is" --terms "8-14 words in YOUR jargon"
   ```
   The header must now report **at least one record** — the seed. `index 0 records + N chunks`
   plus a `ZERO RECORDS` block on stderr has TWO causes and the block names both: no decision
   has been written yet, or `FAMILIES` matches no id in the corpus. On a freshly scaffolded tree
   the first is the expected state and not a bug — the seed record is what tells the two apart.
   With it staged, zero records means `FAMILIES` — fix the conf and re-run (the cache keys on the
   resolved conf, so the repair is not silently served from cache). Delete the seed when green.
3. **Wire both gates — without this the skill-drift check silently never runs.** Add them to the
   project's local gate runner **AND** its CI config, grep-guarded so a re-run doesn't duplicate the
   leg:
   ```bash
   python3 tools/memory-recall/selftest.py                   # kit contract: conf-vs-bash parity, the refusals,
                                                       # cache freshness + eviction, writes-nothing-by-path
   bash tools/memory-recall/adopt-memory-recall.sh --check    # the rendered SKILL.md still matches the conf
   ```
   The `--check` leg resolves its own interpreter by RUNNING each candidate (`RECALL_PY` first if
   set, then `GOV_PYTHON`, then `python3`, `python`, `py`), so a `python3`-only adopter needs no
   extra step — a gate runner that rewrites `python`
   in a leg's argv provably cannot reach this leg, whose first token is `bash`.
4. **Optional, and separately: the `recall-opened` hook.** It records which hit actually answered a
   query (PostToolUse on `Read`, bounded 128 KB log tail, never blocks the tool). Only if wanted:
   ```bash
   mkdir -p tools && cp <gov>/tools/settings-merge.py tools/    # the merge tool — nothing else copies it
   bash tools/memory-recall/adopt-memory-recall.sh --scaffold --with-hook   # the hook already ships in the kit dir
   python3 tools/settings-merge.py --fragment tools/memory-recall/recall-opened.fragment.json
   ```
   The copy is not optional plumbing: nothing else delivers that tool, so without it the merge dies
   with errno 2. Run the two in this order — `settings-merge.py` refuses to wire a hook whose script
   is not there, because settings would then dispatch `node` against nothing on every `Read`.
   Declining the hook is a supported end state, not a gap: with no hook file and no settings block,
   `check-wiring.sh` prints a `skip … opt-in not taken` line. Copying the hook and skipping the merge
   is the one bad state — it prints UNWIRED at every session start until you merge it, and so does
   the reverse (a settings block whose script has gone missing).
5. Commit `memory-recall/` + `.claude/skills/memory-recall/SKILL.md` (+ the hook, `tools/settings-merge.py`
   and the settings block if step 4 was taken) as one landing.

<!-- govkit:entry lexicon -->
## 3f — Adopt the lexicon kit (if chosen in §0)

A closed verb table every definition leads with, a banned type-suffix list, and a (language,
surface) case-convention matrix. Opt-in: with no `.lexicon.conf` the engine reports NOT ADOPTED and
exits 0, so an installed-but-undeclared kit is a legal state rather than a red.

1. Copy the kit dir into the project as a directory **named `lexicon`** (don't rename):
   `cp -r <gov-repo>/tools/lexicon <project>/tools/lexicon`. The name AND the one-segment
   `tools/` prefix are both load-bearing here: `codebase-map`'s `lexicon-verbs` inventory resolves
   the kit at `<root>/tools/lexicon` to borrow its conf reader, so a kit installed anywhere else
   yields an empty verb inventory rather than an error.

   **Then delete the GOV-ONLY GRADING INSTRUMENTS that copy brings with it.** `kit.toml` withholds
   them from `govkit apply`, but a `cp -r` does not read `kit.toml`, so this path needs its own step:
   ```bash
   rm -f <project>/tools/lexicon/{selftest.py,ts-conformance-fixtures.json}
   ```
   Both grade the KIT, not your tree. `selftest.py` stages breaks into copies of the checkers in
   this directory and asserts the checkers still catch them, which has a job only when the kit's own
   source changes and none at all in a tree that copy-installs it. `ts-conformance-fixtures.json`
   holds bounded, provenance-stamped excerpts of a THIRD-PARTY TypeScript tree, drawn to score this
   kit's TypeScript reader — `selftest.py` is its only reader, so shipping it onward would be a
   disclosure of somebody else's source with no consumer at the far end.
   **Delete nothing else.** `SKILL.template.md` is withheld from `apply` too, and it must SURVIVE a
   copy-install: it is the file step 3 renders the adopter's Skill from. Delete it before rendering
   and `--check` prints `not installed, nothing to render` and grades nothing; delete it AFTER, and
   `--check` reds with `cannot verify drift` — neither is a state you want. The two waiver registries ship as
   empty headed files and are yours to fill. The `codebase-map` section above omits
   `map_extractors.py` from its own `rm -f` line for the same reason.
2. `bash <project>/tools/lexicon/adopt-lexicon.sh --scaffold` — DERIVES a proposed verb table
   (which concepts are live in YOUR corpus; each verb's SPELLING from the kit's frozen canon, never
   from your identifiers), seeds the `LANGS` and `CELLS` rows for the extensions it recognises,
   MEASURES both offender pins against your tree, writes `.lexicon.conf` at the project root and
   renders the Skill.
3. **Curate the seed, then stamp it.** The seed lands marked PROPOSED with an empty `ratified` key
   and `--check` reds while that key is empty, so an uncurated table cannot reach your merge bar
   disguised as a vocabulary. Write the NEGATIVE definitions your domain needs (`LEXICON.md` is the
   authoring guide), delete rows you did not mean, arm or leave `dark` each `CELLS` row, then set
   `ratified="<date> node <tag>"`. Re-render with `--render` after any conf edit; the wiring check
   byte-compares, so an edit nobody re-rendered reds.
4. `bash <project>/tools/lexicon/adopt-lexicon.sh --check` — the drift mode, green when the conf
   parses, the stamp is present and the Skill is in sync. `govkit apply` emits two gate legs
   (`lexicon naming predicates`, `lexicon wiring`), and so does `govkit update --write`; a `cp -r`
   install wires them into your own gate runner by hand.
5. Commit `tools/lexicon/`, `.lexicon.conf`, the two waiver registries and
   `.claude/skills/lexicon/SKILL.md` as one landing. Pin the Skill to LF — it is a rendered artifact
   its own gate byte-compares.

## 4 — Write the kickoff manifest (the engine's project layer)

The engine (§1) discovers the manifest by searching `<project>`, **first hit wins**:
the locations `bash tools/manifest-check.sh --locations` prints, in order →
`SESSION-KICKOFF.md` → else it greps `docs/` + root for the `governance-template:` marker (the playbook
from §2). Write the manifest to one of those paths so it resolves.

1. Instantiate it:
   ```bash
   mkdir -p <project>/memory/guides   # or whichever dir --locations names first
   cp <gov>/skills/session-kickoff/MANIFEST-TEMPLATE.md <project>/memory/guides/SESSION-KICKOFF.md
   ```
2. Fill **§B (orientation)** from the repo: repo layout · remote + default branch · branch conventions ·
   governing docs · the **path to the playbook from §2** · the pointer map (area → doc → entrypoints) ·
   the gate commands · the tier rule · the **ID protocol** (id format + slug rules + collision grep +
   where work state is READ from, e.g. the generated `memory/LIVE.md`) · the environment traps. Fill the
   **`manifest-audit` block** per the template's Customize notes: `watch` = the pathspecs the gate/layout
   claims derive FROM (never lockfiles; ≤~8); `verify-paths` = the 2–3 tracked anchors; stamp
   `last-audit` = ISO-8601 datetime with offset (e.g. `date -Iseconds`) `@` full sha per the stamp
   rule those notes state; `registry` = the repo-relative file whose first table
   under `## Node registry` names the project's nodes (the charter from §2 when the playbook is
   adopted) — the checker's `--card` verbs resolve the session's node from its Machine/user
   column; tag claims whose truth lives in another repo
   `(cross-repo — verify at use)`. Keep it SHORT — only what the engine can't derive from
   git/`CLAUDE.md`; reference the playbook, never duplicate it. (§A is derived by the agent per
   kickoff — leave it as the shape, don't fill it.)
3. Delete the "Customize before use" block.
4. **Wire the ratchet gate:**
   ```bash
   mkdir -p <project>/tools && cp <gov>/skills/session-kickoff/manifest-check.sh <project>/tools/
   ```
   (Non-default home → record it in the block's `check-script:` and adjust every path below.) Append
   `tools/manifest-check.sh text eol=lf` (or a repo-wide `*.sh text eol=lf`) to the project's
   `.gitattributes` — the gov repo's EOL rules don't travel with `cp`, and a CRLF checkout kills bash
   silently. Keep the template's standing gate-fence line pointing at the checker. Then `git add` the
   manifest, the checker, and `.gitattributes` — the checker tests TRACKED-ness; an unstaged fresh
   adoption cannot pass.
5. **Offered hardening (each optional, separately):**
   - pre-commit leg, guarded like the memory-tree hook so a scripts-less checkout stays green — note
     it deliberately narrows the drift remedy to "bundle the re-stamp into THIS commit":
     ```sh
     top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
     if [ -f "$top/tools/manifest-check.sh" ]; then bash "$top/tools/manifest-check.sh" --staged || exit 1; fi
     ```
   - CI leg: run `bash tools/manifest-check.sh` in a job whose checkout uses **`fetch-depth: 0`** —
     MANDATORY, not advisory: the actions/checkout default (depth 1) makes the drift check
     WARN-and-skip on every run, so a shallow CI leg never enforces the one check that matters.

**Verify:** `grep -nE '\{\{[A-Z]' <project>/memory/guides/SESSION-KICKOFF.md` prints nothing, and
`cd <project> && bash tools/manifest-check.sh; echo $?` → `0` (the checker resolves the repo from
the INVOKING directory, not from its own location — run it with the cwd inside `<project>`).

**Retrofit an existing v1.0 manifest** *(the durable recipe — the checker's C2 failure points here)*:
1. **Body deltas first:** rewrite the §B intro/heading to the current wording ("derived at
   instantiation; re-audited every kickoff; accretes"); insert the template's ratchet section; insert
   the dated-corrections section (empty — prunable per-entry, never deleted); add the traps-accrete
   note. Without this the file keeps its standing freeze directive and the older in-file contract wins.
2. Insert the `manifest-audit` block (derive `watch`/`verify-paths` as in step 2 above; tag cross-repo
   claims; stamp only AFTER actually re-verifying §B).
3. Copy the checker + `.gitattributes` line + gate-fence line; `git add` everything (step 4 above).
4. `bash tools/manifest-check.sh` → 0.
5. Re-pull the playbook's §1 manifest lines (DoD write-back + Landing reconcile exception) into the
   project's instantiated playbook, and bump its `governance-template:` marker to the version you
   actually pulled FROM — read it out of `<gov>/coding-governance-agents.template.md`, never from
   this line. Stamping an older number on a newer copy makes the marker lie, and the marker is what
   both the kickoff engine's Step-2 fallback and the re-pull mechanism read.
5b. Add `registry: <path>` to the audit block (v1.4) — the file whose first table under
   `## Node registry` names the project's nodes, read by the checker's `--card` verbs for the
   session card's `node —` cell. Without it every card the project writes reads `node — UNKNOWN:
   no registry`, and nothing else fails: the key is what the version WARN is now for.
6. Bump the manifest marker to `kickoff-manifest: v1.4` **LAST** — the bump silences the kit's
   format WARN, the only standing signal that the body still predates the ratchet. The WARN compares
   the marker with the checker's `MANIFEST_FORMAT`, never with `KIT_MANIFEST_VERSION`: that one is
   the kit's vintage and moves whenever its bytes do, with no upgrade step owed.

<!-- govkit:entry push-main -->
## 5 — Optional: worktree tooling + SessionStart nudge

Optional for any pytest project: adopt `tools/pytest-parallel-guardrails/` (bounded + attributable
`pytest-xdist` runs; aiosqlite suites also get the closed-loop seam patch + its regression gate) —
adoption steps in that kit's README; no wiring beyond the adopter's own `pyproject.toml`/conftest.

Only if the project runs multiple nodes/worktrees (playbook §3):
- A `new-stream` script (sibling worktree on a fresh branch off fast-forwarded `main` + dependency
  install) → fill `{{WORKTREE_SCRIPT}}`.
- The tracked pre-commit **branch guard** (refuse a primary-tree commit while off the default branch).
  coding-governance ships a portable reference block in its own `.githooks/pre-commit` (default branch
  derived from `origin/HEAD`, else `main`; pin via `GOV_DEFAULT_BRANCH`; only fires in the primary tree,
  not linked worktrees; red/green self-test `.githooks/pre-commit.test.sh`) — copy that block into the
  project's pre-commit. For a multi-worktree project, also add a per-machine install that points
  `core.hooksPath` at an **out-of-tree copy** under `$(git rev-parse --git-common-dir)`, so a branch that
  lacks `.githooks/` can't render the guard inert.
- Optionally a SessionStart hook that nudges `/session-kickoff` and reports `git worktree list` state.

**Wiring-health self-heal (recommended for ANY project — a fresh clone starts with hooks dormant):**
- Copy `tools/check-wiring.sh` (+ `tools/check-wiring.test.sh`) into `<project>/tools/`. It detects
  coding-governance tools installed-but-unwired — chiefly `core.hooksPath` not resolving to `.githooks`,
  which leaves every pre-commit gate (incl. the branch guard) dormant on a fresh clone — and prints the
  fix. `--fix` wires the zero-risk hooks case; `--session` does the same but always exits 0.
- Wire the SessionStart hooks through the merger, never by hand — each is a fragment beside the
  script it runs, and every one carries a MATCHER, because an entry without one runs on every
  compaction (measured 35–81 s per compaction for the wiring check alone):

  ```bash
  python "$KIT/settings-merge.py" --fragment "$KIT/check-wiring.fragment.json"          # startup|resume|clear
  python "$KIT/settings-merge.py" --fragment "$KIT/process-monitor/procmon-session.fragment.json"   # same, if adopted
  python "$KIT/settings-merge.py" --fragment "$KIT/orientation-card.fragment.json"      # startup|clear — writes the card
  python "$KIT/settings-merge.py" --fragment "$KIT/orientation-replay.fragment.json"    # resume|compact — replays it
  bash "$KIT/check-wiring.sh" --check                                                   # `ok card`, or which half is missing
  ```

  The merger RE-MATCHES: an entry already in the file under no matcher, or under a different one,
  is moved under the fragment's matcher rather than duplicated, so a tree wired by hand before this
  step migrates by running the same four commands. `check-wiring.sh --session` auto-sets an unset
  `core.hooksPath` and NEVER overwrites a deliberate value (e.g. the out-of-tree copy above), so a
  fresh clone self-heals. The two `orientation-*` fragments ship with the kickoff-manifest kit
  (beside `manifest-check.sh`), and the card they write is what `scratch-guard.js` reads before it
  lets a `git commit` through — read that deny's ceiling in the hooks README before relying on it.
- Add `bash tools/check-wiring.test.sh` as a gate-runner leg. Do NOT run `check-wiring.sh --check` itself
  as a merge-bar leg — it would false-fail in CI, where `core.hooksPath` is correctly never set.
- **Land the default branch via `tools/push-main.sh`** (TOOL-aLeasedGauntlet-1): it fetch-reconciles
  origin BEFORE the pre-push gate so the ~min gate never runs on a stale tree, and bounds a during-gate
  remote race at `GOV_PUSH_MAIN_MAX_RETRIES` (default 3). The `pre-push` hook refuses a raw default-branch
  push that bypasses it (a local marker; `--no-verify` bypasses). Add `bash tools/push-main.test.sh` as a
  gate-runner leg (the lander self-test).

**Also copy, if you want the gates this repo runs on itself** (each is a leg, none is wired for you):

- `tools/check-kit-versions.sh` — asserts every kit's version constant and its doc marker agree, which
  is what makes an installed kit's version detectable at all. Edit its `need` list to your kit subset;
  it is a hardcoded list by design, not an enumeration. If your project ships kits onward, the rule
  that goes with it is that **a kit whose shipped bytes move bumps its version**: gov grades it with
  the deployer's `govkit.py epoch` verb, which reads gov's registry and history and so stays in gov.
- `tools/gate-lint/` — the gate-authoring lints. It ships no legs of its own; its README hands leg
  wiring to the consuming project.
- `tools/push-main.sh` + `tools/push-main.test.sh` + `.githooks/pre-push` — §5 already tells you to
  LAND through the lander, and nothing above copies it in. Do that here.
- `tools/check-install-prefix.sh` + `tools/check-install-prefix.test.sh` — only if your project also
  ships kits onward. It polices the SHIPPING surface, not an installed one.

**Concurrency guard (recommended for ANY project that fans out `Workflow` agents — playbook §8):**
- Copy `tools/hooks/agent-cap.js` (+ its `.test.sh` sibling) into the project **under the same kit
  prefix as your other kits** — `<project>/<prefix>/hooks/`, so `<project>/tools/hooks/` in a
  default install. **NOT `<project>/.claude/hooks/`**, which this runbook prescribed until
  TOOL-dRetiredFork-14/21 withdrew that destination: the wiring check now expects the hook beside
  the kit that ships it and reports a `.claude/` copy as a legacy one.
- Wire the `PreToolUse` hook into `.claude/settings.json` idempotently (from the project root):
  ```bash
  python <gov>/tools/settings-merge.py    # merges/creates .claude/settings.json; re-run = no-op; `--check` verifies; backs up to settings.json.bak on change
  ```
  It inserts the block below (a hand-merge works too):
  ```json
  "PreToolUse": [ { "matcher": "Workflow|Agent", "hooks": [ { "type": "command",
    "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\"" } ] } ]
  ```
  The matcher is a LIST OF EXACT STRINGS separated by `|`, in ONE group — not a regular expression,
  and not two blocks. `Workflow` is where the hook reads a script; `Agent` is the direct-spawn
  modality, which carries no script and is COUNTED instead: each spawn claims a numbered slot with
  `O_EXCL` under a session+prompt-keyed directory in the git common dir (`<common>/agent-cap/`, so
  git never tracks it), and the budget resets on the next user prompt. `tools/check-wiring.sh` asserts
  this matcher VALUE, not merely that the file mentions `agent-cap.js`: a group left at `Workflow`
  alone contains the string and used to report ok.
  It DENIES any `Workflow` script that calls raw `parallel(`/`pipeline(` instead of the bounded
  `boundedParallel`/`boundedPipeline` helpers, and it READS the number: the cap argument at each call
  site, the helper's own default parameter, and the width a `gov:bounded-fanout` line claims. The 5 is
  a file constant — there is no environment override, and a set `AGENT_CAP` is refused with a message
  rather than silently ignored. This is the
  mechanical enforcement of the review protocol's TWO rules: route fan-out through the bounded
  helpers, AND a review's verify stage spawns at most the total the hook resolves. A wide fan-out
  trips the server rate
  limiter. The binding rules ship as `tools/workflows/REVIEW-PROTOCOL.template.md` — install it at
  `<MEMORY_ROOT>/guides/REVIEW-PROTOCOL.md` (the path `check-protocol-parity.test.sh` treats as LIVE)
  and cite THAT copy from your manifest, not this runbook.
- Copy the kit dir in as `<project>/tools/workflows/` for a ready consolidated review harness
  (`tier2-review.js`): four finder lenses, then at most five BATCHED verifiers, then one synthesis
  pass — 6–10 agents over the whole run, all within the verify-stage and concurrency bounds
  `tools/hooks/agent-cap.js` resolves.
- Then run `bash <project>/tools/workflows/check-protocol-parity.test.sh --render` once. The kit
  ships the unattended build harness as `unattended-build.template.js`, and this writes
  `unattended-build.js` beside it with your install paths filled in, and the protocol copy with it.
  A copied template with no render is a harness that does not exist. When the memory-tree kit's
  `gotchas.py` is tracked at neither `<tool root>memory-tree/` nor `<tool root>`, the render SKIPS
  the harness out loud, by name, and still renders the protocol; export `MEMORY_TREE_DIR=<dir>` if
  yours lives elsewhere, and an override naming nothing tracked is refused.
- Verify all five workflow legs, not two — the dogfood bar runs every one of these:
  `bash <project>/.claude/hooks/agent-cap.test.sh` · `bash <project>/tools/workflows/check-protocol-parity.test.sh` ·
  `bash <project>/tools/workflows/check-verifier-fanout.sh` · `bash <project>/tools/workflows/check-review-join.sh` ·
  `node <project>/tools/workflows/check-workflow-syntax.js` — each → exit 0.

## 5b — A tree that already carries kits: bootstrap its receipt (`adopt`)

Everything above is the FRESH path — a project with no gov bytes in it, where `apply` lands the files
and writes the receipt as it goes. This section is the other one: a repository somebody already
vendored kits into by hand, which has no `.governance/install.json` and therefore cannot be updated
at all. `update` refuses without a receipt, by design, so such a tree is stuck until one exists.

`adopt` writes it, by MEASURING the tree against gov's own history. It puts no byte into the working
tree — one file under `.governance/`, and `install.sums` beside it — and it is read-only until
`--write`.

```bash
python <gov>/tools/govkit/govkit.py intake --target <project> --kits a,b,…   # the descriptor, once
python <gov>/tools/govkit/govkit.py adopt  --target <project>                # READ-ONLY: read this
python <gov>/tools/govkit/govkit.py adopt  --target <project> --write        # then record it
python <gov>/tools/govkit/govkit.py update --target <project>                # now the tree is live
```

**Read the read-only run before you write it.** Each destination prints with its role and what the
walk found, and the tally at the end is the answer to "is this tree adoptable":

- `verbatim` — the target holds gov's bytes exactly. Nothing to explain.
- `eol` / `relocate` — the bytes differ for a reason gov already knows about: a CRLF checkout, or an
  install at a `prefix` other than the default. Both are PROVEN per row on every run, never read back
  off the receipt.
- `unattributed` — no gov vintage explains these bytes. The row is recorded with no base, and every
  later `update` prints it and writes nothing to it. This is a REPORT, not a failure: partial
  attribution is the normal state of a hand-vendored tree, and a bootstrap that demanded totality
  would bootstrap nothing.
- `forked` — the descriptor declares gov's copy a derivative of the target's. Report-only in both
  directions, whatever the walk found.
- `not-installed` — a destination the kit would write and this target does not track. No row.

**`--pin <path>=<rev>` is how an operator corrects one row**, and only one: it fixes that
destination's base by assertion, and the row records `evidence: "pinned"` so an assertion is never
read back as a proof. Repeat the flag per path. Use it on an `unattributed` row you know the vintage
of; a wrong pin makes a later merge noisier and never destructive, because the raw-write arm stays
closed wherever the two identities differ.

**`--re-adopt` re-measures from scratch** and is the only way past the refusal over an existing
receipt. It preserves nothing the old one recorded — not the commit, not the rung, not the role,
which is re-read from the descriptor on every run anyway.

**The three refusals**, so you can tell them apart from a bug: `--target` resolving to the gov
checkout itself; an existing `install.json` without `--re-adopt`; and a target index that differs
from HEAD. That last one is the INDEX only — an unstaged edit in your own worktree does not block,
because `adopt` reads identities out of the index and writes nothing you could lose.

### One thing `apply` will refuse to hand you

A kit can declare a gate leg whose argv runs an engine gov does not actually ship — and until this
was gated, `apply` would emit that leg into your runner and record it in the receipt as coverage for
a check that can never run. It now names the kit, the leg and the offending path, withholds THAT leg
and emits the rest, and exits 1. **The install still stands and the receipt is still written**: the
condition is a defect in a gov-authored descriptor, not something you can fix in your own tree.

`plan` previews the same condition, over what you already track plus what the plan itself would
write — so a first install is not warned about being new.

If you see one, it is gov's to fix: either the leg is withdrawn or the file starts shipping.

### The leg rows gov emits are gov's to rewrite

A gov-side change to a leg — a new `argv`, a different guard — is a new vintage and is **delivered**,
not refused, however far it has moved from what you hold. Do not answer a newly red leg by editing
its row in your own manifest: that row's NAME is one the receipt claims, so the next `apply` or
`update --write` compares your row against what the receipt records, reports drift naming the leg,
and withholds the whole manifest rather than writing half of it against a file it cannot grade. Put
the row back as gov wrote it, and take the argument you wanted through the leg's own flags or through
a leg of your own under a name gov does not emit.

### Before any of that: how much of each kit did this tree actually take?

`adopt` measures the files a target HOLDS. It says nothing about the ones it never took, and the
only signal this engine had for that was whole-kit — `update`'s `available (not installed)` line,
which needs the receipt you are trying to create. So a tree that took 80 files of a kit and left 20
read exactly like one that took all 100.

`plan --coverage` is the read-only join that answers it, and it needs no receipt — only
`.governance/deploy.toml`:

```bash
python <gov>/tools/govkit/govkit.py plan --target <project> --coverage --kits a,b,…
python <gov>/tools/govkit/govkit.py plan --target <project> --coverage --emit-declines --kits a,b,…
```

**Pass `--kits` deliberately.** The selection resolver branches on `--all`, `--kits` and the
registry's own default set, and it never reads `deploy.toml`'s `kits` — so the same command without
the flag answers a different question, correctly. Ask the one you meant.

It prints one `GAP` row per missing planned write, naming the kit and the gov source it came from,
then a per-kit tally and a total. `gap 0` prints out loud: a clean run that printed nothing is
indistinguishable from a check that never ran. **A gap never changes the exit code** — it is a state
of the world, not a fault in the run.

**Coverage answers PRESENCE only.** A file the target holds and has hand-edited reads as covered
here; that is what `adopt`'s two identities measure instead. And a file the target took under a
different name reads as absent, because rename detection for coverage is a stated non-goal —
`--emit-declines` prints paste-ready `[[decline]]` skeletons to STDOUT, one per gap row, for you to
paste into `deploy.toml` yourself. It never opens that file: a deployer that edits the document
carrying your decisions has made one for you.

### Saying "we deliberately did not take that" — the `[[decline]]` contract

A coverage report with no way to record a deliberate omission is one you read once. The rows you
chose not to take keep being named, the run starts crying wolf, and the only way to quiet it is to
stop running it — which loses the whole signal.

A `[[decline]]` block in the target's own `.governance/deploy.toml` records the decision. It is
graded on every run, and it dies when the world moves underneath it, which is the difference between
a declaration and a fork with a friendlier name.

```toml
[[decline]]
kit  = "review-harness"
dest = "scripts/review-harness/tier2-review.js"
why  = "we vendored this kit under .claude/workflows/ years before adopting gov"
taken_as = ".claude/workflows/tier2-review-indexed.js"   # at most ONE evidence field
```

`kit`, `dest` and `why` are required. **`why` is graded for EXISTENCE only** — grading prose is how
a gate starts lying, and every content predicate is satisfiable by typing something.

**At most one evidence field**, from three: `taken_as` (gov's bytes live at this path instead —
hash-graded against gov's blob, CR-stripped, so a CRLF checkout is not a different file);
`consumed_into` (folded into this tracked file — deliberately weak, because gov cannot know what a
fold means byte-wise); `discharge = { command = [...] }` (this probe proves it is handled, exit 0).
Two evidence fields on one row is two rows, and it reds before either is evaluated.

**A `taken_as` mismatch is not a failure.** The row reclassifies to `diverged`, keeps its reason,
and the run's exit code does not move. Redding it would red the honest adopter who relocated a file
and then edited it, whose only route back to green would be deleting the decline.

**Three staleness arms red, and they are the point.** An empty `why`. A `dest` the target now
tracks — the file arrived, so delete the row. A `dest` no claimed kit ships any more — gov withdrew
it, so delete the row. A row that reds excuses nothing, so a stale decline can never hide a gap.
Both `check` and `plan --coverage` run the same predicate: a decline may only hide a gap row in a
run that also grades it.

Declined rows PRINT, with their state and their reason. A gap that vanishes from a report without
saying why is the failure mode of every exclusion list.

### Recording a kit file you deliberately EDITED — the carve-out ledger contract

A `[[decline]]` records a kit file you did not take. This records one you took and then changed:
a **carve-out**. The two are different questions and want different registers, because a declined
file has no bytes to grade and a carved-out one has bytes that must never be silently overwritten
by the next `update`.

**The contract, in three rules.** Each exists because the obvious design fails, and the failure is
named rather than left for the adopter to rediscover.

1. **The id carries NO denominator.** Tag each site `carve-out <stable-id>` — a number, a slug,
   anything stable — and never `<n>/<total>`. A tag encoding the population size means retiring
   ONE carve-out requires editing every other tag in the tree, so the cheapest operation in the
   whole retirement programme is also the one that touches the most files. Adopters do not do
   expensive things; they leave the carve-out in place.
2. **The population lives in ONE tracked registry**, not in the tags. The tags say "this site is
   carved out"; the registry says how many there are and what each is for. A count derived by
   grepping the tags is a count that changes whenever somebody adds a comment, and a count typed
   into a document is wrong on the next commit.
3. **The guard asserts the registry is READABLE, never that it is NON-EMPTY.** This is the rule
   that decides whether the programme can ever finish. A guard written as "fail if zero
   carve-outs found" reds the moment the last one retires — it makes SUCCESS indistinguishable
   from a broken probe, so the tree can never reach the state the programme exists to produce.
   The anti-vacuity instinct behind it is right and must be kept; it just has to point at the
   registry rather than at the count.

**What rule 3 is protecting, because it is worth keeping.** A census that greps for its own
subjects can be scoped so narrowly that it reaches none of them and reports a clean run. That has
happened twice in the field, both times letting a real regression through a green bar. So the
guard still has to prove it could have found something. It proves it against the REGISTRY — which
is tracked, has a known path, and is readable or not — instead of against the tag count, which is
legitimately zero at the end.

```
# the guard, in shape:
[ -r "$REGISTRY" ] || fail "the carve-out registry is unreadable: the census cannot see its subjects"
declared=$(count rows in "$REGISTRY")
tagged=$(grep -rhoE 'carve-out [A-Za-z0-9_-]+' $ROOTS | sort -u | wc -l)
[ "$declared" = "$tagged" ] || fail "registry has $declared rows, tree has $tagged tagged sites"
# declared == tagged == 0 is a PASS: the programme finished.
```

**Worked example — retiring one carve-out, touching only its own files.** A tree carries carve-outs
`cap-is-four`, `prefix-scripts` and `flat-index`. `cap-is-four` converges upstream, so it goes:

1. Delete the `carve-out cap-is-four` tag from each site that carries it, and take the upstream
   bytes. Only those files are touched.
2. Delete that one row from the registry.
3. Run the guard. Registry rows and tagged sites both fell by one and still agree, so it passes.
   **No other tag was edited**, because no other tag ever named the total.

Retire the last two the same way and the tree reaches zero carve-outs: registry readable, zero
rows, zero tags, guard green. Under an `N/M` scheme step 1 would have meant editing every
remaining tag in the tree, and the final state would have RED the bar.

**Migrating an existing `N/M` ledger.** One commit, and it is mechanical: rewrite each
`carve-out <n>/<total>` to `carve-out <stable-id>` (the old `<n>` is a fine id — it is already
unique and already grep-able), write the registry with one row per id, and repoint the guard at
the registry. Do it BEFORE retiring anything, or the first retirement pays the cost this contract
exists to remove.

### Saying "this program is ours, not gov's" — the `[[own]]` declaration

A carve-out is gov's file with your edit in it. Some trees hold something else under gov's
filename: a program written before gov wrote its own, with no gov vintage behind it. `adopt`
records such a file `unattributed`, and one `unattributed` row withholds the receipt's
`gov_commit` re-stamp on every `update`. Pinning it to the nearest vintage records a base its bytes
never came from. Declare it instead:

```toml
[[own]]
path = "scripts/gen_build_index.py"          # your file, repo-relative
implements = "memory-tree:gen_build_index.py" # <entry>:<gov source relative to the kit home>
why = "written before gov's, a parallel program"
```

Then run `govkit adopt --re-adopt --write`. The row is recorded `adopter-owned` with
`evidence: "declared"` and no gov vintage. After that:

- `update` counts it under `adopter-owned`, writes it in neither direction, and still re-stamps.
- `update` and `check` print one parity line per contract gov declares for that source, such as
  `contract memory-tree/corpus-ids <- scripts/corpus_ids.py: 1/2 clauses hold`. Each failing clause
  is listed with the gov file that needs it. A failing clause never reds, because you own the file.
  Two things change that. When the file that needs the clause is installed in your tree, its line
  says `INSTALLED CONSUMER CANNOT RUN`. When that installed file is also in the argv of a leg your
  receipt emitted, `check` reds.
- A hole whose probe would run gov's program against yours stands down and says so, for example
  memory-tree's `measured-pins` when you own `corpus_ids.py`.
- Your file may sit at a different path from gov's copy, as a stand-in. Gov keeps landing its own
  copy, and each run prints one line saying whether any emitted leg runs it.

`adopt` exits 1 and names the row when `path` carries anything outside the strict path class or
leaves the repository. It does the same when `implements` names a source gov ships as a seed, or
as rendered, generated, forked or project-owned, because each of those already says who owns the
bytes. It also exits 1 when the entry is not in your selection, and when your index does not track
`path`. The declaration is a bridge, not a fork: once your program converges onto gov's, delete the
row and re-adopt.

## 6 — Verify the whole chain, then commit

- Codebase-map (if adopted): `python <kit>/selftest.py` (kit contract) · run the gate file
  directly (`python <GATE_FILE>`) · `python <kit>/gen_map.py --check` (freshness) · make one
  throwaway inventory addition and watch the gate go red with the claim remedy, then revert. On a
  **non-Python repo**, also confirm the explicit `python <GATE_FILE>` leg is actually standing in
  your CI config + gate runner (§3b step 5) — not merely runnable by hand. Last, run
  `python <kit>/reuse_lookup.py "<any behaviour>"` and confirm the corpus line reports a NON-ZERO
  symbol/inventory count: a `corpus: 0 symbols` there means the root resolved somewhere unadopted,
  and every later "no seam fits" would be an answer from an empty population.
- Memory-recall (if adopted): `python3 tools/memory-recall/selftest.py` (kit contract) · one real query
  whose record arm anchors the §3c step-2 seed record (zero records with no decision written yet
  is the expected state, not a `FAMILIES` bug) · `bash tools/memory-recall/adopt-memory-recall.sh --check`
  → 0 · then edit `FAMILIES` in `.memory-tree.conf`, re-run `--check`, watch it go RED naming the
  drift, and revert. Confirm **both** legs are actually standing in your CI config + gate runner
  (§3c step 3) — a kit copied in beside a skill nobody rendered otherwise reads as fully wired.

1. **Kickoff resolves:** run `/session-kickoff` in `<project>`. The engine must find your manifest (§4)
   and surface the playbook + gate + ID protocol. If it can't, re-check the §4 search paths.
2. **Gate green** (if memory-tree adopted): `bash tools/memory-tree/check-memory-hygiene.sh ; echo $?` → 0.
3. **No stray placeholders:** `grep -rn '{{' <project>/docs/PARALLEL.md` → empty, and
   `grep -rnE '\{\{[A-Z]' <project>/memory/guides/SESSION-KICKOFF.md` → empty (the manifest check is
   shape-scoped: its gate fence may legitimately hold `${{ … }}` / Go-template braces).
4. **Commit the chain FIRST:** `cd <project> && git add -A && git commit` (do NOT commit the
   per-machine skill junction — it lives under `~/.claude`, not the repo). The probe below needs the
   chain COMMITTED — §4 leaves it only staged, and a probe commit that sweeps the still-staged
   manifest in would introduce the stamp and stay green instead of demonstrating red.
5. **Ratchet red/green probe** (the drift check reads COMMITTED ranges — an uncommitted touch is
   invisible; use a throwaway branch off the chain commit): *commit* a throwaway change to a watched
   file → `bash tools/manifest-check.sh` goes red (check 5) → re-stamp `last-audit` (bundled or
   follow-up commit) → green → **revert the throwaway AND the probe re-stamp together in ONE
   commit** → still green (a bare revert touches the watched file again and would end the wiring
   session red). If a CI leg was wired: push the probe branch and confirm the CI job actually reds —
   proof it isn't WARN-skipping on a shallow checkout. Then delete the probe branch.
6. **Work state generated, not authored:** `python tools/memory-tree/gen_build_index.py --check` → 0, and
   `memory/LIVE.md` exists. Nothing under `memory/project/` but the six `*.txt` waiver registries.

## 5c — Send a fix back: `contribute`

An adopter that fixes a gov defect in its own copy has, until now, held that fix privately: it gets
re-merged on every release, and gov keeps shipping the defect to everybody else. This build absorbed
eight such fixes by hand, one at a time, because there was no route. `contribute` is the route.

```bash
python tools/govkit/govkit.py contribute --target /path/to/adopter
```

It is **read-only in both directions**. It writes nothing to gov and nothing to the adopter; the
output goes under gov's own git dir, and the verb's acceptance includes the adopter's `git status`
being byte-identical before and after. It emits a patch set. A person lands it, through the merge
bar and the review protocol like any other change.

**What it looks at.** Only rows whose bytes appear in NO gov commit ever. A row that merely differs
from gov's current tip is an OLDER GOV VINTAGE — the adopter is behind, which is `update`'s job.
Proposing one of those would be proposing gov's own history back to it. Rows rendered from a gov
template are excluded and listed separately, because diffing a render against its template measures
the render.

**Every class is a PROPOSAL and none of it is a decision.** The report says so at the top, and the
reason is the failure that matters: a fact true only of one tree, taken as a gov defect, absorbed,
and shipped to every adopter as gov's behaviour. The four classes are gov defect, gov gap, project
fact and layout carriage; the first two carry a patch, the last two carry a reason and nothing else.

**A patch that does not apply is withheld, not shipped.** Each one is run through `git apply --check`
against the vintage it names before it is emitted, and a row whose patch fails is reported with that
fact — it means the map reached a wrong gov path, usually two unrelated files sharing a basename.

**The patches are untrusted content.** They are bytes from a foreign tree. Read one before applying
it.

## Result — what the project now has

```
<project>/
├── AGENTS.md / CLAUDE.md        # (optional) project charter / agent-instruction file (agent-instructions kit)
├── docs/PARALLEL.md             # governance playbook, filled (governance-template marker kept) — ONE file; §2 ships no companion
├── memory/guides/SESSION-KICKOFF.md  # kickoff manifest (v1.4: audit block + sealed §A region + registry key) — the engine reads this
├── tools/manifest-check.sh    # ratchet gate — engine-identical copy (overwrite wholesale on kit updates)
├── .gitattributes               # EOL rules — the checker (+ the memory tree if §3 adopted)
├── .memory-tree.conf            # memory-tree config           ┐
├── memory-tree/                 # the hygiene kit (copied in)  │ only if §3 adopted
└── memory/                      # scaffolded tree; LIVE.md = GENERATED work-state index      ┘
~/.claude/skills/session-kickoff # the engine (per-MACHINE junction/symlink — not in the repo)
```

- Codebase-map (only if §3b adopted): the `codebase-map` kit dir at whatever prefix you chose +
  project-owned `<kit>/map_extractors.py` · `.codebase-map.conf` at the ROOT · the gate at GATE_FILE ·
  `<MAP_ROOT>/` (FOUNDATION.md, baseline.toml, affordance-exempt.toml, features/, generated/).
- Memory-recall (only if §3c adopted): `memory-recall/` kit dir + the generated
  `.claude/skills/memory-recall/SKILL.md` (+ the kit's own `recall-opened.js`, `tools/settings-merge.py`
  and the settings block only if the step-4 opt-in was taken). The index and query log live under the
  common git dir, never in the worktree — nothing to ignore, nothing to commit.

### A check your project needs and gov does not have

Do not edit a kit engine. Write the check as your own script, in your own tree, and register it as a
leg in your gate manifest — `govkit apply` leaves a leg it does not own alone, and so does
`govkit update --write`.

Measured, not assumed: a fixture whose manifest held one project-authored leg came out of `apply`
holding 23, the project's row byte-identical. The run reports nothing about it, so silence is the
success case.

### Gate legs arrive on the safe verb too

`update --write` emits them, from the same implementation `apply` uses. That closes the gap where a
leg gov newly declared over a file you already hold reached you only when you re-ran the verb that
overwrites engine bytes unconditionally — the population is the kits your receipt claims, narrowed
by `--kits`, so a kit whose bytes did not move this run still gets its legs. Two exceptions, both
deliberate: a kit whose writes the verify pass rolled back gets none, because its engine went back
with them; and a read-only `update` emits nothing at all, because it wrote nothing else either.

If your runner file is malformed when the step is reached — hand-edited, or truncated by something
else — the run says so by name and emits nothing, keeps every byte it already wrote, and does not
re-stamp the receipt. Restore that file from your own history and re-run.

Two limits worth knowing before you hit them. Give the leg a **ceiling**, because the runner reds one
that arrives without it. And pick a name gov does not use: a collision makes `apply` exit 2 *after*
partially writing the install, and while your leg is protected rather than overwritten, the tree then
needs a re-run once you rename. Prefixing the leg with your project name is enough.

The full contract, including why this kit will never grow a plugin loader, is in the memory-tree
kit's own README.

## Maintenance

### The orders `update` leaves under `.governance/outbox/`

`update-declined-red-<kit>.md` means that kit's own `[check]` went green-to-red across this run and
the cause was a render step **this run declined**, not the bytes it wrote: nothing was rolled back,
the writes stand, the receipt is not re-stamped, and its first sentence names the declined step to
fix — a missing `[[regenerate]]` argv, or the `GOVKIT_RERENDER=0` that declined a step `update`
otherwise runs by default. Its siblings are
`update-rollback-<kit>.md`, where this run's writes really were reverted, and
`update-preexisting-red-<kit>.md`, where the kit was red before the run started.

When the LAST kit declaring an `[[lf_pin]]` leaves a target — dropped from `kits`, or its descriptor
retired the pin between vintages — `update` reports `pins-withdrawn` rather than `pins-moved`, and
under `--write` it REMOVES gov's marked region from your `.gitattributes` and drops the matching row
from the receipt. Both halves go together on purpose: the region without the row leaves gov's bytes
in a repository gov no longer claims, and the row without the region leaves the next `check` reading
a block that is not there. Nothing outside the marked region is read or rewritten, so a
`.gitattributes` you also maintain by hand keeps every line of its own, byte for byte. A read-only
run says `REMOVED` in so many words before any of it happens.

**Uncommitted edits to `.gitattributes` outside gov's marked region now stop a write.** Both writing
verbs already refuse when a path your receipt claims is uncommitted, and that file is one it claims:
gov writes its pin block there, stages it, and a rollback restores the pre-run index entry over it,
so an uncommitted line of your own would go with it. Commit or stash that edit and re-run. Edits
INSIDE gov's block are not counted — gov rewrites that region on every run and reports it as
`pins-moved` — so the ordinary state straight after an `apply` still proceeds.

**A receipt path that leaves your repository is reported as a receipt defect, and there is nothing to
stage.** `update` grades every path its receipt claims for containment before it asks anything about
your index, so a row carrying `..` or a drive letter is refused by name, naming the row that supplied
it. That refusal is the one you want: the untracked-shadow refusal above would tell you to `git add`
the path, and git answers that a path outside the repository cannot be added. Fix the row in
`.governance/install.json`, or the `prefix` in `.governance/deploy.toml` that produced it.

### `role-moved` — gov changed its mind about who owns a file

A row lands under a role, and a later vintage of gov's descriptor can declare that same destination
under a different one — most often moving a file gov used to supply into your project's own keeping.
`update` re-resolves every row's role against the descriptor as it stands, at every receipt schema,
and prints `role-moved` naming the role the row landed under, the role gov declares today and the
path. **Nothing is written for such a row and nothing in your receipt changes**, with one exception
named below. The two rules disagree about who owns those bytes, so the file on disk is exactly as
you left it — including a destination you have edited or emptied, which an older gov would have
restored from its own copy. There is nothing to undo and no order to read. `govkit apply` re-records
the row under the role the descriptor declares now, which is the verb a role change belongs to, and
the line stops appearing.

**The exception is the move where standing back would protect nothing.** Where the role gov now
declares is served by that kit's own re-render — the argv an `update` runs for every kit it touches —
skipping the row does not stop that argv. It removes only gov's half of the same run, the half that
compares your copy against both vintages and refuses when the three-way conflicts, so the render
lands on your edit with nothing in the run naming it. Such a row therefore keeps the disposition it
landed under: it is graded, reconciled and written like any other row of the role it landed under,
and the move is said on a line of its own rather than in place of that row's verdict. A move to a
role that writes nothing — your project's own keeping, a file your own tooling generates — stands
back exactly as described above.

One exception, and it is deliberate: on a receipt still at schema 1 the same disagreement REFUSES
the row instead. A schema-1 receipt is known to stamp roles its own descriptor contradicts, so
neither answer can be trusted there and acting on either would be a guess.

**`update-conflict-*.md` orders are REAPED, and they are the only family that is.** A conflict order
records a STATE — this row still conflicts — which every run re-derives from scratch, so an order
left standing after the conflict is resolved is a lie the operator keeps reading. An unscoped
`update --write` therefore removes every conflict order it did not itself write this run, unstages
each one from your index alongside the file, and prints the count and the names. The count prints
even when it is zero. Nothing else is touched: a withdrawal, rollback, preexisting-red or
declined-red order records an ACTION, and the row it belongs to has LEFT the receipt, so no later run
could re-derive it — and `apply`'s machine and hole orders are recorded in your receipt's `orders`
list, which `check` asserts against disk.

**A run carrying `--kits` reaps NOTHING and says so in one line.** A scoped run classifies only the
named kits' rows, so an order belonging to a row it never looked at is not stale — it is unexamined,
and removing it would destroy the only record that that row is still conflicted. Widen the scope, or
run unscoped, if you want the outbox tidied.

**A scoped run guards exactly the rows it can write, which is why it and a full run can disagree
about one target.** The refusal over a file that is present in your worktree and missing from your
index covers the named kits' rows only: a row outside the scope is never classified and never
written, so nothing there can be clobbered and nothing there is refused over. Gov's own
`.gitattributes` row belongs to no kit, so a scoped run neither rewrites its LF-pin block nor stands
in front of it; run unscoped to get both. The separate refusal over **uncommitted bytes** at a
claimed path is not scoped and never was — it protects work you have not committed, which a rollback
can destroy whichever kits this run named.

The first unscoped `--write` after you pull this vintage will remove every conflict order written by
an earlier one, because those carry the old filename key. Any whose conflict is still open is
rewritten by the same run under the new key before the reap runs, so you are never left without one.

A rollback order that names `.gitattributes` among its restored paths is not a mistake. Where this
run rewrote govkit's own LF-pin block, that block goes back with ANY kit's rollback, because it is
rendered from every claimed kit's pins at once and so belongs to no single one of them. A run that
rolled one kit of six back therefore restores a block the other five still want; the fix is the next
`update --write`, which re-renders it from the pin set that survived.

A `NOT restored <path>` line in a rollback order means your git refused the call that would have put
that path back — the line names which call — so the rollback is PART done and its receipt row was
deliberately left at this run's values rather than reverted, because a row claiming a pre-run state
the tree does not have is what makes the next run classify from bytes that are not there. The repair
is yours and the order is the only record of it: the next `update` sees that row at this run's
vintage and will not re-offer the work. Where `git checkout-index` is the call that refused, the
index was already reverted to the pre-run blob before it ran, so `git status` shows a change at that
path you did not make.

Where the path was one this run WITHDREW — a `--write-withdrawals` run, whose rollback then could not
put the deleted file back — the line says so instead, and says that its receipt row was KEPT rather
than dropped. A completed withdrawal drops the row; one the rollback left half-undone must not,
because that row is then the only thing naming bytes the target still holds. Expect the path to
appear in `git status` and expect the next `update` to classify it from where it actually is.

### `gate-lint` withdrew its seeded registry — a receipt already carrying that row keeps it silently

The tree-scan leg used to read a registry gov SEEDED under `{memory_root}/project/`. That rule is
gone: the leg's argv names no registry, and the scanner's registry argument is now optional — absent
means an empty declaration, and a path that was supplied and does not resolve is a refusal. Check 3
of the memory-tree hygiene gate treats that directory as a closed name set, so the seed was shipping
a red gate to anyone who cannot widen their own case list, and a FORKED checker takes a widening
never.

**`update` will not tell you.** The row's role is `seed`, `UPDATE_ROLE` maps `seed` to
`report-reseed`, and the seed branch in `update`'s disposition loop rewrites any surviving verdict to
`current` or `patched`. Its only exemptions are `missing` and `renamed`, and a withdrawal grids to
`withdrawn` — so a row gov no longer ships reads as `current` in every future run, and no order
names it. That override is deliberate and this release does not change it: widening its exemption set
re-adjudicates every seed row in every receipt, a verdict change on a population nothing here has
measured.

**So the step is manual, once, and only for a receipt written before this vintage.** That is inCMS
core and NicoCares, the two trees carrying an installed copy of this kit.

1. Pull the kit as usual.
2. Delete `substitution-fed-loops.txt` from the `project/` directory under your `memory_root`, and
   delete its row from `.governance/install.json`. Nothing reads either one from this vintage on.
3. If you had rows in that registry they were always yours — the shipped copy was empty — so carry
   them to wherever your scanner now reads its declaration from before you delete the file.
4. Your own gate manifest still carries the old argv element naming that file. Leg rows arrive as an
   order under `.governance/outbox/`, not as a write, so nothing removes it for you; drop it when you
   apply that order, or the scan refuses a path that no longer resolves.

### The build harness is rendered from review-harness 1.8 — migrating a receipt that rows it as an engine file

Before review-harness 1.8, `unattended-build.js` shipped as an engine file, so a receipt written
then rows `<kit>/unattended-build.js` with role `engine`. From 1.8 it is `rendered` from
`unattended-build.template.js`, and **`update` does not move the row**. It re-resolves every row's
role against the descriptor at every schema, but a destination whose NEW role is served by that
kit's own re-render keeps the disposition it landed under — standing back would not stop the
re-render, only gov's reconciliation of it. So on a schema-3 receipt the row is still graded as an
engine file: with no local edit `update` writes gov's own render, which spells gov's `tools/`
layout, over yours, and with one it reports a three-way conflict, leaves your copy in the index and
writes an order. Every later run then grades that row as an engine file, and a correct render reads
as a local edit. This needs govkit 1.11 or later,
which lands a new template BEFORE it re-renders; an older govkit refuses the render with
`missing shipped copy`.

**For the vintage that introduces review-harness 1.8, this migration REPLACES your routine pull of
this release's kits.** Run it instead of your usual `update --write`, not after it, and pull every
other kit you are behind on once it is done. A tree that already took that pull still migrates:
`update` then finds nothing left to move in review-harness and runs no regenerate, so block 1 runs
the kit's declared regenerate argv itself and carries on.

**The migration is three blocks, with a reading step before the last.** Run block 1 once, from a
clean tree. Set four variables in the shell you run them from, at `<project>`'s root:

```bash
GOV=<gov>        # a gov checkout at the vintage you are moving to
KIT=<kit>        # where review-harness is installed, e.g. scripts/workflows
PY=python        # whatever runs Python 3 here
TRAILER=         # the attribution line your commit-msg hook requires, or empty where none does
```

**`TRAILER` is what lets these commits land where a `commit-msg` hook refuses a message without
an attribution line**, as inCMS core's does. Unset there, every commit below is refused. An agent
sets it in every tree, to the attribution line its charter mandates, because the charter mandates
it on every agent commit. Each commit passes it as a paragraph of its own with a second `-m`, so no
`--trailer` support is needed.

Each block is a subshell, so a `STOP` ends that block and leaves your shell standing. Everything
the blocks pass between them, including the small program block 1 writes, sits in your git
directory and never in the tree. Each block also exports `PYTHONUTF8=1`, because govkit prints an
em dash on every line and, on Windows outside UTF-8 mode, writes it in the ANSI code page, which
the program then cannot read.

**The scope.** Block 1 moves this release's kits and no others. Unscoped, `update --write` moves
every kit your receipt is behind on. At NicoCares that was nine kits. At inCMS core it landed
gate-lint's seed under `memory/project/`, which core's memory hygiene refuses, so block 1 stopped on
every run (`ABL-dMuffledSentinel-7`). Your tree cannot work out which kits one release moves: the
receipt records only how far behind each kit is, and a kit behind for another reason reads the
same. So gov names them in block 1's `RELEASE`, review-harness 1.8 and unattended 1.20, which one
unit released together because the harness and the unattended Skill print one checklist command.
Block 1 drops any your receipt does not claim, and stops if that drops review-harness. `update`
then adds every kit your receipt claims that shares a version marker with one in scope, read from
each descriptor's `marker_carriers`, and prints a `scope:` line naming it. That is how drift-audit
comes along wherever it is installed: its two workflow harnesses sit in review-harness's directory
and carry drift-audit's marker, so moving one kit without the other reds cross-kit version parity.
Every other kit you are behind on waits for your routine pull, after the migration.

<!-- harness-migration 1 -->
```bash
( export PYTHONUTF8=1; G=$(git rev-parse --git-dir); V=$(git -C "$GOV" rev-parse HEAD)
  RELEASE=review-harness,unattended   # the kits this release moves, named by gov: see "The scope"
  rm -f "$G/harness-migration-ready" "$G/harness-migration-moved-to.txt"
  git ls-files -z --others --exclude-standard > "$G/harness-migration-before.txt"
  cat > "$G/harness-migration.py" <<'PY'
import hashlib, json, os, re, subprocess, sys, tomllib
g, mode = sys.argv[1], sys.argv[2]
RECEIPT = (".governance/install.json", ".governance/install.sums")
BLOCK_ROLES = ("merged", "attributes")  # adopt re-synthesizes these, and prints no row for them
def read(name):  # text mode, so output a platform wrote with CRLF reads the same
    with open(f"{g}/harness-migration-{name}.txt", encoding="utf-8") as fh:
        return fh.read()
def stop(why):
    print("STOP: " + why); sys.exit(1)
def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)
def ran_ok():  # kits whose every regenerate argv exited 0, unrefused, in step 1
    ok = {}
    for kit, rest in re.findall(r"  ran ([\w.-]+): .*? -> exit (\d+.*)$",
                                read("update") + read("regen"), re.M):
        ok[kit] = ok.get(kit, True) and rest.strip() == "0"
    return {k for k, v in ok.items() if v}
def tracked(*args):
    return {p for p in git("ls-files", "-z", *args).stdout.split("\0") if p}
def planned():  # every destination the plan at this vintage resolves: {path: (role, kit)}
    return {d: (r, k) for m, r, d, k in re.findall(r"^  (\S+) +\[(\S+) *\] (.+?)   <- (\S+)$",
                                                   read("plan"), re.M) if m != "UNRES."}
def rendered_here():  # every TRACKED destination the plan renders, with its kit
    t = tracked()
    return {d: k for d, (r, k) in planned().items() if r == "rendered" and d in t}
def receipt():
    with open(RECEIPT[0], encoding="utf-8") as fh:
        return {f.get("path"): f for f in json.load(fh).get("files", [])}
def templates(gov):  # {rendered destination: [gov template]}, from gov's own descriptors and the plan
    with open(f"{gov}/tools/govkit/registry.toml", "rb") as fh:
        entries = tomllib.load(fh).get("entry", [])
    plan, out = planned(), {}
    for e in entries:
        with open(f"{gov}/{e['descriptor']}", "rb") as fh:
            d = tomllib.load(fh)
        home = (d.get("home") or "").rstrip("/")
        for rule in d.get("files", []):
            if rule.get("role") != "rendered":
                continue
            inc, to = rule.get("include") or [], rule.get("to") or []
            srcs = [f"{home}/{i}" if home else i for i in ([inc] if isinstance(inc, str) else inc)]
            for pat in [to] if isinstance(to, str) else to:
                rx = re.compile(re.sub(r"\\\{\w+\\\}", ".+", re.escape(pat)))
                for dest, (role, kit) in plan.items():
                    if kit == e["id"] and role == "rendered" and rx.fullmatch(dest):
                        out.setdefault(dest, []).extend(srcs)
    return out
def moved(gov, to, dest, tmpl, rec):  # does every template `dest` renders from hold gov's blob at `to`?
    copies = {f["source"]: p for p, f in rec.items()
              if f.get("source") and f.get("role") != "rendered"}
    for src in tmpl.get(dest) or [None]:
        if src not in copies:
            return False
        have = git("ls-files", "-s", "--", copies[src]).stdout.split()[1:2]
        want = subprocess.run(["git", "-C", gov, "rev-parse", f"{to}:{src}"],
                              capture_output=True, text=True).stdout.strip()
        if have != [want]:
            return False
    return True
if mode == "scope":
    release = [k for k in sys.argv[3].split(",") if k]
    with open(RECEIPT[0], encoding="utf-8") as fh:
        claimed = set(json.load(fh).get("kits") or [])
    if release[0] not in claimed:
        stop(f"this receipt does not claim {release[0]}, the kit this migration moves, so it has "
             "nothing to migrate.")
    for k in release:
        if k not in claimed:
            print(f"scope: {k} is in this release and this receipt does not claim it, so it is left out")
    with open(f"{g}/harness-migration-kits.txt", "w", encoding="utf-8") as fh:
        fh.write(",".join(k for k in release if k in claimed))
elif mode == "step1":
    upd, par = read("update"), read("parity")
    rc = re.search(r"^update exit (\d+)", upd, re.M).group(1)
    if rc != "0" or " 0 conflict(s)" not in upd:
        stop(f"update exited {rc} or left a conflict, and nothing is committed. Return the tree to "
             "HEAD FIRST, with git reset -q --hard HEAD: it discards everything uncommitted, a "
             "resolution included, and leaves update's order under .governance/outbox/. Then "
             "resolve what that order names and COMMIT the resolution, which the restore block "
             "does for a local edit on a row that records a base. Then run this block again.")
    if "review-harness" not in ran_ok():
        stop("the review-harness regenerate did not run at exit 0, so the harness is gov's render.")
    if not re.search(r"^parity exit 0$", par, re.M) or re.search(r"SKIP \S*unattended-build\.js", par):
        stop("the parity check did not grade the harness green, and its output above says why.")
    for p in sorted(tracked("--others", "--exclude-standard") - set(read("before").split(chr(0)))):
        print(f"FLAG {p}: step 1 created it and nothing rows it, so it is NOT staged")
    # The renders are the only regenerate output block 3 stages. Anything else a regenerate did to a
    # tracked file, a deletion included, goes back to what update left, and is named.
    rendered, renders, back = rendered_here(), [], []
    z = git("diff", "--name-status", "-z").stdout.split("\0")
    for st, p in zip(z[0::2], z[1::2]):
        if p not in RECEIPT:
            (renders if st == "M" and p in rendered else back).append((st, p))
    if back and git("checkout", "--", *[p for _st, p in back]).returncode:
        stop("a file a regenerate changed outside every rendered destination could not be restored.")
    for st, p in back:
        print(f"FLAG {p}: a regenerate {'deleted' if st == 'D' else 'changed'} it and no rendered "
              "row names it, so it is restored to what update left and NOT staged")
    with open(f"{g}/harness-migration-renders.z", "w", encoding="utf-8", newline="") as fh:
        fh.write("".join(p + "\0" for _st, p in renders))
elif mode == "pins":
    to, gov, rendered, ran, rec = sys.argv[3], sys.argv[4], rendered_here(), ran_ok(), receipt()
    tmpl = templates(gov)
    # A render's bytes are this vintage's only when its kit re-rendered it AND its template holds
    # gov's bytes here: update writes no fork, and a regenerate over a fork renders the fork.
    pins = [f"--pin {d}={to}" for d, k in sorted(rendered.items())
            if k in ran and moved(gov, to, d, tmpl, rec)]
    t, plan = tracked(), planned()
    for p, f in sorted(rec.items()):
        if (p in t and p in plan and p not in rendered and f.get("commit")
                and f.get("role") not in BLOCK_ROLES + ("rendered",)):
            pins.append(f"--pin {p}={f['commit']}")
    with open(f"{g}/harness-migration-pins.txt", "w", encoding="utf-8") as fh:
        fh.write("".join(x + "\n" for x in pins))
elif mode == "check":
    old, rendered = receipt(), rendered_here()
    pinned = {x.split(" ", 1)[1].rsplit("=", 1)[0] for x in read("pins").splitlines() if x}
    counted, bad, seen = [], [], set()
    for key, role, d, base in re.findall(r"^  (\S+) +\[(\S+) *\] (.+?)( <- [0-9a-f]+)?$",
                                         read("adopt"), re.M):
        if key == "not-installed":
            continue
        was = old.get(d)
        seen.add(d)
        # adopt prints a fork's key as `forked` whatever it measured, and a base only when it has one
        if key != "unattributed" and not (key == "forked" and not base):
            if was is None:
                print(f"FLAG {d}: new to the receipt, measured {key}")
            continue
        if d in rendered and d not in pinned and rendered[d] in ran_ok():
            why = ("its template does not hold gov's bytes at this vintage, a fork update does not "
                   "write, so the regenerate rendered the fork. Carry gov's diff into it, then run "
                   "blocks 2 and 3 again")
        elif was is None:
            why = "new to the receipt, so nothing ever recorded a base for it"
        elif was.get("evidence") == "unattributed":
            why = "it was unattributed before this migration"
        elif d in rendered and d not in pinned:
            why = "its kit did not regenerate it in step 1, so no vintage is claimed for its bytes"
        elif not was.get("commit"):
            why = "it recorded no base before, and adopt now says so"
        else:
            bad.append(d)
            continue
        counted.append(d)
        print(f"FLAG {d}: unattributed, because {why}")
    for d in sorted(set(old) - seen):
        if old[d].get("role") not in BLOCK_ROLES:
            print(f"FLAG {d}: the receipt rows it and the re-adopt does not measure it as "
                  "installed, so block 3 drops its row")
    for d in bad:
        print(f"STOP: the receipt recorded a base for {d}, and the re-adopt cannot attribute it")
    print(f"the re-adopt leaves {len(counted)} row(s) unattributed, and the next update withholds "
          "its stamp over exactly those, or re-stamps when there are none")
    sys.exit(1 if bad else 0)
elif mode == "restore":
    gov = sys.argv[3]
    with open(RECEIPT[0], encoding="utf-8") as fh:
        doc = json.load(fh)
    rows, bodies = {f.get("path"): f for f in doc.get("files", [])}, {}
    paths = re.findall(r"^govkit: '(.+?)' diverged and the three-way conflicts", read("update"), re.M)
    if not paths:
        stop("block 1's last update named no three-way conflict, so there is nothing to set aside.")
    for path in paths:  # every check before any write, so a STOP leaves the tree as it was
        row = rows.get(path, {})
        if not (row.get("commit") and row.get("source") and row.get("gov_oid")):
            stop(f"the receipt records no gov base for {path}, so there is no blob to restore it to.")
        if row.get("carry") == "relocate":
            stop(f"{path}'s row carries a relocate rung, so gov's blob at its base spells gov's "
                 "prefix and not this tree's. Resolve it by hand, the way update's order asks.")
        if git("ls-files", "-s", "--", path).stdout.split()[1:2] == [row["gov_oid"]]:
            stop(f"{path} already holds gov's blob at its recorded base, so this conflict is not a "
                 "local edit's. Resolve it the way update's order asks.")
        body = subprocess.run(["git", "-C", gov, "show", f"{row['commit']}:{row['source']}"],
                              capture_output=True)
        if body.returncode:
            stop(f"gov holds no {row['source']} at {row['commit'][:8]}.")
        bodies[path] = body.stdout
    for path, body in bodies.items():
        row, keep = rows[path], f"{g}/harness-migration-local-edits/{path}"
        os.makedirs(os.path.dirname(keep), exist_ok=True)
        with open(path, "rb") as fh, open(keep, "wb") as out:
            out.write(fh.read())
        with open(path, "wb") as fh:
            fh.write(body)
        if git("hash-object", "--", path).stdout.strip() != row["gov_oid"]:
            stop(f"{path} does not hash to its row's gov_oid once restored.")
        row["oid"], row["sha256"] = row["gov_oid"], hashlib.sha256(body).hexdigest()
        print(f"restored {path} to gov's blob at {row['commit'][:8]}, and set this tree's edit "
              f"aside at {keep}")
    with open(RECEIPT[0], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(doc, indent=2) + "\n")
    with open(RECEIPT[1], "w", encoding="utf-8", newline="\n") as fh:
        fh.write("".join(f"{f['sha256']}  {f['path']}\n" for f in doc["files"] if "sha256" in f))
    with open(f"{g}/harness-migration-restored.z", "w", encoding="utf-8", newline="") as fh:
        fh.write("".join(p + "\0" for p in bodies))
PY
  # 0. The scope: this release's kits that this receipt claims. `update` adds each claimed kit that
  #    shares a version marker with one of them, and prints it.
  "$PY" "$G/harness-migration.py" "$G" scope "$RELEASE" || exit 1
  # 1. Move forward and re-render, then grade the harness this install holds. STOP unless update
  #    exits 0 with no conflict, the review harness's regenerate exited 0, and the harness is green.
  GOVKIT_RERENDER=1 "$PY" "$GOV/tools/govkit/govkit.py" update --target . --write \
    --kits "$(cat "$G/harness-migration-kits.txt")" > "$G/harness-migration-update.txt"
  u=$?; echo "update exit $u" >> "$G/harness-migration-update.txt"; cat "$G/harness-migration-update.txt"
  #    A tree a flag-off pull already moved leaves update nothing to act on in review-harness, so
  #    update ran no regenerate there. Run the kit's declared regenerate argv the same way.
  : > "$G/harness-migration-regen.txt"
  if [ "$u" = 0 ] && ! grep -qF '  ran review-harness: ' "$G/harness-migration-update.txt"; then
    { bash "$KIT/check-protocol-parity.test.sh" --render --tracked-only 2>&1
      echo "  ran review-harness: bash $KIT/check-protocol-parity.test.sh --render --tracked-only -> exit $?"
    } > "$G/harness-migration-regen.txt"; cat "$G/harness-migration-regen.txt"
  fi
  bash "$KIT/check-protocol-parity.test.sh" --tracked-only > "$G/harness-migration-parity.txt" 2>&1
  echo "parity exit $?" >> "$G/harness-migration-parity.txt"; cat "$G/harness-migration-parity.txt"
  "$PY" "$GOV/tools/govkit/govkit.py" plan --target . > "$G/harness-migration-plan.txt" \
    || { echo "STOP: plan failed."; exit 1; }
  "$PY" "$G/harness-migration.py" "$G" step1 || exit 1
  # 2. Commit update's own writes with the receipt that records them, and nothing the regenerate
  #    wrote: the renders stay unstaged until block 3 rows them `rendered`.
  git add -- .governance/install.json .governance/install.sums
  git diff --cached --quiet || git commit -q -m "govkit update: review-harness 1.8" ${TRAILER:+-m "$TRAILER"} \
    || { echo "STOP: that commit was refused."; exit 1; }
  echo "$V" > "$G/harness-migration-moved-to.txt" )
```

<!-- harness-migration 2 -->
```bash
( export PYTHONUTF8=1; G=$(git rev-parse --git-dir)
  rm -f "$G/harness-migration-ready" "$G/harness-migration-stamp.txt"
  V=$(cat "$G/harness-migration-moved-to.txt" 2>/dev/null) || { echo "STOP: block 1 has not finished clean."; exit 1; }
  [ "$(git -C "$GOV" rev-parse HEAD)" = "$V" ] \
    || { echo "STOP: GOV is not at $V, the vintage block 1 moved this tree to, so step 1's log says nothing about it."; exit 1; }
  # 3. Derive the pins from the plan at this vintage. 4. Run the re-adopt READ-ONLY and check it.
  #    Nothing here writes to the tree, so this block can be run again after you fix a STOP.
  "$PY" "$GOV/tools/govkit/govkit.py" plan --target . > "$G/harness-migration-plan.txt" \
    || { echo "STOP: plan failed."; exit 1; }
  "$PY" "$G/harness-migration.py" "$G" pins "$V" "$GOV" || exit 1
  "$PY" "$GOV/tools/govkit/govkit.py" adopt --target . --re-adopt $(cat "$G/harness-migration-pins.txt") \
    > "$G/harness-migration-adopt.txt"; rc=$?; cat "$G/harness-migration-adopt.txt"
  [ "$rc" = 0 ] || { echo "STOP: the read-only re-adopt refused."; exit 1; }
  "$PY" "$G/harness-migration.py" "$G" check || exit 1
  echo "$V $(git hash-object .governance/install.json)" > "$G/harness-migration-stamp.txt"
  touch "$G/harness-migration-ready" )
```

Read every `FLAG` line blocks 1 and 2 printed before you run block 3. Each names its reason, and the
paragraphs after block 3 say why each reason is expected.

<!-- harness-migration 3 -->
```bash
( export PYTHONUTF8=1; G=$(git rev-parse --git-dir); PINS=$(cat "$G/harness-migration-pins.txt" 2>/dev/null)
  [ -f "$G/harness-migration-ready" ] || { echo "STOP: block 2 has not finished clean since the last block 3."; exit 1; }
  [ "$(cat "$G/harness-migration-stamp.txt")" = "$(git -C "$GOV" rev-parse HEAD) $(git hash-object .governance/install.json)" ] \
    || { echo "STOP: GOV or the receipt moved after block 2 derived these pins. Run block 2 again."; exit 1; }
  # 5. Re-row, then commit the re-rendered files with the receipt that now rows them `rendered`.
  "$PY" "$GOV/tools/govkit/govkit.py" adopt --target . --re-adopt $PINS --write || { echo "STOP: adopt refused."; exit 1; }
  git add -- .governance/install.json .governance/install.sums
  [ ! -s "$G/harness-migration-renders.z" ] \
    || git add --pathspec-from-file="$G/harness-migration-renders.z" --pathspec-file-nul
  git diff --cached --quiet || git commit -q -m "govkit adopt --re-adopt: the build harness is rendered" ${TRAILER:+-m "$TRAILER"} \
    || { echo "STOP: that commit was refused. Unstage it with git reset -q, then run blocks 2 and 3 again."; exit 1; }
  # 6. Re-adopt once more. Step 5 read each render's identity from the index before the render was
  #    staged, and this run reads the commit that holds it. A STOP from here on is recovered by
  #    running block 2 again and then this block, whose commits are skipped when nothing is staged.
  "$PY" "$GOV/tools/govkit/govkit.py" adopt --target . --re-adopt $PINS --write || { echo "STOP: adopt refused."; exit 1; }
  git add -- .governance/install.json .governance/install.sums
  git diff --cached --quiet || git commit -q -m "govkit adopt --re-adopt: record the committed renders" ${TRAILER:+-m "$TRAILER"} \
    || { echo "STOP: that commit was refused. Unstage it with git reset -q, then run blocks 2 and 3 again."; exit 1; }
  # These pins describe this receipt at this vintage and no later one, so they go with the migration.
  rm -f "$G/harness-migration-ready" "$G/harness-migration-pins.txt" "$G/harness-migration-stamp.txt" )
```

**Why the re-adopt.** It is the only verb that re-reads a row's role from the descriptor, and it
re-measures EVERY row, not just this one.

**Why step 1 stops on update's exit code, and not on the parity check.** When the three-way merge
conflicts on a file, `update` leaves that row untouched at its old commit, writes an order under
`.governance/outbox/` and exits 1, and the regenerate still runs, so the parity check alone passes.
Carried on, block 3 would record the regenerated harness as current over an edit the merge could not
place. Any STOP in block 1 leaves update's writes in the tree uncommitted, and `update` refuses to
run over dirty paths it claims. **So the remedy runs in one order.** Return the tree to HEAD with
`git reset -q --hard HEAD` FIRST. Then resolve what update's order names, commit the resolution,
and run block 1 again. The reset discards everything uncommitted, so a resolution made before it
is lost: the STOP text once put the resolution first, and NicoCares lost one that way. The order
under `.governance/outbox/` is untracked, and the reset leaves it where it is.

A conflict comes from a local edit on a row that records a base, the harness's or any other file's.
The restore block below resolves it by setting the edit aside: it restores every file block 1's
last `update` named as conflicting to its row's `gov_oid`, which is gov's blob at the row's
`commit`, and commits that. It judges whether the file holds a local edit by its INDEX blob, never
by the row's `oid`, because a receipt `apply` wrote records gov's blob there whatever the tree did
to the file since, while in a receipt `adopt` measured `oid` is your edited bytes, so restoring to
it would recreate the conflict. It refuses a row that carries a `relocate` rung, because gov's
blob at its base spells gov's prefix and not yours; resolve that one by hand. It reads gov's bytes with `git -C "$GOV" show <commit>:<source>`,
saves each edit under `harness-migration-local-edits/` in the git directory, and sets each row's
`oid` to the restored blob in the same commit, which is what a commit-time receipt check needs.
Then run block 1 again, which merges gov's change over the restored file. Carry each edit back
after block 3, the way the paragraph on local edits below carries the harness's into the template.

<!-- harness-migration restore -->
```bash
( export PYTHONUTF8=1; G=$(git rev-parse --git-dir)
  [ -f "$G/harness-migration.py" ] || { echo "STOP: run block 1 first, which writes the program this block runs."; exit 1; }
  [ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "STOP: return the tree to HEAD first."; exit 1; }
  "$PY" "$G/harness-migration.py" "$G" restore "$GOV" || exit 1
  git add --pathspec-from-file="$G/harness-migration-restored.z" --pathspec-file-nul
  git add -- .governance/install.json .governance/install.sums
  git commit -q -m "set each conflicted file's local edit aside: it holds gov's blob at its recorded base" ${TRAILER:+-m "$TRAILER"} \
    || { echo "STOP: that commit was refused."; exit 1; } )
```

**Why block 1 commits only what `update` staged.** Until block 3 the receipt still rows the harness
as an engine file. A commit-time check that compares staged engine blobs with the receipt therefore
reds the re-rendered harness, and the re-adopt that would clear that refuses a staged tree. So step
2 commits update's own writes with the receipt that records them, which passes such a check, and
block 3 stages the renders once their rows are `rendered`. It stages them by name, from the list
step 1 recorded, and that list holds only tracked destinations the plan renders that a regenerate
modified. A file step 1 CREATED is flagged and never staged, because nothing rows it. Anything else
a regenerate did to a tracked file, a deletion included, is restored to what `update` left and
flagged. Staged, such a change would land under the renders' commit subject, and a deleted row the
receipt still pins makes block 3's second re-adopt refuse after that commit has landed. Once step 2
has committed, block 1 is done: its regenerated files stay unstaged, and `update` would refuse them
as dirty. Block 2 writes nothing to the tree, so run it again as often as a STOP needs. Block 2 and
block 3 each refuse a GOV that has moved since block 1, because step 1's log, which says which kits
regenerated, describes that vintage and no other.

**Why these pins, and where each one comes from.**

- Every tracked row that records a `commit`, and that the plan at this vintage still resolves, is
  pinned to it. Unpinned, a row carrying a local edit matches no gov vintage and comes back
  `unattributed`, which loses the base its three-way merge needs. A row the plan no longer resolves
  is not measured, and `adopt` refuses a pin on it.
- A render never equals its template, so it comes back `unattributed` too unless it is pinned. A
  rendered destination is pinned to the vintage you moved to only when its kit's regenerate ran at
  exit 0 in step 1 AND the template it renders from holds gov's blob at that vintage, because only
  then do its bytes come from that vintage. `update` writes no fork, so a template this tree forked
  keeps its own bytes, and a regenerate over it renders the fork: inCMS core's unattended Skill was
  pinned at the new vintage while its template was a 1.19 fork. The template for each render comes
  from gov's own descriptors, `include` against `to`, and its copy here from the receipt row whose
  `source` names it.
- The rendered destinations come from `plan` at that vintage, never from the receipt. A receipt
  `adopt` bootstrapped rows only what was tracked when it ran, so a destination tracked since then
  is one the receipt never names, while `adopt` measures every destination the plan and the index
  share.
- A render whose kit declined its regenerate keeps the bytes of the vintage it was rendered at, so
  it stays unpinned. Pinned to the new vintage, it would record stale bytes as current, and the
  next update would grade it `patched` rather than `re-rendered`. Pinning it to the receipt's old
  stamp is true only when that stamp is the vintage it was rendered at, which a flag-off update can
  break, so that is an assertion you make by hand and never a default.
- A rendered destination is never pinned to a recorded commit. After a conflicted step 1 that
  commit predates the template, and `adopt` refuses a pin naming a base gov does not hold.
- Block rows (`merged`, `attributes`) are left to `adopt`, which re-synthesizes them and prints no
  row for them. Every other role that records a `commit` is pinned to it, `project-owned` and
  `generated` included. `adopt` measures those with the same walk as an engine row, so an edited
  one would come back `unattributed` without its pin, and the check would stop on it. The pins and
  the check read one list of the roles left to `adopt`, so the two cannot disagree about a row.

**What block 2's check reports.** It flags every row new to the receipt, pinned or not, because
nothing recorded a base for it before. It flags every row the re-adopt leaves `unattributed`, with
one of five reasons: a render regenerated from a forked template, new to the receipt, unattributed
before, a render its kit did not regenerate, or a row that recorded no base before. The first is
checked first, because it is the one that asks you to do something. A `forked` row counts as
unattributed when `adopt` prints it with no base, because `adopt` prints a fork's key as `forked`
whatever it measured. The check also
flags every row the receipt holds that the re-adopt does not measure as installed, because block 3
drops that row. It STOPs on a row the receipt recorded a base for that the re-adopt cannot
attribute, because the migration would have made that row worse. Its last line counts the
unattributed rows. `adopt` re-measures only the kits `.governance/deploy.toml` names in `kits`, so
check that list covers every kit the receipt claims first. The pin list is split on whitespace, so
a path holding a space needs its flags passed by hand.

**A local edit to the old harness does not survive step 1.** The re-render overwrites the harness
with the template's render. Carry the edit into `<kit>/unattended-build.template.js` after block 3,
re-run `bash <kit>/check-protocol-parity.test.sh --render`, commit the template and its render, then
run blocks 2 and 3 again, which record the template's delta. A target whose pre-commit compares
staged engine blobs with its receipt refuses that commit, as it refuses any local edit to an engine
file, and that is its own check's rule rather than this migration's.

**A forked kit file takes gov's diff by hand, after block 3.** `update` writes no row it cannot
attribute to a gov vintage. It says how many with "matched no gov vintage at adoption, so there is
no base to write against and none was written", and block 2 flags each one "unattributed before".
A kit file you forked therefore keeps its old bytes through this migration, whatever gov changed in
it. inCMS core held seven unattended forks. For each fork in a kit in scope, carry gov's diff from
the receipt's old `gov_commit` to the vintage you moved to by hand, after block 3 has landed. Then
run the kit's regenerate by hand where the fork is a template, so its render follows it: the review
harness's is `bash "$KIT/check-protocol-parity.test.sh" --render --tracked-only`. Commit the forks
and their renders, then run blocks 2 and 3 again. A fork the carry leaves as gov's bytes then
measures vintage-matched, and a render whose template is now gov's is pinned, which block 2 had
flagged "its template does not hold gov's bytes" and left unpinned. After block 3, and not before,
because block 1 runs from a clean tree and names the forks itself. A target whose pre-commit
compares staged engine blobs with its receipt refuses the carry's commit, and `adopt` refuses the
staged tree that would re-measure it, which inCMS core records as `ABL-dMuffledSentinel-3`. Core
committed its carry in a throwaway `--shared` clone, ran blocks 2 and 3 there, and brought the
receipt back.

**Done looks like this.** The receipt rows the harness `rendered` with `evidence: "pinned"`, and
every row blocks 1 and 2 did not flag keeps the attribution it had. The next `update --write` writes
nothing to the harness. It either re-stamps, or it withholds the stamp over exactly the rows block
2's last line counted, and says how many. That withheld stamp is the migration's end state, not a
fault in it. The message names `adopt --re-adopt --pin <path>=<rev> --write`, and that IS the form to
run. **Do not answer it by dropping the `--pin`.** The bare `--re-adopt --write` is the unpinned
re-adopt: it drops the harness's `pinned` evidence and every edited row's base, and it re-walks the
same bytes to the same answer. Re-running the migration does not clear the message either, because it
measures the same rows the same way. Pin the rows it counted, or live with the withheld stamp; there
is no override, and `DEPL-cMendedVintage-4` retired the one there used to be, because its only
effect was to advance the base those rows must be attributed FROM. Every row of a kit outside the
scope keeps its base, and the re-adopt stamps each
row with its kit's version at the vintage its bytes come from, so `update`'s per-kit delta still
reads that kit behind rather than `level`. Before govkit's re-adopt did that, NicoCares' re-adopt
stamped memory-tree's rows 2.69 over bytes at 2.68. Blocks 2 and 3 are run again only to recover
from a STOP inside the migration, or after carrying a fork, at the vintage block 1 moved to. Block
3 deletes its pins when it finishes, and blocks 2 and 3 refuse a
GOV that has moved since block 1, because pins derived at one vintage and replayed after a later
update would rewind every row that update moved. Having the message name the pinned form is
`DEPL-dPolishedVitrine-1`'s, and so is `update` learning to move a role itself, which retires this
section.

The govkit selftest's `[-PV]` arms cut these blocks out of this file and run them on every
self-test run, so the text you copy is the text that was tested. They run on fixtures `apply`
installed and on ones `adopt` bootstrapped, through inCMS core's two commit-time hooks: a pre-commit
holding its receipt check and the arm of its memory hygiene that refuses a `memory/` file a commit
adds, and a `commit-msg` rule that wants an attribution line. The fixtures carry a row unattributed
before the migration, an edited `project-owned` row, a fork `adopt` cannot attribute, a kit that
declines its regenerate, a kit whose regenerate deletes and edits tracked files, two destinations
the receipt never rowed, a flag-off pull taken first, a conflicting harness edit, a conflict on a
file that is not the harness, a kit outside the release that ships a seed and moves its version,
two kits whose version markers ride in another kit's files, a forked template carried after block
3, and a later update after Done. The blocks run with Python's UTF-8 mode off, so a node that
exports it cannot hide an encoding dependency.

### The hooks ship ONE copy each — migrating a tree that has two

Before `TOOL-dRetiredFork-14`, `agent-cap.js` and `scratch-guard.js` installed to both
`{prefix}/hooks/` and `.claude/hooks/`, and the wired command named the second. Only the first ships
now. A tree adopted before that change has two copies and a command pointing at the one that is no
longer maintained.

**The order is the whole instruction.** Move the wired command to the surviving copy, THEN withdraw
the second. Reversed, the hook is unwired for the window between, and an unwired agent-cap is a
security guard that is silently off:

```bash
python tools/settings-merge.py                                            # repaths agent-cap
python tools/settings-merge.py --fragment "$KIT/hooks/scratch-guard.fragment.json"   # $KIT = your prefix
bash tools/check-wiring.sh --check                                        # confirm before step 2
govkit update --write-withdrawals                                         # only now
```

`check-wiring.sh` REPORTS a legacy copy instead of failing on it, precisely so this two-step is
possible: a tree mid-migration is told what remains, not blocked from finishing.

If your kits are not at `tools/`, nothing above changes — the fragments declare their hook path with
a `{kit}` token and both the writer and the checker expand it against the fragment's own location.

- Codebase-map engine files (`map_lib.py`, `gen_map.py`, `map_diff.py`, `reuse_lookup.py`, the two
  templates, `selftest.py`, `adopt-codebase-map.sh`) are identical across repos — update by
  overwriting from `<gov-repo>` wholesale; NEVER overwrite the project-owned
  `<kit>/map_extractors.py` or `.codebase-map.conf`.
  When an overwrite first introduces the graced `## Reuse affordance` check, run
  `python <kit>/gen_map.py --seed-affordance-baseline` ONCE (or re-run the adopter) and
  commit `<MAP_ROOT>/affordance-exempt.toml` in the same landing — that seed graces the existing
  dossiers so the new check does not retro-red them (it is a no-op once the file is present).
  Any overwrite that moves `KIT_CODEBASE_MAP_VERSION` also owes one `python <kit>/gen_map.py
  --write` in the same landing: the version rides `inventories.json`, `MAP.md` and `symbols.json`
  as `codebase-map@<v>`, and the freshness gate byte-compares them. **1.0 → 1.1** is such a bump.
  It also frees a prefixed install: if the repo carried a `CODEBASE_MAP_ROOT` workaround (an env
  export, or an `os.environ.setdefault` in `map_extractors.py`) to correct the old grandparent
  rule, delete it — the resolver now agrees with it, and a stale override outlives the tree it
  named. An installed `<GATE_FILE>` is project-owned and is NOT overwritten by this rule, so it
  keeps its old kit-dir walk until you re-copy the template; that is safe at a root install and
  required before moving the kit under a prefix.

- **memory-recall is three maintenance classes, not one** — `union.py` is a byte-identical upstream
  copy (its sha prefix is pinned in `verbatim.json` and gated by the kit selftest): overwrite it
  wholesale. `bench.py` is pinned the same way and is NOT a wholesale overwrite any more — it
  carries one deliberate delta (`TOOL-dTracedLattice-7`, `run_rm3` made hash-seed-independent), so
  overwriting it reverts that fix and the pin goes green over the revert. `extract.py`, `query.py`
  and `recall-opened.js` are FORKS — each carries a header naming the upstream path and sha it was
  taken from, so a re-pull is a three-way merge, not archaeology. `recall_conf.py`, `selftest.py`, `SKILL.template.md`, `adopt-memory-recall.sh` and the
  fragment are this kit's own. Never overwrite the RENDERED `.claude/skills/memory-recall/SKILL.md` by
  hand — re-run `--scaffold`, which is what `--check` grades. After any `FAMILIES`/`MEMORY_ROOT` edit,
  re-run `--scaffold`; the cache invalidates itself on the resolved conf, so no manual purge is needed.

- **Precedence on any conflict:** `CLAUDE.md` > manifest > skill — follow the winner, fix the loser.
- **Pull upstream improvements:** the playbook carries `governance-template: vN.N`; re-pull by diffing your
  filled copy against `<gov>/coding-governance-agents.template.md` per §-body (ignore filled
  placeholders + the deleted Customize block) — a re-pull carries the v2.2 §1 manifest lines (DoD
  write-back + Landing reconcile exception) into instantiated playbooks. The manifest carries its own
  `kickoff-manifest: vN.N`. The `memory-tree/` scripts are identical across repos — copy the newer
  versions in wholesale.
  **v2.7 (2026-08-11) DELETES text you may already hold:** companion §1's unattended block is now a
  single pointer at `<MEMORY_ROOT>/guides/UNATTENDED-PROTOCOL.md`, and §8's restatement of the §1
  landing rule is a pointer too. Both were paraphrases of documents the kits install; re-pull §8 and
  the companion together, and delete rather than merge — a kept paraphrase is the drift the collapse
  removed.
  **v2.6 (2026-08-10) moves a rule you may already hold:** §1's Landing bullet and §8's commit bullet
  now accept a committed standing mandate in place of the explicit ask, and the kickoff-manifest
  merge exception left §1 for the new companion §1. Re-pull §1, §8 and the companion in lockstep, and
  read §2's "The two blocks that are not about a kit" plus `drop_blocks` in the target's
  `deploy.toml` first — that is where the conditional-sections row went — because the mandate clauses are keyed on
  adopting `unattended/`, and a repo that keeps them without that kit is carrying a rule nothing can
  make true. Snapshot of the prior release: `memory/archive/parallel-coding-governance.template-v-2-5.md`.
- **`manifest-check.sh` is engine-identical** across repos — overwrite wholesale from `<gov>` (this also
  delivers the version-WARN constant that flags out-of-date manifest bodies). The `manifest-audit`
  block and the manifest BODY are project-owned — never overwritten by kit updates.
- **Stall review (rides this same Maintenance cadence):** at each kit re-pull, the owner compares the
  manifest's BODY-change commits (diffs touching more than the `last-audit` line) against watch-commit
  volume and elapsed time — **≥10 watch-pathspec commits or ≥3 months with zero body growth = the
  manifest is stalling**; that is the trigger for reconsidering heavier accretion tooling (mining the
  build records). Kickoff delta lines are supporting color, not the data source — squash merges and
  chat don't preserve them.
- **memory-tree kit updates** never carry project data (no brand gate, no migrations) — those stay in the
  project. Safe to overwrite `memory-tree/*.sh` + `HYGIENE.template.md` from `<gov>`.
