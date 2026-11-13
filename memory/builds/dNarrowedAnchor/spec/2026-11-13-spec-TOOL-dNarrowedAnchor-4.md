# TOOL-dNarrowedAnchor-4 — drop the closed TOOL-dNarrowedAnchor-1 from the signal-2 baseline set

**Status:** INPROGRESS · rev-2 · 2026-11-13 · node d · Tier-1 · base 2ba17e9d · streams tooling · ratified 2026-11-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-prompt-TOOL-dNarrowedAnchor-4-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dNarrowedAnchor-4-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dNarrowedAnchor-4-2-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dNarrowedAnchor-4-2-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dNarrowedAnchor-4-3-builder.md](../prompts/2026-11-13-prompt-TOOL-dNarrowedAnchor-4-3-builder.md) | journal | — |
| [2026-11-13-prompt-TOOL-dNarrowedAnchor-4-brief.md](../prompts/2026-11-13-prompt-TOOL-dNarrowedAnchor-4-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Delete `TOOL-dNarrowedAnchor-1` from the `non_terminal_specs_cited_by_product_source` entry of
`BASELINES` in `tools/drift-audit/drift_signals.py`. That spec went CLOSED at `6675df24a`, so it is
no longer an offender, and the shrink-only set reds the `drift-audit records` leg with a `stale`
line until the entry goes.

## 2. Scope (IN)

- **S1** — The list under the `non_terminal_specs_cited_by_product_source` key keeps
  `TOOL-aBatchedLintel-1` and loses `TOOL-dNarrowedAnchor-1`. Observed by AC1 and AC2.
- **S2** — The two present-tense sentences in the comment block above the list that count the
  listed ids as two are reworded so they hold for any number of listed ids. Observed by AC3.

## 3. Non-goals (OUT)

- The `new TOOL-aNimbleMend-15` offence on the same signal. It is inherited from `main` at
  `2ba17e9d6` and belongs to node a's live aNimbleMend build, so the leg stays red at this base.
- The `closed_specs_with_no_product_commit` entry, and any other `BASELINES` or `PINS` entry.
- Any change to `tools/drift-audit/drift_report.py`.
- The past-tense sentence of the comment block that says the file was returned "for both pinned
  ids". It reports a measurement taken when both were listed and stays true.

### Edges

none

## 4. Design

The list sits at `tools/drift-audit/drift_signals.py@65361d09b85b:409`, with
`TOOL-aBatchedLintel-1` on line 410 and `TOOL-dNarrowedAnchor-1` on line 411. Delete line 411 and
nothing else for S1. Both the key and the two ids were written by one commit, `bb7fe30ba`
(TOOL-aMendedFleet-56), together with the comment block above them.

Why the entry is now stale, verified in source.
`tools/drift-audit/drift_report.py#signal_spec_status` judges only specs whose status token is in
`NON_TERMINAL` (OPEN, SPECCED, BLOCKED, INPROGRESS). The spec
`memory/builds/dNarrowedAnchor/spec/2026-08-24-spec-TOOL-dNarrowedAnchor-1.md` now reads
`CLOSED · rev-2`, so it leaves the judged population. `drift_report.py#main` then computes
`stale = listed - have` for every signal in `BASELINES`, puts any signal with a non-empty `new` or
`stale` in the red population, and prints `  stale <id> — listed but no longer an offender` per id.

The deletion is a shrink, which the base guard allows. `drift_report.py#build_baseline_findings`
reads the base's `BASELINES` with `ast.literal_eval` and reports only a set that GAINED an id.

S2 touches only the comment. The sentence at line 399 says "both are INPROGRESS"
and the one at line 406 says "both ids keep non-test product citations". After S1 one id is listed
and the first is already false, because `TOOL-dNarrowedAnchor-1` is CLOSED. The reword swaps each
count for count-free wording such as "each listed id", keeps every line within the line-length gate,
and leaves the rest of each sentence as written.

### Files touched (estimate)

- `tools/drift-audit/drift_signals.py`

## 5. Acceptance criteria

- **AC1** — When the probe below runs from the repo root, it prints `[['TOOL-aBatchedLintel-1']]`.
  It reads the literal the way `build_baseline_findings` does, with `ast.literal_eval`.
  Red when: the deleted line is back, or the edit breaks the dict out of literal form.

  ```
  python -c "import ast,pathlib;t=ast.parse(pathlib.Path('tools/drift-audit/drift_signals.py').read_text(encoding='utf-8'));print([ast.literal_eval(n.value)['non_terminal_specs_cited_by_product_source'] for n in t.body if isinstance(n,ast.AnnAssign) and n.target.id=='BASELINES'])"
  ```

  At `65361d09b85b` it prints `[['TOOL-aBatchedLintel-1', 'TOOL-dNarrowedAnchor-1']]`. That reading
  was measured when this spec was written.
- **AC2** — When the probe below runs, it prints `stale: []`. `--json` without `--check` prints one
  JSON document and appends no history row, per the comment above the history write in
  `drift_report.py#main`.
  Red when: `TOOL-dNarrowedAnchor-1` is still listed, which prints
  `stale: ['TOOL-dNarrowedAnchor-1']`.

  ```
  python tools/drift-audit/drift_report.py --json | python -c "import json,sys;s=[x for x in json.load(sys.stdin) if x['signal']=='non_terminal_specs_cited_by_product_source'][0];print('stale:',s['stale'])"
  ```

  The same probe's `new` list keeps `TOOL-aNimbleMend-15`, which is out of scope here.
- **AC3** — When `grep -cE "both are INPROGRESS|both ids keep" tools/drift-audit/drift_signals.py`
  runs, it prints `0`.
  Red when: either count-bearing sentence survives the edit.

## 6. Gates

`drift-audit records` · `drift-audit selftest` · `memory hygiene`

No new arm. `drift-audit selftest` is owed because its guard covers the touched file. It does not
read this unit's list: `tools/drift-audit/selftest.py` writes its own `drift_signals.py` into each
fixture repo it builds, so its verdict should not move. The `drift-audit records` leg stays red at
this base because of `new TOOL-aNimbleMend-15`. What clears here is the
`stale TOOL-dNarrowedAnchor-1` line within it, which AC2 observes without the leg.

## 7. Open questions

- **F1** — Does the comment block above the list get reworded, given the brief says amend it only
  if it names the deleted id? It does not spell the id, but two present-tense sentences count the
  listed ids as two, and one of them already says a CLOSED spec is INPROGRESS.
  - (a) Leave the comment as written, and cut S2 and AC3. This follows the brief's letter.
  - (b) Reword the two present-tense counts only, as S2 states. This keeps the comment true and
    follows the one-fact rule against a count typed beside what it describes.
  - Recommendation: (b). The brief's stated reason for leaving the comment alone is that it stays
    true, and these two sentences do not.
  - RESOLVED (agent, 2026-11-13, delegated): (b). It is no worse than (a) on any count, and the
    owner's standing rule decides a no-worse question rather than parking it.

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.
- rev-2 · 2026-11-13 · F1 resolved to (b); S2 and AC3 stay in scope.
