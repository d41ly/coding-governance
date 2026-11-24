**Serves:** journal TOOL-dTotalRecall-60
**Caused-by:** TOOL-dTotalRecall-60

# TOOL-dTotalRecall-60 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `74f2d411b` from [2026-11-24-prompt-TOOL-dTotalRecall-60-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-60-build-brief.md), recorded whole; the pass tip is `2ec3df383`.

## Why

Spec rev-3 built as written over base 74f2d411b. Every claim it makes about current code was probed first, and none failed. The one snag is a criterion's fixture: AC14's clone as spelled, with no remote, is refused on the build lease. It was observed with a scratch bare remote added, and the ledger says so. Nothing in the code diverges from the spec.

## Summary

Built:
- S24: the split census in `id_grammar.py` lists every maxsplit and rsplit shape except the safe ones. Its two new hits are marked in `tools/policy/check_policy.py` and `tools/process-monitor/census.py`.
- `tools/memory-tree/record_causes.py`: S13 `--backfill --build <slug>`; S20 the cause line behind the Serves line's lead, `not markdown` dropped; S19 `check_ask_live`, with an optional third argument so HEAD is read once per census; S26 the renderer's kept reason admitted for its one file.
- S30 `tools/runlog/README.md`; S31 `RECORD_SCHEMA["cause_line"]`.
- The plants and their arms, `symbols.json`, and the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-60-1-acceptance-ledger.md`. Spec set CLOSED; `gen_build_index.py --write` output and RUN.md are committed with it.

Observed by probe (DERIVED 2026-11-24, node a): AC1 to AC35, except AC2's hygiene half. Each probe stands in for the leg that will grade it:
- The plants `backfill-selection`, `backfill-refusals`, `other-build-causeless`, `pinned-ask-closed`, `departures-pinned`, `pinned-writer-drained`, `marker-in-build-script`, `reason-on-other-file`, `kept-instrument-not-legacy`, `kept-row-drained` and `kept-row-editable` each gave their expected result, for the `memory hygiene` suite arms. That includes the PASS line where a plant prints one.
- Two staged breaks, each in the probe process: `check_ask_live` stubbed, and the plant's build unset. Their plants printed FAIL and exited 1.
- AC3, AC24: `--readers` over a throwaway tree, for the `memory-recall kit selftest` arm. At the tip `--readers` still prints the same 16 lines it printed before the edits.
- AC17 used a shared clone at `7047890d5` in place of a worktree. AC27's `[0]` break was staged in process rather than on a disk copy.
- AC35's packet half ran through `python tools/chain-packet.py --check dTotalRecall`: exit 0, byte compare green.
- `lexicon.py --suggest check_ask_live` says OK; `--measure` leaves `VERB_OFFENDER_PIN` at 1435. This stands in for `lexicon naming predicates`.

Owed to the close:
- AC2's `check-memory-hygiene.sh --only 9` (a gate).
- Both `New arm:` RED-first observations: `check-memory-hygiene.test.sh` (AC11 AC13 AC19 AC20 AC26: each new test skipped, and the `not markdown` refusal restored), and `tools/memory-recall/selftest.py` (AC3 AC24: the old shape restored, and the old marker read).
- All §7 legs. `record_causes.py --check` over the real tree was refused to this role by scratch-guard; `--cause-writers` at the tip exited 0 with no red, in 13 s (DERIVED 2026-11-24).

AC14: the remote-less clone was refused, exit 2, on the build lease, which is neither the usage nor the id refusal. With a scratch bare remote it exited 0 with `node d`. The clone was of base 74f2d411b, and this pass changes nothing that command reads.

Gate note: the builder ran `gen_map.py --check`, `gen_build_index.py --check` and the two as-built `--check` commands because the criteria spell them. `gen_build_index.py --write` moved the build's derived status from INPROGRESS to DEFERRED in `memory/LIVE.md`, `memory/backlog/TOOL.md` and the build README, until unit 65 opens.

`gotchas.py --for-diff HEAD~1..HEAD` ran after the commit. Selected classes checked against the diff (new locals in the long census function, swallowed delegate, heredoc escapes, fixture finding nothing) needed no change. No command was skipped for time. The scratch clones and fixtures under %TEMP% were removed.
