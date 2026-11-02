# TOOL-dFoldedAudit-11 — a chain fold joins to the tree: the spec's header rev and its Revision log

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base 74274869 · streams tooling · order 120

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-11-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-11-ledger.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-11-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-11-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-11-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-11-spec-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-13 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |

<!-- /gen:spec-records -->

## 1. Goal

`--record-round` tests only the grammar of a `local` or `--sibling` row, so a fold that never happened
reaches no reader: with every spec at rev-1, two claimed folds printed `round 2 · STOP · reason own-work`
and no spec changed. Design [survive] 2 requires a fold to name its unit, its new rev and a Revision
log line in that spec. This unit makes the verb read the tree before it writes a byte, and closes
item H3 of the closing review.

## 2. Scope (IN)

- **S1** — The rev join. `write_chain_round` reads the tracked spec of each `local` row's unit and each
  `--sibling` row's unit, and refuses when the header rev is below the row's rev or the Revision log
  has no entry at that rev. Observed by AC1, AC2, AC5 and AC6.
- **S2** — The first draft. A `local` or `--sibling` row claiming a rev below 2 is refused, because a
  fold bumps a rev and rev-1 is a spec's first draft. Observed by AC3.
- **S3** — The missing spec. A `local` or `--sibling` row whose unit no tracked spec carries is refused.
  A `new-mechanism` row is not joined, because a promoted unit has no spec yet. Observed by AC4.
- **S4** — The order. The join runs after every grammar and count test and before any byte is written.
  Observed by AC7.
- **S5** — The census. Every refusal goes through `check_chain_fault`, so the driver gains no `fail`
  site. Observed by AC7.
- **S6** — The suite's fixture. `write_chain_fixture` writes each spec at rev-3 with a Revision log
  holding rev-1 to rev-3, because every `local` and `--sibling` row the suite's chain arms write claims
  rev 2 or 3 and each would now be refused. NOT OBSERVED by a criterion: no acceptance bullet may name
  a suite, and the main loop observes those arms green at the close.

## 3. Non-goals (OUT)

- Any change to the row grammar, or to `derive_chain_verdict`.
- Joining a round to the review row or to `spec-audit` records, which `TOOL-dFoldedAudit-10` holds.
- Testing that a Revision log entry names the finding or the review record. `check_audit_fold` reads
  that citation for the deviation join, and a sibling row carries no finding id to test.
- Refusing a fold into a CLOSED spec. The harness's frozen join owns it, and this verb tests no status.
- The order the harness renders, which is review item M10. The caller commits folds before running
  this verb, so the tree is current.
- A hand-off to `--chain-verdict`. A refused round writes nothing, so the verdict reads the record as
  it stood.
- A closing diff review, which writes no chain round.

### Edges

- **consumes-from** external — the row grammar, `check_chain_fault` and `load_spec_facts`, all shipped, and the rendered route that commits a disposal's folds before it runs the command; a caller reversing that order is refused with its fold on disk
- **hands-off** `TOOL-dFoldedAudit-15` — the refusal list in the `--record-round` entry of `memory/guides/UNATTENDED-VERBS.md` does not gain this refusal here. That unit's batch writes it with the render, and this unit's write set holds no carrier

## 4. Design

Every line cited here was read at `f055a11b`, the branch tip, because units 1 to 8 moved them past
the header's base.

### The join

The two row loops in `write_chain_round` (`tools/unattended/unattended.sh:13525-13534`) each add a
`<unit> <rev>` pair to a local `folds` array, the first for a `local` row and the second for every
`--sibling` row. Every severity joins, because a minor's fold bumps a rev too.
`TOOL-dFoldedAudit-13`, at order 100, leaves a scalar `folds` in those two loops and tests it with
`[ -n "$folds" ]`. This unit retypes that variable as the array, so one name marks a fold, and moves the
test to `[ "${#folds[@]}" -gt 0 ]`, because `$folds` over an empty array is unbound under the driver's
`set -u`. After the count test at `:13535-13538` and before `rec=$_chain_rec` at `:13539`:

```bash
if [ "${#folds[@]}" -gt 0 ]; then
  load_spec_facts $(git ls-files "$M/builds/$slug/spec/*.md" 2>/dev/null | drop_working_specs) \
    || print_env_failure 118 "the build's specs could not be read, so no fold can be joined: $M/builds/$slug"
  for tok in "${folds[@]}"; do check_chain_fold "${tok% *}" "${tok#* }" || return 1; done
fi
```

The read is the one `print_chain_verdict` makes at `:13656-13657`, and `SPEC_PATH` maps a unit id to
its first tracked path (`:4793`). A round with no such row reads no spec.

### The refusals

`check_chain_fold` takes the unit and the rev, reads the unit's spec with one awk, and refuses through
`check_chain_fault`, the one site. The awk compares the rev itself, because a `[0-9]+` token can
overflow `[ -lt ]`.

| Test, in order | Refused with |
|---|---|
| `SPEC_PATH` has no entry for the unit | `a fold names <unit>, and no tracked spec carries that id, so its rev joins to nothing` |
| the rev is below 2 | `a fold claims rev-<r> on <unit>, and rev-1 is a spec's first draft, so no fold produced it` |
| the header rev is below the row's | `<unit>'s spec stands at rev-<h>, below the rev-<r> this row claims, so the fold never reached the tree` |
| no log entry at that rev | `<unit>'s spec has no Revision log entry at rev-<r>, so the fold left no line to read` |

The second row is an addition to the report's judged fix, and both refusals that fix names stand
unchanged. Without it the reproduction passes by spelling `1` for `99`: a row claiming rev 1 on a
rev-1 spec is at the header and has an entry. The records settle it. [survive] 2 says a fold names
its unit's new rev, the format calls rev-1 the first draft, and review item L2's skeptic states that
"a claim of 1 can never be a bump". The harness's own test already requires a rev above the one the
audit read, so no honest row claims 1.

### The reader

The grammar is the kit's, spelled in awk because the driver spawns no Python here and this kit
copy-installs without the memory-tree kit.

| Field | Reads |
|---|---|
| line ending | a trailing CR is cut first, as every driver awk does |
| header rev | the first `^\*\*Status:\*\* [A-Z]+ · rev-[0-9]+ ` line, the anchor `spec_facts` uses at `:4777` |
| log section | a `## ` heading of `^## ([0-9]+[.] )?Revision log`, closed by the next `## ` heading |
| log entry | `^([ \t]*[-*][ \t]*)?(\*\*)?rev-[0-9]+`, `REV_ENTRY` at `tools/memory-tree/design_lib.py:534` |

The heading admits no ordinal as well, where `REV_LOG_HEAD` at `tools/memory-tree/design_lib.py:533`
requires one, because a Tier-1 spec's numbering is free. A header with no rev reads 0, so it takes the
third refusal.

### What the join does not check

The comment above `check_chain_fold` says each of these:

- A rev the spec already held. A row claiming rev-2 on a spec whose rev-2 was an older fold passes, so
  the join proves that the rev exists and never that this finding made it.
- Bytes in the index. It reads the worktree, as `print_chain_verdict` does, so an uncommitted fold
  passes. The caller's order commits it first.
- That the entry names the finding.
- A `new-mechanism` row's unit.

### The suite's move

`write_chain_fixture` (`tools/unattended/unattended.test.sh:2634`) gains the three log lines and writes
`rev-3`. That is the one edit that keeps the chain arms' rows joined. The new arms build their breaks
on it, one spec at a time.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `check_chain_fold` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-02 |
| `folds` | local array in `write_chain_round`, retyping the scalar `TOOL-dFoldedAudit-13` leaves | none, a local |

### Rollout

Live at landing. Only a declared `disposal` renders the command, and `--record-round` writes a record
no tracked build yet holds, so no landed record moves.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Reading the rev through `tools/memory-tree/design_lib.py`.** The unattended kit copy-installs
  without the memory-tree kit.
- **A new field on `spec_facts`.** Its output is three tab fields read by `load_spec_facts` and
  `spec_ids`, for a value one verb needs.
- **Requiring the entry to name the finding id.** A finding id is a bare integer, so the test would
  match a date or a rev, and a sibling row has no id.
- **Comparing the row's rev with the highest the record holds for that unit.** It needs a second read
  of the record for one more false-claim shape, and it is not what the report judged.

## 5. Production-readiness checklist

- security: the verb gains a read of the tree, and the unit id reaches that read only after its
  grammar test. The id keys a map whose paths came from `git ls-files`, so a row cannot name a path.
- perf / scale: one `git ls-files`, the spec-facts read and one awk per joined row, once per round.
- error / empty / loading states: a round with no joined row reads nothing. An unreadable spec has no
  id, so it takes the first refusal.
- observability: each refusal names the unit and both revs.
- risks:
  - The rev join is a lower bound, as §4 states, so a later round can claim a rev an older fold left.
    The first round over rev-1 specs has no such rev to claim.
  - A caller running the command before it commits still passes on worktree bytes, and that is the
    order this unit does not read.
- testing: fixtures per §6, no gate, with the arms on `New arm:` lines in §7.
- migration: none. No chain record is tracked, and a tracked one is never re-read by this verb.
- user docs: N/A. `help/` documents no chain verb, which a grep over it confirmed on 2026-11-02.

## 6. Acceptance criteria

Fixture R is a scratch git repository at `%TEMP%/fa11` holding copies of
`tools/unattended/unattended.sh` and `tools/unattended/lib-unattended.sh` under `u/`, a
`.unattended.conf` carrying `MEMORY_ROOT=memory` and `SPEC_FOLD_CUTOFF="2000-01-01"`, because
`TOOL-dFoldedAudit-13` refuses a `local` or `--sibling` row under a blank cutoff, and a build `dFix`
whose README's roster region names
`FIX-dFix-1` to `FIX-dFix-7`, each with a tracked OPEN spec at rev-3 whose `## 9. Revision log` holds
`- rev-1`, `- rev-2` and `- rev-3` entries, and no `RUN.md`. A step the criterion names commits its
change to a spec. `$V` is `bash "$F/u/unattended.sh"`, run from the fixture root with `GOV_REMOTE` and
`GOV_DEFAULT_BRANCH` cleared. A criterion that spells only a row runs it on a fresh `--subject` of
`$V --record-round dFix --subject s1 --audited FIX-dFix-2 --blockers 0 --highs 0`. Each refusal exits 1
printing `UNATTENDED check 118 FAILED`.

- **AC1** — When every spec is rewritten at rev-1 with one log entry and
  `$V --record-round dFix --subject s1 --audited FIX-dFix-2 --blockers 0 --highs 1 --finding 7/HIGH/local/FIX-dFix-2/FIX-dFix-2/99`
  runs, it refuses printing `stands at rev-1, below the rev-99`, `git ls-files '*-chain-rounds.md'`
  prints nothing, and `$V --chain-verdict dFix` prints `round 0`. The same call with rev 100 refuses
  the same way.
  Red when: the row's grammar is all the verb reads, which is the report's reproduction.
- **AC2** — When a spec's `- rev-2` entry is cut and `--finding 7/HIGH/local/FIX-dFix-2/FIX-dFix-2/2` runs,
  the header reading rev-3, it refuses printing `no Revision log entry at rev-2`.
  Red when: the header test alone stands, so a bump with no line passes.
- **AC3** — When specs stand at rev-1 with one log entry, `--finding 7/HIGH/local/FIX-dFix-2/FIX-dFix-2/1`
  refuses printing `rev-1 is a spec's first draft`, and so does `--sibling FIX-dFix-3@rev-1`.
  Red when: a claim of rev 1 passes, so the reproduction stands with one digit changed.
- **AC4** — When `--finding 7/MEDIUM/local/FIX-dFix-1/FIX-dFix-9/2` runs, it refuses printing
  `no tracked spec carries that id`. When `--finding 7/MEDIUM/new-mechanism/FIX-dFix-1/FIX-dFix-9/1` runs,
  it exits 0.
  Red when: a promoted unit owes a spec, or a minor's fold skips the join.
- **AC5** — When `--sibling FIX-dFix-3@rev-99` runs, it refuses printing `below the rev-99`, and
  `--sibling FIX-dFix-3@rev-3` exits 0.
  Red when: sibling rows skip the join.
- **AC6** — When a spec stands at rev-3, `--finding 7/HIGH/local/FIX-dFix-2/FIX-dFix-2/2` exits 0, because
  rev-2 is logged. It exits 0 at rev 3 with the entry spelled `**rev-3**`, with the spec in CRLF line
  endings, and under a `## Revision log` heading with no ordinal.
  Red when: the test is equality with the header, so a second fold reds the first, or the reader
  misses a shape the corpus writes.
- **AC7** — When a round carries a good `local` row beside one claiming rev 99, it refuses and the
  tracked record's bytes are unchanged. When the same call also carries a `--sibling` token outside its
  grammar, it prints `a --sibling is outside`. `grep -c 'fail 118' tools/unattended/unattended.sh` prints 1,
  and `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` prints the same figure
  before and after the pass.
  Red when: a row is written before the join, the join runs ahead of the grammar, or the join adds a
  `fail` site.
  figure: DERIVED. It reads 318 at `f055a11b`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a fork spent on builtin work)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the report's reproduction and a log gap, staged with `check_chain_fold` returning 0 at its head, which records both · none
New arm: tools/unattended/unattended.test.sh · covers AC3 · a rev-1 claim on a rev-1 spec, staged with the first-draft test cut, which records it · none
New arm: tools/unattended/unattended.test.sh · covers AC4 AC5 · an untracked unit, a promoted one and a sibling row, staged with the `folds` pair for `--sibling` unset, which records the false rev · none
New arm: tools/unattended/unattended.test.sh · covers AC6 · the green shapes, staged with the header test turned into equality, which refuses an older logged rev · none
New arm: tools/unattended/unattended.test.sh · covers AC7 · the record's bytes across a refusal, staged with the join moved below the write, which leaves a row behind · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the closing review's item H3, the promotion notes, and the
  design's [survive] 2.
- rev-2 · 2026-11-02 · §3 · §4 · §6 · Fixture R's conf declares `SPEC_FOLD_CUTOFF="2000-01-01"`, because
  `TOOL-dFoldedAudit-13` ships first and refuses these rows under a blank cutoff, and the list's edge
  is a `hands-off` to `TOOL-dFoldedAudit-15`, which writes that list. M2's cross-read: this spec's
  `folds` array and unit 13's scalar `folds` shared one name in one function, so §4 retypes the scalar.

## 10. Reuse audit

`reuse_lookup.py` on "read a spec header revision and its revision log entry" ranked `read_spec_revisions`
and `tools/memory-tree/design_lib.py`, which do not fit, because this kit copy-installs without the
memory-tree kit and the driver has no shell reader of a spec's rev: a grep over
`tools/unattended/unattended.sh` for a header rev or a Revision log found none. So this unit extends
`write_chain_round` (`tools/unattended/unattended.sh:13494`), `check_chain_fault`
(`tools/unattended/unattended.sh:13462`), `load_spec_facts` (`:4784`) and `drop_working_specs`
(`:4822`), and takes its grammar from `REV_ENTRY`. `tools/memory-tree/gotchas.py --for-paths` selected
`fixture-passes-by-finding-nothing`, which AC6's green shapes answer beside the refusals, and
`two-answers-to-one-question`, which is why the reader's table cites both grammars it copies. The
review's cites were re-read at `f055a11b` and held. The recall hits were the report itself and the
verbs entry, and neither disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit chain round joined to the review row and a fold joined to the spec revision" --terms "spec-audit chain round record-round terminal review row fold rev revision log forged"`
