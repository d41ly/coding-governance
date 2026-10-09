# TOOL-aFrugalTurnstile-11 — a scoped green takes its own slot, and the nearest adoptable green wins

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aFrugalTurnstile-2 found, building it, that one git dir holds ONE `gate-bar-green` slot. A
scoped push writes its own `kind scoped` record into that slot and so deletes the `kind full` record
its own base depends on; the next push from that git dir finds no adoptable base and goes FULL. A
wrapper-bar adopter pushing from one git dir therefore alternates FULL and scoped. Separately, the
hook adopts the FIRST adoptable candidate in a fixed order, runner stamps first, so where an older
full green and a newer scoped record at the graded merge are both adoptable, the push scopes from
the older one and re-grades the whole build. This unit gives a scoped record its own slot and makes
the candidate nearest the tip win.

## 2. Scope (IN)

- **S1 — the slot follows the kind.** In `.githooks/pre-push`'s `write_bar_green`, a `kind full`
  record keeps `gate-bar-green` (and `gate-bar-green.shared` from a linked worktree), and a
  `kind scoped` record goes to `gate-bar-green.scoped` (and `gate-bar-green.scoped.shared`), each
  through the same `.tmp` rename. The record grammar and the writer's line are unchanged except that
  the line names the file written. Observed by AC1, AC2.
- **S2 — the readers see both slots.** `bar_candidates` and `bar_labels` gain the three scoped
  paths after the three full ones, in the same this-git-dir, common-dir, shared order, with labels
  naming the file. `check_bar_base` keeps reading `kind full` records only, now from the full slots.
  The cover pass reads all six. Observed by AC3, AC4.
- **S3 — the nearest adoptable green wins.** After the runner-stamp loop adopts a candidate (or not)
  and before the decision line, every bar-record candidate is evaluated as today; among ALL adoptable
  candidates, runner stamp and bar records alike, the one whose own `sha` has the smallest
  `git rev-list --first-parent --count <sha>..<tip>` is adopted. A tie keeps the earlier candidate in
  today's order, so a runner stamp beats a bar record at the same distance and a full record beats a
  scoped one. The staleness bound a `kind scoped` record is held to is still counted from its base
  (TOOL-aFrugalTurnstile-2 S3b); only the PREFERENCE uses its own sha. The bar-record pass runs only
  for a non-STUB bar, as today, and switching from one adopted candidate to another can never turn a
  scoped decision FULL. The decision line names the adopted record as today. Observed by AC5, AC6.
- **S4 — the header.** The comment above `bar_candidates` states the two slots and why, and the one
  above the selection states the nearest-wins rule and what it does NOT check: that a nearer scoped
  record's base is the SAME full green an adopted runner stamp names. Observed by AC7.
- **S5 — the arms.** New arms in `.githooks/pre-push.test.sh` for AC1 to AC6, written but run at
  VERIFYING.

## 3. Non-goals (OUT)

- The unattended close's writer (TOOL-aFrugalTurnstile-3) writes `kind full` only and is unchanged;
  TOOL-aFrugalTurnstile-9, which makes it write `kind scoped`, inherits S1's slot rule through the
  hook's writer that it mirrors.
- `post-merge.sh` (TOOL-aFrugalTurnstile-6) writes `kind full` into the shared full slot; unchanged.
- Any change to which records are adoptable; this unit changes only where a scoped record lives and
  which of several adoptable records is chosen.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-2` — the record grammar, its writer, `check_bar_record`
  and `check_bar_base`.
- **hands-off** `TOOL-aFrugalTurnstile-9` — a scoped record written by the unattended close goes to
  the scoped slot by the same rule.

## 4. Design

Two slots rather than a list. A list would need a pruning rule and a reader that scans it; two
fixed paths per place keep every read a builtin loop over existing files, and they hold exactly what
a later push can use: the newest full green (a base) and the newest scoped green (a nearer start).

Nearest wins by first-parent distance because that is the unit the staleness bound already counts
in (design D1), and the scoped bar a push runs is the diff from the adopted sha to the tip: a nearer
sha is a smaller diff. Soundness is unchanged: every candidate considered already passed the same
predicates it passes today.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `gate-bar-green.scoped`, `gate-bar-green.scoped.shared` | git-dir record | none |

No new function name: S3 extends the existing selection block.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`

### Rollout

No migration: an absent scoped slot is today's state. A scoped record already written by
TOOL-aFrugalTurnstile-2's code into the full slot is read as before.

### Alternatives rejected

- **The writer keeps a full record when its base sits in the same slot**: then the scoped record is
  lost, and the in-place landing scopes from the older base again.
- **First-wins with scoped slots ahead of full ones**: a stale scoped record would beat a newer
  full green.

## 5. Production-readiness checklist

- security — two more files in the git dir, trusted exactly as `gate-bar-green` is.
- perf / scale — at most three more candidate files, and one `git rev-list --count` per adoptable
  candidate.
- error / empty / loading states — a slot that cannot be written prints the writer's decline line.
- observability — the writer names the file; the decision line names the adopted record.
- testing — S5's arms; the pass observes AC1 to AC7 in a scratch fixture.
- migration — none.
- risks — a nearer scoped record whose own base is older than an adopted runner stamp now wins; it
  was already adoptable on its own predicates, so the change picks among sound candidates only.
- user docs — the hook header (S4).

## 6. Acceptance criteria

Observed in one scratch fixture built as TOOL-aFrugalTurnstile-2's was: a bare remote, a work clone
whose hooks dir holds a copy of the hook, a tracked wrapper bar over a stand-in runner that appends
to a marker file, and the lander marker.

- **AC1** — When a FULL wrapper-bar push writes `kind full` and the next push is scoped and green,
  the git dir holds BOTH `gate-bar-green` (`kind full`, unchanged) and `gate-bar-green.scoped`
  (`kind scoped`). Red when: the scoped record replaced the full one, which is the behaviour at the
  previous commit.
- **AC2** — When that scoped push ran from a linked worktree, the common dir holds
  `gate-bar-green.scoped.shared` byte-identical to the worktree's scoped record. Red when: it is
  absent.
- **AC3** — When a third push follows AC1's two from the same git dir, its decision line reads
  `scoped gate`, not `FULL gate`. Red when: it reads FULL with `no full green this push can adopt`,
  the alternation TOOL-aFrugalTurnstile-2 reported.
- **AC4** — When a `kind scoped` record exists only in the scoped slot and a push's tree equals its
  tree with the base it names adopted, the push is covered. Red when: the cover pass does not read
  the scoped slot.
- **AC5** — When a runner stamp at F and a `kind scoped` bar record at M (base F, one first-parent
  landing behind the tip) are both adoptable, the decision scopes from M. Red when: it scopes from F,
  the first-wins order.
- **AC6** — When a runner stamp and a bar record name the same sha, the scoped decision line names
  `gate-full-green` as the adopted record. Red when: it names `gate-bar-green` instead.
- **AC7** — When `grep -c 'NEAREST ADOPTABLE GREEN WINS' .githooks/pre-push` runs, it prints `1`.
  Red when: `0`.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `testsuite counts (every bar self-test prints one)`

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the scratch fixture above · none

The header sentence S4 adds, quoted: "NEAREST ADOPTABLE GREEN WINS: among every candidate that passes
the predicates, the one whose own sha is fewest first-parent landings behind the tip is adopted, so a
scoped green at the graded merge beats an older full green; this does not check that the two name
the same base."

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §2 S1-S5, §6 AC1-AC7: initial draft, adopted mid-build from
  TOOL-aFrugalTurnstile-2's discovery (protocol §11), insertion points read at b99b2dc38.

## 10. Reuse audit

The seams are TOOL-aFrugalTurnstile-2's own: `write_bar_green`, `bar_candidates`, `read_bar_file`,
`check_bar_record`, `check_bar_base` and the selection block after the runner-stamp loop.
`reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so the seams
were found by reading `.githooks/pre-push` at b99b2dc38; no existing seam keeps two greens per place.

Recall terms used: pre-push full green stamp scoped boundary candidate shared worktree slot nearest lag
