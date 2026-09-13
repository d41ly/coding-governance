**Serves:** journal TOOL-aBatchedArm-4

# Build brief — TOOL-aBatchedArm-4, declared execution modes for the self-test runner

The spec is `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md` at rev-4. It
survived three adversarial audit rounds and its loop exited NON-CONVERGENT with disposition FOLD, so
it is not re-reviewed: **build what it says**, and where it names a line number, that line is the
edit. This brief carries what a builder oriented in the spec alone would still have to re-derive.

## The one sentence

Two runners each get a DECLARED mode — `--serial` or `--pooled` — and every bare form that would
execute a suite REFUSES naming both. Nothing about what any suite asserts changes. Nothing about the
pooled hang bound changes; that is unit 5.

## Read these before the first edit, in this order

1. The spec, whole. §2 is the edit list, §6 is what proves it, §7 is what grades it.
2. `tools/run-gates/run-selftests.sh` lines 100-120 (the argument parser), 290-330 (the width block
   and the `--check` exit), 370-390 (where the refusal goes), 355-365 (the row checker), 655-665
   (the withheld counter), 740-760 (the remedies).
3. `tools/unattended/run-unattended-gates.sh` lines 115-165 (the verb parser — it takes ONE
   positional today and must take two), 250-265 (the `--list` count and the delegating call).
4. `tools/run-gates/run-selftests.test.sh` — find the five arms that invoke the runner with no
   `--check`, `--list`, `--rank`, `--sweep` or `--kit`; those are the bare-mode arms.

## The write set, declared before any edit

Nine files, and the spec's §4 Files touched is the source. Declare all nine with `--dispatch` before
the first edit; if building uncovers a tenth, re-declare WIDER before the commit, never narrower.

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/README.md` ·
`tools/unattended/kit.toml` · `.githooks/gate-env.sh` · `AGENTS.md` ·
`memory/guides/SESSION-KICKOFF.md` · `memory/builds/aBatchedArm/` (records).

## Traps this repo has already recorded, so you do not pay for them again

- **Every `.sh` edit is verified at the BYTE level.** `core.autocrlf=true` here, so the working copy
  is CRLF and `git show rev:path` smudges. Trust `git cat-file -p <oid>` and `git diff --cached | cat -A`.
  Edit with the Edit tool, never with a Python `open()` in text mode — that eats bare CRs.
- **The install-prefix leg is a BAN in both directions.** `tools/install-prefix-carried.txt` pins
  `run-selftests.sh` at six carried literals and `run-unattended-gates.sh` at its own count. Every
  usage line you rewrite is ALREADY one of them: edit the occurrence in place, add none, remove none.
  `ROSE` means you added one; `SLACK` means you removed one or raised the count. Run
  `bash tools/check-install-prefix.sh` before committing.
- **`AGENTS.md` sits 18 bytes under the charter-size cap.** The `:519` edit appends ` --serial` —
  nine bytes — and nothing else. Run `bash tools/check-template-size.sh` before committing.
- **The kickoff manifest is a ratchet.** `memory/guides/SESSION-KICKOFF.md` edits at `:132` and
  `:168-169` require the runner join its `watch:` list and `last-audit` re-stamped in the same commit,
  with a delta line in the commit message. Run `bash skills/session-kickoff/manifest-check.sh`.
- **A new gate is not landed until its failing case has been observed.** For every arm you add to
  `run-selftests.test.sh`, stage the break, run the suite, confirm RED, unstage. Do this for: the
  bare-`run` refusal, the regex admitting `1/8` and refusing a digit-led path, and the
  pooled-withholds / serial-grades pair.
- **`--only 28` is broken** (`TOOL-aHoistedPass-37`) and is not yours. Do not touch it.

## The refusal's exact position in the runner

Between the `--list` exit at `:374` and the filter-liveness refusal at `:383`. Not before `:322`,
where the width block runs on every bar through the unguarded `--check` leg. Not after `:383`, where
the fifth bare-mode arm's verdict would change. The spec's F2 records why.

## The kit runner's grammar, exactly

Two positionals, either order. Verb: `--selftests` (default when absent), `--checks`, `--all`.
Mode: `--serial`, `--pooled`. Every verb that reaches the self-test half — bare, `--selftests`,
`--all` — refuses at the parser when the mode is absent, exit 2, naming both. `--checks` takes no
mode. Under `--serial` the delegating call at `:263` passes `--serial`; under `--pooled` it passes
`--pooled`. The summary line gains ` · serial` or ` · pooled, <k> cost verdicts withheld`, where
`<k>` is parsed from the runner's own `cost verdict(s) WITHHELD` line. Nothing else it prints changes.

## What done looks like

- Every AC in §6 observed, each with the command that observed it in the acceptance ledger.
- `bash tools/run-gates/run-selftests.test.sh` GREEN with the new arms and their floor moved.
- `bash tools/run-gates/run-selftests.sh --check` GREEN — this is the unguarded bar leg.
- `bash tools/unattended/run-unattended-gates.sh --checks` GREEN (no mode needed).
- `bash tools/unattended/run-unattended-gates.sh` exits 2 naming both modes.
- The four install-prefix, charter-size, manifest and line-length gates green on the staged diff.
- One commit for S1 alone, one for S2 through S8, each with the unit id in its subject.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` run after each commit and acted on.

Do NOT run the full self-test population, `--pooled` over the real rows, or the unattended gate
selftest as verification; they cost hours and the spec's AC4 pooled arm is unit 3's measurement.
Verify the refusals and the mode plumbing against the runner's own test fixture.
