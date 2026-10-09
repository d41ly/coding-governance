# TOOL-aFrugalTurnstile-3 — the unattended close records the green of the bar it ran

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 2 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D3's second writer. When the unattended close's `gates-green` item runs the
declared bar and it exits 0 on a clean, unmoved tree, the close leaves the same `gate-bar-green`
record the push boundary writes, so a wrapper bar such as inCMS's, which never earns a usable runner
stamp, still leaves a green the boundary can read.

## 2. Scope (IN)

- **S1 — the writer, one function.** A new column-0 function `write_bar_green` in
  `tools/unattended/unattended.sh`, with the hook's signature
  `<git dir> <head before> <rc> <kind> <base> <bar> <run id>` and the hook's grammar from
  TOOL-aFrugalTurnstile-2 S1: the same five preconditions, the same ten keys in the same order, the
  same `.tmp` rename, the same `.shared` copy into the common dir from a linked worktree. It calls
  git through the library's `GIT` wrapper and writes `by unattended`. It prints nothing when `rc` is
  not 0, because the red is already the item's output. On rc 0 it prints one line, either
  `unattended: gates-green — recorded gate-bar-green for <sha8> (kind <kind>)` or
  `unattended: gates-green — no gate-bar-green written: <why>`. Observed by AC1, AC2, AC3, AC4, AC5.
- **S2 — the arm calls it.** In the `gates-green` arm of `dod_met` (~10126-10240), inside the
  re-run loop and immediately before each `run_bounded`, `_ghb=$(GIT rev-parse HEAD 2>/dev/null)`
  records the HEAD the bar starts on. After the loop, beside the existing
  `_gh=$(GIT rev-parse HEAD 2>/dev/null)`, the arm calls
  `write_bar_green "$_ggd" "$_ghb" "$_grc" "$_gkind" "" "$GATE_CMD" "$_gid"` when `_ggd` is
  non-empty. `_gkind` is `full` under `LANDER_MODE=in-place`, whose bar always runs with GATE_FULL
  set to 1; under `primary` it is `full` only when this process's own environment carries GATE_FULL
  set to 1, which the bar inherits; otherwise it is empty and S1 declines with
  `the bar did not run full`. `base` is always empty here. Observed by AC6, AC7.
- **S3 — the parity arm.** The grammar is spelled in two programs, as `read_policy_key` already
  is, so one arm in `tools/unattended/unattended.test.sh` evaluates both writers out of their files
  with the suite's `slice_fn` recipe (the hook's through the same awk and sed over
  `.githooks/pre-push`), calls each with identical arguments in one clean scratch repo, and compares
  the two records' `cut -f1` key columns with each other and with the literal ten-key list. Observed
  by AC8.
- **S4 — the header sentence.** The comment above the call states what the record does not check
  (§7). Observed by AC9.

## 3. Non-goals (OUT)

- The decision change under a declared post-merge bar, the `scoped` kind and a non-empty `base`
  from this writer, and the `covered` branch: all TOOL-aFrugalTurnstile-9.
- Writing on the inherited-red MET path. A bar that exits non-zero wrote a red, whatever the close
  then decides about it; S1 refuses `rc` other than 0.
- Re-recording after `write_close_commit` commits the run-state file on top of the graded merge
  (F1). The record names the tree the bar graded and no other.

### Edges

- **consumes-from** `TOOL-aFrugalTurnstile-2` — the record grammar and the hook's writer, which the
  S3 parity arm reads. The pass needs only design D3's key list; the arm needs both functions built.
- **hands-off** `TOOL-aFrugalTurnstile-9` — the scoped kind with its base, and the covered case,
  under a declared post-merge bar; and F1's finding, that the in-place landing push carries the
  close's records commit on top of the graded merge.

## 4. Design

The arm already pins a fresh run id per try, reads HEAD after the bar, and holds the git dir in
`_ggd` from `resolve_sidecar_dir`. The writer needs one more fact, the HEAD each try STARTED on, so
`_ghb` is refreshed before every `run_bounded` in the TREE MOVED re-run loop and the value passed is
the last try's. A tree that moved during the bar fails S1's HEAD or porcelain precondition, and the
runner's own exit 3 already says so.

The bar string written is `$GATE_CMD` exactly as `.unattended.conf` declares it. The boundary
compares it byte for byte with the hook's `$gate`. In this repository both read
`bash tools/run-gates/run-gates.sh` at base (`.unattended.conf` line 46, and the hook's default
`bash $GATE_RUNNER`), so the two records name one bar. An adopter whose two spellings differ gets no
cover from this record, which costs a saving and never a verdict.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `write_bar_green` | function | `sh.function`, `python tools/lexicon/lexicon.py --suggest` answered OK |
| `_ghb`, `_gkind` | arm locals | none |

### Rollout

No migration; an absent record is today's state. This unit and TOOL-aFrugalTurnstile-5 both write
`tools/unattended/unattended.sh` in order group 2, so the two passes are not write-disjoint and
sequence.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A shared library function sourced by both writers**: the hook ships verbatim and sources no kit,
  which is why `read_policy_key` is spelled twice and held together by an arm.
- **Recording after the close's records commit**: that names a tree no bar graded.

## 5. Production-readiness checklist

- security — the record is written under the run's own uid into the git dir, the same trust as the
  runner's stamp; the bar string is the declared one, never the environment's.
- perf / scale — four `GIT` spawns on a green close, none on a red one.
- error / empty / loading states — each declined precondition prints its reason; an empty `_ggd`
  skips the call, as the arm already skips its run-record reads.
- observability — the one writer line per green close.
- risks — F1: under `in-place` the landing push carries `records(<slug>): close — LANDING` on top
  of the graded merge, so this record does not cover that push; it covers a later push of the
  graded tree and serves the post-merge path. A green bar that leaves the record unwritten costs a
  saving only.
- testing — S3's parity arm and the end-to-end arm in §7; the pass observes AC1 to AC9 directly.
- migration — none.
- user docs — none of its own; the protocol text is TOOL-aFrugalTurnstile-10's.

## 6. Acceptance criteria

Criteria AC1 to AC5 slice `write_bar_green` out of the driver with the `slice_fn` recipe into a script under
the session scratch, define `GIT` as `git "$@"`, and call it in a scratch repo. AC6 and AC7 run a
slice of the driver suite, its prologue through `fixture()` plus one new block, from the session
scratch with its kit-dir variable pointing at `tools/unattended`; never the whole suite.

- **AC1** — When `write_bar_green` is called with rc 0, kind `full`, the repo's HEAD as the head
  before and a clean tree, `gate-bar-green` carries `by unattended`, `kind full`, the passed bar and
  run id, and a tree equal to `git rev-parse HEAD^{tree}`. Red when: the file is absent.
- **AC2** — When `write_bar_green` is called with rc 1, no file is written and nothing is printed.
  Red when: a record appears.
- **AC3** — When an untracked file sits in the scratch repo, `write_bar_green` writes no file and
  its line names the tree. Red when: a record appears over a dirty tree.
- **AC4** — When `head before` names the parent of HEAD, no file is written. Red when: one is.
- **AC5** — When the scratch repo is a linked worktree made with `git worktree add`, the common dir
  also holds `gate-bar-green.shared`. Red when: it is absent.
- **AC6** — When the suite slice runs `--preflight` then `--close` with GATE_FULL exported as 1 and a
  declared `GATE_CMD` naming a tracked probe that exits 0, the fixture's git dir holds
  `gate-bar-green` whose `bar` is that `GATE_CMD`. Red when: it is absent, which the base driver
  shows when run first, the driver as `git show` prints it at base `bef97330`.
- **AC7** — When the same close runs without GATE_FULL under `primary`, no record is written and the
  output carries `the bar did not run full`; when the probe exits 1, no record is written. Red when:
  either writes one.
- **AC8** — When both `write_bar_green` functions are sliced and called with identical arguments,
  their `cut -f1` columns are equal to each other and to the ten keys in order; when one key is
  dropped from a copy of the driver's function, the comparison reports the difference. Red when:
  the comparison passes over the dropped key.
  fixture: needs TOOL-aFrugalTurnstile-2 built; before it, the hook half is absent and the arm says so.
- **AC9** — When `grep -c 'WHAT THIS RECORD DOES NOT CHECK' tools/unattended/unattended.sh` runs, it
  prints `1`. Red when: it prints `0`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)`

New arm: tools/unattended/unattended.test.sh · covers AC6 AC7 · a close over a tracked probe bar, green with GATE_FULL, green without it, and red · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · both writers sliced and called alike, plus a copy with one key dropped · none

The sentence S4 adds above the call, quoted: "WHAT THIS RECORD DOES NOT CHECK: it says this bar
exited 0 on this tree, never that the push boundary will run the same bar; that equality is the
reader's, which compares the bar string byte for byte."

## 8. Open questions

- **FACT-QUESTION · F1 — Does the in-place landing push carry the tree this close's bar graded, as
  design §1 and D11 state?** Probe: the order of the `gates-green` item and `write_close_commit` in
  `verb_close`, and in an in-place fixture `git rev-parse HEAD^{tree}` after the close against this
  record's `tree`. Observed at writing time by the read: `write_close_commit` (~9752) is called at
  ~10091, after the whole Definition of Done, and commits the run-state file on top of the graded
  merge. Liveness: a re-close over a record already at LANDING commits nothing, and there the two
  trees are equal, so the probe can read the other way. The winner for this unit falls out: the
  record names the graded tree, the mechanism is unchanged, and D11's "covered by construction"
  does not hold for a first close.
  RESOLVED (agent, 2026-10-09, delegated): build S1 to S4 as written; hand the finding to
  TOOL-aFrugalTurnstile-9 and to the main loop for a rev of design D11.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft from design D3, the arm read at base bef97330.

## 10. Reuse audit

`reuse_lookup.py` asked "write a key per line record into the git dir and share it from a linked
worktree" returned no shell seam for a key-per-line git-dir record; the seam this unit extends is
the `gates-green` arm itself, its `_ggd` from `resolve_sidecar_dir` and its pinned `_gid`, and the
grammar is TOOL-aFrugalTurnstile-2's, held together by the parity arm the way `read_policy_key`'s
two copies are. The suite's `slice_fn` is the seam AC1 to AC5 and AC8 reuse.

Recall terms used: gates-green in-place GATE_FULL close bar run id gates-run fact tree moved lander merge record
