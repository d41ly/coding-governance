**Serves:** research TOOL-dQuietDisk-7

# Spec task — dQuietDisk: unit 7's pre-build divergences, ruled

You write specs only. Do not commit. Unit 7's first pass (unit harness run `wf_696a0780-a50`) probed the spec against
the tree before writing any code, and four of rev-5's claims failed. Nothing was built. The run has ruled on each
point (`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`). Write the rulings into
TOOL-dQuietDisk-7, rev-5 → rev-6, and add a revision-log line naming this task by its file stem. The unit's goal, the
template cache, does not move.

## The rulings

1. **Every clone drops its remote.** rev-5's S10 declared keep-remote for the line-length suite on the claim that its
   gate "runs git rev-parse alone". It does not: on a breach the gate reads `budgets.py resolve --explain`, and the
   policy reader finds the landed revision through the remote ladder
   (`tools/policy/policy.py#derive_landed_revision`). With the remote kept, an arm reads the template's commit on
   `origin/master` instead of its own commit on local `main`. The builder probed it, and the arm stayed green only
   because the catalogue default equals the value it commits. **Ruling:** keep-remote is removed. Every clone the
   cache hands out runs S5's `git remote remove origin`, so a clone reads its remotes exactly as the `cp -a` copy it
   replaces did.

2. **No keep-remote option.** With ruling 1, S7 needs no declaration for it and the Inventory gains none (YAGNI).
   `--template` stays `build_fixture`'s only new option.

3. **A cached clone costs three git processes.** `GIT_TRACE2_EVENT` records a local `git clone --shared` as two
   processes, `git` and `git-upload-pack`, and the remote removal is a third. AC7's figure for a cached call is three
   [PINNED, measured by the builder 2026-11-22]. State it in S5, S8 and AC7.

4. **The line-length suite does not move onto the cache.** Its arms copy the fixture with `cp -a` and spawn no git, so
   a clone per arm adds at least 38 git processes [PINNED, the builder's count] where the base spends 20 `cp` and none.
   That contradicts the build's acceptance: a suite moves onto the cache only where it then spends fewer git processes
   and fewer temp entries. **Ruling:** `tools/check-line-length.test.sh` leaves Files touched and scope, along with
   S7's line-length clauses, S10 and AC3's and AC9's line-length readings. The cache is proved by its own arms in
   `tools/lib/lib-selftest.test.sh`, which AC9 now reads. Units 10 to 13 are its consumers. Each suite there builds a
   git repository per case, so the saving is real. Name them in section 4 as the consumers.

5. **How the bash face finds a python.** S9's `policy.py get` from `lib-selftest.sh` resolves python by sourcing
   `tools/lib/resolve-python.sh` beside the library. A copy-installed suite carries that block inline, as the kit
   rules already require. Say so in S9.

6. **The atomic rename.** Plain `mv` into an existing directory nests the stage inside it rather than failing. The
   bash face renames with `mv -T <stage> <key dir>`, which fails when the key exists, and treats that failure as
   "another run built it". Say so in S1.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-7`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.
- Units 10 to 13 consume this unit. If a ruling changes the interface they will call, list each change in your return.
