# TOOL-aMendedFleet-31 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-31

**Evidences:** TOOL-aMendedFleet-31
- AC1 — `<n> hits for:` — the AC1 command on the changed tree printed `40 hits for:` and 40 lines starting `[<n>] `: 12 snippet hits, then 28 pointer lines, no snippet below the first pointer, and `snippets for ranks 1-12 · pointers for 13-40 of 40 hits · raise --budget for more snippets`, every count derived from that stdout by a scratch reader
- AC2 — `git clone --local` — under `%TEMP%/r31`, checked out at the pass's parent `b17e4a1a6`, the same command printed 16,616 B with 40 snippets; the changed tree printed 7,699 B, a ratio of 0.463, and the clone listed no path this run did not
- AC3 — `n_snippets` — the last `query` row under `git rev-parse --git-common-dir` (qid 760) carried `n_snippets` 12, equal to the split line's 12, and `shown_paths` held 40 entries for `n_shown` 40, the pointer hits included; the `--budget 3000` run's row (qid 761) carried 1 and 31 and 31
- AC4 — `--budget 3000` — the AC1 command at that budget printed hit 1 as a snippet, pointers for ranks 2 to 31, the split line `snippets for ranks 1-1 · pointers for 2-31 of 40 hits`, and the kept `shown 31 of 40 within 3,000 B` line
- AC5 — `emit` — a scratch script under the session scratchpad, run from the repo root with the kit directory on `sys.path`, imported `query` and called `emit` on 20 equal hits at 1,414 B, whose `SNIPPET_SHARE` holds 3 of them: 3 snippets, 17 pointers, a fifth return of 3, and `shown` 11 at a budget too small for every pointer. RED first on a staged break in the clone, the share test widened to the whole budget: 13 snippets and 2 pointers
- AC6 — `bash tools/memory-recall/adopt-memory-recall.sh --check` — exit 1 with the paragraph diff after the template edit and before the render, exit 0 after `--scaffold`; `grep -n "pointer"` hit `.claude/skills/memory-recall/SKILL.md` lines 51 and 52 in "Reading the answer" and `tools/memory-recall/README.md` line 77 in `Use`

## The arms

- `test_budget_bounds_emission_and_beats_full_documents` takes the fifth return, accounts for the
  blank line that separates the two tiers, and probes truncation at 600 B, where the pointer tier
  cannot hold all 20 hits. `test_snippet_share_bounds_the_head_and_pointers_keep_the_rest` is new,
  and `SELFTEST_ARMS` moves 76 -> 77 with its provenance line. Both arms were executed alone by a
  scratch script that compiled only those two functions out of `selftest.py`: both passed on the
  changed tree, and the first raised `ValueError` against the parent's four-value `emit`. The suite
  itself did not run.

## Owed at the close

- `memory-recall kit selftest`, `recall floor` and `recall floor arms`, whose guard is the kit
  directory, and the arm-count pin and its provenance chain, which only the suite grades.
- `memory-recall skill wiring`, `check-wiring self-test`, `lexicon naming predicates`,
  `memory hygiene`, `codebase-map coverage + freshness` and `spec tokens`. `gen_map.py --check`
  exited 0 after `--write`; `lexicon.py --suggest render_pointer --as py.function` answered OK;
  `encoding_posture.py` reported no undeclared site.
- The memory-recall kit version bump owed by the README and Skill edits, per the brief.
