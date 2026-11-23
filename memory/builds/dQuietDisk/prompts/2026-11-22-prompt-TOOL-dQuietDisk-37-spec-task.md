**Serves:** research TOOL-dQuietDisk-37

# Spec task — dQuietDisk: the closing review's MEDIUM and LOW findings, batched

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read the spec brief first,
`memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`, and the round-1 closing review
`memory/builds/dQuietDisk/reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md`, its MEDIUM and
LOW sections whole. Write one new spec, `2026-11-22-spec-TOOL-dQuietDisk-37.md`, Tier-2, order 9, base the `HEAD` you
read at.

## Why this unit exists

The closing diff review converged at round 2 with round 1's five MEDIUM and four LOW findings standing. Under
`review.findings` `blocker-high-own` and a budget target of `unit`, they are promoted to ONE batched unit
(`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`, its diff-exit rule). This is that unit. Each item below takes the fix the review's skeptic judged,
or, where the skeptic judged the finder's fix INSTANCE-ONLY, the class-level fix the review states.

## The items

- **M1** — `derive_kit_attestations` (`tools/govkit/govkit.py`) has no committed check: add the govkit self-test arms
  the review names.
- **M2** — the outer swept root, the TEMP/TMP export and the Python sweep faces have no committed check: add the
  run-gates fixture-bar cases the review names, and the Python face's arm.
- **M4** — the template key ignores the builder's arguments: the class-level fix, folding the builder arguments into
  the key inside `resolve_template` itself, in all three byte-equal copies of the block (`tools/lib/template-cache.sh`,
  `tools/lib/lib-selftest.sh`, `.githooks/pre-push.test.sh`), with its arm.
- **M5** — arm 3h1 of `tools/run-gates/run-gates.test.sh` never proves the plain-guarded leg was decided by the one
  moved list: add the two assertions the review names.
- **L1** — `blob_at`'s batch branch (`tools/govkit/upgrade_steps.py`) also routes a name holding a CR to the `git show`
  spawn, as `BatchReader.read_reply` does.
- **L2** — the template race arm in `tools/lib/lib-selftest.test.sh` requires both racers to have built.
- **L3** — BlobBatch's missing, ambiguous and dead-handle branches get govkit self-test arms.
- **L4** — `tools/run-gates/run-selftests.sh`'s owned-root comment: take the review's first option if it holds without a
  new temp entry, else narrow the comment; say which and why.

**M3 is not this unit's.** Its arms belong in `tools/unattended/check-pass-order.test.sh` and
`tools/unattended/check-brief-recorded.test.sh`, unattended-kit suites the owner's standing rule of 2026-08-23 forbids
this run to run, so no pass or close could observe them RED and GREEN. The main loop files it as ask
TOOL-dQuietDisk-39 with the review's fix. Name that in section 3.

## Constraints

- Read every cited line at `HEAD` and cite by symbol or blob; the review cites older blobs, and TOOL-dQuietDisk-36
  has since changed the template block.
- Every new arm is a `New arm:` line in section 7, owed to the main loop RED then GREEN. Raise each suite's assertion
  floor by the arms it gains.
- State the files, generated outputs included. Shell-line and spawn-idiom rows grow only through
  `python tools/memory-tree/ratchet.py widen`, which the main loop runs after the pass; say so.
- Check every git command and shell idiom against the real tool. This build has ruled on these false facts:
  `git rev-parse --short` takes a single revision; a local `git clone --shared` spawns two processes; an MSYS shell
  rewrites a `!/path` argument; `git hash-object --stdin-paths` and an alternates line refuse an MSYS `/c/...` path; a
  plain `x=$(...)` assignment makes the shell-hygiene scanner follow a heredoc loop over `$x`; a function-local
  `local GIT_DIR` does not hide an exported value from children.
- A kit whose shipped bytes move moves its version at the mint, never by hand.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-37`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and fix any red in your spec.
- Mark every figure you add PINNED, DERIVED or with an id on its own line.

Return: the spec path and rev, its files touched, its arms, and any fork.
