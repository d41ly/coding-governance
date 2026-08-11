# TOOL-dNomadicAtlas-1 — a red leg leaves its reason on disk

**Status:** CLOSED · rev-1 · 2026-08-11 · node d · Tier-2 · base 7f614a17 · streams tooling

## 1. Goal

Make a failing leg's own output survive on disk, so a caller who pipes, backgrounds or scrolls away
`tools/run-gates.sh` can still name the failing test without re-running the whole bar. `leg()`
already holds every leg's merged output; the durable record kept only the row.

## 2. Scope (IN)

- **S1** — A `GATE_LEGS` manifest override, so a fixture can drive this runner without re-entering
  the real bar. Everything below is untestable without it.
- **S2** — Persist every leg's output to `<gitdir>/gate-logs/<leg>.log`, passing and failing alike.
- **S3** — On red, add a POINTER line per failing leg to the durable summary, naming its log. A
  pointer, never the bytes: that file is what an operator is told to read after a refused push.
- **S4** — Write `gate-last-failure.txt` on red runs only, so a green re-run cannot erase the
  failing run's evidence.
- **S5** — Redact URL userinfo before it becomes durable, and `chmod 600` the logs best-effort.
- **S6** — `tools/run-gates.evidence.test.sh`, a real fixture harness, wired as a leg.
- **S7** — Claim the new leg in `memory/map/FOUNDATION.md` and add its row to the `AGENTS.md`
  gate-suite section, which is a hand-kept inventory the drift probe counts.
- **S8** — Register node `d` in the `AGENTS.md` node registry, the lowest free tag.

## 3. Non-goals (OUT)

- **Porting inCMS's mechanism.** `ARCH-dNomadicAtlas-2` solved this in a concurrent bounded-pool
  runner with per-leg temp files. This runner is sequential and already holds the output in a shell
  variable, so it gets the small version, not a transplant.
- **A run header / not-run stamp.** The inCMS twin needs one because a fast-phase red SKIP-marks
  heavy legs, leaving stale logs at advertised paths. This runner has no phases and no SKIP-marking
  of that kind, so the staleness class does not exist here and a header would be ceremony.
- **Converging the two repos' summary FORMATS.** They already differ — upstream writes rows plus a
  verdict, inCMS a column table — and this unit does not change that. Only the filename and its
  tail-survival intent were ever shared.
- **Log rotation.** Fixed names, one run's worth, no prune code that could delete the wrong thing.

## 4. Design

### Data model

`<gitdir>/gate-logs/<leg>.log` per leg, replaced per run; the existing `gate-last-summary.txt` gains
pointer lines on red; `gate-last-failure.txt` is a red-only copy. All under the resolved gitdir:
untracked, per-worktree, never cloned.

### Migration

None. `GATE_LEGS` defaults to `tools/gate-legs.json`, so every existing invocation is unchanged.

### Rollout

One commit in this repo. No runtime surface; the fixture harness is the observable.

### Files touched (estimate)

`tools/run-gates.sh`, `tools/run-gates.evidence.test.sh`, `tools/gate-legs.json`,
`memory/map/FOUNDATION.md`, `AGENTS.md`.

### Alternatives rejected

- **Extending `tools/run-gates.test.sh`.** It is a static canary: it parses the manifest and greps
  the runner, and never executes it. Adding execution there would re-enter the real bar recursively
  and clobber the live summary mid-run. The fixture harness is a sibling, not a widening.
- **Testing without a manifest seam.** Rejected because it is impossible: the runner hardcoded
  `tools/gate-legs.json`, so any execution test drove the real 48-leg bar. S1 exists to make S6 exist.
- **Claiming the leg in a feature dossier.** The gate runner is not a feature; it is the merge bar.
  `FOUNDATION.md`'s own claim policy names "ops tooling, the registries themselves".

## 5. Production-readiness checklist

- security — a leg can echo an operator-exported credential, and a file outlives a terminal, so URL
  userinfo is masked before anything becomes durable. `chmod 600` is best-effort and worth little on
  a Windows checkout, where the mode bit is not enforced; the untracked location is the real control.
- perf / scale — one write per leg of bytes already in memory.
- a11y / i18n — N/A, no UI and no user-facing copy.
- error / empty / loading states — an uncreatable log dir disables capture and SAYS so.
- observability — this unit is observability.
- risks — the capture path must never decide whether a leg runs. An absent `GIT_DIR` is already
  refused at the repo guard before any capture code, and a path is never composed from an empty root.
- testing + left-shift gates — S6, mutation-proven in both directions.
- migration / rollback — `git revert`; no data, schema or stored state.
- help/ docs — `AGENTS.md` gains the leg row (S7), which is also what the drift probe counts.

## 6. Acceptance criteria

- **AC1** — When a leg fails, its complete output is readable afterwards at
  `<gitdir>/gate-logs/<leg>.log`.
- **AC2** — When a leg passes, its output is captured too.
- **AC3** — When the run is red, the durable summary NAMES each failing leg's log and contains none
  of its bytes.
- **AC4** — When a red run is followed by a green one, `gate-last-failure.txt` still holds the red
  run's evidence while `gate-last-summary.txt` reflects the latest.
- **AC5** — When `gate-logs/` cannot be created, the run completes on its legs' own verdicts and
  states that capture is OFF.
- **AC6** — When a leg echoes a URL with userinfo, the credential is masked and the line survives.
- **AC7** — When `GATE_LEGS` names an unreadable file, the runner exits 2 and names that file.
- **AC8** — When the persistence is removed, `tools/run-gates.evidence.test.sh` FAILS. Asserted by
  removal and observation, not by inspection.
- **AC9** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

`bash tools/run-gates.sh` (the full bar) · `run-gates evidence` (new) · `run-gates canary` ·
`codebase-map coverage + freshness` · `drift-audit records`.

## 8. Open questions

none — the one judgement call, where to claim the leg, is settled in §4 Alternatives rejected by
`FOUNDATION.md`'s own claim policy.

## 9. Revision log

- rev-1 · 2026-08-11 · built and closed on a green 47/47 bar. Written after the build: the mechanism
  and its adversarial review are `ARCH-dNomadicAtlas-2` in the adopting repo, and this is the
  deferred upstream half that review explicitly sized as "runner change plus new harness machinery".
  The build confirmed that sizing and corrected one inherited assumption — the unresolvable-gitdir
  hazard does not exist here, because `--show-toplevel` refuses before any capture code runs.

## 10. Reuse audit

The seam reused is `leg()`'s existing capture: the output is already in `$out` at the exact line the
durable record is built, so S2 is a write of bytes in hand rather than a new capture path. The
artifact names are reused from `TOOL-aLeasedGauntlet-1`, which introduced the durable summary for the
same reason and stopped at the row. No lookup tool was run: this repo's map indexes its own kits, not
`tools/*.sh` control flow, and the relevant prior art was found by reading the runner.
