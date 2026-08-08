# Review 6 — adversarial pass over the U5 harness meta-gate

**Scope:** `tools/memory-tree/check-arms.py` as implemented, plus the arms added to
`tools/memory-tree/check-memory-hygiene.test.sh`.
**Order note:** this unit was built before its spec was written, because the design is a function of
a measurement — 14 `fail` branches behind 12 numbers, 0 armed — and the measurement needed the parser
that became the module. So this pass reviews CODE rather than a draft, which is stronger evidence.
The deviation is recorded in the sub-spec's §8 Fork B rather than tidied away.

| # | Severity | Where | Finding |
|---|---|---|---|
| K1 | blocker | `branches()` | a start-anchored pattern missed a whole branch, silently |
| K2 | high | `armed_signatures()` | a COMMENT naming the message armed the branch |
| K3 | high | the generator itself | a literal backspace byte reached the compiled regex three times |
| K4 | medium | `--emit-pin` | the measurement is the pin, and that is a loaded footgun |
| K5 | low | scope | the gate and test paths are hardcoded to one pair |

## K1 — the first pattern found 13 of 14 branches and said nothing (blocker)

`FAIL_RE` was anchored with `^\s*`. Check 9's call sits inside `if ! drift=$(…); then fail 9 "…`, so
it never matched, and the branch was invisible to the meta-check — the exact failure the meta-check
exists to prevent, arriving inside the meta-check itself. Nothing distinguished 13 from 14: both are
plausible counts, and the report printed a tidy table either way.

Fixed by searching the whole line, with the helper's own definition and comment lines skipped so the
`fail() {` line and the prose about branches are not counted as call sites. The unit then found 14,
including a message so short (`build index:`) that it tripped the no-assertable-run guard — which is
why check 9's message was reworded to `generated build index differs from a fresh render`.

## K2 — a comment describing an arm counted as the arm (high)

`armed_signatures()` returned every line of the test file except negative assertions. The test's own
prose quotes the messages it covers, so a comment saying "this arm would cover: …" armed the branch.
That is the same shape as the bare `check N` mention and the absence assertion the function already
refused — all three are "something in the file mentions it", which is not "something exercises it".

Comment lines are now skipped, and the case has its own arm.

## K3 — the same environment defect landed three times in one session (high)

Three separate regexes reached the interpreter with a literal `0x08` byte where `\b` was intended,
because the source was written through a shell heredoc into a NON-raw Python string. The symptoms
were all silent and all different:

| Where | Symptom |
|---|---|
| `extract.grammar_for` `ID_RE` | the citation scan returned zero ids while anchors kept working |
| `extract.grammar_for` anchor patterns | anchors matched, boundaries did not |
| `check-arms.FAIL_RE` | zero branches found, on a gate with fourteen |

Each looked like a logic bug and none was. A sweep over tracked AND untracked files found and
repaired the last one — the first sweep scanned tracked files only and reported zero, because the
module was not yet staged, which is the population-selected-too-narrowly class this build already has
a record for.

This belongs in the environment traps, not just in a commit message.

## K4 — `--emit-pin` writes the measurement, which is exactly what a pin must not be re-derived from (medium)

The pin's whole value is that it is a RECORD of a decision to leave a branch unarmed. `--emit-pin`
regenerates it from the current state, so a careless `--emit-pin > pin` after deleting an arm quietly
re-blesses the gap. It is still the right way to seed the file once, and it prints to stdout rather
than writing in place, so redirecting it is a deliberate act. Documented in the module rather than
removed, and the shrink-only rules make a silent re-bless visible on the next honest run: a pinned
branch that IS armed reds, so the only way to grow the pin is to also remove an arm — which trips
`ARMS_ARMED_FLOOR`.

## K5 — one gate, one test, hardcoded (low)

`main()` names `check-memory-hygiene.sh` and its test file directly. That is correct today — the kit
has one gate with `fail` branches — and it would silently cover nothing if a second gate appeared.
Recorded as a non-goal rather than solved, so the next person to add a gate sees the boundary.

## Disposition

K1 and K2 fixed in the implementation before it landed, each with its own arm. K3 repaired
tree-wide and folded into the kickoff manifest's environment traps plus a catalogue record. K4 and
K5 recorded — K4 in the module, K5 in the sub-spec's non-goals.
