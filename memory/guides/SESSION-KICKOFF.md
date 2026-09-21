# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.4 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-09-21T07:21:11+03:00 @ ab0f1bcd89b2e0380f8a3389171cfcd3be1d5ddb
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates/run-gates.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; coding-governance-agents.template.md; skills/session-kickoff/SKILL.md; .unattended.conf; memory/guides/BUILD-METHOD.md
verify-paths: AGENTS.md; coding-governance-agents.template.md; README.md; memory/guides/BUILD-METHOD.md
last-body-change: ab0f1bcd89b2e0380f8a3389171cfcd3be1d5ddb
check-script: skills/session-kickoff/manifest-check.sh
registry: AGENTS.md
-->

The project layer read by the generic `/session-kickoff` skill. Precedence on conflicts:
**`AGENTS.md`/`CLAUDE.md` > this file > the skill**. This repo dogfoods its own kits, so the manifest
here is short — `AGENTS.md` (the charter) holds the substance.

## The ratchet — how this file stays true

- Every kickoff audits this file (`manifest-check.sh`, at `check-script:`) and repairs drift on the spot.
- Every unit that changed what this file front-loads (a gate command, entrypoint, governing doc, a
  trap hit, a doc/memory claim found stale, or a fact re-derived it should have front-loaded) re-stamps
  `last-audit` with a delta line in the commit message; no delta → no touch.
- Stamp rule: sha = `HEAD` on any branch; datetime always advances.
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
  rule, the pass loop, regrounding, the closing review, the README re-read and the wrap-up
  derivation. It is rendered by the memory-tree kit and is in `watch:`, so editing it forces this
  manifest to be re-audited.
- **A build MAY restructure itself, and MUST parallelise what it can prove disjoint.** Both are
  BUILD-METHOD's, both changed under `TOOL-dUnstalledConvoy`, and both invert what a session would
  otherwise assume: M2/M3 give a run delegated authority to retire, supersede or add units inside the
  build's stated goal rather than stalling on a spec that turned out wrong, and M6's default is now
  parallel-where-proven with sequence as the fallback. Conditions and bounds are M3's and M6's. What
  is NOT in force is the VERIFICATION: `--dispatch` records a pass's declared write set and the
  comparison only REPORTS (`TOOL-dUnstalledConvoy-23`). Declare them anyway; green is not a proof.

- **Every session start writes an ORIENTATION CARD** at `<git-common-dir>/orientation/<session_id>.md`
  (`manifest-check.sh --card --write`, wired as a SessionStart hook; `--card --replay` re-injects it
  verbatim after a compaction). Step 1 consumes it; Step 5 appends the READY card through
  `--card --append`. A main-loop `git commit` in a session whose startup card still reads
  `READY — none yet` is REFUSED by `tools/hooks/scratch-guard.js` with the remedy in stderr; an
  absent or replay-written card allows. `KICK-aReplayedCard-1`, `TOOL-aReplayedCard-1`.
- **Repo layout:** primary checkout at `C:/projects/coding-governance` (holds `main`), plus per-unit
  worktrees under `.claude/worktrees/<branch-slug>/`. `git worktree list` is the inventory. A unit
  branch's commits ride its own worktree, never the primary tree (the pre-commit branch guard refuses).
- **Remote · default branch:** `origin` · `main`.
- **Branch conventions:** small units on `main` for a solo tooling repo; `git push` needs an explicit
  ask, or a committed build folder the run did not create. What "did not create" admits depends on the
  ANCHOR the project declares, and this file does not paraphrase it — an earlier paraphrase here said
  "committed before the run's branch existed", which describes one anchor and is false of the other.
  `memory/guides/UNATTENDED-PROTOCOL.md` section 1 is the condition.
- **Governing docs:** `AGENTS.md` (the charter — authoritative) · `coding-governance-agents.template.md`
  (the playbook this repo follows + ships) · `memory/DECISIONS.md` + `memory/backlog/<FAMILY>.md`.
  Two BINDING guides: `memory/guides/REVIEW-PROTOCOL.md` (fan-out) and
  `memory/guides/UNATTENDED-PROTOCOL.md` + `UNATTENDED-VERBS.md` (a run that merges and pushes
  with no owner turn).
- **An unattended run is bound by DIRECTIVES**, not just by the protocol: a kit-owned set, each one a
  POINTER into a `BUILD-METHOD.md` section rather than a copy of it, waivable only by the owner at
  preflight with a named reason. The list an agent reads is the table in the unattended Skill; the
  registry is a driver constant, and a leg joins the two in both directions. Neither the count nor
  the handles are written here — that is the drift the pointer design exists to avoid. Two invert
  the reflex: a discovery is ADOPTED not parked; the idle-wake precedes orienting. §11 and §5.

- **The idle-wake is not the keepalive.** The cron job wakes an idle session and nothing else; what
  resumes a stalled run lives OUTSIDE its session — the stop-guard at every turn end, the
  stall-recorder at every error end, the resume tick from the OS scheduler — reading the LEASE
  (`session:`, `pid:`, `host:`, `pid-image:`, `lease-utc:`) the driver records and the verdict
  `--liveness` derives. `RESUME_STALE_BOUND` is the bound they act on. Protocol §5; `aWokenSentinel`.

- **`GATE_BOUND` bounds `GATE_CMD` and `WIRING_CHECK`; `GATE_REAP_BOUND` the
  teardown reap.** A breach is KILLED, and `gates-green` then says the bar never RETURNED
  — not a leg FAILING. None of them bounds an AGENT-launched
  process; see `tools/process-monitor/`. `TOOL-aBoundedCeiling-6`.

- **An unattended run declares a MODE, and which one decides what binds it**: the authorization
  discipline, WHICH ANCHOR may authorize it, which scoped directives apply, and whether the
  piece-scoped Definition-of-Done items evaluate at all or announce a skip. The set is a driver
  constant and so is the subset admissible on the second anchor, the unattended Skill's routing
  table names a start path per member, and a leg joins the two in both directions. Neither the
  members nor their count are written here, for the reason the directives bullet above gives.

- **A CLOSED Tier-2 unit owes an acceptance ledger** — one line per numbered criterion, in a record
  whose `**Serves:**` kind is `journal`, in one of two forms and no third. The grammar is
  `memory/HYGIENE.md` under "Acceptance ledger" and the gate reads shape and coverage only. The
  cutoff is a `.memory-tree.conf` date, so units that closed before the grammar existed are outside
  it; anything this session closes is inside it.

- **A CLOSED unit whose spec grades THIN blocks `build-complete`** — an empty Scope, Acceptance
  criteria or Gates section, keyed on the heading TITLE and NOT the ordinal, which on a Tier-1 spec
  read Gates as acceptance (`TOOL-dBriefedPass-1`). Date-grandfathered on the spec's FILENAME against
  `.unattended.conf`'s `SPEC_THIN_CUTOFF`; BLANK turns the term OFF. `TOOL-aGradedMandate-4`.

- **Before starting work inside a kit, check whether another node is already rewriting it.**
  `git log origin/main --oneline -20 -- tools/<kit>/` answers it in one second. Hit twice:
  `tools/unattended/` on 2026-08-21, and `check-memory-hygiene.sh` on 2026-09-13 by two sessions
  sharing node tag `c`, for 13 conflicts at the landing. Neither time did anyone run it. §3's rule
  is own STREAMS not files, and a kit is the unit that rule is about.

- **The read-path byte budget is RETIRED** (`TOOL-dSpentCeiling-1`). Check 6's per-class caps are
  the bound; check 16 keeps rules 3 and 4, structural and behind no pin. Do not re-add a sum.

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/DECISIONS.md` §PLAY · `memory/backlog/PLAY.md` | `coding-governance-agents.template.md`, ONE file since v3.0, rendered into `AGENTS.md` by `tools/playbook/` · `check-playbook-parity.sh` (read its refusal before editing prose it owns) · `check-template-size.sh` · `check-placeholders.sh` |
| kickoff (`KICK-`) | `memory/DECISIONS.md` §KICK · `memory/backlog/KICK.md` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/DECISIONS.md` §TOOL · `memory/backlog/TOOL.md` | the `tools/<kit>/` dirs THIS unit touches, not `tools/` — that is what the probes above take; kits self-describe in their own `README.md` |
| deployer (`DEPL-`) | `memory/DECISIONS.md` §DEPL · `memory/backlog/DEPL.md` | `WIRE-INTO-PROJECT.md` · `memory/builds/aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates/run-gates.sh    # runs all legs CONCURRENTLY, at the width tools/run-gates/gate-profiles.txt declares for the detected hardware; the leg list is single-sourced from tools/gate-legs.json — read THAT for it, not this line
# Legs report in CHUNKS, each closing with a verdict line, so a red is readable before the run ends. A chunk whose every leg skipped reports skipped, never green.
GATE_JOBS=1 bash tools/run-gates/run-gates.sh   # the serial bar, same code path — the rollback for a suspected concurrency problem
GATE_FULL=1 bash tools/run-gates/run-gates.sh   # ignore every leg GUARD. .githooks/pre-push no longer sets this unconditionally: it decides, and prints which it chose and why
GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh   # also run EVERY self-test — `subject = kit` OR `chunk = selftests`, both held by default (owner ruling 2026-08-26). GATE_FULL does NOT unlock them. On demand only; the §B correction dated 2026-08-23 says what that costs
# Every leg declares a `ceiling` in tools/gate-legs.json and the runner KILLS one that outlives it, RED naming the leg and the number. TOOL-aBoundedCeiling-1
# The whole RUN has a wall, per profile row; GATE_WALL overrides. A breach kills the legs. TOOL-aQuenchedHarness-1
bash tools/run-gates/run-selftests.sh  # the HELD population on demand, budget-timed. TOOL-aQuenchedHarness-4
python tools/memory-tree/gotchas.py --for-diff <base>..<head>   # the recurring-bug-class checklist for THIS diff — run it before a review
python tools/drift-audit/drift_report.py   # ~seconds, no agents: do this repo's own RECORDS still match reality? Run it before theorizing about drift
```

The repo HAS a codebase map (`memory/map/`), so the kickoff skill's map steps are live. No
environment is needed — the engine resolves this repo's `tools/` install prefix itself:

```bash
python tools/codebase-map/map_diff.py <old>..<new>          # Step 1: what a fast-forward brought in
python tools/codebase-map/reuse_lookup.py "<behaviour>"     # Step 4 / §10: the seam to wire through
python tools/memory-recall/query.py "<question>" --terms "<8-14 words>"  # Step 4: the records that bind it — REFUSES without --terms
python tools/memory-tree/gotchas.py --for-paths <the tooling row's entrypoints>  # Step 4: the bug classes for this area
```

### Tier rule

Tier 2 (spec + adversarial review before building) for: a change to the governance template's rules,
the manifest-check gate semantics, or a new/changed kit's contract; a cross-kit change. Otherwise
Tier 1 (gates + one focused self-review).

### ID + work-state protocol

`FAMILY-<slug>-<seq>`, families `PLAY`/`KICK`/`TOOL`/`DEPL` (per `.memory-tree.conf`). Slug = YOUR node tag
(identify the node by machine/user against the AGENTS.md registry, never by path — all four rows pin the
same primary tree, so the path cannot tell them apart) + CamelCase adjective-noun, minted once per session; collision-grep `memory/`. Work state is
READ from the GENERATED `memory/LIVE.md` + `memory/ledger/<month>.md` (`gen_build_index.py --write`
re-renders them from build front matter); there is no authored ledger to update. Build folders are
`memory/builds/<slug>/`; the discipline is the spec header's `streams` value (`STREAMS_CUTOFF` in
`.memory-tree.conf` arms it).

### Current posture — dated corrections

*Correction OVERRIDES a stale doc/memory claim until fixed; entry: `<date> · <stale where> · <the
correction> · prune when <condition>`. Starts empty; prune per-entry, never delete the section.*

- 2026-08-23 · the owner's standing instruction on the kit self-test suites · `--checks` yes,
  `--selftests` only when they ask · prune when a bar runs them automatically.


### Environment traps worth front-loading

*One line each; link out for detail — check 11 enforces it at 400 bytes per bullet. A recurring BUG
CLASS does not belong here at all: it belongs in `memory/gotchas/`, where `gotchas.py --for-paths`
puts it on the checklist for the areas a unit actually touches.*

Evicted to the catalogue, and reachable from it: `gate-green-by-accident-on-generated-bytes.md`
(an eol pin without a normalising comparison, and the worktree checkout that lands CRLF on a pinned
path) · `absence-assertion-over-whole-file-text.md` (a new gate predicate run for the first time
against the real tree) · `subprocess-resolves-a-different-shell.md` · `heredoc-escape-reaches-the-regex.md`
· `assertion-between-two-derived-values.md` (a core-subset-of-effective assertion the checker itself
composes) · `inputs-inside-the-subjects-reach.md` (what SUPPLIES each of a check's inputs) ·
`arm-literal-strands-on-message-edit.md` (editing a `fail` message strands its arm; the signature
runs to the first interpolation, so lengthening a message always strands it and shortening never
does — hit three times in one file in one session; also the whole-signature and positional facets) · `process-creation-is-the-suite-cost.md` ·
`trace-profile-measures-itself.md` · `fallback-fabricates-the-passing-value.md` ·
`two-readers-of-one-config-one-re-derived.md` · `line-keyed-registry-reds-on-a-file-that-grew.md` (a waiver keyed `<path>:<line>`, and the sibling arm that is a BAN rather than a ratchet) · `naming-leg-grades-what-python-named.md` (nested helpers and dunders count, and arming follows `symbols.json`, so it only reds at the lander)
· `row-driver-emits-a-plausible-file-with-rows-missing.md` · `worktree-crlf-outside-the-gated-population.md` · `settings-edit-takes-effect-mid-session.md` · `node-check-is-not-a-syntax-gate.md`
· `check-format-grades-two-populations.md` · `waiver-row-that-hides-nothing-reds.md` · `a-new-leg-trips-a-growing-set-of-meta-gates.md` · `conf-value-interpolated-into-a-regex.md`
· `pin-gated-checks-arm-nothing-without-a-pin.md` · `record-without-serves-or-with-a-round-counter.md` · `sourced-conf-blank-overrides-the-default.md`
· `shipped-checker-edit-is-an-adopter-contract-change.md` · `concurrency-is-not-a-budget.md` (also the file-constant bound) · `allowlist-narrower-than-the-root-it-guards.md` (also what a
`scratch-guard` denial means). The 2026-09-14 eviction is `TOOL-aReplayedCard-4`; its acceptance ledger maps every bullet to the record it landed in.

- A gate FIXTURE a node may not host: an IGNORED path is never staged, and a name differing only in
  CASE is the same file. Both give an arm that passes because its fixture was never there. `*.bak`
  is ignored on node `d`, on node `a` at NO scope (2026-09-04): run `git check-ignore -v` on YOURS.
- The template is under a 48 KiB gate, and the gate also WARNS when the file grows past its
  recorded high-water. Prefer dropping a conditional block, or trimming non-instructional prose, to
  spending headroom; raising the ceiling is an owner decision, not an edit. Read the current
  margin FROM `bash tools/check-template-size.sh`, never from prose — it moved twice in one day.
- `git -C <dir> rev-parse --show-toplevel` returns `<dir>` ITSELF when an absolute `GIT_DIR` is
  inherited — what git exports to a merge driver in a LINKED WORKTREE. That made the row driver
  conflict every merge there until `repo_root()` walked up for the conf (`TOOL-aCollapsedScan-7`).
  Worktree merges are CLEAN now, re-verified 2026-09-04.
- A `git checkout -- <conf>` run for an unrelated reason silently reverts an UNCOMMITTED floor bump,
  and a floor goes SLACK rather than red when it does. Commit a floor in the pass that earns it.
  `TOOL-aPromptedMandate-4`.
- The turnstile serializes bars WITHIN one repository only; sessions on this node still contend
  across repos. `both expired ... unproven either way` means contention, and now SKIPS that arm
  loudly rather than redding — re-run quiet before believing a latency claim.
  `TOOL-aPacedTurnstile-2`.
- The memory-hygiene gate grades TRACKED files only, so running it on a new build folder BEFORE
  `git add` returns a clean exit that proves nothing. Stage first, then run it. Cost two cycles
  here: checks 5, 9 and 21 all fired only once the folder was staged.
- `gate-guard` is the third `Bash|PowerShell` hook, from the unattended kit: while this branch's
  run-state record is before `VERIFYING` it DENIES a `GATE_FULL=`/`GATE_SELFTESTS=` bar and any
  `*.test.sh` or self-test runner, naming the record. Not a glitch: feed the hook the payload, or
  wait for the main loop's `VERIFYING`.
- `scratch-guard` (aProbedUnit, 2026-09-14) also DENIES a write rooted at an EMPTY `$TMPDIR`/`$TMP`/`$TEMP`
  — and `TMPDIR` IS empty on this node, so `$TMPDIR/x` is `/x` — any `/tmp` target, and root litter.
  Rules: `tools/hooks/README.md`. Write to the session scratchpad; a git clone goes under
  `%TEMP%/<short>` (MAX_PATH).
- A kit path a tool WRITES, RENDERS or PRINTS is DERIVED from that tool's own location, never spelled.
  A hardcoded prefix in a RENDERED artifact is the worst case: it lands a dead path in the adopter's
  committed tree and the byte-compare guarding that file agrees with it.
- A gate that returns a VALUE on stdout cannot also report on stdout — `fail` echoes, so `x=$(check …)`
  captures the diagnostics and the operator sees only the downstream symptom. Use a separate channel.
- A NEW record under `memory/gotchas/` needs `gotchas.py --write` AND a dossier claim, and the
  coverage inventory reads TRACKED files — so `git add` first, then measure, or the gap surfaces on
  the full bar instead.
- Template parity and PLACEHOLDER COMPLETENESS are two different questions. A render whose conf
  declares nothing for a key is byte-identical to a fresh render and still tells the agent to invoke a
  placeholder's name as a tool. Grep the render for a surviving brace-shape as its own arm.
- Under MSYS one directory has two spellings and mount points are NOT symlinks — never compare path
  strings across flavors. Decide repo membership via git identity, both sides normalized through the
  same `cd … && pwd` chain.
- The full bar can TIME OUT on a node whose `TMPDIR` holds tens of thousands of stale scratch dirs:
  every hermetic leg does its own `mktemp -d` into it. Measured on node `a`: 30733 entries, 58 legs,
  >10 min and still running; the same bar finished on a fresh `TMPDIR`. Point `TMPDIR` at an empty
  dir before blaming the diff, and do not delete the shared one.
- A spent budget blocks RECORDING work, not doing it. The read-path ceiling that did that is
  RETIRED (`TOOL-dSpentCeiling-1`); the surviving lesson is general — measure with the checker
  before and after, never estimate, and record every movement beside the number.
