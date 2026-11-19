# TOOL-dTrackedAtlas-3 — the page carries the commit and input digest it was generated from, and `--check` reds a stale one

**Status:** CLOSED · rev-3 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · ratified 2026-11-19 · records-only · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-3-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-3-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-3-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-3-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold.md) | research | TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-3-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-3-spec-brief.md) | research | — |
| [2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-4 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

The Atlas page states the commit it was generated from and a digest of every tracked input it read,
and shows both. Given that page, the generator's `--check` answers whether the tree at a ref has
moved any of those inputs since, so a page the tree has moved past is detectably stale and the
regeneration of `TOOL-dTrackedAtlas-4` has an exit code to read.

## 2. Scope (IN)

- **S1** — `--out` embeds a `stamp` in the page's data: the commit the chain state was read at, the
  input path list of §4 "The input set", the SHA-256 of `git ls-tree -r -z` over that list at that
  commit, and the inputs that differ from it in the working tree. Observed by AC1, AC2 and AC3.
- **S2** — The template's header line shows the stamp's commit and digest, and the count of
  uncommitted inputs when there are any. Observed by AC8.
- **S3** — `--check --page <page> [--ref <rev>]` reads the stamp and exits by the table of §4 "The
  page check": 0 current, 1 stale, dirty, unstamped or absent, 2 when it cannot answer. A stale
  answer names the first-parent commits that moved an input. Observed by AC1, AC4, AC5, AC6 and
  AC7.
- **S4** — The input digest decides staleness, never the commit, as §7 F1 resolved. Observed by AC5
  and AC6.
- **S5** — `--check` with no `--page` and `--check --plant <case>` keep their current meaning and
  output. Observed by AC7.

## 3. Non-goals (OUT)

- The functions this unit touches are the generator's `main` and its module docstring, and it adds
  the constant `STAMP_SCHEMA` and six names: `StampError`, `read_git`, `derive_input_digest`,
  `build_stamp`, `read_stamp` and `check_page` (§4 "Inventory"). In the template it touches one statement, the
  one assigning the text of the `#derived` element. It edits no other function, no other data key
  and no view, so `derive`, `derive_actual`, `corpus` and the template's `footer` stay as
  `TOOL-dTrackedAtlas-2` leaves them.
- The derived data, its views and the chain state's rendering: `TOOL-dTrackedAtlas-2`'s.
- Regenerating the page, deciding when to, and the switch: `TOOL-dTrackedAtlas-4`'s.
- Reading `--ref` and `--claims` for a generation, and the `--check` that derives: those are
  `TOOL-dTrackedAtlas-2`'s. The stamp takes the `commit` of the state document that unit embeds.
- A wall-clock time in the stamp: two generations at one commit stay byte-identical.
- Any file under `tools/`, any new file under `memory/builds/dClosedLoop/build/`, and the page
  itself, which is never committed.
- A gate, a suite arm or a self-test: the generator is a build-folder instrument, checked by its
  fixture observations.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-1` — `GIT_TIMEOUT` bounds each git call, and the module's
  file is itself an input.
- **consumes-from** `TOOL-dTrackedAtlas-2` — the data's `state`, whose `commit` the stamp takes and
  whose builds name the chain folders it digests; `STATE_PATH`; the `--ref` option; and the
  generator and template as that unit leaves them. This unit builds after it and edits only what
  the first non-goal names.
- **hands-off** `TOOL-dTrackedAtlas-4` — deciding to regenerate; it may run the page check of §4 and
  read its exit code, and this unit regenerates nothing.

## 4. Design

### Where it lands

The generator is `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
and its template the `.html` beside it. Today `main` derives, and either prints one summary line
for `--check` or splices the data after the template's one `MARK` and writes `--out`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#main`). The data
already carries a `digest` key, a 12-hex hash of the records' sections
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@c39fd761ae807432455456b49f6d98724832db43:681`).
That key stays as it is and is not the stamp: it is a digest of what was read from the working
tree, and it cannot be recomputed at a ref without deriving the whole page.

`TOOL-dTrackedAtlas-2` gives `main` a `--ref` option, embeds the derivation's state document as
`data["state"]`, and reads dClosedLoop's records and the as-built view from the working tree while
the chain state is read at `--ref`; its §4 leaves to this unit any check that the two agree. The
stamp is that check: its `commit` is `data["state"]["commit"]`, and its `dirty` list compares the
working tree with that commit. `read_git` loads `TOOL-dTrackedAtlas-1`'s module from that unit's
`STATE_PATH` on first use, for `GIT_TIMEOUT` alone, so importing the generator still loads nothing.
The git helper may read `GIT_TIMEOUT` from the module at `STATE_PATH`, as `derive_actual` loads that
module today
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@a587c887a29c32753eccc707ddfef820a8dae0b1:721`),
and the constant is unit 1's
(`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@f24d90e258239b3b2d4acbf304393de200030557:64`).
That is a use of `TOOL-dTrackedAtlas-1`'s interface, not a second derivation: the bound has one
owning source.

### The input set

The stamp's `inputs`, sorted, each repo-relative with a directory ending in `/`:

| Input | Why |
|---|---|
| `memory/builds/dClosedLoop/README.md` | the corpus's first record |
| `memory/builds/dClosedLoop/build/` | the records, the as-built view, v2, the generator and the template |
| `memory/builds/dClosedLoop/reviews/` | the review records |
| `.memory-tree.conf` | the derivation reads its family prefixes, `MEMORY_ROOT` and `FORK_ITEM_CUTOFF`, and the generator `DESIGN_VIEW` and `DESIGN_BASELINE` |
| `TOOL-dTrackedAtlas-1`'s module file | the derivation itself |
| `memory/builds/<slug>/` | one per entry of `data["state"]["builds"]`, each the `slug` of a `[chain]` row |

The first three are written from the generator's `BUILD`, `REVIEWS` and `HERE` constants made
relative to `REPO`, not as literals. Measured at `9e21ac760` on 2026-11-19 (PINNED): 22 chain
builds, so 27 inputs, and `git ls-tree -r` over them lists 7459 entries.

### The stamp

Built by `build_stamp(data)` in `main`'s `--out` branch, after the data is derived and before the
splice, and stored as `data["stamp"]`:

| Field | Value |
|---|---|
| `schema` | `1` |
| `commit` | `data["state"]["commit"]`, the 40-hex commit `--ref` resolved to |
| `digest` | `derive_input_digest(commit, inputs)`: the 64-hex SHA-256 of the raw stdout of `git ls-tree -r -z <commit> -- <inputs>` |
| `inputs` | the input set above |
| `dirty` | sorted, the union of `git diff --name-only -z <commit> -- <inputs>` and `git ls-files --others --exclude-standard -z -- <inputs>` |

`-z` makes the digest independent of `core.quotePath`. `dirty` is judged over every input, the
chain folders read at the ref included, so a page generated at a ref the working tree has moved
past reads dirty; that over-reports a page whose chain folders alone moved, and never under-reports.
A failed or timed-out git call, or a `state` without a 40-hex `commit`, stops `--out` before
anything is written, with `atlas: cannot stamp the page: <reason>` and exit 1, the generator's
existing refusal convention.

### The rendering line

The template statement assigning the `#derived` element's text, at
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html@ebf0993447c72e1b2e03610a7fd88e106aa7a92e:2213`
before `TOOL-dTrackedAtlas-2`'s edit, gains at its end
` · generated from <first 12 hex of D.stamp.commit> · inputs <first 12 hex of D.stamp.digest>`,
followed by ` · <n> uncommitted input(s)` when `D.stamp.dirty` is not empty. It sets `textContent`,
so nothing is escaped by hand.

### The page check

```
python <generator> --check --page <page.html> [--ref <rev>]
```

`--ref` defaults to `HEAD` and is resolved in `REPO` by `git rev-parse --verify -q <rev>^{commit}`;
a value starting with `-` is refused. `--ref` is the option `TOOL-dTrackedAtlas-2` gives `main`,
meaning the ref in every form. The check reads the page file and git in `REPO`, writes nothing and
never calls `derive` or `derive_actual`. `--page` with `--plant`, `--out` or `--claims`, or without
`--check`, is a misuse.

| Exit | Meaning | Output |
|---|---|---|
| 0 | the inputs at the ref hash to the stamp's `digest` and `dirty` is empty | stdout `atlas: current — <page>: inputs <d12> at <rev> (<r12>) match the stamp of <c12>` |
| 1 | stale: the digests differ | stdout `atlas: stale — <page>: the inputs stamped at <c12> moved by <rev> (<r12>)`, then one `  <h12> <subject>` line per commit, at most 20, then `  and <n> more` |
| 1 | dirty: the stamp lists uncommitted inputs | stdout `atlas: dirty — <page>: generated with <n> uncommitted input(s), first <path>` |
| 1 | unstamped: no marker, data that does not parse, no `stamp`, or a field failing the table below | stdout `atlas: unstamped — <page>: <reason>` |
| 1 | absent: no file at the page path | stdout `atlas: absent — no page at <page>` |
| 2 | a misuse, a ref that does not resolve, or a git call that fails or times out | nothing on stdout; one `atlas: cannot check: <reason>` line on stderr |

The order is absent, unstamped, the ref and the digest at it, dirty, stale, current, so a dirty page
never reads current. The commits a stale answer names come from
`git log --first-parent --format=%H%x09%s <stamp commit>..<ref commit> -- <inputs>`, the landings
and direct commits on the ref's line. When `git cat-file -e <stamp commit>^{commit}` fails, the one
line under the stale answer reads `  the stamp's commit <c12> is not in this repository`, and the
answer is still stale.

`read_stamp` validates at this read boundary; a field outside its rule is unstamped, never current:

| Field | Rule |
|---|---|
| `schema` | the integer `1` |
| `commit` | 40 lowercase hex |
| `digest` | 64 lowercase hex |
| `inputs` | a non-empty list of strings, each matching `^[A-Za-z0-9._][A-Za-z0-9._/-]*$` with no `..` segment |
| `dirty` | a list of strings |

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `STAMP_SCHEMA` | constant | `1` |
| `StampError` | exception | a git call failed or timed out, or the ref does not resolve |
| `read_git(*args)` | function | the stdout bytes of `git <args>` run in `REPO` under the derivation's `GIT_TIMEOUT`; raises `StampError` naming the call |
| `derive_input_digest(commit, inputs)` | function | the 64-hex digest the stamp table defines |
| `build_stamp(data)` | function | the stamp dict, from the derived data's `state` and git |
| `read_stamp(page)` | function | `(stamp, None)`, or `(None, reason)` for an unstamped page |
| `check_page(page, ref)` | function | prints the answer and returns the exit code of the table |

### What it does not check

- Run claims under `refs/gov/remote/runs/`: they are refs, not tree content, so a page's claim
  readings can be older than a current answer says.
- The code under `tools/` the derivation reuses, `tree_lib.py`, `deviations.py`,
  `gen_build_index.py`, `breakpoints.py` and the unattended driver among it, and `.unattended.conf`:
  a change there can move derived state without moving the digest.
- A working-tree read outside the input set: `tools/memory-tree/design_lib.py`, through which
  `TOOL-dTrackedAtlas-2` reads the as-built view, is code under `tools/` like the bullet above.
- A hand edit to the page after generation, including one narrowing the stamp's `inputs` to paths
  that did not move.

### Files touched (estimate)

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md`

### Alternatives rejected

- The commit deciding staleness, and a whole-tree digest: §7 F1.
- Refusing `--out` over uncommitted inputs: §7 F2.
- The generator's exact read set as the input set, rather than whole folders. Measured on 2026-11-19
  (PINNED): of the 92 first-parent commits from `b5f83a21d` to `9e21ac760`, 10 touched dClosedLoop's
  folders, and all 10 touched only the as-built view, which the generator skipped then and
  `TOOL-dTrackedAtlas-2` reads. An exact read set is a second list beside the generator's reads that
  every new read must update, and the folder form costs no false red in that history.
- A second `<script>` element for the stamp: the data's one marker already carries it, and the page
  check parses one JSON either way.

## 5. Acceptance criteria

The commands run in a scratch clone of this repository at the run branch's tip carrying this unit,
at `%TEMP%/ta3fx`, from the clone's root, with these names set. Pages are written to the run's
scratch directory, never into the clone or the worktree. Every generation passes `--claims none`,
so no claim is read.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
TPL=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html
S=<the run's scratch directory>
```

- **AC1** — When `"$PY" "$ATLAS" --claims none --out "$S/p0.html"` runs and then
  `"$PY" "$ATLAS" --check --page "$S/p0.html"` runs, the check exits 0 with one stdout line beginning
  `atlas: current`, and the page's `stamp.commit` equals `git rev-parse HEAD` with `stamp.dirty`
  empty.
  Red when: `--out` embeds no stamp, which the same check reads as `atlas: unstamped` with exit 1.
  cost: one generation of the page, minutes rather than seconds.
- **AC2** — When the stamp's `inputs` are read from `$S/p0.html`, they are the five fixed inputs of
  §4 "The input set" and one `memory/builds/<slug>/` per chain build, and
  `git ls-tree -r -z HEAD -- <those inputs> | sha256sum` prints the stamp's `digest`.
  Red when: the digest hashes another byte stream, for instance the output without `-z`, which
  `sha256sum` then disagrees with.
  figure: 27 inputs, DERIVED as 5 plus the builds of the page's `state`; 22 builds at `9e21ac760`.
- **AC3** — When a line is appended to the clone's `memory/builds/dClosedLoop/README.md` and left
  uncommitted, `"$PY" "$ATLAS" --claims none --out "$S/p2.html"` gives a `stamp.dirty` of exactly
  that path and the `digest` AC2's command prints at `HEAD`, and `--check --page "$S/p2.html"` exits
  1 with `atlas: dirty`; the line is then restored with
  `git checkout -- memory/builds/dClosedLoop/README.md`. And with `R` the parent of the last commit
  that changed the generator, `R=$(git log -1 --format=%H -- "$ATLAS")^`, a generation with
  `--ref "$R"` into `$S/p3.html` stamps `git rev-parse "$R"` as its `commit` and lists the
  generator in `dirty`, since the working tree's generator is not the one at `R`.
  Red when: the stamp reads the commit alone, which leaves `dirty` empty and answers
  `atlas: current` for both pages.
  cost: two generations of the page.
- **AC4** — When a page lacking a stamp is checked, it never passes: `--check --page "$TPL"`, whose
  data is `{}`, exits 1 with `atlas: unstamped`; so do `$S/p0.html` with its `stamp` key deleted by a
  `"$PY"` one-liner into `$S/p0-bare.html`, and with `stamp.inputs` set to `["../x"]` into
  `$S/p0-bad.html`, the latter's reason naming `inputs`; and `--check --page "$S/none.html"` exits 1
  with `atlas: absent`.
  Red when: any of the four exits 0.
- **AC5** — When the clone commits a change to `memory/builds/dTrackedAtlas/README.md`, a path
  outside the inputs, `--check --page "$S/p0.html"` still exits 0 with `atlas: current`, naming the
  new `HEAD` beside the stamp's older commit.
  Red when: the commit decides staleness, §7 F1's candidate (a), which reads this commit as a move.
- **AC6** — When a branch from the clone's `HEAD` appends a line to
  `memory/builds/dWitnessedBar/RUN.md`, commits it, and is merged back with `git merge --no-ff`, then
  `--check --page "$S/p0.html"` exits 1 with `atlas: stale`, and a following line begins with the
  merge's first 12 hex; `--check --page "$S/p0.html" --ref HEAD^1` exits 0, so the red is the
  merge's; and `"$PY" "$ATLAS" --claims none --out "$S/p1.html"` at the merge then checks with exit 0.
  Red when: the old page passes after the merge.
  fixture: the clone is planted by the pass and removed after; the real repository's refs are never
  written.
  cost: one generation of the page.
- **AC7** — When `--check --page "$S/p0.html" --ref no-such-ref` runs, it exits 2 with nothing on
  stdout and one stderr line beginning `atlas: cannot check:`, and `--check --page "$S/p0.html"`
  with `--plant view-unread` exits 2 the same way; `--check --claims none` with no `--page` still
  prints its one `atlas: derived —` line with exit 0, and with `--plant view-unread` added still
  exits 1 with its refusal.
  Red when: an unresolvable ref exits 1, which a caller reads as stale and regenerates on.
- **AC8** — When `grep -n "D.stamp.commit" "$S/p0.html"` runs, one line it prints is the statement
  assigning the `#derived` element's text; and `$S/p0.html`, served by `python -m http.server` from
  a temporary launch configuration of the session that is deleted afterwards, shows
  `generated from` and the first 12 hex of `HEAD` in its header line.
  Red when: the template's statement is unedited, where the same `grep` prints nothing.
  cost: a browser pane look at a page of about 16 MB (DERIVED from the page size
  `TOOL-dTrackedAtlas-2` measured).

## 6. Gates

The close runs the plain bar once. The legs below are those the files touched keep green, the last
two owed because `tools/gate-legs.json` guards `memory/builds/dClosedLoop/build/` with them. No
suite arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

- **FACT-QUESTION · F1 — Does the commit or the input digest decide that a page is stale?** Probe:
  over the first-parent history of `9e21ac760` since the page's last write on 2026-11-03, count the
  commits, and the commits touching the input set of §4, with
  `git rev-list --first-parent --since=2026-11-03T23:25 9e21ac760 [-- <inputs>]`. Deciding
  observation: the number of commits that move the commit and touch no input, each a red the commit
  rule gives and the digest rule does not. Liveness: the probe reads a negative when every commit
  touches an input, and the two rules then agree on every commit.
  Measured on 2026-11-19 (PINNED): 92 commits, the oldest `b5f83a21d`, of which 22 touch an input
  and 70 touch none. The owner's own measurement agrees with the digest: regenerated at `9e21ac760`,
  the page was byte-identical to the 2026-11-03 page, and none of the 92 touched a file the
  generator then read.
  (a) The commit decides: stale when the stamp's commit is not the ref's. Rejected: 70 false reds in
  92, and `TOOL-dTrackedAtlas-4` would regenerate on each.
  (b) The input digest at the ref decides. 22 reds in 92, each a commit that moved an input.
  (c) `git log <stamp>..<ref> -- <inputs>` being non-empty decides. It agreed with (b) on all 22,
  whose input digests are 22 distinct values, so the history holds no revert pair to separate them.
  Rejected as the decider because it needs the stamp's commit in the checking repository:
  `git rev-list` over a range from an absent commit fails, while (b) answers from content alone. It
  is kept as the report of which commits moved.
  (d) The whole-tree fingerprint of `tools/run-gates/gate-fingerprint.sh`. Rejected: it hashes the
  whole tree, so it moves on all 92, as (a) does.
  RESOLVED (agent, 2026-11-19, delegated): (b), the observation above.
- **F2 — What does `--out` do when an input differs from `HEAD` in the working tree?**
  (a) Stamp the differing inputs as `dirty`, write the page, and let the page check red it. A
  preview of uncommitted records keeps working, and such a page never reads current.
  (b) Refuse to write the page. The stamp then never lies, but regenerate-and-look over uncommitted
  records, the procedure of the dClosedLoop atlas-instruments record, stops working.
  (c) Ignore the working tree. Rejected: the page then claims a commit whose inputs it does not
  match, which is the defect this unit exists to remove.
  (a) satisfies every criterion (b) does and keeps the preview; it trips none of M3's vetoes, since
  it adds no write path and changes no governance carrier.
  RESOLVED (agent, 2026-11-19, delegated): (a), the most feature-rich option by M3's rule.

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft.
- rev-2 · 2026-11-19 · §5 · the pass legs' reds after `390c2bc05`, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer: AC8's page-size figure is pinned on its
  line. No design change.
- rev-3 · 2026-11-19 · §3 · §4 · the lexicon's verb pin, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-3-name-fold: `git`, `input_digest` and `stamp_page` are
  renamed `read_git`, `derive_input_digest` and `build_stamp`, each leading with a declared verb, and
  §4 "Where it lands" states that the git helper reads unit 1's `GIT_TIMEOUT` through `STATE_PATH`.
  No design change.

## 9. Reuse audit

The seam extended is the generator's own `main`, its `--out` splice after `MARK` and its `--check`
flag, with `TOOL-dTrackedAtlas-1`'s `read_chain` and `GIT_TIMEOUT` for the chain builds and the git
bound. `python tools/codebase-map/reuse_lookup.py "stamp a generated artifact with the commit and input digest and report it stale when the inputs moved"`
ranked name-stem helpers and three readings worth a look, none taken.
`tools/run-gates/gate-fingerprint.sh` digests the whole tree, which is §7 F1's rejected (d).
`tools/memory-tree/asbuilt_view.py#read_view_inputs` reads one view's inputs at its pinned baseline,
not a path set at any ref. `check_generated_output` in `tools/unattended/lib-unattended.sh` only
asks whether a path is a generated index's output, and the codebase map's freshness test compares a
committed artifact with a re-render, while this page is never committed. The recall probe returned `TOOL-dTotalRecall-26`, a different atlas under `help/atlas/`
whose committed pages a byte comparison checks, unbuilt; and the dClosedLoop researcher prompt that
asked how an atlas is kept current, which named a stale-output leg for a committed page.

Recall terms used: `python tools/memory-recall/query.py "how does a generated page record what it was generated from and know when it is stale" --terms "atlas stamp generation commit input digest stale check fingerprint regenerate landing dClosedLoop page"`
