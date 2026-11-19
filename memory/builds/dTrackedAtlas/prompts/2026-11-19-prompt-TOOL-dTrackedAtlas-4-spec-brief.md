**Serves:** research TOOL-dTrackedAtlas-4

# Spec brief — TOOL-dTrackedAtlas-4: the page regenerates on node d after a landing, with nobody running it

You author ONE spec and write no product code. Read first, whole: the build README
`memory/builds/dTrackedAtlas/README.md`, the prompt record
`memory/builds/dTrackedAtlas/prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md`, the committed spec of
TOOL-dTrackedAtlas-1 under `memory/builds/dTrackedAtlas/spec/`, `memory/TEMPLATE-SPEC.md`, and
`memory/guides/BUILD-METHOD.md` at `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`,
`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`, `doc.build-method#m5-recall-and-reuse` and
`doc.build-method#m12-research-test-choose-when-the-solution-is-not-given` (no seam decides this, so M12's candidates and discriminating
tests bind).

## The mechanism

After a landing onto main on node d, the page at `C:/projects/coding-governance-atlas/closed-loop-atlas.html` is
regenerated from the landed tree without anyone typing the command. It is a switchable behaviour whose default is
the answer (the owner's principle: every behaviour is a switchable policy, the default on, the allowed values
including off), and it does nothing on a node without the page home.

## Facts and constraints

- Landings run through `tools/push-main.sh` (`LANDER_MODE="in-place"` in `.unattended.conf`: `--prepare`, then
  `--land` from the run's worktree, which pushes `origin/main`). Hooks live in `.githooks/` (`core.hooksPath`),
  shared by every worktree and every node; `.claude/settings.json` wires harness hooks; node identity is machine
  and user, never a path (the charter's node registry; `tools/playbook/fleet.toml`).
- Nothing under `tools/` may change in this build: it owes a `GATE_SELFTESTS` bar this run may not run. So the
  lander, the policy kit's `catalogue.toml` and every kit stay as they are; where the switch would belong in the
  policy catalogue, M3 decides its interim home and the later move is filed as an ask. A `.githooks/` file is
  carried by kits: read what `tools/check-hook-destinations.sh`, `tools/check-install-prefix.sh` and
  `tools/check-wiring.sh` grade before you pick a hook.
- Candidates to weigh at least (M12, differing in mechanism): a git hook firing when main or `origin/main` moves;
  a harness hook in `.claude/settings.json`; a durable scheduled task that regenerates when the page is stale
  (unit 3's check). For each, write what would make it lose before testing it, then test it by the smallest probe
  against the real tree (a scratch clone for anything that fires a hook). Creating an OS-level scheduled task is a
  persistent machine change the owner must approve: a candidate needing one is parked, not picked.
- The regeneration never commits the page, never blocks or slows the landing past a stated bound, writes only to
  the page home, and leaves a line saying what it did or why it skipped.
- Unit 3 (specced beside you) adds a staleness `--check` on a page; you may call it through the CLI its spec
  states, and only through that.
- Acceptance: on a scratch clone, a landing onto main with the switch on regenerates a page whose stamp names the
  new commit; with the switch off it does not; on a node without the page home it does nothing and says so; each
  observed red before green. No gate, suite or bar in a criterion.
