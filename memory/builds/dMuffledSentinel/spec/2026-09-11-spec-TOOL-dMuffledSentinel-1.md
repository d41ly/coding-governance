# TOOL-dMuffledSentinel-1 — check 21 refuses a bindings parse that did not complete

**Status:** CLOSED · rev-2 · 2026-09-12 · node d · Tier-1 · base 75b85708 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-11-build-TOOL-dMuffledSentinel-1-1-acceptance-ledger.md](../build/2026-09-11-build-TOOL-dMuffledSentinel-1-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/check-memory-hygiene.sh` check 21 captured its delegate with
`2>/dev/null || true`, so a generator that could not answer produced an empty capture, and an empty
capture is what a clean corpus produces. Make the parse's failure a finding of check 21.

## 2. Scope (IN)

- **S1** Check 21 captures `--print-bindings` with its exit status, and fails naming the status and
  the delegate's last five lines when the status is non-zero. Observed by AC1 and AC4.
- **S2** A zero exit with no `N` row fails the same way. `--print-bindings` prints that row on every
  run, so its absence means the mode did not run. Observed by AC2.
- **S3** Two red arms in `tools/memory-tree/check-memory-hygiene.test.sh`, each over a copy of the kit
  whose generator is a stub, plus a green control on the healthy fixture. Observed by AC3 and AC5.
- **S4** `KIT_MEMORY_TREE_VERSION` moves to 2.69, since check 21 can now return a verdict it could
  not before. Observed by AC6.
- **S5** The class is catalogued as `swallowed-delegate-reads-as-clean`, and the rendered hygiene doc
  states the refusal. NOT OBSERVED by a criterion here: gotchas checks 17-19 and the kit/dogfood
  parity leg grade those two files' shape, and no criterion grades prose.

## 3. Non-goals (OUT)

- Not changing `--print-bindings` itself. It already exits 0 and always prints `N`, and S2 relies on
  exactly that.
- Not validating each row the parse prints. The branches select by kind letter and tab, and a stray
  line cannot become a finding.
- Not the adopter's generator. inCMS's fork gained the mode in inCMS, as `ARCH-dMuffledSentinel-1`.

## 4. Design

The engine already has a house pattern for delegates: checks 9, 13-16, 17-19 and 20 all fail on
their delegate's status. Check 21 is brought into line with that pattern rather than given a new one.

The `N` row is the liveness assertion. A non-zero exit alone misses a generator that reads an
unknown flag as its default mode and exits 0 having graded nothing. Requiring a row the real mode
always prints closes that without inspecting the rest of the output.

stderr joins the capture. On success, a stray warning line is inert, because every branch selects
rows by a leading kind letter and a tab. On failure, it is the only explanation available.

### Alternatives rejected

A test seam that lets the environment name the generator. The arms instead run a COPY of the kit with
a stub beside the engine, which is exactly how the adopter met the defect, and the engine gains no
knob that a caller could point at a different program.

## 6. Acceptance criteria

- **AC1** — When `gen_build_index.py --print-bindings` exits 2 beside the engine, check 21 reports
  `the bindings parse did not complete`, proved by the first stub arm in
  `tools/memory-tree/check-memory-hygiene.test.sh`.
  Red when: the capture swallows the status again and the fixture's no-Serves record goes unnamed.
- **AC2** — When the generator exits 0 without an `N` row, check 21 reports the same refusal, proved
  by the second stub arm.
  Red when: the liveness test reads only the exit status, so a no-op mode passes.
- **AC3** — When the real generator answers, the refusal is silent, proved by a `cnot` on the healthy
  fixture's run.
  Red when: the refusal fires on a completed parse, which would make every adopter red.
- **AC4** — When the engine at base `75b85708` runs the new suite, AC1's and AC2's arms FAIL, recorded
  as an observed break rather than asserted.
  Red when: the arms pass against the unfixed engine, meaning they never reached check 21.
- **AC5** — `python tools/memory-tree/check-arms.py --check` exits 0 and reports the new branch ARMED.
  Red when: the arm's literal drifts from the branch's own message and the branch reads as unarmed.
- **AC6** — When `bash tools/memory-tree/check-verdict-epoch.sh 75b85708` runs over the landed range,
  it reports clean at version 2.69.
  Red when: the engine's verdict moved in this range and the constant did not.

## 7. Gates

`memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `kit version markers`
`verdict epoch (kit version dates the engine)` · `kit/dogfood doc parity` · `memory hygiene`
`build README slot contract` · `codebase-map coverage + freshness` · `drift-audit records`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-11 · opened and built in one pass, from the inCMS measurement that found it.
- rev-2 · 2026-09-12 · §7 S5 · the full bar's findings on rev-1's records, all record-side: §7 named
  its legs by abbreviation and wrapped one across a line, so it contributed none; the README was not
  in the slot contract; S5's class was claimed by no dossier. Status CLOSED, landing with the merge.
