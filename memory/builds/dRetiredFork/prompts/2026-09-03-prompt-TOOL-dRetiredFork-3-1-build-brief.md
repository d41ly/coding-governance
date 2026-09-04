# Build brief — TOOL-dRetiredFork-3

**Serves:** journal TOOL-dRetiredFork-3

## What the unit is

`parse_front_matter` raises `Problem` for BOTH "line 1 is not `---`" (the header is ABSENT) and
every malformed case after it (the header is PRESENT and corrupt). Those are different animals, and
gov collapses them: a corrupted header silently becomes a missing one and the index regenerates
around it. NicoCares carries the distinction as `nc carve-out 9/20`.

## What this pass does

1. S1/S2 — `StaleHeader`, raised by the parser for a header that OPENED at line 1 and then failed;
   the line-1 check keeps raising plain `Problem`, because that one really is absent. Handled at
   `collect()`, which reports the file and the offending region.
2. S3 — a shrink-only registry at `memory/project/stale-header-waiver.txt`, consulted at
   `collect()` and NOT inside the parser. The parser decides CONFORMANCE, the caller decides
   TOLERANCE — nc's own comment argues for that seam and is right, because this parser has two
   readers who want different answers.
3. S4 — the file ships with its header and NO rows, plus a `[[hole]]` in the memory-tree `kit.toml`
   whose discharge probe reports it UNARMED rather than passing silently. A waiver list measured on
   gov's corpus is vacuous in any other tree.
4. S6 — `F:stale-header-waiver.txt` joins check 3's whitelist IN THE SAME COMMIT. That whitelist is
   a hardcoded `case` naming nine registries and its population is `git ls-files`, so a new tracked
   file under `memory/project/` reds this unit's own named gate on landing.
5. S7 — bump `KIT_MEMORY_TREE_VERSION` and all SEVEN paired markers.

## Ratified forks, folded

F1 — the registry keys on the build README PATH, matching every sibling registry and gradeable
against `git ls-files`.
F2 — an empty registry prints `0 tolerated` UNCONDITIONALLY, because a clean run printing nothing is
indistinguishable from a check that never ran. AC5 is written around that line existing.

## One refinement worth stating

§4 says `StaleHeader(Exception)`. It subclasses `Problem`, which IS an Exception, so the spec holds
— and an unhandled one then reports as a named failure rather than a traceback, which is this
file's blind-spot-3 rule.

## Acceptance

AC1-AC8, run rather than asserted, with each arm's RED observed before it is wired.
