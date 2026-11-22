**Serves:** research TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 build pass 3 — the builder's return (DIVERGENCE)

The gov-builder return of `unattended-unit.js` run `wf_6d4a45a7-9c9`, at base `17f07b292`, saved in substance. Nothing was written or committed.

## why

DIVERGENCE: rev-10 cannot be built as written, because S7, S13, §4 "Files touched" and §7 cannot all hold. Nothing was written.

The problem. S7 and S13 point every reader at `slug_class`, which is the legacy shape `[<node>][A-Za-z]{2,}` joined with the strict shape. That is narrower than the `[A-Za-z0-9]+` and `[A-Za-z]+` slug parts most readers use today. It refuses the short fixture slugs that many suites feed through those same readers: `x`, `s`, `a`, `bx`, `fx`, `dX`, `dY`, `tA`, `tB`, `tW`, `bD`, `zA` and `tFix2`. `tFix2` has a digit, which both shapes refuse.

The spec has a rule for re-spelling such fixtures, but it is S13's last sentence and covers only ids read through the tree_lib token functions. Its Files touched names only two fixture homes for it: `gen_build_index.py` and `tools/memory-recall/selftest.py`. Its one escape clause ("a hit outside it joins the pass's --dispatch --writes set") covers search hits, and a fixture is not a search hit. Meanwhile §7 expects these suites green: `tier2-review self-test`, `roles render selftest`, `playbook render selftest`, `push-main self-test`, `scratch-guard self-test`, `unattended kit gate`, `unattended-build self-test`, `loop * fixtures` and `policy fixtures`.

Traced at HEAD 17f07b292:
- **tier2-review.** `tools/workflows/tier2-review.test.sh` (53 lines) expects a subject with id `TOOL-x-1` to proceed. The template refuses any id `PIN_ID` rejects (`tools/workflows/tier2-review.template.js@17f07b292:821`). Once `PIN_ID` splices the class, it rejects `x`. (DERIVED, the builder's own run)
- **roles.** `tools/roles/adopt-roles.test.sh` (8 lines) runs `handoff.py render --build bx --unit TOOL-bx-1`. Its build passes through `tools/roles/roles_lib.py#SLUG_RE`, today `^[A-Za-z]+$`, re-pointed by §4's table. `tools/playbook/load_sets.py` (`PLAY-bx-1`) and `tools/roles/render_agents.py` (`PLAY-fx-1`) feed the same readers. (DERIVED, the builder's own run)
- **loop.** `tools/loop/scenario.py#FX_BUILD_2` is `tFix2`, a build slug with a digit. Its `ids: TOOL-tFix2-1` goes through `read_bindings` (S13) and through the re-pointed loop `SLUG` readers.
- **policy.** `tools/policy/check_policy.py` (`TOOL-x-1`, `TOOL-x-0`) and `tools/workflows/replay_scorer.py` (`PLAY-dX-1` in a `**Serves:**` line) feed the tree_lib readers. That is S13's own rule, but neither file is in Files touched.
- **Candidates fed by re-pointed shell or JS unit-id readers, not each traced to its assertion:**
  - `tools/push-main.test.sh` (14 lines: `TOOL-tB-1`, `TOOL-fx-*`) (DERIVED, the builder's own run)
  - `tools/hooks/scratch-guard.test.sh` (67: `TOOL-x-*`)
  - `tools/unattended/unattended.test.sh` (`TOOL-tW-1`)
  - `tools/unattended/gate-guard.test.sh` (`--pass TOOL-s-1`, expects allow)
  - `tools/workflows/unattended-build.test.sh` (`TOOL-bD-1`)
  - `.githooks/straggler-guard.test.sh` (10)
  - `.githooks/pre-push.test.sh` (2)
  - `tools/run-gates/keep_tails.py` (2)
  - `tools/run-gates/verdict_backends.py` (1)
  - `tools/lexicon/selftest.py` (1)

Search: 218 lines across 26 files. Output saved at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/fixture-slugs-pass3.txt (DERIVED, this pass's git grep at 17f07b292).

The census command of §4 "The readers" also hits test-side copies of re-pointed readers that Files touched leaves out and §4 assigns no disposition: `tools/memory-tree/merge-rows.test.sh` (its `ORACLE` copies `merge-rows.py#_ID_RE`), `tools/memory-tree/hygiene-parity.test.sh` (a copy of check 12's record-name grammar), `tools/runlog/selftest.py` (four lines, `ANCHOR_ID` among them) and `tools/govkit/selftest.py` (two). Each is an id reader, so §4's rule ("a hit that is not a slug or id reader at all is recorded as kept") does not let the pass keep it.

What the spec would have to say. Lift S13's fixture rule to S7, so that any fixture slug or id a suite feeds through a re-pointed reader, and which the class refuses, is re-spelled to the legacy shape. Add every such suite file to Files touched, from a stated search command (the one above is a model), and add the test-side census hits with a disposition each: re-pointed, or kept with the reason. Alternatively, choose in §8 (a new F13) that the readers whose only refused population is fixtures keep a looser class, and give the reason. Every other cited claim I probed held at 17f07b292:
- the census prints 73 lines in 37 files; (DERIVED, the builder's own run)
- `policy.py get` prints `1-3` here, and refuses on a master-only repository with a last line naming `refs/heads/main`;
- `drift_report.py#_build_local_ident` and its parity arm;
- `_expand_ids`' `rng`;
- `CAP_NOTE`;
- the master pin and the `BUILD_SLUG_RE` arms of the hygiene suite;
- the `hygiene-print-modes` contract;
- the workflows kit's placeholders and `[[regenerate]]` row;
- `PARITY_ROWS`' marker loop;
- run-gates' `resolve_kit_dir` copy;
- the three catalogue rows;
- the reader-coverage call shape `check_policy.py` reads.

## summary

I built nothing and committed nothing. Rev-10 has its re-pointed readers refuse fixture ids in suites that §7 expects green, and its Files touched leaves those suites out. The divergence is in `why`. This pass started at 17f07b29282578257e7776a95722a0a60bc69606 and wrote no repository path. The only uncommitted change is the main loop's own staged `memory/builds/dTotalRecall/RUN.md`, which I left untouched.

- **Not done:**
  - I did not run the `--brief` record verb. It writes a RUN.md row, and the divergence rule would then make me restore a file the main loop has staged (passes 1 and 2 skipped it for the same reason).
  - I did not run `gotchas.py --for-diff`, because there is no commit for it to read.
  - I made no draft, so there is no patch.
  - No command ran past its time bound.
- **What I checked:**
  - Read-only reads and greps over HEAD.
  - The census command of §4 "The readers": 73 lines in 37 files, as pinned. Output at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/census3-base.txt. (DERIVED, the builder's own run)
  - A search for fixture ids whose slug the class refuses: 218 lines in 26 files, output at C:/Users/d41ly/AppData/Local/Temp/claude/7ca5dd954c018619/16f4ad58-6904-4a66-bc18-9482a47ce656/scratchpad/fixture-slugs-pass3.txt. (DERIVED, the builder's own run)
  - A Python probe of the hygiene suite's fixture folder names: every one passes the legacy shape except the ones planted to fail. `tGenU` and `tGenA` fail only the strict shape.
  - `policy.py get builds.slug-words` in this tree (prints `1-3` in 0.23 s, DERIVED) and in the earlier scratch repository `pg1` on master (exit 2, last line names `refs/heads/main`).
- **Gates:** these checks stand in for no gate, and none ran. Every AC1 to AC14 observation and all four `New arm:` RED-first observations are still owed:
  - `tools/lib/resolve-python.test.sh`
  - `tools/memory-tree/check-memory-hygiene.test.sh`
  - `tools/drift-audit/selftest.py`
  - `gen_build_index.py --selftest`
- **Card mismatch:** the parent's orientation card still says this unit is DEFERRED, but its spec header reads INPROGRESS. The card is stale.
