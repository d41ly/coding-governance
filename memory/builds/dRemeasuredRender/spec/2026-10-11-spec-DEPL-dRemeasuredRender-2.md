# DEPL-dRemeasuredRender-2 — `govkit update` re-probes a hole after the render, and reports only the verdict that stands

**Status:** CLOSED · rev-2 · 2026-10-11 · node d · Tier-2 · base 9a8777b8 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-DEPL-dRemeasuredRender-2-1-acceptance-ledger.md](../build/2026-10-11-build-DEPL-dRemeasuredRender-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-DEPL-dRemeasuredRender-2-1-build-brief.md](../prompts/2026-10-11-prompt-DEPL-dRemeasuredRender-2-1-build-brief.md) | journal | — |
| [2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md](../prompts/2026-10-11-prompt-TOOL-dRemeasuredRender-1-brief.md) | research | TOOL-dRemeasuredRender-1 DEPL-dRemeasuredRender-1 |

<!-- /gen:spec-records -->

## 1. Goal

`update` probes a kit's `[[hole]]` discharges before its regenerate, to name a hole the render is
bound to refuse on. A probe that byte-checks the rendered artifact, as lexicon's
`lexicon-ratified` does, fails there and passes after the render. Both adopters printed
`HOLE lexicon: 'lexicon-ratified' is undischarged` from a run whose own verify then exited 0.
Keep the early probe, and report only what still fails after the render.

## 2. Scope (IN)

- **S1** — The early probe keeps its place and its purpose, and its line no longer states the
  verdict: `HOLE <kit>: '<id>' probes undischarged before the render (probe exit <n>); probed again
  after it — <why>`. Observed by AC1.
- **S2** — After the kit's regenerate argvs run, each hole the early probe called undischarged is
  probed again. One still failing prints the existing
  `HOLE <kit>: '<id>' is undischarged (probe exit <n>) — <why>`. One now passing prints
  `HOLE <kit>: '<id>' is discharged after the render; the early verdict does not stand`. Observed by
  AC1, AC2.
- **S3** — The re-probe runs whether the argv was accepted or refused: the verdict after the render
  is the one that stands either way. Observed by AC2.

## 3. Non-goals (OUT)

- `check --run-discharge`, which probes after everything and is already right.
- A hole the early probe called discharged, or anything other than undischarged: not re-probed.
- Printing the probe verdicts `update` does not print today (`needs-answer`, `no-launch`).

### Edges

- **consumes-from** `DEPL-dRemeasuredRender-1` — sequenced after it; both write
  `tools/govkit/govkit.py` and `tools/govkit/selftest.py`.

## 4. Design

### Evidence

Read at base `9a8777b8`. `run_hole_probes` returns `(id, verdict, detail)` per hole; the regenerate
loop calls it once, before the snapshot and the argvs, and prints `is undischarged` for each
`undischarged` verdict. The self-test's `[aHI-1 S3]` arm asserts that line for a hole whose probe is
`exit 3`, which still fails after the render, so its assertion holds unchanged.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **Move the probe after the regenerate.** Rejected by the prompt: naming a hole before a render that
  refuses on it is the probe's purpose, recorded in `run_hole_probes`' docstring.
- **Suppress the early line.** Rejected: a render that refuses would then be preceded by nothing
  naming the hole it refused on.

## 5. Production-readiness checklist

- security — N/A — re-runs a gov-declared probe the run already runs once.
- perf / scale — one extra probe per hole that failed early; none on a discharged hole.
- error / empty / loading states — a re-probe reading neither verdict prints one line saying so.
- observability — the after-render line names which verdict stands.
- risks — none beyond one more probe run.
- testing — two self-test arms, a hole passing only after the render and one failing throughout,
  each observed RED at base.
- migration — none.
- user docs — the runbook's `update` paragraph in `WIRE-INTO-PROJECT.md` names the re-probe.

## 6. Acceptance criteria

- **AC1** — When `govkit update --write` runs over a fixture kit whose hole probe passes only once
  the render has written its file, the output carries `probes undischarged before the render` and
  `is discharged after the render`, and no `is undischarged` line for that hole. Red when: the run
  reports it undischarged, which base does.
- **AC2** — When the fixture's hole probe fails both before and after the render, the run prints
  `is undischarged (probe exit` for it after the early line. Red when: the run reports only the
  early verdict, which base does.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: `tools/govkit/selftest.py` · covers AC1 AC2 · a fixture kit whose hole probe reads the rendered file · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the owner's prompt.
- rev-2 · 2026-10-11 · AC2 · §5 · the final line prints inside the kit's regenerate loop, before the
  `ran` summary, so AC2 orders it after the early line instead; a re-probe reading neither verdict
  prints a line rather than nothing, so the early line is never left unanswered.

## 10. Reuse audit

The seam is `run_hole_probes`, called a second time with the same arguments over the holes the
first call named undischarged; no new probe runner. `reuse_lookup.py` was run once for the build's
govkit units and named no govkit seam beyond this one. The recall query returned
`DEPL-aHalvedInstall-1`, the unit that added the early probe and lifted the runner out of `check`.

Recall terms used: hole discharge probe regenerate rendered row install.sums sha256 oid re-rendered CAP adopter update
