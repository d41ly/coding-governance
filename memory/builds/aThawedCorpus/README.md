---
slug: aThawedCorpus
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
ids: TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3
authorized-by: prompt
---

# aThawedCorpus — the memory tooling stops paying for a corpus that did not move

Node `a` · opened 2026-08-27 · streams tooling. The owner's prompt is at
[prompts/2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md](prompts/2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md),
verbatim, with what this run read out of it and what it declined to adopt.

## The problem this build exists to solve
Memory tooling re-reads the whole tree on every call, and the tree only grows: 71 builds, 823
tracked files, 1.9 MB. The `memory hygiene` leg carries `subject: repo` and therefore no guard, so
every node pays it on every bar. The recorded ledger figure is 421 s; measured on node `a`
2026-08-27 it is far worse, and the cost is NOT the walk. Checks 1 through the start of 21 cost 38 s
over that whole corpus. Check 21 alone then runs for minutes, because its filename-projection loop
spawns four to six processes for each of 310 records. The owner's mtime observation is true and
reproduced; what it implies is that no mtime-keyed cache can ever hit here.

## Expected improvements
- The dominant term in the memory bar's cost stops being process creation this repo controls.
- A bar that touches no memory file stops re-deriving a verdict nothing could have invalidated.
- Adopters inherit both, from the kit, without hand-fitting anything to their tree.
- The saving is stated as a declared wall-clock ceiling that REDS on breach, not as a claim.

## Detriments if this is not built
- An unguarded leg whose cost grows with the corpus, on every node, forever.
- The next agent that reaches for `--staged` to dodge it also drops the checks that catch the
  defects the leg exists to catch.
- Every adopter inherits the same curve the day their tree gets interesting.

## Build-level rules
- **Verdicts are byte-identical, and that is proven rather than argued.** Every unit's acceptance
  diffs the checker's full-corpus output against the pre-change checker. A performance change that
  moves a verdict is a defect, not a trade.
- **A cache miss costs wall clock and never a verdict.** Absent, corrupt, unreadable or
  version-mismatched skip state means RUN. This is the law `<git-dir>/gate-ledger.tsv` and
  `.githooks/pre-push`'s `gate-full-green` already run under, and it is not renegotiated here.
- **The key covers everything the verdict depends on, or the check is not keyed.** A checker whose
  answer depends on files other than the one in hand may not be skipped per file. Check 2 reds on a
  DELETED link target; check 21 and 23 read an id set defined elsewhere. Those are keyed on their
  whole input set or not at all — a guard that shares a variable with the thing it guards is not a
  guard.
- **Do not key on `CLOSED`.** Status is authored and can lie; content is derived and cannot. Keying
  on "unchanged" subsumes the owner's "fully closed" and also covers the idle-but-open build.
- **The kit stays standalone.** No `../lib/`, no `tools/run-gates/`. `resolve_python` is the
  precedent for what that costs and how it is paid.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aThawedCorpus-1` | 1 | check 21's filename projection stops spawning per record |
| 2 | `TOOL-aThawedCorpus-2` | 2 | a kit-local input-digest skip primitive, conf-declared, fail-open |
| 3 | `TOOL-aThawedCorpus-3` | 2 | wire it through the memory tools with a declared wall-clock ceiling |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aThawedCorpus-1 — hygiene check 21 stops spawning a process per record](spec/2026-08-27-spec-TOOL-aThawedCorpus-1.md) | 1 | 1 | OPEN | rev-1 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aThawedCorpus-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aThawedCorpus-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
