# TOOL-dLinkedLibrary-55 — the micro-format gate's selftest runs the gate alone at a prefix that holds no `lib/`

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 4 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-55-deviation-551.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-55-deviation-551.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 12 at HIGH**, report item **H1**. Ids 3 and 17 share the item, and each is its own unit:
id 3 is `TOOL-dLinkedLibrary-54`'s and id 17 is `TOOL-dLinkedLibrary-56`'s.

Id 12 is the grounding half of the item: `TOOL-dLinkedLibrary-43` grounded its re-point of
`tools/check-microformats.sh` in gov's own tree, and its AC5 and its §7 gate line observe nothing at
another prefix. No standing arm runs the shipped gate where `<prefix>/lib/` is absent, so a gate that
sources a file under `lib/` stays green in gov and fails in every adopter.

This unit adds that arm to the suite that ships with the gate, `tools/check-microformats.test.sh`: it
copies the gate alone into a scratch prefix holding no `lib/` and runs it over the suite's passing
fixture. It repairs `TOOL-dLinkedLibrary-43` and builds one step after it (order 4).

## 2. Scope (IN)

- **S1** — The arm. `tools/check-microformats.test.sh` gains one arm after its existing ones: it copies
  `$GATE` (:12) alone into `$TMP/pfx/kits/`, a directory holding no `lib/` at any depth above the copy
  inside `$TMP`, writes the suite's passing fixture into `$WORK` (:23) with `fixture` (:29), and runs
  `bash "$TMP/pfx/kits/check-microformats.sh" charter.md` from `$WORK`; it asserts exit 0 and counts one
  assertion through `say_ok` or `say_fail`. Observed by AC1 and AC2.
- **S2** — The arm discriminates. The same arm writes a second copy with one line, `.
  "$(dirname "$0")/lib/region.sh"`, inserted after `set -u`, runs it the same way, and asserts a non-zero
  exit, so an arm whose copy step stopped isolating the gate reds rather than passing. Observed by AC1.
- **S3** — The floor. `FLOOR_ASSERTIONS` (`tools/check-microformats.test.sh:143`) rises by the arm's two
  assertions. Observed by AC2.

## 3. Non-goals (OUT)

- The gate's own read: `TOOL-dLinkedLibrary-54`'s inline `region_sh` block (id 3).
- A class check over every shipped file that sources `lib/`: the `install-prefix (shipped surface)` leg's
  rule 3 already reads a kit segment under a derived base, and widening it is not this unit's.
- The suite's existing arms and their fixture: unchanged.

### Edges

- **hands-off** `TOOL-dLinkedLibrary-66` — S1's lib-less arm and S2's staged copy, which unit 66 re-stages as the stripped block and asserts at exit 2 (id 33 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — AC1, which unit 74 answers AMENDED in this unit's ledger (id 1 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/check-microformats.test.sh:12` finds the gate beside the suite, so at every prefix the arm
  copies the gate the install received.
- `tools/check-microformats.test.sh:23-26` builds one scratch repository reused by every arm, and
  `fixture` (:29-41) writes a charter the gate passes.
- `tools/govkit/entries/check-microformats.kit.toml:24-27` ships the suite beside the gate, so the arm
  runs in every adopter that holds the gate.

### Why a copy alone

The gate resolves its repository with `git rev-parse --show-toplevel` (`tools/check-microformats.sh:24`)
and runs from it, so a copy beside no `lib/` is the adopter's shape: the install holds the gate and its
suite, and nothing else from gov's tool root.

### Rollout

Same order as units 54 and 56, and disjoint from both: this unit writes only the suite. The arm reads
`tools/check-microformats.sh` when the suite runs, which no pass does; at the close the gate it copies
is the one unit 54 leaves, and the arm is green only if that unit carried its block inline. That is the
arm doing its work, not an ordering edge.

### Files touched (estimate)

- `tools/check-microformats.test.sh`: S1 to S3

### Alternatives rejected

- **A line on 43's §7 naming the foreign-prefix leg.** That leg runs every self-test at three prefixes
  with gov's whole tool root present, `lib/` included, so naming it observes nothing new.
- **Asserting the gate's text carries no `lib/`.** A grep passes a gate that reads a sibling file by a
  name built at run time; running the copy observes the behaviour.

## 5. Production-readiness checklist

- security — the arm writes under the suite's own `mktemp -d` scratch, removed by its trap (:13).
- perf / scale — one copy and two gate runs over the fixture already written.
- error / empty / loading states — a copy that cannot be made fails the arm naming the step.
- observability — the arm prints `arm ok` or `arm FAIL` with the exit it saw, as every arm does.
- risks — the arm reds in gov until unit 54 lands; both are order 4, and the close runs after both.
- testing — AC1 and AC2 by probe; the arm itself is the close's.
- migration — none.
- user docs — none under `help/`: the suite's header names its arms.

## 6. Acceptance criteria

- **AC1** — When the arm's two runs are reproduced by hand in a scratch git repository under `%TEMP%/mf55`
  holding the suite's passing fixture as `charter.md`, with the gate's bytes at base `5fede642` (`git show`
  of `check-microformats.sh` at that commit) copied alone into the prefix `pfx/kits`, and `bash` running
  that copy from the repository's root with `charter.md` as its one argument, it exits 0; with the line
  `. "$(dirname "$0")/lib/region.sh"` inserted after `set -u` in that copy, it exits non-zero.
  Red when: a gate that sources a sibling `lib/` file still exits 0 at a lib-less prefix.
- **AC2** — When `grep -n "pfx/kits" tools/check-microformats.test.sh` and `grep -n "^FLOOR_ASSERTIONS="
  tools/check-microformats.test.sh` run at this pass's tip, the first prints the arm's copy line and the
  second the raised floor.
  Red when: the arm is absent, or the floor does not count its two assertions.
  figure: DERIVED at the pass, the floor at base plus 2.

## 7. Gates

`micro-format gate selftest` · `micro-format definitions` · `foreign-prefix parity (every self-test at three prefixes)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-microformats.test.sh · covers AC1 AC2 · the gate copied alone to a lib-less prefix, the failing case staged by a gate that sources a sibling lib/region.sh · FLOOR_ASSERTIONS raised by 2

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 12 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-66, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is the suite's own `arm` harness and its one reused scratch repository
(`tools/check-microformats.test.sh:23-63`); the arm adds a run, not a harness. `python
tools/codebase-map/reuse_lookup.py "copy-installed kit carries a shared shell function inline under a
parity row"` ranked `rows`, `row`, `resolve_kit_dir` and `kit_rel`, none a lib-less install probe, so no
existing seam fits beyond the suite being extended.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
