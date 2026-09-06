# aClosedDocket — the acceptance ledger for units 1, 2 and 3

**Serves:** journal TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3

*Node `a`, 2026-08-31, written by a LATER session than the one that built these units. That session
merged their code to main and left every spec reading `OPEN`, which is the state
`non_terminal_specs_cited_by_product_source` found: two OPEN specs cited from product source, against
a shrink-only pin of 2. Closing them needs this record, and this record needs observations that were
actually taken.*

**Unit 4 is NOT in this ledger and stays `OPEN`.** It is genuinely unbuilt: the only occurrence of
`disposition` in `tools/unattended/unattended.sh` is a code comment at `:3758`, there is no
`--disposition` flag, and `tools/unattended/check-unattended.sh` contains the word zero times. Closing
it would be the exact lie this ledger exists to prevent.

## What was observed, and what was not

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form, so a criterion nobody could take had to be AMENDED
rather than quietly marked satisfied — and eleven of the twenty-two were.

**The reason is one sentence, and it is a cost rather than a judgement.** Ten of the eleven name
either a fifteen-minute driver suite, a `--close` against a purpose-built fixture (each of which runs
the project's full merge bar), or a staged break in a driver that several other live sessions were
executing at that moment. The eleventh, unit 2's `AC2`, wants a directory made unwritable on a
Windows checkout, where a POSIX mode change does not reliably deny the owner.

**One defect was found and repaired in the specs rather than worked around.** Unit 2 carried TWO
different criteria both labelled `AC7`. A ledger needs one line per criterion and check 23 joins on
the label, so a duplicate is a criterion that cannot be evidenced at all. The second is relabelled
`AC7b` at rev-5.

**Evidences:** TOOL-aClosedDocket-1
- AC1 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — exit 0, and `memory/guides/BUILD-METHOD.md` M4 carries both dispositions (two occurrences of the FOLD/PROMOTE pair), so the render came from the template rather than a hand-edit.
- AC2 — `wc -c` — `tools/memory-tree/BUILD-METHOD.template.md` is 24571 B and `memory/guides/BUILD-METHOD.md` is 24560 B, both at or under the 24576 B cap the criterion names. It is the only thing measuring that cap, as its own text says.
- AC3 — `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh` — both exit 0.
- AC4 — `bash tools/memory-tree/check-method-carriers.sh` — exit 0.
- AC5 — `grep -c` for the promotion-only wording — returns 0 in `tools/unattended/SKILL.template.md` and 0 in `.claude/skills/unattended/SKILL.md`. Worth one caveat a later reader needs: that paragraph was MERGED with `TOOL-aGradedMandate-8`'s edit after this unit landed, so it now carries this unit's fold-or-promote disposition AND the words `never RETIRED`. The count is still 0 and the criterion still holds; it is simply no longer this unit's paragraph alone.
- AC6 — `bash tools/unattended/adopt-unattended.sh --check` — exit 0, so the render is regenerated from its template.

**Evidences:** TOOL-aClosedDocket-2
- AC1 — `python tools/codebase-map/reuse_lookup.py "acceptance ledger probe"` — the log went from 3 rows to 4, exactly one appended, and the new row's keys are `at`, `n_shown`, `query`, `type`, `worktree` with `type` set to `lookup`. That is the rev-2 shape the criterion asks for.
- AC2 — amended rev-5 — NOT observed: a Windows checkout will not reliably deny its owner a directory. The sibling path was observed under AC7.
- AC3 — amended rev-5 — NOT observed: it needs a `--close` against a fixture, and `--close` runs the full merge bar.
- AC4 — amended rev-5 — NOT observed, for AC3's reason.
- AC5 — amended rev-5 — NOT observed, for AC3's reason.
- AC6 — amended rev-5 — HALF observed and the halves are named apart: `python tools/codebase-map/selftest.py` exits 0; `unattended.test.sh --shard 2/2` was not run.
- AC6a — amended rev-5 — NOT observed: its observation is defined across a run of the whole suite, and there was no run to bracket.
- AC7 — `GIT_DIR=/nonexistent-xyz python tools/codebase-map/reuse_lookup.py "probe"` — printed its candidate header and exited 0 with `.git` unresolvable, which is S3a's observable.
- AC7a — `grep -cE "^\s*(import subprocess|from subprocess|import os\.popen)"` — returns 0. The predicate is the IMPORT and not the word, which is the whole point of the criterion.
- AC7b — `bash tools/check-install-prefix.sh` — exit 0 and the carried-prefix ratchet does not rise. Relabelled from a duplicated `AC7` at rev-5.
- AC8 — `bash tools/check-kit-versions.sh` exits 0, and `bash tools/unattended/check-unattended.sh` reported `GATE ok unattended kit gate` in the merge-bar run at `d554ceea`, which is check 22's key-table join accepting `MAP_CLI`.
  - **CORRECTION, 2026-09-05, by the aTunedCompass build, unit 11.** The second half of this line was FALSE when it was written. `MAP_CLI` appeared nowhere in the product: `grep -rn "MAP_CLI" tools/ .unattended.conf` returned nothing, so check 22's key-table join had no such key to accept and the merge-bar run it cites accepted the key set WITHOUT it. The gate ran and was green; what it was green ABOUT is not what this line claims. The `check-kit-versions.sh` half stands. This note SUPERSEDES rather than rewrites, because a ledger is evidence and annotating evidence is honest where editing it is not. The declaration and its reader landed on 2026-09-05.

**Evidences:** TOOL-aClosedDocket-3
- AC1 — amended rev-4 — NOT observed: two runs of a fifteen-minute suite, one deliberately under load. Neither was taken.
- AC2 — amended rev-4 — NOT observed as a staged break. What was taken is weaker and labelled so: an INSPECTION of both arms in `tools/unattended/unattended.test.sh`, confirming each extracts the driver's own `killed after <n>s` figure from its breach message rather than reading a harness clock.
- AC2a — amended rev-4 — NOT observed, for AC2's reason.
- AC3 — `git show 5a368d98 -- tools/unattended/unattended.test.sh` — exactly TWO hunks, at the `--preflight` and `$GATE_CMD` arm sites, 22 insertions and 2 deletions. No arm outside the two named in S1 changed, which is N4's observable.
- AC4 — `bash tools/unattended/check-unattended.sh` — reported `GATE ok unattended kit gate` in the merge-bar run at `d554ceea`, so the suite's own arm-count and message-literal gates still agree with the edited file.

## What this ledger does not claim

It does not claim these three units are well built. It claims which of their stated criteria were
taken and which were not, and it names the cost of each one that was not so a later session can take
them rather than re-derive why they were skipped. Eleven owed observations remain, and they are owed
against a suite this fleet already has a backlog row about.
