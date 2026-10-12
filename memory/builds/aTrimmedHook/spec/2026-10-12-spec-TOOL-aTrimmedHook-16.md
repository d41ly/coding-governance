# TOOL-aTrimmedHook-16 — the closing bar's reds, this build's own and the inherited ones absorbed

**Status:** CLOSED · rev-1 · 2026-10-12 · node a · Tier-1 · base ad0f5649 · streams tooling+kickoff · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aTrimmedHook-16-1-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aTrimmedHook-16-1-acceptance-ledger.md) | journal | — |
| [2026-10-12-prompt-TOOL-aTrimmedHook-16-1-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aTrimmedHook-16-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The first close's bar went red on twelve legs. Two reds are this build's own, and the owner chose to
absorb the inherited ones that the close attributes to this run because its diff touches the files
they grade. This unit turns each of those legs green with the smallest mechanical fix, so the close
can land.

## 2. Scope (IN)

- **S1 — own: shell hygiene.** `skills/session-kickoff/manifest-check.sh`'s C6 loop splits the listing on
  newlines with globbing off, instead of reading a here-string of a substitution's value. Observed
  by AC1.
- **S2 — own: dead paths.** The staged index-kind pattern in
  `tools/memory-tree/check-memory-hygiene.sh` matches only the index kinds the tree still holds, without `STATUS.md`. Observed by AC2.
- **S3 — absorbed: lexicon.** The five helpers that `tools/run-gates/run-gates.evidence.test.sh` gained
  in `6fbe54e8` take declared verbs (`build_pm_commit`, `run_pm`, `read_pm_key`, `read_pm_red`,
  `print_pm_out`), so the verb-offender count is back at its pin. Observed by AC3.
- **S4 — absorbed: install-prefix.** Two fixture literals in `.githooks/pre-push.test.sh` and one in
  `tools/unattended/unattended.test.sh` spell no kit path. Observed by AC4.
- **S5 — absorbed: harness arms.** `tools/run-gates/post-merge.sh`'s publish-failed exit is pinned in
  `memory/project/unarmed-branches.txt` with its reason: no sibling suite exists. Observed by AC5.
- **S6 — the version steps** every kit this unit moves owes, in this unit's commit. Observed by AC6.

## 3. Non-goals (OUT)

- No suite is run: the owner ruled no self-tests in this run. The renamed helpers and the edited
  fixtures are checked by `bash -n` and by the legs that grade them, not by their suites.
- The routed-commit waiver is re-derived in a records commit after this one, since it lists shas.
- The four legs that timed out on the contended host are not edited; the next close re-runs them.

### Edges

none

## 4. Design

Each fix is the remedy the leg's own refusal names. S3 renames by whole word inside one file; no
other tracked file names the helpers except the generated symbol map, which is regenerated. S4's
literals are arbitrary fixture values that only need to differ from the real ones. S5 uses the row
`check-arms.py --emit-pin` prints, with its reason filled.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push.test.sh`
- `tools/unattended/unattended.test.sh`

## 5. Acceptance criteria

- **AC1** — When `python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
  runs, it reports no finding. Red when: the `manifest-check.sh` site is still reported.
- **AC2** — When `bash tools/check-dead-paths.sh` runs, it prints its clean line.
  Red when: the hygiene script's pattern line is reported.
- **AC3** — When `python3 tools/lexicon/lexicon.py` runs, it exits 0 with the verb-offender count at
  the pin. Red when: it reports the count over the pin.
- **AC4** — When `bash tools/check-install-prefix.sh` runs, it prints its clean line.
  Red when: any kit-path spelling is reported.
- **AC5** — When `python3 tools/memory-tree/check-arms.py --check` runs, it exits 0.
  Red when: the post-merge exit site is reported.
- **AC6** — When `python3 tools/govkit/govkit.py epoch --base 9b7438315` runs, every kit reads clean.
  Red when: a kit moved by this unit reads FAILED.

## 6. Gates

`shell hygiene (a loop fed by a command substitution)` · `manifest-check self-test` · `scratch-guard self-test` · `dead-path carriers (deleted files still named)` · `lexicon naming predicates` · `lexicon wiring` · `install-prefix (shipped surface)` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `codebase-map coverage + freshness`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-12 · initial draft, from the first close's bar attribution and the owner's ruling to absorb.
