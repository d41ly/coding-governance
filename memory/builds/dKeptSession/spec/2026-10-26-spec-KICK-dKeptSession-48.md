# KICK-dKeptSession-48 — the mixed-window limit stated, and a 200k session on a 1M-observed model read against its own window by the harness's variable

**Status:** INPROGRESS · rev-6 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-48-deviation-481.md](../build/2026-10-26-build-KICK-dKeptSession-48-deviation-481.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 |
| [2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 |
| [2026-11-21-prompt-KICK-dKeptSession-48-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-48-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md) | research | KICK-dKeptSession-50 KICK-dKeptSession-47 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-61 |
| [2026-11-22-prompt-KICK-dKeptSession-48-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-48-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-48-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-48-reground-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 43 at HIGH**, report item **H8**, which no other id shares.

`KICK-dKeptSession-30` rung 2 takes the largest observation per model id across the node's newest
`CONTEXT_WINDOW_SCAN` transcripts, and its Evidence records that the model id reads
`claude-opus-5-5` for the 200k and the 1M window alike. So on a node that has logged any 1M session,
every 200k session of that model is read against the 1M rung: its fill reads a fifth of the truth,
`fresh-at-boundary` at 60% never fires, and the harness compacts first. Unit 30's risks line prices
only the opposite direction, and its AC2 asserts the 15% that is wrong for a 200k session. No
transcript field tells the two windows apart, so this unit states the limit in every shipped text
that documents the derivation, names the override that answers it, and observes the override on the
mixed-window root. Unit 30 landed CLOSED, and `KICK-dKeptSession-47`, built just before this unit,
rewrites the same texts' compaction clause, so this unit's sentences sit beside 47's landed ones.

## 2. Scope (IN)

- **S1** — id 43. The limit in the derivation. The docstring of
  `tools/runlog/extract.py#derive_context_window` gains one sentence at its end, after "An
  unreadable transcript is skipped.", which unit 47 leaves as it is: "No transcript record names the
  window, so every session of a model observed past 200000 under the root reads the 1M rung, a 200k
  session of that model included; that session's override is
  `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000`, rung 1 (KICK-dKeptSession-48 S1)." Observed by AC2.
- **S2** — id 43. The limit for the owner. In `help/orientation-card.md`, section "When a session
  resumes", the paragraph opening "The `context —` line shows how full the session's context window
  is" gains one sentence after "rounded up to the 200k or the 1M window.": "No transcript names the
  window a session runs, so on a node that runs one model at both windows a 200k session reads its
  fill against the 1M window unless the owner starts it with `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000`
  set." Observed by AC3.
- **S3** — id 43. The override observed on the mixed root. `test_extract_context_window`
  (`tools/runlog/selftest.py#test_extract_context_window`) gains one check beside unit 30's
  500000 read of the same `main` transcript: with the variable at 200000 in a fresh
  `build_arm_env(base)` copy, `runlog.py context` reads `context-window` from the root that also
  holds `context-window-sibling`. The function's docstring adds `KICK-dKeptSession-48 AC1` to the
  criteria it names. `ASSERTION_FLOOR` rises by 1, with its `RAISED` comment. Observed by AC1.
- **S4** — id 43. The sibling text superseded by name. `KICK-dKeptSession-30`'s risks line, which
  prices only a model never observed past 200k, reads both directions as S1 states them, and unit 30
  AC2's `15%` is the 1M session's share, never a 200k session's. Answered in this unit's own
  acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-48-1-acceptance-ledger.md`,
  which quotes unit 30's risks line and its AC2 and states S1 and this item supersede them. Unit 30
  is CLOSED, so neither its spec nor its ledger is written (F2). Observed by AC4.
- **S5** — id 43. The limit in the kit README. The `context` paragraph of `tools/runlog/README.md`
  gains one sentence immediately before "The share passes 100% only where", which neither unit 47
  nor this unit otherwise edits: "No transcript record names the window a session runs, so every
  session of a model observed past 200000 under the root reads the 1M rung, a 200k session of that
  model included; that session reads its own window only with `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000`
  set (KICK-dKeptSession-48)." Unit 47's rewritten compaction clause in the same paragraph stands.
  Observed by AC5.

## 3. Non-goals (OUT)

- A per-session window signal. No transcript record names the window (unit 30's Evidence), so
  none is derived; F1 under Open questions records the options.
- Whether the harness itself honours the variable for a first-party model: id 17, the batch's
  item, `KICK-dKeptSession-56`.
- The report's left-shift checklist entry, that a risks line prices both directions of every
  derived threshold. No clause of this build names that checklist.
- The shipped texts the table under Design reads as staying true, unit 47's compaction clause
  among them.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_window`'s rung 1 and its mixed-window root, whose limit this unit states and observes (id 43)
- **hands-off** `KICK-dKeptSession-62` — the owner's `CLAUDE_CODE_MAX_CONTEXT_TOKENS` advice, whose ambient value the batch's S26 arm keeps out of every case (id 37)

## 4. Design

### Evidence

Read at `e8b22050a` on 2026-11-22, the run's tree after units 14, 30, 45 and 46 landed.

- Unit 30's Evidence, rev-3: "No transcript record names the window. The `model` field reads
  `claude-opus-5-5` whatever the window, and a grep for `contextWindow` and `context_window` over
  the transcripts printed nothing."
- `derive_context_window(model, root=None, held=None)` returns `(tokens, source)`: the variable
  first when it is a positive integer, source `env`; else, under `root` or the root
  `resolve_projects_root` resolves, the smallest `CONTEXT_WINDOW_RUNGS` rung at or above the
  largest observation on `model` across the newest `CONTEXT_WINDOW_SCAN` main transcripts
  (`tools/runlog/extract.py#derive_context_window`). `CONTEXT_WINDOW_RUNGS` is `(200000, 1000000)`
  and `CONTEXT_WINDOW_SCAN` is 20 (PINNED, read 2026-11-22).
- `measure_context_fill(transcript, until=None)` returns `(share, tokens, source)`, and
  `derive_context_fill(ev, *, window=None, root=None)` raises `ValueError` holding neither
  (`tools/runlog/extract.py#measure_context_fill`, `tools/runlog/extract.py#derive_context_fill`).
  This unit calls neither directly; the CLI reads through the first.
- `cmd_context` prints the share and `context: window <tokens> · <source>` on stderr
  (`tools/runlog/runlog.py#cmd_context`).
- `test_extract_context_window` already reads the mixed root at 15% and under the variable at
  500000 (30%, source `env`) and at `x` (`tools/runlog/selftest.py#test_extract_context_window`).
  The 200000 read is the remedy S1, S2 and S5 name, so S3 pins that value, not a second mechanism.
- `main` pops the variable before any arm, and its comment says "the one arm that reads it sets it
  in its own child's environment" (`tools/runlog/selftest.py#main`). S3's check sits in that arm,
  so the comment stays true.
- `ASSERTION_FLOOR` is 1624 at `e8b22050a` (PINNED, 2026-11-22). Unit 47 raises it first in this run,
  so the builder reads the figure the tree holds and raises it by 1.
- Unit 47 rev-6 rewrites the docstring's "its largest integer compaction `pre_tokens`" and the
  README's "largest compaction `preTokens`" (unit 47's S1). Neither anchor S1 or S5 uses is among
  them.
- No import is added: `record.py`, which the `policy fixtures` leg's runlog-record plant imports,
  imports `extract` at module level (`tools/runlog/record.py`).

### The shipped texts

Every shipped text naming the window's source or `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, by
`git grep` outside `memory/` at `e8b22050a`:

| Text | Verdict |
|---|---|
| `tools/runlog/extract.py#derive_context_window`, docstring | incomplete: S1 |
| `tools/runlog/README.md`, the `context` paragraph | incomplete: S5 |
| `help/orientation-card.md`, the `context —` paragraph | incomplete: S2 |
| `tools/runlog/extract.py`, the comment above `CONTEXT_WINDOW_RUNGS` | stays |
| `tools/runlog/runlog.py`, module docstring's `context` lines | stays |
| `tools/policy/catalogue.toml`, `context.threshold` summary | stays |
| `skills/session-kickoff/manifest-check.sh`, the comment above `render_context_line` | stays |
| `tools/runlog/fixtures/transcripts.json`, `context-window`'s `about` | stays |

The comment above `CONTEXT_WINDOW_RUNGS` says only that the largest observation is rounded up to a
rung, which the limit follows from. The `runlog.py` docstring names `derive_context_window` and no
rule. The catalogue summary names the source, "derives per model from the node's observed usage, or
CLAUDE_CODE_MAX_CONTEXT_TOKENS where set", which holds; its member's fingerprint backs the help
page's usage marker, so it is left unedited. The `manifest-check.sh` comment already says nothing
checks that the window is the model's real one. The fixture's `about` names the readers that minted
it and its 15% read, which still hold. The `CLAUDE_CODE_MAX_CONTEXT_TOKENS` setting in
`tools/policy/check_policy.py`'s owner-ceiling plant is a fixture value and states nothing.

### The reads on the mixed root

```
context-window beside context-window-sibling                              -> 15%  (1M rung, observed 900000)
same, CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000                               -> 75%  (source env)
```

Both shares are DERIVED from the fixture: the `context-window` turn reads 150000 tokens and the
sibling 900000 (`tools/runlog/fixtures/transcripts.json`).

### Inventory

No identifier is minted.

### Migration

None.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, the docstring sentence
- `tools/runlog/README.md`: S5, the `context` paragraph's sentence
- `help/orientation-card.md`: S2
- `tools/runlog/selftest.py`: S3's check in `test_extract_context_window`, its docstring, and the
  `ASSERTION_FLOOR` raise with its `RAISED` comment
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-48-1-acceptance-ledger.md`:
  S4's answer beside the criteria observed

### Alternatives rejected

- **The session's own maximum ranked above the node's.** A fresh 1M session would read its first
  200k against the 200k rung, unit 30's own rejected alternative.
- **The smaller rung whenever the node holds both.** It reverses the error for every 1M session,
  the more common window on this node, as unit 30 rev-3 pins it: its probe read 48963 of its
  57351 main usages above 200000 (PINNED, 2026-11-21 for both counts and the line before).
- **A new `test_` function for S3.** `test_extract_context_window` already builds the mixed root
  and reads it under the variable, and `main`'s comment names one arm that sets it; a second arm
  would make that comment false and add a `symbols.json` entry for one check.

## 5. Production-readiness checklist

- security — none: three documentation sentences and a test check.
- perf / scale — none.
- error / empty / loading states — unchanged.
- observability — `runlog.py context` already prints `context: window <tokens> · <source>`, so a
  200k session reading the 1M rung shows the rung it read.
- risks — a 200k session with no override on a mixed node errs towards a late boundary act; S2 tells
  the owner the remedy.
- testing — the check of AC1 and the arm on the Gates line.
- migration — none.
- user docs — `help/orientation-card.md` (S2) and the kit's `tools/runlog/README.md` (S5); the texts
  the table under Design reads as staying are left as they are.

## 6. Acceptance criteria

- **AC1** — When `runlog.py context` reads `context-window` from a root that also holds
  `context-window-sibling`, with `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` set, it prints `75%` and the
  stderr line `context: window 200000 · env`.
  Red when: a copy of `extract.py` ranking the observation above the variable prints `15%`.
  figure: DERIVED, 150000 over 200000.
- **AC2** — When `python -c "import extract; print(' '.join(extract.derive_context_window.__doc__.split()))"`
  runs in `tools/runlog/`, piped into `grep -c "CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000"` it prints
  `1`, and into `grep -c "a 200k session of that model included"` it prints `1`.
  Red when: the derivation documents one direction of its error.
- **AC3** — When `grep -n "CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000" orientation-card.md` runs in
  `help/`, it prints one line, below the heading "When a session resumes", and `tr -s ' \r\n' ' '`
  over the page piped into `grep -c "a 200k session reads its fill against the 1M window"` prints `1`.
  Red when: the owner's page names no remedy for a 200k session on a mixed node.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "a model
  never observed past 200k on a node reads the 200k rung"` prints `1`, and into `grep -c "a
  150000-token turn, from a root that also holds"` prints `1`; and `git diff --name-only <pass base>
  HEAD --` over unit 30's spec and its acceptance ledger prints nothing.
  Red when: S4's answer lands in a record of unit 30, or this unit's ledger quotes neither passage.
- **AC5** — `tr -s ' \r\n' ' '` over `tools/runlog/README.md` piped into `grep -c "a 200k session of
  that model included"` prints `1`, and into `grep -c "whose newest earlier main usage in the same
  transcript is on that model"` prints `1`; and `grep -c "CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000"
  tools/runlog/README.md` prints `1`.
  Red when: the kit README states the window's source with no limit, or S5's edit overwrites unit
  47's compaction clause.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 · one check added to `test_extract_context_window`, the mixed root read with the variable at 200000, staged red by a copy of `extract.py` ranking the observation above the variable · `ASSERTION_FLOOR`, raised by 1 for the one check, the arm's decoy checks unchanged

## 8. Open questions

- **F1 — How does a 200k session on a 1M-observed model read its own window?** Options: (a) the
  limit stated and the harness's variable named as the session's override, the skeptic's corrected
  fix; (b) a per-session signal derived from the session's own maximum; (c) the smaller rung whenever
  both are observed. (b) misreads a fresh 1M session below 200k; (c) misreads every 1M session.
  (a) meets AC1 to AC3 and adds no surface. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the skeptic's corrected fix. widens: none · relaxes: none
- **F2 — Where is S4's answer to unit 30's superseded wording recorded?** Unit 30 builds at order
  13, one step before this unit, so it is CLOSED when this unit builds, and its ledger is in neither
  this unit's Files touched nor its write set. (a) Unit 30's acceptance ledger, a record of a closed
  unit written by a later one; (b) this unit's own acceptance ledger, quoting the unit 30 spec text
  it supersedes. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED
  unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected:
  (a), writing the earlier unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H8 (id 43).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S2 · S4 · §3 · §4 · §5 · §7 · §10 · re-grounded on the run's BASE
  `c2a407b0` under the brief `2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief`.
  The Gates line names `policy fixtures`, which `extract.py` trips; the Evidence quotes unit 30
  rev-3 and records that the help page's resume section stands and its `context —` paragraph is
  unbuilt; S2 names the section and the two units that write the paragraph; the more-common-window
  claim re-read from unit 30 rev-3 and pinned; every section-number reference to unit 30 named by
  its section. Nothing narrowed: units 14 and 30 are unbuilt, so no landed unit satisfies an item.
- rev-4 · 2026-11-21 · S3 · §4 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief`: S3's case sets the variable in its own
  child's environment, since unit 30 rev-4 has the selftest's `main` pop it before any arm; the
  policy fixture's import of `extract` shown unbroken; the floor raise and `symbols.json`, with the
  `recall floor` legs its path trips, added. No landed unit since base touched a cited symbol.
- rev-5 · 2026-11-21 · S4 · §4 · AC4 · §8 · S4's answer to unit 30 moves to this unit's own
  acceptance ledger, which joins Files touched, F2 resolved (b) and AC4 observing the quoted
  passages, under the brief `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`; the class of
  `KICK-dKeptSession-50`'s divergence, which unit 49's rev-6 first resolved.
- rev-6 · 2026-11-22 · §1 · S1 · S2 · S3 · S5 · §3 · §4 · §5 · AC1 · AC2 · AC3 · AC5 · §7 · §10 ·
  re-grounded at `e8b22050a` on the landed units 14, 30, 45 and 46, with unit 47 rev-6 read as
  landing first, under the brief `2026-11-22-prompt-KICK-dKeptSession-48-reground-brief`. Every
  shipped text naming the window's source tabled: the kit README's `context` paragraph joins Files
  touched under the new S5 and AC5, the rest read as staying with a reason each; S1, S2 and S5 give
  their exact sentences and anchors clear of unit 47's rewritten clause; S3's check moves into
  `test_extract_context_window`, which already reads the mixed root, so `symbols.json` leaves Files
  touched and the floor rises by 1 from the figure unit 47 leaves; the landed signatures and the
  floor's 1624 re-read and pinned.

## 10. Reuse audit

The seam is unit 30's own rung 1, the harness's `CLAUDE_CODE_MAX_CONTEXT_TOKENS`
(`tools/runlog/extract.py#derive_context_window`), which this unit documents and observes rather
than adding a second override, and its test arm `test_extract_context_window`, which S3 extends. Re-run at
`e8b22050a`, `python tools/codebase-map/reuse_lookup.py "state the limit of a derived context window
and the override a session sets"` ranked `derive_*` and `set_env_aside` functions of other kits by
name stem only; none reads a window, so no existing seam fits a per-session signal and none is
minted. The recall query below returned this build's specs 30 and 48, scout C's row for unit 14
and unit 14's spec brief; no landed unit outside this build reads a window.

Recall terms used: `python tools/memory-recall/query.py "how does a 200k session read its fill on a
node that also runs 1M sessions" --terms "context window rung CLAUDE_CODE_MAX_CONTEXT_TOKENS 200000
1000000 mixed observed fill fresh-at-boundary override"`
