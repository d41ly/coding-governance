# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.3 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-08-20T16:41:45+03:00 @ 43a6c13e853ba6149600a2053cd439962413dc9d
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates/run-gates.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; coding-governance-agents.template.md; skills/session-kickoff/SKILL.md; .unattended.conf; memory/guides/BUILD-METHOD.md
verify-paths: AGENTS.md; coding-governance-agents.template.md; README.md; memory/guides/BUILD-METHOD.md
last-body-change: 4a5778e5ae8350c8d3f3f1c65bd2bfc539854b46
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
- **Governing docs:** `AGENTS.md` (the charter — authoritative) · `coding-governance-agents.template.md`
  (the playbook this repo follows + ships) · `memory/DECISIONS.md` + `memory/backlog/<FAMILY>.md`.
  Two BINDING guides: `memory/guides/REVIEW-PROTOCOL.md` (fan-out) and
  `memory/guides/UNATTENDED-PROTOCOL.md` (a run that merges and pushes with no owner turn).
- **An unattended run is bound by DIRECTIVES**, not just by the protocol: a kit-owned set, each one a
  POINTER into a `BUILD-METHOD.md` section rather than a copy of it, waivable only by the owner at
  preflight with a named reason. The list an agent reads is the table in the unattended Skill; the
  registry is a driver constant, and a leg joins the two in both directions. Neither the count nor
  the handles are written here — that is the drift the pointer design exists to avoid.

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/DECISIONS.md` §PLAY · `memory/backlog/PLAY.md` | `coding-governance-agents.template.md`, ONE file since v3.0, rendered into `AGENTS.md` by `tools/playbook/` · `check-playbook-parity.sh` (read its refusal before editing prose it owns) · `check-template-size.sh` · `check-placeholders.sh` |
| kickoff (`KICK-`) | `memory/DECISIONS.md` §KICK · `memory/backlog/KICK.md` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/DECISIONS.md` §TOOL · `memory/backlog/TOOL.md` | `tools/` — read the dir, not this cell; kits self-describe in their own `README.md` |
| deployer (`DEPL-`) | `memory/DECISIONS.md` §DEPL · `memory/backlog/DEPL.md` | `WIRE-INTO-PROJECT.md` · `memory/builds/aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates/run-gates.sh    # runs all legs CONCURRENTLY, at the width tools/run-gates/gate-profiles.txt declares for the detected hardware; the leg list is single-sourced from tools/gate-legs.json — read THAT for it, not this line
GATE_JOBS=1 bash tools/run-gates/run-gates.sh   # the serial bar, same code path — the rollback for a suspected concurrency problem
GATE_FULL=1 bash tools/run-gates/run-gates.sh   # ignore every leg guard — what .githooks/pre-push runs, and what a DoD needs
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

- A gate FIXTURE this node cannot host: `git add` never stages a `*.bak` path (the global
  `core.excludesfile` carries it), and a name differing only in CASE is the same file. Both
  produce an arm that passes because its fixture was never there. Check what `git ls-files`
  actually holds before trusting a near-miss control.
- The read-path ceiling is spent by things nobody thinks of as reading: the generated
  `memory/LIVE.md` row a NEW BUILD FOLDER adds, and every `memory/DECISIONS.md` append. A
  build can red check 16 on its own bookkeeping before it edits a guide. Read the margin
  from `python tools/memory-tree/corpus_ids.py --report`, never from the ceiling alone.
- The template is under a 48 KiB gate, and the gate also WARNS when the file grows past its
  recorded high-water. Prefer dropping a conditional block, or trimming non-instructional prose, to
  spending headroom; raising the ceiling is an owner decision, not an edit. Read the current
  margin FROM `bash tools/check-template-size.sh`, never from prose — it moved twice in one day.
- Merging in a LINKED WORKTREE leaves conflict markers in the row-merged files: the driver's
  grammar load raises against a conf path and it fails CLOSED rather than take-ours. Recover by
  running `tools/memory-tree/merge-rows.py <base> <ours> <theirs>` directly on the three stages
  (`git show :1: :2: :3:`) — it merges them clean. `TOOL-aCandidStub-4`.
- Two branches can BOTH rotate `memory/backlog/<FAMILY>.md` to archive independently. The row
  driver then reports the other side's rotation as DELETES and conflicts. Before resolving,
  verify every id absent from the union is present in some `memory/archive/<FAMILY>.*.md` —
  0 unaccounted is the check — then union the rows and carry BOTH rotation notes.
- A `git checkout -- <conf>` run for an unrelated reason silently reverts an UNCOMMITTED floor bump,
  and a floor goes SLACK rather than red when it does. Commit a floor in the pass that earns it.
  `TOOL-aPromptedMandate-4`.
- Several sessions share this node and the bar has no admission control: four concurrent full
  bars turned the run-gates canary's timing arms RED at every width and stretched the driver
  selftest from 11 to 99 minutes. `both expired ... unproven either way` means contention —
  re-run on a quiet box before believing a latency claim. `TOOL-aPacedTurnstile-2`.
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with
  `git diff --cached --check`.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook is wired on `Workflow|Agent` (kit 1.4) and enforces four rules;
  the bound is a FILE CONSTANT and `AGENT_CAP` is refused, not honoured. Binding rules:
  `memory/guides/REVIEW-PROTOCOL.md`. Ready-made harness: `tools/workflows/tier2-review.js`. The
  concurrency half of this trap is `memory/gotchas/concurrency-is-not-a-budget.md`.
- A conf value interpolated into a REGEX must be VALIDATED, not escaped: `MEMORY_ROOT="docs/mem"`
  matched nothing and `docs|memory` swallowed a subtree, both silently. A vacuity arm firing only at
  zero cannot see a PARTIAL exclusion. Detail: `memory/builds/aDeclaredBound/reviews/`.
- Two constants that COINCIDE are not pinned equal. Ownership belongs to the one that CHANGES THE
  OUTCOME — verify by moving it, not by reading it.
- An exclusion is only as wide as the control it defers to, and a guard that a binding pair EXISTS
  is not a guard that it COVERS. Prefer deleting an exclusion to widening its justification.
- Editing `.claude/settings.json` takes effect MID-SESSION — hooks are re-read, not snapshotted at
  start. Measured 2026-08-10 with a throwaway `PreToolUse` hook that fired on the call which checked
  for it. Do not skip the liveness half of such a probe.
- A CRLF fixture cannot test a CR guard on a Cygwin node: the runtime strips CR before `awk` sees a
  byte, through a filename, through `getline` AND through a pipe. Assert at source level.
- `node --check <file>` is NOT a syntax gate on node v24 — module auto-detection retries the parse and
  swallows the failure. Parse by constructing an `AsyncFunction`: `tools/workflows/check-workflow-syntax.js`.
- A kit that resolves the repo root by counting directories UP breaks SILENTLY at any other install
  prefix — codebase-map answered from an empty corpus. Walk up for the conf, bounded by `.git`.
- A build README's top level is a SLOT SEQUENCE gated by its own leg,
  `gen_build_index.py --check-format`: authored content after the first generated marker reds it.
  Detail in `memory/map/features/build-readme-surface.md`.
- `--write` CREATES a missing generated region pair; `--check` never demands one. Rely on that when
  adding a region: it is what lets a new one ship without re-rendering the corpus in the same commit.
- `memory/builds/*/STATUS.md` no longer exists. The slot was retired at kit 2.17 — one file existed
  corpus-wide and contradicted its own build README. Check 8's population is the backlog shards alone.
- A build README's `ids:` key is DERIVED and rewritten by `--write` from the id corpus. It is not a
  reservation range and a planned unit cannot be added to it by hand; the next render removes it.
- A build README's `roster:` is `+`-JOINED (`PLAY+TOOL`); a space-joined value reds check 9 with a
  message that reads like a families misconfiguration.
- Hygiene check 12's skeleton scan matches a literal date-shape or id-shape ANYWHERE in a spec body,
  so QUOTING a stale artifact that contains one reds the spec. Paraphrase the shape instead.
- A new tool at the REPO ROOT rather than under `tools/` silently leaves the enforced surface: the
  source-level gates, the codebase-map inventories and drift-audit's globs all scope to `tools/**`.
- Adding ONE gate leg trips a SET of meta-gates that GROWS as new ones land — run the full bar, not
  this list. MEASURED 2026-08-18: map freshness, the kickoff ratchet, govkit selfcheck + selftest (a
  leg needs a `[[gate_leg]]` in its kit's `kit.toml`, else an `[[exempt_leg]]` row). The coverage
  assert and handkept signal did NOT fire; this line claimed both and neither govkit gate.
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
- `merge-rows.py` takes `%O %A %B` — BASE, OURS, THEIRS — and writes into the OURS path. A wrong
  order does not error: it emits a plausible file with the other side's rows silently dropped.
  Diff the merged id-set against BOTH inputs, never eyeball the output.
- A HARNESS-CREATED WORKTREE starts with a RED bar and a refusing `--preflight`: it carries CRLF on
  the `eol=lf`-pinned `.claude/` renders, which reds the `memory-recall skill wiring` leg and makes
  `check-wiring.sh --check` exit 1. NOT `git worktree add`, which measures clean. Run
  `bash tools/check-wiring.sh --fix` first. Prune when the memory-recall adopter CR-normalises.
- Under MSYS one directory has two spellings and mount points are NOT symlinks — never compare path
  strings across flavors. Decide repo membership via git identity, both sides normalized through the
  same `cd … && pwd` chain.
- The full bar can TIME OUT on a node whose `TMPDIR` holds tens of thousands of stale scratch dirs:
  every hermetic leg does its own `mktemp -d` into it. Measured on node `a`: 30733 entries, 58 legs,
  >10 min and still running; the same bar finished on a fresh `TMPDIR`. Point `TMPDIR` at an empty
  dir before blaming the diff, and do not delete the shared one.
- Every NEW file under `builds/*/{build,prompts,reviews}/` needs a `**Serves:**` line or check 21 reds;
  grammar in `memory/HYGIENE.md`. The filename must PROJECT it — family, slug, ordinal of the lowest id
  served. A ROUND COUNTER there cites an id nothing defines: check 14 reds and a phantom id reaches the
  front matter. Use `…-<slug>-1-round2.md`.
- A new CHECK inside the hygiene gate is far cheaper than a new gate LEG: the codebase-map coverage
  assert and drift-audit's leg signal both key on `tools/gate-legs.json`, so neither moves. It still
  costs `ARMS_FLOORS`, an arm per `fail` call site (not per check number), and the leg's own name if
  that name states a count.
- The hygiene engine PRE-SETS its conf keys and sources `.memory-tree.conf` OVER them, so a blank line
  overrides a default WITH BLANK — which every measured pin uses to mean "skip". A key that must not be
  skippable needs re-normalising AFTER the source; `_resolve_cap` is the seam.
- A spent budget blocks RECORDING work, not doing it, and this repo hit it twice in one session: the
  TOOL backlog with nothing terminal to rotate, and `READ_PATH_CEILING` breached by ONE build's row in
  the generated `memory/LIVE.md`. Measure headroom in DAYS — 93.5% read survivable at 0.65 days left.
