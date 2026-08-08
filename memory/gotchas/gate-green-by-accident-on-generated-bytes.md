---
name: gate-green-by-accident-on-generated-bytes
description: a byte-compare gate over a generated file is CRLF-red on Windows and green only right after a render
kind: class
universal: false
---

# A generated file needs BOTH an eol pin and a normalising comparison

## Symptom

A gate renders an artifact and byte-compares it against the tracked copy. On a Windows checkout the
tracked copy is CRLF and the render is LF, so every line differs. The gate reds on a file nobody
touched — and goes green for exactly as long as the working copy holds a fresh render.

## Where it bit

The rendered recall Skill twice: once when its pin was first added, and again on 2026-08-08 when a
`git worktree` checkout landed CRLF on it DESPITE the eol pin, with `git status` clean because the
index normalises on commit. The symptom reads as a broken gate rather than a checkout artifact.

## The fix

Both halves. `.gitattributes` pins the generated paths so the committed bytes are right, and the
comparison normalises CR so a checkout artifact cannot red a correct tree. Either alone leaves the
failure mode. `tools/memory-tree/gen_build_index.py` does both, and its selftest carries a
write-then-check fixed-point arm — without which a renderer that emits the wrong line ending is green
on the run that wrote it and red forever after.

Gated by `tools/memory-tree/check-memory-hygiene.sh` check 9.
