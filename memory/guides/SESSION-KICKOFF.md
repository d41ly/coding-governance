# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.3 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-08-15T18:30:00+03:00 @ 709d260da8c81551e59da769aceca47202bb5923
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; parallel-coding-governance.template.md; skills/session-kickoff/SKILL.md; .unattended.conf; memory/guides/BUILD-METHOD.md
verify-paths: AGENTS.md; parallel-coding-governance.template.md; README.md; memory/guides/BUILD-METHOD.md
last-body-change: 5fd7c7efaa3942ea5fd77777c74bbee7ef132787
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

Derived from the `/session-kickoff` message plus the adjacent memory (`memory/DECISIONS.md`,
`memory/backlog/`, `memory/builds/<slug>/`) and the code. The field set below is SEALED — check 10
byte-compares it against the contract `manifest-check.sh` carries, so editing it here reds the bar.
Restore it with `bash skills/session-kickoff/manifest-check.sh --task-skeleton`. The tier lives in
§B's tier rule, not here.

<!-- kickoff:task -->
> - **Title:** …
> - **Goal (1–2 sentences):** …
> - **IN scope:** …
> - **OUT / non-goals** (explicit cut-line): …
> - **Acceptance check** (the observation that proves THIS change — a test it adds, a gate it
>   moves, an observed behavior; *not* an unrelated green check): …
> - **Gates it must pass:** …
<!-- /kickoff:task -->

## §B — Orientation (derived at instantiation; re-audited every kickoff; accretes)

- A build of more than one pass runs on `memory/guides/BUILD-METHOD.md` — the spec set, the fork
  rule, the pass loop, regrounding, the closing review and the wrap-up derivation. It is rendered by
  the memory-tree kit and is in `watch:`, so editing it forces this manifest to be re-audited.

- **Repo layout:** primary checkout at `C:/projects/coding-governance` (holds `main`), plus per-unit
  worktrees under `.claude/worktrees/<branch-slug>/`. `git worktree list` is the inventory. A unit
  branch's commits ride its own worktree, never the primary tree (the pre-commit branch guard refuses).
- **Remote · default branch:** `origin` · `main`.
- **Branch conventions:** small units on `main` for a solo tooling repo; `git push` needs an explicit
  ask, or a build folder committed before the run's branch existed (`memory/guides/UNATTENDED-PROTOCOL.md`).
- **Governing docs:** `AGENTS.md` (the charter — authoritative) · `parallel-coding-governance.template.md`
  (the playbook this repo follows + ships) · `memory/DECISIONS.md` + `memory/backlog/<FAMILY>.md`.
  Two BINDING guides: `memory/guides/REVIEW-PROTOCOL.md` (fan-out) and
  `memory/guides/UNATTENDED-PROTOCOL.md` (a run that merges and pushes with no owner turn).

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/DECISIONS.md` §PLAY · `memory/backlog/PLAY.md` | `parallel-coding-governance.template.md` + `.customize.md` + `.domain-rules.md` · `tools/check-template-size.sh` |
| kickoff (`KICK-`) | `memory/DECISIONS.md` §KICK · `memory/backlog/KICK.md` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/DECISIONS.md` §TOOL · `memory/backlog/TOOL.md` | `tools/` — read the dir, not this cell; kits self-describe in their own `README.md` |
| deployer (`DEPL-`) | `memory/DECISIONS.md` §DEPL · `memory/backlog/DEPL.md` | `WIRE-INTO-PROJECT.md` · `memory/builds/aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates.sh    # runs all legs CONCURRENTLY (width min(8,nproc)), single-sourced from tools/gate-legs.json — read THAT for the list, not this line
GATE_JOBS=1 bash tools/run-gates.sh   # the serial bar, same code path — the rollback for a suspected concurrency problem
GATE_FULL=1 bash tools/run-gates.sh   # ignore every leg guard — what .githooks/pre-push runs, and what a DoD needs
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

*One line each; link out for detail — check 11 enforces it at 400 bytes per bullet. A recurring BUG
CLASS does not belong here at all: it belongs in `memory/gotchas/`, where `gotchas.py --for-paths`
puts it on the checklist for the areas a unit actually touches.*

Evicted to the catalogue, and reachable from it: `gate-green-by-accident-on-generated-bytes.md`
(an eol pin without a normalising comparison, and the worktree checkout that lands CRLF on a pinned
path) · `absence-assertion-over-whole-file-text.md` (a new gate predicate run for the first time
against the real tree) · `subprocess-resolves-a-different-shell.md` · `heredoc-escape-reaches-the-regex.md`
· `assertion-between-two-derived-values.md` (a core-subset-of-effective assertion the checker itself
composes) · `inputs-inside-the-subjects-reach.md` (what SUPPLIES each of a check's inputs).

- The template is under a STRICT 32 KiB gate. Never raise it; externalize into
  `parallel-coding-governance.domain-rules.md` instead. Read the current margin FROM
  `bash tools/check-template-size.sh`, never from prose — it moved twice in one day.
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with
  `git diff --cached --check`.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook is wired on `Workflow|Agent` (kit 1.4) and enforces four rules;
  the bound is a FILE CONSTANT and `AGENT_CAP` is refused, not honoured. Binding rules:
  `memory/guides/REVIEW-PROTOCOL.md`. Ready-made harness: `tools/workflows/tier2-review.js`. The
  concurrency half of this trap is `memory/gotchas/concurrency-is-not-a-budget.md`.
- Editing `.claude/settings.json` takes effect MID-SESSION — hooks are re-read, not snapshotted at
  start. Measured 2026-08-10 with a throwaway `PreToolUse` hook that fired on the call which checked
  for it. Do not skip the liveness half of such a probe.
- A CRLF fixture cannot test a CR guard on a Cygwin node: the runtime strips CR before `awk` sees a
  byte, through a filename, through `getline` AND through a pipe. Assert at source level.
- `node --check <file>` is NOT a syntax gate on node v24 — module auto-detection retries the parse and
  swallows the failure. Parse by constructing an `AsyncFunction`: `tools/workflows/check-workflow-syntax.js`.
- A kit that resolves the repo root by counting directories UP breaks SILENTLY at any other install
  prefix — codebase-map answered from an empty corpus. Walk up for the conf, bounded by `.git`.
- A build README's `roster:` is `+`-JOINED (`PLAY+TOOL`); a space-joined value reds check 9 with a
  message that reads like a families misconfiguration.
- Hygiene check 12's skeleton scan matches a literal date-shape or id-shape ANYWHERE in a spec body,
  so QUOTING a stale artifact that contains one reds the spec. Paraphrase the shape instead.
- A new tool at the REPO ROOT rather than under `tools/` silently leaves the enforced surface: the
  source-level gates, the codebase-map inventories and drift-audit's globs all scope to `tools/**`.
- Adding ONE gate leg trips FOUR gates at once, worth doing in one pass: the codebase-map coverage
  assert, the map freshness byte-compare, the kickoff-manifest ratchet, and drift-audit's handkept
  signal — which is pinned at 0 of 53 with ZERO slack, so an uncited leg reds immediately.
- A kit path a tool WRITES, RENDERS or PRINTS is DERIVED from that tool's own location, never spelled.
  A hardcoded prefix in a RENDERED artifact is the worst case: it lands a dead path in the adopter's
  committed tree and the byte-compare guarding that file agrees with it.
- A gate that returns a VALUE on stdout cannot also report on stdout — `fail` echoes, so `x=$(check …)`
  captures the diagnostics and the operator sees only the downstream symptom. Use a separate channel.
- CRLF in a worktree is NOT limited to what a gate byte-compares, and `check-wiring.sh` will not tell
  you: its eol population is scoped to `.claude/` paths carrying the pin. Ask which CONSUMER reads a
  file whole (a launcher, a sourced conf, a hook), not which gate diffs it.
- A NEW record under `memory/gotchas/` needs `gotchas.py --write` AND a dossier claim, and the
  coverage inventory reads TRACKED files — so `git add` first, then measure, or the gap surfaces on
  the full bar instead.
- Template parity and PLACEHOLDER COMPLETENESS are two different questions. A render whose conf
  declares nothing for a key is byte-identical to a fresh render and still tells the agent to invoke a
  placeholder's name as a tool. Grep the render for a surviving brace-shape as its own arm.
- An arm must contain the branch's ENTIRE literal signature — a readable PREFIX of a long message
  reds — and a literal word between the sentence and the first interpolation is part of it, so end
  the sentence and let only interpolations follow. Adding branches RENUMBERS the per-check
  ordinals, invalidating any `unarmed-branches.txt` row below the insertion point.
- A positional in a gate's `fail` message CANNOT be armed — `check-arms.py` reads a bare `$1` as
  literal text inside the signature. Bind it to a name and put it at the END, after the sentence.
- Hygiene checks 13-19 are OFF unless a pin is armed; a fixture tree written WITHOUT pins arms nothing
  in that range. Set the pin in the scratch tree, or the arm passes by finding nothing.
- Under MSYS one directory has two spellings and mount points are NOT symlinks — never compare path
  strings across flavors. Decide repo membership via git identity, both sides normalized through the
  same `cd … && pwd` chain.
