**Serves:** research TOOL-dQuietDisk-9

# Spec task — dQuietDisk: unit 9's build divergences, ruled

You write specs only. Do not commit. Unit 9's first build pass (unit harness run `wf_13bf29df-96d`) built every part of
rev-5 it could and committed nothing: one claim of the spec cannot be built as written. The run has ruled on each point
(`doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`). Write the rulings into
TOOL-dQuietDisk-9, rev-5 → rev-6, and add a revision-log line naming this task by its file stem. The unit's goal, one
owned swept scratch root and one chmod-and-retry removal, does not move.

## The rulings

1. **Landed step programs are frozen, so they leave the population.** `tools/govkit/steps/conf_pins_to_ledger.py`,
   `tools/govkit/steps/registry_to_ledger.py` and `tools/govkit/steps/kickoff_facts_to_overlay.py` are programs that
   landed `[[upgrade]]` rows name in their argv (in `tools/codebase-map/kit.toml`, `tools/drift-audit/kit.toml`,
   `tools/memory-tree/kit.toml`, `tools/playbook/kit.toml` and `tools/govkit/entries/kickoff-manifest.kit.toml`), and
   `tools/govkit/upgrade_steps.py#check_frozen` fails the `step-rows-frozen` leg on any byte change to one. **Ruling,
   option (a):** S3's moved set excludes every program a landed step row names. Their two cleanup sites enter
   `memory/project/cleanup-sites.txt` as waived rows, each with its reason, and the kickoff step's hand-written hook
   stays. The section 3 non-goal "starts with its header and no row" changes accordingly, and AC4 reads the two waived
   rows. Shipping successor steps is a separate mechanism this unit does not need (YAGNI); say so under Alternatives.
2. **S4 admits two command substitutions in `run-selftests.sh`.** The pass used `$(git rev-parse --git-dir
   --git-common-dir)` and `$(derive_health_log)`, and normalised the common dir with `cd` and `$PWD` with no subshell.
   State that count, and name the `spawn-idiom-sites` row the second one adds (`pure-fn-subst`), which the main loop
   widens through `ratchet.py widen` after the pass.
3. **The cleanup ledger is no longer empty.** With ruling 1 it carries two rows, so `ratchet (populated)` has a
   population. Name the new cleanup leg in section 7 if it is not already there.
4. **Kit versions.** Section 3's "no hand bump" stands: versions move when the close mints. The pass was right to
   follow it.
5. **The pass's patches are the base for the next pass.** Name them in the revision-log line:
   `TOOL-dQuietDisk-9-build.patch` (56 files, PINNED by the first pass's return) and, for the record, `TOOL-dQuietDisk-9-frozen-steps.patch`, which the
   next pass does not apply.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-9`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and fix any red in your spec.
- Mark every figure you add PINNED, DERIVED or with an id on its own line. A section number before a noun reads as a
  count, so word around it.
