# TOOL-aRoutedQuill-7 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-7

No merge bar and no self-test suite ran in this pass. The preflight criteria were observed by the new
arms in `tools/unattended/unattended.test.sh`, run as a slice of the suite's prologue and the new
block on node a, 2026-10-10: 60 of 60 assertions held, the block's 40 among them. The same slice run
against the pre-unit driver redded every arm but AC3's, which asserts the absence of behaviour that
driver never had. F1's probe ran rule 1's awk from the pre-unit driver and observed an exact match,
so rule 1 is built as an in-order subsequence (spec rev-3). The close still owes the legs §7 names,
the unattended suite whole among them.

**Evidences:** TOOL-aRoutedQuill-7
- AC1 — `### Limitations` — past the key, a five-sub-head record refused at check 112 naming the record, `rule 1` and `### Limitations`, and no `RUN.md` was written.
- AC2 — `--brief-skeleton` — a record carrying the seven sub-heads the fixture checker prints printed `preflight OK`, and the checker's spawn log held exactly one call, `--brief-skeleton`.
- AC3 — `PROMPT_BRIEF_SKELETON_CUTOFF` — with the key declared after the README's `opened:`, a five-sub-head record printed `preflight OK` and the spawn log held no `--brief-skeleton` call.
- AC4 — `PROMPT_BRIEF_SKELETON_CUTOFF` — with the key blank, AC1's fixture printed `preflight OK` and the NOTE naming the key as off.
- AC5 — `check 117` — with no checker tracked, the refusal named the install receipt, both probes and `the index tracks 0 manifest-check.sh`, and wrote no `RUN.md`; with two tracked it named `the index tracks 2 manifest-check.sh`.
- AC6 — `check 117` — a checker exiting 4 on the verb, a skeleton without `### Items`, and one with `### Gates` before `### Acceptance` each refused, naming `exits 4`, `### Items` and `### Gates` with the blob.
- AC7 — `### Reuse` — with the committed checker printing `### Reuse` and the working tree editing it out, a record without `### Reuse` was refused naming it.
- AC8 — `PROMPT_BRIEF_SKELETON_CUTOFF` — `grep -n` found the blank line in `tools/unattended/.unattended.conf.example`, the §8 row in `memory/guides/UNATTENDED-PROTOCOL.md`, and the initialiser entry in `tools/unattended/unattended.sh`.
- AC9 — `--brief-skeleton` — `grep -n -- '--brief-skeleton' memory/guides/UNATTENDED-VERBS.md` found the prompt path's step 3 naming `bash <check-script> --brief-skeleton` as the source of the sub-heads.
- AC10 — `kickoff-manifest` — `govkit.py plan --kits unattended,memory-tree,review-harness,settings-merge` on a scratch target printed `UNMET  [unattended   ] requires 'kickoff-manifest'`; with the pre-unit `kit.toml` staged back it printed no such row.
