---
name: header-rationale-contradicts-the-registration
description: a hook's header gives a reason for its registration that the registered matcher contradicts, so a reader narrows the matcher to the stated reason and drops the channel the hook alone carries
kind: class
universal: false
---

# A hook's header rationale contradicts its registration

## Symptom

A hook's header explains why it is registered, and the reason it gives covers fewer tools than the
matcher its fragment and the settings file register. Nothing reds, because a header executes
nothing. A reader who trusts the reason narrows the matcher to it, or calls the hook redundant on the
tools the reason leaves out, and the line the hook alone carries stops reaching the session there.

## Where it bit

The closing diff review of the dKeptSession build,
2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1, finding 8, item L3. The
`WHY POSTTOOLUSE` paragraph of `tools/unattended/mail-notice.js` said the `PostToolUse` registration
existed only to cover the tools the hooks kit's scratch-guard matcher does not route, while
`tools/unattended/mail-notice.fragment.json` and the settings file register it on matcher `*`, and
scratch-guard's `PreToolUse` context carries the card pointers and no mail. KICK-dKeptSession-79 S8
rewrote the paragraph: registered on every tool, the only carrier of the unread-mail line.

## What to do

Hold a hook header's coverage sentence against its registered matcher, in its fragment and in every
settings file that installs it, whenever either changes. Name what the hook alone carries and say
what any sibling hook on another event carries instead. The nearest class is
`comment-claims-a-check-the-case-does-not-run`, a comment crediting code with more or less than it
runs; this one credits a registration with a reason its matcher does not have.

## The gate

There is no machine gate: no reader parses a header's prose against a matcher. A reader holds a hook
header's coverage against its registered matcher.
