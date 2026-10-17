---
name: subagent-scratch-overwrites-the-parents-files
description: a subagent shares its parent session's scratchpad, so a snapshot it names like a file the parent keeps there overwrites that file silently, and the scratch guard admits the write
kind: class
universal: false
---

# A subagent's scratch overwrites its parent's files

## Symptom

A parent session keeps working files in its scratchpad: instruments, captured outputs, snapshots. It
dispatches a subagent, which shares that scratchpad. The subagent snapshots records into the scratchpad's
root under short names, such as `systems.md` or `ownership.md`. Where the parent already holds a file of that
name, the snapshot replaces it with no warning. The scratch guard admits the write, because the path is
inside the scratchpad. The parent finds out only if the subagent says so, or when an instrument reads the
wrong bytes.

## Where it bit

dClosedLoop's ownership re-verification, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`, `[misfire]`).

One of three reviewers wrote about 110 record snapshots into the parent's scratchpad root, and 8 of them
replaced files already there. It reported the overwrite itself. No script of the parent's read those 8, so
nothing that counted was lost.

## The fix

- Give each subagent its own scratch folder in its task, and forbid the scratchpad's root.
- Keep the parent's own working files in named folders, never at the root.
- An instrument that reads a scratch file checks that file's provenance, its sha or its writer, before
  trusting it.
