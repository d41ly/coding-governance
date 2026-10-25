**Serves:** research TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56

# The promoted-fix pass — dPlacedRequest round 5, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-10-spec-writer.md`, run direct/add35d2325a57aa74, extracted from its transcript by script.

The one `[bar]` hit is fixed, with an edit to TOOL-dPlacedRequest-56 alone, and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now exits 0 with no hits. Nothing was committed and no index was rendered.

**The hit:** AC5 had `tools/unattended/unattended.test.sh` as a backticked token of its own. The spec-tokens checker reads a token like that as a suite run, even though the criterion only greps two specs. AC5 now spells the observation as one grep pipeline:

```text
`grep -n 'in sequence' 2026-10-25-spec-TOOL-dPlacedRequest-48.md 2026-10-25-spec-TOOL-dPlacedRequest-50.md | grep -F tools/unattended/unattended.test.sh`
```

It passes when that prints one line from each spec and each line names the other unit. The red case is unchanged. With `grep` first after the `|`, the checker's pattern (`tools/check-spec-tokens.py:357-361`) treats the suite path as a grep argument, not a run. The path is tracked in git, so the path check still resolves it. The suite stays on its §7 `New arm:` line, which covers AC3, AC4, AC20 and AC22.

**Rev and log:** the Status header is now rev-2, and §9 has a rev-2 line for this change.

**One thing to know:** the `in sequence` lines don't exist in units 48 and 50 yet, so AC5 would print nothing today. That is expected: unit 56's S5 adds them when it is built.

I staged the edited spec, as the brief's hygiene run expects.

The file: `C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-56.md`
