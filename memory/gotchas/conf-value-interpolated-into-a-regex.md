---
name: conf-value-interpolated-into-a-regex
description: a config value spliced into a regex must be VALIDATED as a plain path, not escaped — a quoted value matches nothing and a value with a pipe swallows a subtree, both silently
kind: class
---

# A conf value interpolated into a REGEX is validated, not escaped

## Symptom

A shell gate reads a key out of `.memory-tree.conf` with its own `sed` and splices the value into
an ERE — `FROZEN="^$MEMORY_ROOT/(builds|archive)/"`. Two legal spellings break it in opposite
directions and neither errors. `MEMORY_ROOT="docs/mem"` keeps its quotes, the pattern matches no
path, and every frozen record is scanned as live. `MEMORY_ROOT=docs|memory` makes `^docs` a
top-level alternation that swallows the whole `docs/` subtree, and the gate prints clean over a live
carrier. A vacuity arm that fires only at zero scanned cannot see a PARTIAL exclusion.

## Where it bit

`tools/check-agent-cap-restatement.sh`, found by round 2 of the `aDeclaredBound` cumulative review
and reproduced both ways in a scratch repo; the finding with both transcripts is under
`memory/builds/aDeclaredBound/reviews/`. It was the one reader in the repo that stripped nothing
where every sibling stripped quotes, comments and CR — `tools/memory-tree/check-memory-hygiene.sh`
SOURCES the conf, so bash does it for free.

## The fix

Refuse a value that is not a plain relative path before it reaches the pattern. Escaping is the
wrong tool: an escaped `"docs/mem"` still names a directory that does not exist, so the exclusion
still vanishes, only now without the quotes to show why. Validation makes the illegal spelling a
named refusal instead of a wrong population. And where the conf has a language, use it — sourcing
or one shared parser — rather than a private extraction (`two-readers-of-one-config-one-re-derived.md`
is the class one door over).

Gated by `tools/check-agent-cap-restatement.test.sh`'s arm that a `MEMORY_ROOT` which is not a plain
path is REFUSED with exit 2; the vacuity-at-zero limit is the general shape and has no gate of its
own.
