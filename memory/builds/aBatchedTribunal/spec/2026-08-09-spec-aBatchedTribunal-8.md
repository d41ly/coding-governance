# TOOL-aBatchedTribunal-8 — W6: the epoch gate's endpoint hole, and the trade measured

**Status:** CLOSED · rev-1 · 2026-08-09 · node a · Tier-2 · base 3ed99a33 · streams tooling

## 1. Goal

Close `TOOL-aBatchedTribunal-7`. `check-verdict-epoch.sh` compared `KIT_MEMORY_TREE_VERSION` at the
two ENDPOINTS of a range, which is satisfied by a bump ANYWHERE in it — so one early bump excused
every verdict change after it. The row also said the per-commit alternative was "stricter but
noisier, and the trade is unmeasured". Measuring it is half this unit.

## 2. Scope (IN)

- **S1** — the hole is REPRODUCED before it is fixed: `base(1.5)` → `bump + change(1.6)` →
  `later change, no bump` read `clean — the version moved 1.5 -> 1.6`.
- **S2** — the trade is MEASURED on this repo's own history, not argued. 129 commits; 22 move a
  behaviour-bearing line of the engine or its delegates; 7 bumps actually happened. A per-commit rule
  would demand 22 — three times the churn — and a constant that increments on a fifth of all commits
  stops meaning "the verdict epoch" and starts meaning "someone edited the file".
- **S3** — so the rule is TOPOLOGICAL, not per-commit: let W be the newest commit in the range that
  moves a behaviour-bearing engine line, and S the newest that actually changes the constant's VALUE;
  W must be an ancestor of, or equal to, S. One bump per range, correctly PLACED.
- **S3b** — that is `skills/session-kickoff/manifest-check.sh` check 5's rule verbatim, applied to a
  different constant. It is here because it is proven in this repo, not because it is new.
- **S4** — S is VALIDATED against its parent rather than matched. Rewording the comment ON the
  constant's line moves that line without dating anything, and an unvalidated candidate would let a
  reflow launder every later verdict change — the same structural lesson manifest-check learned about
  its own stamp.
- **S5** — W is the newest BEHAVIOUR-bearing commit, not the newest touching one, so a trailing
  comment-only commit cannot re-open a range that was correctly dated.
- **S6** — the topological rule SUBSUMES the endpoint rule: when the endpoints are equal there is no
  qualifying S in the range, so the gate fails. Two rules are not kept where one answers.
- **S7** — the "no bump at all" case gets its own message. "You never dated this" and "you dated it
  too early" are different mistakes and a single sentence for both is a worse remedy.

## 3. Non-goals (OUT)

- A per-commit rule. Measured and rejected in S2. The row asked for the measurement, and the
  measurement is what decides it.
- Widening the scanned set beyond the engine and its three delegates. The delegates were added by the
  W4 review because 8 of the 19 verdicts come from them; under a topological rule their inclusion
  costs no extra bumps, only a later W.
- Making `hygiene-parity.test.sh` consume W and S directly. It derives its floor from the constant,
  and the point of this unit is that the constant can now be trusted to date the change.

## 4. Design

### Data model

```
SCAN : check-memory-hygiene.sh + gen_build_index.py + corpus_ids.py + gotchas.py
W    : newest commit in <base>..HEAD whose diff over SCAN has a non-comment, non-blank +/- line
S    : newest commit in <base>..HEAD where the PARSED value of the constant differs from its parent
rule : S must exist, and W must be an ancestor of S or equal to it
```

### Inventory

| File | Change |
|---|---|
| `tools/memory-tree/check-verdict-epoch.sh` | endpoint comparison → topological W/S rule; `-S` → `-G`; per-commit behaviour counter |
| `tools/memory-tree/check-verdict-epoch.test.sh` | 8 new arms: the hole, the bundle, the re-bump, no-bump-at-all, the decoy, the trailing comment, the delegate |
| `memory/backlog/TOOL.md` · `memory/DECISIONS.md` | the row closes; the measurement is recorded |

### Alternatives rejected

- **Per-commit.** 22 demanded bumps against 7 real ones. Rejected on the measurement the row asked
  for.
- **Keeping the endpoint check alongside the topological one.** Rejected: the topological rule fails
  every case the endpoint rule fails, so a second check is a second answer to one question.
- **A dedicated `VERDICT_EPOCH` constant.** Already rejected in W4 and unchanged here: it is the bump
  plus one more literal to keep honest.

## 5. Production-readiness checklist

- security — N/A; the gate reads git history.
- perf / scale — one `git diff-tree` per touching commit until the first behaviour-bearing one, and
  one `git show` per bump candidate. Both walks stop at the first hit.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty range, a missing engine, an unresolvable base, a bogus
  base and an unparseable constant are each a distinct NAMED outcome.
- observability — the failure prints W and S by sha, so the remedy is "bump at or after W" rather
  than "bump somewhere".
- risks — the gate now fails a range whose bump is mis-ordered, which is a state that used to pass.
  That is the point, and the remedy is the same three-file bump.
- migration / rollback — one commit; no data, no schema.
- user docs — the gate's own header carries the reproduction and the measurement.

## 6. Acceptance criteria

- **AC1** — When a bump is BUNDLED with the last behaviour change (W == S), the gate is clean.
- **AC2** — When a behaviour change lands AFTER the bump, the gate fails naming both shas.
- **AC3** — When the bump is then re-applied after that change, the gate clears.
- **AC4** — When the range has a behaviour change and NO bump, the message says so, distinctly from
  AC2's.
- **AC5** — When the constant's LINE moves without its VALUE, that commit is not counted as a bump.
- **AC6** — When a comment-only commit lands after a correct bump, the range stays clean.
- **AC7** — When a DELEGATE changes after the bump, the gate fails — the delegates are in the
  population, not just in the comment.
- **AC8** — When the full bar runs, it is green.

## 7. Gates

`bash tools/run-gates.sh`; the `verdict epoch` and `verdict-epoch self-test` legs carry this unit.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-09 · reproduced the hole, measured the per-commit trade (22 vs 7 over 129 commits),
  and took the manifest ratchet's topological rule rather than either alternative. One defect found
  while building: `git log -S` counts OCCURRENCES, and the constant's name occurs once before and
  once after any bump, so the count never moves and the first cut found no bump at all — `-G` matches
  changed lines, which is what a bump is, and is what manifest-check already uses on its own stamp.

## 10. Reuse audit

The rule, the validation-against-parent, and the ancestor test are `manifest-check.sh` check 5's,
read across to a different constant — including its `-G`-not-`-S` lesson, which this unit re-learned
the hard way before going to look. The gate keeps its existing comment-exemption, its delegate list
and its named misconfiguration exits from W4. The arms extend the harness written in W4 rather than
starting a second one, and use its `engine`/`newrepo` helpers with one addition, `commit_engine`,
which is those two plus the commit they were always followed by.
