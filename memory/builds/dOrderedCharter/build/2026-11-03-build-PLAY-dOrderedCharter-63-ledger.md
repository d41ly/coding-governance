# PLAY-dOrderedCharter-63 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-63

Each line is a probe this pass ran with the pass applied: the checker run in a scratch repo built by
a copy of the suite's own `scratch` and the three new arms' lines, extracted from the suite file
(the suite itself was not run), or a `python -c` over the checker loaded by path. The spec-tokens
self-test, the merge bar and each `New arm:` line's RED-first observation are the main loop's at the
close: a role agent runs none of them.

**Evidences:** PLAY-dOrderedCharter-63
- AC1 — `deferred-fenced` — `python tools/check-spec-tokens.py` exit 0, `spec-tokens: 1 live spec(s) · 1 terminal spec(s) not graded`, no line naming `nope.sh`. The same plant under the checker before the change (`LIVE.search`) exit 1 with `2 live spec(s)`. OWED to the main loop: the arm's RED-first observation
- AC2 — `fence-above-header` — `python tools/check-spec-tokens.py` exit 0, `1 live spec(s) · 1 terminal spec(s) not graded`, no line naming `nope.sh`. A `python -c` over the plant's second spec: the first status line of the whole text (option A) reads live, `check_live_header` reads not live. OWED to the main loop: the arm's RED-first observation
- AC3 — `live-fenced-closed` — `python tools/check-spec-tokens.py` exit 1, `not tracked by git ls-files` for `nope.sh`, `spec-tokens: 1 live spec(s) · 0 terminal spec(s) not graded`. A `python -c` over the plant's spec: a read taking its last status line, the fenced CLOSED one, reads not live; `check_live_header` reads live. OWED to the main loop: the arm's RED-first observation
- AC4 — `grep -n 'check_live_header\|LIVE.search' tools/check-spec-tokens.py` printed four lines, the docstring (`:157`), the comment above `LIVE` (`:358`), the definition (`:1197`) and the call in `main` (`:1514`), and no `LIVE.search`; `grep -c 'check_live_header' memory/map/generated/symbols.json` printed 1 after `gen_map.py --write`.
- AC5 — the §4 measure probe — printed `2823 ['memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-12.md']`: one flip, TOOL-dIndexedDesign-12, over 2823 tracked specs at the pass tip (2822 at `4e14dd8ab`; the one spec added since is this unit's own).
