# Brief — KICK-aReplayedCard-1, the card verbs

**Serves:** journal KICK-aReplayedCard-1

What this pass is handed: the unit's spec at rev-4, three spec audits and their folds, the build
README, and `skills/session-kickoff/manifest-check.sh` at 427 lines with its self-test at 671 lines
and `FLOOR_ASSERTIONS=62`.

What it builds: the `--card --write`, `--card --replay` and `--card --path` verbs on that checker,
their arms, the manifest's `registry:` key riding a format bump from v1.3 to v1.4, and nothing
that reads the card.

What is not obvious, each verified at the base:

- **The argument loop at the script's lines 74–79 takes ANY unrecognised argument as a manifest
  path** (`*) MF="$a"`). The card verbs and `--session <sid>` must be consumed before that loop
  reaches them, and they run AFTER the repo probe at line 72 and the manifest resolution at lines
  82–108, because `registry:` is read from `$MF`'s audit block with the same `getval` the block
  parser at lines 210–220 uses. `--card --path` alone answers before any of that.
- **Refusals are the `MANIFEST env ERROR — …; exit 2` shape** at lines 72–73 and 112, never the
  numbered `fail N` recorder at line 133, which `check-arms.py` counts and which would misnumber
  a manifest check. `ARMS_FLOORS` must not move; `FLOOR_ASSERTIONS` in the self-test must, by the
  arms you add, and every arm is observed RED before it lands — the ledger names how each was
  staged.
- **The kit version has five carriers and a leg that joins them.** `KIT_MANIFEST_VERSION="1.3"`
  and its `gov:kit kickoff-manifest@1.3` marker at `manifest-check.sh:21`; the template marker
  `kickoff-manifest: v1.3` at `MANIFEST-TEMPLATE.md:3`; the live manifest's marker line in
  `memory/guides/SESSION-KICKOFF.md`; `tools/check-kit-versions.sh:53-60` compares the first two;
  the `kit version markers` and `verdict epoch` legs grade the rest. Bump them together to 1.4, and
  the checker's own WARN at line 127–129 tells you whether the live manifest agrees.
- **The seed's audit block gains `registry: {{REGISTRY_PATH}}`** so C1's placeholder check forces
  the fill; `WIRE-INTO-PROJECT.md` §4's retrofit list and the manifest recipe gain the key; the
  self-test's seed arm at lines 615–617 asserts every key the card verb reads is present in the
  seed. This repository's manifest gains `registry: AGENTS.md`.
- **The manifest owes two stamps**: the body changes (the key and the marker), so `last-audit` AND
  `last-body-change` move, with the delta line in the commit message. `manifest-check.sh` itself
  is in `watch:`. Run `bash skills/session-kickoff/manifest-check.sh` plain and `--staged` before
  committing.
- **The card home is `$(git rev-parse --git-common-dir)/orientation/`**, shared by every worktree
  on this node. Every criterion runs in a scratch CLONE of this repository under `mktemp -d`,
  never in this worktree, and AC11 asserts this repository's real common dir holds no card the
  suite wrote. Do not leave a card for the session that runs you: `TOOL-aReplayedCard-1`'s deny is
  not built yet, but the next unit's is.
- **The toplevel spelling is the bytes `git rev-parse --show-toplevel` prints**, captured BEFORE
  the `cd "$ROOT" && pwd` normalisation at line 73 that turns `C:/…` into `/c/…`. The card's
  `tree —` cell carries the former.
- **The registry reader takes the FIRST table under `## Node registry`** (`AGENTS.md:60`), strips
  backticks, and matches `$USERNAME` by equality or the prefix `$USERNAME @`; the charter's second
  registry-shaped table at `AGENTS.md:155` must not win. The self-test's two fixture tables and
  the real `AGENTS.md` inside the clone are the AC4 fixture; on this node the answer is `a`.
- **No fetch, no ref move, no manifest audit** in the verb; AC9's arm stages a remote one commit
  ahead and asserts `HEAD`, `origin/main` and the absence of `FETCH_HEAD` afterwards.
- **`live —` reads `MEMORY_ROOT` from `.memory-tree.conf` and the row count of its `LIVE.md`**;
  either absent is `live — skipped: <why>`, never a refusal — the kickoff kit has
  `requires = []` and must keep working without the memory-tree kit. A kit file names nothing
  outside itself by literal: `AGENTS.md`, `memory/` and `LIVE.md` reach the script only through
  the manifest key and the conf.
- **Function names are graded by the lexicon leg** (`sh:shell-tokens:parser`): lead with a table
  verb — `render_card`, `derive_node_tag`, `write_card`, `print_replay` are the spec's; ask
  `python tools/lexicon/lexicon.py --suggest <name> --as sh` before inventing another.
- **The replay-written card names `--card --replay` in its header line**; the `--write` card
  names `--card --write`. The deny unit reads that byte to tell the two apart.
- **The acceptance ledger** is a `build/` record, `**Serves:** journal KICK-aReplayedCard-1`, one
  `**Evidences:** KICK-aReplayedCard-1` block, one line per AC1–AC11 in the OBSERVED form with a
  backticked token, or AMENDED with the rev and §9 line where you had to change the spec first.
  Name it `2026-09-14-build-KICK-aReplayedCard-1-1-acceptance-ledger.md`.
- **Author files with the Write tool, never a heredoc into python or sed**; the tree is LF; check
  `git diff --cached --check`. The self-test runs in seconds; the hygiene gate in minutes, never
  through `tail`.
- **Finish with the records**: spec status CLOSED with today's date, `gen_build_index.py --write`,
  `git add -A`, `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/check-spec-tokens.py`,
  `bash tools/check-kit-versions.sh`, `python tools/check-install-prefix.py` if it exists else the
  `install-prefix (shipped surface)` leg's argv from `tools/gate-legs.json`, and the self-test with
  `bash skills/session-kickoff/manifest-check.test.sh`. Commit with the unit id in the subject. No
  push, no merge.
