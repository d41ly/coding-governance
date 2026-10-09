# TOOL-dHomedResolver-2 — the build-index generator refuses while a file under the archive folder is untracked

**Status:** CLOSED · rev-2 · 2026-10-09 · node d · Tier-2 · base 5a836bf0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-dHomedResolver-2-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-dHomedResolver-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md](../prompts/2026-10-09-prompt-TOOL-dHomedResolver-1-0-run-mandate.md) | journal | TOOL-dHomedResolver-1 TOOL-dHomedResolver-3 |
| [2026-10-09-prompt-TOOL-dHomedResolver-2-1-build-brief.md](../prompts/2026-10-09-prompt-TOOL-dHomedResolver-2-1-build-brief.md) | journal | — |
| [2026-10-09-review-TOOL-dHomedResolver-1-2-3-diff-review-round1.md](../reviews/2026-10-09-review-TOOL-dHomedResolver-1-2-3-diff-review-round1.md) | diff-review | TOOL-dHomedResolver-1 TOOL-dHomedResolver-3 |

<!-- /gen:spec-records -->

## 1. Goal

`gen_build_index.py` derives every build README's `ids:` and `LIVE.md` from `git ls-files`. A
rotation moves rows from a tracked index into a new archive file, and until that file is staged
the moved rows look deleted. `--write` then rewrites every README citing one of them, and nothing
says why. Refuse `--write` and `--check` while any file under the archive folder is untracked, and
name the remedy.

## 2. Scope (IN)

- **S1** — `check_archives_tracked` lists untracked, non-ignored files under `<MEMORY_ROOT>/archive/`
  with `git ls-files --others --exclude-standard`, and raises a `Problem` naming every path and the
  remedy, `git add` them first. Observed by AC1 and AC3.
- **S2** — `cmd_write` calls it before `plan()`, so a refused write writes nothing. Observed by AC1.
- **S3** — `cmd_check` calls it before `plan()`, so the drift gate refuses with the same remedy rather
  than printing a `--write` remedy that would do the damage. Hygiene check 9 surfaces that refusal.
  Observed by AC2 and AC4.
- **S4** — The guard's header states what it does NOT check: ignored files, and untracked files
  outside the archive folder, which are ordinary work in progress. NOT OBSERVED — docstring prose
  no arm reads; AC5 greps for the guard and its call sites, not for this paragraph.
- **S5** — The HYGIENE catalogue's check 9 entry and its kit template say the check refuses over an
  untracked archive. Observed by AC5.

## 3. Non-goals (OUT)

- Core's `rotate_index.py --write` staging the archive it writes: a core-local fix, owed by the
  re-pull run.
- Any other verb that reads `collect()`, such as `--asks` or `--print-bindings`. They render
  nothing over the tree.
- Untracked files anywhere else under the memory root.

### Edges

- **hands-off** `TOOL-dHomedResolver-3` — the gotcha record for the half-staged-move class this unit closes.
- **hands-off** `TOOL-dHomedResolver-5` — the closing review's fixes to this guard: its reach into
  `--new-build`, its arm that could not fail, and its remedy's quoting.

## 4. Design

### Evidence

Read at base `5a836bf0`. `collect()` reads `git ls-files -- <m>/`, and `cmd_write` writes every
artifact `plan()` returns with no precondition. The hygiene suite's `rotarchive` fixture already
builds the half-staged state, with `git rm --cached` on an archive, and asserts only check 14's
orphan line there.

### Inventory

- `check_archives_tracked` — a function in `gen_build_index.py`.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/HYGIENE.md`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **Announce and continue.** Rejected: the prompt names the write as the damage, and a line printed
  above seventeen rewritten READMEs does not undo them.
- **Read untracked archives into the corpus.** Rejected: the corpus would then disagree with the
  hygiene gate's own `git ls-files` population, which is the two-answers class.
- **Refuse on any untracked file under the memory root.** Rejected: an unstaged spec draft is
  ordinary work, and refusing it would make `--write` unusable mid-build.

## 5. Production-readiness checklist

- security — N/A — reads git's index; writes nothing new.
- perf / scale — one `git ls-files` call per `--check` or `--write`.
- error / empty / loading states — an empty archive folder, or none, passes; a failed git call raises.
- observability — the refusal names every untracked path and the command that clears it.
- risks — check 9 now reds on a half-staged rotation where it printed drift. That is the intent.
- testing — new arms in the generator's self-test and the hygiene suite, each observed RED at base.
- migration — none: a tree with no untracked archive behaves exactly as before.
- user docs — the HYGIENE catalogue entry and the memory-tree README upgrade note.

## 6. Acceptance criteria

- **AC1** — When `gen_build_index.py --selftest` runs its new arm, `cmd_write` over a fixture holding
  an untracked DECISIONS archive under the archive folder raises a refusal naming that path and `git add`,
  and the build README's bytes are unchanged.
  Red when: `--write` renders over the half-staged tree.
- **AC2** — When the same arm calls `cmd_check` over that fixture, it raises the same refusal.
  Red when: the drift gate prints its `--write` remedy instead.
- **AC3** — When the arm's fixture holds an IGNORED file under `memory/archive/` and nothing untracked,
  `cmd_write` succeeds.
  Red when: the guard refuses a file git will not stage.
- **AC4** — When `check-memory-hygiene.sh` runs over the `rotarchive` fixture after its archive is
  unstaged, check 9's output names the unstaged ARCH archive and `git add`.
  Red when: hygiene reports drift without naming the untracked archive.
- **AC5** — When `git grep -n 'check_archives_tracked'` runs, it prints the guard and its two call
  sites in `tools/memory-tree/gen_build_index.py`, and `grep -n 'untracked' memory/HYGIENE.md` prints
  the check 9 entry.
  Red when: the guard or its carrier is missing.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 · an untracked archive file under --write and --check, and an ignored one · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC4 · the rotarchive fixture's unstaged archive · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §2 S4 is marked NOT OBSERVED instead of claiming AC5; §3 Edges hands off to
  TOOL-dHomedResolver-5 (closing review round 1, L2 and the promotion).

## 10. Reuse audit

The seam is `cmd_check` and `cmd_write`, whose shared `plan()` is the one place both reach the
corpus; the guard sits above it and raises the module's own `Problem`, which `main()` already prints
as `build-index: <message>` at exit 1. The fixture is the hygiene suite's `rotarchive` tree, which
already stages exactly this state. `reuse_lookup.py` returned no existing untracked-file guard in
the memory-tree kit. Recall returned the `rotarchive` fixture's history, the corpus-membership
reading of `cSteadyMetronome`'s report in an `aRelaxedShard` review, and TOOL-aStagedLane-5, a
sibling of this class in `check-pass-order.sh`, where a staged `git rm --cached` dropped a build from
grading. None rules that the generator should tolerate a half-staged rotation.

Recall terms used: gen_build_index ids derived git ls-files untracked archive rotation half-staged write check drift corpus membership
