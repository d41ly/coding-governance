# The closing review's fold — sixteen findings, three shapes, and what each one cost

**Serves:** journal TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

The M8 closing review returned BLOCKED: 27 raw findings, 21 confirmed, 6 refuted, precision 0.78,
resolving to 16 distinct defects — one BLOCKER, eight HIGH, five MEDIUM, two LOW. Every one of them
was in code this build wrote. The report is
[the cumulative review](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-cumulative.md).

## What the shapes were

Three shapes carried thirteen of the sixteen, which is the finding behind the findings:

1. **A gate that reports a violation and exits 0** — B1, H1, M2. A check can be completely correct
   about what it found and still be worth nothing, because the only thing anybody reads is the exit
   code. B1 is the sharpest: `check-memory-hygiene.sh` called a bare `GIT` this file never defines,
   inherited by eye from `check-unattended.sh` where it does. On Windows that resolves to `git.exe`
   because PATH lookup is case-insensitive. On any case-sensitive host both substitutions return
   nothing, the population is empty, and check 22 prints *"measured NO unit"* and passes. A check
   that announces its own vacuity as a legitimate empty is worse than one that is simply absent.
2. **An id compared as a substring** — H3, H4. `TOOL-dUnstalledConvoy-1` is a prefix of
   `TOOL-dUnstalledConvoy-10`, and this build minted both. Five id tests were written by hand in one
   sitting and three were unanchored. Every one fails OPEN.
3. **A containment test with the wrong relation** — H5, H6, H8, M3. `--writes memory` was accepted
   by a guard that refuses `--writes memory/DECISIONS.md`, because `memory` is not *under* the record
   it contains. The widest possible declaration passed every refusal in the verb.

## What was done about each

| Finding | Fix | Where |
|---|---|---|
| B1 | bare `GIT` → `git`, and the LISTING routed through `pop_guard` so an empty one reds | `tools/memory-tree/check-memory-hygiene.sh` |
| H1 | `\| while` → `for`; `fail` now runs in the parent | `tools/unattended/check-unattended.sh` |
| H2 | check 23 grades the LAST row per (group, unit) — the widening repair supersedes | `tools/unattended/check-unattended.sh` |
| H3, H4 | `id_rows`/`id_in`, anchored once, used at every site | `tools/unattended/check-unattended.sh` |
| H5, H6, M3 | `covers`/`overlaps`, and every path relation routed through them | `tools/unattended/unattended.sh` |
| H7 | the witness is the commit the TAKEN arm validated, not HEAD by default | `tools/unattended/unattended.sh` |
| H8 | the sibling set is every pass that has not COMMITTED, not the rows sharing this HEAD | `tools/unattended/unattended.sh` |
| M1 | a glob metacharacter in `--writes` is refused | `tools/unattended/unattended.sh` |
| M2 | folded into B1 — the empty population reds rather than printing | `tools/memory-tree/check-memory-hygiene.sh` |
| M4 | both keys shipped, and the parity arm's population DERIVED from the engine's reads | `tools/memory-tree/.memory-tree.conf.example` |
| M5 | the flattener accepts the bold `AC` form the spec-side extractor accepts | `tools/memory-tree/check-memory-hygiene.sh` |
| L1 | `SHARED_RECORDS`'s default resolved AFTER the conf, via a sentinel | `tools/unattended/unattended.sh` |
| L2 | the refusal names `--pass`, which is the flag that exists | `tools/unattended/unattended.sh` |

## The left-shift, which is the part that matters

Fixing sixteen instances buys nothing if the seventeenth is written next week. Three classes went
into `memory/gotchas/`, so `gotchas.py --for-diff` hands them to the next reviewer of these files:

- [`status-set-in-a-subshell`](../../../gotchas/status-set-in-a-subshell.md)
- [`id-matched-as-a-substring`](../../../gotchas/id-matched-as-a-substring.md)
- [`containment-tested-one-way`](../../../gotchas/containment-tested-one-way.md)

And two gates were widened rather than merely satisfied:

- The example-conf parity arm now derives its population from every `${NAME:-}` the engine reads,
  minus the names the engine assigns itself, minus a DECLARED exemption asserted in both directions.
  Run over the real tree before wiring, it surfaced two names the original symptom never reached
  (`GOV_PYTHON`, `MAP_ROOT`) — both correctly exempt, both now documented as to why. Observed RED on
  a staged break before being trusted.
- Eleven arms were added across the two suites, each pinning a case the shipped code ADMITTED.

## What this fold did not do

It did not re-run the full adversarial fan. M8 asks for a re-review of the FIX, not of the diff
again, and the fix was re-reviewed by exercising it: the dedup on synthetic rows, the new refusals
against a live fixture repo, the parity arm against a staged break. Reading the code a second time
would have been the cheaper thing and the less honest one.

It also did not touch the six refuted findings. They stay refuted and the report keeps its reasoning.
