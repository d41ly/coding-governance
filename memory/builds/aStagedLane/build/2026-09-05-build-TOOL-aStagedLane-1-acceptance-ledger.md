**Serves:** journal TOOL-aStagedLane-1

# Acceptance ledger — TOOL-aStagedLane-1, the widened pass-order leg

**Evidences:** TOOL-aStagedLane-1

Every arm named below is in `tools/unattended/check-pass-order.test.sh`, which reports
`72 arms, exit 0`. Each fixture builds a real repository with real commits, because the subject is
COMMIT ORDER and a fixture that fakes the history proves nothing about a check that reads it.

- **AC1** — `bash tools/unattended/check-pass-order.test.sh`, arm *"no RUN.md, build BEFORE spec: the
  leg REDS"* — exits 1 and names `ARCH-tOrder-1`. RED observed before the code that greens it: the
  arm was written against the unwidened leg, where the build was skipped entirely.
- **AC2** — `graded 1 closed unit` — same suite, arm *"no RUN.md, spec BEFORE build: the leg is green"* — exits 0 and the unit
  appears in `graded 1 closed unit`. The matched passing case, without which the refusal could not be
  told from a leg that reds on everything.
- **AC3** — `bash tools/unattended/check-pass-order.sh` — same suite, arm *"liveness: the run-state-free population is counted by name"*, plus
  `bash tools/unattended/check-pass-order.sh` over the real tree, whose line reads
  `3 build(s) graded with no run-state file` — non-zero, and named rather than counted.
- **AC4** — the suite reports `72 arms, exit 0`, against 19 before this unit.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh --checks`. The ceiling is re-declared in
  both carriers from measurement: `BUDGET_pass_order_history=1800` carries its readings inline, and
  the `pass-order history` row of `tools/gate-legs.json` is 2400. **Stated rather than claimed
  clean:** the readings (804 s, 889 s, 1141 s on node `a`) were all taken UNDER LOAD, and that file's
  own header says this figure should be calibrated IDLE. No idle box was available. The line says so
  and records that an idle re-declaration is owed.
- **AC6** — arm *"working-tree `opened:` back-date does NOT exempt the build"*, with its control arm
  immediately above it proving the same fixture reds before the working copy is touched.
- **AC7** — `1 pre-anchor violation(s)` — arm *"pre-anchor build commit: the leg REDS"* — the fixture puts product code before the
  build folder exists, and the leg exits 1 reporting `1 pre-anchor violation(s)` rather than folding
  it into `unbuilt-in-range`.
- **AC8** — `bash tools/unattended/check-pass-order.test.sh` — arm *"violation AT the folder's first commit: the leg REDS"* — the boundary an exclusive
  range anchor drops.
- **AC9** — `bash tools/unattended/check-pass-order.test.sh` — arm *"garbage RUN.md base: still graded, and the violation still REDS"*.
- **AC10** — arm *"COMMITTED `opened:` back-date still exempts — the declared residual"*. This
  criterion PASSES BY EXITING 0, and that is deliberate: it proves the residual S6 declares is real
  rather than theoretical. The leg's header states it.
- **AC11** — `with no pinned run BASE` — arm *"liveness: the retired skip count is GONE, not pinned at zero"*, asserting the
  string `with no pinned run BASE` is absent from the output.
- **AC12** — `SHARED_RECORDS` — arm *"pre-anchor RECORD-only commit: green, because the exclusion still applies"* — a
  commit touching only a `SHARED_RECORDS` path and naming the id is NOT reported.
- **AC13** — `PASS_ORDER_PREANCHOR_CAP=1` — arm *"pre-anchor cap: the truncation is COUNTED"*, driven by declaring
  `PASS_ORDER_PREANCHOR_CAP=1` rather than by building a 400-commit fixture.
- **AC14** — `bash tools/unattended/check-pass-order.sh --preview` over the real tree printed exactly
  two violations, `DEPL-dGaugedVintage-12` and `-13`, which is exactly the set
  `memory/project/pass-order-waiver.txt` declares. The wired leg then exits 0 reporting
  `2 waived by memory/project/pass-order-waiver.txt`.
- **AC15** — `bash tools/unattended/check-pass-order.test.sh` — arm *"STALE waiver row: REDS"*, plus its multi-row sibling. The stale row is named.
- **AC16** — `bash tools/unattended/check-pass-order.test.sh` — arm *"violation at the PARENT of the folder's first commit: the leg REDS"*.
- **AC17** — arm *"no CLOSED unit: exits 0"* with `graded 0 closed unit`.
- **AC18** — `bash tools/memory-tree/check-memory-hygiene.sh` accepts
  `memory/project/pass-order-waiver.txt`, which required `.memory-tree.conf` to declare it in
  `PROJECT_REGISTRY_EXTRA`; the run prints
  `memory-hygiene: project key PROJECT_REGISTRY_EXTRA='pass-order-waiver.txt'`.

## What this ledger does not claim

The leg measures ORDER and nothing else — not whether a spec was good, reviewed, or followed. The
COMMITTED `opened:` value is still authored by the graded run; S6 narrowed the lever and did not
close the class, and AC10 exists to keep that honest rather than to hide it.

**And the arms were not enough, twice.** The closing diff review found a blocker these arms could not
see: the reads that select WHICH builds are graded still came from the working tree and then from the
index, while the record reads had moved to the graded commit. The arms mutate file CONTENT with
`sed -i`, which leaves the path in the index and never reaches the selector — so the fix's own arms
were structurally blind to the fix's own gap. The arms that cover it now use `git rm --cached`, and
that is the honest reading of this ledger: the suite passing is necessary and was not sufficient.
