# PLAY-dOrderedCharter-46 — the overlay's landed revision defined, its unborn-HEAD outcome stated, and a write door rendering the rows it just wrote

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 32 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-46-deviation-461.md](../build/2026-10-24-build-PLAY-dOrderedCharter-46-deviation-461.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 80 at HIGH**, its item **H7**. `PLAY-dOrderedCharter-32` S1 has `read_overlay` read
`.governance/instructions.toml` "at the landed revision, never the working tree", and never defines the
term, nor says what happens with no commit at all, nor how a write followed by a render in one command
sees the row it wrote. Unit 15's write verb writes a row and re-renders in the same command, so it
renders the old overlay and the render gate reds after the commit; unit 37's tutorial adds a rule and
renders in an empty repository; unit 31's `update` step writes adopter rules into the overlay and the
render drops them until a commit and a second render. This unit defines the revision, gives the
unborn HEAD a named outcome, and gives the write doors one explicit candidate read that every check
refuses. It repairs unit 32 and is built right after it.

## 2. Scope (IN)

- **S1** — The landed revision is the commit `HEAD` names: `read_overlay(root)` reads the blob
  `HEAD:.governance/instructions.toml` through `git cat-file`, never the index and never the working
  tree. A path absent from that commit is the empty overlay unit 32 S1 states, silently, because a
  repository with no rules is ordinary. This supersedes unit 32 S1's undefined "landed revision".
  Observed by AC1.
- **S2** — The unborn HEAD. Where `git rev-parse --verify -q HEAD` names no commit, `read_overlay`
  returns the empty overlay with its state `unarmed`, and every caller that renders prints one line,
  `overlay — unarmed: no commit yet, so there is no landed revision to read`, never a silent empty.
  Observed by AC2.
- **S3** — The candidate read. `read_overlay(root, candidate=<text>)` parses the given text in place
  of the landed blob, through the same parse and refusals, and returns the state `candidate`. The
  renderer takes it as `--overlay-from <file>` on a render verb, which writes, and refuses it on every
  check verb (`--check`, `--check-render`), so no gate grades a tree against bytes that have not
  landed. Observed by AC3 and AC4.
- **S4** — The doors use it. Unit 15's write verbs, which validate the would-be tree before they write
  (its S2), re-render with `--overlay-from` naming the overlay file they just wrote, so the render
  shows the new row in the same command; a later commit lands exactly those bytes and the render gate,
  reading `HEAD`, agrees. This supersedes unit 15 S2's "re-renders the targets unit 20's renderer
  assigns" for the overlay's source. Observed by AC4.
- **S5** — The plants, through unit 32's fixture (`python tools/playbook/overlay.py --fixture --plant
  <case>`): `unborn-head`, `staged-not-landed` (a row staged and not committed), `write-then-render`
  and `check-refuses-candidate`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- The overlay's grammar, its `repo.` units, its policy rows and its composition: units 32, 34 and 35.
- The write command's guard and proof: unit 15's.
- Reading a revision other than `HEAD` (a `--rev` option): no caller needs one.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-32` — `read_overlay`, its parse and its fixture, which S1 to S3 define the revision of and S5 extends; without them there is no reader to pin
- **consumes-from** `PLAY-dOrderedCharter-15` — the write verbs and their re-render, which S4 points at the candidate
- **hands-off** `PLAY-dOrderedCharter-31` — its adopter-rules step re-renders with the candidate read over the overlay it has just written, so update keeps the rules in the charter before any commit
- **hands-off** `PLAY-dOrderedCharter-37` — its tutorial commits the overlay before a standalone render, or renders through a write door, and expects the unarmed line in a repository with no commit

## 4. Design

### Evidence

Read at `ce13efbe`; the seams are designs, not yet code. Unit 32 S1 reads "at the landed revision,
never the working tree, as every composer does" and §4 Migration "until then `read_overlay` returns an
empty overlay". The phrase comes from dGroundRules' reader clause, `cl-dClosedLoop-0008`, quoted in
architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1765`):
"read at the landed revision, never from the working tree"; dGroundRules has no spec yet
(`memory/builds/dGroundRules/` holds no `spec/` folder). Unit 15 S2 writes the row, its change record
and "re-renders the targets unit 20's renderer assigns" in one command. Unit 37 S6's tutorial is
"install gov into an empty repository, add a repository rule, render".

### Data model

```python
@dataclass(frozen=True)
class Overlay:
    units: tuple          # unit 32's rows
    policies: tuple
    state: str            # "landed" | "absent" | "unarmed" | "candidate"

def read_overlay(root, candidate: str | None = None) -> Overlay: ...
```

### Why HEAD and not the index

The index holds what is staged, which is neither reviewed nor landed, and a node that stages a row and
renders would publish a rule that a reset discards. `HEAD` is the last commit a check can grade and a
lander can push. dGroundRules' reader, which unit 32 mirrors, names the same revision for the policy
file; when that reader lands, the two read one revision.

### Inventory

Minted: the `Overlay.state` values `landed`, `absent`, `unarmed` and `candidate`; the keyword
`candidate`; the renderer flag `--overlay-from`; the line prefix `overlay — unarmed:`; four plant names.
Naming cells: `lexicon naming predicates` grades the Python names.

### Files touched (estimate)

- `tools/playbook/overlay.py`
- `tools/playbook/render_playbook.py`
- `tools/playbook/instructions_edit.py`
- `help/overlay.md`

### Rollout

Live at landing, order 32, after unit 32 at order 31. Unit 33 shares order 32 and also writes
`tools/playbook/render_playbook.py` and `help/overlay.md`, so the two write sets intersect and the
dispatch sequences them rather than running them together (M6).

### Alternatives rejected

- **The index as the landed revision**, the review's other reading: staged bytes are not landed.
- **A `--from-worktree` read on every verb**, the review's other door: it lets any caller render from
  unlanded bytes; S3 admits the candidate only on a write and refuses it on every check.
- **Committing inside the write verb.** A command that commits takes the commit away from the session
  that owns it.

## 5. Production-readiness checklist

- security: the candidate read widens what a render may read to a file the caller names, on a write
  verb only; every check verb refuses it, so a render from unlanded bytes cannot pass a gate. Stated
  as a widening in §8 F3.
- perf / scale: one `git cat-file` per read instead of one file read.
- error / empty / loading states: S1's absent and S2's unarmed are distinct states; a parse failure of
  the landed or the candidate text refuses as unit 32 does, naming the source.
- observability: S2's line; a render from a candidate says `overlay — candidate: <path>`.
- risks: a render from a candidate that is never committed leaves a rendered file the next check reds,
  which is the gate doing its job.
- testing: AC1 to AC4 by fixture.
- migration: none.
- user docs: `help/overlay.md` (unit 32's) gains one paragraph on which revision is read.

## 6. Acceptance criteria

- **AC1** — When `python overlay.py --fixture --plant staged-not-landed` runs, a row
  added and staged but not committed is absent from `read_overlay`, and present once committed.
  Red when: the reader reads the index or the working tree.
- **AC2** — When `--plant unborn-head` runs in a fixture repository with no commit, `read_overlay`
  returns state `unarmed`, and a render prints the `overlay — unarmed:` line once and exits 0.
  Red when: the reader raises, or returns an empty overlay with nothing printed.
- **AC3** — When `--plant check-refuses-candidate` runs `render_playbook.py --check-render
  --overlay-from <file>`, it exits 2 naming the flag; a render verb with the same flag exits 0.
  Red when: a check grades a candidate.
- **AC4** — When `--plant write-then-render` runs a write verb of `instructions_edit.py` with its
  guard stubbed open in the fixture, the rendered target holds the new row in the same command, and
  after the fixture commits the overlay, `--check-render` over that target exits 0.
  Red when: the render shows the old overlay, or the post-commit check reds.
  fixture: the write guard of unit 15 S4 is stubbed in the scratch tree only, as unit 15's own fixture
  stubs it.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 AC4 · the playbook-render selftest runs the four overlay plants, each failing case staged by a working-tree read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 32's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Which revision is landed.** Options: (a) `HEAD`; (b) the index; (c) the working tree with a
  flag. (b) and (c) admit unreviewed bytes. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, the
  reader clause unit 32 mirrors says "never from the working tree", and only `HEAD` is landed.
  widens: none · relaxes: none
- **F3 — How a write door renders its own row.** Options: (a) a candidate read admitted on render
  verbs and refused on checks; (b) commit inside the verb; (c) leave the render stale until a second
  command. (b) takes the commit from the session and (c) is the defect. RESOLVED (agent, 2026-10-24,
  delegated): (a), rung 3. widens: the renderer may read a caller-named overlay file on a render verb
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 80 (HIGH, item H7).

## 10. Reuse audit

The seam extended is unit 32's `read_overlay` in `tools/playbook/overlay.py` (its S1), whose revision
this unit defines rather than adds a second reader beside. `python tools/codebase-map/reuse_lookup.py
"read a tracked file at the last commit rather than the working tree"` ranked `read`, `read_text`
(`tools/memory-tree/tree_lib.py`) and `tree` by name stem, none a revision reader; the tree's committed-blob reader is `tree_lib.read_blobs_at` (`tools/memory-tree/tree_lib.py:328`),
which unit 19 already uses, and S1's one-path read is the same `git cat-file` call. The recall query
returned the review's own H7 text and unit 32's S1, and TOOL-dTrueNorth-16's "one revision reader",
which agrees that a reader of record names its revision once.

Recall terms used: `python tools/memory-recall/query.py "what revision does a policy or overlay reader read and what about an unborn HEAD" --terms "landed revision working tree read_policy_key unborn HEAD overlay reader git show candidate"`
