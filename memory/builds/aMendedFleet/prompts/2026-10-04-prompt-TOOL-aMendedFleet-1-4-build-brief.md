# Build brief — aMendedFleet, every unit pass

**Serves:** journal TOOL-aMendedFleet-1

The brief every unit pass of this build is handed, beside its own spec. The spec is the scope; this
brief is the build's conventions. Read the mandate record `...-1-0-run-mandate.md` once for the
owner's four answers.

## The pass

1. Read `memory/guides/BUILD-METHOD.md` whole, then your unit's spec whole.
2. Re-verify the spec's evidence against the tree before you build: main moved since base
   `7af5f564`, and earlier units of this build moved it again. A criterion already met on the tree
   is built as nothing and said so in your return, never re-done.
3. Declare the write set BEFORE editing:
   `bash tools/unattended/unattended.sh --dispatch aMendedFleet --pass <unit-id> --writes <path> ...`
   one `--writes` per path. Widen it before the commit if you need another file; `.githooks/commit-msg`
   refuses a staged path outside the declaration and prints the widening command.
4. Build what the spec says. To diverge, change the spec first (rev bump + §9 line), then the code.
5. Verify with the direct checks your §6 names, each observed RED on a staged break first where the
   spec says so, then GREEN. No merge bar, no `*.test.sh` suite, no `GATE_*` run, no kit selftest
   suite: the bar and the suites run once at the close. A check that needs a suite verdict goes in
   your return as a need, not a run.
6. Commit ONCE, on the current branch, with the unit id in the subject and these trailers last:
   `Pass: <unit-id>`, any `Decided: <choice> — <why>` lines, and
   `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
7. Flip your spec's status to CLOSED in that same commit (rev unchanged unless the spec moved), and
   for a Tier-2 unit write the acceptance ledger under `memory/builds/aMendedFleet/build/` per
   `memory/HYGIENE.md` "Acceptance ledger", named `2026-10-04-build-<unit-id>-1-acceptance-ledger.md`
   with `**Serves:** journal <unit-id>`.
8. After the commit run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`, finish the
   checklist, and fix any class you violated in a second commit with the same trailers.

## Conventions this build adds

- **Kit versions are NOT bumped per unit.** Leave every `gov:kit` marker, `kit.toml` version and
  carrier alone; the main loop bumps each touched kit once after the last unit. The `kit epoch` and
  `kit version markers` legs are the close's to satisfy.
- **The kickoff manifest.** A commit touching a path on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in that same commit (the pre-commit staged
  leg refuses otherwise), re-reads §B against the change, and advances `last-body-change`. Include the
  manifest in your `--dispatch` write set when you touch a watched path.
- **Generated artifacts ride the commit that moves their source.** `python tools/memory-tree/gen_build_index.py --write`
  after any spec or record change; `python tools/codebase-map/gen_map.py --write` after adding or
  renaming a public definition; `python tools/memory-tree/gotchas.py --write` after a gotcha change.
  `git add` new files BEFORE running a generator or the hygiene gate: both read tracked files only.
- **Node d's live build** on `origin/branch/unattended-build-closing-f90fd9` is rewriting
  `tools/unattended/`. Where your spec names one of its commits, reuse those bytes exactly.
- **Ids.** Never write an id-shaped token for an id main does not define (node d's and aGraftedHelix's
  unlanded ids): paraphrase "node d's dUnstuckLanding unit 25".
- **Shared records are the main loop's.** `memory/DECISIONS.md` and `memory/project/readme-contract.txt`
  are `SHARED_RECORDS`; `--dispatch` check 49 refuses either in any pass write set. If your spec needs
  an edit to one, do NOT stop: build everything else, leave the spec SPECCED, and return the exact edit
  (file, old line, new line) as a need. The main loop applies it in a records commit and closes you.
- **New ids are the main loop's.** A pass never mints an id. If your spec needs one, return the need.
- **Scratch** is the session scratchpad your grounding sentence names; a clone or fixture repository
  goes under `%TEMP%/<short-name>`.
- **Windows host.** Author files with the Write/Edit tools; bash heredocs and python text mode corrupt
  backslashes and bare CRs. `tools/unattended/check-unattended.sh` holds raw CR bytes: edit it in
  binary mode only.

## Return

Your harness return: committed, the sha, why, a summary that names every check you ran with its
observed RED and GREEN, any need for a suite verdict at the close, and anything you parked.
