# TOOL-dPlacedRequest-54 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-54

The unit was built from its spec at rev-6 on base `0e36a95af`. It touches no product file: it
observes the own-merge test on this worktree's history before `--prepare`, in the one oracle block
the close runs, the one in unit 55's design section, and reads the spec texts that carry the test. No
gate, suite or bar ran in this pass. The oracle was cut by `awk` from unit 55's spec into a scratch
file under the session scratch and run by `bash`; the base was read by unit 57's S1 `awk` over the
run-state file's `## Run facts` section, never typed.

**Evidences:** TOOL-dPlacedRequest-54
- AC1 — `TOOL-dPlacedRequest-55`'s block, run in this worktree before `--prepare` with the base unit 57's S1 reads, `9e21ac76`, printed `version oracle: no prepared merge on HEAD` and exited 2. (DERIVED)
- AC1 — `TOOL-dPlacedRequest-57`'s S1 read gave the base `9e21ac760dc0a43d6ed007396922722ccee98d57`. (DERIVED)
- AC1 — `9e21ac76` is the merge fact 1 finds, `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD`; its subject is `merge: dDeclaredLoop — land onto origin/main at c1f80c00`, and it is the base itself, so the ancestor test succeeds on it. (DERIVED)
- AC1 — `TOOL-dPlacedRequest-55`'s block in a scratch copy with the subject case and the ancestor test cut, the refusal keyed on an empty `t` alone, printed `version oracle: 9e21ac76^1..9e21ac76^2 · 1 commits` and exited 0: the header names the merge fact 1 finds and the copy walks it, the red the criterion names. (DERIVED)
- AC1 — `9e21ac76`, the base, has this slug's earlier landings `60d90cb71` and `ed2fbc1f2`, deeper on the first-parent line, as ancestors by `git merge-base --is-ancestor`, so the ancestor test refuses them too: a reading beside the criterion. (DERIVED)
- AC2 — `2026-10-25-spec-TOOL-dPlacedRequest-55.md`'s AC3 bullet, cut by `awk` and squeezed by `tr -s`, names the three foreign shapes of S2, another build's landing under a branch commit, a merge of the default branch into the branch and this slug's earlier landing under a later base, and expects `no prepared merge on HEAD` of each. (DERIVED)
- AC2 — `2026-10-25-spec-TOOL-dPlacedRequest-55.md` at rev-2, read by `git show e57eca71b`, carries no AC3 bullet: the red, where no foreign shape is staged. (PINNED)
- AC4 — `2026-10-25-spec-TOOL-dPlacedRequest-52.md`'s section 8 F1 item, at rev-10 (CLOSED), reads "Superseded in part by `TOOL-dPlacedRequest-54` F1": `grep -c` for the id over the item printed 1. (DERIVED)
- AC4 — `TOOL-dPlacedRequest-54` is named by none of the same F1 item at rev-9, read by `git show e57eca71b`: the count printed 0, the red. (PINNED)

## Items diverged

None: each criterion was observed as written.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop: memory hygiene, spec tokens, lexicon naming predicates, recall floor and recall floor arms. The spec declares no new arm.
- S3, which the spec marks NOT OBSERVED here: the close runs unit 55's block on the prepared merge after the last `--prepare`, with the observing run's base.
