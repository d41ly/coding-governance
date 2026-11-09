# PLAY-dOrderedCharter-8 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-8

Each line is a probe this pass ran at rev-3 of the spec, with the pass applied. No leg, suite or `--selftest`
ran in the pass: the card engine was run by hand over a scratch repository under the short temp path with one
linked worktree, the scratch guard's `renderRouteContext` and the handoff's `render` verb were called directly,
the two envelope canonicals were compared byte for byte, and the three new plants of `instruction_units.py
fixture` were run alone through `run_fixture`. The live compaction fixture was not run: launching the harness
is the main loop's. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-8
- AC1 — `card-compaction.fixture.sh` — over a stub `claude` placed first on PATH, never the harness: a stub answering from the primary tree's card exited 1 naming limb A and the `P-` nonce, one answering from the worktree's exited 0 naming the `W-` nonce, one printing `no` for session B exited 1 naming limb B; with no argument, a non-empty dir, or no `claude` on PATH it exited 2. The live run, two headless sessions and a compaction, is owed to the main loop, and the card import stays dark until it is green.
- AC2 — `cwd` — `--card --write` run from the scratch primary tree with a SessionStart JSON whose `cwd` was the worktree, its backslashes JSON-escaped: exit 0; the worktree's `.claude/orientation-card.md` equalled, by `cmp`, the opener, the stored card's bytes and the closer; the primary tree held no such file; the verb's stdout still equalled the stored card.
- AC3 — `--card --replay` — after a second write, a replay with the payload and `--card --append --session s1` run in the worktree each left the file equal to the envelope around the stored card's new bytes, the appended line included; with the file's path made a directory, write, replay and append each exited 0 and printed one `card-file — skipped:` line.
- AC4 — `git status --porcelain` — printed nothing in either tree after the write, and the clone's `info/exclude` carried `/.claude/orientation-card.md` once after two writes; with a tracked file planted at the path, two writes printed `card-file — skipped:` naming it as not ignored, left the tracked bytes alone and kept the exclude line at one.
- AC8 — `ROUTE_CONTEXT_CAP` — `renderRouteContext` over a scratch tree with a conf and no routed card printed the bare one-line text; with a card file planted, the same text between the file's first and last lines, byte-identical by `cmp`; over a 400-unit route with the file, 9997 characters, its first and last lines the envelope.
- AC9 — `## Card` — `handoff.py render --role gov-builder --build dOrderedCharter --card <card> --stdout` with the card file in the tree printed one `## Card` block inside the `## Task` part, after the level-0 practices block's closer and before the level-6 task opener, holding the card file's envelope lines around the route; `check_envelope_order` read the task part's levels as `0 1 6` with no finding; with the file removed the output equalled, by `cmp`, the render made before any card file existed.
- AC10 — `envelope_sh` — `bash envelope.sh .claude/orientation-card.md 1 "<direction>"` and `render_envelope` in `envelope.py` gave equal bytes around an empty body and around a body lacking its final newline; the parity extractor found the block in `manifest-check.sh` equal to the canonical, and a planted change to the copied opener's format made the two differ; `git grep` found no `render_envelope` block in `manifest-check.sh`; the new cross-language part of the parity suite, run alone over a planted `envelope.sh`, named both bodies.
- AC11 — `doc.orientation-card` — plant `card-absent`: the gate exited 0 with the row and no file, `--list` counted it at zero files without a red, and an `untracked` that is no boolean refused the registry with exit 2; plant `card-level`: a planted card file whose opener names level 2 exited 1 naming the path, the same file at level 1 exited 0 with three documents covered; plant `card-tracked`: the file force-added to the index exited 1 naming it as tracked.

**Owed to the close.** The live AC1 run on a node with `claude`; the bar; `python tools/playbook/gov_tag.py check`,
which the role gate refused this pass; the envelope gate over gov's own tree with and without a card file; and
the RED-first observation of each `New arm:` line: the card-file arms of `skills/session-kickoff/manifest-check.test.sh`
staged by writing to `$ROOT`, the S-AC8 arms of `tools/hooks/scratch-guard.test.sh` staged by dropping the close
line, the `envelope_sh` parity row and its cross-language part of `tools/lib/resolve-python.test.sh` staged by a
one-character change to the inline copy, and the three card plants of `instruction_units.py fixture` staged by a
level-2 opener. `AGENTS.md` measures 23279 bytes against its 23161-byte size row, a warning under the warn posture.
