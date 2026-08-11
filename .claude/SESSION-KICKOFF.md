# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.1 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-08-11T22:38:18+03:00 @ 1edceeb5951fd157d26a0161d7345d4c73280f79
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates.sh; tools/gate-legs.json; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; parallel-coding-governance.template.md; skills/session-kickoff/SKILL.md; .unattended.conf; memory/guides/BUILD-METHOD.md
verify-paths: AGENTS.md; parallel-coding-governance.template.md; README.md; memory/guides/BUILD-METHOD.md
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

*Accretes — append the trap that cost time, prune the one that stopped being true.*

- The template is under a STRICT 32 KiB gate — never raise the limit; externalize to a companion instead.
  It sits at 32682/32768 (**86 bytes free**, measured 2026-08-11 by `bash tools/check-template-size.sh`
  — read that number FROM the gate, never from here: this number moved TWICE in one day, so treat any figure written here as a lower bound on staleness), so a line added to it either fits that margin or
  funds itself by moving prose into `parallel-coding-governance.domain-rules.md`. It was 80 free
  before the unattended build's playbook unit needed 114 for the standing-mandate clauses and funded
  them by externalizing the kickoff-manifest merge exception — a ~490-byte procedure that only
  applies when the project keeps a manifest — into companion §1. That is the sanctioned move and it
  is available again: the §-stub parentheticals in §9/§11/§12/§13 duplicate the companion's own
  headings and are the next candidate. (Paraphrased rather than cited by id on purpose — the drift
  signal `non_terminal_specs_cited_by_product_source` counts `.claude/` as product source and sits
  AT its pin, so naming a non-terminal spec's id here reds the bar. It did, once.)
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with `git diff --cached --check`.
- A gate that BYTE-COMPARES a generated file needs both halves: an `eol=lf` pin so the committed
  bytes are right, AND CR normalisation in the comparison so a Windows checkout does not red every
  line. Either alone leaves the file green only right after a render.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook is wired on `Workflow|Agent` and enforces FOUR rules (kit 1.3):
  route fan-out through the helpers; a verify stage spawns at most 5 agents TOTAL; the BOUND ITSELF
  is resolved wherever it is written (call site, default parameter, `gov:bounded-fanout` width); and
  a direct `Agent` spawn is COUNTED at runtime, 5 per user prompt. Concurrency is not a budget —
  `boundedParallel(t, 5)` still spawns N agents for N findings, five at a time. Bound the group
  COUNT: `chunk(x, Math.ceil(x.length / MAX_VERIFIERS)) // gov:fixed-verifiers`. The 5 is a FILE
  CONSTANT: `AGENT_CAP` is refused, not honoured, and an `<expr> || <int>` fallback no longer
  resolves as a bound anywhere. Binding rules: `memory/guides/REVIEW-PROTOCOL.md`. Ready-made
  harness: `tools/workflows/tier2-review.js`.
- Editing `.claude/settings.json` DOES take effect mid-session — hooks are re-read, not snapshotted
  at session start. Measured 2026-08-10 by wiring a throwaway `PreToolUse` hook and observing it fire
  on the very call that checked for it. This is what makes a live hook measurement trustworthy; do
  not assume the opposite and skip the probe, and do not skip the LIVENESS half either, because a
  hook that silently never fires returns a false negative that looks like a real answer.
- A new gate PREDICATE is run over the real tree BEFORE it is trusted. Both source-level bans added
  in `TOOL-aBatchedLintel-1` were wrong on their first run — the interval ban matched the `) {`
  opening each if-block, and the `LC_ALL` ban fired on the comment explaining the ban. Hit twice more
  by the agent-cap bound-reading predicate: an argument-position check denied
  `tools/workflows/tier2-review.js` on its prettier TRAILING COMMA, which splits into a phantom empty
  argument, and an acceptance grep for a banned spelling matched the comment explaining why it was
  banned — the `LC_ALL` shape again.
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
- A gate that returns a VALUE on stdout cannot also report on stdout. `fail` echoes, so
  `x=$(some_check …)` captures the diagnostics into `x` and the operator sees only the downstream
  symptom. Measured 2026-08-10: `--close` printed "a machine-checked DoD item is unmet" and swallowed
  the sentence explaining why. Return via a global (or a separate fd); the value channel and the
  message channel must not be the same channel.
- When hardening a check, ask what SUPPLIES each of its inputs. The unattended mandate check was
  sound in design and defeated three ways at once because all three inputs were reachable by the
  subject it distrusts: a value read back from the file the run writes, an anchor ref the run can
  `git branch -f`, and an error signal dropped with `|| true`. Reproduce each with a control before
  and after — a review finding that has not been reproduced is a hypothesis.
- CRLF in a worktree is NOT limited to what a gate byte-compares, and `check-wiring.sh` will never
  tell you: its eol population is scoped to `.claude/` paths carrying the pin. Every UNPINNED path
  smudges, because `.gitattributes` opens with `* text=auto` and this fleet runs `core.autocrlf=true`.
  Measured 2026-08-10: all four `tools/workflows/*.js` came out at CRLF (`tier2-review.js`, 350 CR
  bytes) and **no gate saw it** — `check-workflow-syntax.js` parses CRLF happily. It surfaced when
  the shipped Tier-2 harness could not be LAUNCHED: a workflow script is inlined into the tool call
  that runs it, and the permission layer rejects control characters in that payload. Ask which
  CONSUMER reads a file whole (a launcher, a `.`-sourced conf, a hook), not which gate diffs it.
  Pinned since: `tools/workflows/*.js`, `skills/session-kickoff/SKILL.md`, `tools/unattended/*.md`,
  `.unattended.conf`. Still unpinned and latent: `AGENTS.md`, `WIRE-INTO-PROJECT.md`, `.gitattributes`.
- A NEW record file under `memory/gotchas/` needs THREE things, and two of them are separate gates:
  `gotchas.py --write` to re-render `INDEX.md` (hygiene check 17), and a dossier claim for its key
  (codebase-map coverage). Adding the file and regenerating the map is not enough — the coverage
  inventory reads TRACKED files, so a `test_codebase_map.py` run before `git add` reports ok over a
  file it cannot see, and the gap surfaces on the full bar instead. Stage first, then measure.
- This node's `merge.rows.driver` pointed at `tools/memory-tree/merge-rows.sh`, which does not exist
  (only the `.py` and its `.test.sh` do), so `bash tools/check-wiring.sh --check` exited 1 on a
  worktree whose SessionStart line had said `ok merge`. `--fix` correctly DECLINES to overwrite a set
  value, so it self-heals only an UNSET one. Remedy, and it is machine state that travels with no
  commit: `git config merge.rows.driver 'bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P'`.
  Worth front-loading because a broken value reads as configured to every check but this one.
- Template parity and PLACEHOLDER COMPLETENESS are two different questions about a rendered file. A
  render whose conf declares nothing for a key is byte-identical to a fresh render — perfectly in
  sync — and instructs the agent to invoke the placeholder's own name as if it were a tool. A
  `--check` that only diffs against the template cannot see that; grep the render for a surviving
  brace-shaped placeholder as its OWN arm. (Paraphrased on purpose: `manifest-check.sh` check 1 bans
  the literal double-brace shape anywhere in this file, so quoting one reds the manifest — the same
  trap hygiene check 12's skeleton scan sets, one file over.)
- A "core set ⊆ effective set" assertion is VACUOUS whenever the checker COMPOSES the effective set
  from the core one. Measured 2026-08-10 in the new unattended leg: the leg built `PHASES` as
  `$PHASES_CORE $PHASES_EXTRA` and then asserted every core member was in `PHASES` — a subset by
  construction, unfailable, and it armed cleanly. Pin a shrink-only COUNT instead (the `ARMS_FLOORS`
  / `baseline.toml` shape), so the names stay single-sourced and deletion still reds; and make an
  UNDECLARED floor its own refusal, because omitting the key is the quietest way to disarm a pin.
  The general rule: an assertion between two values the same code derives from one source is a
  tautology — assert against something declared INDEPENDENTLY.
- A positional in a gate's `fail` message CANNOT be armed. `check-arms.py` reads `${?[A-Za-z_]…` as
  an interpolation to drop, but a bare `$1` is literal text, so it lands INSIDE the signature and no
  assertion can ever name it — the branch reads unarmed no matter what the test says. Bind the value
  to a name (`local slug="$1"`) and put it at the END of the message, after the literal sentence.
  Measured 2026-08-10 on two branches of the new driver. This also means `check-arms.py` DISCOVERS
  any tracked `*.sh` that defines `fail() {` and calls `fail <n> "` — a new script gets pulled into
  the meta-gate's population automatically and needs a sibling `<stem>.test.sh` with a positive arm
  per branch, plus an `ARMS_FLOORS` entry.
- Hygiene checks 13-19 are OFF unless a pin is armed. `corpus_ids.py`'s `armed(conf)` returns early
  when every one of `ORPHAN_ID_PIN`/`DEAD_PATH_PIN`/`READ_PATH_CEILING`/`CHARTER` is blank, and
  `gotchas.py` short-circuits on an empty record set. So a fixture tree written WITHOUT pins arms
  nothing in that range: measured 2026-08-10 while adding a check-13 arm — `def_builds` held both
  colliding slugs and `--check` still returned 0. The main fixture tree in
  `check-memory-hygiene.test.sh` deliberately sets no pins, so any 13-19 arm belongs in its own
  scratch tree with the pin set. This is the `vacuous-selector-empty-population` class one level up:
  the population is fine, the CHECK is switched off.
- Under MSYS/git-bash one directory has two spellings (`/tmp/x` vs `/c/.../Temp/x`) and mount points are
  NOT symlinks — never compare path strings (or `realpath --relative-to` outputs) across those flavors;
  decide repo membership via git identity (`rev-parse --show-toplevel`/`--show-prefix`), both sides
  normalized through the same `cd … && pwd` chain.
