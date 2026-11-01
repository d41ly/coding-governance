# TOOL-dEasedEffort-2 — the ledger's AC1 and AC3 lines record their observations at a named commit, and the class names the form

**Status:** SPECCED · rev-1 · 2026-11-02 · node d · Tier-1 · base 2a6f3975 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dEasedEffort-2-round1-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dEasedEffort-2-round1-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 confirmed two lows, L1 and L2, both in `TOOL-dEasedEffort-1`'s acceptance
ledger. The record is
`memory/builds/dEasedEffort/reviews/2026-11-02-review-TOOL-dEasedEffort-1-closing-diff-review-round1.md`.
This unit makes the ledger's AC1 and AC3 lines each record an observation of the form their criterion
names, and writes the form they exposed into the class those two defects belong to. It is the one
batched unit M4 of `memory/guides/BUILD-METHOD.md` owes for them, and the brief is
`memory/builds/dEasedEffort/prompts/2026-11-02-prompt-TOOL-dEasedEffort-2-round1-fix-brief.md`.

## 2. Scope (IN)

"The ledger" is
`memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md`, and
"the class" is `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. The ledger's
AC1 and AC3 lines answer `TOOL-dEasedEffort-1`'s criteria. Every "Observed by" below names this
spec's own criteria.

- **S1** — L1. The ledger's AC3 line stops claiming a command printed on a commit it could not have
  run at, and records the spec's `HEAD` form observed at `e74ef35e8`, with that output. Observed by
  AC1 and AC5.
- **S2** — L2. The ledger's AC1 line keeps its staged form and the reason that form ran first, and
  adds the spec's `HEAD` form observed at `e74ef35e8`, with that output. Observed by AC2 and AC5.
- **S3** — The class's Symptom list gains the form L1 found, a criterion graded on `HEAD` whose
  ledger line lands in the commit it observes, and its count word moves from "Six" to "Seven".
  Observed by AC3 and AC6.
- **S4** — The class's Where it bit section gains L1 and L2. Observed by AC4 and AC6.
- **S5** — The pass writes this unit's own journal record,
  `memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-2-1-acceptance-ledger.md`, with
  one line per criterion in the grammar `memory/HYGIENE.md` states under "Acceptance ledger".
  NOT OBSERVED: check 23 selects Tier-2 specs only, and a record of the criteria cannot be one of the
  observations it records.

## 3. Non-goals (OUT)

- Any code, kit file or effort level.
- A re-review. Round 1 ended CONVERGED (`memory/builds/dEasedEffort/RUN.md:45`), and M4 makes that
  terminal for its subject.
- `TOOL-dEasedEffort-1`'s spec, which is CLOSED and stays as written. So L2's alternative fix, a spec
  revision naming both forms, is not taken.
- The ledger's prose paragraphs and its AC2, AC4 and AC5 lines, the build's agent ledger, and the
  review record.
- The class's count words beyond the one S3 moves, and its front matter, `## The fix` and `## Its gate`.
- A new gotcha class, or a machine gate. The class records that none fits.

## 4. Design

Read at `666fe2a88` on 2026-11-02. This is Tier-1 by the tier rule
(`memory/guides/SESSION-KICKOFF.md:118-122`): records only, with no template rule, gate semantics or
kit contract moved.

- **The form observed.** Both criteria diff to `HEAD`, and the commit each diff needs is the one its
  ledger line landed in. `git diff --name-only 2a6f3975 00866ea0a -- .claude` prints no line, which
  is what L1 found. S1 and S2 spell `HEAD` as `e74ef35e8`, the render's commit, because a fixed
  commit is one a later commit cannot move. The sha survives landing: `tools/push-main.sh:17` merges
  the branch and rewrites none of it.
- **The builder's order.** The builder runs both `git diff` commands first and writes what they
  print. Output that differs from AC1 or AC2 is a divergence to return, never a line to write. A
  ledger line that claims what its author did not run is the defect this unit closes.
- **In place, one physical line each.** Check 23's form test reads a line's first physical line, and
  its map keeps the first answer per label (`tools/memory-tree/check-memory-hygiene.sh:3244`, `:3351`).
  So each edit stays on its existing line, and a second AC1 or AC3 line would be read by nothing. The
  tokens the join uses stay first on their lines, `load_policy` and `render_agents.py --check`.
- **The class stays indexed as it is.** `memory/gotchas/INDEX.md` renders the front matter and the
  anchor count, and check 17 byte-compares it (`memory/HYGIENE.md:399`). An anchor is a backticked
  token that carries `/` or a file extension (`tools/memory-tree/gotchas.py:65`). The new text carries
  none, so the row does not move and no index render is owed for this file.
- **This unit's own criteria.** None diffs to `HEAD`. Each names fixed commits or the working tree,
  so each prints the same before and after the pass commit. Measured 2026-11-02 on a fixture clone
  with the edits below applied: uncommitted and committed gave the same output, and the unedited tree
  gave the red side AC1 to AC4 name.
- **S5's reason.** A Tier-1 unit owes no ledger (`memory/guides/SESSION-KICKOFF.md:63`). L2's finding
  is that a return is not a kept record, so a unit fixing that finding keeps one.

### The ledger's edits

The AC1 line gains these three sentences after "printed 4 added and 4 deleted.", on the same line.

```text
The staged form ran first because the pass commit AC1's `HEAD` form diffs does not exist while its own ledger is written. `TOOL-dEasedEffort-2`'s pass then observed that form at a named commit: `git diff --numstat 2a6f3975 e74ef35e8 -- tools/roles/house/policy.toml` printed 4 added and 4 deleted.
```

In the AC3 line, this clause goes.

```text
`git diff --name-only 2a6f3975 HEAD -- .claude` printed exactly those four paths on the render's commit, and `--check` exited 0.
```

This text stands in its place, on the same line.

```text
and `--check` exited 0. This line landed in the render's commit, so `HEAD` was still `00866ea0a` when it was written, and the spec's `HEAD` form prints nothing there. `TOOL-dEasedEffort-2`'s pass observed that form at a named commit: `git diff --name-only 2a6f3975 e74ef35e8 -- .claude` printed exactly `.claude/agents/gov-builder.md`, `.claude/agents/gov-diff-reviewer.md`, `.claude/agents/gov-orienter.md` and `.claude/agents/gov-skeptic.md`.
```

### The class's edits

In the Symptom list's opening line, "Six ways" becomes "Seven ways". This bullet is the list's new last
item.

```markdown
- **Its ledger line lands in the commit it observes.** A criterion graded on `HEAD` names a diff
  whose far end is the commit its own ledger line lands in, so that commit does not exist while the
  line is written. The command prints the tree before it, and the line either claims an output
  nobody saw or records another form. A spec audit asks of each such criterion which commit its
  ledger line lands in, and wants a form observable before that commit or a line landing after it.
```

This paragraph is the new last paragraph of Where it bit, directly above `## The fix`. Its final
sentence is L2's left-shift, which the review states as a check for the close.

```markdown
The commit that holds its own ledger line bit dEasedEffort at its closing diff review, round 1, as
items L1 and L2. `TOOL-dEasedEffort-1` AC3 graded a diff on `HEAD`, its rollout added the line and
then committed, and the line said the command printed four paths on a commit it landed inside, when
`HEAD` was still the commit before and that form printed nothing. AC1 named the same form, the
ledger recorded a `--cached` spelling, and the reason lived only in a commit trailer, as
`TOOL-aOrientedCast-21` AC2's deviation had. A close compares each criterion's command with the form
its ledger line records, and a difference owes a spec amendment or an observation of the named form.
```

### Files touched (estimate)

`memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md`
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
`memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-2-1-acceptance-ledger.md`

## 5. Acceptance criteria

Run these from the worktree root in one Bash shell with the two names below set. The `git diff`
pathspecs are relative to that root.

```bash
L=memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md
G=memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md
```

- **AC1** — When `git diff --name-only 2a6f3975 e74ef35e8 -- .claude` runs, it prints exactly the four
  agent-type paths, and the ledger's AC3 line names that commit and that output:
  `grep '^- AC3 — ' "$L" | grep -c -- "--name-only 2a6f3975 e74ef35e8 -- .claude"` prints `1`,
  `grep '^- AC3 — ' "$L" | grep -o '\.claude/agents/gov-[a-z-]*\.md' | sort | diff - <(git diff --name-only 2a6f3975 e74ef35e8 -- .claude)` prints nothing and exits 0, and
  `grep -c "2a6f3975 HEAD" "$L"` prints `0`.
  Red when: the line still claims the `HEAD` form printed on the render's commit, where the last
  command prints `1` today, or the paths it names differ from the diff's.
- **AC2** — When `git diff --numstat 2a6f3975 e74ef35e8 -- tools/roles/house/policy.toml` runs, it
  prints 4 added and 4 deleted, and the ledger's AC1 line names that commit and that output:
  `grep '^- AC1 — ' "$L" | grep -c -- "--numstat 2a6f3975 e74ef35e8 -- tools/roles/house/policy"` prints `1`,
  `grep '^- AC1 — ' "$L" | grep -o "4 added and 4 deleted" | wc -l` prints `2`,
  `grep '^- AC1 — ' "$L" | grep -c -- "--cached --numstat 2a6f3975"` prints `1`, and
  `grep '^- AC1 — ' "$L" | grep -c "does not exist while its own ledger is written"` prints `1`.
  Red when: the line carries no observation of the spec's form, where the first and last greps print
  `0` today, or the staged form or its reason left the line.
  figure: PINNED — 4 and 4 are a diff between two fixed commits, measured 2026-11-02.
- **AC3** — When `sed -n '/^## Symptom/,/^## Where it bit/p' "$G" | grep -c '^- \*\*'` runs, it prints
  `7`, where it prints `6` today, and over the same `sed` range
  `grep -c '^- \*\*Its ledger line lands in the commit it observes\.\*\*'` and
  `grep -c 'A criterion graded on .HEAD.'` each print `1`. `grep -c "Seven ways, and a spec set" "$G"`
  prints `1` and `grep -c "Six ways" "$G"` prints `0`.
  Red when: the bullet sits outside the Symptom list, or the count word disagrees with the bullets.
- **AC4** — When `sed -n '/^## Where it bit/,/^## The fix/p' "$G" | grep -c "TOOL-dEasedEffort-1"` runs,
  it prints `1`, and over the same range `grep -c "items L1 and L2"` prints `1`. Both print `0` today.
  Red when: the paragraph sits outside Where it bit, or names the unit without the review's items.
- **AC5** — When `grep -cP '^- AC[1-5] — \x60[^\x60]+\x60 — ' "$L"` runs, it prints `5`, so every AC
  line still opens with its backticked token on its first physical line, and
  `git diff --numstat e74ef35e8 -- "$L"` prints 2 added and 2 deleted.
  Red when: an edit wraps a line or moves its token, which check 23 reads as a line in neither legal
  form, or a line beyond the two moved.
- **AC6** — When `git diff e74ef35e8 -- "$G" | grep -c '^-[^-]'` runs, it prints `1`, the count-word
  line, so the class's front matter and `## The fix` did not move, and
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import gotchas as g; print(len(set(g.ANCHOR_RE.findall(open(sys.argv[1], encoding='utf-8').read().split('---', 2)[2]))))" "$G"`
  prints `3`, the count `memory/gotchas/INDEX.md` holds for this class.
  Red when: the new text adds a backticked path, which moves the index row, or another line moved.
  figure: PINNED — 3 is the anchor count measured 2026-11-02 at `666fe2a88`.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

This unit adds no gate arm. The main loop runs these legs once, at the close, with the full bar, and
no pass runs one. The brief names the first two. The other two are owed because both Files touched
paths trip the `memory/` guard in `tools/gate-legs.json`, which two legs carry, under
`BROAD_LEG_FLOOR` (`tools/check-spec-tokens.py:362`).

What no leg checks: that a ledger line's observation was made. Check 23 grades shape and coverage only
(`memory/HYGIENE.md:713`), and it passed both defects. AC1 and AC2 observe the fix, and no leg
re-observes it.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 9. Reuse audit

No code seam applies: `tools/codebase-map/reuse_lookup.py` run on "acceptance ledger line records an
observation at a named commit, a criterion graded on HEAD" returned name-stem hits only, such as
`build_commit` and `check_line`, and none writes a ledger line. The seam is the class itself,
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, which review items L1 and L2
both name. Its Fix section already holds the rule that a criterion found wrong at build time is amended
where its spec allows, so this unit adds a form and two instances. The sibling class
`memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md` is about a tree a later fold
of one commit moved. It records one honest observation gone stale, where L1 records one that could
not have happened, so it takes no edit.

Where the records and the source disagreed. The review cites AC3 at line 183 and Rollout step 2 at
line 121 of `TOOL-dEasedEffort-1`'s spec, and both sit a line later today, at 184 and 122. The brief
names two legs, and the guards join owes four (section 6).

Recall terms used: acceptance ledger criterion HEAD form observed commit trailer deviation AMENDED
gotcha Symptom Where-it-bit, with the question "how is an acceptance ledger line corrected when the
command it records could not have printed its result".
