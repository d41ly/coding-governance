# TOOL-dPlacedRequest-56 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-56

The unit was built from its spec at rev-8 on base `634946b2a`. It builds the product its first
section lists as left: the scratch-directory case in `skills/session-kickoff/manifest-check.test.sh`
(S7, S8) and the torn-stamp and duplicate-key rows in `tools/unattended/unattended.test.sh` (S20,
S22), each suite's floors raised with a `RAISED` comment. Every other item is observed by a probe or
stands as the spec resolves it. No gate, suite or bar ran in this pass. The new case and rows were
cut from their suites by `awk` and run alone: the case under a stand-in `check_eq` and counters, the
rows over the suite's own lease fixture helpers (`write_lease_fixture`, `add_lease_commit`,
`add_claim_sighting`, `read_clock_row`, cut the same way) against the real driver and the rows'
scratch copies. The oracle is the block under the spec's "The oracle the close runs" heading, cut
by `awk` and run by `bash` on fixture repositories built by the probe under `%TEMP%` in spec 55's
shapes; spec 55's block was cut the same way.

**Evidences:** TOOL-dPlacedRequest-56
- AC3 — `rm -rf "$pr_h/once" "$pr_h/held" "$pr_h/release"`: the block cut by the criterion's `awk` holds its `for pr_n in 1 2 3` loop, and the loop holds that clear once, `zq-race-marker-48-%s` on both texts, `pr_e0=` once and `tail -n "+$((pr_e0 + 1))"` once; the block holds the `jobs -p` row. (DERIVED)
- AC3 — `jobs -p`: a scratch copy of the block with the clear deleted held it in its loop zero times, the red. (DERIVED)
- AC6 — `version oracle: rev-list failed`: under a stub `git` first on `PATH`, exiting 128 with no output on a `rev-list` carrying `--count`, the block printed that line and exited 2; spec 55's block printed its header with an empty count, an `integer expected` error and `version oracle: walked no commit of the build`, exit 2, the red. (DERIVED)
- AC6 — `rev-list failed`: with no stub on the same merge the block printed the header ending `· 2 commits` and both version lines, exit 1, so the stub is what moved it. (PINNED)
- AC6 — `version oracle`: on spec 55's AC1 bump merge the block printed the header ending `· 2 commits`, then `-KIT_UNATTENDED_VERSION=1.110` and `+KIT_UNATTENDED_VERSION=1.111`, exit 1; on the clean merge the header alone, exit 0. (PINNED)
- AC6 — `version oracle`: under spec 55's AC2 stub, exiting 128 on a `log` carrying `-p`, the block printed its header, the stub's `fatal:` line and `version oracle: the walk failed`, exit 2. (DERIVED)
- AC6 — `version oracle`: on spec 55's AC3 shapes, a base of forty zeros printed `base does not resolve`, and the run branch before the merge, another build's landing under a branch commit, the default branch merged into the branch, and this slug's earlier landing under a later base each printed `no prepared merge on HEAD`; every one exited 2. (DERIVED)
- AC6 — `version oracle`: on spec 55's AC4 merge built by `git commit-tree -p <tip> -p <base>` the block printed the header ending `· 0 commits` and `walked no commit of the build`, exit 2. (DERIVED)
- AC6 — `version oracle`: on spec 55's AC5 shape, a `records: close` commit stacked on the bump merge, the header named the merge's `<t8>^1..<t8>^2` and both version lines printed, exit 1. (DERIVED)
- AC7 — `claims — skipped: no scratch directory under`: the case cut by `awk '/TOOL-dPlacedRequest-56 AC7/,/^$/'` ran its `check_eq` green, `derive_claims_line write` printing that line with the staged `$s/f/sub` path, and held no `chmod`. (DERIVED)
- AC7 — `awk`: the first cut also caught the floor comment, which named the same id and opened a second range to the file's end; the comment was reworded so the cut holds the case's own lines alone. (DERIVED)
- AC8 — `the scratch-directory stage did not take`: a scratch copy of the case staging a `chmod 555` directory in place of the file printed `FAIL DPR56 AC8 the scratch-directory stage did not take`, counted one failure and no pass, and judged no cell. (DERIVED)
- AC12 — `grep -cE`: the criterion's pattern over `memory/gotchas/a-merge-of-the-default-branch-read-as-additions.md` printed 0, and over a scratch copy with a bare first-parent row planted it printed 1, the red. (DERIVED)
- AC16 — `grep -cF -e`: each of spec 51's AC1 commands over the record, `--first-parent --no-merges <base>..HEAD`, `--first-parent -p <base>..HEAD` and `--no-merges HEAD^1..HEAD^2`, printed 1 and exited 0. (DERIVED)
- AC20 — `read_clock_row`: the torn-stamp row printed `live` on `$SCRIPT` and `unknown -` on `$oc_copy/torn.sh`, and its copy row read the walk's ISO-shape clause once in the driver and not at all in the copy. (DERIVED)
- AC21 — `description`: `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` printed the record's checklist entry with its front-matter `description` value byte for byte as its second line, the field `tools/memory-tree/gotchas.py#build_record` reads. (DERIVED)
- AC22 — `read_clock_row`: the duplicate-key row printed `stale` on `$SCRIPT` and `live` on `$oc_copy/last-line.sh`, and its copy row read the first-line match once in the driver, not at all in the copy, and the unguarded match once in the copy. (DERIVED)

## Items diverged

None: each item the spec builds or observes held as written. Two readings of the design's case sketch
were taken in the suite's own idiom and change no criterion: the suite defines no `fail` function, its
`fail` being a counter, so the stage-failed branch prints its `FAIL` line and counts it as the suite's
neighbours do; and `mktemp -d` takes the suite's own `$TMP` template, so the trap removes the case's
scratch with the rest.

## Owed at the close

- New arm: `tools/unattended/unattended.test.sh`, AC20 and AC22, RED-first observation by the main loop; the suite is waived for this build's landing by README rule 8, and its clean reading is owed with PLAY-dClosedLoop-14.
- New arm: `skills/session-kickoff/manifest-check.test.sh`, AC7 and AC8, RED-first observation by the main loop, and the `manifest-check self-test` leg green at the raised floor.
- The legs the spec's Gates section names, run once by the main loop.
