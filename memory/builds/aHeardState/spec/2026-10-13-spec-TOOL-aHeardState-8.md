# TOOL-aHeardState-8 — the closing review's mediums and lows: fixtures that can see the defects, and three small fixes

**Status:** SPECCED · rev-1 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 confirmed 18 MEDIUM and LOW findings. Ids 2 and 25 close in
`TOOL-aHeardState-5` and id 12 in `TOOL-aHeardState-7`. This unit closes the rest, as the batch M4 and
the unattended verbs require: three fixes in the code, and fixtures that make each named red condition
observable.

## 2. Scope (IN)

- **S1** — the fence (M3, id 16): in `tools/hooks/format-guard.js` and `tools/runlog/prose.py`, a line
  opens or closes a fence only when its backtick or tilde run is not closed again on the same line, so
  an inline triple-backtick span leaves the fence state alone. Observed by AC1.
- **S2** — the witness (M4 id 17, L6 id 23): an unreadable git dir or HEAD writes a witness instead of
  silently skipping the commit check, and witnesses accumulate, one line each, never overwrite.
  Observed by AC2.
- **S3** — wording (L2 id 13, L3 id 7): the suite header says the harness half of the live witness is
  the owner's; the block reason says LIVE.md lists the build as not yet terminal, and that a committed
  or merged line names a commit. Observed by AC3.
- **S4** — UTF-8 (L4, id 6): `read_charter_shapes` in `prose.py` also catches `UnicodeDecodeError`, so
  an unreadable charter prints `pair — unknown`. Observed by AC4.
- **S5** — hook fixtures (M5 id 18, M6 id 19, M7 id 20, L5 id 22), new arms in
  `tools/hooks/format-guard.test.sh`: a linked worktree as the payload cwd, a payload without
  `last_assistant_message`, a route unit with no spec, and a sidecar sha that is not an ancestor of
  HEAD. Observed by AC5.
- **S6** — prose fixtures (M2 ids 11 and 26, M8 id 15, L7 id 24, M9 id 21): the runlog arms read a
  withheld fixture charter, `tools/runlog/fixtures/prose-charter.md`, instead of the live AGENTS.md; the
  mixed scenario gains one message id carrying two text blocks and one `isSidechain` record; the AC5
  arm asserts the full projects path. Observed by AC6.

## 3. Non-goals (OUT)

- The left-shift lints the review proposes beside each item; each is a gate of its own build.

### Edges

- **consumes-from** `TOOL-aHeardState-7` — the header paragraph this unit's suite-header wording sits
  beside, so the two edits to `format-guard.js` land in sequence.

## 4. Design

The fence rule, in both readers: a line whose leading run of three or more backticks or tildes appears
again later on the same line is an inline span, not a fence. The fixture charter is a byte copy of the
microformats fence block only, so the pinned pair figures stop depending on the live charter.

### Files touched (estimate)

- `tools/hooks/format-guard.js`
- `tools/hooks/format-guard.test.sh`
- `tools/runlog/prose.py`
- `tools/runlog/selftest.py`
- `tools/runlog/kit.toml`
- `tools/runlog/fixtures/prose.json`
- `tools/runlog/fixtures/prose-charter.md`

## 5. Acceptance criteria

- **AC1** — When a message carrying "```npm test``` passed" above a correct bare pair is piped to
  `format-guard.js`, and the same text goes through `prose.check_pair`, both allow. Red when: the
  inline span opens a fence and the pair reads fenced.
- **AC2** — When the fixture worktree's HEAD file names a ref that does not exist, the hook allows and
  stderr carries a line naming the unreadable HEAD in `format-guard.js`'s witness wording. Red when: the
  commit check is skipped with nothing on stderr.
- **AC3** — When the block reason is printed by `format-guard.js`, it says "not yet terminal" and
  "committed or merged". Red when: it still says "in progress" or names only committed lines.
- **AC4** — When `runlog.py prose --charter` names a UTF-16 file, it exits 0 and the pair line reads
  `unknown`. Red when: a `UnicodeDecodeError` escapes as a traceback.
- **AC5** — When the four new hook fixtures run, the linked worktree's sidecar lands under
  `.git/worktrees/<name>/format-guard/`, the missing message allows with a witness, the spec-less route
  allows a lone BUILD line that the spec'd route blocks, and the reset HEAD allows with
  `along no first-parent path`. Red when: any of the four reads as the other branch.
- **AC6** — When `runlog.py prose` reads the extended mixed scenario against `prose-charter.md`, its
  pinned figures move by exactly what the two-block message and the sidechain record contribute when
  counted correctly, and the AC5 arm's stderr holds the full projects path. Red when: the two blocks
  count twice, the sidechain record counts, or a basename-only match passes.
  figure: PINNED in the runlog selftest.

## 6. Gates

`format-guard self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1's 18 minors.
