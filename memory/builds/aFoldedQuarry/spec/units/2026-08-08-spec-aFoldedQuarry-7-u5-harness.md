# TOOL-aFoldedQuarry-7 — U5: the harness disciplines, made mechanical

**Status:** CLOSED · rev-1 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

## 1. Goal

Turn the transferable harness disciplines into a gate rather than advice: every `fail` branch in the
hygiene gate is either ARMED by a positive assertion naming its own failure text, or listed in a
shrink-only pin that makes its absence visible. Advice about test quality decays; a gate does not.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/check-arms.py` derives every `fail` call site from the gate's source and
  keys each on `(check number, ordinal within that number)`. Not on the label prose, which gets
  reworded; not on the check number, which is NOT unique — this gate has 14 branches behind 12
  numbers.
- **S2** — a branch is ARMED only by a POSITIVE assertion in the test file naming a literal slice of
  that branch's own message. Three things do not arm it: a bare `check N` mention, an ABSENCE
  assertion, and a COMMENT. All three are "something in the file mentions it", which is not
  "something exercises it".
- **S3** — unarmed branches are listed in `<MEMORY_ROOT>/project/unarmed-branches.txt`, keyed the same
  way and carrying the signature verbatim. The pin is shrink-only and reds three ways: a pinned
  branch that is now armed, a pinned branch that no longer exists, and a signature the message has
  been reworded out from under.
- **S4** — the pin is EXCLUDED from its own scan. It holds each signature verbatim in order to name
  it, so a scan that reached the pin would report every pinned branch as armed and the meta-check
  would ship vacuous. Upstream shipped exactly that.
- **S5** — PINNED IN BOTH DIRECTIONS. `ARMS_BRANCH_FLOOR` catches a deleted guard;
  `ARMS_ARMED_FLOOR` catches an assertion dropped by widening the pin — which a branch count alone
  cannot see, because the count falls and the pin still holds. Both measured, both one-sided upward.
- **S6** — a branch whose message carries no literal run long enough to assert on is a NAMED error,
  not a silent skip: an arm that cannot name its branch is not an arm.
- **S7** — the existing self-tests keep their batched-fixture shape and their `PASS`-printed-last
  discipline, and five branches gain real arms as part of this unit.

## 3. Non-goals (OUT)

- Arming all fourteen branches. The pin exists so the remaining nine are VISIBLE and shrink over
  time; writing nine fixtures in this unit would be the same work with none of the ratchet.
- Extending the meta-gate beyond `check-memory-hygiene.sh`. Its gate and test are named explicitly;
  a second pair is a follow-up when a second pair exists.
- Timing the fixture batching. The batched shape is already this kit's; the discipline is recorded,
  not re-measured.

## 4. Design

### Data model

```
branch  : (check-number, ordinal, source line, signature)
armed   : signature appears on a non-comment, non-negative line of the test file
pin row : check<TAB>ordinal<TAB>signature
floors  : ARMS_BRANCH_FLOOR (branch count) · ARMS_ARMED_FLOOR (armed count)
```

The signature is the longest literal run of the message after every shell interpolation is dropped.
An interpolation is a value, not text a test can assert on, and a short run like a colon appears in
every message and would arm every branch.

### Inventory

| Artifact | Role |
|---|---|
| `tools/memory-tree/check-arms.py` | the meta-gate, its report, its pin emitter, its self-test |
| `<MEMORY_ROOT>/project/unarmed-branches.txt` | the shrink-only pin |
| `ARMS_BRANCH_FLOOR` / `ARMS_ARMED_FLOOR` | the two measured floors |

### Migration

None. The pin is emitted from the current measurement by `--emit-pin`.

### Rollout

One commit: the module, the pin, the two floors, five new arms, the gate legs and the documentation.

### Files touched (estimate)

One new module, one new pin file, the hygiene gate's test, the conf, the gate-leg manifest.

### Alternatives rejected

- **Key the pin on the check number.** Rejected: 14 branches behind 12 numbers, so the cheapest arm
  would empty a number while its sibling branch stayed unwritten and invisible.
- **Count `fail` calls and compare to a floor, without a per-branch pin.** Rejected: it catches a
  deleted guard and nothing else. It cannot say WHICH branch is unarmed, so it cannot shrink.

## 5. Production-readiness checklist

- security — N/A. Reads two source files and a pin.
- perf / scale — two file reads.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a gate with no `fail` branch reports zero and the floors decide;
  a malformed pin row is a named error.
- observability — `--report` prints every branch with its line, signature and armed state.
- risks — the meta-gate could itself be vacuous, which is why S4 and the selftest's
  signature-only-in-the-pin arm exist.
- testing + left-shift gates — 12 self-test arms covering every red and green path.
- migration / rollback — one commit.
- user docs — `HYGIENE.template.md` and the kit README.

## 6. Acceptance criteria

- **AC1** — When two `fail` calls share a check number, they are two branches with distinct
  ordinals.
- **AC2** — When a branch has no arm and no pin row, `--check` fails naming the file, line, check
  number, ordinal and signature.
- **AC3** — When the only mention of a branch's message is a bare `check N`, an absence assertion, or
  a comment, the branch is NOT armed.
- **AC4** — When a pinned branch becomes armed, `--check` fails and asks for the row to be deleted.
- **AC5** — When a pinned branch no longer exists, or its message was reworded, `--check` fails.
- **AC6** — When a signature appears ONLY in the pin, it arms nothing.
- **AC7** — When a guard is deleted, `ARMS_BRANCH_FLOOR` fails; when an assertion is dropped by
  widening the pin, `ARMS_ARMED_FLOOR` fails. Both with the measured and the current number.
- **AC8** — When a branch message has no assertable literal run, `--check` fails naming it.
- **AC9** — When `python tools/memory-tree/check-arms.py --selftest` runs, every arm above has a red
  and a green side and the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh` in full, plus two new legs: `check-arms.py --check` and
`check-arms.py --selftest`.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — arm everything now, or pin and shrink?** RESOLVED (owner, 2026-08-08): pin and shrink.
  Nine fixtures written in one pass is the same work with none of the ratchet, and the pin is what
  makes the gap visible instead of assumed.
- **Fork B — the order this unit was built in.** RESOLVED (owner, 2026-08-08): the design was DERIVED
  from measuring the gate — 14 branches behind 12 numbers, 0 armed — so the module was written
  against that measurement and this spec records what it does. The adversarial pass ran against the
  IMPLEMENTATION rather than the draft, which is stronger evidence, and the deviation from the
  spec-then-review order is recorded here rather than hidden.

## 9. Revision log

- rev-1 · 2026-08-08 · written against the measured gate, then folded the adversarial pass over the
  implementation (review 6).

## 10. Reuse audit

The meta-gate reads the two files the kit already has and adds no parallel harness. The pin file
follows the shape of the kit's existing grandfather lists — `legacy-files.txt`, `curation-debt.txt`,
`id-orphan-waiver.txt`, `corpus-path-unresolved.txt` — down to the stale-entry guard all of them
carry, so a reader who understands one understands this. The floors follow the measured-pin
convention U3 established and the disabled-when-blank contract the whole kit uses. The legs register
in `tools/gate-legs.json`. Nothing here duplicates the gate's own `fail` protocol: it READS it.
