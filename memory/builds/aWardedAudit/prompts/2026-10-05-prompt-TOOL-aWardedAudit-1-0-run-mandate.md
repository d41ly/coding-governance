# Run mandate — aWardedAudit

**Serves:** journal TOOL-aWardedAudit-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-05. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> The owner has noticed that LLM sessions have been opting-in to the unattended build spec reviews on
> their own, without any owner ruling. The kit must be systemically changed in a way that only the
> OWNER can opt-in to the spec reviews, without an explicit authorization from them an LLM/agent
> should NOT go for the spec reviews and opt itself in.

## How the run reads it

- "Spec reviews" is the pre-code spec audit the build method's M4 owns, opted in today by a
  `spec-audit: <date>` line in the build README or a `SPEC_AUDIT_DEFAULT` in `.unattended.conf`.
- "Only the OWNER" is read the way rulings D12-a and D12-j already read it for `asks:` and `may:`:
  an opt-in counts only from a record the owner landed on the default branch. A README under
  `authorized-by: prompt` or `recipe` can resolve at a tip the run pushed, so its key is refused.
- Two observed self-opt-ins: `aGraftedHelix` and `dHashedPrelude`, both prompt-mode READMEs the run
  wrote, the first following the driver's own "recommend spec-audit:" line.
- No question was asked: ACCEPTANCE and GATES derive from the existing `asks:`/`may:` refusals and
  the fan-out hook's rule 0.
