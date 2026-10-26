# KICK-dKeptSession-48 — the mixed-window limit stated, and a 200k session on a 1M-observed model read against its own window by the harness's variable

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 |
| [2026-10-26-build-KICK-dKeptSession-48-deviation-481.md](../build/2026-10-26-build-KICK-dKeptSession-48-deviation-481.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 43 at HIGH**, report item **H8**, which no other id shares.

`KICK-dKeptSession-30` S1 rung 2 takes the largest observation per model id across the node's newest
20 transcripts, and its §4 Evidence records that the model id reads `claude-opus-5-5` for the 200k
and the 1M window alike. So on a node that has logged any 1M session, every 200k session of that
model is read against the 1M rung: its fill reads a fifth of the truth, `fresh-at-boundary` at 60%
never fires, and the harness compacts first. Unit 30 §5 prices only the opposite direction, and its
AC2 asserts the 15% that is wrong for a 200k session. No transcript field tells the two windows
apart, so this unit states the limit where the derivation and its readers are documented, names
the override that answers it, and observes the override on the mixed-window root. It repairs
`KICK-dKeptSession-30` and builds one step after it (order 14).

## 2. Scope (IN)

- **S1** — id 43. The limit in the derivation. `derive_context_window`'s docstring in
  `tools/runlog/extract.py` states that every session of a model observed past 200000 on the node
  reads the 1M rung, a 200k session of that model included, and that the session's override is
  `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000`, rung 1. Observed by AC2.
- **S2** — id 43. The limit for the owner. `help/orientation-card.md`'s `context —` paragraph
  (`KICK-dKeptSession-30` S5) gains one sentence: on a node that runs one model at both windows, a
  200k session sets `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` or reads its fill against the larger
  window. Observed by AC3.
- **S3** — id 43. The override observed on the mixed root. A selftest case reads unit 30's AC2 root,
  the 150000-token `context-window` beside the 900000-token `context-window-sibling`, with the
  variable set to 200000. Observed by AC1.
- **S4** — id 43. The sibling text superseded by name. `KICK-dKeptSession-30` §5's risks line, which
  prices only a model never observed past 200k, reads both directions as S1 states them, and unit 30
  AC2's `15%` is the 1M session's share, never a 200k session's. Answered in unit 30's acceptance
  ledger. Observed by AC2.

## 3. Non-goals (OUT)

- A per-session window signal. No transcript record names the window (unit 30 §4 Evidence), so
  none is derived; §8 F1 records the options.
- Whether the harness itself honours the variable for a first-party model: id 17, the batch's
  item, `KICK-dKeptSession-56`.
- The report's left-shift checklist entry, that §5 risks prices both directions of every derived
  threshold. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_window`'s rung 1 and its mixed-window root, whose limit this unit states and observes (id 43)
- **hands-off** `KICK-dKeptSession-62` — the owner's `CLAUDE_CODE_MAX_CONTEXT_TOKENS` advice, whose ambient value the batch's S26 arm keeps out of every case (id 37)

## 4. Design

### Evidence

- Unit 30 §4: "The `model` field reads `claude-opus-5-5` whatever the window, and a grep for
  `contextWindow` and `context_window` over the transcripts printed nothing."
- Unit 30 S1 rung 1 reads `CLAUDE_CODE_MAX_CONTEXT_TOKENS` first when it is a positive integer, with
  source `env`.

### The reads on the mixed root

```
context-window beside context-window-sibling                              -> 15%  (1M rung, observed 900000)
same, CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000                               -> 75%  (source env)
```

### Inventory

No identifier is minted.

### Migration

None.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, the docstring
- `tools/runlog/selftest.py`: S3's case
- `help/orientation-card.md`: S2

### Alternatives rejected

- **The session's own maximum ranked above the node's.** A fresh 1M session would read its first
  200k against the 200k rung, unit 30 §4's rejected alternative.
- **The smaller rung whenever the node holds both.** It reverses the error for every 1M session,
  which is the more common window on this node by unit 30 §4's measurement.

## 5. Production-readiness checklist

- security — none: a docstring, a help sentence and a test case.
- perf / scale — none.
- error / empty / loading states — unchanged.
- observability — `runlog.py context` already prints `context: window <tokens> · <source>`, so a
  200k session reading the 1M rung shows the rung it read.
- risks — a 200k session with no override on a mixed node errs towards a late boundary act; S2 tells
  the owner the remedy.
- testing — the case of §6 and the arm in §7.
- migration — none.
- user docs — `help/orientation-card.md`, S2.

## 6. Acceptance criteria

- **AC1** — When `runlog.py context` reads `context-window` from a root that also holds
  `context-window-sibling`, with `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` set, it prints `75%` and the
  stderr line `context: window 200000 · env`.
  Red when: the variable is ignored on a root holding a larger observation, printing `15%`.
- **AC2** — When `python -c "import extract; print(extract.derive_context_window.__doc__)"` runs in
  the runlog kit, the text names both `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` and the 1M rung for a
  200k session.
  Red when: the derivation documents one direction of its error.
- **AC3** — When `grep -n "CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000" orientation-card.md` runs in
  `help/`, it prints the `context —` paragraph's sentence.
  Red when: the owner's page names no remedy for a 200k session on a mixed node.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 · the mixed root read with the variable at 200000, staged red by a copy of `extract.py` ranking the observation above the variable · none

## 8. Open questions

- **F1 — How does a 200k session on a 1M-observed model read its own window?** Options: (a) the
  limit stated and the harness's variable named as the session's override, the skeptic's corrected
  fix; (b) a per-session signal derived from the session's own maximum; (c) the smaller rung whenever
  both are observed. (b) misreads a fresh 1M session below 200k; (c) misreads every 1M session.
  (a) meets AC1 to AC3 and adds no surface. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the skeptic's corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H8 (id 43).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seam is unit 30's own rung 1, the harness's `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, which this unit
documents and observes rather than adding a second override. `python
tools/codebase-map/reuse_lookup.py "derive the context window size of a model from observed session
usage"`, unit 30's probe, ranked `extract_session` and `resolve_session_tree`; neither tells two
windows apart, so no existing seam fits a per-session signal and none is minted.

Recall terms used: `python tools/memory-recall/query.py "how does a 200k session read its fill on a
node that also runs 1M sessions" --terms "context window rung CLAUDE_CODE_MAX_CONTEXT_TOKENS 200000
1000000 mixed observed fill fresh-at-boundary override"`
