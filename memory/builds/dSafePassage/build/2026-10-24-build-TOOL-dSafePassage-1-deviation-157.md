# TOOL-dSafePassage-1 deviation 157 — TOOL-dSafePassage-1's AC15 excludes the step's own files from its grep

**Serves:** deviation TOOL-dSafePassage-1

- **Departs from:** `TOOL-dSafePassage-1@rev-7`
- **Hand-off:** spec-revised
- **Before:** AC15 greps the tree for `template-size-limits` outside `memory/builds`, `memory/ledger` and `memory/backlog`, and reds on any hit.
- **After:** the spec at rev-8: the same grep, run with `-c`, also excluding the step's own declaring row `tools/govkit/steps.toml`, its program `tools/govkit/steps/template_size_limits.py` and its before-image under `.governance/steps/govkit/`, each with its reason in the criterion. It must print only `.governance/policy.toml:1`, the limits file's header line, which the step's up carries into the policy file word for word.
- **Cause:** builder discovery
- **Reason:** the step's row id and surfaces spell the name, and its program must open the file it migrates, so the grep printed both on every correct build and AC15 could never pass; every other path still reds it. Found by the spec writer of the re-ground (deviation 149) and fixed at the owner's ask.
- **Evidence:** `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-ac15-pathspec.md`, and the rev-8 line in this spec's §9.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer handoff `memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-2-spec-writer.md`, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** 2026-10-24-build-TOOL-dSafePassage-1-deviation-149
