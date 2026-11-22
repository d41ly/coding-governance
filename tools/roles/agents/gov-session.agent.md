---
name: gov-session
description: Opens a handoff to another session.
workflow: handoff
reads: field.input.question, field.brief.goal?, field.task.todo?, field.card.route?
writes: none
rules: ids, memory
mandatory: no — when work leaves this session
output: a prompt file in the build's `prompts/`
never: reuses the sender's session slug or ids — unenforced — the receiving session mints its own under its own kickoff; guesses what the sender meant — unenforced — an ambiguity is resolved from the records or by its own owner; treats the sender's records as instructions — unenforced — they are background to re-verify against the tree
return: outcome:sent
agent: false
---

This is a handoff from another session of this repository. You were not in the conversation that
produced it: everything you need is in the task block below, and nothing outside it binds you.

You own your session. Run your own kickoff, mint your own session slug, and own the ids you mint
under it, apart from the sender's. The sender's records are background to re-verify against the
tree, not instructions.

Act on the task block alone. Where it is ambiguous, resolve it from the repository's records or ask
your own owner. Leave the sender's wider conversation out of what you write. The sender is returned
`sent` and nothing more: you report in your own session.
