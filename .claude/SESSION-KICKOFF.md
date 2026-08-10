# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.1 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-08-10T21:34:11+03:00 @ 16aeb5efe98083c31a927a73541644020ee6bb57
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; parallel-coding-governance.template.md
verify-paths: AGENTS.md; parallel-coding-governance.template.md; README.md
check-script: skills/session-kickoff/manifest-check.sh
-->

The project layer read by the generic `/session-kickoff` skill. Precedence on conflicts:
**`AGENTS.md`/`CLAUDE.md` > this file > the skill**. This repo dogfoods its own kits, so the manifest
here is short — `AGENTS.md` (the charter) holds the substance.

## The ratchet — how this file stays true

- Every kickoff audits this file (`manifest-check.sh`, at `check-script:`) and repairs drift on the spot.
- Every unit that changed what this file front-loads (a gate command, entrypoint, governing doc, a
  trap hit, a doc/memory claim found stale, or a fact re-derived it should have front-loaded) re-stamps
  `last-audit` with a delta line in the commit message; no delta → no touch.
- Stamp rule: sha = `HEAD` on `main`, else `git merge-base origin/main HEAD`; datetime always advances.
- Dated entries carry a prune-when condition and are deleted once it holds.

## §A — Task (the agent DERIVES this per kickoff — the user does NOT fill it)

> - **Title / Goal / IN scope / OUT / Acceptance / Gates it must pass / Risk tier** — derived from
>   the `/session-kickoff` message + the adjacent memory (`memory/DECISIONS.md`, `memory/backlog/`,
>   `memory/builds/<slug>/`) and the code.

## §B — Orientation (derived at instantiation; re-audited every kickoff; accretes)

- **Repo layout:** primary checkout at `C:/projects/coding-governance` (holds `main`), plus per-unit
  worktrees under `.claude/worktrees/<branch-slug>/`. `git worktree list` is the inventory. A unit
  branch's commits ride its own worktree, never the primary tree (the pre-commit branch guard refuses).
- **Remote · default branch:** `origin` · `main`.
- **Branch conventions:** small units on `main` for a solo tooling repo; `git push` needs an explicit ask.
- **Governing docs:** `AGENTS.md` (the charter — authoritative) · `parallel-coding-governance.template.md`
  (the playbook this repo follows + ships) · `memory/DECISIONS.md` + `memory/backlog/<FAMILY>.md`.

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/DECISIONS.md` §PLAY · `memory/backlog/PLAY.md` | `parallel-coding-governance.template.md` + `.customize.md` + `.domain-rules.md` · `tools/check-template-size.sh` |
| kickoff (`KICK-`) | `memory/DECISIONS.md` §KICK · `memory/backlog/KICK.md` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/DECISIONS.md` §TOOL · `memory/backlog/TOOL.md` | `tools/` — read the dir, not this cell; kits self-describe in their own `README.md` |
| deployer (`DEPL-`) | `memory/DECISIONS.md` §DEPL · `memory/backlog/DEPL.md` | `WIRE-INTO-PROJECT.md` · `memory/builds/aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates.sh    # runs all legs, single-sourced from tools/gate-legs.json — read THAT for the list, not this line
python tools/memory-tree/gotchas.py --for-diff <base>..<head>   # the recurring-bug-class checklist for THIS diff — run it before a review
python tools/drift-audit/drift_report.py   # ~seconds, no agents: do this repo's own RECORDS still match reality? Run it before theorizing about drift
```

The repo HAS a codebase map (`memory/map/`), so the kickoff skill's map steps are live. No
environment is needed — the engine resolves this repo's `tools/` install prefix itself:

```bash
python tools/codebase-map/map_diff.py <old>..<new>          # Step 1: what a fast-forward brought in
python tools/codebase-map/reuse_lookup.py "<behaviour>"     # Step 4 / §10: the seam to wire through
```

### Tier rule

Tier 2 (spec + adversarial review before building) for: a change to the governance template's rules,
the manifest-check gate semantics, or a new/changed kit's contract; a cross-kit change. Otherwise
Tier 1 (gates + one focused self-review).

### ID + work-state protocol

`FAMILY-<slug>-<seq>`, families `PLAY`/`KICK`/`TOOL`/`DEPL` (per `.memory-tree.conf`). Slug = node tag
(`a`) + CamelCase adjective-noun, minted once per session; collision-grep `memory/`. Work state is
READ from the GENERATED `memory/LIVE.md` + `memory/ledger/<month>.md` (`gen_build_index.py --write`
re-renders them from build front matter); there is no authored ledger to update. Build folders are
`memory/builds/<slug>/`; the discipline is the spec header's `streams` value (`STREAMS_CUTOFF` in
`.memory-tree.conf` arms it).

### Current posture — dated corrections

*Correction OVERRIDES a stale doc/memory claim until fixed; entry: `<date> · <stale where> · <the
correction> · prune when <condition>`. Starts empty; prune per-entry, never delete the section.*


### Environment traps worth front-loading

*Accretes — append the trap that cost time, prune the one that stopped being true.*

- The template is under a STRICT 32 KiB gate — never raise the limit; externalize to a companion instead.
  It sits at 32688/32768 (**80 bytes free** at v2.5, measured 2026-08-10 by `bash tools/check-template-size.sh`
  — read that number FROM the gate, never from here), so a line added to it either fits that margin or
  funds itself by moving prose into `parallel-coding-governance.domain-rules.md`.
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with `git diff --cached --check`.
- A gate that BYTE-COMPARES a generated file needs both halves: an `eol=lf` pin so the committed
  bytes are right, AND CR normalisation in the comparison so a Windows checkout does not red every
  line. Either alone leaves the file green only right after a render.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook enforces TWO rules: route fan-out through the cap-5 helpers, AND a
  review's verify stage spawns at most 5 agents TOTAL. Concurrency is not a budget —
  `boundedParallel(t, 5)` still spawns N agents for N findings, five at a time. Bound the group
  COUNT: `chunk(x, Math.ceil(x.length / MAX_VERIFIERS)) // gov:fixed-verifiers`. Binding rules:
  `memory/guides/REVIEW-PROTOCOL.md`. Ready-made harness: `tools/workflows/tier2-review.js`.
- A new gate PREDICATE is run over the real tree BEFORE it is trusted. Both source-level bans added
  in `TOOL-aBatchedLintel-1` were wrong on their first run — the interval ban matched the `) {`
  opening each if-block, and the `LC_ALL` ban fired on the comment explaining the ban.
- A CRLF fixture cannot test a CR guard on a Cygwin node: the runtime strips CR before `awk` sees a
  byte, through a filename argument, through `getline` AND through a pipe. Assert at source level.
- A `git worktree` checkout can land CRLF on a path `.gitattributes` pins `eol=lf`, and `git status`
  stays CLEAN because the index normalises on commit. Symptom: a gate that diffs a rendered file
  against a fresh render reports EVERY line as drift on a file the session never touched. Seen on
  `.claude/skills/memory-recall/SKILL.md` (2026-08-08); `rm` plus `git checkout --` restores LF.
- `node --check <file>` is NOT a syntax gate on node v24: module auto-detection retries the parse and
  swallows the failure, so it exits 0 on a file whose parse genuinely fails. Parse a workflow script
  by constructing an `AsyncFunction` from it — `tools/workflows/check-workflow-syntax.js`.
- `subprocess.run(["bash", …])` from Python resolves the SYSTEM32 WSL launcher on this node, not
  git-bash. WSL sees a different filesystem: an existing path reports `No such file or directory` and
  a relative path resolves under `/mnt/c/`. Name the executable — see `resolve_bash()` in
  `tools/memory-tree/corpus_ids.py`; `GOV_BASH` overrides.
- Generating source through a shell heredoc into a NON-raw Python string turns an escape into a
  CONTROL BYTE in the written file. A ``\b`` becomes a backspace, the compiled regex silently stops
  matching, and printing the pattern shows nothing wrong — only `repr()` does. Hit three times on
  2026-08-08 with three different misleading symptoms. Write source with a file tool or a raw string,
  and sweep TRACKED AND UNTRACKED files when repairing.
- A kit that resolves the repo root by counting directories UP from itself breaks at any install
  prefix but the one it assumed, and it breaks SILENTLY — codebase-map answered from an empty corpus
  printing "no seam fits" and "mapped 0/N". Fixed in the engine (`resolve_root` walks up for the
  conf, bounded by `.git`), and the `CODEBASE_MAP_ROOT` workaround that preceded it is now BANNED by
  the kit's own selftest. Kept as a trap because the class outlives the instance: this repo installs
  every kit under `tools/`, so a kit written against a root install is wrong here by one segment.
- Two memory-tree spec-authoring traps, both found by hitting them. A build README's `roster:` is
  `+`-JOINED (`PLAY+TOOL`); a space-joined value reds check 9 with "roster value 'PLAY TOOL' is
  outside the FAMILIES set", which reads like a families misconfiguration rather than a separator.
  And check 12's skeleton scan matches the literal `YYYY-MM-DD` or `<FAMILY-slug-seq>` ANYWHERE in a
  spec body — so QUOTING a stale artifact that contains one reds the spec as an unfilled skeleton.
  Paraphrase the quoted shape (`builds/<date>-<FAMILY>-<slug>/`) instead.
- A new tool placed at the REPO ROOT rather than under `tools/` silently leaves the enforced surface.
  `check-arms.py`, `check-review-join.sh` and `check-workflow-syntax.js` are all scoped to `tools/**`;
  `map_extractors._tool_kits()` enumerates `tools/*` and nothing else, so a root dir is in no
  codebase-map inventory and demands no dossier; and it falls outside drift-audit's PRODUCT_GLOBS.
  Nothing reds — the tool is simply ungoverned. Put new tooling under `tools/<name>/`.
- Adding ONE gate leg trips FOUR gates at once, and they are worth doing in one pass rather than
  serially: the codebase-map `gate-legs` coverage assert (claim the leg in a dossier), the
  codebase-map freshness byte-compare (re-render `MAP.md` + `inventories.json`), the kickoff-manifest
  ratchet (`tools/gate-legs.json` is a watched pathspec, so `last-audit` re-stamps), and drift-audit's
  handkept signal (cite the leg's script path in this charter's `## The gate suite` section). That
  last one has ZERO slack — the pin is 7 of 40 at tolerance 0, so an uncited leg 41 reds immediately.
- A kit path a tool WRITES, RENDERS or PRINTS is DERIVED from that tool's own location, never
  spelled. Three shapes ship here: shell `KIT_REL=${HERE#"$ROOT_N"/}` with both sides normalised
  through the same `cd … && pwd` chain (`adopt-memory-tree.sh`), python `kit_rel()` walking up for
  `.git` (`gen_build_index.py`), and brace-delimited KIT_DIR / TOOL_ROOT placeholders rendered at
  scaffold time (`HYGIENE.template.md`; the literal token shape is omitted here because the manifest
  ratchet's check 1 scans this file for exactly it). A hardcoded prefix in a RENDERED artifact is the worst case — it
  lands a dead path in the adopter's own committed tree and the byte-compare that guards the file
  agrees with it.
- Under MSYS/git-bash one directory has two spellings (`/tmp/x` vs `/c/.../Temp/x`) and mount points are
  NOT symlinks — never compare path strings (or `realpath --relative-to` outputs) across those flavors;
  decide repo membership via git identity (`rev-parse --show-toplevel`/`--show-prefix`), both sides
  normalized through the same `cd … && pwd` chain.
