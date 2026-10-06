# TOOL-aMendedFleet-94 — the wrapper's product-only prose loads from a path-scoped rule when a session opens a product file

**Status:** CLOSED · rev-3 · 2026-10-06 · node a · Tier-2 · base 7af5f564 · streams tooling+playbook · ratified 2026-10-04 · order 95

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-94-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-94-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`AGENTS.md` loads whole into every session and every unit agent. Part of its authored wrapper binds
only while a session works on the product: the `## What ships here (the product)` section, 2453
bytes at base, and two `## Conventions` bullets about where kits live and the template's byte
ceiling. A session filing records under `memory/` pays for them anyway. Claude Code loads a file
under `.claude/rules/` whose `paths` frontmatter matches a file the session opens, and only then.
This unit moves that product-only prose into one such rule, leaves a pointer in the wrapper that
says when it loads, and observes the CLI loading it. The report's ordering holds: it runs after the
diet units 67, 68, 79 and the A/B unit 93, so it moves the wrapper as those left it (§8 F2).

## 2. Scope (IN)

- **S1** — A new rule file, `.claude/rules/product.md`, opens with YAML frontmatter whose `paths`
  list carries four entries: `tools/**`, `skills/**`, `coding-governance-agents.template.md` and
  `WIRE-INTO-PROJECT.md`. Below it sit an H1, then the body of the wrapper's
  `## What ships here (the product)` section verbatim as it reads at the unit's own base, then the
  two Conventions bullets S2 moves here, verbatim. Observed by AC1 and AC2.
- **S2** — In `AGENTS.md`, the `## What ships here (the product)` heading stays and its body is
  replaced by one paragraph of at most 400 bytes. It names `.claude/rules/product.md`, says Claude
  Code loads it when a session opens a file under `tools/` or `skills/`, the template or the
  runbook, and says a tool that does not read `.claude/rules/` should read the file directly. The
  Conventions bullets opening "Kits live in `tools/`" and "The template is the operating ruleset"
  are removed from the wrapper, because S1 carries them. Observed by AC2 and AC3.
  **Readers:** by name: `AGENTS.md` alone spells the two bullets and the section body, and the
  section heading is kept, so a reader citing it by name still lands on it. by value: NO VALUE
  READERS — no checker parses the wrapper's prose; `tools/check-template-size.sh` measures the
  file's bytes, which AC3 observes falling.
- **S3** — The charter's byte high-water in `tools/template-size-highwater.txt` is re-recorded with
  `bash tools/check-template-size.sh --bump AGENTS.md` at the shrunk size, so regrowth toward the old
  figure prints that gate's WARN. Observed by AC3.
- **S4** — The rule loads, observed once through the CLI's own `InstructionsLoaded` hook event, which
  reports a `path_glob_match` load reason with the globs that matched. Observed by AC4.

## 3. Non-goals (OUT)

- Moving any part of the RENDERED `gov:playbook` region. Its lexicon naming bullets and its §11 are
  the obvious area-scoped candidates, but they are template text: routing a template block into a
  rule file needs either a renderer route, a new deploy-time surface, or a hand-kept second copy of
  template text, which is the stale-copy class (§8 F1).
- Rules tied to running a command, such as the merge bar. The report lists them under do-not-build,
  because a command has no path to trigger on.
- A standing gate that every rule's globs match a tracked file. One rule with four literal globs is
  observed by AC1; a checker is owed when a second rule file lands, and is the class to gate then.
- A byte ceiling row for the rule file in `tools/template-size-limits.txt`. The rule loads only on a
  path match, and a ceiling that nothing reaches is a number nobody questions.
- The `## Layout` and `## Node registry` sections, which orient every session; the node registry is
  unit 97's.
- Measuring a per-session token saving. The commit records the byte delta, and unit 93 owns the A/B.

### Edges

- **consumes-from** `TOOL-aMendedFleet-74` — the path-scoped-rules half of the report's point, split
  to this unit at that unit's §8 F1, with the rule-loading facts it first read from the PATH CLI.
- **hands-off** external — routing rendered template blocks into path-scoped rules, which needs a
  renderer route this build's grant does not reach.
- **hands-off** external — a standing check that each rule's `paths` globs match a tracked file, owed
  once a second rule file exists.

## 4. Design

### Evidence

Read at base `7af5f564`; `AGENTS.md` is byte-identical at the worktree tip `8312d315`.

- The running session's CLI, 2.1.286, and the PATH CLI, 2.1.178, both carry the sentence that
  `.claude/rules/` files "can be scoped to specific file paths using `paths` frontmatter", read with a
  read-only `grep -a -o` over each binary on 2026-10-04. Both carry the `InstructionsLoaded` hook
  event, whose payload holds `file_path`, `memory_type`, `globs` and a `load_reason` from the closed
  set `session_start`, `nested_traversal`, `path_glob_match`, `include` and `compact`. The bundled
  loader sets `path_glob_match` when the loaded file carries globs. PINNED 2026-10-04.
- This repository has no `.claude/rules/` directory, and `git grep` over `tools/` and `skills/`
  names none.
- `awk` over `AGENTS.md` sizes the wrapper's sections at base: What ships here 2453 bytes, Layout 950,
  Node registry 2144, Conventions 1096. PINNED 2026-10-04; the build re-measures after unit 79 moved
  its part. Unit 97, which reshapes the Node registry, is ordered after this unit.
- `tools/agent-instructions/` wires `AGENTS.md` as canonical with `CLAUDE.md` an import, and the
  `agent-instructions wiring` leg runs it with `--aliases claude` alone, so Claude Code is the one
  tool this repository declares. A rule file is read by Claude Code only, which is why S2's pointer
  names the file for any other tool.
- Hygiene check 16 counts charter pointers under `MEMORY_ROOT` only, so a pointer at `.claude/rules/`
  adds no read-path member. `tools/check-dead-paths.sh` scans every tracked file outside `memory/`,
  so the moved text stays under the deleted-file check.
- The codebase map inventories `.claude/skills` and not `.claude/rules`, so the rule is no unclaimed
  key.

### The rule file

```markdown
---
paths:
  - "tools/**"
  - "skills/**"
  - "coding-governance-agents.template.md"
  - "WIRE-INTO-PROJECT.md"
---

# What ships here — the product, loaded when you open a product file

<the What ships here body, verbatim>

<the two Conventions bullets, verbatim>
```

### The wrapper pointer

Under the kept heading, the whole body:

```markdown
What this repository ships, kit by kit, is `.claude/rules/product.md`. Claude Code loads it when a
session opens a file under `tools/` or `skills/`, the charter template or `WIRE-INTO-PROJECT.md`;
any other tool reads that file directly before touching one.
```

About 300 bytes. The ESTIMATED net shrink is about 2.4 KB; AC3 derives it.

### Files touched (estimate)

- `.claude/rules/product.md`
- `AGENTS.md`
- `tools/template-size-highwater.txt`

### Rollout

One commit carrying the rule, the trimmed wrapper and the bump. The wrapper and the rule are gov's own
and no adopter receives either, so nothing ships and no kit version moves.

### Alternatives rejected

- **A pointer to a guide under `memory/guides/`.** That is the §-stub shape the v3.0 convergence
  removed, because a file a session must choose to open kept falling out of reach. A rule loads
  without that choice, which is the whole difference.
- **Keep the section and add a rule beside it.** Two copies of one text, with no saving.
- **One rule per area.** The two moved bullets bind on the same paths as the section, so a second
  file would load at the same moments for no gain.

## 5. Production-readiness checklist

- security — N/A — prose moved between two tracked files; the rule carries no tool permission and no
  hook.
- perf / scale — every session that opens no product file reads about 2.4 KB less, ESTIMATED; one that
  does reads the same bytes as before.
- error / empty / loading states — a glob matching nothing loads the rule never, silently, and a
  misspelt `paths` key loads it at EVERY session start, unscoped, with `load_reason` `session_start`;
  AC1 observes every glob, and AC4 observes the scoped load.
- observability — the CLI's `InstructionsLoaded` event names every load, with the matching globs.
- risks — an agent that greps product files through Bash without opening one never triggers the
  load, and whether a Workflow sidechain agent loads path rules is UNVERIFIED. Both lose the
  kit-by-kit list, which a spec or brief names anyway; the pointer says where it lives.
- testing — AC1 to AC4 directly; no suite owns a rule file.
- migration — N/A — no stored state.
- user docs — N/A — the wrapper is the repository's own working guide, and the pointer is its doc.

## 6. Acceptance criteria

- **AC1** — When `sed -n 1,8p` over the rule file S1 names runs, it prints a frontmatter block opened and
  closed by `---` whose `paths` list holds the four globs of S1; and for each glob,
  `git ls-files --` followed by that glob, piped to `head -1`, prints a tracked path.
  Red when: a glob matches no tracked file, staged by spelling `tool/**` for `tools/**`, which makes
  that glob's listing empty.
- **AC2** — When the section body is cut from the base `AGENTS.md`, read with `git show`, between the
  `## What ships here` and `## Layout` headings, and compared with `diff` against the rule body between
  its H1 and the first moved Conventions bullet, there is no difference; and
  `grep -c -e "Kits live in" -e "keep it ≤48 KiB" AGENTS.md` prints 0 while the same grep over the
  rule prints 2.
  Red when: the move rewrote a sentence, dropped one, or left a bullet behind in the wrapper.
- **AC3** — When `bash tools/check-template-size.sh AGENTS.md` runs after S3's bump, it exits 0, prints
  no WARN line and a byte figure lower than the base by at least the moved bytes less 400; and
  `grep -n "^AGENTS.md" tools/template-size-highwater.txt` prints that same figure; and the wrapper
  section measured by `awk '/^## What ships here/,/^## Layout/' AGENTS.md` piped to `wc -c` is at most
  450 bytes, heading included.
  Red when: the charter did not shrink, the pointer outgrew its budget, or the high-water was left at
  the pre-trim figure.
  figure: the base and post-trim byte counts are DERIVED by the run; 400 and 450 are PINNED here.
- **AC4** — When a scratchpad settings file declaring one `InstructionsLoaded` command hook that
  appends its stdin to a scratchpad log is passed as `claude -p --settings <file>` from this tree, with
  a prompt asking the session to Read `tools/lib/resolve-python.sh` and reply with its first line, the
  log carries a record whose `load_reason` is `path_glob_match` and whose `file_path` names the rule
  file S1 adds.
  Red when: the CLI does not load the rule on a matching open, staged by renaming the frontmatter key
  `paths` to `path`, after which the same run logs no such record.
  cost: one short headless session, about a minute and the tokens of one charter load, run twice for
  the staged break.
  permission: a nested headless session; where the pass may not start one, it returns this
  observation to the main loop rather than skipping it, and says so.

## 7. Gates

`charter size` · `line length` · `agent-instructions wiring` · `check-wiring self-test` · `lexicon naming predicates` · `dead-path carriers (deleted files still named)` · `playbook render wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The two `.claude/` legs are owed by S1's path; neither grades markdown, and both run once at the
close.

## 8. Open questions

- **F1 — Which always-loaded prose moves?**
  Options: the wrapper's product-only prose; rendered template blocks, routed into rules by the
  renderer; rendered blocks dropped from the render with an authored rule holding the same text. The
  second is a new deploy-time surface for every adopter, which veto 2 reserves to the owner and the
  diet grant does not name. The third is a hand-kept copy of template text, the stale-prose class.
  RESOLVED (agent, 2026-10-04, delegated): the wrapper's product-only prose, per S1 and S2.
- **F2 — Does the diet measurement gate this unit?**
  The report orders this point after its items 14, 15 and 20 are measured, the brief after units 67,
  68, 79 and 93. Unit 93 measures whether workflow judges need the charter at all; this unit moves
  wrapper prose an editing session needs only on product paths, so the A/B cannot change the pick.
  What the ordering buys is a wrapper that unit 79 has already reshaped, so the moved bytes
  and the byte delta are measured once, on the final text.
  RESOLVED (agent, 2026-10-04, delegated): build at order 95, moving the section as it reads at the
  unit's base, with no condition on unit 93's verdict.
- **F3 — Does a Claude-only carrier break the canonical-file rule?**
  The charter's §6 makes one file canonical so every tool reads one text. This repository declares
  Claude Code alone, and the moved prose stays in one file, named by the canonical one.
  RESOLVED (agent, 2026-10-04, delegated): move it, with S2's pointer naming the file for any other
  tool.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; split from unit 74 at its F1, the CLI's rule loading read from
  both binaries, and the wrapper's sections sized at base.
- rev-2 · 2026-10-04 · §3 · §4 · §8 · M2 cross-read: the split from unit 74 is now a declared
  consumes-from `TOOL-aMendedFleet-74`, reciprocal to its hands-off; §4 said unit 97 moves its part
  before this unit re-measures, but unit 97 is ordered after it; §8 F2 named unit 68 as reshaping
  the wrapper, which edits the unattended Skill and not `AGENTS.md`.
- rev-3 · 2026-10-06 · §5 · the build pass observed AC4's staged break: the CLI read a rule whose
  key was spelt `path` as an unscoped rule and loaded it at session start, so §5's "a malformed
  frontmatter loads the rule never" was wrong for that malformation; AC4's red still holds, since
  no `path_glob_match` record names the file.

## 10. Reuse audit

No existing seam fits: this repository has no `.claude/rules/` directory and no code loads area
rules, so the seam is the CLI's own rule loader, extended only by data. `python
tools/codebase-map/reuse_lookup.py "load area-specific instructions only when an agent opens files
under that path"` returned only `load_conf`, `load_corpus` and other `load_*` name-stem neighbours,
none of which reads instructions; `git grep -n "rules/"` over `tools/`, `skills/` and `.claude/`
found nothing. Recall returned the aFusedCharter convergence record and `PLAY-aCandidStub-2`, which
together say a pointer a session must CHOOSE to follow falls out of the deploy path and that a stub
needs an activity trigger; a path-scoped rule has the trigger and needs no choice, which is why §4
rejects the guide shape. It also returned unit 74's spec, which first read the rule facts from the
PATH binary. Where the report and the tree disagree: the report pairs this point with a budgeted
pre-build checklist, which unit 74 keeps, and calls the editing areas "rules"; nothing in the tree
holds any yet.

Recall terms used: `python tools/memory-recall/query.py "should area-specific charter rules load
only when a session touches files in that area instead of always" --terms "path-scoped rules
.claude/rules paths frontmatter editing areas context diet always-loaded charter wrapper AGENTS.md
externalize InstructionsLoaded"`
