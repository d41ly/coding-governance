# TOOL-dLinkedLibrary-65 — the micro-format gate refuses by name when its inline region reader is absent

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 5 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |
| [2026-10-27-build-TOOL-dLinkedLibrary-65-deviation-651.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-65-deviation-651.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-74 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
finding **id 24 at HIGH**, report item **H1**. Id 33 shares the item and is its own unit,
`TOOL-dLinkedLibrary-66`. Item M1 (ids 1 and 34) is the same defect at medium, batched in
`TOOL-dLinkedLibrary-74`.

`TOOL-dLinkedLibrary-54` AC3 stages the red half of its lib-less check by inserting `.
"$(dirname "$0")/lib/region.sh"` after `set -u`. The gate runs `set -u` with no `set -e`
(`tools/check-microformats.sh:23`), so a failed `.` prints an error and the script carries on, and 54's
inline `region_sh` block still defines `region`: the staged copy exits 0, as the audit reproduced. The
break that matters is the one `TOOL-dLinkedLibrary-43` would ship, the inline block absent and a source
line in its place. Under it `region` is undefined, and 54's read (`block=$(region …) || { …; exit 2; }`,
54 §4) exits 2 saying the fence pair is not one open above one close, which names the wrong cause.

This unit has the gate check that its reader is defined before it reads, and refuse naming the absent
block, so 54's isolation is observed on the real break. It repairs `TOOL-dLinkedLibrary-54` and builds
one step after it (order 5).

## 2. Scope (IN)

- **S1** — The guard. Below its `# <<< region_sh` marker and above the read, `tools/check-microformats.sh`
  runs `declare -F region >/dev/null || { echo "check-microformats: the inline region_sh block is absent,
  so this gate has no region reader, and the gov library directory never ships with it"; exit 2; }`. The
  line names no path under the library directory. Observed by AC1 and AC2.
- **S2** — The staged break. The red case of the gate's isolation is a copy holding, where the lines
  from `# >>> region_sh` to `# <<< region_sh` stood, only the line `. "$(dirname "$0")/lib/region.sh"`. At a prefix holding no library directory that copy exits 2 printing S1's line; beside a
  copy of the canonical `region.sh` in that directory it exits 0. Observed by AC2.

## 3. Non-goals (OUT)

- The standing arm that runs this break in the suite that ships with the gate:
  `TOOL-dLinkedLibrary-66` (id 33).
- Unit 54's acceptance ledger answer for its AC3: `TOOL-dLinkedLibrary-74`'s item for id 34.
- `set -e`: unchanged. It would turn every unguarded failing command into an exit the gate's exit table
  (:22) does not name.
- The `region_sh` block's body: `TOOL-dLinkedLibrary-18`'s, carried by 54 unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-54` — S1's inline `region_sh` block and AC3's staged break, which S1 guards and S2 re-stages as the stripped block (id 24)
- **hands-off** `TOOL-dLinkedLibrary-74` — the guard's `region_sh` line, which unit 74 records in unit 54's ledger (id 34 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `tools/check-microformats.sh:22-23`: "Exit 0 = every definition satisfies the grammar · 1 = an
  offender · 2 = could not run", then `set -u`; the file sets no `-e` and no `-o`.
- `tools/unattended/check-unattended.sh:211-216`: the `region` body the factory carries defines one
  function, `region`, so `declare -F region` answers exactly whether the block ran.
- The audit's reproduction (finding id 33): the base gate copied to a lib-less prefix with the source line
  inserted printed `No such file or directory`, then `microformats OK`, rc 0.

### The read after S1

```bash
# <<< region_sh
declare -F region >/dev/null || {
  echo "check-microformats: the inline region_sh block is absent, so this gate has no region reader, and the gov library directory never ships with it"; exit 2; }
block=$(region "$FILE" "$OPEN" "$CLOSE") || {
  echo "check-microformats: the fence pair in $FILE is not one open above one close"; exit 2; }
```

### Files touched (estimate)

- `tools/check-microformats.sh`: S1

### Alternatives rejected

- **`. "$(dirname "$0")/lib/region.sh" || exit 2` as the staged line.** It exits 2 too, but it names
  nothing and S2 would then stage a line the shipped gate must never hold.
- **Keeping 54's inserted source line as the break.** It exits 0 on a correct gate, so the criterion
  is red on every correct build.

## 5. Production-readiness checklist

- security — read-only gate; the guard runs before any line of the charter is graded.
- perf / scale — one builtin call.
- error / empty / loading states — an absent reader exits 2 naming the block, never a misleading pair
  message and never a clean set.
- observability — the refusal line names `region_sh`.
- risks — none beyond 54's: the guard reads only a function the block defines.
- testing — AC1 and AC2 by probe and a scratch install.
- migration — none: an adopter receives the guard on update.
- user docs — none under `help/`: the gate's header states its exits.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'declare -F region' tools/check-microformats.sh` and `grep -n '^# <<< region_sh'
  tools/check-microformats.sh` run at this pass's tip, each prints one line, the guard's number the
  greater.
  Red when: the guard is absent, or sits above the block it tests.
- **AC2** — When the gate at this pass's tip is copied alone to the prefix `gov` of a scratch git
  repository under `%TEMP%/mf65` holding `coding-governance-agents.template.md`, and `bash` runs that copy
  from the repository's root: the copy as shipped exits 0; S2's stripped copy exits 2 and prints `region_sh
  block is absent`; and the stripped copy with the canonical `region.sh` placed in the prefix's library
  directory exits 0.
  Red when: the stripped copy exits 0 at a lib-less prefix, or exits 2 with another cause.

## 7. Gates

`micro-format definitions` · `micro-format gate selftest` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: `TOOL-dLinkedLibrary-66` re-stages the shipped arm on S2's break, and AC2 is this pass's
probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, id 24 (HIGH, item
  H1).

## 10. Reuse audit

The seam extended is unit 54's inline `region_sh` block and the gate's own exit-2 refusals
(`tools/check-microformats.sh:38-57`); the guard adds one test of a function the block defines. `python
tools/codebase-map/reuse_lookup.py "refuse a micro-format gate whose inline region reader is missing"`
ranked `read`, `read_text`, `read_conf`, `read_journal` and `region` (`tools/unattended/check-unattended.sh`,
the body being carried), none a definition guard, so no existing seam fits beyond the block and the gate.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
