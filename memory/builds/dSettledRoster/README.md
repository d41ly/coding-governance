---
slug: dSettledRoster
node: d
opened: 2026-08-20
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-dSettledRoster-1 DEPL-dSettledRoster-2 TOOL-dSettledRoster-1 TOOL-dSettledRoster-2 TOOL-dSettledRoster-3 TOOL-dSettledRoster-4 TOOL-dSettledRoster-5 TOOL-dSettledRoster-6
---

# dSettledRoster — the records-only close-out, and the shell bug it walked into

Node `d` · opened 2026-08-20 · streams tooling and deployer.

## Start here

**State.** CLOSED. One specced unit, `TOOL-dSettledRoster-5`, landed at `474043e` with its naming
and map follow-up at `d2a40aa`, both on `origin/main` at `d2a40aa`. The rest of the roster is
backlog and decision rows this session minted, listed below.

**This folder was opened AFTER the work landed**, at the owner's request, and every date in it is
the day it was written rather than the day the work happened. That is the honest shape and it has
one machine-visible consequence, recorded rather than absorbed: the product commits could not name a
slug that did not exist when they landed, so drift signal 6 cannot trace this unit and
`memory/project/trace-waiver.txt` carries the row that says why.

## How a records close-out became a kit change

The session was asked to close thirteen builds whose product had landed and whose spec status
headers had never been flipped. Seven closed. Six could not: hygiene check 12 machine-enforces a
resolved §8 before a terminal status, and each of those six carries forks that are the owner's to
answer, not a session's.

The push that would have landed the seven was BLOCKED by a leg that was already red on `main` and
that nobody had seen, because it is guarded — only `GATE_FULL=1` runs it — and because it needs WSL
installed to reproduce at all. Nodes `a` through `c` are green on the same commit. Unblocking it is
`TOOL-dSettledRoster-5`, and it is the only unit here with a spec.

**The first root cause was wrong**, and that is kept rather than tidied away. `resolve_python`'s
`-c 'import sys'` probe was blamed, and it IS too weak to reject an interpreter below a kit's floor
— but every python launcher on this node is 3.12 or newer, so no probe over them could have yielded
the 3.10 in the traceback. The 3.10 belonged to the WSL that the bare name `bash` pulled in. The
wrong cause sat in `TOOL-dSettledRoster-3` for one commit before being replaced with the measured
one.

## The rest of the roster — rows, not units

These were minted by the same session and carry no spec. They are listed so the slug's id space is
readable from one place.

| Id | Kind | What it holds |
|---|---|---|
| `TOOL-dSettledRoster-1` | backlog | `AGENTS.md` is reachable by no path gate; parked by the closing `cKeyedLaunchpad` README and homeless without a row |
| `TOOL-dSettledRoster-2` | decision | the trace waiver is the remedy for an untraceable close, never a raised pin |
| `TOOL-dSettledRoster-3` | backlog | the `govkit acceptance matrix` red — CLOSED by unit 5, and carrying the corrected root cause |
| `TOOL-dSettledRoster-4` | backlog | `check-verdict-epoch.sh` names three kit-version carriers and six exist |
| `TOOL-dSettledRoster-6` | backlog | three `resolve_bash` copies, two different probes — the §10 audit's finding |
| `DEPL-dSettledRoster-1` | backlog | govkit's `eol=lf` pins are appended LAST, so gov overrides a target that set the opposite |
| `DEPL-dSettledRoster-2` | backlog | an `apply` against a manifest-kind target runs that target's own command twice |

## What the closing pass would have caught, had there been one

Recorded because the value is in the misses, not the hits.

- The reuse audit was run for §10 rather than skipped, and it **changed a claim this session had
  already committed**. There are THREE `resolve_bash` functions, not the two the gotcha record
  named, and `tools/run-gates/profile_bar.py`'s probes a stronger property than the other two.
- Two gates caught the new code on the way in, which is them working: `lexicon` went two offenders
  over a shrink-only pin, and `symbols.json` went stale. Both were repaired by conforming — renaming
  to verbs already in the table — rather than by moving a pin.
- Three ratchets fired in sequence during the landing and each was a real defect, not noise: the
  verdict epoch, the kit-version markers, and the manifest maintenance stall. The last one found two
  genuinely stale §B claims, including the manifest stating node tag `a` as if it were the constant
  when four registered nodes share one primary tree.

## Units — the authored roster

<!-- roster:units -->
| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSettledRoster-5` | 2 | name the bash EXECUTABLE, so a descriptor's leg stops running under WSL |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-08-20 · streams tooling+deployer
ids DEPL-dSettledRoster-1 DEPL-dSettledRoster-2 TOOL-dSettledRoster-1 TOOL-dSettledRoster-2 TOOL-dSettledRoster-3 TOOL-dSettledRoster-4 TOOL-dSettledRoster-5 TOOL-dSettledRoster-6

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dSettledRoster-5 — name the bash executable, so a descriptor's leg stops running under WSL](spec/2026-08-20-spec-TOOL-dSettledRoster-5.md) | CLOSED | rev-1 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-20-spec-TOOL-dSettledRoster-5.md](spec/2026-08-20-spec-TOOL-dSettledRoster-5.md)
<!-- /gen:build-docs -->
