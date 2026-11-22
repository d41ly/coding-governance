# TOOL-dWitnessedBar-4 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-4

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by probing the unit's own code over scratch fixtures under `%TEMP%`: the runner over a
one-leg fixture clone (before the role's runner refusal was met, see AC1), isolated copies of the new
and amended arms of `.githooks/pre-push.test.sh` and `tools/push-main.test.sh` assembled with their
suites' fixture preambles and run alone, `python -c` calls into `loop_transition.py`, its `record` verb,
`policy.py get` and `lists --write`, and `render_playbook.py --reference`. The close owes every leg of
section 7 and the RED-first observation of each of its three `New arm:` lines.

**Evidences:** TOOL-dWitnessedBar-4
- AC1 — `kind full` — over a scratch clone and a fixture manifest of one passing leg, a full run printed
  `run-gates: per-tree verdict GREEN (full) written to …/.git/gate-verdict/<tree>`, the file named for
  `git rev-parse HEAD^{tree}` and reading `verdict GREEN`, `kind full`, `by runner`, and the run record's
  `verdict` file holding the same `tree`. The linked-worktree half (written into the common dir, never
  its own git dir, keyed by the tree) is the new evidence arm's, owed to the close: the role's
  scratch-guard refused a direct runner run from this pass.
- AC2 — `verdict RED` — the same fixture with its leg failing rewrote the per-tree file `verdict RED`;
  with an untracked file planted the run wrote no per-tree file, printed `run-gates: no per-tree verdict
  written — the tree was not clean when the run started`, and the directory's count stayed put.
- AC3 — `.scoped` — a scoped run after the full green of the same tree wrote `<tree>.scoped` reading
  `kind scoped` with the scoped base, and the full file still read `kind full`.
- AC4 — `.githooks/pre-push` — the amended BG arms, run alone over the suite's fixture: a planted full
  GREEN per-tree verdict of the pushed tree was adopted with no bar run (the marker unmoved), the
  covered line naming `…/gate-verdict/<tree> sha <x>` and `by runner`.
- AC5 — `reused_cache` — the same arms planted the pushed tree's verdict `verdict RED`, with another
  `manifest`, with `reused_cache 1`, with the self-tests held and with no tree: each ran the bar and the
  `not covered` line named `it reads verdict 'RED', not GREEN`, `earned on the leg manifest
  elsewhere/other-legs.json`, `reused 1 leg(s) from the cache`, `self-tests HELD`, `could not be read`.
  49 of 49 arms from the BG section to the suite's end read ok.
- AC6 — `git grep -c 'write_bar_green' -- .githooks tools` — printed nothing, exit 1, on the built tree.
- AC7 — `build-tip` — arm 42 of `push-main.test.sh`, run alone: `--prepare` under a planted reader
  printing `build-tip` exited 0 with HEAD unchanged and printed `push-main: test.merge build-tip <tip8>
  tree <tip tree>`; under `prepared-merge` it printed the merge's line with first parent the advertised
  tip; `--land` on the pinned branch exited 0 and the fixture remote's main is a merge whose first
  parent is the advertised tip and second the pinned tip.
- AC8 — `--field tree=<hash>` — `loop_transition.py record --build dWitnessedBar --from testing --item
  item.test.exit --outcome recorded --witness HEAD --field tree=<hash>` with no per-tree file exited 1
  printing `refused — item.test.exit · tree <hash>: no full per-tree verdict at …`; `check_tree_verdict`
  called in process over a scratch repository returned the RED file's reason, `None` once it read
  GREEN, and refused `../x` as no tree hash. The GREEN record path writing the transition is owed to
  the `loop transition record` leg at the close.
- AC9 — `prepared-merge` — `python tools/policy/policy.py get verdict.tree` printed `prepared-merge`;
  `policy.py lists --write` drained `verdict.tree`, `grep -cx 'verdict.tree' unsummarised-keys.txt`
  printed 0, and after `render_playbook.py --reference` `grep -c '^## .verdict\.tree.$'
  help/reference/policy.md` printed 1.
