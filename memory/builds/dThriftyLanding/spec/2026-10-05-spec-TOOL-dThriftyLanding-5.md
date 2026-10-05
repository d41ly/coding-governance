# TOOL-dThriftyLanding-5 — gov declares its doc class and what its bar legs read of it

**Status:** CLOSED · rev-1 · 2026-10-05 · node d · Tier-2 · base c3ef6742 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md) | journal | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 |
| [2026-10-05-build-TOOL-dThriftyLanding-5-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-5-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-5-1-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md) | diff-review | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-6 |

<!-- /gen:spec-records -->

## 1. Goal

Units 1 to 4 build a mechanism that does nothing until a repository declares two things: which paths
are its doc class, and, per leg, which of those paths the leg reads. This unit declares both for gov,
in `.githooks/gate-env.sh` and in `tools/gate-legs.json`, and copies each kit leg's value into its
kit descriptor so adopters receive it. A doc push here then skips the legs that cannot move, the
222-second `unattended kit gate` first among them when no build record changed.

## 2. Scope (IN)

- **S1** — `.githooks/gate-env.sh` declares `GATE_DOC_PATHS` as the memory tree and the root
  markdown files: `memory/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `WIRE-INTO-PROJECT.md` and
  `coding-governance-agents.template.md`. Observed by AC1.
- **S2** — Every bar leg that is not held and costs more than 5 s in this clone's
  `gate-ledger.tsv` declares `doc_reads`, set from a read of its script and the conf keys it resolves:
  the doc-class paths it opens, or `[]` when it opens none. A leg whose script cannot be settled that
  way keeps no declaration and is named in the acceptance ledger with the reason. Observed by AC2.
- **S3** — A cheaper leg declares `doc_reads: []` only when its argv and script read no doc-class path
  at all — a scan of shell, python or kit files, a version or wiring probe. Any other cheap leg keeps
  no declaration. Observed by AC2.
- **S4** — Each declared leg that a kit descriptor also declares carries the same value there, with
  `{memory_root}` for `memory`, so selfcheck 7h holds the two equal. Observed by AC3.
- **S5** — The decisions are recorded per leg in the acceptance ledger, with the path or conf key
  that decided each, so a later reader can re-check one without re-reading the script. Observed by
  AC2.

## 3. Non-goals (OUT)

- The mechanism: units 1 to 4.
- Guards: no leg's `guard` changes.
- Making `unattended kit gate` itself cheaper on a records push: it reads every build record, and a
  push that changes one still runs it. An ask is filed for the internal scoping.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-1` — the `doc_reads` key.
- **consumes-from** `TOOL-dThriftyLanding-3` — `GATE_DOC_PATHS` read at R.
- **consumes-from** `TOOL-dThriftyLanding-4` — selfcheck 7h's equality.

## 4. Design

### Evidence

Read at base `c3ef6742`. 61 legs are not held; 53 of them carry no guard. This clone's
`gate-ledger.tsv` costs them, under the width-8 pool, at 242 s for `unattended kit gate`, 83 s for
`pass-order history`, 69 s for `memory hygiene`, 54 s each for `brief-recorded` and `drift-audit
records`, 41 s for `marker contracts`, and under 22 s for every other one. `unattended kit gate`
alone took 222 s standalone on node `d`, and `memory hygiene` 39 s.

### Files touched (estimate)

- `.githooks/gate-env.sh`
- `tools/gate-legs.json`
- `tools/unattended/kit.toml`
- `tools/memory-tree/kit.toml`
- `tools/drift-audit/kit.toml`

### Alternatives rejected

- **Declare every leg.** A declaration on a 1-second leg saves a second and risks a skip; the cheap
  legs that read docs keep running, which is what an absent key means.
- **Declare the whole memory tree for every memory reader.** True and useless: the commonest doc push
  here edits one memory file, so a leg that names `memory/` always runs. Each declaration names the
  subtree its script opens.

## 5. Production-readiness checklist

- perf / scale — the saving is measured, not argued: a docs bar is timed against the base bar.
- security — the class is gov's own file, read at R by the hook.
- error / empty / loading states — an undeclared leg runs.
- observability — every skip is a named `GATE skip` line.
- testing — the canary's tracked-path arm and selfcheck 7h cover the values; the measurement covers
  the effect.
- migration — none.
- user docs — the charter's merge-bar section, in `TOOL-dThriftyLanding-6`.
- risks — a declaration missing a path skips its leg on a doc push until the next full bar, at most
  `GATE_FULL_MAX_LAG` commits later.

## 6. Acceptance criteria

- **AC1** — When `read_policy_key` reads `GATE_DOC_PATHS` from `.githooks/gate-env.sh`, it returns
  the six paths of S1, and each matches a tracked path.
  Red when: the key is absent, or an element names nothing.
- **AC2** — When the bar runs in this tree with `GATE_DOCS_BASE` at a commit before a one-line edit to
  a file under `memory/gotchas/`, `unattended kit gate` prints `GATE skip` with `docs-only`, and the
  acceptance ledger records the run's wall beside the base bar's.
  Red when: the base tree runs it, because nothing declares what it reads.
- **AC3** — When `govkit selfcheck` runs, block 7h reports no `doc_reads` disagreement.
  Red when: a descriptor and the manifest spell one leg's reads differently.

## 7. Gates

`govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `drift-audit selftest` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: none · declarations only; the canary's tracked-path arm from `TOOL-dThriftyLanding-1` grades them · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from this clone's ledger and the legs' scripts at base.

## 10. Reuse audit

No existing seam fits beyond the keys units 1, 3 and 4 add, which this unit only fills.
`python tools/codebase-map/reuse_lookup.py "which paths does each bar leg read"` was run and names
no per-leg read inventory; the read sets come from the legs' scripts. The ledger costs come from
`<git-dir>/gate-ledger.tsv`, which the charter names as the place per-leg seconds live. The recall
query returned `TOOL-aTimedTurnstile-2`, the open ask that guards make the bar diff-scoped, and its
note that guards landed for few legs; this unit answers the doc half of it.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
