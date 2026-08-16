# Review 7 — closing adversarial pass over the whole build diff

**Serves:** diff-review TOOL-aFoldedQuarry-1 TOOL-aFoldedQuarry-2 TOOL-aFoldedQuarry-3 TOOL-aFoldedQuarry-4 TOOL-aFoldedQuarry-5 TOOL-aFoldedQuarry-6 TOOL-aFoldedQuarry-7  <!-- inferred: closing pass over the whole build diff -->

**Scope:** `42c3f4dc..HEAD` — 140 files, +6404 / -584, six units.
**Method:** the build's own tool first. `python tools/memory-tree/gotchas.py --for-diff 42c3f4dc..HEAD`
selected six anchored classes plus three universal ones out of nine, and each was walked against the
diff rather than nodded at. That is the first time the checklist has been used on a real diff, and it
is the acceptance evidence for U4 as much as the selftest is.

| # | Severity | Where | Finding | State |
|---|---|---|---|---|
| L1 | high | `gotchas.append_only_re` | a sibling's `Problem` is a DIFFERENT class, so a hygiene gate emitted a traceback | fixed |
| L2 | medium | `corpus_ids.ask_shell` | a bash that cannot be LAUNCHED raises before any return code exists | fixed |
| L3 | medium | `check-arms` | a missing gate or test file was a traceback, not a named error | fixed |
| L4 | low | `check-arms` scope | one gate/test pair, named explicitly | recorded |
| L5 | low | `--staged` coverage | checks 13-19 do not run in the pre-commit fast leg | by design, stated |

## L1 — two classes with one name are two classes (high)

`gotchas.py` calls into `corpus_ids.py` for the append-only classification, which is the right
arrangement: one owner per fact. But `corpus_ids` raises ITS OWN `Problem`, and `gotchas.do_check`'s
`except Problem` catches only its own. Reproduced by pointing `GOV_BASH` at a path that does not
exist: the hygiene gate printed a `subprocess` stack ending in `WinError 2`.

A traceback out of a gate is the worst possible failure output — it buries the finding, it looks like
a broken tool rather than a broken tree, and it trains people to ignore the gate. Every failure
crossing that boundary is now re-raised as this module's `Problem`, with an arm that sets `GOV_BASH`
to a non-existent path and asserts the named message.

## L2 — the launch failure happens before the return code (medium)

`ask_shell` checked `out.returncode`, which presumes a process started. `subprocess` raises `OSError`
when the executable cannot be launched at all, so the check never ran. Now caught and named, pointing
at `GOV_BASH` as the remedy — which is the same class as L1 one layer down, and was found by the same
probe.

## L3 — the meta-gate's own inputs were unguarded (medium)

`check-arms.py` reads the gate's source and its test file by path. Either missing produced a
`FileNotFoundError` from `read()`. The test-file case is the more interesting one: with no test file
every branch reads as unarmed, which IS loud — but a missing harness is its own finding and deserves
its own sentence rather than fourteen derived ones. Both are named errors now, each with an arm.

## L4 — one gate, one test, by name (low)

`check-arms.py` names `check-memory-hygiene.sh` and its test directly. Correct today; a second gate
with `fail` branches would be silently uncovered. Recorded as a non-goal in the sub-spec and as
`TOOL-aFoldedQuarry-8` in the backlog rather than solved speculatively.

## L5 — checks 13-19 are full-mode only (low, by design)

The three delegated modules run only when `STAGED = 0`. They are tree-wide classifications — an id
corpus, a path corpus, a catalogue — and running them against a staged subset would answer a
different question than the one they were built for. The pre-commit fast leg therefore covers checks
1-12; the full bar at the push boundary covers all nineteen. That matches the kit's stated
gate-economy rule rather than contradicting it.

## What the checklist caught that reading would not have

The `--for-diff` run put `two-answers-to-one-question` and `fixture-passes-by-finding-nothing` at the
top of the list for a diff that is largely about single-sourcing facts and arming branches. Walking
those two deliberately is what surfaced L1: the append-only classification has ONE owner, and the
mechanism for asking it had a second failure vocabulary. The class named the defect before the code
was read.

## Verification after the fixes

`bash tools/run-gates.sh` — 27/27 legs green, 1 skipped as unchanged. Every module's selftest re-run
individually. The whole bar is green at the push boundary, which is where this repo's rule puts it.
