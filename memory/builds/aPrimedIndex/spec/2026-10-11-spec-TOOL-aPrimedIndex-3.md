# TOOL-aPrimedIndex-3 — the runner refuses to start a bar while a declared output is stale, before it queues for the host

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPrimedIndex-3-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPrimedIndex-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-build-TOOL-aPrimedIndex-3-m12-probe.md](../build/2026-10-11-build-TOOL-aPrimedIndex-3-m12-probe.md) | research | — |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md) | journal | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-4 |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1.md) | research | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-4 |
| [2026-10-11-review-TOOL-aPrimedIndex-1-4-implementation-diff-round1.md](../reviews/2026-10-11-review-TOOL-aPrimedIndex-1-4-implementation-diff-round1.md) | diff-review | TOOL-aPrimedIndex-1 TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

Make every merge and landing bar prove the declared generated outputs fresh before it runs a leg,
and refuse in about a minute when one is not, naming each stale output and the one command that
regenerates them all. Every bar entry point reaches the runner, so this binds all of them.

## 2. Scope (IN)

- **S1** — After its profile and process-monitor lines and before the host turnstile, the runner
  calls TOOL-aPrimedIndex-2's `--check`. A stale, failed or timed-out item, or a refused
  declaration, ends the run with exit 2, REFUSED, before any leg is dispatched. Observed by AC1.
- **S2** — The refusal names every stale output with its check command and output tail, which the
  verb prints, then one remedy line naming `run-gates.sh --regen` by this kit's derived path and
  saying to commit what it moves. Observed by AC1.
- **S3** — A fresh set prints the verb's count line and the run continues exactly as before. A tree
  with no kit descriptor at the tool root prints one line saying none is declared and spawns no
  python, so the skip announces itself and a suite's scratch bars stay cheap. Observed by AC2.
- **S4** — `GATE_REGEN_CHECK=0` skips the call with one announced line naming the knob and what a
  stale output does instead: it reds its own leg at the end of the bar. A missing `regen.py` beside
  the runner is announced the same way and the run continues. Observed by AC3.
- **S5** — The `--print-profile` verb and the three `--regen` verbs are untouched: none runs the
  preflight. Observed by AC4.
- **S6** — The runner's header comment states the new refusal and what it does not check, and the
  kit README states where it sits in the run. Observed by AC4.

## 3. Non-goals (OUT)

- The runner never writes the tree it grades: it refuses and names the remedy.
- No leg changes. The freshness legs still grade what they grade, so a skipped preflight costs an
  early signal and never a verdict.
- No change to `.githooks/pre-push`, `tools/push-main.sh` or the unattended close. Each reaches the
  runner and reads a non-zero exit as a blocked bar already; the lander's regeneration is
  TOOL-aPrimedIndex-4.
- No run-log line for a refused preflight: it exits before the run record exists, as the runner's
  other early refusals do.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-2` — the `--check` verb and its exit codes.
- **consumes-from** `TOOL-aPrimedIndex-1` — the declared rows; with none, the preflight checks
  nothing and says so.

## 4. Design

### Placement

The call sits after the `run-gates: process-monitor:` line and before `GATE_TURNSTILE` is read.
Before the queue, because a refusal after an hour's wait for another bar's turnstile is the
cost this build exists to remove. After the profile line, because the canary reads that line as the
runner's first.

### The refusal

```text
run-gates: REFUSED — <s> declared generated output(s) are stale or unproven, and a bar over them reds on that alone.
  regenerate every one, in stage order:  bash <kit>/run-gates.sh --regen
  then commit what it moved and run the bar again; GATE_REGEN_CHECK=0 skips this check
```

`<kit>` is the runner's own directory relative to the repo root, the derivation the canary already
holds the runner to; no prefix is spelled.

### Cost

PINNED, measured 2026-10-11 on node `a` in a clone of this tree with the draft reader: eleven checks
ran concurrently in 49 s on a fresh tree and 56 s with one stale, and the clone's whole one-leg bar
took 3 m 26 s. The record is `build/2026-10-11-build-TOOL-aPrimedIndex-3-m12-probe.md`; the
acceptance ledger re-measures it on the built runner.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `memory/guides/MERGE-BAR.md`

### Alternatives rejected

- **Regenerate in place, then refuse if anything moved.** It saves one command and makes the grader
  a writer of the tree it grades; at the push boundary the hook refuses a dirty tree anyway, and a
  green earned over an uncommitted regeneration is never reusable.
- **Run the checks beside the legs and kill the pool on a stale one.** It saves the two minutes on
  a fresh tree, and costs a kill path through the pool, the wall watcher and the census for an
  early signal the sequential call already gives.
- **A PreToolUse hook on the agent's bar command.** It binds only an agent's call: not the pre-push
  hook a plain `git push` fires, not remote CI, not a person.
- **Per-entry-point regeneration** in the lander, the close and the hook. Three copies of one rule,
  and the plain bar and remote CI would still bind nothing.

## 5. Production-readiness checklist

- security: N/A — the runner already executes every declared leg; the preflight executes declared
  checks from the same tracked tree.
- perf / scale: about two minutes on the loaded node `a`, recorded at build; the verb's own knobs
  bound it.
- error / empty / loading states: an empty set and a missing verb each print one announced line.
- observability: the verb's count line is on every bar's stdout.
- risks: a check that is red for a reason a regeneration cannot fix refuses the bar too. That bar
  would red on the same leg anyway; the refusal text names the check and its output so the reader
  sees which.
- testing: canary arms on a fixture descriptor, and a direct observation in a scratch clone.
- migration: none for an adopter beyond the kit update; a project with no staged rows sees a zero
  count.
- user docs: the kit README and one pointer line in `memory/guides/MERGE-BAR.md` (S6).

## 6. Acceptance criteria

- **AC1** — When the new canary arm runs as a slice with `bash` against a fixture whose descriptor
  declares a staged row whose `check` exits 1, the runner exits 2, prints `run-gates: REFUSED` with
  the `--regen` remedy, and prints no `GATE ` leg line and no `gate queue:` line. Red when: any leg
  line or queue line precedes the refusal, or the exit is not 2.
  fixture: built inside the kit dir from the canary's prologue at build time, deleted before commit.
- **AC2** — When the same slice's check exits 0, the runner prints the verb's count line and every
  leg line the fixture manifest declares; with no kit descriptor at the tool root it prints its own
  `no kit descriptor under` line, spawns no python, and runs its legs. Red when: the fresh run is
  refused, or the empty set prints nothing.
- **AC3** — When the slice sets `GATE_REGEN_CHECK=0` over the stale fixture, the runner prints the
  skip line naming `GATE_REGEN_CHECK` and runs its legs. Red when: the skip is silent or still
  refuses.
- **AC4** — When `grep -n "regen" tools/run-gates/README.md memory/guides/MERGE-BAR.md` runs, both
  name the preflight, and the slice's `--print-profile` run prints no `regen:` line. Red when: either
  document omits it, or the profile verb pays for the check.
- **AC5** — When a scratch clone of this repository has one row of `memory/gotchas/INDEX.md`
  removed and committed, the runner run there exits 2 within the preflight naming the gotchas item,
  and after `--regen` and a commit its preflight reads fresh. Red when: the clone's run reaches a
  leg, or stays refused after the regeneration.
  cost: two preflight runs, about four minutes on node `a`.
  fixture: a clone under a short root in `TEMP`, made at build time.

## 7. Gates

`codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `line length` · `memory hygiene` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 · a fixture descriptor whose staged check exits 1 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S3 · AC2 · the empty case is a tree with no kit descriptor, announced by the
  runner's own line with no python spawn; `regen: 0 declared` is the verb's line for descriptors that
  stage nothing.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` returned no seam in the runner for a pre-dispatch refusal; the
runner's own early refusals (`prof_die`, the manifest parse) are the pattern followed, exit 2 and no
run record. The check itself is TOOL-aPrimedIndex-2's verb, reached through the kit dir the runner
already derives as `KITDIR`.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
