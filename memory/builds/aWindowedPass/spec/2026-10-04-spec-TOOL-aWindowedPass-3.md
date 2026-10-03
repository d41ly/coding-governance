# TOOL-aWindowedPass-3 — a commit-time step refuses an open pass's undeclared write, naming the re-declare

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 5 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aWindowedPass-3-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aWindowedPass-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-3-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-3-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A pass may widen its declaration with `--dispatch` BEFORE its commit; after the commit no repair
exists. Today the miss is found at the close, hours later. This unit checks at the moment repair is
still legal: a `--check-commit` driver verb, run from the `commit-msg` hook, refuses a commit that
belongs to an open dispatched pass and stages paths outside its declaration, printing the exact
`--dispatch` command that widens it. It also requires the `Pass:` trailer on a commit whose subject
names an open pass, so attribution is structural from then on.

## 2. Scope (IN)

- **S1** — `bash <kit>/unattended.sh --check-commit <message file>`: finds the non-terminal run whose
  `run-branch` equals the current branch, reads the message's `Pass:` trailer, and exits 0 with no
  output when no run is bound. Observed by AC1.
- **S2** — With `Pass: <unit>`, the unit must have an open dispatch row in that run; the staged paths,
  less the run-state file, that unit's recorded brief paths and the effective generated outputs, must
  be covered by the union of the unit's open declarations. Otherwise it exits 1, naming each uncovered
  path and printing `bash <kit>/unattended.sh --dispatch <slug> --pass <unit>` with one `--writes`
  per declared and per uncovered path. Observed by AC2 and AC3.
- **S3** — With no `Pass:` trailer and a subject naming an open pass of the run, it exits 1 asking for
  `Pass: <unit>` or `Pass: none`. `Pass: none` always passes. Observed by AC4.
- **S4** — `.githooks/commit-msg` runs the verb before its merge-only audit, resolving the kit path
  as that hook resolves its own, and an absent kit is an announced skip. That hook is gov's own and
  is not shipped (`TOOL-dDerivedDocket-9`, `tools/govkit/registry.toml`): the kit README gives the
  adopter the one line to wire into its own carrier, naming this hook as the reference. Observed by
  AC5.
- **S5** — The verb carrier documents `--check-commit`, and the kit README states the hook's limits.
  Observed by AC5.

## 3. Non-goals (OUT)

- A commit made with `--no-verify` bypasses the hook; check 23 at the close still grades it.
- No refusal for a commit that is no pass: records commits pass untouched.

### Edges

- **consumes-from** `TOOL-aWindowedPass-4` — the effective generated outputs.
- **consumes-from** `TOOL-aWindowedPass-2` — the trailer reader and its meaning.

## 4. Design

The verb reuses the driver's `check_pass_open`, `covers` and the run-state reader; the staged set is
`git diff --cached --name-only`. A path whose staged change is confined to `<!-- gen:… -->` regions
counts as generated, by the same comparison `check_generated_render` makes, here between `HEAD:` and
`:` blobs. The trailer is read with `git interpret-trailers --parse` over the message file.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/README.md`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `.githooks/commit-msg`

### Alternatives rejected

- **A `pre-commit` step.** It cannot read the message, so it cannot tell a records commit from a pass.
- **A tool-call hook on `git commit`.** It would parse `-m` and `-F` from a command line and miss every
  message an editor wrote; the git hook sees the message itself.

## 5. Production-readiness checklist

- security — reads the index and the message; writes nothing.
- perf / scale — one staged listing and one row read per commit, only while a run is bound.
- error / empty / loading states — no run, no kit or no python is an announced skip, never a block.
- observability — the refusal names each path and the command.
- risks — a run that must commit through a hook-less clone loses the early catch; the close still
  grades it.
- testing — fixtures for each branch of S1 to S3, and the hook wiring.
- migration — an adopter wires the README's one line into its own `commit-msg`; until it does, check
  23 at the close is the only grader, as before.
- user docs — verb carrier entry and README limits.

## 6. Acceptance criteria

- **AC1** — When `--check-commit` runs on a branch no run names, it exits 0 and prints nothing.
  Red when: the verb grades a commit with no run bound.
- **AC2** — When the message carries `Pass: TOOL-x-1` and the staged set holds a path outside that
  pass's declaration, it exits 1 naming the path and printing `--dispatch` with `--writes` for it.
  Red when: the subset test is skipped.
- **AC3** — When the only extra staged path is a declared generated output or the run-state file,
  `--check-commit` exits 0.
  Red when: the effective generated set is not subtracted.
- **AC4** — When the subject names an open pass and no trailer is present, it exits 1 naming
  `Pass: none`; with `Pass: none`, it exits 0.
  Red when: the trailer requirement is not applied.
- **AC5** — When `grep -c 'check-commit' .githooks/commit-msg` runs, it prints at least 1, and
  `grep -c 'check-commit' tools/unattended/README.md` prints at least 1.
  Red when: the hook does not call the verb.

## 7. Gates

`unattended kit gate` · `govkit selfcheck`

New arm: tools/unattended/unattended.test.sh · one fixture per branch of S1 to S3 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's part (2) and the hooks at base.
- rev-2 · 2026-10-04 · build pass · S4 · AC5 · §4 · `.githooks/commit-msg` is gov-own and deliberately
  unshipped, a recorded decision rev-1 missed: a hook file is copied whole and would overwrite an
  adopter's own. The adopter gets a README line instead of a merged block. The gen-region comparison
  moved into the kit library as `check_gen_region_only`, so check 23 and this verb share one answer.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a commit that writes outside its declared set"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`. Extended: the driver's
`check_pass_open` and `verb_dispatch`, `covers` and `read_brief_paths` in the kit library, the
`commit-msg` hook's kit-path ladder, and govkit's `merged` role, which already ships the branch guard
into adopters' `pre-commit`.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
