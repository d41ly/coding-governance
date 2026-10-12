# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.4 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-10-12T19:45:09+03:00 @ 59ae2687d9193ea31786e1e4041361666e256969
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates/run-gates.sh; tools/run-gates/run-selftests.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; coding-governance-agents.template.md; skills/session-kickoff/SKILL.md; .unattended.conf; memory/guides/BUILD-METHOD.md
verify-paths: AGENTS.md; coding-governance-agents.template.md; README.md; memory/guides/BUILD-METHOD.md
last-body-change: 78110101c6c3e494cd10648a8bfb4cedea9470e3
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

One line per bullet (KICK-aDistilledCharter-1): a pointer or a trap, never a procedure. The detail
lives where each bullet points.

- A build of more than one pass runs on `memory/guides/BUILD-METHOD.md`; it is in `watch:`, so editing it re-audits this manifest.
- A build may amend its own roster (BUILD-METHOD M2, M3) and must run delegated disjoint passes in parallel (M6); both invert a session's default.
- Every session start writes an orientation card; a commit is refused until its READY line is appended, and only from a tree the card names (`tools/hooks/scratch-guard.js`).
- A card's `## route` lands only when its build, unit specs and brief all resolve; a write under `ROUTED_PATHS` needs a route naming a buildable unit, and a pushed commit there names a specced one (`TOOL-aRoutedQuill-2`, `-3`).
- The card's READY anchor accepts both the bare and the `- ` list-item spelling (`TOOL-cMendedVintage-16`).
- Layout: `main` lives in `C:/projects/coding-governance`; every unit's branch rides its own worktree under `.claude/worktrees/<branch-slug>/`, and `git worktree list` is the inventory.
- Remote `origin`, default branch `main`; a push needs an explicit ask or the authorization `memory/guides/UNATTENDED-PROTOCOL.md` section 1 defines.
- Governing docs: `AGENTS.md`, the template it renders from, and `memory/DECISIONS.md`; binding guides are `memory/guides/REVIEW-PROTOCOL.md` and the unattended protocol and verbs.
- An unattended run is bound by directives the unattended Skill lists, waivable only by the owner at preflight; a discovery is adopted, not parked.
- An unattended run declares a mode, which decides its authorization, its anchor and the directives that bind; the Skill's routing table is the list.
- The idle-wake only wakes an idle session; resuming a stalled run is the stop-guard's, the stall-recorder's and the resume tick's, from the lease (protocol §5).
- `GATE_BOUND` bounds every declared command and kills it on breach; nothing bounds an agent-launched process except `tools/process-monitor/`.
- An adopter's bar holds a leg by `subject = "kit"` alone: govkit never emits `chunk`, so a shipped self-test declares it in its descriptor (`aBenchedProbe`).
- A CLOSED Tier-2 unit owes an acceptance ledger in a `journal` record; the grammar is `memory/HYGIENE.md` "Acceptance ledger".
- A live spec retiring a named thing owes a `**Readers:**` clause (hygiene check 25), and a CLOSED unit whose spec grades THIN blocks `build-complete`.
- A live spec's leg line names every leg its files-touched trips: `python tools/check-spec-tokens.py --list` prints them before the spec is dated.
- A spec audit is owed only where the owner declares `spec-audit:` or `SPEC_AUDIT_DEFAULT`; a run never declares either, and kickoff asks.
- Before working inside a kit, `git log origin/main --oneline -20 -- tools/<kit>/` shows whether another node is rewriting it.
- A landing that edits a grader owns every red that grader prints at the tip (KF3): reproduce at R in a detached worktree, then fix or ABSORB it (`memory/guides/UNATTENDED-STOPS.md` §13; `dHomedResolver`).
- `tools/unattended/check-unattended.sh` carries raw CR bytes in its awk regexes: edit it in binary mode (`memory/gotchas/text-mode-read-eats-a-bare-cr.md`).
- The read-path byte budget is retired (`TOOL-dSpentCeiling-1`): check 6's per-class caps are the bound, and a sum is not re-added.
- A live `RUN.md` is outside check 6 by class (`TOOL-cMendedVintage-13`); a retired one is capped.

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/DECISIONS.md` §PLAY · view `memory/backlog/PLAY.md` | `coding-governance-agents.template.md`, ONE file since v3.0, rendered into `AGENTS.md` by `tools/playbook/` · `check-playbook-parity.sh` (read its refusal before editing prose it owns) · `check-template-size.sh` · `check-placeholders.sh` |
| kickoff (`KICK-`) | `memory/DECISIONS.md` §KICK · view `memory/backlog/KICK.md` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/DECISIONS.md` §TOOL · view `memory/backlog/TOOL.md` | the `tools/<kit>/` dirs THIS unit touches, not `tools/` — that is what the probes above take; kits self-describe in their own `README.md` |
| deployer (`DEPL-`) | `memory/DECISIONS.md` §DEPL · view `memory/backlog/DEPL.md` | `WIRE-INTO-PROJECT.md` · `memory/builds/aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates/run-gates.sh    # runs all legs CONCURRENTLY, at the width gate-profiles.txt declares for this hardware; the leg list is single-sourced from tools/gate-legs.json — read THAT for it, not this line
# Legs report in CHUNKS, each closing with a verdict line, so a red is readable before the run ends. A chunk whose every leg skipped reports skipped, never green.
GATE_JOBS=1 bash tools/run-gates/run-gates.sh   # the serial bar, same code path — the rollback for a suspected concurrency problem
GATE_FULL=1 bash tools/run-gates/run-gates.sh   # ignore every leg GUARD and the docs mode (GATE_DOCS_BASE). .githooks/pre-push decides, and prints which it chose and why
GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh   # also run EVERY self-test — `subject = kit` OR `chunk = selftests`, both held by default (owner ruling 2026-08-26). GATE_FULL does NOT unlock them. On demand only; the §B correction dated 2026-08-23 says what that costs
# Every leg declares a `ceiling` in tools/gate-legs.json; one outliving it gets ONE serial retry (a pass is green); all-HOST exits 4. TOOL-aBoundedCeiling-1
# Per profile row: a whole-RUN wall (GATE_WALL; a breach kills the legs, TOOL-aQuenchedHarness-1), and mempause holding dispatch while used memory is above it (TOOL-aGraftedHelix-7)
GATE_ATTRIBUTE=<rev> bash tools/run-gates/run-gates.sh   # re-run each RED leg at <rev> and print whose red it is: OWN, INHERITED, MIXED, CONTENDED or DEAD PROBE. Report-only, the exit never moves; .githooks/pre-push exports the remote sha. TOOL-dDerivedDocket-23
bash tools/run-gates/run-selftests.sh --serial  # the HELD population on demand, budget-timed; --pooled withholds cost verdicts and REFUSES an uncalibrated row until --pooled --calibrate; bare REFUSES; GOV_NODE must be a registry tag; a pooled red keeps each row's output under <git-dir>/gate-logs/selftests/. TOOL-aBatchedArm-4, -5
bash tools/unattended/run-unattended-gates.sh --pooled   # DoD for tools/unattended/ work: pooled PARITY against tools/run-gates/selftest-pooled-evidence.txt, or `--selftests --serial --attribute <BASE>` reading `verdict clean`. TOOL-dDerivedDocket-1
python tools/memory-tree/gotchas.py --for-diff <base>..<head>   # bug-class checklist + by-design block for THIS diff; run before a review
python tools/drift-audit/drift_report.py   # ~seconds, no agents: do this repo's own RECORDS still match reality?
python tools/govkit/govkit.py epoch --base <base>   # a kit whose shipped bytes moved since <base> and whose version did not: run after a commit that touches a kit. TOOL-aRepatriatedFork-15
python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills   # text IO that names no encoding; the registry may fall and never rise. TOOL-aRepatriatedFork-3
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

Tier 2 (a spec before building; the spec audit only where the build or its project declares it, M4) for: a change to the governance template's
rules, the manifest-check gate semantics, or a new/changed kit's contract; a cross-kit change. Otherwise
Tier 1 (a micro-spec, graded by heading title in check 12 from `SPEC_TIER1_CUTOFF` and written by
`gen_build_index.py --new-spec <ID> --tier 1`, then gates + one focused self-review;
`TOOL-aRoutedQuill-1`).

### ID + work-state protocol

`FAMILY-<slug>-<seq>`, families `PLAY`/`KICK`/`TOOL`/`DEPL` (per `.memory-tree.conf`). Slug = YOUR node tag
(identify the node by machine/user against the AGENTS.md registry, never by path: all four rows pin
one primary tree) + CamelCase adjective-noun, minted once per session; collision-grep `memory/`. Work state is
READ from the GENERATED `memory/LIVE.md` + `memory/ledger/<month>.md` (`gen_build_index.py --write`
re-renders them from build front matter); there is no authored ledger to update. Build folders are
`memory/builds/<slug>/`; the discipline is the spec header's `streams` value (`STREAMS_CUTOFF` in
`.memory-tree.conf` arms it). A unit id is DEFINED by its spec's H1 under `builds/<slug>/spec/`: the
index generator and recall read that line through one predicate, `tree_lib.parse_spec_h1`, and
check 14 counts only present-tense citations against it. `TOOL-aRepatriatedFork-39`, `-40`.

### Current posture — dated corrections

*Correction OVERRIDES a stale doc/memory claim until fixed; entry: `<date> · <stale where> · <the
correction> · prune when <condition>`. Starts empty; prune per-entry, never delete the section.*

- 2026-08-23 · the owner's standing instruction on the kit self-test suites · `--checks` yes,
  `--selftests --serial` only when they ask. The cost is process creation, not logic:
  `memory/gotchas/process-creation-is-the-suite-cost.md` · prune when a bar runs them automatically.


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
does) · `process-creation-is-the-suite-cost.md` ·
`trace-profile-measures-itself.md` · `fallback-fabricates-the-passing-value.md` ·
`two-readers-of-one-config-one-re-derived.md` · `line-keyed-registry-reds-on-a-file-that-grew.md` (a waiver keyed `<path>:<line>`, and the sibling arm that is a BAN rather than a ratchet) · `naming-leg-grades-what-python-named.md` (nested helpers and dunders count, and arming follows `symbols.json`, so it only reds at the lander)
· `row-driver-emits-a-plausible-file-with-rows-missing.md` · `worktree-crlf-outside-the-gated-population.md` · `settings-edit-takes-effect-mid-session.md` · `node-check-is-not-a-syntax-gate.md`
· `check-format-grades-two-populations.md` · `waiver-row-that-hides-nothing-reds.md` · `a-new-leg-trips-a-growing-set-of-meta-gates.md` · `conf-value-interpolated-into-a-regex.md`
· `pin-gated-checks-arm-nothing-without-a-pin.md` · `record-without-serves-or-with-a-round-counter.md` · `sourced-conf-blank-overrides-the-default.md`
· `shipped-checker-edit-is-an-adopter-contract-change.md` · `concurrency-is-not-a-budget.md` (also the file-constant bound) · `allowlist-narrower-than-the-root-it-guards.md` (also what a
`scratch-guard` denial means) · `inherited-git-dir-pins-the-work-tree-to-the-cwd.md` (a `-C`
probe under a hook's `GIT_DIR`; a leg bans it now). The 2026-09-14 eviction is `TOOL-aReplayedCard-4`; its acceptance ledger maps every bullet to the record it landed in.

- A gate FIXTURE a node may not host: an IGNORED path is never staged, and a name differing only in
  CASE is the same file. Both give an arm that passes because its fixture was never there. `*.bak`
  is ignored on node `d`, on node `a` at NO scope (2026-09-04): run `git check-ignore -v` on YOURS.
- The template is under a 48 KiB gate that also WARNS past its recorded high-water. Raising the
  ceiling is an owner decision, not an edit. Read the margin FROM `bash tools/check-template-size.sh`.
- A `git checkout -- <conf>` run for an unrelated reason silently reverts an UNCOMMITTED floor bump,
  and a floor goes SLACK rather than red when it does. Commit a floor in the pass that earns it.
  `TOOL-aPromptedMandate-4`.
- The turnstile serializes bars WITHIN one repository only; sessions on this node still contend
  across repos. `both expired ... unproven either way` means contention, and now SKIPS that arm
  loudly rather than redding — re-run quiet before believing a latency claim.
  `TOOL-aPacedTurnstile-2`.
- The memory-hygiene gate grades TRACKED files only, so running it on a new build folder BEFORE
  `git add` returns a clean exit that proves nothing. Stage first, then run it: checks
  5, 9 and 21 all fired only once the folder was staged.
- `gate-guard` is a `Bash|PowerShell` hook from the unattended kit: while this branch's
  run-state record is before `VERIFYING` it DENIES a `GATE_FULL=`/`GATE_SELFTESTS=` bar and any
  `*.test.sh` or self-test runner, naming the record. Not a glitch: feed the hook the payload, or
  wait for the main loop's `VERIFYING`.
- `scratch-guard` (aProbedUnit, 2026-09-14) also DENIES a write rooted at an EMPTY `$TMPDIR`/`$TMP`/`$TEMP`
  — and `TMPDIR` IS empty on this node, so `$TMPDIR/x` is `/x` — any `/tmp` target, and root litter.
  Rules: `tools/hooks/README.md`. Write to the session scratchpad; a git clone goes under
  `%TEMP%/<short>` (MAX_PATH).
- Node `a`: a `mktemp -d` fixture is `/tmp/x`, an MSYS mount git spells `C:/…/Temp/x`; compare through git, never as strings. A leaked `%TEMP%/.memory-tree.conf` reds every walk-up (`fixture-inherits-ambient-machine-state.md`).
- A kit path a tool WRITES, RENDERS or PRINTS is DERIVED from that tool's own location, never spelled.
  A hardcoded prefix in a RENDERED artifact is the worst case: it lands a dead path in the adopter's
  committed tree and the byte-compare guarding that file agrees with it.
- An ADOPTER-declared path renders from deploy.toml via the playbook engine's `--answers` (1.11+,
  else a phrase), a protocol from its receipt row; never gov's layout. `TOOL-aRepatriatedFork-42`.
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
- The bar owns its scratch (TOOL-dDerivedDocket-25): every leg's `TMPDIR` is the runner's own
  `gate-work.*/tmp`, gone on exit; a SIGKILLed bar's is swept by the next once its pid is dead.
  `TMPDIR entries <n>` prints the ambient count, which now grows only from older bars or another
  repository's. The measured cost is in the run-gates kit README.
- A spent budget blocks RECORDING work, not doing it. The read-path ceiling that did that is
  RETIRED (`TOOL-dSpentCeiling-1`). Lesson: measure with the checker before and after, never
  estimate, and record every movement beside the number.
