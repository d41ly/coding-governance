# TOOL-dHomedResolver-5 — the closing review's minors: the guard reaches --new-build, its arm can fail, its remedy quotes

**Status:** SPECCED · rev-1 · 2026-10-09 · node d · Tier-2 · base 04b0b239 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 1 confirmed no blocker and no high, and five mediums and two lows
merging into four items. The severity rule promotes them all into ONE unit, and this is it. It
closes each item with its own arm, observed red first, and adopts the one real gap the review
refuted as older than this build.

## 2. Scope (IN)

- **S1** — M1 (ids 3, 7): `cmd_new_build` calls `check_archives_tracked` before `check_slug_claimed`
  and before any write, so a refusal over a half-staged rotation leaves no README and no registry
  row behind. Observed by AC1.
- **S2** — M2 (ids 1, 4, 5): the generator self-test's "wrote nothing" arm counts calls to
  `write_text` during a refused `cmd_write` and asserts zero, replacing the byte compare that an
  unguarded render also passed. Observed by AC2.
- **S3** — L1 (id 2): `check_archives_tracked` lists with `git ls-files -z` and builds its remedy as
  `git add --` followed by each path through `shlex.quote`, so a name with a space stays one
  argument. Observed by AC3.
- **S4** — L2 (id 8): spec 1's S2 and S6 and spec 2's S4 stop claiming an AC observes prose no AC
  reads; each names the prose `NOT OBSERVED` with the reason, as a rev-2 bump with its §9 line.
  Observed by AC4.
- **S5** — Adopted from refuted id 6: a row-grammar arm for check 24's missing-home branch, which had
  no arm before this build either. Observed by AC5.

## 3. Non-goals (OUT)

- Any structural lint that every writing verb calls the guard first, or that every `Observed by`
  claim is read by its AC. Both were offered as left-shift ideas; neither is a confirmed finding.
- Changing what the guard refuses.

### Edges

- **consumes-from** `TOOL-dHomedResolver-2` — the guard whose call sites, arm and remedy this unit fixes.

## 4. Design

### Evidence

The round-1 record, `reviews/2026-10-09-review-TOOL-dHomedResolver-1-2-3-diff-review-round1.md`,
items M1, M2, L1 and L2 with the skeptics' reproductions. `cmd_new_build` writes the README, adds the
contract row and stages both before it returns `cmd_write`. The self-test's `_read_refusal` helper
already asserts "folder=False" for every other `--new-build` refusal.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/row_grammar.py`
- `memory/builds/dHomedResolver/spec/2026-10-09-spec-TOOL-dHomedResolver-1.md`
- `memory/builds/dHomedResolver/spec/2026-10-09-spec-TOOL-dHomedResolver-2.md`

### Alternatives rejected

- **For M2, a real half-staged fixture that deletes a cited row.** Rejected for the counting shim:
  the shim reds on ANY write before the refusal, which is the property, while a fixture reds only on
  writes that change the bytes it happens to compare.
- **For L1, remedy `git add -- <MEMORY_ROOT>/archive/`.** Rejected: it would also stage whatever
  else sits in the folder, which the operator did not ask for.

## 5. Production-readiness checklist

- security — L1 removes a remedy line a reader could paste with a split or unintended argument.
- perf / scale — none.
- error / empty / loading states — the guard now fires before `--new-build` writes anything.
- observability — the remedy names every path, quoted.
- risks — none beyond the arms: each is observed red against `04b0b239` first.
- testing — four generator arms and one row-grammar arm.
- migration — none.
- user docs — none: the behaviour each item fixes is already documented.

## 6. Acceptance criteria

- **AC1** — When `_read_refusal` runs `cmd_new_build` over the `sc` fixture holding an untracked
  archive, it prints `rc=1 folder=False` and `git add`, and `readme-contract.txt` gains no row.
  Red when: `--new-build` writes and stages before the guard fires.
- **AC2** — When the refused `cmd_write` runs under the `write_text` counting shim, the count is
  `writes=0`.
  Red when: the guard is moved below the write loop, which the byte compare did not catch.
- **AC3** — When an untracked archive named with a space sits under the archive folder, the refusal
  prints the path as one `shlex.quote` argument after `git add --`.
  Red when: the remedy space-joins raw paths.
- **AC4** — When `grep -n 'NOT OBSERVED'` runs over specs 1 and 2, it prints spec 1's S2 and S6 and
  spec 2's S4.
  Red when: an S item still claims an AC that does not read it.
- **AC5** — When `row_grammar.py --selftest` runs, a `cut` tree whose ARCH archive has no shard prints
  the `declares its live index at` finding naming the ARCH shard's home as not tracked.
  Red when: check 24's missing-home branch is deleted or its text drifts.

## 7. Gates

`build-index selftest` · `row-grammar selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 · an untracked archive under --new-build, a write-counting shim, and a space-named archive · none
New arm: tools/memory-tree/row_grammar.py · covers AC5 · a cut archive whose family has no shard · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the closing review's round 1.

## 10. Reuse audit

The seams are the guard itself, the self-test's `_read_refusal` helper and its `halfstaged` block, and
row-grammar's `_tree` fixture with `cmd_check_rotation`. Each fix is the one the review's skeptic
judged sound. `reuse_lookup.py "refuse when a file is untracked"` returned no guard to reuse;
every seam above is this build's own. No recall query was re-run for this unit: it changes no rule and adds no mechanism, and
the build's query is recorded in units 1 and 2.

Recall terms used: gen_build_index ids derived git ls-files untracked archive rotation half-staged write check drift corpus membership
