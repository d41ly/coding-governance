# KICK-dKeptSession-30 — the context window derived per model from the node's observed usage, never pinned at 200000

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 13 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 |
| [2026-10-26-build-KICK-dKeptSession-30-deviation-301.md](../build/2026-10-26-build-KICK-dKeptSession-30-deviation-301.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 16 at BLOCKER**, report item **B1**, which no other id shares.

`KICK-dKeptSession-14` §4 "The window" pins `CONTEXT_WINDOW_TOKENS = 200000`, marked UNVERIFIED, and
§8 F2 resolves on it. On this node the owner session runs a window of about 1M tokens, so the fill
reads up to about 490% and the default `context.threshold` of 60% fires at 120k tokens, about 12% of
the real window: under `fresh-at-boundary` every owner session past 120k is told to end at its next
item boundary. This unit replaces the constant with a window derived per model from what the node's
own transcripts show the window holds, and lets the harness's own window variable win. It repairs
`KICK-dKeptSession-14` and builds one step after it (order 13).

## 2. Scope (IN)

- **S1** — id 16. The window, `derive_context_window(model, root=None)` in
  `tools/runlog/extract.py`, returning `(tokens, source)`:
  1. `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, when it is set to a positive integer, with source `env`. It
     is the harness's own variable for a model's real window (§4 Evidence), read and never written.
  2. Otherwise the smallest rung of `CONTEXT_WINDOW_RUNGS = (200000, 1000000)` at or above the
     largest context the node has observed for `model`, with source `observed <n> on <model>`.
     The observation is the largest `derive_context_tokens(ev)` over the main-source `usage`
     events whose `model` is `model`, and the largest `pre_tokens` of the `compact` events, over
     the newest `CONTEXT_WINDOW_SCAN` (20) main transcripts under `root`. `root` defaults to the
     harness's projects root, `~/.claude/projects`. An observation past the top rung is its own
     window.
  3. With no observation for `model`, the bottom rung, with source `no observation`.
  Observed by AC1, AC2, AC3 and AC4.
- **S2** — id 16. The readers re-pointed. `measure_context_fill(transcript, until=None)` divides by
  `derive_context_window(<the event's model>, root=<the transcript's projects root>)`, the
  transcript's parent's parent. `derive_context_fill(ev, window=None)` takes an explicit window, or
  derives one from `ev["model"]` under the default root, so `KICK-dKeptSession-9`'s per-stage rows
  read the same window with no change to their call. `python tools/runlog/runlog.py context
  <transcript>` keeps its stdout, `<n>%` or `none`, and prints `context: window <tokens> · <source>`
  on stderr. Observed by AC1, AC2 and AC5.
- **S3** — id 16. The constant retired. `CONTEXT_WINDOW_TOKENS` is deleted, not left beside the
  rungs, and `KICK-dKeptSession-14` §4 "The window" and §8 F2 are superseded by name here and
  answered in that unit's acceptance ledger. Observed by AC5.
  **Readers:** by name: READER NOT IN TREE — the constant is minted by unit 14 S1 and spelled only
  by that unit's unbuilt fill function and help paragraph, so no tracked reader spells it at this
  base · by value: NO VALUE READERS — its only value readers are unit 14's fill and unit 9's
  per-stage column, both unbuilt at this base, which divide by it and which S2 re-points.
- **S4** — id 16. The fixture. Two scenarios in `tools/runlog/fixtures/transcripts.json`,
  `context-window` with a last main usage of 150000 tokens on `fixture-model`, and
  `context-window-sibling` with one main usage of 900000 tokens on the same model, written the way
  the store's other scenarios are. One selftest case in `tools/runlog/selftest.py` writes them into one
  scratch projects root, or the first alone, as each criterion says. Observed by AC1 to AC4.
- **S5** — id 16. `help/orientation-card.md`'s `context —` paragraph says the window is derived per
  model from the node's observed usage and names `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, in place of the
  word "pinned".
  Observed by AC6.

## 3. Non-goals (OUT)

- The threshold, the lines and the boundary act: `KICK-dKeptSession-14`'s, unchanged.
- A policy key for the window. No clause names one, and §8 F1 records why it is not taken.
- A model-to-window table. A transcript's `model` field does not say which window the account runs,
  as §4 measures.
- A cache of the observation. One scan costs under a second on this node (§5).
- The report's left-shift entry, a checklist line that a pinned UNVERIFIED platform constant cites a
  node measurement. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-14` — `measure_context_fill`, `derive_context_fill`, `derive_context_tokens` and `CONTEXT_WINDOW_TOKENS`, the fill this unit re-points from the pinned window to the derived one (id 16)
- **hands-off** `KICK-dKeptSession-45` — `derive_context_window`'s `root` argument, whose default that unit resolves through `resolve_projects_root` (id 28)
- **hands-off** `KICK-dKeptSession-46` — `derive_context_fill` and `derive_context_window`, whose root that unit makes the caller's (id 38)
- **hands-off** `KICK-dKeptSession-47` — the observation's compact events, which that unit attributes to a model (id 16)
- **hands-off** `KICK-dKeptSession-48` — rung 1 and the mixed-window root, whose limit that unit states and observes (id 43)
- **hands-off** `KICK-dKeptSession-56` — the window's scan, its rung 1, §3's cache non-goal and §5's price, and §7's legs, the batch's S11, S12, S14, S21 and S26 (ids 20, 45, 17, 29, 35)

## 4. Design

### Evidence

- A probe over the 40 newest coding-governance transcripts on this node, run 2026-10-26, read main
  usage maxima of 967091 tokens on `claude-opus-5-5` over 35195 usages, 922025 on `claude-opus-5`,
  and 95946 on `claude-opus-4-8` over 69. The audit's own probe found 27748 of 31116 main usages
  above 200000. PINNED, measured 2026-10-26; S1 re-derives it at every call.
- Eight compaction records on this node carry `compactMetadata.preTokens` between 834709 and
  949239. A window holds at least what was compacted out of it.
- No transcript record names the window. The `model` field reads `claude-opus-5-5` whatever the
  window, and a grep for `contextWindow` and `context_window` over the transcripts printed nothing.
- The installed harness, `claude --version` 2.1.292, carries the text "set
  CLAUDE_CODE_MAX_CONTEXT_TOKENS to its real window" and "append [1m] to the model name for 1M"
  (`grep -a -o` over the binary on PATH, 2026-10-26). The 1M rung is the harness's own figure.
- `extract_session` already yields `model` on every usage event and `pre_tokens` on every compact
  event (`tools/runlog/extract.py:818-821`, and `:834-836` with the usage event built at `:835`),
  so the scan needs no new parser field.
- `measure_ready_tree` globs main transcripts as `root.glob("*/*.jsonl")` filtered by `SID_RE`
  (`:1209`). The scan takes the same population, newest first by modification time.

### The read

```
derive_context_window("claude-opus-5-5")  -> (1000000, "observed 967091 on claude-opus-5-5")
derive_context_window("fixture-model")    -> (200000, "no observation")
CLAUDE_CODE_MAX_CONTEXT_TOKENS=500000     -> (500000, "env")
```

The scan reads each file's lines and parses only those carrying `"usage"` or `preTokens`. It runs
through `extract_session` only where a line needs it, so a long transcript costs one pass of reads.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_context_window` | function, `tools/runlog/extract.py` | `py.function`, asked at the pass |
| `CONTEXT_WINDOW_RUNGS`, `CONTEXT_WINDOW_SCAN` | constants, `tools/runlog/extract.py` | none declared |
| `context-window`, `context-window-sibling` | fixture scenarios | none |

### Migration

None. No stored state holds a fill; every read derives it.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, S2 and S3
- `tools/runlog/selftest.py`: the window case
- `tools/runlog/fixtures/transcripts.json`: S4's two scenarios
- `help/orientation-card.md`: S5

### Alternatives rejected

- **A larger pinned constant.** A 200k-window session would then read a fifth of its true share and
  compact before any boundary act fired.
- **The session's own maximum alone.** A fresh 1M-window session reads its first 200k against a
  200k rung, the defect's own range, until it passes 200k.
- **The window from the model id.** The transcript records `claude-opus-5-5` for both windows.

## 5. Production-readiness checklist

- security — transcripts are read, never written, and only token counts and model ids leave them.
- perf / scale — one scan per call over at most 20 main transcripts: 0.84 s over 210 MB on this node,
  measured 2026-10-26. Reading only each file's last megabyte is the upgrade if a boundary shows it.
- error / empty / loading states — an unreadable transcript is skipped; no observation reads the
  bottom rung with its source named; a non-integer variable is ignored with its source unchanged.
- observability — `runlog.py context` names the window and its source on stderr.
- risks — a model never observed past 200k on a node reads the 200k rung, so its first session
  there errs towards going fresh, the cheaper error by RT-1's measurement, until one session passes
  200k or the variable is set.
- testing — the selftest case of §6 and the arm in §7.
- migration — none.
- user docs — `help/orientation-card.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `runlog.py context` reads the `context-window-sibling` transcript, a 900000-token
  main turn, from a scratch projects root holding it alone, it prints `90%` and the stderr line
  `context: window 1000000 · observed 900000 on fixture-model`.
  Red when: the 200000 constant decides the share, which prints `450%`.
- **AC2** — When `runlog.py context` reads the `context-window` transcript, a 150000-token turn, from
  a root that also holds `context-window-sibling`, it prints `15%`.
  Red when: the window is taken from the transcript alone, which prints `75%`.
- **AC3** — When `runlog.py context` reads `context-window` from a root holding it alone, it prints
  `75%` and names the source `observed 150000 on fixture-model` on the 200000 rung.
  Red when: an unobserved larger window is assumed, so the probe can never answer the small rung.
- **AC4** — When `CLAUDE_CODE_MAX_CONTEXT_TOKENS=500000` is set for AC2's read, it prints `30%` with
  source `env`; set to `x`, it prints AC2's `15%`.
  Red when: the harness's variable is ignored, or a malformed value is used.
- **AC5** — When `grep -n "CONTEXT_WINDOW_TOKENS" tools/runlog/extract.py` runs, it prints nothing,
  and `grep -n "def derive_context_window" tools/runlog/extract.py` prints one line.
  Red when: the pinned constant survives beside the derivation.
- **AC6** — When `grep -n "CLAUDE_CODE_MAX_CONTEXT_TOKENS" orientation-card.md` runs in `help/`, it
  prints the `context —` paragraph's line, and `grep -c "pinned window" orientation-card.md` prints
  `0`.
  Red when: the page still describes a pinned window.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 AC2 AC3 AC4 · the window case over the two scenarios, staged red by a copy of `extract.py` dividing by 200000 · none

## 8. Open questions

- **F1 — Where does the window come from?** Options: (a) the derivation of S1, the harness's
  variable first, then the node's observed maximum per model rounded up to a rung; (b) a policy key
  `context.window`; (c) a model-to-window table; (d) the pinned constant, as unit 14 resolved.
  (b) is a public surface no clause names, an owner turn under BUILD-METHOD M3's veto 2. (c) cannot
  tell two windows apart, since the transcript records one model id for both. (d) fails the audit's
  criterion, a 900k turn reading under 100%. (a) meets AC1 to AC4 and adds no surface.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most capable survivor. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's B1 (id 16).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-45`, `KICK-dKeptSession-46`,
  `KICK-dKeptSession-47`, `KICK-dKeptSession-48`, `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-14`'s fill in `tools/runlog/extract.py`, its
`derive_context_tokens` reused as the observation's sum, with `measure_ready_tree`'s main-transcript
glob (`tools/runlog/extract.py:1209`) and `extract_session`'s `model` and `pre_tokens` fields
(`:818-821`, `:834-836`). `python tools/codebase-map/reuse_lookup.py "derive the context window size
of a model from observed session usage"` ranked `extract_session` and `resolve_session_tree` in
`tools/runlog/extract.py`, the seam named here, and `build_run_model` and four `derive_*` functions by
name stem only; none derives a window, so no existing seam fits the derivation itself and it is
minted beside the sum it reuses.

Recall terms used: `python tools/memory-recall/query.py "how is the context window a session's fill
is a share of derived" --terms "context window CONTEXT_WINDOW_TOKENS fill threshold fresh-at-boundary
transcript usage model compaction preTokens rung"`
