# Acceptance ledger — TOOL-aGraftedHelix-6

**Serves:** journal TOOL-aGraftedHelix-6

Node `a`, 2026-10-05. The build commit is `afad3628`, over the spec's rev-4 commit `3e454066`, which
recorded the pass's divergences before any code: the content key lives in `row_grammar.py`, its one
reader, and `derive_relation_base` gains a defaulted `check` argument. No merge bar and no self-test
suite ran in this pass. The direct check was the module's own `--selftest`, which went from 148 arms
to 160, all held. Each of the 12 new arms was observed RED: 15 breaks were staged one at a time in a
copy of the kit under the scratchpad, the tracked tree never edited, and every break redded new arms
only. The breaks: each of the key's six operations dropped in turn (link text, date, emphasis, case,
whitespace runs, the leading separator), identity keyed on path and id, landed keys reported, a key
counted landed when any holder landed, empty keys compared, a finding naming only two holders, an
empty population printing nothing, a missing base refusing, an explicit base refused as check 27's,
and a gotcha body that keeps its front matter. Every new arm went red under at least one of them.

Before the dispatch block was wired, the predicate ran over the real tree: 367 records, 268 rows
and 99 gotchas, 367 distinct keys, so no live duplicate and none landed. Its near misses were read
too: the shortest key is 148 characters, and no two keys share even their first 40.

**Evidences:** TOOL-aGraftedHelix-6
- AC1 — `check 28:` — the selftest's fixture of two gotchas apart only by case, a whitespace run, a date, a link target and emphasis printed `rc=1 check 28: 2 records hold one content key — memory/gotchas/crlf-a.md (crlf-a), memory/gotchas/crlf-b.md (crlf-b)`, one finding line. Dropping the link, date, emphasis, case or whitespace step each redded it, and so did keying the whole file rather than the body.
- AC2 — `python tools/memory-tree/row_grammar.py --selftest` — a row re-minted as `- **ARCH-tB-1** — **…**` beside its `- ARCH-tA-1 · …` original printed `rc=1 check 28: 2 records hold one content key — memory/DECISIONS.md:1 (ARCH-tA-1), memory/DECISIONS.md:2 (ARCH-tB-1)`. Dropping the emphasis step or the leading separator strip redded it.
- AC3 — `ROTATION_MODE=snapshot` — one id in the decision index and in `memory/archive/DECISIONS.2026-01-01.md`, with two distinct gotcha bodies, all added after the base, printed `rc=0 row-grammar: check 28 graded 4 record(s)` with `2 row(s), 2 gotcha(s)` and no finding. Keying identity on path and id redded it.
- AC4 — `python tools/memory-tree/row_grammar.py --selftest` — with the decision index deleted and no gotcha, the mode printed `rc=0 row-grammar: check 28 graded 0 record(s)`. A break returning before the summary on an empty population redded it.
- AC5 — `python tools/memory-tree/row_grammar.py --check-content` — at `afad3628` it exited 0 printing `graded 367 record(s) in cfa2cc45..HEAD — 268 row(s), 99 gotcha(s), 0 with an empty key, 0 key(s) held twice`, and `scan_records` over the same tree returned 367.
- AC6 — `memory/gotchas/two-answers-to-one-question.md` — in a `--local` clone under a short `%TEMP%` directory, a committed copy of it as `two-answers-copied.md` made the mode exit 1 printing `check 28: 2 records hold one content key — memory/gotchas/two-answers-copied.md (two-answers-copied), memory/gotchas/two-answers-to-one-question.md (two-answers-to-one-question)`. The clone was removed after.
- AC7 — `grep -n 'CONTENT_CHECK = 28' tools/memory-tree/row_grammar.py` — printed one line, `1365`; the hygiene engine grep for `check-content` printed one line, `2510`.
- AC8 — `28 checks` — `grep -c '^28\. ' memory/HYGIENE.md` printed 1, and the kit README's row for `check-memory-hygiene.sh` reads `28 checks`.
- AC9 — `tools/memory-tree/row_grammar.py` — its header's CHECK 28 section lists five NOT-checked items at lines 57 to 63: a PARAPHRASE, an ID HELD TWICE, a RECORD OUTSIDE THE TWO KINDS, FRONT MATTER and a duplicate whose EVERY HOLDER HAD LANDED at the base.
- AC10 — `row_grammar.py --check-content <base>` — two rows of one text committed at the fixture's base printed `rc=0` with `1 landed key(s) held twice and not reported`; a third row restating them under `ARCH-tL-3` then printed `rc=1 check 28: 3 records hold one content key` naming lines 1, 2 and 3. Reporting landed keys redded the first arm; counting a key landed when any holder landed, or naming two holders, redded the second.
- AC11 — `check 28:` — two rows whose texts are only a date printed no finding and `2 with an empty key`; two rows and a gotcha holding one text printed `rc=1 check 28: 3 records hold one content key` naming `memory/gotchas/three.md (three)` third. Comparing empty keys redded the first arm, and naming two holders the second.
- AC12 — `memory/guides/BUILD-METHOD.md` — `git diff 3e454066 afad3628` over it printed one hunk, `@@ -1 +1 @@`, changing `memory-tree@2.124` to `memory-tree@2.125` and nothing else.
