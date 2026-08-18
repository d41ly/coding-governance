# Wire the coding-governance chain into a project — agent runbook

You are wiring the **full coding-governance chain** into a target project. Follow this top to bottom;
verify after every step. This file is agent-facing: imperative steps, exact commands, explicit
derive-vs-ask calls.

**The chain is three composing layers:**

1. **Governance playbook** (`parallel-coding-governance.template.md`) — the multi-node ruleset (IDs,
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
    (`parallel-coding-governance.template.md` §5, and `.customize.md` says it twice): §5's work-state
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
## 2 — Install the governance playbook (per project)

1. Copy the playbook **and its two companions** in (the template's §4/§9/§10/§11/§12/§13 are §-stubs
   that reference `parallel-coding-governance.domain-rules.md` by name — it MUST travel alongside):
   ```bash
   cp <gov>/parallel-coding-governance.template.md    <project>/docs/PARALLEL.md
   cp <gov>/parallel-coding-governance.domain-rules.md <project>/docs/parallel-coding-governance.domain-rules.md
   # the customize companion is deploy-time only — read it, don't ship it
   ```
   (or install the filled playbook as the canonical `AGENTS.md` via the agent-instructions kit —
   see its own install step below, §3c.)
   **Keep the `<!-- governance-template: vN.N -->` marker verbatim** — the kickoff engine's Step-2
   fallback and the upstream-re-pull mechanism both read it.
2. Fill every `{{PLACEHOLDER}}` per **`<gov>/parallel-coding-governance.customize.md`** (the deploy-time
   placeholder catalog — externalized from the template as of v2.3). The groups:
   - **Fleet** (ask): node-registry rows + stream ownership.
   - **Records & docs** (derive/ask): id families, doc-routing table, product preamble, repo-layout map,
     command catalog, product-context home, help dir, review dir.
   - **Memory tree** (only if §3 chosen): `{{MEMORY_ROOT}}` + `{{MEMORY_DISCIPLINES}}` — else delete them
     and the two §5 memory-tree lines.
   - **Gates & git** (derive): gate commands, CI file, gate runner, commit trailer, worktree script,
     toolchain notes.
   - **Runtime/verification · architecture/design-system · output-discipline** — fill what applies, delete
     what doesn't per the customize companion's conditional-sections list.
3. The customize companion lists the conditional sections to delete when they don't apply; apply that.

**Verify:** `grep -nE '\{\{[A-Z]' <project>/docs/PARALLEL.md <project>/docs/parallel-coding-governance.domain-rules.md`
prints nothing. BOTH files — the companion carries 14 of the 37 placeholders, and a template-only grep
passes green while the §-stubs point at a file the project never filled. The grep is SHAPE-scoped
(`\{\{[A-Z]`) rather than a bare `{{`, because a filled `{{GATE_COMMANDS}}` may legitimately contain
GitHub Actions `${{ }}` expressions; the shipped template contains none, so an unscoped grep is green
today and false-fails the first repo whose gate commands are a workflow. `{{ID_FAMILIES}}` must
match the memory-tree `FAMILIES` (§3) — the build records and the decision logs share one id scheme.

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
   (shipped reinvention, over ALL new code) and routes each to `<MAP_ROOT>/reinvention-backlog.md`
   (deduped); it is a report + WARN, never a merge gate (a token-stem collision has false positives).
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
   bash tools/memory-recall/adopt-memory-recall.sh --scaffold --with-hook   # -> .claude/hooks/recall-opened.js
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
   `last-audit` = ISO-8601 datetime with offset (e.g. `date -Iseconds`) `@` full sha (HEAD on the
   default branch, else `git merge-base <remote>/<default> HEAD`; no remote →
   `git merge-base <local-default> HEAD`); tag claims whose truth lives in another repo
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
   actually pulled FROM — read it out of `<gov>/parallel-coding-governance.template.md`, never from
   this line. Stamping an older number on a newer copy makes the marker lie, and the marker is what
   both the kickoff engine's Step-2 fallback and the re-pull mechanism read.
6. Bump the manifest marker to `kickoff-manifest: v1.3` **LAST** — the bump silences the kit's
   version WARN, the only standing signal that the body still predates the ratchet.

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
- Add a SessionStart hook to `.claude/settings.json` running
  `bash "${CLAUDE_PROJECT_DIR}/tools/check-wiring.sh" --session` (`settings-merge.py` handles only the
  agent-cap block — add SessionStart by hand). It auto-sets an unset `core.hooksPath` and NEVER
  overwrites a deliberate value (e.g. the out-of-tree copy above), so a fresh clone self-heals.
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
  it is a hardcoded list by design, not an enumeration.
- `tools/gate-lint/` — the gate-authoring lints. It ships no legs of its own; its README hands leg
  wiring to the consuming project.
- `tools/push-main.sh` + `tools/push-main.test.sh` + `.githooks/pre-push` — §5 already tells you to
  LAND through the lander, and nothing above copies it in. Do that here.
- `tools/check-install-prefix.sh` + `tools/check-install-prefix.test.sh` — only if your project also
  ships kits onward. It polices the SHIPPING surface, not an installed one.

**Concurrency guard (recommended for ANY project that fans out `Workflow` agents — playbook §8):**
- Copy `tools/hooks/agent-cap.js` (+ `tools/hooks/agent-cap.test.sh`) into the project (e.g. `<project>/.claude/hooks/`).
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
  It DENIES any `Workflow` script that calls raw `parallel(`/`pipeline(` instead of the cap-5
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
- Verify all five workflow legs, not two — the dogfood bar runs every one of these:
  `bash <project>/.claude/hooks/agent-cap.test.sh` · `bash <project>/tools/workflows/check-protocol-parity.test.sh` ·
  `bash <project>/tools/workflows/check-verifier-fanout.sh` · `bash <project>/tools/workflows/check-review-join.sh` ·
  `node <project>/tools/workflows/check-workflow-syntax.js` — each → exit 0.

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

## Result — what the project now has

```
<project>/
├── AGENTS.md / CLAUDE.md        # (optional) project charter / agent-instruction file (agent-instructions kit)
├── docs/PARALLEL.md             # governance playbook, filled (governance-template marker kept)
├── docs/parallel-coding-governance.domain-rules.md  # the §4/§9–§13 domain checklists (travels with the template)
├── memory/guides/SESSION-KICKOFF.md  # kickoff manifest (v1.3: audit block + sealed §A region) — the engine reads this
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
  `.claude/skills/memory-recall/SKILL.md` (+ `.claude/hooks/recall-opened.js`, `tools/settings-merge.py`
  and the settings block only if the step-4 opt-in was taken). The index and query log live under the
  common git dir, never in the worktree — nothing to ignore, nothing to commit.

## Maintenance

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

- **memory-recall is three maintenance classes, not one** — `bench.py` and `union.py` are byte-identical
  upstream copies (their sha prefixes are pinned in `verbatim.json` and gated by the kit selftest):
  overwrite them wholesale. `extract.py`, `query.py` and `recall-opened.js` are FORKS — each carries a
  header naming the upstream path and sha it was taken from, so a re-pull is a three-way merge, not
  archaeology. `recall_conf.py`, `selftest.py`, `SKILL.template.md`, `adopt-memory-recall.sh` and the
  fragment are this kit's own. Never overwrite the RENDERED `.claude/skills/memory-recall/SKILL.md` by
  hand — re-run `--scaffold`, which is what `--check` grades. After any `FAMILIES`/`MEMORY_ROOT` edit,
  re-run `--scaffold`; the cache invalidates itself on the resolved conf, so no manual purge is needed.

- **Precedence on any conflict:** `CLAUDE.md` > manifest > skill — follow the winner, fix the loser.
- **Pull upstream improvements:** the playbook carries `governance-template: vN.N`; re-pull by diffing your
  filled copy against `<gov>/parallel-coding-governance.template.md` per §-body (ignore filled
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
  read the customize companion's conditional-sections row first — the mandate clauses are keyed on
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
