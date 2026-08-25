# TOOL-dScaffoldedMirror-5 — the three RATCHETS rows and the delete-then-re-add repair

**Status:** WONTDO · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · S1 cut as specced-worthless; the S2-S4 repair re-files as a drift-audit unit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |

<!-- /gen:spec-records -->

## 1. Goal

`RATCHETS` at `drift_signals.py:264-276` holds eight rows and none of them is `.lexicon.conf`, while
that file hand-writes `RAISED 412 -> 415` in exactly the format `ratchet_findings` parses. The
convention is being followed and nothing reads it. Add the three rows, and close the hole underneath
them: `ratchet_findings` (`drift_report.py:198-221`) skips whenever either side is `None`, so a
ratcheted key that VANISHES passes silently and one that REAPPEARS passes silently. This unit is a
DOCUMENTATION ratchet, it does not answer the pressure demand, and `TOOL-dScaffoldedMirror-9`
deletes its three rows. All three of those facts are stated in §4 rather than discovered later.

## 2. Scope (IN)

- **S1** — three rows into gov's own `RATCHETS`: `VERB_OFFENDER_PIN`, `SUFFIX_OFFENDER_PIN` and
  `LAYER_OFFENDER_PIN`, all `{"file": ".lexicon.conf", "weakens": "up"}`. They land in
  `tools/drift-audit/drift_signals.py`, which is gov's own declaration, not in
  `drift_signals.template.py`, so no adopter receives a row for a kit they may not have.
- **S2** — the vanish arm. A `RATCHETS` row whose key is absent at HEAD while its FILE is present at
  HEAD is a finding, naming the key and the file. A row whose file is absent at HEAD stays skipped,
  because an adopter who never adopted the kit must not red.
- **S3** — the reappear arm. When the key is absent at the base and present at HEAD, the comparison
  operand is DERIVED rather than skipped: walk `git rev-list <base>..HEAD -- <file>` newest-first
  and take the key's value at the newest commit in that window where it was present. That value
  becomes `was`, and the existing weakening test and justification lookback run against it
  unchanged.
- **S4** — when S3 finds no such commit, the key is genuinely new in this window and the row reports
  that as its own line rather than as a pass. A seeded pin is a legitimate state; an unreported one
  is not.
- **S5** — three arms in `tools/drift-audit/selftest.py`, beside the existing `test_ratchet_guard`,
  `test_ratchet_lookback` and `test_ratchet_message_states_its_window`.

## 3. Non-goals (OUT)

- **No claim that this answers demand 2.** §4 prices the move it deters and the price is five
  minutes of prose. Reporting this unit as pressure would be the third time this kit's records
  claimed a mechanism it does not have.
- **No new pin, no pin change, no pin deletion.** `.lexicon.conf` keeps all three pins at their
  current values and this unit reads them; deleting them is `TOOL-dScaffoldedMirror-9`.
- **No compound-shape coverage.** `RATCHETS` stays scalars-only. `ARMS_FLOORS` and `CORE_FLOOR` keep
  their own one-sided checks, as the existing header already states, and the per-extension mode
  ratchet that needs a non-scalar shape is `TOOL-dScaffoldedMirror-6`.
- **No change to `RATCHET_LOOKBACK`.** It stays at the declared 14.
- **No waiver-count row.** `TOOL-dScaffoldedMirror-4` declares its own watermark row using this
  unit's mechanism; §4 states that edge.

## 4. Design

### What the three rows actually buy, priced

The pin's last move was 417 → 463, and it landed with three paragraphs of archaeology written
directly above it. Measured on this worktree: `.lexicon.conf`'s justification block runs from line
28 to line 90 and `VERB_OFFENDER_PIN` sits at line 91, so a `463 -> N` marker written where the
existing ones are written falls inside the 14-line lookback and satisfies `_justified` on the first
try. The guard converts a free move into a five-minute move. Against an LLM author, five minutes of
prose is a subroutine rather than a deterrent.

That is the whole value, and it is worth the three lines because the alternative is a convention
already being honoured that no machine reads. It is not pressure. The pressure design is
`TOOL-dScaffoldedMirror-9`, which deletes these three rows in its own commit and adds an assert that
every `RATCHETS` row names a key present in its file. This unit ships knowing it is temporary, and
that is a reason to keep it to three lines rather than a reason to skip it.

### The hole underneath, and the arm that is actually invisible today

`ratchet_findings` reads:

```python
now, at = _scalar_at(head_txt, key)
was, _ = _scalar_at(base.stdout, key)
if now is None or was is None or now == was:
    continue
```

Both `None` branches are silent passes. So delete-in-commit-1 and re-add-at-900-in-commit-2 is a
two-commit, zero-finding bypass of every one of the eight rows already declared.

For `VERB_OFFENDER_PIN` specifically, the first commit does not actually get away with it, and the
spec says so rather than letting a builder discover it: `lexicon.py:531-536` reads an absent pin as
the empty string and falls back to `pin = 0`, so with 463 unwaived offenders the lexicon leg reds on
the deletion commit. The bypass is blocked there by accident, not by the ratchet.

The arm that IS invisible today is the other two. `SUFFIX_OFFENDER_PIN` and `LAYER_OFFENDER_PIN` are
both `"0"` over populations of 0, so deleting either key changes nothing anywhere: `0 > 0` is false,
the lexicon leg stays green, `drift-audit` skips the row, and the key is simply gone. Re-adding it
at any value in a later commit is equally silent. **That is the failing case, it exists in the tree
today, and staging it is one line deleted from `.lexicon.conf`.** It is the better arm precisely
because nothing else in the repo catches it.

### The repair, derived rather than declared

S3 does not ask for a new marker spelling. Asking the author to write `absent -> 900` would put the
proof inside the same edit the guard is checking, which is the guard-shares-a-variable class.
Instead the operand is derived from git: the key's last value before it vanished is a fact about
commits already made, and no edit to the present tree changes it.

```
was is None and now is not None
  -> for sha in git rev-list <base>..HEAD -- <file>:        # newest first
         v = _scalar_at(git show <sha>:<file>, key)
         if v is not None: was = v; break
  -> if nothing found: report "key is new in this window at <now>"
```

Cost is one `git rev-list` plus at most one `git show` per commit in the window that touched the
file, in a branch that fires only when a ratcheted key is absent at the base. On this repo
`.lexicon.conf` is touched a handful of times per window.

`now is None` needs no derivation. A ratcheted key that is gone at HEAD is a finding on its face,
guarded only by the file's presence so that an adopter without the kit is not redded for not having
it. That guard is the same property `_resolve_lexicon_conf` establishes for the two lexicon signals:
an adopter without `.lexicon.conf` gets no raise and no red.

### Inventory

| row | file | key | today |
|---|---|---|---|
| new | `.lexicon.conf` | `VERB_OFFENDER_PIN` | `"463"`, at line 91 |
| new | `.lexicon.conf` | `SUFFIX_OFFENDER_PIN` | `"0"`, at line 92 |
| new | `.lexicon.conf` | `LAYER_OFFENDER_PIN` | `"0"`, at line 93 |
| existing | `.memory-tree.conf` | five pins | unchanged |
| existing | `drift_signals.py` | three PINS entries | unchanged |

The repair in S2, S3 and S4 applies to all eleven rows, not only the three this unit adds. That is
the larger half of the unit's value and it is why the repair is not deferred to `-9`.

**Two new edges, neither in the build's declared set.** `TOOL-dScaffoldedMirror-4` declares a fourth
`RATCHETS` row for its waiver-count watermark, and `TOOL-dScaffoldedMirror-6` declares a fifth for
its coverage floor with `weakens: "down"` — the first row in the list whose weakening direction is
downward. Both use this unit's mechanism, both are declared in their own units rather than here, and
both outlive this unit's three rows. Filing them here would put them inside `-9`'s deletion.

### Files touched (estimate)

`tools/drift-audit/drift_signals.py` (3 lines plus a comment naming their expiry),
`tools/drift-audit/drift_report.py` (~35 lines in `ratchet_findings`),
`tools/drift-audit/selftest.py` (the arms in §6). `.lexicon.conf` is READ and not edited.

### Alternatives rejected

- **Require a `<key> new <value>` marker on the reappear arm.** The proof would live in the same
  edit the guard checks. Derivation from git is the same cost and is not defeatable by the author.
- **Treat a vanished key as a tightening move and pass it.** A ratcheted key that is gone has no
  guarantee left to tighten, and this is exactly the reading that makes the two-commit bypass work.
- **Wait for `-9` and skip this unit.** The repair covers eight existing rows that `-9` does not
  touch, and `-9` is four phases away.

## 5. Production-readiness checklist

- **security** — N/A. No new input and no new write path; the added git reads are of the repo the
  checker already reads.
- **perf / scale** — the derivation in S3 fires only when a ratcheted key is absent at the base,
  which is rare by construction. Worst case is one `git rev-list` plus one `git show` per commit in
  the window that touched the named file. `drift-audit` is seconds-scale today and stays so.
- **a11y** — N/A, a CLI report.
- **i18n** — N/A.
- **error / empty / loading states** — the three states are now distinguishable and each has its own
  line: key present at both ends (compare), key absent at HEAD (finding), key absent at base
  (derive, or report as new). The fourth state — file absent at HEAD — stays a skip, deliberately.
- **observability** — S4 is the observability change: a seeded pin is reported rather than silently
  skipped, so a reader can tell "nothing moved" from "nothing was compared".
- **risks** — the honest risk is misreporting. Three rows landing in `RATCHETS` will read, in a
  landing report, as though the lexicon pins are now guarded against absorption. They are not; §4
  prices the move at five minutes. The mitigation is textual and it is in scope: the comment beside
  the three rows names their expiry and names `-9` as what replaces them.
- **testing + left-shift gates** — three arms in `tools/drift-audit/selftest.py` (§6). The class is
  `memory/gotchas/vacuous-selector-empty-population.md`: a comparison whose operand is `None` is a
  check with nothing to disagree with.
- **migration / rollback** — none. No persisted artifact changes shape; reverting removes three rows
  and restores the previous guard.
- **user docs** — the `RATCHETS` header block gains one paragraph on the two `None` branches, since
  that header is where an adopter reads what the mechanism does and does not cover.

## 6. Acceptance criteria

- **AC1** — When `SUFFIX_OFFENDER_PIN` is deleted from `.lexicon.conf` and nothing else changes,
  `python tools/drift-audit/drift_report.py` reports a finding naming that key. Today the same edit
  produces `lexicon OK` and a clean drift report; the arm is staged from this tree.
- **AC2** — When that key is deleted in one commit and re-added as `"900"` in a second,
  `python tools/drift-audit/drift_report.py` over the two-commit window reports a weakening move
  `0 -> 900` with no justification. This is the two-commit bypass and it is silent today.
- **AC3** — When `.lexicon.conf` is absent from the tree entirely, the three rows produce no finding
  and no error, so an adopter without the kit is not redded by gov's own declaration.
- **AC4** — When `VERB_OFFENDER_PIN` moves 463 → 470 with a `463 -> 470` marker within 14 lines
  above it, `python tools/drift-audit/drift_report.py` reports nothing; without the marker it
  reports the weakening move. Both arms in `tools/drift-audit/selftest.py`.
- **AC5** — When a `RATCHETS` key is newly introduced in the window with no prior value anywhere in
  it, the report carries a line naming the key and its seeded value rather than omitting it.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs after the change, `drift-audit selftest`
  and `drift-audit records` are green and the three lexicon legs are unchanged.

## 7. Gates

Keeps green: `drift-audit selftest`, `drift-audit records`, `drift-audit wiring`, and the three
lexicon legs `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, which this unit does
not touch. Adds no new gate leg — the three rows and the repair ride the existing `drift-audit
records` leg, and the arms ride `drift-audit selftest`. The leg count is not the coverage.

## 8. Open questions

- **F1 — should the vanish arm be a finding, or a hard refusal that exits non-zero?**
  `ratchet_findings` returns a list of findings and the caller decides; making this one special
  would give the module two severities where it has one. RECOMMENDATION: a finding, on the existing
  path. The row is already gateable by the `drift-audit records` leg's own rules, so a separate
  severity buys a second mechanism for the same outcome. RESOLVED (agent, 2026-08-24, delegated): a
  finding on the existing path, no new severity.
- **F2 — should these three rows carry an expiry marker a machine reads, since `-9` deletes them?**
  A machine-read expiry would need a date or a sha, and both are authored values that rot. `-9`'s
  own assert — that every `RATCHETS` row names a key present in its file — reds these three the
  moment `-9` deletes the pins, which is a derived expiry rather than a declared one.
  RECOMMENDATION: a comment naming `-9`, and rely on `-9`'s assert to do the enforcing. RESOLVED
  (agent, 2026-08-24, delegated): a prose comment naming `TOOL-dScaffoldedMirror-9`; the enforcement
  is that unit's assert, not a marker here.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R4 of the `dScaffoldedMirror`
  research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`) and on the
  read-only probe of `incms/main` taken the same day. One correction to R4 is recorded rather than
  folded silently: R4 states the delete-then-re-add bypass as uniformly silent, and it is not —
  deleting `VERB_OFFENDER_PIN` reds the lexicon leg immediately, because `lexicon.py:531-536` reads
  an absent pin as 0. The genuinely invisible arm is `SUFFIX_OFFENDER_PIN` and `LAYER_OFFENDER_PIN`,
  whose populations are 0, and §6 stages the failing case from those instead.
- rev-1 status 2026-08-24 · WONTDO as a unit. S1 (the three RATCHETS rows) is CUT: this spec prices its own product at five minutes of prose and states that `-9` deletes it, so building it is motion. S2-S4 (the delete-then-re-add repair) RE-FILE as a drift-audit unit - the mechanism covers eight existing rows in two other kits and has nothing to do with the lexicon - and the repair as written is a NO-OP that must be fixed first: its branch fires only when the key is absent at base, so walking base..HEAD newest-first returns `now` as `was`, and AC2 tests S1 instead of the repair.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py ratchet pin weakening justification scalar` returns
`ratchet_findings` (`tools/drift-audit/drift_report.py`, fan-in 1), the three existing arms
`test_ratchet_guard`, `test_ratchet_lookback` and `test_ratchet_message_states_its_window`
(`tools/drift-audit/selftest.py`), `parse_pin` (`tools/memory-tree/check-arms.py`, fan-in 1), and
the gotcha class `pin-copied-from-another-corpus.md`. The seam is `ratchet_findings` itself, and
this unit extends it in place rather than adding a sibling: a second function answering "did this
number weaken" would be two answers to one question, and the existing three arms already establish
the fixture shape a fourth and fifth extend. `parse_pin` is memory-tree's own reader for its arms
declaration and shares no grammar with `_scalar_at`. No new helper is introduced; the only new code
is a derivation branch inside the existing loop.
