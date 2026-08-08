# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.1 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-08-08T22:15:00+03:00 @ 6ff9a73165cddf6afa7daa7e17f2c030e35009aa
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

- **Repo layout:** single checkout at the repo root (`C:/projects/coding-governance`); no worktree fan.
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

### Tier rule

Tier 2 (spec + adversarial review before building) for: a change to the governance template's rules,
the manifest-check gate semantics, or a new/changed kit's contract; a cross-kit change. Otherwise
Tier 1 (gates + one focused self-review).

### ID + ledger protocol

`FAMILY-<slug>-<seq>`, families `PLAY`/`KICK`/`TOOL`/`DEPL` (per `.memory-tree.conf`). Slug = node tag
(`a`) + CamelCase adjective-noun, minted once per session; collision-grep `memory/`. Ledger:
`memory/project/in-flight/<tag>.md`. Build folders are `memory/builds/<slug>/`; the discipline is the
spec header's `streams` value (`STREAMS_CUTOFF` in `.memory-tree.conf` arms it).

### Current posture — dated corrections

*Correction OVERRIDES a stale doc/memory claim until fixed; entry: `<date> · <stale where> · <the
correction> · prune when <condition>`. Starts empty; prune per-entry, never delete the section.*

- *(none yet)*

### Environment traps worth front-loading

*Accretes — append the trap that cost time, prune the one that stopped being true.*

- The template is under a STRICT 32 KiB gate — never raise the limit; externalize to a companion instead.
  It now sits at 32758/32768 (**10 bytes free**, measured 2026-08-03), so the next line added to it must
  fund itself by moving prose into `parallel-coding-governance.domain-rules.md`.
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with `git diff --cached --check`.
- A gate that BYTE-COMPARES a generated file needs both halves: an `eol=lf` pin so the committed
  bytes are right, AND CR normalisation in the comparison so a Windows checkout does not red every
  line. Either alone leaves the file green only right after a render.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook caps Workflow fan-out at 6 concurrent — route fan-out through the cap-6 helpers.
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
- Under MSYS/git-bash one directory has two spellings (`/tmp/x` vs `/c/.../Temp/x`) and mount points are
  NOT symlinks — never compare path strings (or `realpath --relative-to` outputs) across those flavors;
  decide repo membership via git identity (`rev-parse --show-toplevel`/`--show-prefix`), both sides
  normalized through the same `cd … && pwd` chain.
