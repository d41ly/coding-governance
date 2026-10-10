# Run mandate — aHomedAnchor

**Serves:** journal TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2

node a · 2026-10-09 · order 0 · streams tooling · authorized-by prompt

## The prompt, verbatim

The owner invoked `/unattended` with `--prompt` and this value, taken as the prompt itself because
it carries whitespace and names no readable file:

```
The unattended kit rules have to be amended to allow <slug> mode to run from the same worktree/branch or local main that wrote the build. Pushing to origin should not be a requirement. Do not run the kit self-tests for this build.
```

The bytes travel here rather than a reference, because the build folder is the authorization and may
not point at a file that can be edited after the run starts.

## The one opening turn

Four questions, one `AskUserQuestion`, every answer the recommended option:

| Question | Answer |
|---|---|
| which push stops being required | authorization only: starting and holding a run; landing still pushes `main` |
| how the no-push anchor is switched on | a new value, `ANCHOR_SCOPE="local"`; this repository's conf flips to it |
| which modes the local anchor admits | all three, `slug`, `prompt` and `recipe` |
| how the bar admits a local-anchored BASE | it reads the scope from `.unattended.conf` at the remote's default-branch tip |
